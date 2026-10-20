# Research conversation: Search for "Beyond Binary" by Cheng et al. at WWW 2025 — it's about multi-class AI text detection (role recognition in h

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aaa655adf37a64747.jsonl`
- **Structured JSON:** [`a63bb7bee5a56eefebb1.json`](../../sessions/a6/a63bb7bee5a56eefebb1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-19T00:56:03.198Z_

Search for "Beyond Binary" by Cheng et al. at WWW 2025 — it's about multi-class AI text detection (role recognition in human-LLM collaboration). I need to know:
1. Full title
2. Authors
3. Venue and year
4. What exactly it does (multi-class roles? what classes?)
5. How it differs from generation depth classification

Check the bib file at /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib for the existing `beyond_binary` entry first, then search the web if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "aaa655adf37a64747",
  "type": "user",
  "uuid": "6112f202-a7ba-42b3-9f98-901fb378c5f9",
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

_source line 2 · 2026-05-19T00:56:07.686Z_

I'll search for the "Beyond Binary" paper by checking the bib file first, then the web if needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6112f202-a7ba-42b3-9f98-901fb378c5f9",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xSVVKwjRdBCG4nr9j",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35bcf36b-1af6-4fc0-8fe5-4a3ecc65522f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSwEjxNvPV8Gf2JNFDN7Vt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27300,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27300,
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

_source line 3 · 2026-05-19T00:56:07.904Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UUGfjm3Nh5QTiBvfvFULCp`</summary>

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
  "parentUuid": "35bcf36b-1af6-4fc0-8fe5-4a3ecc65522f",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xSVVKwjRdBCG4nr9j",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1be3182a-e5c5-44fe-94f9-8025d3d12653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSwEjxNvPV8Gf2JNFDN7Vt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27300,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27300,
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

_source line 4 · 2026-05-19T00:56:07.911Z_

<details><summary>↩ Tool result · `toolu_01UUGfjm3Nh5QTiBvfvFULCp`</summary>

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
  "parentUuid": "1be3182a-e5c5-44fe-94f9-8025d3d12653",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "aaa655adf37a64747",
  "type": "user",
  "uuid": "a01e3a30-cfa7-405a-8b2e-2dfc4b0b5092",
  "sourceToolAssistantUUID": "1be3182a-e5c5-44fe-94f9-8025d3d12653",
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

_source line 5 · 2026-05-19T00:56:08.161Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Sn5cTwaM97JYgX34q49fqP`</summary>

```json
{
  "pattern": "beyond_binary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a01e3a30-cfa7-405a-8b2e-2dfc4b0b5092",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xSVVKwjRdBCG4nr9j",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b969682-9e92-42e6-9e76-ba66f5dfad61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSwEjxNvPV8Gf2JNFDN7Vt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27300,
      "cache_read_input_tokens": 0,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 199,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27300,
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

_source line 6 · 2026-05-19T00:56:08.179Z_

<details><summary>↩ Tool result · `toolu_01Sn5cTwaM97JYgX34q49fqP`</summary>

```text
Found 4 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b969682-9e92-42e6-9e76-ba66f5dfad61",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "aaa655adf37a64747",
  "type": "user",
  "uuid": "290227c4-d333-41bd-a8f8-74977c91a0a0",
  "sourceToolAssistantUUID": "6b969682-9e92-42e6-9e76-ba66f5dfad61",
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

_source line 7 · 2026-05-19T00:56:09.798Z_

Perfect! I found the entry in the bib file. Let me search the paper to see how it's being used and get more context about what this paper does.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "290227c4-d333-41bd-a8f8-74977c91a0a0",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xoQpuLg1WbL2pT1nU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40ec9343-a515-4ac6-8c8d-1deb6cf13a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012y5CKP61WLC3NFo6gep9Sf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9724,
      "cache_read_input_tokens": 27300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9724,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 8 · 2026-05-19T00:56:10.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_015azQZ6mXQ1AtiZmGrcPK2J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ec9343-a515-4ac6-8c8d-1deb6cf13a53",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xoQpuLg1WbL2pT1nU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e117ea2b-514f-48ee-a9ab-3f5b0824f8b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012y5CKP61WLC3NFo6gep9Sf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9724,
      "cache_read_input_tokens": 27300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9724,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 9 · 2026-05-19T00:56:10.126Z_

<details><summary>↩ Tool result · `toolu_015azQZ6mXQ1AtiZmGrcPK2J`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
12	Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
13	Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
14	This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO evaluation decouples generator identity from depth.
15	
16	\subsection{Model Collapse and Iterative Generation}
17	\label{sec:related-collapse}
18	
19	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad}, and model collapse is inevitable without fresh human data \cite{curse_of_recursion}, though careful data mixing can mitigate this \cite{model_collapse_avoidable,strong_model_collapse}.
20	These studies focus on \emph{training-loop} degradation; our setting studies \emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.
21	Iterative self-refinement \cite{self_refine} represents another form of recursive LLM processing, but targets output improvement through feedback loops rather than open-ended continuation; the distributional drift we study arises specifically from unconstrained recursive generation.
22	
23	Two concurrent works are most directly relevant.
24	\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss.
25	\citet{markovian_chains} demonstrate that semantic-preservation constraints induce attractor dynamics bounding distinguishable depth to approximately three classes; their analysis focuses on characterizing convergence behavior through model-based perplexity tracking.
26	We differ in three respects: (i) we study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal; (ii) we use handcrafted features rather than model-internal representations, enabling the DDR decomposition into drifting vs.\ stationary components; and (iii) we focus on \emph{classifying} depth from text rather than characterizing the convergence dynamics of the generation process.
27	
28	That both works independently converge on approximately three distinguishable classes reflects different mechanisms reaching the same practical ceiling.
29	\citet{markovian_chains} derive this bound from Markovian attractor dynamics: semantic-preservation constraints create fixed points where successive outputs become indistinguishable under model-internal perplexity.
30	We observe the same bound empirically through feature-space compression: inter-class KS statistics drop sharply after depth 2 (gen-1$\rightarrow$gen-2: KS\,=\,0.28 vs.\ gen-2$\rightarrow$gen-3: KS\,=\,0.09 for entropy mean), collapsing discriminative margins.
31	The approaches are complementary: their theoretical framework explains \emph{why} convergence occurs (attractor dynamics in semantic space), while our DDR decomposition reveals \emph{what} converges (location properties) versus what shows an order-of-magnitude smaller effect (shape features), providing an empirical signature that can be exploited for detection without access to model internals.
32	
33	\subsection{Vocabulary Diversity and Stylometry}
34	\label{sec:related-diversity}
35	
36	Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
37	Our surface features (TTR and hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship} that we apply to inference chains, showing monotonic diversity decline across depths without model retraining.
38	We push beyond generator identity \cite{uchendu_attribution} to the \emph{depth} dimension, and show that diversity declines monotonically even under top-$p$ sampling \cite{nucleus_sampling}.
39	
40	\subsection{Data Quality and Provenance}
41	\label{sec:related-provenance}
42	
43	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth is a complementary provenance signal characterizing \emph{how many steps removed} text is from a human source.
44	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns, but watermark strength decays across multi-step chains \cite{chainwash}, motivating passive post-hoc methods like ours.
45	At the feature level, our NLL analysis connects to \citet{min_k_percent}, who use the probability tail for membership inference; we analyze the full NLL distribution for generation depth classification.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e117ea2b-514f-48ee-a9ab-3f5b0824f8b4",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "aaa655adf37a64747",
  "type": "user",
  "uuid": "71d67ff2-d9e3-453a-89b2-00ff82931b0d",
  "sourceToolAssistantUUID": "e117ea2b-514f-48ee-a9ab-3f5b0824f8b4",
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

_source line 10 · 2026-05-19T00:56:10.800Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GTQoe7A1koCGEgkyKfS92P`</summary>

```json
{
  "pattern": "beyond_binary|Cheng.*Zhou.*Jiang",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71d67ff2-d9e3-453a-89b2-00ff82931b0d",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xoQpuLg1WbL2pT1nU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "babcf2c4-f2b3-4353-b807-a250b53568e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012y5CKP61WLC3NFo6gep9Sf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9724,
      "cache_read_input_tokens": 27300,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9724
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 256,
          "cache_read_input_tokens": 27300,
          "cache_creation_input_tokens": 9724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9724,
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

_source line 11 · 2026-05-19T00:56:10.821Z_

<details><summary>↩ Tool result · `toolu_01GTQoe7A1koCGEgkyKfS92P`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-5-\label{sec:related-detection}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-7-Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-8-Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-9-A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex:10:Recent multi-class extensions (role recognition in human-LLM collaboration \cite{beyond_binary}, multi-generator attribution \cite{semeval2024_task8}) discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-11-Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (binary F1 from 0.52 to 0.71; Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-12-Adversarial training approaches (e.g., RADAR \cite{radar}) improve robustness to paraphrasing but remain binary detectors without depth awareness.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-13-Our contribution is not a new detection method but the task formulation (generation depth classification, framed within the broader ordinal classification literature \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-14-This is orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}, which identifies \emph{which} model generated text; our LOGO evaluation decouples generator identity from depth.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-15-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-63-Tianqi Chen and Carlos Guestrin. 2016.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-64-\newblock {XGBoost: A Scalable Tree Boosting System}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-65-\newblock In \emph{Proceedings of the ACM SIGKDD International Conference on
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-66-  Knowledge Discovery and Data Mining}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-67-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl:68:\bibitem[{Cheng et~al.(2025)Cheng, Zhou, Jiang, Wang, and Li}]{beyond_binary}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl:69:Zihao Cheng, Li~Zhou, Feng Jiang, Benyou Wang, and Haizhou Li. 2025.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-70-\newblock {Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-71-  Role Recognition and Involvement Measurement}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-72-\newblock In \emph{Proceedings of the ACM Web Conference}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-73-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.bbl-74-\bibitem[{Dathathri et~al.(2024)Dathathri, See, Ghaisas, Huang, McAdam, Welbl,
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-104-  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-105-  journal = {arXiv preprint arXiv:1908.09203},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-106-  year = {2019},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-107-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-108-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib:109:@inproceedings{beyond_binary,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-110-  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib:111:  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-112-  booktitle = {Proceedings of the ACM Web Conference},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-113-  year = {2025},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-114-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-115-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-116-@inproceedings{semeval2024_task8,
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-101-\citation{intrinsic_dimension}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-102-\citation{diveye}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-103-\citation{generator_barrier}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-104-\citation{wu_survey_2025}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-105-\citation{jawahar_survey}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux:106:\citation{beyond_binary}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-107-\citation{semeval2024_task8}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-108-\citation{paraphrase_evades,detection_possibilities}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-109-\citation{radar}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-110-\citation{gutierrez_ordinal_survey,coral_ordinal}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-111-\citation{uchendu_attribution,munir_looking_glass}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-893-\bibcite{diveye}{{5}{2026}{{Basani and Chen}}{{}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-894-\bibcite{pythia}{{6}{2023}{{Biderman et~al.}}{{Biderman, Schoelkopf, Anthony, Bradley, O'Brien, Hallahan, Khan, Purohit, Prashanth, Raff, Skowron, Sutawika, and {van der Wal}}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-895-\bibcite{coral_ordinal}{{7}{2020}{{Cao et~al.}}{{Cao, Mirjalili, and Raschka}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-896-\bibcite{detection_possibilities}{{8}{2024}{{Chakraborty et~al.}}{{Chakraborty, Bedi, Zhu, An, Manocha, and Huang}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-897-\bibcite{xgboost}{{9}{2016}{{Chen and Guestrin}}{{}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux:898:\bibcite{beyond_binary}{{10}{2025}{{Cheng et~al.}}{{Cheng, Zhou, Jiang, Wang, and Li}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-899-\bibcite{synthid_text}{{11}{2024}{{Dathathri et~al.}}{{Dathathri, See, Ghaisas, Huang, McAdam, Welbl, Bachani, Kaskasoli, Stanforth, Matejovicova, Hayes, Vyas, Al~Merey, Brown-Cohen, Bunel, Balle, Cemgil, Ahmed, Stacpoole, Shumailov, Baetu, Gowal, Hassabis, and Kohli}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-900-\bibcite{qlora}{{12}{2023}{{Dettmers et~al.}}{{Dettmers, Pagnoni, Holtzman, and Zettlemoyer}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-901-\bibcite{strong_model_collapse}{{13}{2025}{{Dohmatob et~al.}}{{Dohmatob, Feng, Subramonian, and Kempe}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-902-\bibcite{frank_hall_ordinal}{{14}{2001}{{Frank and Hall}}{{}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.aux-903-\bibcite{gltr}{{15}{2019}{{Gehrmann et~al.}}{{Gehrmann, Strobelt, and Rush}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "babcf2c4-f2b3-4353-b807-a250b53568e0",
  "isSidechain": true,
  "promptId": "eee9fab2-09a6-42b6-8db9-7d474a52fc33",
  "agentId": "aaa655adf37a64747",
  "type": "user",
  "uuid": "e25c2329-ea08-44e2-b239-8aa09f11ee92",
  "sourceToolAssistantUUID": "babcf2c4-f2b3-4353-b807-a250b53568e0",
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

_source line 12 · 2026-05-19T00:56:17.512Z_

Excellent! I have all the information I need from the bibliography and the paper's related work section. Let me compile the findings:

## "Beyond Binary" by Cheng et al. (WWW 2025) - Complete Information

**1. Full Title:**
"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement"

**2. Authors:**
- Zihao Cheng
- Li Zhou
- Feng Jiang
- Benyou Wang
- Haizhou Li

**3. Venue and Year:**
Proceedings of the ACM Web Conference, 2025 (also known as WWW 2025)

**4. What It Does (Multi-class Classification):**
The paper addresses a key limitation of existing AI text detection methods: they produce only binary (human vs. synthetic) decisions. "Beyond Binary" moves beyond this binary paradigm by implementing **role recognition** and **involvement measurement** in human-LLM collaboration contexts. This enables **multi-class detection** that discriminates among different **sources** (different roles or involvement levels of humans vs. LLMs) rather than just a binary real/fake distinction.

**5. How It Differs from Generation Depth Classification:**
This is the crucial distinction highlighted in your paper's related work section (line 10):

- **Beyond Binary (Cheng et al.)**: Focuses on **multi-class detection based on different _sources_** — distinguishing among different roles in human-LLM collaboration (e.g., human-only, LLM-only, human-LLM hybrid with varying involvement levels).

- **Your Work (Generation Depth Classification)**: Focuses on **ordinal classification of _recursive generation depth_** — distinguishing how many iterative generation steps removed text is from a human source (depth 0 = human, depth 1 = first LLM generation, depth 2 = second generation, etc.).

In other words, "Beyond Binary" classifies **who/what created the text** (source attribution with roles), while your paper classifies **how many generative steps the text underwent** (ordinal depth). The paper explicitly notes that role recognition and your depth classification are "orthogonal" problems — they address different facets of the LLM-generated text detection challenge.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e25c2329-ea08-44e2-b239-8aa09f11ee92",
  "isSidechain": true,
  "agentId": "aaa655adf37a64747",
  "requestId": "req_011CbB1xzhyptiY6HkjbjpZH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "597134c4-6050-4879-b4de-9c347b3f27f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014i6nvz2o1Ea71mUoBW6ZGw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5877,
      "cache_read_input_tokens": 37024,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 522,
          "cache_read_input_tokens": 37024,
          "cache_creation_input_tokens": 5877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5877,
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
