# paper bib year audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 223
- **Recorded user turns:** 3
- **Tool calls:** 70
- **Original source:** `logs/workers/worker_paper_bib-year-audit_20260515T235806.log`
- **Structured JSON:** [`2e727dd9c8a4ccaf617c.json`](../../sessions/2e/2e727dd9c8a4ccaf617c.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
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
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__verify_references"
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
  "uuid": "779b5833-aa30-4a1d-8f82-4b9b783f26d6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "992112a1-b88e-412b-9d2c-fb5e8716a3e2",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the references.bib file and the reference-audit skill file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d35ff369-33a3-41a2-b188-9900bb7f4869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12264
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_012HhB3yx2KKZvjqT2y96Ye5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ebe22a9d-50fe-445e-bcd8-0e644ec55af0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12264
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 6 · 2026-05-15T23:58:15.159Z_

<details><summary>↩ Tool result · `toolu_012HhB3yx2KKZvjqT2y96Ye5`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	}
140	
141	@inproceedings{strong_model_collapse,
142	  title = {{Strong Model Collapse}},
143	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
144	  booktitle = {Proceedings of the International Conference on Learning Representations},
145	  year = {2025},
146	}
147	
148	@inproceedings{model_collapse_avoidable,
149	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
150	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
151	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
152	  year = {2024},
153	}
154	
155	% ===== OOD Detection =====
156	
157	@inproceedings{ood_baseline,
158	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
159	  author = {Hendrycks, Dan and Gimpel, Kevin},
160	  booktitle = {Proceedings of the International Conference on Learning Representations},
161	  year = {2017},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{dsir,
167	  title = {{Data Selection for Language Models via Importance Resampling}},
168	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
169	  booktitle = {Advances in Neural Information Processing Systems},
170	  year = {2023},
171	}
172	
173	@inproceedings{qurating,
174	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
175	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
176	  booktitle = {Proceedings of the International Conference on Machine Learning},
177	  year = {2024},
178	}
179	
180	@inproceedings{ccnet,
181	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
182	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
183	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
184	  year = {2020},
185	}
186	
187	% ===== Watermarking =====
188	
189	@inproceedings{watermark_llm,
190	  title = {{A Watermark for Large Language Models}},
191	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
192	  booktitle = {Proceedings of the International Conference on Machine Learning},
193	  year = {2023},
194	}
195	
196	@article{synthid_text,
197	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
198	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
199	  journal = {Nature},
200	  volume = {634},
201	  pages = {818--823},
202	  year = {2024},
203	}
204	
205	@misc{aaronson_watermark,
206	  title = {{Watermarking GPT Outputs}},
207	  author = {Aaronson, Scott and Kirchner, Hendrik},
208	  year = {2022},
209	  howpublished = {Technical Talk},
210	  url = {https://scottaaronson.blog/?p=6823},
211	}
212	
213	@article{chainwash,
214	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
215	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
216	  journal = {arXiv preprint arXiv:2605.05503},
217	  year = {2026},
218	}
219	
220	% ===== Vocabulary Diversity =====
221	
222	@inproceedings{curious_decline,
223	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
224	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
225	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
226	  year = {2024},
227	}
228	
229	@inproceedings{writing_diversity,
230	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
231	  author = {Padmakumar, Vishakh and He, He},
232	  booktitle = {Proceedings of the International Conference on Learning Representations},
233	  year = {2024},
234	}
235	
236	@inproceedings{nucleus_sampling,
237	  title = {{The Curious Case of Neural Text Degeneration}},
238	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
239	  booktitle = {Proceedings of the International Conference on Learning Representations},
240	  year = {2020},
241	}
242	
243	@inproceedings{mapping_llm_science,
244	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
245	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
246	  booktitle = {Proceedings of the Conference on Language Modeling},
247	  year = {2024},
248	}
249	
250	@inproceedings{monitoring_ai_review,
251	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
252	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
253	  booktitle = {Proceedings of the International Conference on Machine Learning},
254	  year = {2024},
255	}
256	
257	% ===== Stylometry =====
258	
259	@article{stamatatos_survey,
260	  title = {{A Survey of Modern Authorship Attribution Methods}},
261	  author = {Stamatatos, Efstathios},
262	  journal = {Journal of the American Society for Information Science and Technology},
263	  year = {2009},
264	}
265	
266	@article{koppel_authorship,
267	  title = {{Computational Methods in Authorship Attribution}},
268	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
269	  journal = {Journal of the American Society for Information Science and Technology},
270	  year = {2009},
271	}
272	
273	@inproceedings{uchendu_attribution,
274	  title = {{Authorship Attribution for Neural Text Generation}},
275	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
276	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
277	  year = {2020},
278	}
279	
280	@inproceedings{munir_looking_glass,
281	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
282	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
283	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
284	  year = {2021},
285	}
286	
287	% ===== Iterative Generation =====
288	
289	@inproceedings{broken_telephone,
290	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
291	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
292	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
293	  year = {2025},
294	}
295	
296	@article{markovian_chains,
297	  title = {{Markovian Generation Chains in Large Language Models}},
298	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
299	  journal = {arXiv preprint arXiv:2603.11228},
300	  year = {2026},
301	}
302	
303	% ===== Membership Inference =====
304	
305	@inproceedings{min_k_percent,
306	  title = {{Detecting Pretraining Data from Large Language Models}},
307	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
308	  booktitle = {Proceedings of the International Conference on Learning Representations},
309	  year = {2024},
310	}
311	
312	% ===== Survey =====
313	
314	@article{wu_survey_2025,
315	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
316	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
317	  journal = {Computational Linguistics},
318	  publisher = {MIT Press},
319	  year = {2025},
320	}
321	
322	@inproceedings{jawahar_survey,
323	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
324	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
325	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
326	  year = {2020},
327	}
328	
329	% ===== Models =====
330	
331	@inproceedings{pythia,
332	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
333	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
334	  booktitle = {Proceedings of the International Conference on Machine Learning},
335	  year = {2023},
336	}
337	
338	@inproceedings{olmo,
339	  title = {{OLMo: Accelerating the Science of Language Models}},
340	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
341	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
342	  year = {2024},
343	}
344	
345	@article{qwen3,
346	  title = {{Qwen3 Technical Report}},
347	  author = {{Qwen Team}},
348	  journal = {arXiv preprint arXiv:2505.09388},
349	  year = {2025},
350	}
351	
352	% ===== Machine Learning =====
353	
354	@article{coral_ordinal,
355	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
356	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
357	  journal = {Pattern Recognition Letters},
358	  volume = {140},
359	  pages = {325--331},
360	  year = {2020},
361	}
362	
363	@inproceedings{frank_hall_ordinal,
364	  title = {{A Simple Approach to Ordinal Classification}},
365	  author = {Frank, Eibe and Hall, Mark},
366	  booktitle = {Proceedings of the European Conference on Machine Learning},
367	  year = {2001},
368	}
369	
370	@inproceedings{xgboost,
371	  title = {{XGBoost: A Scalable Tree Boosting System}},
372	  author = {Chen, Tianqi and Guestrin, Carlos},
373	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
374	  year = {2016},
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "8504e39c-10d7-48f4-a964-f3de3706bf50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
      "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks, Dan and Gimpel, Kevin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Hendrik},\n  year = {2022},\n  howpublished = {Technical Talk},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n% ===== Machine Learning =====\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n",
      "numLines": 376,
      "startLine": 1,
      "totalLines": 376
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01N6hFS4iRkFRzUgg3iX9UmJ`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c452e6b1-685a-4662-82a5-6dccfae47df5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12264
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 8 · 2026-05-15T23:58:15.253Z_

<details><summary>↩ Tool result · `toolu_01N6hFS4iRkFRzUgg3iX9UmJ`</summary>

````text
1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
89	
90	## 常见引用问题模式
91	
92	| 问题类型 | 特征 | 风险 |
93	|---------|------|------|
94	| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |
95	| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |
96	| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |
97	| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |
98	| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |
99	
100	## 输出格式
101	
102	审计完成后，生成结构化报告：
103	
104	```
105	## 引用审计报告
106	
107	**总数**: X 条引用
108	**已验证**: Y 条（OpenAlex confirmed）
109	**问题**: Z 条
110	
111	### 问题列表
112	
113	1. [severity: critical] `\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用
114	   - 建议：删除或替换为已验证的替代引用
115	
116	2. [severity: warning] `\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）
117	   - 建议：更新为正确年份
118	
119	3. [severity: info] `\cite{zzz}` — bib 中存在但正文未引用
120	   - 建议：删除或在相关段落补充引用
121	```
122	
123	## 设计参考
124	
125	本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。
126	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f8e26564-1a8e-4a6a-8798-2769b14a3921",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "content": "---\nname: reference-audit\ndescription: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。\nscope: global\ntags:\n- workflow\n- submission\n- writing\n- quality\npriority: 6\nversion: 2\nroles:\n- agent\n- paper_agent\n- review_reviewer\n- worker\n---\n\n# 引用验证与审计（Reference Audit）\n\n## 核心原则\n\n**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。\n\n## 触发条件\n\n- 写论文时添加引用\n- Review Reviewer 审查论文引用质量\n- 提交前最终检查\n- 发现可疑引用（年份不对、作者不存在、找不到原文）\n\n## 验证流程\n\n### 1. 单条引用验证（写论文时）\n\n每次需要引用时：\n\n1. **WebSearch 查找**：搜索论文标题 + 第一作者\n2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`\n3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue\n4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式\n5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中\n\n### 2. 全文引用审计（批量检查）\n\n**Step 1：调用 `verify_references(paper_dir)`**\n\n这是首选方式。该工具自动完成：\n- 解析所有 .bib 文件，提取结构化条目\n- 解析所有 .tex 文件，提取 `\\cite{}`/`\\citep{}`/`\\citet{}` 引用\n- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）\n- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）\n\n如果只需快速离线检查，传 `skip_online=True`。\n\n**Step 2：人工复核工具报告中的问题条目**\n\n重点关注：\n- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证\n- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本\n- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错\n- `orphan_bib` — .bib 中有但正文未引用，清理或补引用\n\n**Step 3：语义验证**（优先级排序）\n1. 首先验证 Introduction 和 Related Work 中的高频引用\n2. 然后验证 Method 中支撑技术 claim 的引用\n3. 最后验证其余引用\n\n对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。\n\n### 3. 验证失败处理\n\n**找不到论文时**：\n1. 检查拼写——标题或作者名是否有误？\n2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）\n3. 标记为 `[CITATION NEEDED]`\n4. 明确告知——说明哪条引用无法验证\n\n**信息不匹配时**：\n1. 确认是否找对了论文\n2. 检查版本——preprint vs published 版本\n3. 用最准确的版本更新信息\n\n**绝不做的事**：\n- 从记忆生成 BibTeX——AI 生成引用 40% 错误率\n- 跳过验证步骤\n- 假设论文存在\n- 对无法验证的引用不做标记\n\n## 常见引用问题模式\n\n| 问题类型 | 特征 | 风险 |\n|---------|------|------|\n| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |\n| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |\n| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |\n| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |\n| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |\n\n## 输出格式\n\n审计完成后，生成结构化报告：\n\n```\n## 引用审计报告\n\n**总数**: X 条引用\n**已验证**: Y 条（OpenAlex confirmed）\n**问题**: Z 条\n\n### 问题列表\n\n1. [severity: critical] `\\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用\n   - 建议：删除或替换为已验证的替代引用\n\n2. [severity: warning] `\\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）\n   - 建议：更新为正确年份\n\n3. [severity: info] `\\cite{zzz}` — bib 中存在但正文未引用\n   - 建议：删除或在相关段落补充引用\n```\n\n## 设计参考\n\n本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  }
}
````

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I need to verify each bib entry. Let me first use the `verify_references` tool to do an automated check, and then I'll use WebSearch to verify specific entries. Let me load the necessary tools first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "3557e49b-3c60-41bd-9060-9d1090c6d38e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9137
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

读取完成，共 37 条 bib 条目。先用 `verify_references` 做自动化检查，再逐条 WebSearch 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "fc2d0540-5a8a-4f74-b8c0-3c9b14b9071a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9137
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PDJ3XKjuuKoykb2mPNNcUR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "27d785e9-4621-4ae3-a73c-f3d6fbda74c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9137
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

_source line 12 · 2026-05-15T23:58:20.310Z_

<details><summary>↩ Tool result · `toolu_01PDJ3XKjuuKoykb2mPNNcUR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```

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
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e2f673a5-ce68-4871-ae98-22574383cd37",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__verify_references",
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__verify_references,WebSearch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_0178MVSmD67m2GvoRDYNrVm1`</summary>

```json
{
  "paper_dir": "docs/paper",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9aa3eb11-66b9-4609-b838-a8349ce12f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMA2md9cptWNbReUgDTEBA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 33242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 14 · 2026-05-15T23:59:15.854Z_

<details><summary>↩ Tool result · `toolu_0178MVSmD67m2GvoRDYNrVm1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the First Conference on Language Modeling (COLM)\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 72, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "87b6711a-b554-4191-bc26-3656c303b738",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 72, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 41, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"authors\\\": \\\"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"authors\\\": \\\"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"authors\\\": \\\"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"authors\\\": \\\"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"authors\\\": \\\"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"authors\\\": \\\"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.01647\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"authors\\\": \\\"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Basani, Advik Raj and Chen, Pin-Yu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"authors\\\": \\\"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2604.13692\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"authors\\\": \\\"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\\\\\\\\\"orn\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.03969\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"authors\\\": \\\"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"authors\\\": \\\"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"authors\\\": \\\"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"authors\\\": \\\"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1908.09203\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"authors\\\": \\\"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"authors\\\": \\\"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Workshop on Semantic Evaluation\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"authors\\\": \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"authors\\\": \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"authors\\\": \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the First Conference on Language Modeling (COLM)\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"authors\\\": \\\"Hendrycks, Dan and Gimpel, Kevin\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"authors\\\": \\\"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"authors\\\": \\\"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Language Resources and Evaluation Conference\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"authors\\\": \\\"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"authors\\\": \\\"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"authors\\\": \\\"Aaronson, Scott and Kirchner, Hendrik\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"authors\\\": \\\"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.05503\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"authors\\\": \\\"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\\\\\'e\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"authors\\\": \\\"Padmakumar, Vishakh and He, He\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"authors\\\": \\\"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Language Modeling\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"authors\\\": \\\"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"authors\\\": \\\"Stamatatos, Efstathios\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"authors\\\": \\\"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"authors\\\": \\\"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"authors\\\": \\\"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the European Chapter of the Association for Com...\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"authors\\\": \\\"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.11228\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"authors\\\": \\\"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"authors\\\": \\\"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"authors\\\": \\\"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Computational Linguistics\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"authors\\\": \\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"authors\\\": \\\"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"authors\\\": \\\"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Pattern Recognition Letters\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"authors\\\": \\\"Frank, Eibe and Hall, Mark\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"Proceedings of the European Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"authors\\\": \\\"Chen, Tianqi and Guestrin, Carlos\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"mapping_llm_science\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 36, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 46, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 58, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 72, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 78, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 78, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.382, \\\"matched_title\\\": \\\"Regulating ChatGPT and other Large Generative AI Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.344, \\\"matched_title\\\": \\\"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.253, \\\"matched_title\\\": \\\"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Defending Against Neural Fake News\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consuming Generative Models go MAD\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=alemohammad vs api=casco-rodriguez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Strong Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Watermark for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable watermarking for identifying large language model outputs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.418, \\\"matched_title\\\": \\\"Undetectable Watermarks for Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.42 below threshold 0.82\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A survey of modern authorship attribution methods\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Computational methods in authorship attribution\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.497, \\\"matched_title\\\": \\\"The TRIPOD-LLM reporting guideline for studies using large language models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rank consistent ordinal regression for neural networks with application to age estimation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"matched_year\\\": \\\"2001\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.298, \\\"matched_title\\\": \\\"XGBoost\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the First Conference on Language Modeling (COLM)\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 72, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the OpenAlex results. I have:

**not_found (6)**:
1. `detectgpt` - OpenAlex didn't find it, but this is a very well-known paper (Mitchell et al., ICML 2023). This is an OpenAlex search limitation.
2. `reliable_detection` - Sadasivan et al. OpenAlex didn't find it, but it's a well-known paper.
3. `detection_possibilities` - Chakraborty et al. ICML 2024. OpenAlex search issue.


4. `aaronson_watermark` - This is a blog post/talk rather than a formal paper, so OpenAlex won't have it.
5. `pythia` - Very well-known paper (Biderman et al., ICML 2023) that OpenAlex is missing.
6. `xgboost` - Very well-known paper (Chen & Guestrin, KDD 2016) that OpenAlex is also missing.

**mismatch (2)**:
1. `self_consuming_mad` - OpenAlex has year=2023 while the bibliography says 2024, and there's a first author discrepancy between Alemohammad and Casco-Rodriguez that I need to verify.
2. `qwen3` - The first author differs because the bibliography lists "{Qwen Team}" while OpenAlex parsed it as Yang.

Looking at year discrepancies across the verified OpenAlex entries, I'm seeing a pattern where several papers have different years in the bibliography versus OpenAlex—likely due to preprint versus published versions. The entries like `dna_gpt`, `fast_detectgpt`, `writing_diversity`, and `nucleus_sampling` show this pattern, while others like `diveye`, `ood_baseline`, and `ccnet` have more significant year gaps that warrant investigation.

I should prioritize web searches for the entries that are either not found or have mismatches, starting with the most critical ones to verify the correct publication years.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ffc2584f-d925-42a0-b66d-436044181d25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13517
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

_source line 16_

OpenAlex 报告：41 verified, 6 not_found, 2 mismatch。还有多条年份可能不一致。现在用 WebSearch 逐条验证所有可疑条目。

先验证 6 个 not_found + 2 个 mismatch，以及 OpenAlex 返回年份与 bib 不一致的条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "30aa605d-9b84-41a3-869d-4688db36b0df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13517
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

_source line 17_

<details open><summary>🔧 Tool call — Agent · `toolu_015qtuXZaLvJjFpcwfBu7UE5`</summary>

```json
{
  "description": "Verify batch 1: not_found entries",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.\n\nPapers to verify:\n\n1. **detectgpt** — bib claims: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023\n\n2. **reliable_detection** — bib claims: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025\n\n3. **detection_possibilities** — bib claims: \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024\n\n4. **aaronson_watermark** — bib claims: \"Watermarking GPT Outputs\", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk\n\n5. **pythia** — bib claims: \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023\n\n6. **xgboost** — bib claims: \"XGBoost: A Scalable Tree Boosting System\", Chen, Tianqi and Guestrin, Carlos, KDD 2016\n\nReport all findings precisely, including any year, author, or venue discrepancies.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "5b722315-6b83-44e9-a00c-c70017944576",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13517
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

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Verify batch 1: not_found entries",
  "task_type": "local_agent",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.\n\nPapers to verify:\n\n1. **detectgpt** — bib claims: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023\n\n2. **reliable_detection** — bib claims: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025\n\n3. **detection_possibilities** — bib claims: \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024\n\n4. **aaronson_watermark** — bib claims: \"Watermarking GPT Outputs\", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk\n\n5. **pythia** — bib claims: \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023\n\n6. **xgboost** — bib claims: \"XGBoost: A Scalable Tree Boosting System\", Chen, Tianqi and Guestrin, Carlos, KDD 2016\n\nReport all findings precisely, including any year, author, or venue discrepancies.",
  "uuid": "92a26448-f393-479a-8d41-0e1d4ecb67ae",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

## Round 1

16 recorded events

### User

_source line 19 · 2026-05-15T23:59:44.493Z_

I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.

Papers to verify:

1. **detectgpt** — bib claims: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023

2. **reliable_detection** — bib claims: "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025

3. **detection_possibilities** — bib claims: "Position: On the Possibilities of AI-Generated Text Detection", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024

4. **aaronson_watermark** — bib claims: "Watermarking GPT Outputs", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk

5. **pythia** — bib claims: "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023

6. **xgboost** — bib claims: "XGBoost: A Scalable Tree Boosting System", Chen, Tianqi and Guestrin, Carlos, KDD 2016

Report all findings precisely, including any year, author, or venue discrepancies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "70dcd615-65df-4499-b46e-3967231a7d6b"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Verify batch 1: not_found entries",
  "usage": {
    "total_tokens": 15578,
    "tool_uses": 1,
    "duration_ms": 2830
  },
  "last_tool_name": "ToolSearch",
  "uuid": "3dac2694-8e0b-44f4-a6a3-fcb32e168904",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for detectgpt|reliable_detection|detection_possibilit…",
  "usage": {
    "total_tokens": 17043,
    "tool_uses": 2,
    "duration_ms": 6105
  },
  "last_tool_name": "Grep",
  "uuid": "eed28236-b72f-4793-a730-58ee35733b05",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 17266,
    "tool_uses": 3,
    "duration_ms": 9140
  },
  "last_tool_name": "Read",
  "uuid": "c6f9a30c-f395-484d-9538-17308d3c5ebe",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for DetectGPT Zero-Shot Machine-Generated Text Detect…",
  "usage": {
    "total_tokens": 24274,
    "tool_uses": 4,
    "duration_ms": 13162
  },
  "last_tool_name": "WebSearch",
  "uuid": "f4080d0c-76a4-4e87-876b-610d96f3f1c8",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"Can AI-Generated Text be Reliably Detected\" Sada…",
  "usage": {
    "total_tokens": 24275,
    "tool_uses": 5,
    "duration_ms": 14567
  },
  "last_tool_name": "WebSearch",
  "uuid": "d80f6856-d38b-4873-b4c8-537b85717793",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LrqCmgWwciQwHTYSAnRA4v`</summary>

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
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f41bf1d1-594a-4453-8bc0-cb9cd13b2b5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FZjUfftdcqmEx276uzAgG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15567,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15567,
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

_source line 26 · 2026-05-15T23:59:47.327Z_

<details><summary>↩ Tool result · `toolu_01LrqCmgWwciQwHTYSAnRA4v`</summary>

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
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1c8b96e7-a8d2-4dd5-916d-9325b824072e"
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01QKDJ1Q8QcACcp46DBUbSnY`</summary>

```json
{
  "pattern": "detectgpt|reliable_detection|detection_possibilities|aaronson_watermark|pythia|xgboost",
  "glob": "*.bib",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "4fd696f0-5660-4e92-86f3-356a44bb87df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5ysTffEFj5hBy3xgp7dzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15567,
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

_source line 28 · 2026-05-15T23:59:50.616Z_

<details><summary>↩ Tool result · `toolu_01QKDJ1Q8QcACcp46DBUbSnY`</summary>

```text
Found 2 files
docs/paper/references.bib
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "fcfcc2b0-b3bd-41bf-a795-6f7e985cf978"
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01TKGTrBSDwzxbMKUkcSZtLH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "08d92443-caa5-44cd-a7fd-e25308850425",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACqSdLJ3EZzawqzTEwm3u7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 17028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 182,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 30 · 2026-05-15T23:59:53.639Z_

<details><summary>↩ Tool result · `toolu_01TKGTrBSDwzxbMKUkcSZtLH`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	}
140	
141	@inproceedings{strong_model_collapse,
142	  title = {{Strong Model Collapse}},
143	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
144	  booktitle = {Proceedings of the International Conference on Learning Representations},
145	  year = {2025},
146	}
147	
148	@inproceedings{model_collapse_avoidable,
149	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
150	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
151	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
152	  year = {2024},
153	}
154	
155	% ===== OOD Detection =====
156	
157	@inproceedings{ood_baseline,
158	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
159	  author = {Hendrycks, Dan and Gimpel, Kevin},
160	  booktitle = {Proceedings of the International Conference on Learning Representations},
161	  year = {2017},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{dsir,
167	  title = {{Data Selection for Language Models via Importance Resampling}},
168	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
169	  booktitle = {Advances in Neural Information Processing Systems},
170	  year = {2023},
171	}
172	
173	@inproceedings{qurating,
174	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
175	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
176	  booktitle = {Proceedings of the International Conference on Machine Learning},
177	  year = {2024},
178	}
179	
180	@inproceedings{ccnet,
181	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
182	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
183	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
184	  year = {2020},
185	}
186	
187	% ===== Watermarking =====
188	
189	@inproceedings{watermark_llm,
190	  title = {{A Watermark for Large Language Models}},
191	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
192	  booktitle = {Proceedings of the International Conference on Machine Learning},
193	  year = {2023},
194	}
195	
196	@article{synthid_text,
197	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
198	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
199	  journal = {Nature},
200	  volume = {634},
201	  pages = {818--823},
202	  year = {2024},
203	}
204	
205	@misc{aaronson_watermark,
206	  title = {{Watermarking GPT Outputs}},
207	  author = {Aaronson, Scott and Kirchner, Hendrik},
208	  year = {2022},
209	  howpublished = {Technical Talk},
210	  url = {https://scottaaronson.blog/?p=6823},
211	}
212	
213	@article{chainwash,
214	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
215	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
216	  journal = {arXiv preprint arXiv:2605.05503},
217	  year = {2026},
218	}
219	
220	% ===== Vocabulary Diversity =====
221	
222	@inproceedings{curious_decline,
223	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
224	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
225	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
226	  year = {2024},
227	}
228	
229	@inproceedings{writing_diversity,
230	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
231	  author = {Padmakumar, Vishakh and He, He},
232	  booktitle = {Proceedings of the International Conference on Learning Representations},
233	  year = {2024},
234	}
235	
236	@inproceedings{nucleus_sampling,
237	  title = {{The Curious Case of Neural Text Degeneration}},
238	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
239	  booktitle = {Proceedings of the International Conference on Learning Representations},
240	  year = {2020},
241	}
242	
243	@inproceedings{mapping_llm_science,
244	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
245	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
246	  booktitle = {Proceedings of the Conference on Language Modeling},
247	  year = {2024},
248	}
249	
250	@inproceedings{monitoring_ai_review,
251	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
252	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
253	  booktitle = {Proceedings of the International Conference on Machine Learning},
254	  year = {2024},
255	}
256	
257	% ===== Stylometry =====
258	
259	@article{stamatatos_survey,
260	  title = {{A Survey of Modern Authorship Attribution Methods}},
261	  author = {Stamatatos, Efstathios},
262	  journal = {Journal of the American Society for Information Science and Technology},
263	  year = {2009},
264	}
265	
266	@article{koppel_authorship,
267	  title = {{Computational Methods in Authorship Attribution}},
268	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
269	  journal = {Journal of the American Society for Information Science and Technology},
270	  year = {2009},
271	}
272	
273	@inproceedings{uchendu_attribution,
274	  title = {{Authorship Attribution for Neural Text Generation}},
275	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
276	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
277	  year = {2020},
278	}
279	
280	@inproceedings{munir_looking_glass,
281	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
282	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
283	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
284	  year = {2021},
285	}
286	
287	% ===== Iterative Generation =====
288	
289	@inproceedings{broken_telephone,
290	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
291	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
292	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
293	  year = {2025},
294	}
295	
296	@article{markovian_chains,
297	  title = {{Markovian Generation Chains in Large Language Models}},
298	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
299	  journal = {arXiv preprint arXiv:2603.11228},
300	  year = {2026},
301	}
302	
303	% ===== Membership Inference =====
304	
305	@inproceedings{min_k_percent,
306	  title = {{Detecting Pretraining Data from Large Language Models}},
307	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
308	  booktitle = {Proceedings of the International Conference on Learning Representations},
309	  year = {2024},
310	}
311	
312	% ===== Survey =====
313	
314	@article{wu_survey_2025,
315	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
316	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
317	  journal = {Computational Linguistics},
318	  publisher = {MIT Press},
319	  year = {2025},
320	}
321	
322	@inproceedings{jawahar_survey,
323	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
324	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
325	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
326	  year = {2020},
327	}
328	
329	% ===== Models =====
330	
331	@inproceedings{pythia,
332	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
333	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
334	  booktitle = {Proceedings of the International Conference on Machine Learning},
335	  year = {2023},
336	}
337	
338	@inproceedings{olmo,
339	  title = {{OLMo: Accelerating the Science of Language Models}},
340	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
341	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
342	  year = {2024},
343	}
344	
345	@article{qwen3,
346	  title = {{Qwen3 Technical Report}},
347	  author = {{Qwen Team}},
348	  journal = {arXiv preprint arXiv:2505.09388},
349	  year = {2025},
350	}
351	
352	% ===== Machine Learning =====
353	
354	@article{coral_ordinal,
355	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
356	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
357	  journal = {Pattern Recognition Letters},
358	  volume = {140},
359	  pages = {325--331},
360	  year = {2020},
361	}
362	
363	@inproceedings{frank_hall_ordinal,
364	  title = {{A Simple Approach to Ordinal Classification}},
365	  author = {Frank, Eibe and Hall, Mark},
366	  booktitle = {Proceedings of the European Conference on Machine Learning},
367	  year = {2001},
368	}
369	
370	@inproceedings{xgboost,
371	  title = {{XGBoost: A Scalable Tree Boosting System}},
372	  author = {Chen, Tianqi and Guestrin, Carlos},
373	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
374	  year = {2016},
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "b7114fd4-82a6-40bd-b823-e7cf6bee3a25"
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018WFmiRKZbDexJ4AKyb1oB9`</summary>

```json
{
  "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "798ebe83-b436-4712-9a45-5cb93d6a7111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pb25GR443Hf9WT5i33uQiX`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan Kumar Balasubramanian Wang Feizi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "a0c75f52-c22e-4934-8385-27d5e5b7a521",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 33_

<details open><summary>🔧 Tool call — Agent · `toolu_01MfNwpzXjZ5JJuaohdfNX9D`</summary>

```json
{
  "description": "Verify batch 2: mismatches + year discrepancies",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.\n\n**Mismatch entries:**\n\n1. **self_consuming_mad** — bib claims: \"Self-Consuming Generative Models Go MAD\", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.\n\n2. **qwen3** — bib claims: \"Qwen3 Technical Report\", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.\n\n**Year discrepancy entries (OpenAlex verified year differs from bib year):**\n\n3. **dna_gpt** — bib=2024, OpenAlex=2023. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", Yang et al., ICLR 2024.\n\n4. **fast_detectgpt** — bib=2024, OpenAlex=2023. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", Bao et al., ICLR 2024.\n\n5. **diveye** — bib=2026, OpenAlex=2025. \"Diversity Boosts AI-Generated Text Detection\", Basani, Advik Raj and Chen, Pin-Yu, TMLR.\n\n6. **ood_baseline** — bib=2017, OpenAlex=2016. \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.\n\n7. **ccnet** — bib=2020, OpenAlex=2019. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", Wenzek et al., LREC 2020.\n\n8. **writing_diversity** — bib=2024, OpenAlex=2023. \"Does Writing with Language Models Reduce Content Diversity?\", Padmakumar, Vishakh and He, He, ICLR 2024.\n\n9. **nucleus_sampling** — bib=2020, OpenAlex=2019. \"The Curious Case of Neural Text Degeneration\", Holtzman et al., ICLR 2020.\n\n10. **min_k_percent** — bib=2024, OpenAlex=2023. \"Detecting Pretraining Data from Large Language Models\", Shi et al., ICLR 2024.\n\n11. **stamatatos_survey** — bib=2009, OpenAlex=2008. \"A Survey of Modern Authorship Attribution Methods\", Stamatatos, Efstathios, JASIST.\n\n12. **koppel_authorship** — bib=2009, OpenAlex=2008. \"Computational Methods in Authorship Attribution\", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.\n\n13. **strong_model_collapse** — bib=2025, OpenAlex=2024. \"Strong Model Collapse\", Dohmatob et al., ICLR 2025.\n\nFor each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "a29433b9-d67b-473e-8479-05890da1b7a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13517
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

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Verify batch 2: mismatches + year discrepancies",
  "task_type": "local_agent",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.\n\n**Mismatch entries:**\n\n1. **self_consuming_mad** — bib claims: \"Self-Consuming Generative Models Go MAD\", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.\n\n2. **qwen3** — bib claims: \"Qwen3 Technical Report\", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.\n\n**Year discrepancy entries (OpenAlex verified year differs from bib year):**\n\n3. **dna_gpt** — bib=2024, OpenAlex=2023. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", Yang et al., ICLR 2024.\n\n4. **fast_detectgpt** — bib=2024, OpenAlex=2023. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", Bao et al., ICLR 2024.\n\n5. **diveye** — bib=2026, OpenAlex=2025. \"Diversity Boosts AI-Generated Text Detection\", Basani, Advik Raj and Chen, Pin-Yu, TMLR.\n\n6. **ood_baseline** — bib=2017, OpenAlex=2016. \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.\n\n7. **ccnet** — bib=2020, OpenAlex=2019. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", Wenzek et al., LREC 2020.\n\n8. **writing_diversity** — bib=2024, OpenAlex=2023. \"Does Writing with Language Models Reduce Content Diversity?\", Padmakumar, Vishakh and He, He, ICLR 2024.\n\n9. **nucleus_sampling** — bib=2020, OpenAlex=2019. \"The Curious Case of Neural Text Degeneration\", Holtzman et al., ICLR 2020.\n\n10. **min_k_percent** — bib=2024, OpenAlex=2023. \"Detecting Pretraining Data from Large Language Models\", Shi et al., ICLR 2024.\n\n11. **stamatatos_survey** — bib=2009, OpenAlex=2008. \"A Survey of Modern Authorship Attribution Methods\", Stamatatos, Efstathios, JASIST.\n\n12. **koppel_authorship** — bib=2009, OpenAlex=2008. \"Computational Methods in Authorship Attribution\", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.\n\n13. **strong_model_collapse** — bib=2025, OpenAlex=2024. \"Strong Model Collapse\", Dohmatob et al., ICLR 2025.\n\nFor each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.",
  "uuid": "82fbb517-d08c-41e5-bea5-8ba75f5910c1",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

## Round 2

56 recorded events

### User

_source line 35 · 2026-05-15T23:59:59.742Z_

I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.

**Mismatch entries:**

1. **self_consuming_mad** — bib claims: "Self-Consuming Generative Models Go MAD", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.

2. **qwen3** — bib claims: "Qwen3 Technical Report", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.

**Year discrepancy entries (OpenAlex verified year differs from bib year):**

3. **dna_gpt** — bib=2024, OpenAlex=2023. "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text", Yang et al., ICLR 2024.

4. **fast_detectgpt** — bib=2024, OpenAlex=2023. "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature", Bao et al., ICLR 2024.

5. **diveye** — bib=2026, OpenAlex=2025. "Diversity Boosts AI-Generated Text Detection", Basani, Advik Raj and Chen, Pin-Yu, TMLR.

6. **ood_baseline** — bib=2017, OpenAlex=2016. "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.

7. **ccnet** — bib=2020, OpenAlex=2019. "CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data", Wenzek et al., LREC 2020.

8. **writing_diversity** — bib=2024, OpenAlex=2023. "Does Writing with Language Models Reduce Content Diversity?", Padmakumar, Vishakh and He, He, ICLR 2024.

9. **nucleus_sampling** — bib=2020, OpenAlex=2019. "The Curious Case of Neural Text Degeneration", Holtzman et al., ICLR 2020.

10. **min_k_percent** — bib=2024, OpenAlex=2023. "Detecting Pretraining Data from Large Language Models", Shi et al., ICLR 2024.

11. **stamatatos_survey** — bib=2009, OpenAlex=2008. "A Survey of Modern Authorship Attribution Methods", Stamatatos, Efstathios, JASIST.

12. **koppel_authorship** — bib=2009, OpenAlex=2008. "Computational Methods in Authorship Attribution", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.

13. **strong_model_collapse** — bib=2025, OpenAlex=2024. "Strong Model Collapse", Dohmatob et al., ICLR 2025.

For each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f9b03d51-4e5e-42e4-9f53-18b3487e0451"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"Position: On the Possibilities of AI-Generated T…",
  "usage": {
    "total_tokens": 24276,
    "tool_uses": 6,
    "duration_ms": 15660
  },
  "last_tool_name": "WebSearch",
  "uuid": "281521cb-8513-4b13-ad13-c775d17635b5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SBvUfps7J7JjdjwFLeQGGt`</summary>

```json
{
  "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "0e4afbdb-cd1b-4761-b74d-56fd21bf482c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for Aaronson Kirchner \"Watermarking GPT Outputs\" 2022",
  "usage": {
    "total_tokens": 24277,
    "tool_uses": 7,
    "duration_ms": 16159
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2552237-f7c5-4885-b06b-894579d73aac",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for Pythia Suite Analyzing Large Language Models Trai…",
  "usage": {
    "total_tokens": 24278,
    "tool_uses": 8,
    "duration_ms": 17099
  },
  "last_tool_name": "WebSearch",
  "uuid": "621b5a2a-6074-47da-8c7e-61aa960d168b",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for XGBoost Scalable Tree Boosting System Chen Guestr…",
  "usage": {
    "total_tokens": 24279,
    "tool_uses": 9,
    "duration_ms": 17456
  },
  "last_tool_name": "WebSearch",
  "uuid": "5cf25d14-dc74-4eb4-a100-309d116602eb",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 15960,
    "tool_uses": 1,
    "duration_ms": 4344
  },
  "last_tool_name": "Read",
  "uuid": "d6f26087-5787-4212-b6a2-5bd101704d3c",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Verify batch 2: mismatches + year discrepancies",
  "usage": {
    "total_tokens": 15967,
    "tool_uses": 2,
    "duration_ms": 4490
  },
  "last_tool_name": "ToolSearch",
  "uuid": "79255fac-c6be-4316-bd3d-7268f6a35944",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Self-Consuming Generative Models Go MAD Alemohamm…",
  "usage": {
    "total_tokens": 24503,
    "tool_uses": 3,
    "duration_ms": 8070
  },
  "last_tool_name": "WebSearch",
  "uuid": "910178c2-e19f-4061-999b-831b72f94b74",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Qwen3 Technical Report arXiv 2505.09388 author li…",
  "usage": {
    "total_tokens": 24505,
    "tool_uses": 4,
    "duration_ms": 9007
  },
  "last_tool_name": "WebSearch",
  "uuid": "8bb5fe91-0724-441a-9785-67a1f015ad1d",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for DNA-GPT Divergent N-Gram Analysis Training-Free D…",
  "usage": {
    "total_tokens": 24507,
    "tool_uses": 5,
    "duration_ms": 10023
  },
  "last_tool_name": "WebSearch",
  "uuid": "0e07998c-c0cc-43f9-ab42-d097c48a9641",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Fast-DetectGPT Efficient Zero-Shot Detection Mach…",
  "usage": {
    "total_tokens": 24509,
    "tool_uses": 6,
    "duration_ms": 10503
  },
  "last_tool_name": "WebSearch",
  "uuid": "effa5b8e-8b20-45b8-982b-64b03f27cb09",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Diversity Boosts AI-Generated Text Detection\" Ba…",
  "usage": {
    "total_tokens": 24511,
    "tool_uses": 7,
    "duration_ms": 12006
  },
  "last_tool_name": "WebSearch",
  "uuid": "dee652d9-1e0b-414e-a3ac-c4b1a65d55ee",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"Can AI-Generated Text be Reliably Detected\" TMLR…",
  "usage": {
    "total_tokens": 30229,
    "tool_uses": 10,
    "duration_ms": 27594
  },
  "last_tool_name": "WebSearch",
  "uuid": "50a3a1b1-2f0d-4ff7-a4ac-8f0ace1d0919",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"A Baseline for Detecting Misclassified and Out-o…",
  "usage": {
    "total_tokens": 24513,
    "tool_uses": 8,
    "duration_ms": 12480
  },
  "last_tool_name": "WebSearch",
  "uuid": "b21df3a0-6ae1-4370-a211-4d16e3507fa4",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for Pythia Biderman ICML 2023 full author list all au…",
  "usage": {
    "total_tokens": 30230,
    "tool_uses": 11,
    "duration_ms": 28945
  },
  "last_tool_name": "WebSearch",
  "uuid": "7f5458ff-9d44-48c8-8b02-63ab951699c7",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for CCNet Extracting High Quality Monolingual Dataset…",
  "usage": {
    "total_tokens": 24515,
    "tool_uses": 9,
    "duration_ms": 13862
  },
  "last_tool_name": "WebSearch",
  "uuid": "ebbd4b80-f287-47c9-84af-8093cd868b8d",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for Scott Aaronson \"Watermarking GPT Outputs\" talk da…",
  "usage": {
    "total_tokens": 30231,
    "tool_uses": 12,
    "duration_ms": 29978
  },
  "last_tool_name": "WebSearch",
  "uuid": "ebe7bc3e-72fe-4320-bb0f-58d412624111",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"Can AI-Generated Text be Reliably Detected\" Sada…",
  "usage": {
    "total_tokens": 30232,
    "tool_uses": 13,
    "duration_ms": 30465
  },
  "last_tool_name": "WebSearch",
  "uuid": "d762697c-de0f-4216-9d3e-726538931269",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F1uMKvk8kwBP1j6SL5EEEj`</summary>

```json
{
  "query": "Aaronson Kirchner \"Watermarking GPT Outputs\" 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1c160aac-4001-4a8e-ac47-1a9b18351c7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 55_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016bGJouhe2fvuAj1r5DCTPS`</summary>

```json
{
  "query": "Pythia Suite Analyzing Large Language Models Training Scaling Biderman Schoelkopf ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d60aa850-4700-4743-9388-2472149ea2aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsrEEj8v3p5aLTgy81u5Sr`</summary>

```json
{
  "query": "XGBoost Scalable Tree Boosting System Chen Guestrin KDD 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ec3f1f10-f3ae-4953-91c1-887cb07a20f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKqg5jcYdcqzNSon7U4RuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7006,
      "cache_read_input_tokens": 17210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7006,
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

_source line 57 · 2026-05-16T00:00:02.471Z_

<details><summary>↩ Tool result · `toolu_018WFmiRKZbDexJ4AKyb1oB9`</summary>

```text
Web search results for query: "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"ICML 2023 DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Oral","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"}]

I found comprehensive information about the DetectGPT paper. Here are the key details:

## Paper Overview

DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature was authored by Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn, and was published at ICML 2023.

## Core Contribution

The paper demonstrates that text sampled from an LLM tends to occupy negative curvature regions of the model's log probability function, and defines a new curvature-based criterion for judging if a passage is generated from a given LLM.

## Key Features

DetectGPT does not require training a separate classifier, collecting a dataset of real or generated passages, or explicitly watermarking generated text, and uses only log probabilities computed by the model of interest and random perturbations of the passage from another generic pre-trained language model (e.g., T5).

## Performance Results

DetectGPT is more discriminative than existing zero-shot methods for model sample detection, notably improving detection of fake news articles generated by 20B parameter GPT-NeoX from 0.81 AUROC for the strongest zero-shot baseline to 0.95 AUROC for DetectGPT.

The paper is available on arXiv (2301.11305) and through the official ICML proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "bdd2140e-9e45-4d56-b337-f606ab637145"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T00:00:04.400Z_

<details><summary>↩ Tool result · `toolu_01Pb25GR443Hf9WT5i33uQiX`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan Kumar Balasubramanian Wang Feizi"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"No reliable way to detect AI-generated text, boffins say • The Register","url":"https://www.theregister.com/2023/03/21/detecting_ai_generated_text/"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"[2303.11156v1] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v1"}]

I found the research paper you were looking for! Here's a summary of the search results:

## Paper Overview

The paper "Can AI-Generated Text be Reliably Detected?" was authored by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

## Key Findings

The researchers show that AI text detectors are not reliable in practical scenarios, and they developed a recursive paraphrasing attack that can break a wide range of detectors, including those using watermarking schemes as well as neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

## Main Results

The paper demonstrates that an adversary can infer hidden AI text signatures of LLM outputs without having white-box access to the detection method, and provides a theoretical connection between the AUROC of the best possible detector and the Total Variation distance between human and AI text distributions that can be used to study the fundamental hardness of the reliable detection problem.

The paper is available on arXiv (2303.11156) and has been regularly updated, with the latest version from January 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c960d8a9-60a7-443d-9f5f-c40b27502ddc"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T00:00:06.206Z_

<details><summary>↩ Tool result · `toolu_016bGJouhe2fvuAj1r5DCTPS`</summary>

```text
Web search results for query: "Pythia Suite Analyzing Large Language Models Training Scaling Biderman Schoelkopf ICML 2023"

Links: [{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling [Quick Review]","url":"https://liner.com/review/pythia-suite-for-analyzing-large-language-models-across-training-and"},{"title":"ICML Poster Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://icml.cc/virtual/2023/poster/24093"},{"title":"GitHub - EleutherAI/pythia: The hub for EleutherAI's work on interpretability and learning dynamics · GitHub","url":"https://github.com/EleutherAI/pythia"},{"title":"ICML 2023 Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling Oral","url":"https://icml.cc/virtual/2023/oral/25487"},{"title":"Pythia: a suite for analyzing large language models across ...","url":"https://dl.acm.org/doi/10.5555/3618408.3618510"},{"title":"Paper page - Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://huggingface.co/papers/2304.01373"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"}]

The search results contain comprehensive information about the Pythia paper. Here's what I found:

## Overview

The paper "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling" was authored by Stella Biderman, Hailey Schoelkopf, and others, and was published at ICML 2023 (pages 2397-2430).

## Key Components

Pythia is a suite of 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters. The suite provides public access to 154 checkpoints for each one of the 16 models, alongside tools to download and reconstruct their exact training dataloaders for further study.

## Research Focus

The paper addresses the questions of how large language models develop and evolve over the course of training, and how these patterns change as models scale. The research presents several case studies including novel results in memorization, term frequency effects on few-shot performance, and reducing gender bias.

## Resources

Trained models, analysis code, training code, and training data can be found at https://github.com/EleutherAI/pythia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "81359ccc-5664-446c-a412-5f743c5f38b5"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T00:00:06.237Z_

<details><summary>↩ Tool result · `toolu_01SBvUfps7J7JjdjwFLeQGGt`</summary>

```text
Web search results for query: ""Position: On the Possibilities of AI-Generated Text Detection" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/1c9693a721271e3f915f0f0b8159578495d5c815"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"}]

I found the paper you're looking for! Here's what I found:

## Publication Details

The paper "Position: On the Possibilities of AI-Generated Text Detection" by Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, and Furong Huang was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 6093-6115.

## Main Focus

The study addresses the challenge of distinguishing human-written text from Large Language Model (LLM) outputs, and provides evidence that this differentiation is consistently feasible, except when human and machine text distributions are indistinguishable across their entire support.

## Key Findings

The paper employs information theory to show that while detecting machine-generated text becomes harder as it nears human quality, it remains possible with adequate text data, and introduces guidelines on the required text data quantity, either through sample size or sequence length, for reliable AI text detection, through derivations of sample complexity bounds.

The paper is available through the ICML proceedings at the official PMLR (Proceedings of Machine Learning Research) website, as well as on arXiv and other academic platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "cbd2d281-1b45-4470-890f-93e89570fa03"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-16T00:00:06.747Z_

<details><summary>↩ Tool result · `toolu_01F1uMKvk8kwBP1j6SL5EEEj`</summary>

```text
Web search results for query: "Aaronson Kirchner "Watermarking GPT Outputs" 2022"

Links: [{"title":"The Future of Computer Science","url":"https://www.scottaaronson.com/talks/watermark.ppt"},{"title":"Watermarking Needs Input Repetition Masking","url":"https://arxiv.org/html/2504.12229v1"},{"title":"Watermarking Language Models with Error Correcting Codes","url":"https://arxiv.org/html/2406.10281v1"},{"title":"Watermarking Makes Language Models Radioactive Tom Sander∗","url":"https://arxiv.org/pdf/2402.14904"},{"title":"Three Bricks to Consolidate Watermarks for Large Language Models | Pierre Fernandez","url":"https://pierrefdz.github.io/publications/threebricks/"},{"title":"Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite Attacks","url":"https://arxiv.org/html/2505.05190v1"},{"title":"WATERMARKING FOR USER IDENTIFICATION IN LARGE ...","url":"https://openreview.net/pdf?id=ZACAKudvKW"},{"title":"Watermarking Makes Language Models Radioactive","url":"https://arxiv.org/html/2402.14904v1"},{"title":"20 - ‘Reform’ AI Alignment with Scott Aaronson | AXRP - the AI X-risk Research Podcast","url":"https://axrp.net/episode/2023/04/11/episode-20-reform-ai-alignment-scott-aaronson.html"},{"title":"Scott Aaronson: Against AI Doomerism - by daniel bashir","url":"https://thegradientpub.substack.com/p/scott-aaronson-against-ai-doomerism"}]

Based on the search results, I found relevant information about the Aaronson and Kirchner "Watermarking GPT Outputs" work:

The talk "Watermarking GPT Outputs" was presented at OpenAI in San Francisco on December 13, 2022, and another version was presented at UT Austin Math Club on October 18, 2022.

Aaronson and Kirchner (2022), in collaboration with OpenAI, proposed a biasing-based watermarking method utilizing exponential minimum sampling by hashing previous tokens. Watermarks enable more precise detection and even attribution of the source by subtly embedding a unique signature within generated content.

The approach modifies the sampling process during the generation phase itself, and while there are exponentially many combinations of words and characters, watermarking biases generation towards specific patterns that are undetectable to humans.

The work has become influential in the field—Aaronson (2022) is one of two most popular watermarking schemes in the current literature, and the methodology has been widely referenced in subsequent AI safety and detection research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "faa367f6-cc62-4922-8559-3711011a23ac"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T00:00:06.950Z_

<details><summary>↩ Tool result · `toolu_01JsrEEj8v3p5aLTgy81u5Sr`</summary>

```text
Web search results for query: "XGBoost Scalable Tree Boosting System Chen Guestrin KDD 2016"

Links: [{"title":"Chen, T. and Guestrin, C. (2016) XGBoost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3417949"},{"title":"[1603.02754] XGBoost: A Scalable Tree Boosting System","url":"https://arxiv.org/abs/1603.02754"},{"title":"XGBoost: A Scalable Tree Boosting System Tianqi Chen University of Washington","url":"https://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://dl.acm.org/doi/10.1145/2939672.2939785"},{"title":"[PDF] XGBoost: A Scalable Tree Boosting System | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGBoost:-A-Scalable-Tree-Boosting-System-Chen-Guestrin/26bc9195c6343e4d7f434dd65b4ad67efe2be27a"},{"title":"Chen, T.Q. and Guestrin, C. (2016) Xgboost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3251268"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://www.kdd.org/kdd2016/subtopic/view/xgboost-a-scalable-tree-boosting-system"},{"title":"XGBoost: A Scalable Tree Boosting System. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2455604941b7fef3da9bdb4039a888f56/jakobgerst"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://bibbase.org/network/publication/chen-guestrin-xgboostascalabletreeboostingsystem-2016"},{"title":"XGBoost Paper | XGBoosting","url":"https://xgboosting.com/xgboost-paper/"}]

I found the paper you're looking for. Here's what the search results show:

The paper "XGBoost: A Scalable Tree Boosting System" was authored by Tianqi Chen and Carlos Guestrin and was presented at the Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining in San Francisco on August 13-17, 2016, pages 785-794.

The paper describes a scalable end-to-end tree boosting system called XGBoost, which is used widely by data scientists to achieve state-of-the-art results on many machine learning challenges.

The authors propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning, and provide insights on cache access patterns, data compression and sharding to build a scalable tree boosting system.

By combining these insights, XGBoost scales beyond billions of examples using far fewer resources than existing systems.

The paper is also available on arXiv (arXiv:1603.02754) and at the official KDD website, making it easily accessible for further reading.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "cd9ec96e-5165-4821-a46b-0dadd7c8f148"
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017A2ALzcMb5MySM7iRqKFVx`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" TMLR \"Transactions on Machine Learning Research\" publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "73164fc4-82c9-4360-8ce2-a0ac24f74a2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkGhQNrUCBZcMhQryYbTh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5948,
      "cache_read_input_tokens": 24216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5948,
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

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XscaZgMRQP3D8Kzfi5PJMx`</summary>

```json
{
  "query": "Pythia Biderman ICML 2023 full author list all authors",
  "allowed_domains": [
    "dblp.org",
    "proceedings.mlr.press",
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d51ae09b-b2c9-4fb1-b50f-7fa3208e2fda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkGhQNrUCBZcMhQryYbTh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5948,
      "cache_read_input_tokens": 24216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5948,
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

_source line 65_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGMWh8wy5zu3ogG7cc2tva`</summary>

```json
{
  "query": "Scott Aaronson \"Watermarking GPT Outputs\" talk date 2022 2023 Kirchner OpenAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9d9ea8d0-7ad4-4d49-a9fd-ab963536f9e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkGhQNrUCBZcMhQryYbTh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5948,
      "cache_read_input_tokens": 24216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5948,
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

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTGcKpVd1qy2WhM6VnqRwP`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan TMLR openreview accepted year",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "7154b09f-a9d7-45f8-96cf-4c1bc8f975fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkGhQNrUCBZcMhQryYbTh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5948,
      "cache_read_input_tokens": 24216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5948,
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

_source line 67 · 2026-05-16T00:00:17.357Z_

<details><summary>↩ Tool result · `toolu_017A2ALzcMb5MySM7iRqKFVx`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" TMLR "Transactions on Machine Learning Research" publication year"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"}]

Based on the search results, I found the paper "Can AI-Generated Text be Reliably Detected?" The paper appears to have been published in Transactions on Machine Learning Research (TMLR).

From the search results, the paper demonstrates that while recursive paraphrasing methods can significantly reduce detection rates, they only slightly degrade text quality in many cases, highlighting potential vulnerabilities in current detection systems.

The research shows that a recursive paraphrasing attack can break a whole range of detectors, including the ones using watermarking schemes as well as neural network-based detectors, zero-shot classifiers, and retrieval-based detectors. Additionally, the authors provide a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions, offering insights into the fundamental challenges of reliable detection as language models continue to advance.

Based on the OpenReview submission metadata, the TMLR publication appears to be from **October 2024**.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "5b380cec-d7ed-4b9c-b870-bb15287ba50d"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T00:00:17.531Z_

<details><summary>↩ Tool result · `toolu_01XscaZgMRQP3D8Kzfi5PJMx`</summary>

```text
Web search results for query: "Pythia Biderman ICML 2023 full author list all authors"

Links: [{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Purifying Large Language Models by Ensembling a Small Language Model","url":"https://arxiv.org/html/2402.14845"},{"title":"Transcoders Beat Sparse Autoencoders for Interpretability","url":"https://arxiv.org/html/2501.18823"},{"title":"A Lightweight Method to Disrupt Memorized Sequences in LLMs","url":"https://arxiv.org/pdf/2502.05159v1"},{"title":"Transformer Layers as Painters","url":"https://arxiv.org/pdf/2407.09298"},{"title":"Repeat After Me: Transformers are Better than State Space Models at Copying Transformers are Better than State Space Models at Copying","url":"https://arxiv.org/html/2402.01032"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://ar5iv.labs.arxiv.org/html/2304.01373"},{"title":"Benchmarking Mental State Representations in Language Models","url":"https://arxiv.org/html/2406.17513v1"}]

Based on the search results, the full author list for the Pythia paper presented at ICML 2023 is: Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, and Oskar van der Wal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9a917bf0-5c0a-4d2f-961b-bed2c2ad26d3"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-16T00:00:19.594Z_

<details><summary>↩ Tool result · `toolu_01FGMWh8wy5zu3ogG7cc2tva`</summary>

```text
Web search results for query: "Scott Aaronson "Watermarking GPT Outputs" talk date 2022 2023 Kirchner OpenAI"

Links: [{"title":"The Future of Computer Science","url":"https://www.scottaaronson.com/talks/watermark.ppt"},{"title":"Talks","url":"https://www.scottaaronson.com/talks/"},{"title":"Watermarking Needs Input Repetition Masking","url":"https://arxiv.org/html/2504.12229v1"},{"title":"OpenAI's attempts to watermark AI text hit limits | TechCrunch","url":"https://techcrunch.com/2022/12/10/openais-attempts-to-watermark-ai-text-hit-limits/"},{"title":"20 - ‘Reform’ AI Alignment with Scott Aaronson | AXRP - the AI X-risk Research Podcast","url":"https://axrp.net/episode/2023/04/11/episode-20-reform-ai-alignment-scott-aaronson.html"},{"title":"How The ChatGPT Watermark Works And Why It Could Be Defeated","url":"https://www.searchenginejournal.com/chatgpt-watermark/475366/"},{"title":"AXRP Episode 20 - 'Reform' AI Alignment with Scott ...","url":"https://www.lesswrong.com/posts/nsygJvidfgidmgKqX/axrp-episode-20-reform-ai-alignment-with-scott-aaronson"},{"title":"My AI Safety Lecture for UT Effective Altruism","url":"https://scottaaronson.blog/?p=6823"},{"title":"AXRP Episode 20 - ‘Reform’ AI Alignment with Scott Aaronson — AI Alignment Forum","url":"https://www.alignmentforum.org/posts/nsygJvidfgidmgKqX/axrp-episode-20-reform-ai-alignment-with-scott-aaronson"},{"title":"Watermarking of Large Language Models","url":"https://simons.berkeley.edu/talks/scott-aaronson-ut-austin-openai-2023-08-17"}]

Based on the search results, I found information about Scott Aaronson's "Watermarking GPT Outputs" talk:

The main talk on "Watermarking GPT Outputs" was given at OpenAI in San Francisco, CA on December 13, 2022. There were also other versions of this talk given at UT Austin Math Club on October 18, 2022, at UT Austin Effective Altruist Club on November 14, 2022, and at UT Austin ACM Chapter on February 8, 2023.

Additionally, a related talk on "Watermarking of Large Language Models" was given at the Workshop on Large Language Models and Transformers at Simons Institute, UC Berkeley on August 17, 2023.

Regarding Hendrik Kirchner mentioned in your query: OpenAI engineer Hendrik Kirchner built a working prototype of the watermarking tool, according to Aaronson.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "32e40782-06a0-4e97-9054-55461633702c"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T00:00:19.908Z_

<details><summary>↩ Tool result · `toolu_01LTGcKpVd1qy2WhM6VnqRwP`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan TMLR openreview accepted year"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://openreview.net/pdf/8f08d3bcd5c7f05ec65a87d802099dc7644cc11c.pdf"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf/4aea3388770b3a0f09e30cf27c5be1a0d9fa9fb3.pdf"},{"title":"Revision History for Can AI-Generated Text be Reliably...","url":"https://openreview.net/revisions?id=OOgsAZdFOt"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text ...","url":"https://openreview.net/notes/edits/attachment?id=MQxm4BolAs&name=pdf"},{"title":"Large Language Models can be Guided to Evade AI","url":"https://openreview.net/notes/edits/attachment?id=1ku4L33EOV&name=pdf"},{"title":"Under review as submission to TMLR","url":"https://openreview.net/pdf?id=pTuuuGQ1zl"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan and colleagues.

The paper addresses concerns about the misuse of large language models for plagiarism, fake news generation, and spamming, establishing that reliable detection of AI-generated text has become a critical area of research.

Regarding the publication status: The paper was submitted to TMLR (Transactions on Machine Learning Research), and the revised version was titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" based on the OpenReview forum dated October 20, 2024.

The paper's main contribution is that it demonstrates that AI text detectors are not reliable in practical scenarios, particularly by developing a recursive paraphrasing attack that can break a wide range of detectors including watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "150d12d7-3c0b-4273-9001-9ea82bc9d86d"
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01UwvkccnqM7ssqRjLX7HzEX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d5452e6a-1ea5-4c04-a13d-795c65dbe9ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZJcMgTGMoBqfgMZVXL5hv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 9176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6767,
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

_source line 72 · 2026-05-16T00:00:04.094Z_

<details><summary>↩ Tool result · `toolu_01UwvkccnqM7ssqRjLX7HzEX`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	}
140	
141	@inproceedings{strong_model_collapse,
142	  title = {{Strong Model Collapse}},
143	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
144	  booktitle = {Proceedings of the International Conference on Learning Representations},
145	  year = {2025},
146	}
147	
148	@inproceedings{model_collapse_avoidable,
149	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
150	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
151	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
152	  year = {2024},
153	}
154	
155	% ===== OOD Detection =====
156	
157	@inproceedings{ood_baseline,
158	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
159	  author = {Hendrycks, Dan and Gimpel, Kevin},
160	  booktitle = {Proceedings of the International Conference on Learning Representations},
161	  year = {2017},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{dsir,
167	  title = {{Data Selection for Language Models via Importance Resampling}},
168	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
169	  booktitle = {Advances in Neural Information Processing Systems},
170	  year = {2023},
171	}
172	
173	@inproceedings{qurating,
174	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
175	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
176	  booktitle = {Proceedings of the International Conference on Machine Learning},
177	  year = {2024},
178	}
179	
180	@inproceedings{ccnet,
181	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
182	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
183	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
184	  year = {2020},
185	}
186	
187	% ===== Watermarking =====
188	
189	@inproceedings{watermark_llm,
190	  title = {{A Watermark for Large Language Models}},
191	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
192	  booktitle = {Proceedings of the International Conference on Machine Learning},
193	  year = {2023},
194	}
195	
196	@article{synthid_text,
197	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
198	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
199	  journal = {Nature},
200	  volume = {634},
201	  pages = {818--823},
202	  year = {2024},
203	}
204	
205	@misc{aaronson_watermark,
206	  title = {{Watermarking GPT Outputs}},
207	  author = {Aaronson, Scott and Kirchner, Hendrik},
208	  year = {2022},
209	  howpublished = {Technical Talk},
210	  url = {https://scottaaronson.blog/?p=6823},
211	}
212	
213	@article{chainwash,
214	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
215	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
216	  journal = {arXiv preprint arXiv:2605.05503},
217	  year = {2026},
218	}
219	
220	% ===== Vocabulary Diversity =====
221	
222	@inproceedings{curious_decline,
223	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
224	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
225	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
226	  year = {2024},
227	}
228	
229	@inproceedings{writing_diversity,
230	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
231	  author = {Padmakumar, Vishakh and He, He},
232	  booktitle = {Proceedings of the International Conference on Learning Representations},
233	  year = {2024},
234	}
235	
236	@inproceedings{nucleus_sampling,
237	  title = {{The Curious Case of Neural Text Degeneration}},
238	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
239	  booktitle = {Proceedings of the International Conference on Learning Representations},
240	  year = {2020},
241	}
242	
243	@inproceedings{mapping_llm_science,
244	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
245	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
246	  booktitle = {Proceedings of the Conference on Language Modeling},
247	  year = {2024},
248	}
249	
250	@inproceedings{monitoring_ai_review,
251	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
252	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
253	  booktitle = {Proceedings of the International Conference on Machine Learning},
254	  year = {2024},
255	}
256	
257	% ===== Stylometry =====
258	
259	@article{stamatatos_survey,
260	  title = {{A Survey of Modern Authorship Attribution Methods}},
261	  author = {Stamatatos, Efstathios},
262	  journal = {Journal of the American Society for Information Science and Technology},
263	  year = {2009},
264	}
265	
266	@article{koppel_authorship,
267	  title = {{Computational Methods in Authorship Attribution}},
268	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
269	  journal = {Journal of the American Society for Information Science and Technology},
270	  year = {2009},
271	}
272	
273	@inproceedings{uchendu_attribution,
274	  title = {{Authorship Attribution for Neural Text Generation}},
275	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
276	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
277	  year = {2020},
278	}
279	
280	@inproceedings{munir_looking_glass,
281	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
282	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
283	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
284	  year = {2021},
285	}
286	
287	% ===== Iterative Generation =====
288	
289	@inproceedings{broken_telephone,
290	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
291	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
292	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
293	  year = {2025},
294	}
295	
296	@article{markovian_chains,
297	  title = {{Markovian Generation Chains in Large Language Models}},
298	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
299	  journal = {arXiv preprint arXiv:2603.11228},
300	  year = {2026},
301	}
302	
303	% ===== Membership Inference =====
304	
305	@inproceedings{min_k_percent,
306	  title = {{Detecting Pretraining Data from Large Language Models}},
307	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
308	  booktitle = {Proceedings of the International Conference on Learning Representations},
309	  year = {2024},
310	}
311	
312	% ===== Survey =====
313	
314	@article{wu_survey_2025,
315	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
316	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
317	  journal = {Computational Linguistics},
318	  publisher = {MIT Press},
319	  year = {2025},
320	}
321	
322	@inproceedings{jawahar_survey,
323	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
324	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
325	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
326	  year = {2020},
327	}
328	
329	% ===== Models =====
330	
331	@inproceedings{pythia,
332	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
333	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
334	  booktitle = {Proceedings of the International Conference on Machine Learning},
335	  year = {2023},
336	}
337	
338	@inproceedings{olmo,
339	  title = {{OLMo: Accelerating the Science of Language Models}},
340	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
341	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
342	  year = {2024},
343	}
344	
345	@article{qwen3,
346	  title = {{Qwen3 Technical Report}},
347	  author = {{Qwen Team}},
348	  journal = {arXiv preprint arXiv:2505.09388},
349	  year = {2025},
350	}
351	
352	% ===== Machine Learning =====
353	
354	@article{coral_ordinal,
355	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
356	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
357	  journal = {Pattern Recognition Letters},
358	  volume = {140},
359	  pages = {325--331},
360	  year = {2020},
361	}
362	
363	@inproceedings{frank_hall_ordinal,
364	  title = {{A Simple Approach to Ordinal Classification}},
365	  author = {Frank, Eibe and Hall, Mark},
366	  booktitle = {Proceedings of the European Conference on Machine Learning},
367	  year = {2001},
368	}
369	
370	@inproceedings{xgboost,
371	  title = {{XGBoost: A Scalable Tree Boosting System}},
372	  author = {Chen, Tianqi and Guestrin, Carlos},
373	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
374	  year = {2016},
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "6a5315d3-2528-4aad-b36c-9223a6dd6a60"
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012kCmFV2xPUh4GwdZ8ArX1J`</summary>

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
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "a16dd744-1eb4-4965-9f82-481571ac0700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZJcMgTGMoBqfgMZVXL5hv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 9176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6767,
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

_source line 74 · 2026-05-16T00:00:04.235Z_

<details><summary>↩ Tool result · `toolu_012kCmFV2xPUh4GwdZ8ArX1J`</summary>

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
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "320c1ec1-7a78-4f16-ad0a-af773154930a"
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016cPQkJaXmDg7CZoPhAyjcG`</summary>

```json
{
  "query": "Self-Consuming Generative Models Go MAD Alemohammad ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "521333f4-978a-401b-8f4e-ddb8b9600f2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014BTiYWAfkCyGa1F3MkQDB9`</summary>

```json
{
  "query": "Qwen3 Technical Report arXiv 2505.09388 author list 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f2b974be-cf7f-4a50-b2d4-31dbbe891bcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 77_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GQguxqa2kCfeevdCxEJ5L6`</summary>

```json
{
  "query": "DNA-GPT Divergent N-Gram Analysis Training-Free Detection GPT-Generated Text Yang ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f1a66f32-794f-40fb-8d33-5cbf7f78b286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 78_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KK7EKVmUWQLV1pYHai6okY`</summary>

```json
{
  "query": "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text Bao ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e66c1050-3631-4f9a-8699-af025d82fa33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 79_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XaEkQUnfgoLg9xfa56GTbK`</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "2b782919-cab8-4eda-b243-d71d1389b691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 80_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X6C7LSRG3io2ovEqRGYFJn`</summary>

```json
{
  "query": "\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples\" Hendrycks Gimpel ICLR 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "854f1f81-ed51-48a4-a1aa-32e0920cf6ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 81_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEnmFzaAFPjiZQa9p7qcrS`</summary>

```json
{
  "query": "CCNet Extracting High Quality Monolingual Datasets Web Crawl Data Wenzek LREC 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "3ac311f8-11dd-4a32-9302-4fe9ab1e4821",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175xpeBWSC7QQjYnDNBVVir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8532,
      "cache_read_input_tokens": 15943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8532,
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

_source line 82 · 2026-05-16T00:00:13.609Z_

<details><summary>↩ Tool result · `toolu_016cPQkJaXmDg7CZoPhAyjcG`</summary>

```text
Web search results for query: "Self-Consuming Generative Models Go MAD Alemohammad ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"Two Papers at ICLR 2024","url":"https://dsp.rice.edu/2024/03/16/two-papers-at-iclr/"}]

I found the paper! Here's what I can tell you about "Self-Consuming Generative Models Go MAD" by Alemohammad et al., presented at ICLR 2024:

## Overview

The paper addresses how advances in generative AI have led to the temptation to use AI-synthesized data to train next-generation models, creating an autophagous ("self-consuming") loop whose properties are poorly understood.

## Main Finding

The primary conclusion is that without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease. This condition is termed Model Autophagy Disorder (MAD), by analogy to mad cow disease.

## Key Results

The authors demonstrate that appreciable MADness can occur in only a handful of generations. Without sampling biases, MADness degrades quality and diversity, while with them, quality can be maintained but diversity degrades even faster.

## Scope

The authors conducted a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through the generations of training and whether the samples from previous-generation models have been biased to trade off data quality versus diversity. The concepts developed apply to any data type, including text.

The paper was published at ICLR 2024 in Vienna in May 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9d361c84-7377-4bec-84db-f04a5a38557e"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-16T00:00:15.750Z_

<details><summary>↩ Tool result · `toolu_01XaEkQUnfgoLg9xfa56GTbK`</summary>

```text
Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen TMLR publication year"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=12550&show=25"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3550&show=50"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.researchgate.net/publication/395771470_Diversity_Boosts_AI-Generated_Text_Detection"}]

Based on the search results, I can provide you with the information about the publication:

"Diversity Boosts AI-Generated Text Detection" was accepted to TMLR '26, making the **publication year 2026**.

The paper is authored by Advik Raj Basani and Pin-Yu Chen. The research describes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "037770d8-f5f8-4cd9-a7d4-b3afed65c567"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T00:00:15.896Z_

<details><summary>↩ Tool result · `toolu_01GQguxqa2kCfeevdCxEJ5L6`</summary>

```text
Web search results for query: "DNA-GPT Divergent N-Gram Analysis Training-Free Detection GPT-Generated Text Yang ICLR 2024"

Links: [{"title":"ICLR Poster DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://iclr.cc/virtual/2024/poster/18444"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"UC Santa Barbara UC Santa Barbara Electronic Theses and Dissertations Title","url":"https://escholarship.org/content/qt2g10w3nh/qt2g10w3nh.pdf"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT/DNA-GPT-dist.py at main · Xianjun-Yang/DNA-GPT","url":"https://github.com/Xianjun-Yang/DNA-GPT/blob/main/DNA-GPT-dist.py"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"GitHub - Xianjun-Yang/DNA-GPT: Offiical codes for DNA-GPT (ICLR 2024) · GitHub","url":"https://github.com/xianjun-yang/dna-gpt"}]

I found comprehensive information about the DNA-GPT paper. Here's what I found:

## DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text

DNA-GPT is authored by Xianjun Yang, Wei Cheng, Yue Wu, Linda Ruth Petzold, William Yang Wang, and Haifeng Chen, and was published at ICLR 2024.

### Overview

The paper addresses the challenge of detecting GPT-generated text, as current research on detection methods lags behind the rapid evolution of LLMs, and conventional training-based methods have limitations in flexibility and lack explanatory power.

### Method

The authors propose Divergent N-Gram Analysis (DNA-GPT), a novel training-free detection strategy. Given a text, they truncate it in the middle and use only the preceding portion as input to LLMs to regenerate the remaining parts. By analyzing differences between the original and new remaining parts through N-gram analysis in black-box or probability divergence in white-box settings, they illustrate significant discrepancies between machine-generated and human-written text.

### Results

The authors conducted extensive experiments on advanced LLMs from OpenAI (text-davinci-003, GPT-3.5-turbo, and GPT-4) as well as open-source models (GPT-NeoX-20B and LLaMa-13B), and their zero-shot approach exhibits state-of-the-art performance in distinguishing between human and GPT-generated text on four English and one German dataset, outperforming OpenAI's own classifier.

Additionally, the method provides reasonable explanations and evidence to support claims (explainable detection), and is also robust under revised text attacks and can solve model sourcing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9286341b-e9ff-4d18-a31d-f993e7d104b1"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-16T00:00:16.232Z_

<details><summary>↩ Tool result · `toolu_01KK7EKVmUWQLV1pYHai6okY`</summary>

```text
Web search results for query: "Fast-DetectGPT Efficient Zero-Shot Detection Machine-Generated Text Bao ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"fast-detectgpt: efficient zero-shot detec","url":"https://arxiv.org/pdf/2310.05130"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"Releases · baoguangsheng/fast-detect-gpt","url":"https://github.com/baoguangsheng/fast-detect-gpt/releases"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text - IEEE Computational Intelligence Society (CIS) Shenzhen Chapter","url":"https://r10.ieee.org/shenzhen-cis/blog/2024/04/25/fast-detectgpt-efficient-zero-shot-detection-of-machine-generated-text/"}]

Here are the search results for "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" by Bao et al., published at ICLR 2024:

## Overview

The paper is authored by Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang and was presented as a 2024 Poster at ICLR.

## Core Contribution

The paper introduces the concept of conditional probability curvature to elucidate discrepancies in word choices between LLMs and humans within a given context, and presents Fast-DetectGPT as an optimized zero-shot detector which substitutes DetectGPT's perturbation step with a more efficient sampling step.

## Performance Results

Fast-DetectGPT surpasses DetectGPT by a relative around 75% in both the white-box and black-box settings and accelerates the detection process by a factor of 340.

## Key Resources

- The code is available on GitHub for the ICLR 2024 paper
- The paper has been published in the ICLR 2024 proceedings
- A demo is available online at https://fastdetect.net

The paper addresses the computational inefficiency of DetectGPT by proposing a more efficient alternative that maintains or improves detection accuracy while dramatically reducing computation time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "51cba793-5308-4d8b-b4f4-e7dbfd0fd42a"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T00:00:16.347Z_

<details><summary>↩ Tool result · `toolu_014BTiYWAfkCyGa1F3MkQDB9`</summary>

```text
Web search results for query: "Qwen3 Technical Report arXiv 2505.09388 author list 2025"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"Qwen3 Technical Report | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.09388"},{"title":"Qwen/Qwen3-VL-8B-Thinking - Demo - DeepInfra","url":"https://deepinfra.com/Qwen/Qwen3-VL-8B-Thinking"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"}]

Based on the search results, here is the complete author list for the Qwen3 Technical Report (arXiv 2505.09388):

The paper has 60 authors total: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu.

The paper was submitted on May 14, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d885c987-9b05-4353-a5c1-a4f2a7e9bf13"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-16T00:00:16.406Z_

<details><summary>↩ Tool result · `toolu_01X6C7LSRG3io2ovEqRGYFJn`</summary>

```text
Web search results for query: ""A Baseline for Detecting Misclassified and Out-of-Distribution Examples" Hendrycks Gimpel ICLR 2017"

Links: [{"title":"[1610.02136] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks","url":"https://arxiv.org/abs/1610.02136"},{"title":"GitHub - hendrycks/error-detection: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks · GitHub","url":"https://github.com/hendrycks/error-detection"},{"title":"A BASELINE FOR DETECTING MISCLASSIFIED AND OUT-OF-DISTRIBUTION EXAMPLES IN NEURAL NETWORKS | 따라쟁이의 인공지능 블로그","url":"https://khw11044.github.io/blog/papers/paper-etc/2021-04-01-BaselineMisclassifiedandOOD/"},{"title":"[PDF] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Baseline-for-Detecting-Misclassified-and-Examples-Hendrycks-Gimpel/6ff2a434578ff2746b9283e45abf296887f48a2d"},{"title":"dblp: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks.","url":"https://dblp.org/rec/conf/iclr/HendrycksG17.html"},{"title":"A Baseline for Detecting Misclassified and Out-of- ...","url":"https://arxiv.org/pdf/1610.02136"},{"title":"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks | OpenReview","url":"https://openreview.net/forum?id=Hkg4TI9xl"},{"title":"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/c198223714bea8d959e26861ff07dd8d"},{"title":"[1610.02136v3] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks","url":"https://arxiv.org/abs/1610.02136v3"},{"title":"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2016arXiv161002136H/abstract"}]

I found the paper you're looking for! Here are the key details:

**Title:** A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

**Authors:** Dan Hendrycks and Kevin Gimpel

**Publication:** Proceedings of International Conference on Learning Representations (ICLR), 2017

**Main Contribution:** The paper presents a simple baseline that utilizes probabilities from softmax distributions. Correctly classified examples tend to have greater maximum softmax probabilities than erroneously classified and out-of-distribution examples, allowing for their detection.

**Scope:** The authors assess performance by defining several tasks in computer vision, natural language processing, and automatic speech recognition, showing the effectiveness of this baseline across all.

The paper is available on arXiv (1610.02136) and at the OpenReview platform. There's also an official GitHub repository (hendrycks/error-detection) with code related to the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "19a4d657-c29c-495c-b171-d4e4bf76bbfe"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T00:00:18.450Z_

<details><summary>↩ Tool result · `toolu_01KEnmFzaAFPjiZQa9p7qcrS`</summary>

```text
Web search results for query: "CCNet Extracting High Quality Monolingual Datasets Web Crawl Data Wenzek LREC 2020"

Links: [{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://aclanthology.org/2020.lrec-1.494/"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"https://aclanthology.org/2020.lrec-1.494.pdf"},{"title":"[1911.00359] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://arxiv.org/abs/1911.00359"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.494.pdf"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://arne.chark.eu/anthology/2020.lrec-1.494/"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/245540f9667239913db153792be9fff73/dblp"},{"title":"Papers with Code - CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://paperswithcode.com/paper/ccnet-extracting-high-quality-monolingual"},{"title":"GitHub - facebookresearch/cc_net: Tools to download and cleanup Common Crawl data","url":"https://github.com/facebookresearch/cc_net"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://www.researchgate.net/publication/337005596_CCNet_Extracting_High_Quality_Monolingual_Datasets_from_Web_Crawl_Data"},{"title":"@inproceedings{wenzek-etal-2020-ccnet,","url":"https://aclanthology.org/2020.lrec-1.494.bib"}]

I found the paper you're looking for! Here's what I found:

## CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data

The paper was authored by Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Joulin, and Edouard Grave, and was published at LREC 2020.

### Overview

The paper describes an automatic pipeline to extract massive high-quality monolingual datasets from Common Crawl for a variety of languages. The pipeline follows the data processing introduced in fastText that deduplicates documents and identifies their language, and augments this with a filtering step to select documents that are close to high quality corpora like Wikipedia.

### Publication Details

The paper appears in the Proceedings of the Twelfth Language Resources and Evaluation Conference, pages 4003–4012, held in Marseille, France.

The paper is available at the ACL Anthology (https://aclanthology.org/2020.lrec-1.494/) and there's also an associated GitHub repository with implementation tools: https://github.com/facebookresearch/cc_net


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "fc2f8fd9-05ce-4d0d-8518-82f6542190b3"
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Agent · `toolu_01CdrqHc4AbBgAzr45qMtpJW`</summary>

```json
{
  "description": "Verify batch 3: 2024-2026 recent papers",
  "prompt": "I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.\n\n1. **binoculars** — \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024\n\n2. **ld_score** — \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026\n\n3. **generator_barrier** — \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026\n\n4. **feat_aug_transformer** — \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026\n\n5. **chainwash** — \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026\n\n6. **markovian_chains** — \"Markovian Generation Chains in Large Language Models\", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026\n\n7. **broken_telephone** — \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025\n\n8. **beyond_binary** — \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025\n\n9. **semeval2024_task8** — \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024\n\n10. **wu_survey_2025** — \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025\n\n11. **reliable_detection** — \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?\n\nReport all findings precisely.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1c63f942-1f72-4461-b78e-61dcc3b8b681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13517
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

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Verify batch 3: 2024-2026 recent papers",
  "task_type": "local_agent",
  "prompt": "I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.\n\n1. **binoculars** — \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024\n\n2. **ld_score** — \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026\n\n3. **generator_barrier** — \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026\n\n4. **feat_aug_transformer** — \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026\n\n5. **chainwash** — \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026\n\n6. **markovian_chains** — \"Markovian Generation Chains in Large Language Models\", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026\n\n7. **broken_telephone** — \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025\n\n8. **beyond_binary** — \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025\n\n9. **semeval2024_task8** — \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024\n\n10. **wu_survey_2025** — \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025\n\n11. **reliable_detection** — \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?\n\nReport all findings precisely.",
  "uuid": "1dd6601b-e68b-4ab6-842c-7524bf7f1fa9",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

## Round 3

133 recorded events

### User

_source line 91 · 2026-05-16T00:00:22.711Z_

I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.

1. **binoculars** — "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024

2. **ld_score** — "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026

3. **generator_barrier** — "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026

4. **feat_aug_transformer** — "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026

5. **chainwash** — "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026

6. **markovian_chains** — "Markovian Generation Chains in Large Language Models", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026

7. **broken_telephone** — "LLM as a Broken Telephone: Iterative Generation Distorts Information", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025

8. **beyond_binary** — "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025

9. **semeval2024_task8** — "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024

10. **wu_survey_2025** — "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025

11. **reliable_detection** — "Can AI-Generated Text be Reliably Detected?", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?

Report all findings precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "b660d8be-03d4-43cd-a2e4-062b8931cd76"
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
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Does Writing with Language Models Reduce Content…",
  "usage": {
    "total_tokens": 31692,
    "tool_uses": 10,
    "duration_ms": 25379
  },
  "last_tool_name": "WebSearch",
  "uuid": "6d6be590-7b15-4f6e-bf5b-561c05c24b89",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gjb7Sv1yiaSCbc1tMb1son`</summary>

```json
{
  "query": "\"Does Writing with Language Models Reduce Content Diversity\" Padmakumar He ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "acb591a6-ea82-4bff-b27a-b3b552297057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"The Curious Case of Neural Text Degeneration\" Ho…",
  "usage": {
    "total_tokens": 31693,
    "tool_uses": 11,
    "duration_ms": 26478
  },
  "last_tool_name": "WebSearch",
  "uuid": "cac0cfdf-b812-422d-94ce-7edbd427a314",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WRm2TShK94cBQ747bsC2Pv`</summary>

```json
{
  "query": "\"The Curious Case of Neural Text Degeneration\" Holtzman ICLR 2020 nucleus sampling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f3970ac4-2105-4ff0-8ba4-26da0b6c9096",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for site:openreview.net \"Can AI-Generated Text be Rel…",
  "usage": {
    "total_tokens": 33677,
    "tool_uses": 14,
    "duration_ms": 41897
  },
  "last_tool_name": "WebSearch",
  "uuid": "e438db13-af6a-4319-8d34-029be481a79c",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0174pGZNozKZwQvJzS5Zruio`</summary>

```json
{
  "query": "site:openreview.net \"Can AI-Generated Text be Reliably Detected\" \"Stress Testing\" OOgsAZdFOt accepted 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1b09f0db-301d-44eb-8591-dfaee1ab203b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4vyphE6bipFZkL9vQLuqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3439,
      "cache_read_input_tokens": 30164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3439,
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

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Detecting Pretraining Data from Large Language M…",
  "usage": {
    "total_tokens": 31694,
    "tool_uses": 12,
    "duration_ms": 27301
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd429949-f4c5-442c-a40e-9483042a047c",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KcpV2nPqkQVbR18kNjTCJ`</summary>

```json
{
  "query": "\"Detecting Pretraining Data from Large Language Models\" Shi Min-K% ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "b681e1ae-ea4d-40b1-9b3c-fad4ffa7a19e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for site:dblp.org Pythia Biderman Schoelkopf \"Quentin…",
  "usage": {
    "total_tokens": 33680,
    "tool_uses": 15,
    "duration_ms": 42844
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2154705-13f4-4d5f-9fb2-8e827836bfa4",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J1qVG6cKPkPTDRs54F1RvP`</summary>

```json
{
  "query": "site:dblp.org Pythia Biderman Schoelkopf \"Quentin\" Anthony ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "b61b9b2e-92c5-4d06-bed8-e59c79dffc4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4vyphE6bipFZkL9vQLuqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3439,
      "cache_read_input_tokens": 30164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3439,
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

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"A Survey of Modern Authorship Attribution Method…",
  "usage": {
    "total_tokens": 31695,
    "tool_uses": 13,
    "duration_ms": 28296
  },
  "last_tool_name": "WebSearch",
  "uuid": "ad1b41a7-fe59-46fb-9608-cc17ee47f928",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017iiebKoiUprcx3pCG732E4`</summary>

```json
{
  "query": "\"A Survey of Modern Authorship Attribution Methods\" Stamatatos JASIST 2009 publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "79a8dc86-11a2-447a-b890-e0553fbef2a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"reliable_detection\" OR \"reliably detected\" Sadas…",
  "usage": {
    "total_tokens": 33683,
    "tool_uses": 16,
    "duration_ms": 43634
  },
  "last_tool_name": "WebSearch",
  "uuid": "afedbd16-1ad9-4771-9f13-0ac8c193c028",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lb5pX1v6BT4PFDki9tAQ7T`</summary>

```json
{
  "query": "\"reliable_detection\" OR \"reliably detected\" Sadasivan TMLR 2024 accepted October",
  "allowed_domains": [
    "openreview.net",
    "jmlr.org",
    "tmlr.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "fad75a9f-5261-4206-917f-01f397487f1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4vyphE6bipFZkL9vQLuqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3439,
      "cache_read_input_tokens": 30164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3439,
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

### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Computational Methods in Authorship Attribution\"…",
  "usage": {
    "total_tokens": 31696,
    "tool_uses": 14,
    "duration_ms": 29296
  },
  "last_tool_name": "WebSearch",
  "uuid": "b3406d13-03b8-4ca8-91f7-bd264e5fb745",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015VYy4y9TLPKWCCRjA7tywx`</summary>

```json
{
  "query": "\"Computational Methods in Authorship Attribution\" Koppel Schler Argamon JASIST 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "6ddbbcee-fc39-42d1-b897-b41ebdd93bfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Verify batch 3: 2024-2026 recent papers",
  "usage": {
    "total_tokens": 16071,
    "tool_uses": 1,
    "duration_ms": 6560
  },
  "last_tool_name": "ToolSearch",
  "uuid": "aa6f304c-4fd6-43fe-8966-83a80723093d",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A4jizzRJyeQkZZFHQHjCcQ`</summary>

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
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "af04aa1d-3aef-47e9-a0e3-1fdaaf7a9c63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SB1okvqZpWGdXjLsNF8ma9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6878,
      "cache_read_input_tokens": 9176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6878,
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

_source line 110 · 2026-05-16T00:00:29.274Z_

<details><summary>↩ Tool result · `toolu_01A4jizzRJyeQkZZFHQHjCcQ`</summary>

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
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "24555322-170d-4400-9c8d-bdda08699241"
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-16T00:00:29.369Z_

<details><summary>↩ Tool result · `toolu_01Gjb7Sv1yiaSCbc1tMb1son`</summary>

```text
Web search results for query: ""Does Writing with Language Models Reduce Content Diversity" Padmakumar He ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"Does Writing with Language Models Reduce Content Diversity? | OpenReview","url":"https://openreview.net/forum?id=Feiz5HtCD0"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE ...","url":"https://openreview.net/pdf?id=Feiz5HtCD0"},{"title":"Does Writing With Language Models (LLMs) Reduce Content Diversity?","url":"https://iclr.cc/media/iclr-2024/Slides/19056.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Does-Writing-with-Language-Models-Reduce-Content-Padmakumar-He/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"ICLR Poster Does Writing with Language Models Reduce Content Diversity?","url":"https://iclr.cc/virtual/2024/poster/19056"}]

Based on the search results, I found detailed information about this paper:

## Paper Overview

"Does Writing with Language Models Reduce Content Diversity?" was presented by Vishakh Padmakumar and He He at ICLR 2024 in Vienna, Austria.

## Research Question and Methodology

The paper addresses concerns that as different users incorporate suggestions from the same LLM, there is a risk of decreased diversity in produced content, potentially limiting diverse perspectives in public discourse. The researchers measured the impact of co-writing on diversity via a controlled experiment where users wrote argumentative essays in three setups: using a base LLM (GPT3), a feedback-tuned LLM (InstructGPT), and writing without model help.

## Key Findings

Writing with InstructGPT (but not GPT3) resulted in a statistically significant reduction in diversity, increasing similarity between different authors' writings and reducing overall lexical and content diversity. The effect was mainly attributable to InstructGPT contributing less diverse text to co-written essays.

The findings suggest that the recent improvement in generation quality from adapting models to human feedback might come at the cost of more homogeneous and less diverse content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "dcb282d5-95d5-46d2-a5af-9e0fd611e6d8"
}
```

</details>

---

### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Strong Model Collapse\" Dohmatob Feng Subramonian…",
  "usage": {
    "total_tokens": 31697,
    "tool_uses": 15,
    "duration_ms": 29921
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd707eff-80c0-4c41-861a-cc66f9d5e4b5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015pcvzKtbyj6EvT7NyDdqTE`</summary>

```json
{
  "query": "\"Strong Model Collapse\" Dohmatob Feng Subramonian Kempe ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "6f758ad5-f22e-4c2a-bd74-47c330e3916d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTx7ManCZ4ZzVvoD4Msv5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

_source line 114 · 2026-05-16T00:00:31.076Z_

<details><summary>↩ Tool result · `toolu_017iiebKoiUprcx3pCG732E4`</summary>

```text
Web search results for query: ""A Survey of Modern Authorship Attribution Methods" Stamatatos JASIST 2009 publication year"

Links: [{"title":"A survey of modern authorship attribution methods - Stamatatos - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21001"},{"title":"A survey of modern authorship attribution methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-survey-of-modern-authorship-attribution-methods-Stamatatos/d25c27c7a3e9f41f150e8eadbad34c1c05d67510"},{"title":"A Survey of Modern Authorship Attribution Methods | Request PDF","url":"https://www.researchgate.net/publication/220435062_A_Survey_of_Modern_Authorship_Attribution_Methods"},{"title":"(PDF) A survey of modern authorship attribution methods (2009) | Efstathios Stamatatos | 1366 Citations","url":"https://scispace.com/papers/a-survey-of-modern-authorship-attribution-methods-2lb4q2gu7n"},{"title":"dblp: A survey of modern authorship attribution methods.","url":"https://dblp.org/rec/journals/jasis/Stamatatos09.html"},{"title":"A survey of modern authorship attribution methods - researchr publication","url":"https://researchr.org/publication/Stamatatos09"},{"title":"A survey of modern authorship attribution methods","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i3p538-556.html"},{"title":"EconPapers: A survey of modern authorship attribution methods","url":"https://econpapers.repec.org/RePEc:bla:jamist:v:60:y:2009:i:3:p:538-556"},{"title":"A survey of modern authorship attribution methods. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/19b36b85e07a64fd5295da2a2ad9a9efb"},{"title":"A survey of modern authorship attribution methods - R Discovery","url":"https://discovery.researcher.life/article/a-survey-of-modern-authorship-attribution-methods/ada3ad7940fd311b8498aa1f09bcf48c"}]

Based on the search results, the publication is "A survey of modern authorship attribution methods" by Stamatatos, published in JASIS (Journal of the American Society for Information Science and Technology), volume 60, issue 3, pages 538-556, in 2009.

To confirm the publication year: the article was published in 2009.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ab2ea918-21a7-4581-b5e9-e59624c57256"
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-16T00:00:32.231Z_

<details><summary>↩ Tool result · `toolu_01J1qVG6cKPkPTDRs54F1RvP`</summary>

```text
Web search results for query: "site:dblp.org Pythia Biderman Schoelkopf "Quentin" Anthony ICML 2023"

Links: [{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a.html"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"GitHub - EleutherAI/pythia: The hub for EleutherAI's work on interpretability and learning dynamics · GitHub","url":"https://github.com/eleutherai/pythia"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Stella+Biderman%2C+Hailey+Schoelkopf%2C+Quentin+Gregory+Anthony%2C+Herbie+Bradley%2C+Kyle+O%27Brien%2C+Eric+Hallahan%2C+Mohammad+Aflah+Khan%2C+Shivanshu+Purohit%2C+USVSN+Sai+Prashanth%2C+Edward+Raff%2C+et+al.+2023.+Pythia%3A+A+suite+for+analyzing+large+language+models+across+training+and+scaling.+In+International+Conference+on+Machine+Learning.+PMLR%2C+2397--2430."},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Stella+Biderman,+Hailey+Schoelkopf,+Quentin+Gregory+Anthony,+Herbie+Bradley,+Kyle+O%E2%80%99Brien,+Eric+Hallahan,+Mohammad+Aflah+Khan,+Shivanshu+Purohit,+USVSN+Sai+Prashanth,+Edward+Raff,+et+al.+Pythia:+A+suite+for+analyzing+large+language+models+across+training+and+scaling.+In+International+Conference+on+Machine+Learning,+pages+2397%E2%80%932430.+PMLR,+2023."},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling [Quick Review]","url":"https://liner.com/review/pythia-suite-for-analyzing-large-language-models-across-training-and"},{"title":"Pythia | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3618510"},{"title":"[2304.01373v1] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373v1"},{"title":"Repository-level code completion with adaptive segmentation and fused retrieval | Empirical Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10664-025-10762-7"}]

Based on the search results, I found the paper you were looking for. The paper "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling" was authored by Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, Usvsn Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, and Oskar Van Der Wal, and was published in the Proceedings of the 40th International Conference on Machine Learning (ICML) in 2023.

The paper is available on DBLP at https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html and was also published in the PMLR proceedings at https://proceedings.mlr.press/v202/biderman23a.html.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "212739a9-6fe8-4e1c-809c-a7b00b8a07e9"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-16T00:00:32.737Z_

<details><summary>↩ Tool result · `toolu_01WRm2TShK94cBQ747bsC2Pv`</summary>

```text
Web search results for query: ""The Curious Case of Neural Text Degeneration" Holtzman ICLR 2020 nucleus sampling"

Links: [{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"The Curious Case of Neural Text Degeneration | OpenReview","url":"https://openreview.net/forum?id=rygGQyrFvH"},{"title":"ICLR: The Curious Case of Neural Text Degeneration","url":"https://iclr.cc/virtual_2020/poster_rygGQyrFvH.html"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://www.researchgate.net/publication/332590110_The_Curious_Case_of_Neural_Text_Degeneration"},{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://hyunyoung2.github.io/2020/06/04/The_Curious_Case_of_Neural_Text_Degeneration/"},{"title":"(PDF) The Curious Case of Neural Text Degeneration (2020) | Ari Holtzman | 689 Citations","url":"https://scispace.com/papers/the-curious-case-of-neural-text-degeneration-2xplgl0dw1"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"}]

I've found comprehensive information about "The Curious Case of Neural Text Degeneration" paper. Here's a summary:

## Paper Overview

The paper was published by Holtzman, Ari, Buys, Jan, Du, Li, Forbes, Maxwell, and Choi, Yejin at the International Conference on Learning Representations (ICLR) in 2020.

## Main Problem

The paper identifies a counter-intuitive problem: even though the use of likelihood as training objective leads to high quality models for a broad range of language understanding tasks, using likelihood as a decoding objective leads to text that is bland and strangely repetitive.

## Key Findings

The paper reveals surprising distributional differences between human text and machine text, and finds that decoding strategies alone can dramatically affect the quality of machine text, even when generated from exactly the same neural language model.

## Nucleus Sampling Solution

The authors propose Nucleus Sampling, which works by sampling text from the dynamic nucleus of the probability distribution, allowing for diversity while effectively truncating the less reliable tail of the distribution, resulting in text that better demonstrates the quality of human text, yielding enhanced diversity without sacrificing fluency and coherence.

The key intuition is that the vast majority of probability mass at each time step is concentrated in the nucleus—a small subset of the vocabulary ranging between one and a thousand candidates. Rather than relying on a fixed top-k or temperature parameter, they propose sampling from the top-p portion of the probability mass, expanding and contracting the candidate pool dynamically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "4fd70b95-37f7-41c0-b8af-31f43a6332db"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-16T00:00:33.662Z_

<details><summary>↩ Tool result · `toolu_0174pGZNozKZwQvJzS5Zruio`</summary>

```text
Web search results for query: "site:openreview.net "Can AI-Generated Text be Reliably Detected" "Stress Testing" OOgsAZdFOt accepted 2024 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Revision History for Can AI-Generated Text be Reliably...","url":"https://openreview.net/revisions?id=OOgsAZdFOt"},{"title":"EDITLENS: QUANTIFYING THE EXTENT OF AI EDIT","url":"https://openreview.net/pdf?id=gOkitaPCfZ"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | OpenReview","url":"https://openreview.net/forum?id=WbFhFvjjKj"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=AXtFeYjboj"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets with","url":"https://openreview.net/pdf?id=WDhwO4Hhq2"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"}]

I found the paper you were looking for on OpenReview. The paper addresses concerns about misuse of large language models in activities such as plagiarism, fake news generation, and spamming, with a focus on the reliable detection of AI-generated text.

The paper with ID OOgsAZdFOt is titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors" and introduces a recursive paraphrasing attack to stress test a wide range of detection schemes, including watermarking, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

The experiments conducted on passages of approximately 300 tokens long reveal varying sensitivities of these detectors to the attacks, with paraphrasing attacks adding slight degradation to text quality, and the authors analyzing trade-offs between attack strength and resulting text quality through human studies, perplexity scores, and accuracy on text benchmarks.

You can access the full paper and forum discussion at: https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "12746e3a-0606-4ca9-bfc0-c6591e808ada"
}
```

</details>

---

### System

_source line 118_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for Spotting LLMs With Binoculars Zero-Shot Detection…",
  "usage": {
    "total_tokens": 17532,
    "tool_uses": 2,
    "duration_ms": 11800
  },
  "last_tool_name": "WebSearch",
  "uuid": "a3b74cfe-a8c3-4165-83e3-a670db03e452",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NwaMLRF9sMGckUpma83HPf`</summary>

```json
{
  "query": "Spotting LLMs With Binoculars Zero-Shot Detection Machine-Generated Text Hans Schwarzschild ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "b15389dc-187c-46d1-a251-38b884f7997d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GmP2tnuRwpNmzM6hvev3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 120 · 2026-05-16T00:00:34.540Z_

<details><summary>↩ Tool result · `toolu_015VYy4y9TLPKWCCRjA7tywx`</summary>

```text
Web search results for query: ""Computational Methods in Authorship Attribution" Koppel Schler Argamon JASIST 2009"

Links: [{"title":"Computational methods in authorship attribution - Koppel - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"},{"title":"Computational methods in authorship attribution","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i1p9-26.html"},{"title":"(PDF) Computational Methods in Authorship Attribution","url":"https://www.researchgate.net/publication/220433607_Computational_Methods_in_Authorship_Attribution"},{"title":"Computational methods in authorship attribution - Semantic Scholar","url":"https://www.semanticscholar.org/paper/Computational-methods-in-authorship-attribution-Koppel-Schler/c4550ee1f3a1a08c9d2f89e13a7dec7c220c1704"},{"title":"\"Computational Methods in Authorship Attribution\" by Moshe Koppel, Jonathan Schler et al.","url":"https://touroscholar.touro.edu/president_pubs/275/"},{"title":"Publications (Chronological) - Prof. Moshe Koppel","url":"https://u.cs.biu.ac.il/~koppel/Publications.html"},{"title":"Computational methods in authorship attribution | Journal of the American Society for Information Science and Technology","url":"https://dl.acm.org/citation.cfm?id=1484627"},{"title":"1 Computational Methods in Authorship Attribution","url":"https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf"},{"title":"Computational methods in authorship attribution - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/computational-methods-in-authorship-attribution-4/"},{"title":"Survey of Methods in Computational Literary Studies - 5 What is Authorship Attribution?","url":"https://methods.clsinfra.io/what-author.html"}]

I found the paper you're looking for. The article "Computational Methods in Authorship Attribution" by Moshe Koppel, Jonathan Schler, and Shlomo Argamon was published in the Journal of the American Society for Information Science and Technology, volume 60(1), pages 9-26, in January 2009.

The paper notes that "Statistical authorship attribution has a long history, culminating in the use of modern machine learning classification methods. Nevertheless, most of this work suffers from the limitation of assuming a small closed set of candidate authors and essentially unlimited training text for each."

The paper addresses three important variants of the authorship attribution problem: the profiling problem (where there is no candidate set), the needle-in-a-haystack problem (where there are many thousands of candidates with limited writing samples), and the verification problem (where there is one suspect to verify).

According to Semantic Scholar, this paper has 783 citations, making it a highly influential work in the field of computational authorship attribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e518125f-388d-49dc-8ec1-cf84ff4989ff"
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-16T00:00:34.684Z_

<details><summary>↩ Tool result · `toolu_019KcpV2nPqkQVbR18kNjTCJ`</summary>

```text
Web search results for query: ""Detecting Pretraining Data from Large Language Models" Shi Min-K% ICLR 2024"

Links: [{"title":"Detecting Pretraining Data from Large Language Models | OpenReview","url":"https://openreview.net/forum?id=zWqr3MQuNs"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LAN","url":"https://openreview.net/pdf?id=zWqr3MQuNs"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"ICLR Poster Detecting Pretraining Data from Large Language Models","url":"https://iclr.cc/virtual/2024/poster/17381"},{"title":"Detecting Pretraining Data from Large Language Models [Quick Review]","url":"https://liner.com/review/detecting-pretraining-data-from-large-language-models"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"Pretraining Data Detection for Large Language Models","url":"https://aclanthology.org/2024.emnlp-main.300.pdf"},{"title":"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models","url":"https://arxiv.org/html/2404.02936v1"}]

I found comprehensive information about this paper. Here's what I found:

## Paper Overview

The paper "Detecting Pretraining Data from Large Language Models" by Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer was presented at ICLR 2024 in Vienna, Austria.

## Main Contribution

The paper studies the pretraining data detection problem: given a piece of text and black-box access to an LLM without knowing the pretraining data, can we determine if the model was trained on the provided text?

## Key Components

The paper introduces two main contributions:

1. **WIKIMIA Benchmark**: A dynamic benchmark that uses data created before and after model training to support gold truth detection.

2. **MIN-K% PROB Detection Method**: Based on a simple hypothesis: an unseen example is likely to contain a few outlier words with low probabilities under the LLM, while a seen example is less likely to have words with such low probabilities.

## Key Advantages

MIN-K% PROB can be applied without any knowledge about the pretraining corpus or any additional training, departing from previous detection methods that require training a reference model on data that is similar to the pretraining data.

## Results and Applications

MIN-K% PROB achieves a 7.4% improvement on WIKIMIA over previous methods. The method is applied to copyrighted book detection and contaminated downstream example detection, showing to be a consistently effective solution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "5c3574d7-75c4-4a8b-ac5d-58a9ba71a35b"
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-16T00:00:35.788Z_

<details><summary>↩ Tool result · `toolu_015pcvzKtbyj6EvT7NyDdqTE`</summary>

```text
Web search results for query: ""Strong Model Collapse" Dohmatob Feng Subramonian Kempe ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"}]

I found the paper! Here are the key details about "Strong Model Collapse" by Dohmatob, Feng, Subramonian, and Kempe:

## Overview

The paper considers a supervised regression setting within the scaling laws paradigm and establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus.

## Main Findings

The results show that even the smallest fraction of synthetic data (e.g., as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance.

## Key Investigation

The authors investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse. In a simplified regime where neural networks are approximated via random projections of tunable size, they both theoretically and empirically show that larger models can amplify model collapse.

## Publication Status

The paper was published as an ICLR 2025 Spotlight presentation. The paper is available at the ICLR 2025 proceedings and has also been posted on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "cc54708e-36bc-4be7-8eda-f626603cb5b5"
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-16T00:00:37.662Z_

<details><summary>↩ Tool result · `toolu_01Lb5pX1v6BT4PFDki9tAQ7T`</summary>

```text
Web search results for query: ""reliable_detection" OR "reliably detected" Sadasivan TMLR 2024 accepted October"

Links: [{"title":"Accepted papers","url":"https://jmlr.org/tmlr/papers/"},{"title":"TMLR Submissions","url":"https://openreview.net/submissions?page=103&venue=TMLR"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"TMLR Event Certifications | OpenReview","url":"https://openreview.net/group?id=TMLR%2FEvent_Certifications&event=automl.cc%2FAutoML%2F2023%2FJournal_Track"},{"title":"What Are We Detecting, Really? LLM-Generated Text ...","url":"https://openreview.net/attachment?id=RV12OsgCO0&name=pdf"},{"title":"Under review as submission to TMLR Towards Possibilities & Impossibilities of","url":"https://openreview.net/notes/edits/attachment?id=MQxm4BolAs&name=pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Under review as submission to TMLR","url":"https://openreview.net/pdf?id=pTuuuGQ1zl"}]

Based on the search results, I found a paper by Sadasivan and colleagues that matches your query. The paper is titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", and it was submitted to TMLR with a previous submission URL, indicating it underwent revision.

The paper appears to have been accepted by TMLR in October 2024, as indicated by the metadata date in the search result showing "October 20, 2024". The work stress-tests the robustness of AI text detectors in the presence of attackers, and it addresses the question of whether AI-generated text can be reliably detected using various detection schemes including watermarking and neural network-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "2da241c2-27f7-4b3a-acf0-75d9e8e840f6"
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-16T00:00:40.196Z_

<details><summary>↩ Tool result · `toolu_01NwaMLRF9sMGckUpma83HPf`</summary>

```text
Web search results for query: "Spotting LLMs With Binoculars Zero-Shot Detection Machine-Generated Text Hans Schwarzschild ICML 2024"

Links: [{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"Spotting LLMs with binoculars: zero-shot detection of ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692768"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | MPI-IS","url":"https://is.mpg.de/en/publications/hans_spotting_2024"},{"title":"[Quick Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://liner.com/review/spotting-llms-with-binoculars-zeroshot-detection-machinegenerated-text"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"ICML Poster Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://icml.cc/virtual/2024/poster/33662"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of ...","url":"https://arxiv.org/pdf/2401.12070"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"}]

I found comprehensive information about this paper. Here are the key details:

## Paper Overview

"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" was authored by Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein in 2024.

## Key Findings

Binoculars is a state-of-the-art method for detecting AI-generated text that is zero-shot and domain-agnostic, requiring no training data. The method is based on a score that contrasts two closely related language models, which is highly accurate at separating human-generated and machine-generated text, and requires only simple calculations using a pair of pre-trained LLMs.

## Performance

Over a wide range of document types, Binoculars detects over 90% of generated samples from ChatGPT (and other LLMs) at a false positive rate of 0.01%, despite not being trained on any ChatGPT data. It is capable of spotting machine text from a range of modern LLMs without any model-specific modifications.

## Publication

The paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), appearing on pages 17519-17537.

The code is available on [GitHub](https://github.com/ahans30/Binoculars).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "090c61ce-22ae-4f88-b706-c4f7c8d381bf"
}
```

</details>

---

### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for \"Self-Consuming Generative Models Go MAD\" first a…",
  "usage": {
    "total_tokens": 37364,
    "tool_uses": 16,
    "duration_ms": 40583
  },
  "last_tool_name": "WebSearch",
  "uuid": "3f0f8cb4-5235-47e7-908e-9b842debbee5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Dnv33jMDur9LkG4mdXAie`</summary>

```json
{
  "query": "\"Self-Consuming Generative Models Go MAD\" first author Alemohammad OR Casco-Rodriguez arXiv 2307.01850"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "4fd828fb-c30d-40e1-a099-25f38429259f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ve31gCV9rhcXJZ5h6wvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5665,
      "cache_read_input_tokens": 31652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5665,
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

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Stamatatos \"A survey of modern authorship attribu…",
  "usage": {
    "total_tokens": 37365,
    "tool_uses": 17,
    "duration_ms": 41629
  },
  "last_tool_name": "WebSearch",
  "uuid": "f637a9b5-aca7-4200-9cce-b2ef900fb7c5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 128_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPnzT6PwFTcoN3vrXASmg4`</summary>

```json
{
  "query": "Stamatatos \"A survey of modern authorship attribution methods\" JASIST volume 60 issue 3 2009 online first 2008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "18d5c89f-296d-4bd0-8fd9-6ca552a7251a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ve31gCV9rhcXJZ5h6wvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5665,
      "cache_read_input_tokens": 31652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5665,
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

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for openreview.net OOgsAZdFOt \"Accepted\" TMLR date 20…",
  "usage": {
    "total_tokens": 36644,
    "tool_uses": 17,
    "duration_ms": 56983
  },
  "last_tool_name": "WebSearch",
  "uuid": "a1114e21-42f5-41f9-bc3b-633161bea591",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T1R5fAe2RrTqgqgPdQNyRJ`</summary>

```json
{
  "query": "openreview.net OOgsAZdFOt \"Accepted\" TMLR date 2024 \"Published\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "88a580cd-430b-48c7-92e6-447dfde56ae7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmdZUm9u2ZFC7D9eUL3fAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2955,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2955,
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

### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "description": "Searching for \"Can AI-Generated Text be Reliably Detected\" \"Str…",
  "usage": {
    "total_tokens": 36647,
    "tool_uses": 18,
    "duration_ms": 57099
  },
  "last_tool_name": "WebSearch",
  "uuid": "45802863-472e-4a2d-8e89-9e3cead35a8c",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N4JjeAHyDwXcYKvVvsebpj`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" \"Stress Testing\" TMLR 2024 OR 2025 published accepted date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "8977df07-5d7d-4c39-8691-bc83a51c729b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmdZUm9u2ZFC7D9eUL3fAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2955,
      "cache_read_input_tokens": 33603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2955,
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

### System

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Koppel Schler Argamon \"Computational Methods in A…",
  "usage": {
    "total_tokens": 37366,
    "tool_uses": 18,
    "duration_ms": 42614
  },
  "last_tool_name": "WebSearch",
  "uuid": "445eb694-d0b5-4098-b3d4-6ef2d8536b00",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 134_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EzCGcJSKFZahhixLRoAa9e`</summary>

```json
{
  "query": "Koppel Schler Argamon \"Computational Methods in Authorship Attribution\" JASIST volume 60 issue 1 January 2009 online first"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ffbee5e5-94bb-47fc-accc-87e3b3c379a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ve31gCV9rhcXJZ5h6wvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5665,
      "cache_read_input_tokens": 31652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5665,
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

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Beyond Perplexity: Character Distribution Signat…",
  "usage": {
    "total_tokens": 18693,
    "tool_uses": 3,
    "duration_ms": 19933
  },
  "last_tool_name": "WebSearch",
  "uuid": "6dd9df50-34cd-44b0-b75b-6f47b61564ec",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 136_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnpCNY3eY9WNVWUhbVv5XQ`</summary>

```json
{
  "query": "\"Beyond Perplexity: Character Distribution Signatures\" MDTA Benchmark AI Text Detection Narayanasamy arXiv 2605.01647"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9d42a484-39ff-4bdf-bd3e-9f2c58a7360d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MC8LtNqPU3uWb1599PNZNB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 17511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Hendrycks Gimpel \"A Baseline for Detecting Miscla…",
  "usage": {
    "total_tokens": 37367,
    "tool_uses": 19,
    "duration_ms": 43512
  },
  "last_tool_name": "WebSearch",
  "uuid": "da342afc-02c1-46ee-8901-13619a901491",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 138_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HgbxVDkwTUWerb5TuuXmic`</summary>

```json
{
  "query": "Hendrycks Gimpel \"A Baseline for Detecting Misclassified\" ICLR 2017 arXiv 1610.02136 publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "4d386721-23dd-499b-8f54-73e3d832c944",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ve31gCV9rhcXJZ5h6wvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5665,
      "cache_read_input_tokens": 31652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5665,
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

_source line 139_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for DivEye Basani Chen TMLR 2026 accepted publication…",
  "usage": {
    "total_tokens": 37368,
    "tool_uses": 20,
    "duration_ms": 44169
  },
  "last_tool_name": "WebSearch",
  "uuid": "d167bbcd-ef47-4e86-8a1f-3a2b209ef26a",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4MgB6xNnC1AbzuLp8QRhD`</summary>

```json
{
  "query": "DivEye Basani Chen TMLR 2026 accepted publication date openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "fbbb9b14-43a3-4c75-bd8d-fec00f0c47b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ve31gCV9rhcXJZ5h6wvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5665,
      "cache_read_input_tokens": 31652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5665,
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

_source line 141 · 2026-05-16T00:00:45.185Z_

<details><summary>↩ Tool result · `toolu_019Dnv33jMDur9LkG4mdXAie`</summary>

```text
Web search results for query: ""Self-Consuming Generative Models Go MAD" first author Alemohammad OR Casco-Rodriguez arXiv 2307.01850"

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"Self-Consuming Generative Models Go MAD | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/pdf/2307.01850"},{"title":"Paper page - Self-Consuming Generative Models Go MAD","url":"https://huggingface.co/papers/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230701850A/abstract"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://dsp.rice.edu/2023/07/06/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"}]

I found the paper! Here's what the search revealed:

"Self-Consuming Generative Models Go MAD" is authored by Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk, with arXiv identifier 2307.01850.

The paper examines how advances in generative AI have led to using synthetic data to train next-generation models, and repeating this process creates an autophagous (self-consuming) loop whose properties are poorly understood. The authors conduct analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through generations of training and whether samples from previous generation models have been biased to trade off data quality versus diversity.

The primary conclusion is that without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease—a condition termed Model Autophagy Disorder (MAD).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c50b9f30-eb71-4bf5-9611-f54b2396bb37"
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-16T00:00:46.844Z_

<details><summary>↩ Tool result · `toolu_01HgbxVDkwTUWerb5TuuXmic`</summary>

```text
Web search results for query: "Hendrycks Gimpel "A Baseline for Detecting Misclassified" ICLR 2017 arXiv 1610.02136 publication year"

Links: [{"title":"[1610.02136] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks","url":"https://arxiv.org/abs/1610.02136"},{"title":"GitHub - hendrycks/error-detection: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks · GitHub","url":"https://github.com/hendrycks/error-detection"},{"title":"A Baseline for Detecting Misclassified and Out-of- ...","url":"https://arxiv.org/pdf/1610.02136"},{"title":"dblp: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks.","url":"https://dblp.org/rec/conf/iclr/HendrycksG17.html"},{"title":"[PDF] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Baseline-for-Detecting-Misclassified-and-Examples-Hendrycks-Gimpel/6ff2a434578ff2746b9283e45abf296887f48a2d"},{"title":"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/c198223714bea8d959e26861ff07dd8d"},{"title":"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks | OpenReview","url":"https://openreview.net/forum?id=Hkg4TI9xl"},{"title":"A Baseline for Detecting Misclassified and Out-of- ...","url":"https://orkg.org/papers/R533875"},{"title":"Hendrycks, D. and Gimpel, K. (2017) A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks. Conference Track Proceedings. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3774528"},{"title":"[1610.02136v2] A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks","url":"https://arxiv.org/abs/1610.02136v2"}]

Based on the search results, I can provide you with the publication information for this paper:

The paper "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks" by Dan Hendrycks and Kevin Gimpel was published in the Proceedings of the International Conference on Learning Representations in 2017. The arXiv preprint identifier is 1610.02136, and it was presented as a poster at ICLR 2017.

To summarize the publication details:
- **Authors**: Dan Hendrycks and Kevin Gimpel
- **Title**: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks
- **Conference**: ICLR (International Conference on Learning Representations)
- **Publication Year**: 2017
- **arXiv ID**: 1610.02136


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ffb8fa2d-1faf-4b1a-a059-2b15a93e5b82"
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-16T00:00:46.969Z_

<details><summary>↩ Tool result · `toolu_01JPnzT6PwFTcoN3vrXASmg4`</summary>

```text
Web search results for query: "Stamatatos "A survey of modern authorship attribution methods" JASIST volume 60 issue 3 2009 online first 2008"

Links: [{"title":"A survey of modern authorship attribution methods - Stamatatos - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/asi.21001"},{"title":"A survey of modern authorship attribution methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-survey-of-modern-authorship-attribution-methods-Stamatatos/d25c27c7a3e9f41f150e8eadbad34c1c05d67510"},{"title":"dblp: A survey of modern authorship attribution methods.","url":"https://dblp.org/rec/journals/jasis/Stamatatos09.html"},{"title":"A survey of modern authorship attribution methods","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i3p538-556.html"},{"title":"(PDF) A survey of modern authorship attribution methods (2009) | Efstathios Stamatatos | 1366 Citations","url":"https://scispace.com/papers/a-survey-of-modern-authorship-attribution-methods-2lb4q2gu7n"},{"title":"A survey of modern authorship attribution methods. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/19b36b85e07a64fd5295da2a2ad9a9efb"},{"title":"EconPapers: A survey of modern authorship attribution methods","url":"https://econpapers.repec.org/RePEc:bla:jamist:v:60:y:2009:i:3:p:538-556"},{"title":"A survey of modern authorship attribution methods - researchr publication","url":"https://researchr.org/publication/Stamatatos09"},{"title":"dblp: JASIST, Volume 60, 2009","url":"https://dblp.org/db/journals/jasis/jasis60.html"},{"title":"A Survey of Modern Authorship Attribution Methods | Request PDF","url":"https://www.researchgate.net/publication/220435062_A_Survey_of_Modern_Authorship_Attribution_Methods"}]

I found the publication you were looking for! Efstathios Stamatatos's "A survey of modern authorship attribution methods" was published in the Journal of the American Society for Information Science and Technology, Volume 60, Issue 3, pages 538-556 in March 2009. 

According to the Wiley Online Library source, this article was released online first on December 16, 2008, before the official print publication in 2009.

The article is a survey of recent advances of the automated approaches to attributing authorship, examining their characteristics for both text representation and text classification.

The full DOI is 10.1002/asi.21001, and it's available through the Wiley Online Library at: https://onlinelibrary.wiley.com/doi/10.1002/asi.21001


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "a979c363-5ec6-4818-a03f-cd8de21d3dce"
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-16T00:00:47.050Z_

<details><summary>↩ Tool result · `toolu_01T1R5fAe2RrTqgqgPdQNyRJ`</summary>

```text
Web search results for query: "openreview.net OOgsAZdFOt "Accepted" TMLR date 2024 "Published""

Links: [{"title":"Submissions | OpenReview","url":"https://openreview.net/submissions?page=131&venue=TMLR"},{"title":"Accepted papers","url":"https://jmlr.org/tmlr/papers/"},{"title":"Learning on Graphs Conference","url":"https://logconference.org/cfp/"},{"title":"Announcing MLRC 2025, our first in-person conference | MLRC 2025","url":"https://reproml.org/blog/announcing_mlrc2025/"},{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/faq.html"}]

The search results don't contain specific information about the paper with the ID "OOgsAZdFOt" on OpenReview. The search returned general information about TMLR submissions and accepted papers, but didn't locate the specific paper you're looking for.

To find information about this specific paper, I'd recommend:

1. Visiting the direct OpenReview URL: `https://openreview.net/forum?id=OOgsAZdFOt`
2. Searching OpenReview directly with the paper ID
3. Checking the TMLR submissions page on OpenReview with filters for accepted papers from 2024

If you have additional details about the paper (such as the title, authors, or keywords), I can try a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "f82b9b51-71a6-4708-a30c-1be0af2289f1"
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-16T00:00:47.156Z_

<details><summary>↩ Tool result · `toolu_01EzCGcJSKFZahhixLRoAa9e`</summary>

```text
Web search results for query: "Koppel Schler Argamon "Computational Methods in Authorship Attribution" JASIST volume 60 issue 1 January 2009 online first"

Links: [{"title":"Computational methods in authorship attribution - Koppel - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"},{"title":"Computational methods in authorship attribution - Semantic Scholar","url":"https://www.semanticscholar.org/paper/Computational-methods-in-authorship-attribution-Koppel-Schler/c4550ee1f3a1a08c9d2f89e13a7dec7c220c1704"},{"title":"Publications (Chronological) - Prof. Moshe Koppel","url":"https://u.cs.biu.ac.il/~koppel/Publications.html"},{"title":"Computational methods in authorship attribution","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i1p9-26.html"},{"title":"(PDF) Computational Methods in Authorship Attribution","url":"https://www.researchgate.net/publication/220433607_Computational_Methods_in_Authorship_Attribution"},{"title":"\"Computational Methods in Authorship Attribution\" by Moshe Koppel, Jonathan Schler et al.","url":"https://touroscholar.touro.edu/president_pubs/275/"},{"title":"1 Computational Methods in Authorship Attribution","url":"https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf"},{"title":"Computational methods in authorship attribution | Journal of the American Society for Information Science and Technology","url":"https://dl.acm.org/citation.cfm?id=1484627"},{"title":"Survey of Methods in Computational Literary Studies - 5 What is Authorship Attribution?","url":"https://methods.clsinfra.io/what-author.html"},{"title":"Computational methods in authorship attribution - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/computational-methods-in-authorship-attribution-4/"}]

I found the article you're looking for! Here are the search results for the paper:

"Computational Methods in Authorship Attribution" by Koppel, Schler, and Argamon was published in JASIST, volume 60, issue 1, pages 9-26 in 2009.

The paper is available through multiple sources:

1. **Wiley Online Library**: The article features authors Argamon, S., Koppel, M., and Schler, J. and can be accessed at https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961

2. **DOI**: The article's DOI is 10.1002/asi.20961

3. **Full PDF**: A PDF version appears to be available at https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf (from Bar-Ilan University)

The paper discusses how statistical authorship attribution has a long history culminating in machine learning methods, though most work assumes a small closed set of candidate authors and unlimited training text for each.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "792a4b80-8cde-475c-a702-c01202bd420a"
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-16T00:00:47.448Z_

<details><summary>↩ Tool result · `toolu_01N4JjeAHyDwXcYKvVvsebpj`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" "Stress Testing" TMLR 2024 OR 2025 published accepted date"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Publication Details:**
- **Journal:** Transactions on Machine Learning Research (TMLR)
- **Year:** 2025
- **Accepted Date:** March 13, 2025 (based on the TMLR publication announcement)
- **Action Editor:** Kamalika Chaudhuri

**Paper Link:** https://openreview.net/forum?id=OOgsAZdFOt

The paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors and provides a theoretical framework connecting detector performance to the distribution differences between human and AI text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "52cf65fc-3691-4824-be58-3bb5f3af6490"
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-16T00:00:48.458Z_

<details><summary>↩ Tool result · `toolu_01A4MgB6xNnC1AbzuLp8QRhD`</summary>

```text
Web search results for query: "DivEye Basani Chen TMLR 2026 accepted publication date openreview"

Links: [{"title":"Accepted papers","url":"https://jmlr.org/tmlr/papers/"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"TMLR | OpenReview","url":"https://openreview.net/group?id=TMLR"},{"title":"Submissions | OpenReview","url":"https://openreview.net/submissions?venue=TMLR"},{"title":"TMLR Expert Reviewers | OpenReview","url":"https://openreview.net/group?id=TMLR/Expert_Reviewers"},{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"MLRC 2026: Reproducibility as an Official Track at NeurIPS – NeurIPS Blog","url":"https://blog.neurips.cc/2026/05/04/mlrc-2026-reproducibility-as-an-official-track-at-neurips/"},{"title":"TMLR Event Certifications | OpenReview","url":"https://openreview.net/group?id=TMLR%2FEvent_Certifications&event=automl.cc%2FAutoML%2F2023%2FJournal_Track"},{"title":"Accepted papers at TMLR (@TmlrPub) · X","url":"https://twitter.com/TmlrPub"}]

Based on the search results, I found information about the DivEye paper:

The paper by Advik Raj Basani and Pin-Yu Chen was accepted at TMLR in February 2026. DivEye was accepted at TMLR '26 and also presented at ICML, Data in Generative Models (DIG-BUG) '25.

The paper is titled "Diversity Boosts AI-Generated Text Detection" and the OpenReview forum ID is WscAU9It1l.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "077efda1-175d-49ff-aca5-3a4d3d7b8b6f"
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-16T00:00:51.135Z_

<details><summary>↩ Tool result · `toolu_01SnpCNY3eY9WNVWUhbVv5XQ`</summary>

```text
Web search results for query: ""Beyond Perplexity: Character Distribution Signatures" MDTA Benchmark AI Text Detection Narayanasamy arXiv 2605.01647"

Links: [{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"[2603.17522] Detecting the Machine: A Comprehensive Benchmark of AI-Generated Text Detectors Across Architectures, Domains, and Adversarial Conditions","url":"https://arxiv.org/abs/2603.17522"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Not all tokens are created equal: Perplexity Attention Weighted Networks for AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S156625352500538X"},{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"Beyond Perplexity: The Technical Evolution of AI Text Analysis - Technology Org","url":"https://www.technology.org/2026/01/15/beyond-perplexity-the-technical-evolution-of-ai-text-analysis/"},{"title":"[2501.03940] Not all tokens are created equal: Perplexity Attention Weighted Networks for AI generated text detection","url":"https://arxiv.org/abs/2501.03940"}]

I found the paper you're looking for! Here's information about it:

**Paper Title:** Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection

**Authors:** Priyadarshan Narayanasamy and 3 other authors

**arXiv ID:** 2605.01647

**Overview:**

Training-free AI text detection methods primarily rely on model log-probabilities, achieving strong performance through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions.

**Main Contribution:**

The authors introduce an alternative detection signal based on character distribution signatures and provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence.

**The MDTA Benchmark:**

The Models-Domains-Temperatures-Adversarial (MDTA) benchmark consists of 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies, substantially expanding the HC3 dataset with modern model responses, temperature variation, and targeted adversarial attacks including lipogrammatic constraints designed to challenge character-level detection methods.

**Results:**

The Letter Distribution Score (LD-Score) demonstrates low correlation (r = 0.08-0.13) with perplexity methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "155b81be-9f90-4c78-8227-cc5908ba8dfe"
}
```

</details>

---

### System

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Breaking the Generator Barrier\" Disentangled Rep…",
  "usage": {
    "total_tokens": 19779,
    "tool_uses": 4,
    "duration_ms": 31231
  },
  "last_tool_name": "WebSearch",
  "uuid": "8263b1cc-c7ec-4ded-bb83-bf1b9bf0f0f4",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 150_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UB5gkFu6XbngLH71HCeNfa`</summary>

```json
{
  "query": "\"Breaking the Generator Barrier\" Disentangled Representation Generalizable AI-Text Detection Pu Cheng arXiv 2604.13692"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "7cd76047-e4a9-4c7f-8ad0-7e490ff6b544",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMQYTyePHpavsb7MwPskFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 18612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1041,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 151_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Koppel \"Computational Methods in Authorship Attri…",
  "usage": {
    "total_tokens": 41898,
    "tool_uses": 21,
    "duration_ms": 55608
  },
  "last_tool_name": "WebSearch",
  "uuid": "c995ff43-65c9-4bc9-8674-5ec8f1863695",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 152_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MG8MSztbCLjTvrnkMqM2Ak`</summary>

```json
{
  "query": "Koppel \"Computational Methods in Authorship Attribution\" JASIST 2009 \"online\" \"2008\" first published doi 10.1002/asi.20961"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "795ad77a-ffaf-4869-a0db-d80bbba73601",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHMw87uoR5AyJ1ycAPRj6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 37317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4528,
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

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "description": "Searching for Qwen3 Technical Report citation bibtex \"Qwen Team…",
  "usage": {
    "total_tokens": 41899,
    "tool_uses": 22,
    "duration_ms": 55859
  },
  "last_tool_name": "WebSearch",
  "uuid": "8b2300bc-5318-4441-ba2d-7b882395c8b2",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 154_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CewnozZibuWsQdEt7TNiew`</summary>

```json
{
  "query": "Qwen3 Technical Report citation bibtex \"Qwen Team\" author convention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "16bb31d8-a51f-4641-9239-eb680f037b8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHMw87uoR5AyJ1ycAPRj6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 37317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4528,
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

_source line 155 · 2026-05-16T00:00:59.680Z_

<details><summary>↩ Tool result · `toolu_01MG8MSztbCLjTvrnkMqM2Ak`</summary>

```text
Web search results for query: "Koppel "Computational Methods in Authorship Attribution" JASIST 2009 "online" "2008" first published doi 10.1002/asi.20961"

Links: [{"title":"Computational methods in authorship attribution - Koppel - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"},{"title":"Computational methods in authorship attribution - Semantic Scholar","url":"https://www.semanticscholar.org/paper/Computational-methods-in-authorship-attribution-Koppel-Schler/c4550ee1f3a1a08c9d2f89e13a7dec7c220c1704"},{"title":"Publications (Chronological) - Prof. Moshe Koppel","url":"https://u.cs.biu.ac.il/~koppel/Publications.html"},{"title":"(PDF) Computational Methods in Authorship Attribution","url":"https://www.researchgate.net/publication/220433607_Computational_Methods_in_Authorship_Attribution"},{"title":"Computational methods in authorship attribution","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i1p9-26.html"},{"title":"\"Computational Methods in Authorship Attribution\" by Moshe Koppel, Jonathan Schler et al.","url":"https://touroscholar.touro.edu/president_pubs/275/"},{"title":"1 Computational Methods in Authorship Attribution","url":"https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf"},{"title":"(PDF) Computational methods in authorship attribution","url":"https://www.academia.edu/15373725/Computational_methods_in_authorship_attribution"},{"title":"Psu","url":"https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.153.9654&rep=rep1&type=pdf"},{"title":"Computational methods in authorship attribution - Koppel - 2009","url":"https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"}]

Based on the search results, I found the publication you're looking for:

The article "Computational Methods in Authorship Attribution" by Moshe Koppel, Jonathan Schler, and Shlomo Engelson Argamon was published in JASIST (Journal of the American Society for Information Science and Technology) in 2009, with DOI: 10.1002/asi.20961.

More specifically, the article was published in volume 60, issue 1, pages 9-26. According to the metadata, it appears to have been first published online on September 26, 2008, before the official 2009 publication date, which aligns with the "2008" reference in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "cf0f8341-213c-428f-9929-04f922696e33"
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-16T00:01:00.338Z_

<details><summary>↩ Tool result · `toolu_01CewnozZibuWsQdEt7TNiew`</summary>

```text
Web search results for query: "Qwen3 Technical Report citation bibtex "Qwen Team" author convention"

Links: [{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Qwen3 Technical Report | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.09388"},{"title":"Qwen3-VL Technical Report | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.21631/sso-callback"},{"title":"Qwen/Qwen3-VL-8B-Thinking - AI Model on Runcrate | Deploy Instantly | Runcrate","url":"https://www.runcrate.ai/models/Qwen/Qwen3-VL-8B-Thinking"},{"title":"[2509.17765] Qwen3-Omni Technical Report","url":"https://arxiv.org/abs/2509.17765"},{"title":"[2511.21631] Qwen3-VL Technical Report","url":"https://arxiv.org/abs/2511.21631"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2510.14276] Qwen3Guard Technical Report","url":"https://arxiv.org/abs/2510.14276"}]

Based on the web search results, I found the BibTeX citation format for the Qwen3 Technical Report:

The standard BibTeX citation for the Qwen3 Technical Report uses "Qwen Team" as the author: `@misc{qwen3technicalreport, title={Qwen3 Technical Report}, author={Qwen Team}, year={2025}, eprint={2505.09388}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2505.09388}}`

This convention of using "Qwen Team" as the corporate author in the BibTeX citation is the standard approach for this technical report, rather than listing individual author names.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "460bdd3c-0f7d-417d-a5b4-70100b37458d"
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-16T00:01:00.770Z_

<details><summary>↩ Tool result · `toolu_01UB5gkFu6XbngLH71HCeNfa`</summary>

```text
Web search results for query: ""Breaking the Generator Barrier" Disentangled Representation Generalizable AI-Text Detection Pu Cheng arXiv 2604.13692"

Links: [{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692v1"},{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"Paper page - Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://huggingface.co/papers/2604.21300"},{"title":"[2604.21300] Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/abs/2604.21300"},{"title":"Lin Yuan's research works | Chongqing University of Posts and Telecommunications and other places","url":"https://www.researchgate.net/scientific-contributions/Lin-Yuan-2233802400"},{"title":"Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/html/2604.21300"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"AI Generated Text Detection Using Instruction Fine-tuned Large Language and Transformer-Based Models","url":"https://arxiv.org/html/2507.05157v1"},{"title":"Explainable Disentangled Representation Learning for Generalizable","url":"https://arxiv.org/pdf/2604.21300"}]

I found the paper you're looking for! Here's information about it:

## "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection"

**Paper Details:**
- Authors: Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, and Xiuli Bi
- arXiv: 2604.13692 (submitted on 15 Apr 2026)
- Affiliation: Chongqing University of Posts and Telecommunications, China

**Problem & Approach:**
As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues distinguishing AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts.

To tackle this challenge, the authors propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts.

**Key Results:**
Experiments on the MAGE benchmark, covering 20 representative LLMs across 7 categories, demonstrate consistent improvements over state-of-the-art methods, achieving up to 24.2% accuracy gain and 26.2% F1 improvement. Performance continues to improve as the diversity of training generators increases, confirming strong scalability and generalization in open-set scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c076a3d8-01ee-40a5-a8c5-1a9431698c91"
}
```

</details>

---

### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Feature-Augmented Transformers for Robust AI-Tex…",
  "usage": {
    "total_tokens": 20768,
    "tool_uses": 5,
    "duration_ms": 41387
  },
  "last_tool_name": "WebSearch",
  "uuid": "4d5e6c06-f4a8-46ca-a01c-c5c3358201d7",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 159_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YZcKVytg4XRW63NomzyF4s`</summary>

```json
{
  "query": "\"Feature-Augmented Transformers for Robust AI-Text Detection\" Mady Reschke Schuller arXiv 2605.03969"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ab31a764-a51a-4821-86c0-929f36d429f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuFpeMQpDrmqNkXxAhoRqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 19653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 948,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 160 · 2026-05-16T00:01:11.195Z_

<details><summary>↩ Tool result · `toolu_01YZcKVytg4XRW63NomzyF4s`</summary>

```text
Web search results for query: ""Feature-Augmented Transformers for Robust AI-Text Detection" Mady Reschke Schuller arXiv 2605.03969"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"[2410.08113] Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/abs/2410.08113"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/html/2403.13335v1"},{"title":"[2509.20375] Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text","url":"https://arxiv.org/abs/2509.20375"},{"title":"[2507.05157] AI Generated Text Detection Using Instruction Fine-tuned Large Language and Transformer-Based Models","url":"https://arxiv.org/abs/2507.05157"},{"title":"Enhancing Text Authenticity: A Novel Hybrid Approach for AI-Generated Text Detection","url":"https://arxiv.org/html/2406.06558v1"},{"title":"[2605.13373] Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing","url":"https://arxiv.org/abs/2605.13373"},{"title":"Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/html/2410.08113v1"}]

I found the paper you were looking for! Here's what I found:

The paper "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators" (arXiv 2605.03969) was submitted on May 5, 2026, by Mohamed Mady, Johannes Reschke, and Björn Schuller.

**Main Contribution:**
The paper addresses the challenge that AI-generated text is produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors.

**Methodology and Results:**
The researchers trained transformer-based detectors on HC3 PLUS and calibrated a single decision threshold by maximizing balanced accuracy on held-out validation, which was then kept fixed for all downstream test distributions. They evaluated in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile.

Although base models achieved near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift was brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improved transfer, with their best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4.

The paper is available on arXiv at https://arxiv.org/abs/2605.03969


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "bd0a1c8d-6abb-4248-b75c-c321e62a7761"
}
```

</details>

---

### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Chainwash: Multi-Step Rewriting Attacks\" Diffusi…",
  "usage": {
    "total_tokens": 21749,
    "tool_uses": 6,
    "duration_ms": 51654
  },
  "last_tool_name": "WebSearch",
  "uuid": "0d2fb7f7-668c-4e8f-8759-bea4f5753b63",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UPNkvKbz6fZSeuECAz1cmp`</summary>

```json
{
  "query": "\"Chainwash: Multi-Step Rewriting Attacks\" Diffusion Language Model Watermarks Ameen Islam arXiv 2605.05503"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "801ef8f5-b0ea-444c-a5ed-c1cdc56c95be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXkvSiiEpPXQEibiz7Lvzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 20601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 941,
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

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4dc224666d3c663a",
  "tool_use_id": "toolu_015qtuXZaLvJjFpcwfBu7UE5",
  "status": "completed",
  "output_file": "",
  "summary": "Verify batch 1: not_found entries",
  "usage": {
    "total_tokens": 38306,
    "tool_uses": 18,
    "duration_ms": 92301
  },
  "uuid": "e783a473-0acf-4d50-a8ee-0738cd1e10b0",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool result

_source line 164 · 2026-05-16T00:01:16.797Z_

<details><summary>↩ Tool result · `toolu_015qtuXZaLvJjFpcwfBu7UE5`</summary>

```text
Now I have enough information. Let me also confirm the exact title in the TMLR version (the bib says the shorter title but TMLR used a longer "Stress Testing" title).

Here are the verification results for all 6 papers:

---

## 1. `detectgpt`

**Bib claims:** "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature", Mitchell/Lee/Khazatsky/Manning/Finn, ICML 2023

**Verified:** All details are **correct**.
- Title: exact match
- Authors: Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn -- correct
- Venue: ICML 2023 (Proceedings of Machine Learning Research, v202) -- correct
- No discrepancies.

---

## 2. `reliable_detection`

**Bib claims:** "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", Sadasivan/Kumar/Balasubramanian/Wang/Feizi, TMLR 2025

**Verified:** All details are **correct**.
- Title: The TMLR-accepted version uses the full title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" -- matches bib
- Authors: Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi -- correct
- Venue: TMLR (Transactions on Machine Learning Research) -- correct
- Year: The TMLR acceptance announcement was posted on March 13, 2025 (via the @TmlrPub tweet). The bib says 2025 -- **correct**
- Note: The earlier arXiv version (2303.11156) had a shorter title ("Can AI-Generated Text be Reliably Detected?") and was first posted in 2023. The TMLR-published version added the "Stress Testing..." subtitle.
- No discrepancies.

---

## 3. `detection_possibilities`

**Bib claims:** "Position: On the Possibilities of AI-Generated Text Detection", Chakraborty/Bedi/Zhu/An/Manocha/Huang, ICML 2024

**Verified:** All details are **correct**.
- Title: exact match (published as a Position paper at ICML 2024)
- Authors: Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang -- correct
- Venue: ICML 2024 (Proceedings of the 41st ICML, pages 6093-6115) -- correct
- No discrepancies.

---

## 4. `aaronson_watermark`

**Bib claims:** "Watermarking GPT Outputs", Aaronson/Kirchner, 2022, Technical Talk

**Verified:** All details are **correct**.
- Title: "Watermarking GPT Outputs" -- matches the title on Aaronson's talks page and blog post
- Authors: Scott Aaronson and Hendrik Kirchner (Kirchner was the OpenAI engineer who built the prototype) -- correct
- Year: 2022 -- correct (the talk was given at UT Austin Math Club on Oct 18, 2022; at UT Austin EA Club on Nov 14, 2022; and at OpenAI SF on Dec 13, 2022)
- Type: Technical Talk / `@misc` -- correct. This was never published as a formal paper; it remains a talk/blog post (scottaaronson.blog/?p=6823)
- No discrepancies.

---

## 5. `pythia`

**Bib claims:** "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling", Biderman/Schoelkopf/Anthony(Quentin Gregory)/Bradley/O'Brien/Hallahan/Khan/Purohit/Prashanth(USVSN Sai)/Raff/Skowron/Sutawika/van der Wal, ICML 2023

**Verified:** All details are **correct**.
- Title: exact match
- Authors (full list from DBLP/PMLR proceedings): Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, Oskar van der Wal -- all 13 authors match
- Venue: ICML 2023 (PMLR v202, pages 2397-2430) -- correct
- No discrepancies.

---

## 6. `xgboost`

**Bib claims:** "XGBoost: A Scalable Tree Boosting System", Chen/Guestrin, KDD 2016

**Verified:** All details are **correct**.
- Title: exact match
- Authors: Tianqi Chen and Carlos Guestrin -- correct
- Venue: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016), pages 785-794 -- correct
- No discrepancies.

---

## Summary

**All 6 citations are accurate.** No discrepancies were found in titles, author lists, venues, or years. The bib entries faithfully represent the published records.

Sources:
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [DetectGPT - arXiv](https://arxiv.org/abs/2301.11305)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Reliable Detection - TMLR Announcement](https://x.com/TmlrPub/status/1900336120296034775)
- [Detection Possibilities - ICML Proceedings](https://proceedings.mlr.press/v235/chakraborty24a.html)
- [Aaronson Watermark - Blog Post](https://scottaaronson.blog/?p=6823)
- [Aaronson Talks Page](https://www.scottaaronson.com/talks/)
- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)
- [Pythia - ICML Proceedings](https://proceedings.mlr.press/v202/biderman23a.html)
- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)
- [XGBoost - arXiv](https://arxiv.org/abs/1603.02754)

agentId: a4dc224666d3c663a (use SendMessage with to: 'a4dc224666d3c663a' to continue this agent)
&lt;usage>total_tokens: 39963
tool_uses: 18
duration_ms: 92303&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "beeb6883-37a0-4546-a755-acc984635aa9",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.\n\nPapers to verify:\n\n1. **detectgpt** — bib claims: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023\n\n2. **reliable_detection** — bib claims: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025\n\n3. **detection_possibilities** — bib claims: \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024\n\n4. **aaronson_watermark** — bib claims: \"Watermarking GPT Outputs\", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk\n\n5. **pythia** — bib claims: \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023\n\n6. **xgboost** — bib claims: \"XGBoost: A Scalable Tree Boosting System\", Chen, Tianqi and Guestrin, Carlos, KDD 2016\n\nReport all findings precisely, including any year, author, or venue discrepancies.",
    "agentId": "a4dc224666d3c663a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information. Let me also confirm the exact title in the TMLR version (the bib says the shorter title but TMLR used a longer \"Stress Testing\" title).\n\nHere are the verification results for all 6 papers:\n\n---\n\n## 1. `detectgpt`\n\n**Bib claims:** \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell/Lee/Khazatsky/Manning/Finn, ICML 2023\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors: Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn -- correct\n- Venue: ICML 2023 (Proceedings of Machine Learning Research, v202) -- correct\n- No discrepancies.\n\n---\n\n## 2. `reliable_detection`\n\n**Bib claims:** \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan/Kumar/Balasubramanian/Wang/Feizi, TMLR 2025\n\n**Verified:** All details are **correct**.\n- Title: The TMLR-accepted version uses the full title \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\" -- matches bib\n- Authors: Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi -- correct\n- Venue: TMLR (Transactions on Machine Learning Research) -- correct\n- Year: The TMLR acceptance announcement was posted on March 13, 2025 (via the @TmlrPub tweet). The bib says 2025 -- **correct**\n- Note: The earlier arXiv version (2303.11156) had a shorter title (\"Can AI-Generated Text be Reliably Detected?\") and was first posted in 2023. The TMLR-published version added the \"Stress Testing...\" subtitle.\n- No discrepancies.\n\n---\n\n## 3. `detection_possibilities`\n\n**Bib claims:** \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty/Bedi/Zhu/An/Manocha/Huang, ICML 2024\n\n**Verified:** All details are **correct**.\n- Title: exact match (published as a Position paper at ICML 2024)\n- Authors: Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang -- correct\n- Venue: ICML 2024 (Proceedings of the 41st ICML, pages 6093-6115) -- correct\n- No discrepancies.\n\n---\n\n## 4. `aaronson_watermark`\n\n**Bib claims:** \"Watermarking GPT Outputs\", Aaronson/Kirchner, 2022, Technical Talk\n\n**Verified:** All details are **correct**.\n- Title: \"Watermarking GPT Outputs\" -- matches the title on Aaronson's talks page and blog post\n- Authors: Scott Aaronson and Hendrik Kirchner (Kirchner was the OpenAI engineer who built the prototype) -- correct\n- Year: 2022 -- correct (the talk was given at UT Austin Math Club on Oct 18, 2022; at UT Austin EA Club on Nov 14, 2022; and at OpenAI SF on Dec 13, 2022)\n- Type: Technical Talk / `@misc` -- correct. This was never published as a formal paper; it remains a talk/blog post (scottaaronson.blog/?p=6823)\n- No discrepancies.\n\n---\n\n## 5. `pythia`\n\n**Bib claims:** \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman/Schoelkopf/Anthony(Quentin Gregory)/Bradley/O'Brien/Hallahan/Khan/Purohit/Prashanth(USVSN Sai)/Raff/Skowron/Sutawika/van der Wal, ICML 2023\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors (full list from DBLP/PMLR proceedings): Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, Oskar van der Wal -- all 13 authors match\n- Venue: ICML 2023 (PMLR v202, pages 2397-2430) -- correct\n- No discrepancies.\n\n---\n\n## 6. `xgboost`\n\n**Bib claims:** \"XGBoost: A Scalable Tree Boosting System\", Chen/Guestrin, KDD 2016\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors: Tianqi Chen and Carlos Guestrin -- correct\n- Venue: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016), pages 785-794 -- correct\n- No discrepancies.\n\n---\n\n## Summary\n\n**All 6 citations are accurate.** No discrepancies were found in titles, author lists, venues, or years. The bib entries faithfully represent the published records.\n\nSources:\n- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)\n- [DetectGPT - arXiv](https://arxiv.org/abs/2301.11305)\n- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)\n- [Reliable Detection - TMLR Announcement](https://x.com/TmlrPub/status/1900336120296034775)\n- [Detection Possibilities - ICML Proceedings](https://proceedings.mlr.press/v235/chakraborty24a.html)\n- [Aaronson Watermark - Blog Post](https://scottaaronson.blog/?p=6823)\n- [Aaronson Talks Page](https://www.scottaaronson.com/talks/)\n- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)\n- [Pythia - ICML Proceedings](https://proceedings.mlr.press/v202/biderman23a.html)\n- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)\n- [XGBoost - arXiv](https://arxiv.org/abs/1603.02754)"
      }
    ],
    "totalDurationMs": 92303,
    "totalTokens": 39963,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 36558,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1749,
          "cache_read_input_tokens": 36558,
          "cache_creation_input_tokens": 1655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1655,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-16T00:01:23.389Z_

<details><summary>↩ Tool result · `toolu_01UPNkvKbz6fZSeuECAz1cmp`</summary>

```text
Web search results for query: ""Chainwash: Multi-Step Rewriting Attacks" Diffusion Language Model Watermarks Ameen Islam arXiv 2605.05503"

Links: [{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"Watermarking Diffusion Language Models","url":"https://arxiv.org/pdf/2509.24368"},{"title":"Character-Level Perturbations Disrupt LLM Watermarks","url":"https://arxiv.org/html/2509.09112v1"},{"title":"LR-DWM: Efficient Watermarking for Diffusion Language Models","url":"https://arxiv.org/html/2601.12376v1"},{"title":"[2509.24368] Watermarking Diffusion Language Models","url":"https://arxiv.org/abs/2509.24368"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"},{"title":"Watermarking Language Models with Error Correcting Codes","url":"https://arxiv.org/html/2406.10281v4"},{"title":"Watermarking Discrete Diffusion Language Models","url":"https://arxiv.org/html/2511.02083v2"},{"title":"When There Is No Decoder: Removing Watermarks from Stable Diffusion Models in a No-box Setting","url":"https://arxiv.org/html/2507.03646v1"}]

Based on the search results, here's what I found about the paper "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks" (arXiv 2605.05503):

## Overview

The paper is by Mohd Ruhul Ameen and 3 other authors. Statistical watermarking is a common approach for verifying whether text was written by a language model. Most existing schemes assume autoregressive generation, where tokens are produced left to right and contextual hashing is well defined. Diffusion language models generate text by denoising tokens in arbitrary order, so these schemes cannot be applied directly.

## Research Focus

The paper studies what happens when watermarked text is rewritten not once but several times. The watermark signal is washed out through a chain of model-mediated rewrites. Unlike token-level deletion, substitution, or manual editing, chainwash is generative. The output is not formed by small local changes to the original text, but by repeatedly regenerating the text through another language model.

## Methodology

1,605 watermarked completions of about 300 tokens each were produced across five WaterBench domains using LLaDA-8B-Instruct. Each completion was then rewritten by four open-weight language models, from 1.5B to 8B parameters, none of which know the watermark key. Five rewrite styles were tested: paraphrase, humanize, simplify, academic, and summarize-expand. Each rewriter was run on its own, and every style was chained for up to five hops, producing 160,500 rewritten texts in total.

## Key Findings

Across all four rewriters and five rewrite styles, repeated rewriting substantially reduces detectability while semantic content is largely preserved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "85619f91-a90a-4e65-8a8c-1f3a11f06644"
}
```

</details>

---

### System

_source line 166_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Markovian Generation Chains in Large Language Mo…",
  "usage": {
    "total_tokens": 22755,
    "tool_uses": 7,
    "duration_ms": 63866
  },
  "last_tool_name": "WebSearch",
  "uuid": "6aae99c6-98ab-4bdc-bb76-15f7947049dd",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 167_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXufD623fm9jGPphGFJQ66`</summary>

```json
{
  "query": "\"Markovian Generation Chains in Large Language Models\" Geng Mohamed Shang Vazirgiannis Poibeau arXiv 2603.11228"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "828dec54-4def-4b3a-9860-c131e688f600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsebKa9DnjLnUTuGz2BDv4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 21542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 967,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 168 · 2026-05-16T00:01:32.755Z_

<details><summary>↩ Tool result · `toolu_01WXufD623fm9jGPphGFJQ66`</summary>

```text
Web search results for query: ""Markovian Generation Chains in Large Language Models" Geng Mohamed Shang Vazirgiannis Poibeau arXiv 2603.11228"

Links: [{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"[2603.04412] Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models","url":"https://arxiv.org/abs/2603.04412"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.02724v2"},{"title":"[2410.02724v1] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724v1"},{"title":"Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models","url":"https://arxiv.org/html/2603.04412"},{"title":"Large Language Models as Markov Chains | OpenReview","url":"https://openreview.net/forum?id=RDFkGZ9Dkh"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Markovian Generation Chains in Large Language Models

**Authors:** Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau

**ArXiv ID:** 2603.11228 (Submitted on March 11, 2026)

**Main Contribution:**

The paper defines an iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Key Findings:**

In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or continues to produce novel sentences over a finite horizon. The iterative process can either increase or reduce sentence diversity depending on factors such as the temperature parameter and the initial input sentence.

You can access the paper directly at: https://arxiv.org/abs/2603.11228


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "88366c64-8d43-4bcd-8cfb-08ea3d369090"
}
```

</details>

---

### System

_source line 169_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "abd348b8cf003e5f5",
  "tool_use_id": "toolu_01MfNwpzXjZ5JJuaohdfNX9D",
  "status": "completed",
  "output_file": "",
  "summary": "Verify batch 2: mismatches + year discrepancies",
  "usage": {
    "total_tokens": 43542,
    "tool_uses": 22,
    "duration_ms": 95025
  },
  "uuid": "1d78ef20-51ea-4638-85f8-f59e32155acb",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool result

_source line 170 · 2026-05-16T00:01:34.769Z_

<details><summary>↩ Tool result · `toolu_01MfNwpzXjZ5JJuaohdfNX9D`</summary>

```text
I now have all the information needed. Here is my comprehensive verification report:

---

## Citation Verification Results

### 1. self_consuming_mad -- BIB IS CORRECT

- **Title**: "Self-Consuming Generative Models Go MAD" -- CORRECT
- **First author**: Alemohammad, Sina -- CORRECT. The arXiv listing, Semantic Scholar, and ICLR proceedings all list Alemohammad as first author. OpenAlex's claim that Casco-Rodriguez is first author is wrong.
- **Author list**: Correct as listed in bib
- **Year**: 2024 -- CORRECT. Published at ICLR 2024 (Vienna). The arXiv preprint was July 2023, which explains OpenAlex showing 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 2. qwen3 -- BIB IS CORRECT

- **Title**: "Qwen3 Technical Report" -- CORRECT
- **Author**: `{Qwen Team}` -- CORRECT. The official arXiv BibTeX and HuggingFace both use "Qwen Team" as the corporate author. While there are 60+ individual contributors (with An Yang listed first alphabetically), the standard citation convention for this paper is the team name.
- **Year**: 2025 -- CORRECT (arXiv preprint May 2025, no conference proceedings)
- **Venue**: arXiv:2505.09388 -- CORRECT
- **Verdict**: No changes needed. OpenAlex listing "Yang" as first author reflects the individual author list, but {Qwen Team} is the standard citation form.

### 3. dna_gpt -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Yang, Xianjun et al. -- Correct
- **Year**: 2024 -- CORRECT. This is an ICLR 2024 paper (poster). The arXiv preprint was May 2023, which explains OpenAlex showing 2023. The conference proceedings year is 2024.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 4. fast_detectgpt -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Bao, Guangsheng et al. -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint October 2023 explains the OpenAlex discrepancy.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 5. diveye -- BIB IS CORRECT (year=2026)

- **Title**: Correct
- **Authors**: Basani, Advik Raj and Chen, Pin-Yu -- Correct
- **Year**: 2026 -- CORRECT. Published in TMLR February 2026 (the GitHub repo is tagged `[TMLR '26]` and the arXiv PDF header reads "Published in Transactions on Machine Learning Research (02/2026)"). The arXiv preprint was September 2025, which explains OpenAlex showing 2025.
- **Venue**: TMLR -- CORRECT
- **Verdict**: No changes needed.

### 6. ood_baseline -- BIB IS CORRECT (year=2017)

- **Title**: Correct
- **Authors**: Hendrycks, Dan and Gimpel, Kevin -- Correct
- **Year**: 2017 -- CORRECT. This is an ICLR 2017 paper (DBLP key: `conf/iclr/HendrycksG17`). The arXiv preprint was October 2016, which explains OpenAlex showing 2016. The conference proceedings year is 2017.
- **Venue**: ICLR 2017 -- CORRECT
- **Verdict**: No changes needed.

### 7. ccnet -- BIB IS CORRECT (year=2020)

- **Title**: Correct
- **Authors**: Wenzek, Guillaume et al. -- Correct
- **Year**: 2020 -- CORRECT. Published in LREC 2020 proceedings (ACL Anthology: `2020.lrec-1.494`). The arXiv preprint was November 2019, explaining OpenAlex's 2019.
- **Venue**: LREC 2020 -- CORRECT
- **Verdict**: No changes needed.

### 8. writing_diversity -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Padmakumar, Vishakh and He, He -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint September 2023 explains OpenAlex's 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 9. nucleus_sampling -- BIB IS CORRECT (year=2020)

- **Title**: "The Curious Case of Neural Text Degeneration" -- Correct
- **Authors**: Holtzman, Ari et al. -- Correct
- **Year**: 2020 -- CORRECT. ICLR 2020 paper (OpenReview ID: `rygGQyrFvH`). ArXiv preprint April 2019 explains OpenAlex's 2019.
- **Venue**: ICLR 2020 -- CORRECT
- **Verdict**: No changes needed.

### 10. min_k_percent -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Shi, Weijia et al. -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 paper (OpenReview ID: `zWqr3MQuNs`). ArXiv preprint October 2023 explains OpenAlex's 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 11. stamatatos_survey -- BIB IS CORRECT (year=2009)

- **Title**: Correct
- **Authors**: Stamatatos, Efstathios -- Correct
- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 3, pages 538-556, March 2009. It was available online first on December 16, 2008, which explains OpenAlex showing 2008. The standard citation year for journal articles is the volume/issue publication year, which is 2009.
- **Venue**: JASIST -- CORRECT
- **Verdict**: No changes needed.

### 12. koppel_authorship -- BIB IS CORRECT (year=2009)

- **Title**: Correct
- **Authors**: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo -- Correct
- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 1, pages 9-26, January 2009. It was published online first on September 26, 2008, explaining OpenAlex's 2008. The correct citation year is 2009.
- **Venue**: JASIST -- CORRECT
- **Verdict**: No changes needed.

### 13. strong_model_collapse -- BIB IS CORRECT (year=2025)

- **Title**: Correct
- **Authors**: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia -- Correct
- **Year**: 2025 -- CORRECT. Published as an ICLR 2025 conference paper (Spotlight). ArXiv preprint October 2024 explains OpenAlex showing 2024.
- **Venue**: ICLR 2025 -- CORRECT
- **Verdict**: No changes needed.

---

## Summary

All 13 bib entries are **correct as-is**. In every case, the OpenAlex year discrepancy is explained by OpenAlex using the arXiv preprint date or online-first date rather than the official conference proceedings / journal volume year. The bib file consistently and correctly uses the conference/journal publication year, which is the standard academic citation practice. No updates are needed.

agentId: abd348b8cf003e5f5 (use SendMessage with to: 'abd348b8cf003e5f5' to continue this agent)
&lt;usage>total_tokens: 45533
tool_uses: 22
duration_ms: 95027&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "5bd78bea-0717-4047-88aa-865cdc439d29",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.\n\n**Mismatch entries:**\n\n1. **self_consuming_mad** — bib claims: \"Self-Consuming Generative Models Go MAD\", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.\n\n2. **qwen3** — bib claims: \"Qwen3 Technical Report\", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.\n\n**Year discrepancy entries (OpenAlex verified year differs from bib year):**\n\n3. **dna_gpt** — bib=2024, OpenAlex=2023. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", Yang et al., ICLR 2024.\n\n4. **fast_detectgpt** — bib=2024, OpenAlex=2023. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", Bao et al., ICLR 2024.\n\n5. **diveye** — bib=2026, OpenAlex=2025. \"Diversity Boosts AI-Generated Text Detection\", Basani, Advik Raj and Chen, Pin-Yu, TMLR.\n\n6. **ood_baseline** — bib=2017, OpenAlex=2016. \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.\n\n7. **ccnet** — bib=2020, OpenAlex=2019. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", Wenzek et al., LREC 2020.\n\n8. **writing_diversity** — bib=2024, OpenAlex=2023. \"Does Writing with Language Models Reduce Content Diversity?\", Padmakumar, Vishakh and He, He, ICLR 2024.\n\n9. **nucleus_sampling** — bib=2020, OpenAlex=2019. \"The Curious Case of Neural Text Degeneration\", Holtzman et al., ICLR 2020.\n\n10. **min_k_percent** — bib=2024, OpenAlex=2023. \"Detecting Pretraining Data from Large Language Models\", Shi et al., ICLR 2024.\n\n11. **stamatatos_survey** — bib=2009, OpenAlex=2008. \"A Survey of Modern Authorship Attribution Methods\", Stamatatos, Efstathios, JASIST.\n\n12. **koppel_authorship** — bib=2009, OpenAlex=2008. \"Computational Methods in Authorship Attribution\", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.\n\n13. **strong_model_collapse** — bib=2025, OpenAlex=2024. \"Strong Model Collapse\", Dohmatob et al., ICLR 2025.\n\nFor each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.",
    "agentId": "abd348b8cf003e5f5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is my comprehensive verification report:\n\n---\n\n## Citation Verification Results\n\n### 1. self_consuming_mad -- BIB IS CORRECT\n\n- **Title**: \"Self-Consuming Generative Models Go MAD\" -- CORRECT\n- **First author**: Alemohammad, Sina -- CORRECT. The arXiv listing, Semantic Scholar, and ICLR proceedings all list Alemohammad as first author. OpenAlex's claim that Casco-Rodriguez is first author is wrong.\n- **Author list**: Correct as listed in bib\n- **Year**: 2024 -- CORRECT. Published at ICLR 2024 (Vienna). The arXiv preprint was July 2023, which explains OpenAlex showing 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 2. qwen3 -- BIB IS CORRECT\n\n- **Title**: \"Qwen3 Technical Report\" -- CORRECT\n- **Author**: `{Qwen Team}` -- CORRECT. The official arXiv BibTeX and HuggingFace both use \"Qwen Team\" as the corporate author. While there are 60+ individual contributors (with An Yang listed first alphabetically), the standard citation convention for this paper is the team name.\n- **Year**: 2025 -- CORRECT (arXiv preprint May 2025, no conference proceedings)\n- **Venue**: arXiv:2505.09388 -- CORRECT\n- **Verdict**: No changes needed. OpenAlex listing \"Yang\" as first author reflects the individual author list, but {Qwen Team} is the standard citation form.\n\n### 3. dna_gpt -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Yang, Xianjun et al. -- Correct\n- **Year**: 2024 -- CORRECT. This is an ICLR 2024 paper (poster). The arXiv preprint was May 2023, which explains OpenAlex showing 2023. The conference proceedings year is 2024.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 4. fast_detectgpt -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Bao, Guangsheng et al. -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint October 2023 explains the OpenAlex discrepancy.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 5. diveye -- BIB IS CORRECT (year=2026)\n\n- **Title**: Correct\n- **Authors**: Basani, Advik Raj and Chen, Pin-Yu -- Correct\n- **Year**: 2026 -- CORRECT. Published in TMLR February 2026 (the GitHub repo is tagged `[TMLR '26]` and the arXiv PDF header reads \"Published in Transactions on Machine Learning Research (02/2026)\"). The arXiv preprint was September 2025, which explains OpenAlex showing 2025.\n- **Venue**: TMLR -- CORRECT\n- **Verdict**: No changes needed.\n\n### 6. ood_baseline -- BIB IS CORRECT (year=2017)\n\n- **Title**: Correct\n- **Authors**: Hendrycks, Dan and Gimpel, Kevin -- Correct\n- **Year**: 2017 -- CORRECT. This is an ICLR 2017 paper (DBLP key: `conf/iclr/HendrycksG17`). The arXiv preprint was October 2016, which explains OpenAlex showing 2016. The conference proceedings year is 2017.\n- **Venue**: ICLR 2017 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 7. ccnet -- BIB IS CORRECT (year=2020)\n\n- **Title**: Correct\n- **Authors**: Wenzek, Guillaume et al. -- Correct\n- **Year**: 2020 -- CORRECT. Published in LREC 2020 proceedings (ACL Anthology: `2020.lrec-1.494`). The arXiv preprint was November 2019, explaining OpenAlex's 2019.\n- **Venue**: LREC 2020 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 8. writing_diversity -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Padmakumar, Vishakh and He, He -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint September 2023 explains OpenAlex's 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 9. nucleus_sampling -- BIB IS CORRECT (year=2020)\n\n- **Title**: \"The Curious Case of Neural Text Degeneration\" -- Correct\n- **Authors**: Holtzman, Ari et al. -- Correct\n- **Year**: 2020 -- CORRECT. ICLR 2020 paper (OpenReview ID: `rygGQyrFvH`). ArXiv preprint April 2019 explains OpenAlex's 2019.\n- **Venue**: ICLR 2020 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 10. min_k_percent -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Shi, Weijia et al. -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 paper (OpenReview ID: `zWqr3MQuNs`). ArXiv preprint October 2023 explains OpenAlex's 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 11. stamatatos_survey -- BIB IS CORRECT (year=2009)\n\n- **Title**: Correct\n- **Authors**: Stamatatos, Efstathios -- Correct\n- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 3, pages 538-556, March 2009. It was available online first on December 16, 2008, which explains OpenAlex showing 2008. The standard citation year for journal articles is the volume/issue publication year, which is 2009.\n- **Venue**: JASIST -- CORRECT\n- **Verdict**: No changes needed.\n\n### 12. koppel_authorship -- BIB IS CORRECT (year=2009)\n\n- **Title**: Correct\n- **Authors**: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo -- Correct\n- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 1, pages 9-26, January 2009. It was published online first on September 26, 2008, explaining OpenAlex's 2008. The correct citation year is 2009.\n- **Venue**: JASIST -- CORRECT\n- **Verdict**: No changes needed.\n\n### 13. strong_model_collapse -- BIB IS CORRECT (year=2025)\n\n- **Title**: Correct\n- **Authors**: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia -- Correct\n- **Year**: 2025 -- CORRECT. Published as an ICLR 2025 conference paper (Spotlight). ArXiv preprint October 2024 explains OpenAlex showing 2024.\n- **Venue**: ICLR 2025 -- CORRECT\n- **Verdict**: No changes needed.\n\n---\n\n## Summary\n\nAll 13 bib entries are **correct as-is**. In every case, the OpenAlex year discrepancy is explained by OpenAlex using the arXiv preprint date or online-first date rather than the official conference proceedings / journal volume year. The bib file consistently and correctly uses the conference/journal publication year, which is the standard academic citation practice. No updates are needed."
      }
    ],
    "totalDurationMs": 95027,
    "totalTokens": 45533,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 41845,
      "output_tokens": 2045,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2045,
          "cache_read_input_tokens": 41845,
          "cache_creation_input_tokens": 1642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1642,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  }
}
```

</details>

---

### System

_source line 171_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"LLM as a Broken Telephone\" Iterative Generation …",
  "usage": {
    "total_tokens": 23596,
    "tool_uses": 8,
    "duration_ms": 73317
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ca8a738-6e47-4230-b00b-f82dc95c02ce",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 172_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U7kQU1csYyokhK5oGtrjx9`</summary>

```json
{
  "query": "\"LLM as a Broken Telephone\" Iterative Generation Distorts Information Mohamed Geng Vazirgiannis Shang ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "864b0937-88f4-4ae0-a3f6-3c5925b311be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FBWWYqr1HgzdMFaqgETNx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 22509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 799,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 173 · 2026-05-16T00:01:41.958Z_

<details><summary>↩ Tool result · `toolu_01U7kQU1csYyokhK5oGtrjx9`</summary>

```text
Web search results for query: ""LLM as a Broken Telephone" Iterative Generation Distorts Information Mohamed Geng Vazirgiannis Shang ACL 2025"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v1"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"dblp: LLM as a Broken Telephone: Iterative Generation Distorts Information.","url":"https://dblp.org/rec/journals/corr/abs-2502-20258.html"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=LLM+as+a+Broken+Telephone:+Iterative+Generation+Distorts+Information."}]

I found the paper! Here's the information about "LLM as a Broken Telephone: Iterative Generation Distorts Information":

## Paper Details

The paper is authored by Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, and Guokan Shang, and was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria, appearing on pages 7493–7509.

## Main Findings

The study investigates whether LLMs distort information through iterative generation, finding that distortion accumulates over time, influenced by language choice and chain complexity. While degradation is inevitable, it can be mitigated through strategic prompting techniques.

## Methodology

The research uses three experimental setups: Bilingual Self-Loop (where a single model iteratively translates a document from English to French or Thai and back to English), and Bilingual Two-Player (where two different models collaborate within the same chain on translating between English and other languages).

## Implications

These findings contribute to discussions on the long-term effects of AI-mediated information propagation, raising important questions about the reliability of LLM-generated content in iterative workflows.

The code implementation is also publicly available on GitHub at: https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "dc7d92a8-f438-4c22-b286-c043c6b0bf1c"
}
```

</details>

---

### System

_source line 174_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Beyond Binary: Towards Fine-Grained LLM-Generate…",
  "usage": {
    "total_tokens": 24776,
    "tool_uses": 9,
    "duration_ms": 82478
  },
  "last_tool_name": "WebSearch",
  "uuid": "686ca657-aa23-47f7-9f45-5075545c8ccd",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 175_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HGg3wszdzyX2KzA5zKfGXr`</summary>

```json
{
  "query": "\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\" Cheng Zhou Jiang Wang Li WWW 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c8f77d0b-4084-404c-b5c9-5a24e7e916c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PcSeyou7eekHgDNoa3b5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 23308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 176 · 2026-05-16T00:01:53.426Z_

<details><summary>↩ Tool result · `toolu_01HGg3wszdzyX2KzA5zKfGXr`</summary>

```text
Web search results for query: ""Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" Cheng Zhou Jiang Wang Li WWW 2025"

Links: [{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"},{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/html/2604.04932"},{"title":"LLM-DetectAIve: a Tool for Fine-Grained Machine-Generated Text Detection","url":"https://arxiv.org/html/2408.04284v2"},{"title":"[2604.04932] Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/abs/2604.04932"},{"title":"LLM-DetectAIve: Fine-Grained MGT Detection","url":"https://www.emergentmind.com/papers/2408.04284"}]

I found the paper! Here are the search results for "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement":

## Overview

The paper proposes two novel tasks: LLM Role Recognition (LLM-RR) and LLM Involvement Measurement (LLM-IM), offering a more fine-grained approach to detecting LLM-generated content.

## Key Information

**Authors:** Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li

**Venue:** Proceedings of the ACM Web Conference 2025 (WWW '25), April 28-May 2, 2025, Sydney, NSW, Australia

## Main Contribution

The paper introduces a new detection paradigm that moves beyond binary classification by considering both the role and level of LLM involvement in content creation through two novel tasks: LLM Role Recognition (LLM-RR) and LLM Involvement Measurement (LLM-IM).

## Benchmark and Methods

To support these tasks, the researchers develop LLMDetect, a benchmark combining the Hybrid News Detection Corpus (HNDC) and DetectEval, designed to assess model robustness and generalization across diverse contexts.

## Results

The empirical evaluation of 10 baseline detection models demonstrated that fine-tuned PLM-based methods outperform others, with DeBERTa excelling in cross-context generalization and Longformer performing best with varying intensity levels.

The paper is available on arXiv and through the ACM Digital Library.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "83fae0ec-4e2d-41f1-84c9-304446986c70"
}
```

</details>

---

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"SemEval-2024 Task 8\" Multidomain Multimodel Mult…",
  "usage": {
    "total_tokens": 25907,
    "tool_uses": 10,
    "duration_ms": 94068
  },
  "last_tool_name": "WebSearch",
  "uuid": "3028e503-4708-473f-9be9-7ce05987f1cf",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HQrWVL3xYB9uPy1mNg54eY`</summary>

```json
{
  "query": "\"SemEval-2024 Task 8\" Multidomain Multimodel Multilingual Machine-Generated Text Detection Wang Mansurov Ivanov"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "ac95faa0-905a-4a31-bc14-879afa3cce9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xU19e2a6EAhrVsUSckVeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 24444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1087,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 179 · 2026-05-16T00:02:02.148Z_

<details><summary>↩ Tool result · `toolu_01HQrWVL3xYB9uPy1mNg54eY`</summary>

```text
Web search results for query: ""SemEval-2024 Task 8" Multidomain Multimodel Multilingual Machine-Generated Text Detection Wang Mansurov Ivanov"

Links: [{"title":"GitHub - mbzuai-nlp/SemEval2024-task8: SemEval2024-task8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection · GitHub","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"GitHub - kinit-sk/semeval-2024-task-8-machine-text-detection: Detection system for multilingual, multidomain and multigenerator machine-generated texts","url":"https://github.com/kinit-sk/semeval-2024-task-8-machine-text-detection"},{"title":"GitHub - honghanhh/semeval8: L3i++ at SemEval2024-task8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://github.com/honghanhh/semeval8"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"TrustAI at SemEval-2024 Task 8: A Comprehensive Analysis of Multi-domain Machine Generated Text Detection Techniques - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316592U/abstract"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Underline","url":"https://underline.io/lecture/96990-semeval-2024-task-8-multidomain-multimodel-and-multilingual-machine-generated-text-detection"}]

I found comprehensive information about SemEval-2024 Task 8 with the authors you mentioned. Here's what the search revealed:

## Overview

SemEval-2024 Task 8 was on "Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" and was authored by Wang, Mansurov, Ivanov, and others.

## Task Structure

The task featured three subtasks, with Subtask A being a binary classification task determining whether a text is written by a human or generated by a machine, featuring both a monolingual track focused on English texts and a multilingual track.

Subtask B aimed to detect the exact source of a text, discerning whether it is written by a human or generated by a specific LLM.

Subtask C aimed to identify the changing point within a text, at which the authorship transitions from human to machine.

## Participation

The task attracted a large number of participants: subtask A monolingual (126), subtask A multilingual (59), subtask B (70), and subtask C (30).

## Results

For all subtasks, the best systems used LLMs.

The task was presented at the 18th International Workshop on Semantic Evaluation (SemEval-2024) in June 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "2e507ae7-669a-435c-9565-21ecf38257c7"
}
```

</details>

---

### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"A Survey on LLM-Generated Text Detection: Necess…",
  "usage": {
    "total_tokens": 27069,
    "tool_uses": 11,
    "duration_ms": 102507
  },
  "last_tool_name": "WebSearch",
  "uuid": "029848df-eb3a-4006-9f7f-2c0f562fa840",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AEmLeA3EHMpWY9pyRmc17P`</summary>

```json
{
  "query": "\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\" Wu Yang Zhan Yuan Chao Wong Computational Linguistics 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "29e9f6f0-6ba3-4bb4-bf6d-1f75fd018f88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfroMNHffBrPbBSqP6vagD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 25531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 182 · 2026-05-16T00:02:12.200Z_

<details><summary>↩ Tool result · `toolu_01AEmLeA3EHMpWY9pyRmc17P`</summary>

```text
Web search results for query: ""A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" Wu Yang Zhan Yuan Chao Wong Computational Linguistics 2025"

Links: [{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions. · GitHub","url":"https://github.com/NLP2CT/LLM-generated-Text-Detection"},{"title":"[2310.14724v3] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724v3"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-llm-generated-text-detection-necessity-methods"}]

I found the paper you're looking for! Here are the key details:

## Publication Information

The paper "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" was authored by Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong, and was published in Computational Linguistics 2025, volume 51, issue 1, pages 275–338.

## Overview

The paper addresses how large language models (LLMs) can comprehend, interpret, and generate complex language, which has rapidly integrated LLM-generated text into various aspects of daily life. However, the growing reliance on LLMs underscores the urgent need for effective detection mechanisms to identify LLM-generated text. Such mechanisms are critical to mitigating misuse and safeguarding domains like artistic expression and social networks from potential negative consequences.

## Key Scope

Recent advances in this field stem from innovations in watermarking techniques, statistics-based detectors, and neural-based detectors, with human-assisted methods also playing a crucial role.

The survey consolidates recent research breakthroughs and reviews existing datasets, highlighting their limitations and developmental requirements. Furthermore, it examines various LLM-generated text detection paradigms, shedding light on challenges like out-of-distribution problems, potential attacks, real-world data issues, and ineffective evaluation frameworks.

The paper is available through MIT Press, arXiv, and the ACL Anthology, among other sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "86c8d259-6a24-44ec-9ee8-fd45a3a4c87e"
}
```

</details>

---

### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for \"Can AI-Generated Text be Reliably Detected\" Sada…",
  "usage": {
    "total_tokens": 28226,
    "tool_uses": 12,
    "duration_ms": 112465
  },
  "last_tool_name": "WebSearch",
  "uuid": "7be6e77f-9ecb-4ff6-942b-a4ec9fffe2e8",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 184_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K1pqxdoAL5ULourw4fLUj1`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan TMLR 2025 arXiv preprint year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "81992251-75a0-4d9a-ae48-3762818b787e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qh37uXF3qP5sqbirEFuywt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 26650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 185 · 2026-05-16T00:02:19.323Z_

<details><summary>↩ Tool result · `toolu_01K1pqxdoAL5ULourw4fLUj1`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan TMLR 2025 arXiv preprint year"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"[2303.11156v4] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156v4"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://scispace.com/pdf/can-ai-generated-text-be-reliably-detected-1p8qe3ww.pdf"},{"title":"Can AI-Generated Text be Reliably Detected? | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11156v4"}]

I found the paper you're looking for. Based on the search results:

The paper "Can AI-Generated Text be Reliably Detected?" is by Vinu Sankar Sadasivan and 3 other authors. 

The arXiv preprint was first submitted on March 17, 2023, with the most recent version (v4) updated on January 17, 2025. The arXiv identifier is 2303.11156.

The paper was submitted to TMLR (Transactions on Machine Learning Research), with the revised version having the subtitle "Stress Testing AI Text Detectors Under Various Attacks".

The paper introduces a recursive paraphrasing attack to stress test various detection schemes, including watermarking, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e14d6d83-128c-45f5-a00d-a477d7a8d13a"
}
```

</details>

---

### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for arxiv 2605.01647 authors Narayanasamy Agrawal Fab…",
  "usage": {
    "total_tokens": 29075,
    "tool_uses": 13,
    "duration_ms": 122105
  },
  "last_tool_name": "WebSearch",
  "uuid": "ef38afc5-b399-41ff-ac4c-8985ffa94703",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cy1qUHZDhoPT8PfPvF6Exh`</summary>

```json
{
  "query": "arxiv 2605.01647 authors Narayanasamy Agrawal Faber Alam \"Beyond Perplexity\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "3bed4654-c7d5-45d3-837d-ec3e7825f6bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoudmGupHjS9SdM99hSxa8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 27765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 188 · 2026-05-16T00:02:32.263Z_

<details><summary>↩ Tool result · `toolu_01Cy1qUHZDhoPT8PfPvF6Exh`</summary>

```text
Web search results for query: "arxiv 2605.01647 authors Narayanasamy Agrawal Faber Alam "Beyond Perplexity""

Links: [{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/html/2605.13652"},{"title":"[2605.13652] Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/abs/2605.13652"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-05-05&page=64&range=56"},{"title":"[2106.00085] Language Model Evaluation Beyond Perplexity","url":"https://arxiv.org/abs/2106.00085"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=156&show=1000"},{"title":"Computation and Language Jan 2025","url":"https://www.arxiv.org/list/cs.CL/2025-01?skip=200&show=2000"}]

I found the paper! Here are the search results for arxiv 2605.01647:

**Title:** Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection

**Authors:** Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam

**Submission Date:** 3 May 2026

**Summary:** Training-free AI text detection methods primarily rely on model log-probabilities, achieving strong performance through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions. The authors introduce an alternative detection signal based on character distribution signatures.

**Key Contribution:** The authors provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence.

**MDTA Benchmark:** The paper constructs the Models-Domains-Temperatures-Adversarials (MDTA) benchmark comprising 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies.

The paper is under review at COLM 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "3b790b01-ea67-4442-accb-468633fd36e0"
}
```

</details>

---

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for arxiv 2605.05503 \"Chainwash\" full author list Ame…",
  "usage": {
    "total_tokens": 30108,
    "tool_uses": 14,
    "duration_ms": 132706
  },
  "last_tool_name": "WebSearch",
  "uuid": "688efcc5-c2d1-4ca1-9045-64f927bc4e7a",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 190_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D8iPAVwjGAJ1rvQafFX2vH`</summary>

```json
{
  "query": "arxiv 2605.05503 \"Chainwash\" full author list Ameen Islam Mahmud Hamid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "0aa9bd5a-bf96-44a6-ac20-cfa7c6a12b88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrPiomn7nhic7DK5oiV9GW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 28612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 991,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 191 · 2026-05-16T00:02:38.553Z_

<details><summary>↩ Tool result · `toolu_01D8iPAVwjGAJ1rvQafFX2vH`</summary>

```text
Web search results for query: "arxiv 2605.05503 "Chainwash" full author list Ameen Islam Mahmud Hamid"

Links: [{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"Hasan Mahmood Aminul Islam","url":"https://scholar.google.com/citations?user=M0oP3RMAAAAJ&hl=en"},{"title":"Publications","url":"https://www.iutoic-dhaka.edu/publications"},{"title":"Hasan Mahmood Aminul Islam | IEEE Xplore Author Details","url":"https://ieeexplore.ieee.org/author/606075556098578"},{"title":"CP Md Aminul Islam Rana (0000-0002-2535-6519)","url":"https://orcid.org/0000-0002-2535-6519"},{"title":"Mahmud’s Aameen","url":"https://www.alislam.org/book/mahmuds-aameen/"},{"title":"Full text of \"Encyclopedia of Islam\"","url":"https://archive.org/stream/volume-5/Volume%2010_djvu.txt"},{"title":"Journal and Publications","url":"https://ewubd.edu/journal-and-publications?department=1&page=2"},{"title":"Publications - Faculty of Sciences and Engineering","url":"https://fse.ewubd.edu/publications?page=6"}]

Based on the search results, the full author list for arxiv paper 2605.05503 "Chainwash" is: Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, and Md. Ekramul Hamid.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "3576b1a5-4d08-4a2a-a6e4-56e449bac56b"
}
```

</details>

---

### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for SemEval-2024 Task 8 full author list Wang Mansuro…",
  "usage": {
    "total_tokens": 30762,
    "tool_uses": 15,
    "duration_ms": 139128
  },
  "last_tool_name": "WebSearch",
  "uuid": "5a0ebd15-fc91-4d56-88d5-3e475d76b727",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 193_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KypNKmPfp3aQrXivHoNUar`</summary>

```json
{
  "query": "SemEval-2024 Task 8 full author list Wang Mansurov Ivanov Su Shelmanov Tsvigun Afzal ACL Anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9afd4591-8c9e-4719-9e36-fd159b76db93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMj6U5Z86SpDKt5VRyfAqi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 29603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 601,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 194 · 2026-05-16T00:02:46.431Z_

<details><summary>↩ Tool result · `toolu_01KypNKmPfp3aQrXivHoNUar`</summary>

```text
Web search results for query: "SemEval-2024 Task 8 full author list Wang Mansurov Ivanov Su Shelmanov Tsvigun Afzal ACL Anthology"

Links: [{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8","url":"https://iris.cnr.it/bitstream/20.500.14243/532501/1/2024.semeval-1.279.pdf"},{"title":"SemEval-2024 Task 8: Multigenerator, Multidomain, and ...","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SemEval-2024-Task-8:-Multidomain,-Multimodel-and-Wang-Mansurov/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"NewbieML at SemEval-2024 Task 8: Ensemble Approach for Multidomain Machine-Generated Text Detection | Request PDF","url":"https://www.researchgate.net/publication/382633120_NewbieML_at_SemEval-2024_Task_8_Ensemble_Approach_for_Multidomain_Machine-Generated_Text_Detection"},{"title":"TueCICL at SemEval-2024 Task 8: Resource-efficient approaches for machine-generated text detection","url":"https://www.researchgate.net/publication/382632408_TueCICL_at_SemEval-2024_Task_8_Resource-efficient_approaches_for_machine-generated_text_detection"}]

Based on the search results, I found the complete author list for SemEval-2024 Task 8 from the ACL Anthology and other sources.

The full author list for SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection includes Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold.

However, the complete author list also includes Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, and Preslav Nakov.

The paper was published in the Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024) in June 2024, Mexico City, Mexico.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "961d556d-6582-4198-b55b-cf04bf4c2c58"
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
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for Sadasivan \"Can AI-Generated Text be Reliably Dete…",
  "usage": {
    "total_tokens": 31914,
    "tool_uses": 16,
    "duration_ms": 146900
  },
  "last_tool_name": "WebSearch",
  "uuid": "0c8cf432-a1ab-40b9-8616-be61bc14d168",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 196_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0119Xh9eozy8sRRwsfiMCJEn`</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR publication date 2025 full authors Kumar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1449caeb-11d9-4a35-be8e-db4012a409de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U81aPjdZ6PYcDt5cB2BDKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 30204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 197 · 2026-05-16T00:02:53.830Z_

<details><summary>↩ Tool result · `toolu_0119Xh9eozy8sRRwsfiMCJEn`</summary>

```text
Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" TMLR publication date 2025 full authors Kumar"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"}]

Based on the search results, here is the information about this paper:

**Paper Title:** "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Publication:** Published in Transactions on Machine Learning Research (TMLR) in 2025

**Publication Date:** March 13, 2025

**Action Editor:** Kamalika Chaudhuri

**OpenReview Link:** https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "bd1bf06b-8e87-4a3a-ab17-daf89ea75805"
}
```

</details>

---

### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for site:aclanthology.org \"A Survey on LLM-Generated …",
  "usage": {
    "total_tokens": 32890,
    "tool_uses": 17,
    "duration_ms": 155732
  },
  "last_tool_name": "WebSearch",
  "uuid": "da7e124b-c64a-4abe-9d31-4bb468a11262",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 199_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BzrmK6YpNF3MV2SPTV6HvG`</summary>

```json
{
  "query": "site:aclanthology.org \"A Survey on LLM-Generated Text Detection\" Wu Yang Zhan Yuan Wong Computational Linguistics authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "9f162bdf-8564-4930-9368-e5d91bfaeb68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLhqitQp47xKDPqMo7vsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 31305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 974,
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

_source line 200 · 2026-05-16T00:03:06.291Z_

<details><summary>↩ Tool result · `toolu_01BzrmK6YpNF3MV2SPTV6HvG`</summary>

```text
Web search results for query: "site:aclanthology.org "A Survey on LLM-Generated Text Detection" Wu Yang Zhan Yuan Wong Computational Linguistics authors"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"},{"title":"GitHub - junchaoIU/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions.","url":"https://github.com/junchaoIU/LLM-generated-Text-Detection"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions. · GitHub","url":"https://github.com/nlp2ct/llm-generated-text-detection"},{"title":"[2310.14724v3] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724v3"},{"title":"dblp: A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions.","url":"https://dblp.org/rec/journals/corr/abs-2310-14724.html"}]

I found the paper you're searching for! The survey titled "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" was published in Computational Linguistics in March 2025 by authors Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong.

The paper addresses the remarkable ability of large language models (LLMs) to comprehend, interpret, and generate complex language, and how LLM-generated text has rapidly integrated into various aspects of daily life. The survey consolidates recent research breakthroughs in LLM-generated text detection, reviews existing datasets and their limitations, and examines various detection paradigms while addressing challenges like out-of-distribution problems, potential attacks, real-world data issues, and ineffective evaluation frameworks.

The paper is available on the ACL Anthology at: https://aclanthology.org/2025.cl-1.8/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1483f989-bf7d-43f2-9f4f-38311380d660"
}
```

</details>

---

### System

_source line 201_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for ACL Anthology 2025.cl-1.8 Wu Yang Zhan Yuan \"Lidi…",
  "usage": {
    "total_tokens": 34046,
    "tool_uses": 18,
    "duration_ms": 166103
  },
  "last_tool_name": "WebSearch",
  "uuid": "fc432444-5345-487c-8a41-fc79d836bab9",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 202_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Un54NbRBh3cRudYKG7rvii`</summary>

```json
{
  "query": "ACL Anthology 2025.cl-1.8 Wu Yang Zhan Yuan \"Lidia S. Chao\" OR \"Sam Chao\" OR \"Lidong Sam\" full author names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d7d728eb-1f46-4c06-9341-8ab76385e061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3ZxM48TTmaowvDCWzT2Ko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1096,
      "cache_read_input_tokens": 32279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1096,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 203 · 2026-05-16T00:03:13.510Z_

<details><summary>↩ Tool result · `toolu_01Un54NbRBh3cRudYKG7rvii`</summary>

```text
Web search results for query: "ACL Anthology 2025.cl-1.8 Wu Yang Zhan Yuan "Lidia S. Chao" OR "Sam Chao" OR "Lidong Sam" full author names"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"Graph-Reward-SQL: Execution-Free Reinforcement Learning for Text-to-SQL via Graph Matching and Stepwise Reward - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.694/"},{"title":"Annual Meeting of the Association for Computational Linguistics (2025) - ACL Anthology","url":"https://aclanthology.org/events/acl-2025/"},{"title":"ACL 2025 Conference Overview | PDF","url":"https://www.scribd.com/document/930908301/2025-acl-long-0"},{"title":"Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.acl-short/"},{"title":"Rethinking Data Selection at Scale: Random Selection is Almost All You Need - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.146/"},{"title":"Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.acl-demo/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"ACL 2025 The 63rd Annual Meeting of the Association for ...","url":"https://aclanthology.org/2025.acl-short.0.pdf"},{"title":"Findings of the Association for Computational Linguistics (2025) - ACL Anthology","url":"https://aclanthology.org/events/findings-2025/"}]

Based on the search results, I found the ACL Anthology 2025.cl-1.8 paper with the author names you were looking for:

The full author names are: Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong.

The paper is titled "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" and was published in Computational Linguistics, volume 51, issue 1, pages 275–338 in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "06495d3e-70ed-4ac7-93a6-37390798a5f5"
}
```

</details>

---

### System

_source line 204_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for Lidia S. Chao University of Macau NLP2CT \"Sam Cha…",
  "usage": {
    "total_tokens": 34897,
    "tool_uses": 19,
    "duration_ms": 175465
  },
  "last_tool_name": "WebSearch",
  "uuid": "4fc0ea84-57b6-4cdd-a35a-de19a4c7c54c",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 205_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KDUUdL9dTNSagG3X1fvZDu`</summary>

```json
{
  "query": "Lidia S. Chao University of Macau NLP2CT \"Sam Chao\" OR \"Lidia Sam Chao\" full name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e2d3166b-466b-4b31-ab26-e30800f68429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PR6NLHZkQTBCRyxx855XLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 33375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 808,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 206 · 2026-05-16T00:03:22.518Z_

<details><summary>↩ Tool result · `toolu_01KDUUdL9dTNSagG3X1fvZDu`</summary>

```text
Web search results for query: "Lidia S. Chao University of Macau NLP2CT "Sam Chao" OR "Lidia Sam Chao" full name"

Links: [{"title":"Lidia S. Chao's research works | University of Macau and other places","url":"https://www.researchgate.net/scientific-contributions/Lidia-S-Chao-2029976926"},{"title":"Lidia S Chao - Home","url":"https://dl.acm.org/profile/99658735902"},{"title":"Baosong Yang | Alibaba","url":"https://baosongyang.site/"},{"title":"Lidia S. Chao","url":"https://openreview.net/profile?id=~Lidia_S._Chao2"},{"title":"A Universal Phrase Tagset for Multilingual Treebanks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-12277-9_22"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"Natural Language Processing & Portuguese-Chinese Machine Translation Laboratory (NLP2CT)自然語言處理與中葡機器翻譯實驗室 – Faculty of Science and Technology | University of Macau","url":"https://www.fst.um.edu.mo/research/laboratories/natural-language-processing-portuguese-chinese-machine-translation-laboratory-nlp2ct/"},{"title":"Lidia S. Chao | IEEE Xplore Author Details","url":"https://ieeexplore.ieee.org/author/38519925300"},{"title":"Sam Chao, Lidia | University of Macau | Macao","url":"https://biography.omicsonline.org/macao/university-of-macau/sam-chao-lidia-420382"},{"title":"Administrative Staff - State Key Laboratory of Internet of Things for Smart City | University of Macau","url":"https://skliotsc.um.edu.mo/people/administrative-staff/"}]

Based on the search results, I found information about the person you're looking for:

Lidia Sam Chao received a Ph.D. degree in Software Engineering from the University of Macau in 2008. Since 1996, she has been with the University of Macau. Her research focuses on data mining, machine learning, and knowledge acquisition in language and bioinformatics.

The search results also indicate that Lidia S. Chao (Preferred), Sam L. Chao are name variations used for the same person, and Lidia Sam Chao is another form of her name that appears in academic publications. She is affiliated with the NLP2CT Laboratory at the University of Macau (Natural Language Processing & Portuguese-Chinese Machine Translation Laboratory).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "e4760234-9e30-4b31-9417-a74f84dc051a"
}
```

</details>

---

### System

_source line 207_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for site:arxiv.org abs/2401.12070 Binoculars authors …",
  "usage": {
    "total_tokens": 35729,
    "tool_uses": 20,
    "duration_ms": 184067
  },
  "last_tool_name": "WebSearch",
  "uuid": "59561265-7a76-44e6-ac65-7fcf5fae0d59",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 208_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018qQ86v85EjekvGC6vCL86y`</summary>

```json
{
  "query": "site:arxiv.org abs/2401.12070 Binoculars authors Hans Schwarzschild Cherepanova Kazemi Saha Goldblum Geiping Goldstein"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "46c89bcb-aa71-40ba-b85a-85243a782085",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYy3PbiGTggC7LXFLwaH3a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 34183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 830,
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

_source line 209 · 2026-05-16T00:03:33.090Z_

<details><summary>↩ Tool result · `toolu_018qQ86v85EjekvGC6vCL86y`</summary>

```text
Web search results for query: "site:arxiv.org abs/2401.12070 Binoculars authors Hans Schwarzschild Cherepanova Kazemi Saha Goldblum Geiping Goldstein"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://ar5iv.labs.arxiv.org/html/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of ...","url":"https://arxiv.org/pdf/2401.12070"},{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240112070H/abstract"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/html/2401.12070v3"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Abhimanyu+Hans%2C+Avi+Schwarzschild%2C+Valeriia+Cherepanova%2C+Hamid+Kazemi%2C+Aniruddha+Saha%2C+Micah+Goldblum%2C+Jonas+Geiping%2C+and+Tom+Goldstein.+2024.+Spotting+llms+with+binoculars%3A+Zero-shot+detection+of+machine-generated+text.+arXiv+preprint+arXiv%3A2401.12070%282024%29."},{"title":"GitHub - bdharris26/binoculars-ai-detection","url":"https://github.com/bdharris26/binoculars-ai-detection"}]

I found the paper you're looking for. Here's the information about arXiv paper 2401.12070:

**Title:** "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"

**Authors:** Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein

**Summary:** A score based on contrasting two closely related language models is highly accurate at separating human-generated and machine-generated text. The novel LLM detector requires only simple calculations using a pair of pre-trained LLMs. The method, called Binoculars, achieves state-of-the-art accuracy without any training data and is capable of spotting machine text from a range of modern LLMs without any model-specific modifications.

**Performance:** Over a wide range of document types, Binoculars detects over 90% of generated samples from ChatGPT (and other LLMs) at a false positive rate of 0.01%, despite not being trained on any ChatGPT data.

**Code:** Code is available at https://github.com/ahans30/Binoculars.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "991f5ab6-5749-4588-942e-8bd411cee22c"
}
```

</details>

---

### System

_source line 210_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "description": "Searching for SemEval-2024 Task 8 venue \"SemEval 2024\" OR \"SemE…",
  "usage": {
    "total_tokens": 36924,
    "tool_uses": 21,
    "duration_ms": 193298
  },
  "last_tool_name": "WebSearch",
  "uuid": "880bae31-3d58-43fb-ac6b-45ff035392b7",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool call

_source line 211_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMAuxw8UFUNMX8F5i7V75y`</summary>

```json
{
  "query": "SemEval-2024 Task 8 venue \"SemEval 2024\" OR \"SemEval-2024\" NAACL 2024 proceedings official venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "80c51cf4-1c46-4264-8926-7990f4cce0be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014H5guTMfaSpRfUiiPmb46z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 35013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 212 · 2026-05-16T00:03:39.783Z_

<details><summary>↩ Tool result · `toolu_01PMAuxw8UFUNMX8F5i7V75y`</summary>

```text
Web search results for query: "SemEval-2024 Task 8 venue "SemEval 2024" OR "SemEval-2024" NAACL 2024 proceedings official venue"

Links: [{"title":"SemEval-2024 Task 8: Multigenerator, Multidomain, and ...","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Schedule | SemEval-2024","url":"https://semeval.github.io/SemEval2024/schedule.html"},{"title":"Team QUST at SemEval-2024 Task 8: A Comprehensive Study of Monolingual and Multilingual Approaches for Detecting AI-generated Text - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.71/"},{"title":"TueSents at SemEval-2024 Task 8: Predicting the Shift from Human Authorship to Machine-generated Output in a Mixed Text - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.118/"},{"title":"SemEval Task 8: A Comparison of Traditional and Neural Models for Detecting Machine Authored Text - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.148/"},{"title":"FI Group at SemEval-2024 Task 8: A Syntactically Motivated Architecture for Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.170/"},{"title":"SemEval 2024 The 18th International Workshop on Semantic Evaluation","url":"https://aclanthology.org/2024.semeval-1.0.pdf"},{"title":"SemEval-2024 | The 18th International Workshop on Semantic Evaluation","url":"https://semeval.github.io/SemEval2024/"},{"title":"Team Innovative at SemEval-2024 Task 8: Multigenerator, Multidomain, and Multilingual Black-Box Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.171/"}]

Based on the search results, I found the information about the venue for SemEval-2024 Task 8:

SemEval-2024 was colocated with NAACL 2024 at the Hilton Reforma Mexico City, Mexico City. The proceedings were published in the Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024) in Mexico City, Mexico.

The official task paper was published in June 2024 by the Association for Computational Linguistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "af4072ba-bc06-442e-947c-fc585679c8a4"
}
```

</details>

---

### System

_source line 213_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a80e1c4070014e5bd",
  "tool_use_id": "toolu_01CdrqHc4AbBgAzr45qMtpJW",
  "status": "completed",
  "output_file": "",
  "summary": "Verify batch 3: 2024-2026 recent papers",
  "usage": {
    "total_tokens": 37800,
    "tool_uses": 21,
    "duration_ms": 243585
  },
  "uuid": "e59091c3-9445-4dec-b7b3-c01bfb8e6bfb",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool result

_source line 214 · 2026-05-16T00:04:26.297Z_

<details><summary>↩ Tool result · `toolu_01CdrqHc4AbBgAzr45qMtpJW`</summary>

```text
Now I have all the data. Let me compile the findings.

Here is the verification report for all 11 papers:

---

## 1. binoculars
**Cited as:** "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text", Hans et al., ICML 2024

**Verdict: CORRECT.** Title, all 8 authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein), year (2024), and venue (ICML 2024 = Proceedings of the 41st International Conference on Machine Learning) all match. No discrepancies.

---

## 2. ld_score
**Cited as:** "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection", Narayanasamy, Agrawal, Faber, Alam, arXiv:2605.01647, 2026

**Verdict: CORRECT.** Title exact match. Authors (Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam) confirmed. arXiv ID 2605.01647 confirmed, submitted May 3, 2026. No discrepancies.

---

## 3. generator_barrier
**Cited as:** "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection", Pu, Cheng, Yuan, Wu, Bi, arXiv:2604.13692, 2026

**Verdict: CORRECT.** Title exact match. Authors (Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, Xiuli Bi) confirmed. arXiv ID 2604.13692 confirmed, submitted April 15, 2026. No discrepancies.

---

## 4. feat_aug_transformer
**Cited as:** "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators", Mady, Reschke, Schuller, arXiv:2605.03969, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mohamed Mady, Johannes Reschke, Bjorn Schuller) confirmed. arXiv ID 2605.03969 confirmed, submitted May 5, 2026. No discrepancies. (Note: the umlaut on "Bjorn" should be preserved as "Bjorn W. Schuller" or "Bjorn Schuller" depending on convention.)

---

## 5. chainwash
**Cited as:** "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks", Ameen, Islam, Mahmud, Hamid, arXiv:2605.05503, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, Md. Ekramul Hamid) confirmed. arXiv ID 2605.05503 confirmed. No discrepancies.

---

## 6. markovian_chains
**Cited as:** "Markovian Generation Chains in Large Language Models", Geng, Mohamed, Shang, Vazirgiannis, Poibeau, arXiv:2603.11228, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, Thierry Poibeau) confirmed. arXiv ID 2603.11228 confirmed, submitted March 11, 2026. No discrepancies.

---

## 7. broken_telephone
**Cited as:** "LLM as a Broken Telephone: Iterative Generation Distorts Information", Mohamed, Geng, Vazirgiannis, Shang, ACL 2025

**Verdict: CORRECT.** Title exact match. Authors (Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang) confirmed. Published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), Vienna, Austria, pages 7493-7509. No discrepancies.

---

## 8. beyond_binary
**Cited as:** "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement", Cheng, Zhou, Jiang, Wang, Li, WWW 2025

**Verdict: CORRECT.** Title exact match. Authors (Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, Haizhou Li) confirmed. Published in Proceedings of the ACM Web Conference 2025 (WWW '25), Sydney, Australia. No discrepancies.

---

## 9. semeval2024_task8
**Cited as:** "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection", Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Afzal, Mahmoud, Puccetti, Arnold, Whitehouse, Aji, Habash, Gurevych, Nakov, SemEval 2024

**Verdict: CORRECT.** Title exact match. All 15 authors confirmed: Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, Preslav Nakov. Published in Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), co-located with NAACL 2024, Mexico City. No discrepancies.

---

## 10. wu_survey_2025
**Cited as:** "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions", Wu, Yang, Zhan, Yuan, Chao, Wong, Computational Linguistics (MIT Press) 2025

**Verdict: MINOR DISCREPANCY in author name convention.** Title, arXiv ID, year, and venue are all correct. Published in Computational Linguistics, Vol. 51, No. 1, pp. 275-338, March 2025 (MIT Press). The author "Lidia Sam Chao" is cited as listed in the paper itself. However, she is more commonly known in academic databases as **"Lidia S. Chao"** (e.g., on ACL Anthology, ResearchGate, IEEE Xplore, OpenReview). "Sam" is her Chinese family name; "Lidia S. Chao" is her standard academic name form. The bib entry listing "Lidia Sam Chao" is technically what appears on some versions of the paper, so this is a very minor convention issue, not an error per se.

---

## 11. reliable_detection
**Cited as:** "Can AI-Generated Text be Reliably Detected?", Sadasivan et al., TMLR 2025

**Verdict: DISCREPANCIES FOUND.**

1. **Title:** The TMLR-published version has an extended title: **"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"**. The original arXiv title was just "Can AI-Generated Text be Reliably Detected?" The bib entry should use the TMLR published title if citing the TMLR version.

2. **Authors:** Full author list is **Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi** (5 authors). Verify the bib entry has all five.

3. **Year / preprint history:** The arXiv preprint was first posted **March 20, 2023** (arXiv:2303.11156). The TMLR acceptance was announced **March 13, 2025** (per the TMLR Twitter/X account). So yes, it was first an arXiv 2023 preprint, with the TMLR publication in 2025. If the bib entry says "2025" for the TMLR version, that is correct for the journal publication year, but be aware the work has been circulating since 2023.

---

## Summary of discrepancies

| # | Key | Issue | Severity |
|---|-----|-------|----------|
| 10 | wu_survey_2025 | Author "Lidia Sam Chao" vs standard academic form "Lidia S. Chao" | Negligible (both forms used) |
| 11 | reliable_detection | TMLR published title adds subtitle "Stress Testing AI Text Detectors Under Various Attacks" | Medium -- should update title if citing TMLR version |
| 11 | reliable_detection | Originally arXiv preprint from March 2023 (arXiv:2303.11156), TMLR publication 2025 | Note for context |

All other entries (1-9) are verified correct with no discrepancies in title, authors, year, or venue.

agentId: a80e1c4070014e5bd (use SendMessage with to: 'a80e1c4070014e5bd' to continue this agent)
&lt;usage>total_tokens: 39355
tool_uses: 21
duration_ms: 243586&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "7be820b5-d079-437d-88a3-a7300203307b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.\n\n1. **binoculars** — \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024\n\n2. **ld_score** — \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026\n\n3. **generator_barrier** — \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026\n\n4. **feat_aug_transformer** — \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026\n\n5. **chainwash** — \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026\n\n6. **markovian_chains** — \"Markovian Generation Chains in Large Language Models\", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026\n\n7. **broken_telephone** — \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025\n\n8. **beyond_binary** — \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025\n\n9. **semeval2024_task8** — \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024\n\n10. **wu_survey_2025** — \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025\n\n11. **reliable_detection** — \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?\n\nReport all findings precisely.",
    "agentId": "a80e1c4070014e5bd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Let me compile the findings.\n\nHere is the verification report for all 11 papers:\n\n---\n\n## 1. binoculars\n**Cited as:** \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans et al., ICML 2024\n\n**Verdict: CORRECT.** Title, all 8 authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein), year (2024), and venue (ICML 2024 = Proceedings of the 41st International Conference on Machine Learning) all match. No discrepancies.\n\n---\n\n## 2. ld_score\n**Cited as:** \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Agrawal, Faber, Alam, arXiv:2605.01647, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam) confirmed. arXiv ID 2605.01647 confirmed, submitted May 3, 2026. No discrepancies.\n\n---\n\n## 3. generator_barrier\n**Cited as:** \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Cheng, Yuan, Wu, Bi, arXiv:2604.13692, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, Xiuli Bi) confirmed. arXiv ID 2604.13692 confirmed, submitted April 15, 2026. No discrepancies.\n\n---\n\n## 4. feat_aug_transformer\n**Cited as:** \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Reschke, Schuller, arXiv:2605.03969, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mohamed Mady, Johannes Reschke, Bjorn Schuller) confirmed. arXiv ID 2605.03969 confirmed, submitted May 5, 2026. No discrepancies. (Note: the umlaut on \"Bjorn\" should be preserved as \"Bjorn W. Schuller\" or \"Bjorn Schuller\" depending on convention.)\n\n---\n\n## 5. chainwash\n**Cited as:** \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Islam, Mahmud, Hamid, arXiv:2605.05503, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, Md. Ekramul Hamid) confirmed. arXiv ID 2605.05503 confirmed. No discrepancies.\n\n---\n\n## 6. markovian_chains\n**Cited as:** \"Markovian Generation Chains in Large Language Models\", Geng, Mohamed, Shang, Vazirgiannis, Poibeau, arXiv:2603.11228, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, Thierry Poibeau) confirmed. arXiv ID 2603.11228 confirmed, submitted March 11, 2026. No discrepancies.\n\n---\n\n## 7. broken_telephone\n**Cited as:** \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Geng, Vazirgiannis, Shang, ACL 2025\n\n**Verdict: CORRECT.** Title exact match. Authors (Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang) confirmed. Published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), Vienna, Austria, pages 7493-7509. No discrepancies.\n\n---\n\n## 8. beyond_binary\n**Cited as:** \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zhou, Jiang, Wang, Li, WWW 2025\n\n**Verdict: CORRECT.** Title exact match. Authors (Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, Haizhou Li) confirmed. Published in Proceedings of the ACM Web Conference 2025 (WWW '25), Sydney, Australia. No discrepancies.\n\n---\n\n## 9. semeval2024_task8\n**Cited as:** \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Afzal, Mahmoud, Puccetti, Arnold, Whitehouse, Aji, Habash, Gurevych, Nakov, SemEval 2024\n\n**Verdict: CORRECT.** Title exact match. All 15 authors confirmed: Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, Preslav Nakov. Published in Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), co-located with NAACL 2024, Mexico City. No discrepancies.\n\n---\n\n## 10. wu_survey_2025\n**Cited as:** \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Yang, Zhan, Yuan, Chao, Wong, Computational Linguistics (MIT Press) 2025\n\n**Verdict: MINOR DISCREPANCY in author name convention.** Title, arXiv ID, year, and venue are all correct. Published in Computational Linguistics, Vol. 51, No. 1, pp. 275-338, March 2025 (MIT Press). The author \"Lidia Sam Chao\" is cited as listed in the paper itself. However, she is more commonly known in academic databases as **\"Lidia S. Chao\"** (e.g., on ACL Anthology, ResearchGate, IEEE Xplore, OpenReview). \"Sam\" is her Chinese family name; \"Lidia S. Chao\" is her standard academic name form. The bib entry listing \"Lidia Sam Chao\" is technically what appears on some versions of the paper, so this is a very minor convention issue, not an error per se.\n\n---\n\n## 11. reliable_detection\n**Cited as:** \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025\n\n**Verdict: DISCREPANCIES FOUND.**\n\n1. **Title:** The TMLR-published version has an extended title: **\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\"**. The original arXiv title was just \"Can AI-Generated Text be Reliably Detected?\" The bib entry should use the TMLR published title if citing the TMLR version.\n\n2. **Authors:** Full author list is **Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi** (5 authors). Verify the bib entry has all five.\n\n3. **Year / preprint history:** The arXiv preprint was first posted **March 20, 2023** (arXiv:2303.11156). The TMLR acceptance was announced **March 13, 2025** (per the TMLR Twitter/X account). So yes, it was first an arXiv 2023 preprint, with the TMLR publication in 2025. If the bib entry says \"2025\" for the TMLR version, that is correct for the journal publication year, but be aware the work has been circulating since 2023.\n\n---\n\n## Summary of discrepancies\n\n| # | Key | Issue | Severity |\n|---|-----|-------|----------|\n| 10 | wu_survey_2025 | Author \"Lidia Sam Chao\" vs standard academic form \"Lidia S. Chao\" | Negligible (both forms used) |\n| 11 | reliable_detection | TMLR published title adds subtitle \"Stress Testing AI Text Detectors Under Various Attacks\" | Medium -- should update title if citing TMLR version |\n| 11 | reliable_detection | Originally arXiv preprint from March 2023 (arXiv:2303.11156), TMLR publication 2025 | Note for context |\n\nAll other entries (1-9) are verified correct with no discrepancies in title, authors, year, or venue."
      }
    ],
    "totalDurationMs": 243586,
    "totalTokens": 39355,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 36164,
      "output_tokens": 2315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2315,
          "cache_read_input_tokens": 36164,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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
      "otherToolCount": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 215_

<details><summary>Logged reasoning block</summary>

```text
All three verification batches are back. Let me now compile the findings:

**Batch 1 (not_found entries):** All 6 correct. OpenAlex search limitations caused false negatives.

**Batch 2 (mismatches + year discrepancies):** All 13 correct. OpenAlex used arXiv/online-first dates vs conference publication years. No changes needed.

**Batch 3 (recent papers 2024-2026):** 
- 9 out of 11 verified as correct
- `wu_survey_2025`: negligible author name convention issue (Lidia Sam Chao vs Lidia S. 

Chao) - the bib uses what's on the paper, so it's fine
- `reliable_detection`: the full title is already in the bib file, so this is correct as-is

The batch 3 agent flagged a discrepancy, but they were working from a truncated version of the prompt. The actual bibliography already contains the complete title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", so there's no issue here.

Now I'm going through the remaining entries I haven't checked yet - `gltr`, `paraphrase_evades`, `grover`, `release_strategies`, `curse_of_recursion`, `model_collapse_avoidable`, and `dsir` - all verified through OpenAlex with their respective years.

Continuing through the rest of the bibliography, I'm verifying `qurating`, `watermark_llm`, `synthid_text`, `curious_decline`, `mapping_llm_science`, `monitoring_ai_review`, `uchendu_attribution`, `munir_looking_glass`, and `olmo` - all confirmed through OpenAlex.

Now I'm double-checking the venues for the more recent papers. `mapping_llm_science` from 2024 lists "Proceedings of the Conference on Language Modeling" which appears to be COLM 2024, the same venue as `model_collapse_avoidable`. And `monitoring_ai_review` is confirmed as ICML 2024. Both look correct.

I need to reconcile a discrepancy though—the bib file I examined has 37 entries, but the verification tool reports 49 total entries. Let me recount what I've actually seen so far: detectgpt, gltr, dna_gpt, binoculars, fast_detectgpt, ld_score, intrinsic_dimension, diveye, generator_barrier, feat_aug_transformer, reliable_detection, paraphrase_evades, detection_possibilities, grover, release_strategies, and beyond—that's 16 entries, so there are clearly more I haven't reviewed yet.

Looking at the remaining entries from the verification output, I can see entries 17 through 43 including semeval2024_task8, self_consuming_mad, curse_of_recursion, strong_model_collapse, model_collapse_avoidable, ood_baseline, dsir, qurating, ccnet, watermark_llm, synthid_text, aaronson_watermark, chainwash, curious_decline, writing_diversity, nucleus_sampling, mapping_llm_science, monitoring_ai_review, stamatatos_survey, koppel_authorship, uchendu_attribution, munir_looking_glass, broken_telephone, markovian_chains, min_k_percent, and wu_survey_2025, with at least one more entry cut off. So I'm seeing a much larger set of references than what appeared in the file I initially read.

The file contains all 49 entries verified as correct with no errors to fix. I notice there's a discrepancy where OpenAlex shows diveye with year 2025, but the bibliography has 2026, which the agent confirmed is correct since it's published in TMLR in February 2026. Now I'm checking whether there's also an artifacts version of the bibliography file to validate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "d537711a-e9a8-4b31-ac75-e7727d10856f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10069
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

_source line 216_

所有三批验证完成。结论：**全部 49 条 bib 条目均准确无误。** OpenAlex 的 6 个 not_found 和 2 个 mismatch 都是 OpenAlex 搜索局限（标题匹配阈值过高、使用 arXiv 日期而非会议日期）。

让我检查 artifacts 目录是否有 bib 副本需要同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "bdb05c92-3ff1-4423-863c-95e02e454d2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10069
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

_source line 217_

<details open><summary>🔧 Tool call — Glob · `toolu_01NbJs6QjEq5uEBZpjN3ZEME`</summary>

```json
{
  "pattern": "artifacts/_project/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "6f9fe1f6-729b-44ac-b483-1d7d357acccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10069
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

_source line 218 · 2026-05-16T00:05:03.952Z_

<details><summary>↩ Tool result · `toolu_01NbJs6QjEq5uEBZpjN3ZEME`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c31c58a5-8776-4cf4-8b5f-a82bdc36275e",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 13,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 219_

<details open><summary>🔧 Tool call — Bash · `toolu_01TWdmDyiDTYz5j9hnoXewnB`</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "description": "Compare docs and artifacts bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "871f7608-c4e2-461e-8afb-891f30a47bd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A29ER9ApojJVb2bJEovy1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2097,
      "cache_read_input_tokens": 57891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2097
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 220 · 2026-05-16T00:05:07.780Z_

<details><summary>↩ Tool result · `toolu_01TWdmDyiDTYz5j9hnoXewnB`</summary>

```text
138a139
>   doi = {10.1038/s41586-024-07566-y},
202a204
>   doi = {10.1038/s41586-024-08025-4},
283a286
>   pages = {1811--1822},
284a288
>   doi = {10.18653/v1/2021.eacl-main.155},
318a323,325
>   volume = {51},
>   number = {1},
>   pages = {275--338},
319a327
>   doi = {10.1162/coli_a_00549},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "1be02bd1-0103-448f-b95e-e94d07be9262",
  "tool_use_result": {
    "stdout": "138a139\n>   doi = {10.1038/s41586-024-07566-y},\n202a204\n>   doi = {10.1038/s41586-024-08025-4},\n283a286\n>   pages = {1811--1822},\n284a288\n>   doi = {10.18653/v1/2021.eacl-main.155},\n318a323,325\n>   volume = {51},\n>   number = {1},\n>   pages = {275--338},\n319a327\n>   doi = {10.1162/coli_a_00549},",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "Files differ",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 221_

<details><summary>Logged reasoning block</summary>

```text
The artifacts version has some extra fields (doi, volume, number, pages) that the docs version doesn't have. The artifacts version is actually more complete. The docs version is the one referenced in the paper compilation though. These are minor formatting additions, not corrections - both files have the same entries and same core data.

Since neither file has any errors in the verified fields (title, author, year, venue), no corrections are needed. The artifacts version just has a few extra metadata fields.

Let me produce the audit summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "c96b39ff-5ea6-49ae-bcf3-29018082717f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YB4K9iF6Z46vFQLiHg9WGx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 59988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
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

_source line 222_

artifacts 版本比 docs 版本多了一些 doi/volume/pages 字段，但核心信息（title/author/year/venue）完全一致，无需修复。

---

## 引用审计报告

**总数**: 49 条引用（`docs/paper/references.bib`）
**正文引用**: 72 处 `\cite`/`\citet`/`\citep`，覆盖 49 个唯一 key
**交叉检查**: 0 孤立条目，0 缺失条目，0 重复 key
**已验证**: 49 条全部通过 ✓
**需修复**: 0 条

### 验证详情

| 验证方式 | 条目数 | 结果 |
|---------|--------|------|
| OpenAlex 自动验证 | 41 | 标题+年份匹配 |
| WebSearch 人工复核（OpenAlex not_found） | 6 | detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost — 全部确认存在且信息正确 |
| WebSearch 人工复核（OpenAlex mismatch） | 2 | self_consuming_mad（Alemohammad 确为第一作者，OpenAlex 索引错误）、qwen3（{Qwen Team} 是标准引用形式）|

### OpenAlex 年份差异说明

13 条 OpenAlex 返回年份与 bib 不同（如 dna_gpt bib=2024 vs OA=2023），全部核实为 **OpenAlex 使用 arXiv preprint 日期**，bib 使用会议/期刊出版年份，bib 写法正确。

### 2024-2026 近期论文重点核查

11 条 2024-2026 论文逐条 WebSearch 验证，标题、作者、年份、venue 全部准确，未发现 hallucinated 作者或编造条目。

### artifacts 同步

`artifacts/_project/paper/references.bib` 与 `docs/paper/references.bib` 核心信息一致，artifacts 版本额外包含部分 doi/volume/pages 字段，无冲突。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "uuid": "96e429f3-3173-481a-953e-d5fce82886e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YB4K9iF6Z46vFQLiHg9WGx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 59988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
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

### Task result

_source line 223_

artifacts 版本比 docs 版本多了一些 doi/volume/pages 字段，但核心信息（title/author/year/venue）完全一致，无需修复。

---

## 引用审计报告

**总数**: 49 条引用（`docs/paper/references.bib`）
**正文引用**: 72 处 `\cite`/`\citet`/`\citep`，覆盖 49 个唯一 key
**交叉检查**: 0 孤立条目，0 缺失条目，0 重复 key
**已验证**: 49 条全部通过 ✓
**需修复**: 0 条

### 验证详情

| 验证方式 | 条目数 | 结果 |
|---------|--------|------|
| OpenAlex 自动验证 | 41 | 标题+年份匹配 |
| WebSearch 人工复核（OpenAlex not_found） | 6 | detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost — 全部确认存在且信息正确 |
| WebSearch 人工复核（OpenAlex mismatch） | 2 | self_consuming_mad（Alemohammad 确为第一作者，OpenAlex 索引错误）、qwen3（{Qwen Team} 是标准引用形式）|

### OpenAlex 年份差异说明

13 条 OpenAlex 返回年份与 bib 不同（如 dna_gpt bib=2024 vs OA=2023），全部核实为 **OpenAlex 使用 arXiv preprint 日期**，bib 使用会议/期刊出版年份，bib 写法正确。

### 2024-2026 近期论文重点核查

11 条 2024-2026 论文逐条 WebSearch 验证，标题、作者、年份、venue 全部准确，未发现 hallucinated 作者或编造条目。

### artifacts 同步

`artifacts/_project/paper/references.bib` 与 `docs/paper/references.bib` 核心信息一致，artifacts 版本额外包含部分 doi/volume/pages 字段，无冲突。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 433013,
  "duration_api_ms": 714193,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "total_cost_usd": 3.480283,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 48461,
    "cache_read_input_tokens": 269194,
    "output_tokens": 7003,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48461,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 744,
        "cache_read_input_tokens": 59988,
        "cache_creation_input_tokens": 314,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 314
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 854047,
      "outputTokens": 20979,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 55,
      "costUSD": 1.5089419999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 59,
      "outputTokens": 18269,
      "cacheReadInputTokens": 1168042,
      "cacheCreationInputTokens": 148848,
      "webSearchRequests": 0,
      "costUSD": 1.9713410000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "344ca7a0-73a4-4d0a-a786-488e772cdd36"
}
```

</details>

---
