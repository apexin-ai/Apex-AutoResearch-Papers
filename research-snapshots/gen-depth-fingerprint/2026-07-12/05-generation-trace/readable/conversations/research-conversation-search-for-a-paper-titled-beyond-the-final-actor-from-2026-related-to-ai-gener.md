# Research conversation: Search for a paper titled "Beyond the Final Actor" from 2026, related to AI-generated text detection or iterative/recurs

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a986658dcb8f7ee5b.jsonl`
- **Structured JSON:** [`ef574ac8a24ef362ef78.json`](../../sessions/ef/ef574ac8a24ef362ef78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-19T00:56:07.733Z_

Search for a paper titled "Beyond the Final Actor" from 2026, related to AI-generated text detection or iterative/recursive LLM generation. I need:
1. Full title
2. Authors
3. Venue and year  
4. What it does
5. How it relates to generation depth classification

Search in the bib file at /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib for any existing entry, and also search the literature map at /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "a986658dcb8f7ee5b",
  "type": "user",
  "uuid": "9c13b51d-c1d4-403c-9393-83850f0263cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T00:56:08.925Z_

I'll search for information about the "Beyond the Final Actor" paper in both the bibliography and literature map files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c13b51d-c1d4-403c-9393-83850f0263cd",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xmZTPjT8fRWcPru6f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af5c653f-fb22-474e-a430-4a70c5f476f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFjaneBEBMutypcWuu2myj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 26729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T00:56:09.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E9fM41KsEVwr81Waivjucg`</summary>

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
  "parentUuid": "af5c653f-fb22-474e-a430-4a70c5f476f8",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xmZTPjT8fRWcPru6f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a556b5d9-788a-4a7d-98d7-1123815eda06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFjaneBEBMutypcWuu2myj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 26729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T00:56:09.151Z_

<details><summary>↩ Tool result · `toolu_01E9fM41KsEVwr81Waivjucg`</summary>

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
155	% ===== Fine-tuning =====
156	
157	@inproceedings{qlora,
158	  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},
159	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
160	  booktitle = {Advances in Neural Information Processing Systems},
161	  year = {2023},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{fineweb,
167	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
168	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
169	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
170	  year = {2024},
171	}
172	
173	@inproceedings{dolma,
174	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
175	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
176	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
177	  year = {2024},
178	}
179	
180	@inproceedings{dsir,
181	  title = {{Data Selection for Language Models via Importance Resampling}},
182	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
183	  booktitle = {Advances in Neural Information Processing Systems},
184	  year = {2023},
185	}
186	
187	@inproceedings{qurating,
188	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
189	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
190	  booktitle = {Proceedings of the International Conference on Machine Learning},
191	  year = {2024},
192	}
193	
194	@inproceedings{ccnet,
195	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
196	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
197	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
198	  year = {2020},
199	}
200	
201	% ===== Watermarking =====
202	
203	@inproceedings{watermark_llm,
204	  title = {{A Watermark for Large Language Models}},
205	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
206	  booktitle = {Proceedings of the International Conference on Machine Learning},
207	  year = {2023},
208	}
209	
210	@article{synthid_text,
211	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
212	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
213	  journal = {Nature},
214	  volume = {634},
215	  pages = {818--823},
216	  year = {2024},
217	}
218	
219	@misc{aaronson_watermark,
220	  title = {{Watermarking GPT Outputs}},
221	  author = {Aaronson, Scott and Kirchner, Hendrik},
222	  year = {2022},
223	  howpublished = {Technical Talk},
224	  url = {https://scottaaronson.blog/?p=6823},
225	}
226	
227	@article{chainwash,
228	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
229	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
230	  journal = {arXiv preprint arXiv:2605.05503},
231	  year = {2026},
232	}
233	
234	% ===== Vocabulary Diversity =====
235	
236	@inproceedings{curious_decline,
237	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
238	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
239	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
240	  year = {2024},
241	}
242	
243	@inproceedings{writing_diversity,
244	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
245	  author = {Padmakumar, Vishakh and He, He},
246	  booktitle = {Proceedings of the International Conference on Learning Representations},
247	  year = {2024},
248	}
249	
250	@inproceedings{nucleus_sampling,
251	  title = {{The Curious Case of Neural Text Degeneration}},
252	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
253	  booktitle = {Proceedings of the International Conference on Learning Representations},
254	  year = {2020},
255	}
256	
257	@inproceedings{mapping_llm_science,
258	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
259	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
260	  booktitle = {Proceedings of the Conference on Language Modeling},
261	  year = {2024},
262	}
263	
264	@inproceedings{monitoring_ai_review,
265	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
266	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
267	  booktitle = {Proceedings of the International Conference on Machine Learning},
268	  year = {2024},
269	}
270	
271	% ===== Stylometry =====
272	
273	@article{stamatatos_survey,
274	  title = {{A Survey of Modern Authorship Attribution Methods}},
275	  author = {Stamatatos, Efstathios},
276	  journal = {Journal of the American Society for Information Science and Technology},
277	  year = {2009},
278	}
279	
280	@article{koppel_authorship,
281	  title = {{Computational Methods in Authorship Attribution}},
282	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
283	  journal = {Journal of the American Society for Information Science and Technology},
284	  year = {2009},
285	}
286	
287	@inproceedings{uchendu_attribution,
288	  title = {{Authorship Attribution for Neural Text Generation}},
289	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
290	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
291	  year = {2020},
292	}
293	
294	@inproceedings{munir_looking_glass,
295	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
296	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
297	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
298	  year = {2021},
299	}
300	
301	% ===== Iterative Generation =====
302	
303	@inproceedings{broken_telephone,
304	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
305	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
306	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
307	  year = {2025},
308	}
309	
310	@article{markovian_chains,
311	  title = {{Markovian Generation Chains in Large Language Models}},
312	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
313	  journal = {arXiv preprint arXiv:2603.11228},
314	  year = {2026},
315	}
316	
317	@inproceedings{self_refine,
318	  title = {{Self-Refine: Iterative Refinement with Self-Feedback}},
319	  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	  year = {2023},
322	}
323	
324	% ===== Membership Inference =====
325	
326	@inproceedings{min_k_percent,
327	  title = {{Detecting Pretraining Data from Large Language Models}},
328	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
329	  booktitle = {Proceedings of the International Conference on Learning Representations},
330	  year = {2024},
331	}
332	
333	% ===== Survey =====
334	
335	@article{wu_survey_2025,
336	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
337	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
338	  journal = {Computational Linguistics},
339	  publisher = {MIT Press},
340	  year = {2025},
341	}
342	
343	@inproceedings{jawahar_survey,
344	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
345	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
346	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
347	  year = {2020},
348	}
349	
350	% ===== Models =====
351	
352	@inproceedings{pythia,
353	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
354	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
355	  booktitle = {Proceedings of the International Conference on Machine Learning},
356	  year = {2023},
357	}
358	
359	@inproceedings{olmo,
360	  title = {{OLMo: Accelerating the Science of Language Models}},
361	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
362	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
363	  year = {2024},
364	}
365	
366	@article{qwen3,
367	  title = {{Qwen3 Technical Report}},
368	  author = {{Qwen Team}},
369	  journal = {arXiv preprint arXiv:2505.09388},
370	  year = {2025},
371	}
372	
373	@inproceedings{ghostbuster,
374	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
375	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Jurafsky, Dan},
376	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
377	  year = {2024},
378	}
379	
380	@inproceedings{radar,
381	  title = {{RADAR: Robust AI-Text Detection via Adversarial Learning}},
382	  author = {Hu, Xiaomeng and Chen, Pin-Yu and Ho, Tsung-Yi},
383	  booktitle = {Advances in Neural Information Processing Systems},
384	  year = {2023},
385	}
386	
387	% ===== Machine Learning =====
388	
389	@article{gutierrez_ordinal_survey,
390	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
391	  author = {Guti{\'e}rrez, Pedro Antonio and Perez-Ortiz, Maria and Sanchez-Monedero, Javier and Fernandez-Navarro, Francisco and Hervas-Martinez, Cesar},
392	  journal = {IEEE Transactions on Knowledge and Data Engineering},
393	  volume = {28},
394	  number = {1},
395	  pages = {127--146},
396	  year = {2016},
397	}
398	
399	@article{coral_ordinal,
400	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
401	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
402	  journal = {Pattern Recognition Letters},
403	  volume = {140},
404	  pages = {325--331},
405	  year = {2020},
406	}
407	
408	@inproceedings{frank_hall_ordinal,
409	  title = {{A Simple Approach to Ordinal Classification}},
410	  author = {Frank, Eibe and Hall, Mark},
411	  booktitle = {Proceedings of the European Conference on Machine Learning},
412	  year = {2001},
413	}
414	
415	@inproceedings{xgboost,
416	  title = {{XGBoost: A Scalable Tree Boosting System}},
417	  author = {Chen, Tianqi and Guestrin, Carlos},
418	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
419	  year = {2016},
420	}
421	
422	@article{lakens_equivalence,
423	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
424	  author = {Lakens, Dani{\"e}l},
425	  journal = {Social Psychological and Personality Science},
426	  volume = {8},
427	  number = {4},
428	  pages = {355--362},
429	  year = {2017},
430	}
431	
432	% ===== Generator Model References =====
433	
434	@article{llama3,
435	  title = {{The Llama 3 Herd of Models}},
436	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
437	  journal = {arXiv preprint arXiv:2407.21783},
438	  year = {2024},
439	}
440	
441	@article{mistral7b,
442	  title = {{Mistral 7B}},
443	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
444	  journal = {arXiv preprint arXiv:2310.06825},
445	  year = {2023},
446	}
447	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a556b5d9-788a-4a7d-98d7-1123815eda06",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "a986658dcb8f7ee5b",
  "type": "user",
  "uuid": "deddb35e-919d-4fcb-83a0-ecd27103893e",
  "sourceToolAssistantUUID": "a556b5d9-788a-4a7d-98d7-1123815eda06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T00:56:09.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KM8LMJYoLP2tx5CUjEgc5Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deddb35e-919d-4fcb-83a0-ecd27103893e",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xmZTPjT8fRWcPru6f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "947364b4-2fa0-4394-ba2b-aada3f2e2edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFjaneBEBMutypcWuu2myj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 26729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T00:56:09.356Z_

<details><summary>↩ Tool result · `toolu_01KM8LMJYoLP2tx5CUjEgc5Z`</summary>

```text
1	# Literature Map for gen-depth-fingerprint
2	# 递归 LLM 生成链深度指纹识别
3	# Updated: 2026-05-15
4	# Categories: detection, model-collapse, data-quality, stylometry,
5	#             iterative-generation, watermarking, vocabulary-diversity,
6	#             membership-inference, ood-detection, survey
7	# Total: 39 papers
8	
9	##############################################################################
10	# 1. Perplexity-based / Zero-shot Detection
11	##############################################################################
12	
13	- id: detectgpt
14	  title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
15	  authors: "Mitchell et al."
16	  year: 2023
17	  venue: "ICML 2023"
18	  arxiv: "2301.11305"
19	  category: detection
20	  role: background
21	  relevance: "基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补"
22	  key_finding: "机器生成文本倾向于占据模型 log-probability 函数的负曲率区域"
23	
24	- id: gltr
25	  title: "GLTR: Statistical Detection and Visualization of Generated Text"
26	  authors: "Gehrmann et al."
27	  year: 2019
28	  venue: "ACL 2019"
29	  arxiv: "1906.04043"
30	  category: detection
31	  role: background
32	  relevance: "早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化"
33	  key_finding: "使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%"
34	
35	- id: dna_gpt
36	  title: "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text"
37	  authors: "Yang et al."
38	  year: 2024
39	  venue: "ICLR 2024"
40	  arxiv: "2305.17359"
41	  category: detection
42	  role: background
43	  relevance: "通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析"
44	  key_finding: "截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测"
45	
46	- id: binoculars
47	  title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
48	  authors: "Hans et al."
49	  year: 2024
50	  venue: "ICML 2024"
51	  arxiv: "2401.12070"
52	  category: detection
53	  role: background
54	  relevance: "双模型对比打分检测法；depth fingerprint 需要验证与 Binoculars score 在不同深度下的相关性"
55	  key_finding: "对比两个近似 LLM 的 perplexity 比值可在 0.01% FPR 下检测 90%+ 的 ChatGPT 输出"
56	
57	- id: fast_detectgpt
58	  title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
59	  authors: "Bao et al."
60	  year: 2024
61	  venue: "ICLR 2024"
62	  arxiv: "2310.05130"
63	  category: detection
64	  role: background
65	  relevance: "DetectGPT 加速版，用采样替代扰动；可作为 depth fingerprint pipeline 中的快速 baseline"
66	  key_finding: "用条件概率曲率替代扰动步骤，检测速度提升 340 倍，性能相对提升 75%"
67	
68	- id: ld_score
69	  title: "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection"
70	  authors: "Narayanasamy et al."
71	  year: 2026
72	  venue: "arXiv preprint"
73	  arxiv: "2605.01647"
74	  category: detection
75	  role: method-component
76	  relevance: "字符级分布特征 (LD-Score) 与 perplexity 正交（r=0.08-0.13）；可作为 depth fingerprint 的互补信号"
77	  key_finding: "LLM 近似全局字符分布而人类展示领域特化分布，形成可检测的 Wall of Separation"
78	
79	- id: intrinsic_dimension
80	  title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
81	  authors: "Tulchinskii et al."
82	  year: 2023
83	  venue: "NeurIPS 2023"
84	  arxiv: "2306.04723"
85	  category: detection
86	  role: method-component
87	  relevance: "用嵌入空间内在维度做检测；depth fingerprint 可探索内在维度随生成深度的变化趋势"
88	  key_finding: "人类文本嵌入的内在维度约 9（字母语言），AI 文本约低 1.5；跨域/跨模型稳定"
89	
90	- id: diveye
91	  title: "Diversity Boosts AI-Generated Text Detection"
92	  authors: "Basani & Chen"
93	  year: 2026
94	  venue: "TMLR 2026"
95	  arxiv: "2509.18880"
96	  category: detection
97	  role: method-component
98	  relevance: "用 surprisal diversity 特征检测 AI 文本——人类文本 surprisal 分布离散度更高、尾部更重；与本项目 shape 特征（entropy_std, tail_decay）直接可比"
99	  key_finding: "DivEye 框架捕捉 token surprisal 的波动模式，zero-shot 检测超现有方法最多 33.2%，对改写鲁棒"
100	
101	- id: generator_barrier
102	  title: "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection"
103	  authors: "Pu et al."
104	  year: 2026
105	  venue: "arXiv preprint"
106	  arxiv: "2604.13692"
107	  category: detection
108	  role: background
109	  relevance: "通过解耦表征实现跨生成器泛化检测（MAGE 20 个 LLM），与本项目 LOGO 跨生成器评估目标一致；不同方法论（表征学习 vs 特征工程）"
110	  key_finding: "解耦 AI 检测语义与生成器特有伪影，在未见生成器上准确率提升 24.2%、F1 提升 26.2%"
111	
112	- id: feat_aug_transformer
113	  title: "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators"
114	  authors: "Mady et al."
115	  year: 2026
116	  venue: "arXiv preprint"
117	  arxiv: "2605.03969"
118	  category: detection
119	  role: background
120	  relevance: "语言特征增强 Transformer 做跨域/跨生成器检测（DeBERTa+FeatAttn 85.9% bal-acc on M4）；验证了语言特征对泛化性的价值，支撑本项目特征工程路线"
121	  key_finding: "基模型域内近满分但迁移脆弱；attention-based 语言特征融合显著提升跨分布迁移能力"
122	
123	##############################################################################
124	# 2. Model Collapse Theory
125	##############################################################################
126	
127	- id: self_consuming_mad
128	  title: "Self-Consuming Generative Models Go MAD"
129	  authors: "Alemohammad et al."
130	  year: 2023
131	  venue: "arXiv preprint"
132	  arxiv: "2307.01850"
133	  category: model-collapse
134	  role: background
135	  relevance: "定义 autophagous loop 三种模式并证明精度/多样性递减；本项目的 depth fingerprint 可量化此递减"
136	  key_finding: "无足够新鲜真实数据时，自噬循环导致生成质量（精度）或多样性（召回）逐步下降"
137	
138	- id: curse_of_recursion
139	  title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
140	  authors: "Shumailov et al."
141	  year: 2024
142	  venue: "Nature 2024"
143	  arxiv: "2305.17493"
144	  category: model-collapse
145	  role: background
146	  relevance: "Nature 发表的 model collapse 里程碑论文；本项目关注推理链（非训练循环）的类似退化现象"
147	  key_finding: "递归训练导致不可逆缺陷——原始分布的尾部消失，在 VAE/GMM/LLM 中普遍存在"
148	
149	- id: strong_model_collapse
150	  title: "Strong Model Collapse"
151	  authors: "Dohmatob et al."
152	  year: 2024
153	  venue: "ICLR 2025"
154	  arxiv: "2410.04840"
155	  category: model-collapse
156	  role: background
157	  relevance: "证明即使 1% 合成数据也会导致 collapse，更大模型可能放大效应；支撑 depth fingerprint 的理论动机"
158	  key_finding: "最小比例合成数据即可导致 strong collapse；更大模型在简化体制下可放大此效应"
159	
160	- id: model_collapse_avoidable
161	  title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
162	  authors: "Gerstgrasser et al."
163	  year: 2024
164	  venue: "arXiv preprint"
165	  arxiv: "2404.01413"
166	  category: model-collapse
167	  role: background
168	  relevance: "证明累积数据时 collapse 可避免；本项目的生成链场景是纯推理无累积，collapse 更难避免"
169	  key_finding: "当数据累积而非替换时，混合真实与合成数据可避免 model collapse"
170	
171	##############################################################################
172	# 3. OOD Detection
173	##############################################################################
174	
175	- id: ood_baseline
176	  title: "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks"
177	  authors: "Hendrycks & Gimpel"
178	  year: 2017
179	  venue: "ICLR 2017"
180	  arxiv: "1610.02136"
181	  category: ood-detection
182	  role: background
183	  relevance: "OOD 检测基线方法；depth fingerprint 可视为 OOD scoring 的一种特殊形式——检测偏离人类分布的程度"
184	  key_finding: "正确分类样本的最大 softmax 概率高于错误分类和 OOD 样本"
185	
186	##############################################################################
187	# 4. Data Quality Scoring
188	##############################################################################
189	
190	- id: dsir
191	  title: "Data Selection for Language Models via Importance Resampling"
192	  authors: "Xie et al."
193	  year: 2023
194	  venue: "NeurIPS 2023"
195	  arxiv: "2302.03169"
196	  category: data-quality
197	  role: background
198	  relevance: "数据质量筛选框架；depth fingerprint 可作为 DSIR 类 pipeline 中合成数据污染度的质量信号"
199	  key_finding: "用 n-gram 特征空间的重要性权重做数据选择，100M 文档 4.5 小时处理"
200	
201	- id: qurating
202	  title: "QuRating: Selecting High-Quality Data for Training Language Models"
203	  authors: "Wettig et al."
204	  year: 2024
205	  venue: "ICML 2024"
206	  arxiv: "2402.09739"
207	  category: data-quality
208	  role: background
209	  relevance: "LLM 成对判断的数据质量评分；depth fingerprint 类似地为文本分配生成深度分数"
210	  key_finding: "LLM 可准确判断文本的写作风格/专业性/教育价值等质量维度，用于预训练数据选择"
211	
212	- id: ccnet
213	  title: "CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data"
214	  authors: "Wenzek et al."
215	  year: 2020
216	  venue: "LREC 2020"
217	  arxiv: "1911.00359"
218	  category: data-quality
219	  role: background
220	  relevance: "基于 perplexity 的 web 数据过滤 pipeline；depth fingerprint 可集成为额外的质量过滤维度"
221	  key_finding: "用语言模型 perplexity 过滤 Common Crawl 数据，接近维基百科质量水平"
222	
223	##############################################################################
224	# 5. Watermarking
225	##############################################################################
226	
227	- id: watermark_llm
228	  title: "A Watermark for Large Language Models"
229	  authors: "Kirchenbauer et al."
230	  year: 2023
231	  venue: "ICML 2023"
232	  arxiv: "2301.10226"
233	  category: watermarking
234	  role: background
235	  relevance: "绿色 token 列表 watermark 方案；depth fingerprint 检测非水印场景下的生成痕迹，形成互补"
236	  key_finding: "通过在采样前划分 green/red token 列表实现不可见水印，短文本即可检测"
237	
238	- id: synthid_text
239	  title: "Scalable Watermarking for Identifying Large Language Model Outputs"
240	  authors: "Dathathri et al."
241	  year: 2024
242	  venue: "Nature 2024"
243	  arxiv: ""
244	  category: watermarking
245	  role: background
246	  relevance: "生产级 LLM 水印方案（Google Gemini 部署）；depth fingerprint 面向无水印的 post-hoc 检测"
247	  key_finding: "Tournament Sampling 算法实现生产级文本水印，Google Gemini 实际部署"
248	
249	- id: aaronson_watermark
250	  title: "Watermarking GPT Outputs"
251	  authors: "Aaronson & Kirchner"
252	  year: 2022
253	  venue: "Technical Talk"
254	  arxiv: ""
255	  category: watermarking
256	  role: background
257	  relevance: "LLM 文本水印的原始提案；depth fingerprint 定位为不依赖水印的被动检测方案"
258	  key_finding: "用伪随机函数选择 next token，对短文本即可检测，对轻微编辑鲁棒"
259	
260	- id: chainwash
261	  title: "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks"
262	  authors: "Ameen et al."
263	  year: 2026
264	  venue: "arXiv preprint"
265	  arxiv: "2605.05503"
266	  category: watermarking
267	  role: background
268	  relevance: "多步重写链攻击水印（5 hop 后检测率从 87.9% 降到 4.86%）；证明生成链深度影响水印信号，支撑 depth fingerprint 的动机——被动检测不依赖水印"
269	  key_finding: "链式重写（chainwash）通过生成式多步改写有效消除扩散语言模型水印，5 步后 94.76% 原可检测文本不再被标记"
270	
271	##############################################################################
272	# 6. Vocabulary Diversity
273	##############################################################################
274	
275	- id: curious_decline
276	  title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
277	  authors: "Guo et al."
278	  year: 2024
279	  venue: "NAACL 2024 Findings"
280	  arxiv: "2311.09807"
281	  category: vocabulary-diversity
282	  role: direct-competitor
283	  relevance: "直接相关：量化递归微调导致的词汇/句法/语义多样性下降；本项目扩展到推理链场景"
284	  key_finding: "递归微调导致词汇/句法/语义多样性持续下降，创意任务尤为显著"
285	
286	- id: writing_diversity
287	  title: "Does Writing with Language Models Reduce Content Diversity?"
288	  authors: "Padmakumar & He"
289	  year: 2024
290	  venue: "ICLR 2024"
291	  arxiv: "2309.05196"
292	  category: vocabulary-diversity
293	  role: background
294	  relevance: "实验证明 InstructGPT 协写降低多样性；支撑 depth fingerprint 中 diversity 随深度递减的假设"
295	  key_finding: "InstructGPT 协写显著降低不同作者间的文本相似度和词汇多样性"
296	
297	- id: nucleus_sampling
298	  title: "The Curious Case of Neural Text Degeneration"
299	  authors: "Holtzman et al."
300	  year: 2020
301	  venue: "ICLR 2020"
302	  arxiv: "1904.09751"
303	  category: vocabulary-diversity
304	  role: background
305	  relevance: "定义了 neural text degeneration 和 nucleus sampling；depth fingerprint 中的 shape 特征与采样策略相关"
306	  key_finding: "最大化解码导致退化；Nucleus Sampling 截断不可靠尾部，生成质量接近人类"
307	
308	- id: mapping_llm_science
309	  title: "Mapping the Increasing Use of LLMs in Scientific Papers"
310	  authors: "Liang et al."
311	  year: 2024
312	  venue: "arXiv preprint"
313	  arxiv: "2404.01268"
314	  category: vocabulary-diversity
315	  role: background
316	  relevance: "大规模量化科学论文中 LLM 修改内容的比例；depth fingerprint 可检测多轮修改的深度"
317	  key_finding: "95 万篇论文分析显示 CS 领域 LLM 修改率最高达 17.5%"
318	
319	- id: monitoring_ai_review
320	  title: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews"
321	  authors: "Liang et al."
322	  year: 2024
323	  venue: "ICML 2024"
324	  arxiv: "2403.07183"
325	  category: vocabulary-diversity
326	  role: background
327	  relevance: "检测同行评审中 LLM 修改内容；depth fingerprint 提供互补的深度维度信号"
328	  key_finding: "6.5-16.9% 的 AI 会议 peer review 可能被 LLM 实质性修改"
329	
330	##############################################################################
331	# 7. Stylometry / Authorship Attribution
332	##############################################################################
333	
334	- id: stamatatos_survey
335	  title: "A Survey of Modern Authorship Attribution Methods"
336	  authors: "Stamatatos"
337	  year: 2009
338	  venue: "JASIST 2009"
339	  arxiv: ""
340	  category: stylometry
341	  role: background
342	  relevance: "风格计量学经典综述；depth fingerprint 的特征工程可借鉴 stylometric 特征体系"
343	  key_finding: "综述词汇/字符/句法等多层次文体特征在作者归属中的应用"
344	
345	- id: koppel_authorship
346	  title: "Computational Methods in Authorship Attribution"
347	  authors: "Koppel et al."
348	  year: 2009
349	  venue: "JASIST 2009"
350	  arxiv: ""
351	  category: stylometry
352	  role: background
353	  relevance: "开放集作者归属方法；depth fingerprint 可视为 LLM 生成深度的归属问题"
354	  key_finding: "解决大规模候选集和开放集场景下的作者归属问题"
355	
356	- id: uchendu_attribution
357	  title: "Authorship Attribution for Neural Text Generation"
358	  authors: "Uchendu et al."
359	  year: 2020
360	  venue: "EMNLP 2020"
361	  arxiv: ""
362	  category: stylometry
363	  role: background
364	  relevance: "将作者归属扩展到 neural text 生成源识别；depth fingerprint 进一步细化到生成深度维度"
365	  key_finding: "可区分不同神经文本生成器的多类归属，超越二分类人/机检测"
366	
367	##############################################################################
368	# 8. Iterative Generation
369	##############################################################################
370	
371	- id: broken_telephone
372	  title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
373	  authors: "Mohamed et al."
374	  year: 2025
375	  venue: "ACL 2025"
376	  arxiv: "2502.20258"
377	  category: iterative-generation
378	  role: direct-competitor
379	  relevance: "最直接相关：通过翻译链研究 LLM 迭代生成的信息失真；本项目扩展到非改写式生成链"
380	  key_finding: "LLM 迭代翻译链中失真随深度累积，语言相似度和提示策略影响退化速率"
381	
382	- id: markovian_chains
383	  title: "Markovian Generation Chains in Large Language Models"
384	  authors: "Geng et al."
385	  year: 2026
386	  venue: "arXiv preprint"
387	  arxiv: "2603.11228"
388	  category: iterative-generation
389	  role: direct-competitor
390	  relevance: "定义 Markovian generation chains 并研究收敛/发散行为；本项目关注非改写链的 depth fingerprint"
391	  key_finding: "迭代重述/翻译中输出或收敛到小循环集，或继续产生新句子，取决于温度和初始输入"
392	
393	##############################################################################
394	# 9. Membership Inference
395	##############################################################################
396	
397	- id: min_k_percent
398	  title: "Detecting Pretraining Data from Large Language Models"
399	  authors: "Shi et al."
400	  year: 2024
401	  venue: "ICLR 2024"
402	  arxiv: "2310.16789"
403	  category: membership-inference
404	  role: method-component
405	  relevance: "Min-K% 用最低概率 token 做成员推断；depth fingerprint 可借鉴其概率分布分析思路"
406	  key_finding: "未见过的文本更可能包含低概率离群 token；Min-K% Prob 在 WikiMIA 上提升 7.4%"
407	
408	##############################################################################
409	# 10. Robustness / Adversarial / Theoretical
410	##############################################################################
411	
412	- id: reliable_detection
413	  title: "Can AI-Generated Text be Reliably Detected?"
414	  authors: "Sadasivan et al."
415	  year: 2024
416	  venue: "ICLR 2024"
417	  arxiv: "2303.11156"
418	  category: detection
419	  role: background
420	  relevance: "递归改写攻击显著降低检测率；depth fingerprint 面向非改写链，攻击面不同"
421	  key_finding: "递归改写可将 DetectGPT 从 70.3% 降到 4.6%；检测上界与分布 TV 距离相关"
422	
423	- id: paraphrase_evades
424	  title: "Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense"
425	  authors: "Krishna et al."
426	  year: 2023
427	  venue: "NeurIPS 2023"
428	  arxiv: "2303.13408"
429	  category: detection
430	  role: background
431	  relevance: "改写攻击 vs 检索防御；depth fingerprint 检测非改写链，与此正交但需考虑改写鲁棒性"
432	  key_finding: "DIPPER 改写器将 DetectGPT 准确率从 70.3% 降到 4.6%；检索方法是有效防御"
433	
434	- id: detection_possibilities
435	  title: "Position: On the Possibilities of AI-Generated Text Detection"
436	  authors: "Chakraborty et al."
437	  year: 2024
438	  venue: "ICML 2024"
439	  arxiv: "2304.04736"
440	  category: detection
441	  role: background
442	  relevance: "理论证明 AI 文本检测在分布可区分时始终可行；支撑 depth fingerprint 的可行性"
443	  key_finding: "信息论证明：除非人/机分布完全不可分，检测始终可行；给出样本复杂度下界"
444	
445	##############################################################################
446	# 11. Surveys / Early Detection
447	##############################################################################
448	
449	- id: jawahar_survey
450	  title: "Automatic Detection of Machine Generated Text: A Critical Survey"
451	  authors: "Jawahar et al."
452	  year: 2020
453	  venue: "COLING 2020"
454	  arxiv: "2011.01314"
455	  category: survey
456	  role: background
457	  relevance: "机器文本检测早期综述；depth fingerprint 定位在该领域的新维度"
458	  key_finding: "系统梳理统计方法和神经方法在机器文本检测中的应用与局限"
459	
460	- id: grover
461	  title: "Defending Against Neural Fake News"
462	  authors: "Zellers et al."
463	  year: 2019
464	  venue: "NeurIPS 2019"
465	  arxiv: "1905.12616"
466	  category: detection
467	  role: background
468	  relevance: "生成器即最佳检测器的早期发现；depth fingerprint 不依赖生成器 access"
469	  key_finding: "Grover 自身是检测 Grover 生成假新闻的最佳检测器（92% vs 73% baseline）"
470	
471	- id: release_strategies
472	  title: "Release Strategies and the Social Impacts of Language Models"
473	  authors: "Solaiman et al."
474	  year: 2019
475	  venue: "arXiv preprint"
476	  arxiv: "1908.09203"
477	  category: detection
478	  role: background
479	  relevance: "GPT-2 分阶段发布策略和检测工具；depth fingerprint 面向更复杂的生成链场景"
480	  key_finding: "分阶段发布 GPT-2 允许在模型升级间进行风险/收益分析和检测器开发"
481	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "947364b4-2fa0-4394-ba2b-aada3f2e2edc",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "a986658dcb8f7ee5b",
  "type": "user",
  "uuid": "526bdaf0-c8e3-47c4-bf1b-73b778c6e7b6",
  "sourceToolAssistantUUID": "947364b4-2fa0-4394-ba2b-aada3f2e2edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T00:56:09.778Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vo9owcCsj4bvpkryJdm1cF`</summary>

```json
{
  "pattern": "Beyond the Final Actor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "526bdaf0-c8e3-47c4-bf1b-73b778c6e7b6",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xmZTPjT8fRWcPru6f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0924e3e-d2f1-4ec0-975a-ff0207c65388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFjaneBEBMutypcWuu2myj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 26729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T00:56:09.809Z_

<details><summary>↩ Tool result · `toolu_01Vo9owcCsj4bvpkryJdm1cF`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0924e3e-d2f1-4ec0-975a-ff0207c65388",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "a986658dcb8f7ee5b",
  "type": "user",
  "uuid": "5e14d67d-0896-42a3-907e-087cdd52ad79",
  "sourceToolAssistantUUID": "f0924e3e-d2f1-4ec0-975a-ff0207c65388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T00:56:10.236Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01L335Un5vW577NeeR1rR5Zd`</summary>

```json
{
  "pattern": "Beyond the Final Actor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e14d67d-0896-42a3-907e-087cdd52ad79",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xmZTPjT8fRWcPru6f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0298a816-9e3c-44bc-a8bb-b7d7737c4120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HFjaneBEBMutypcWuu2myj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 26729,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 582
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 399,
          "cache_read_input_tokens": 26729,
          "cache_creation_input_tokens": 582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 582,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T00:56:10.250Z_

<details><summary>↩ Tool result · `toolu_01L335Un5vW577NeeR1rR5Zd`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0298a816-9e3c-44bc-a8bb-b7d7737c4120",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "a986658dcb8f7ee5b",
  "type": "user",
  "uuid": "b13b06eb-abd2-43e6-9aab-242e93871302",
  "sourceToolAssistantUUID": "0298a816-9e3c-44bc-a8bb-b7d7737c4120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T00:56:16.559Z_

The "Beyond the Final Actor" paper from 2026 does **not appear to exist** in either the bibliography or literature map files. My search returned no matches.

## Search Results Summary

**In `/docs/paper/references.bib`**: No entry found for "Beyond the Final Actor"

**In `literature_map.yaml`**: No entry found for "Beyond the Final Actor"

The files I searched contain:
- **references.bib**: 39 papers covering detection methods, model collapse, data quality, watermarking, vocabulary diversity, stylometry, iterative generation, membership inference, and machine learning methods
- **literature_map.yaml**: 39 categorized papers with detailed relevance assessments for the gen-depth-fingerprint project

## Possible Next Steps

1. **Check if the paper title is different** - It might be listed under an alternative title
2. **Search related papers on similar topics** - The literature map includes relevant papers on:
   - **Iterative generation**: "LLM as a Broken Telephone: Iterative Generation Distorts Information" (Mohamed et al., ACL 2025)
   - **Markovian chains**: "Markovian Generation Chains in Large Language Models" (Geng et al., 2026)
   - **Vocabulary diversity**: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" (Guo et al., NAACL 2024)

3. **Search in other locations** - The paper might be referenced in:
   - Project memory files
   - Roadmap or ideas documents
   - Other configuration files

Would you like me to search for this paper under different names or search other project files?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b13b06eb-abd2-43e6-9aab-242e93871302",
  "isSidechain": true,
  "agentId": "a986658dcb8f7ee5b",
  "requestId": "req_011CbB1xxdi8qrqpjBKeCYPX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c439e84-5a94-4a8a-bde9-570ccf0202f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EYKUNueDmF1NGCTnctKxTk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 27311,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 389,
          "cache_read_input_tokens": 27311,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17933,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
