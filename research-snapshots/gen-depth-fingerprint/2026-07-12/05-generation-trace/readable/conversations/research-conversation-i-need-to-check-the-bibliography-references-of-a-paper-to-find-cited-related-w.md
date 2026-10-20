# Research conversation: I need to check the bibliography/references of a paper to find cited related work papers. Read the file at /home/ubuntu/

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a270fc364e5b3772c.jsonl`
- **Structured JSON:** [`7713e61821848add047f.json`](../../sessions/77/7713e61821848add047f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

7 recorded events

### User

_source line 1 · 2026-05-18T14:16:05.768Z_

I need to check the bibliography/references of a paper to find cited related work papers. Read the file at /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related.tex and /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib (or similar bib file). 

I want to identify the key empirical/analysis papers cited (especially detection papers like FastDetectGPT, Binoculars, DetectGPT, GLTR, LD-Score, etc.) and their venues. Just list the paper titles/keys and venues. Search breadth: quick.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d32410c1-13ba-4b64-9c72-537ff0a5ca80",
  "agentId": "a270fc364e5b3772c",
  "type": "user",
  "uuid": "09324c17-ab65-4db4-a08e-fb32b46b5bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T14:16:07.260Z_

I'll read the bibliography and references files to identify the key empirical/analysis papers cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09324c17-ab65-4db4-a08e-fb32b46b5bf8",
  "isSidechain": true,
  "agentId": "a270fc364e5b3772c",
  "requestId": "req_011CbAB9zd7x4oU86LpbUZTk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6c9d787-539c-46ae-9a8d-bc8583a4e6a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KYPvi4CQ17YV3Egcw8vwSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37349,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37349,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-18T14:16:07.738Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U7aU5vYu3NA1TY8k4pTg6H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c9d787-539c-46ae-9a8d-bc8583a4e6a6",
  "isSidechain": true,
  "agentId": "a270fc364e5b3772c",
  "requestId": "req_011CbAB9zd7x4oU86LpbUZTk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3f6441a-b805-4004-9f56-daf120d56e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KYPvi4CQ17YV3Egcw8vwSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37349,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37349,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 4 · 2026-05-18T14:16:07.750Z_

<details><summary>↩ Tool result · reported error · `toolu_01U7aU5vYu3NA1TY8k4pTg6H`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f6441a-b805-4004-9f56-daf120d56e02",
  "isSidechain": true,
  "promptId": "d32410c1-13ba-4b64-9c72-537ff0a5ca80",
  "agentId": "a270fc364e5b3772c",
  "type": "user",
  "uuid": "495fb8a2-01ff-41de-97ca-59937b37443d",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f.",
  "sourceToolAssistantUUID": "f3f6441a-b805-4004-9f56-daf120d56e02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:16:07.858Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QnPcLqxYVTZDu2Rr3hWxRw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "495fb8a2-01ff-41de-97ca-59937b37443d",
  "isSidechain": true,
  "agentId": "a270fc364e5b3772c",
  "requestId": "req_011CbAB9zd7x4oU86LpbUZTk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11c2d502-86b0-41d2-9ff7-e7193b047da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KYPvi4CQ17YV3Egcw8vwSJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37349,
      "cache_read_input_tokens": 0,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 184,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37349,
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

_source line 6 · 2026-05-18T14:16:07.868Z_

<details><summary>↩ Tool result · `toolu_01QnPcLqxYVTZDu2Rr3hWxRw`</summary>

```text
1	% ===== Lexical Richness =====
2	
3	@article{mccarthy2010mtld,
4	  title = {{MTLD, vocd-D, and HD-D: A Validation Study of Sophisticated Approaches to Lexical Diversity Assessment}},
5	  author = {McCarthy, Philip M. and Jarvis, Scott},
6	  journal = {Behavior Research Methods},
7	  volume = {42},
8	  number = {2},
9	  pages = {381--392},
10	  year = {2010},
11	}
12	
13	@article{covington2010mattr,
14	  title = {{Cutting the Gordian Knot: The Moving-Average Type-Token Ratio (MATTR)}},
15	  author = {Covington, Michael A. and McFall, Joe D.},
16	  journal = {Journal of Quantitative Linguistics},
17	  volume = {17},
18	  number = {2},
19	  pages = {94--100},
20	  year = {2010},
21	}
22	
23	% ===== Data Provenance / Contamination =====
24	
25	@inproceedings{oren2024proving,
26	  title = {{Proving Test Set Contamination in Black Box Language Models}},
27	  author = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laber, Faisal and Stern, Avi},
28	  booktitle = {Proceedings of the International Conference on Learning Representations},
29	  year = {2024},
30	}
31	
32	@inproceedings{golchin2024time,
33	  title = {{Time Travel in LLMs: Tracing Data Contamination in Large Language Models}},
34	  author = {Golchin, Shahriar and Surdeanu, Mihai},
35	  booktitle = {Proceedings of the International Conference on Learning Representations},
36	  year = {2024},
37	}
38	
39	@inproceedings{longpre2024data,
40	  title = {{Data Authenticity, Consent, and Provenance for AI Are All Broken: What Will It Take to Fix Them?}},
41	  author = {Longpre, Shayne and Mahari, Robert and Lee, Naana and Luccioni, Sasha and Jernite, Yacine and others},
42	  booktitle = {Proceedings of the International Conference on Machine Learning},
43	  year = {2024},
44	}
45	
46	% ===== Statistics =====
47	
48	@book{cohen1988statistical,
49	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
50	  author = {Cohen, Jacob},
51	  edition = {2nd},
52	  publisher = {Lawrence Erlbaum Associates},
53	  year = {1988},
54	}
55	
56	@article{tang2024science,
57	  title = {{The Science of Detecting LLM-Generated Text}},
58	  author = {Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},
59	  journal = {Communications of the ACM},
60	  volume = {67},
61	  number = {4},
62	  pages = {50--59},
63	  year = {2024},
64	}
65	
66	@article{neal2017surveying,
67	  title = {{Surveying Stylometry Techniques and Applications}},
68	  author = {Neal, Tempestt and Sundararajan, Kalaivani and Fatima, Aneez and Yan, Yiming and Xiang, Yingfei and Woodard, Damon L.},
69	  journal = {ACM Computing Surveys},
70	  volume = {50},
71	  number = {6},
72	  pages = {1--36},
73	  year = {2017},
74	}
75	
76	% ===== Detection =====
77	
78	@inproceedings{detectgpt,
79	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
80	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
81	  booktitle = {Proceedings of the International Conference on Machine Learning},
82	  year = {2023},
83	}
84	
85	@inproceedings{gltr,
86	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
87	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
88	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
89	  year = {2019},
90	}
91	
92	@inproceedings{dna_gpt,
93	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
94	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
95	  booktitle = {Proceedings of the International Conference on Learning Representations},
96	  year = {2024},
97	}
98	
99	@inproceedings{binoculars,
100	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
101	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
102	  booktitle = {Proceedings of the International Conference on Machine Learning},
103	  year = {2024},
104	}
105	
106	@inproceedings{fast_detectgpt,
107	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
108	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
109	  booktitle = {Proceedings of the International Conference on Learning Representations},
110	  year = {2024},
111	}
112	
113	@article{ld_score,
114	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
115	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
116	  journal = {arXiv preprint arXiv:2605.01647},
117	  year = {2026},
118	}
119	
120	@inproceedings{intrinsic_dimension,
121	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
122	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
123	  booktitle = {Advances in Neural Information Processing Systems},
124	  year = {2023},
125	}
126	
127	@article{diveye,
128	  title = {{Diversity Boosts AI-Generated Text Detection}},
129	  author = {Basani, Advik Raj and Chen, Pin-Yu},
130	  journal = {Transactions on Machine Learning Research},
131	  year = {2026},
132	}
133	
134	@article{generator_barrier,
135	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
136	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
137	  journal = {arXiv preprint arXiv:2604.13692},
138	  year = {2026},
139	}
140	
141	@article{feat_aug_transformer,
142	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
143	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
144	  journal = {arXiv preprint arXiv:2605.03969},
145	  year = {2026},
146	}
147	
148	@article{reliable_detection,
149	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
150	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
151	  journal = {Transactions on Machine Learning Research},
152	  year = {2025},
153	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
154	}
155	
156	@inproceedings{paraphrase_evades,
157	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
158	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
159	  booktitle = {Advances in Neural Information Processing Systems},
160	  year = {2023},
161	}
162	
163	@inproceedings{detection_possibilities,
164	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
165	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
166	  booktitle = {Proceedings of the International Conference on Machine Learning},
167	  year = {2024},
168	}
169	
170	@inproceedings{grover,
171	  title = {{Defending Against Neural Fake News}},
172	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
173	  booktitle = {Advances in Neural Information Processing Systems},
174	  year = {2019},
175	}
176	
177	@article{release_strategies,
178	  title = {{Release Strategies and the Social Impacts of Language Models}},
179	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
180	  journal = {arXiv preprint arXiv:1908.09203},
181	  year = {2019},
182	}
183	
184	@inproceedings{beyond_binary,
185	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
186	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
187	  booktitle = {Proceedings of the ACM Web Conference},
188	  year = {2025},
189	}
190	
191	@inproceedings{semeval2024_task8,
192	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
193	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
194	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
195	  year = {2024},
196	}
197	
198	@article{abburi_multifaceted,
199	  title = {{AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification}},
200	  author = {Abburi, Harika and Bhattacharya, Sanmitra and Bowen, Edward and Pudota, Nirmala},
201	  journal = {arXiv preprint arXiv:2505.11550},
202	  year = {2025},
203	}
204	
205	@article{defactify_dataset,
206	  title = {{A Comprehensive Dataset for Human vs.\ AI Generated Text Detection}},
207	  author = {Roy, Rajarshi and Imanpour, Nasrin and Aziz, Ashhar and Bajpai, Shashwat and Singh, Gurpreet and Biswas, Shwetangshu and Wanaskar, Kapil and Patwa, Parth and Ghosh, Subhankar and Dixit, Shreyas and Pal, Nilesh Ranjan and Rawte, Vipula and Garimella, Ritvik and Jena, Gaytri and Sheth, Amit and Sharma, Vasu and Reganti, Aishwarya Naresh and Jain, Vinija and Chadha, Aman and Das, Amitava},
208	  journal = {arXiv preprint arXiv:2510.22874},
209	  year = {2025},
210	}
211	
212	% ===== Model Collapse =====
213	
214	@inproceedings{self_consuming_mad,
215	  title = {{Self-Consuming Generative Models Go MAD}},
216	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
217	  booktitle = {Proceedings of the International Conference on Learning Representations},
218	  year = {2024},
219	}
220	
221	@article{curse_of_recursion,
222	  title = {{AI models collapse when trained on recursively generated data}},
223	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
224	  journal = {Nature},
225	  volume = {631},
226	  pages = {755--759},
227	  year = {2024},
228	}
229	
230	@inproceedings{strong_model_collapse,
231	  title = {{Strong Model Collapse}},
232	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
233	  booktitle = {Proceedings of the International Conference on Learning Representations},
234	  year = {2025},
235	}
236	
237	@inproceedings{model_collapse_avoidable,
238	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
239	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
240	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
241	  year = {2024},
242	}
243	
244	% ===== Fine-tuning =====
245	
246	@inproceedings{qlora,
247	  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},
248	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
249	  booktitle = {Advances in Neural Information Processing Systems},
250	  year = {2023},
251	}
252	
253	% ===== Data Quality =====
254	
255	% ===== (orphan entries removed: fineweb, dolma) =====
256	
257	@inproceedings{dsir,
258	  title = {{Data Selection for Language Models via Importance Resampling}},
259	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
260	  booktitle = {Advances in Neural Information Processing Systems},
261	  year = {2023},
262	}
263	
264	@inproceedings{qurating,
265	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
266	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
267	  booktitle = {Proceedings of the International Conference on Machine Learning},
268	  year = {2024},
269	}
270	
271	@inproceedings{ccnet,
272	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
273	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
274	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
275	  year = {2020},
276	}
277	
278	% ===== Watermarking =====
279	
280	@inproceedings{watermark_llm,
281	  title = {{A Watermark for Large Language Models}},
282	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
283	  booktitle = {Proceedings of the International Conference on Machine Learning},
284	  year = {2023},
285	}
286	
287	@article{synthid_text,
288	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
289	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
290	  journal = {Nature},
291	  volume = {634},
292	  pages = {818--823},
293	  year = {2024},
294	}
295	
296	@misc{aaronson_watermark,
297	  title = {{Watermarking GPT Outputs}},
298	  author = {Aaronson, Scott and Kirchner, Hendrik},
299	  year = {2022},
300	  howpublished = {Technical Talk},
301	  url = {https://scottaaronson.blog/?p=6823},
302	}
303	
304	@article{chainwash,
305	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
306	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
307	  journal = {arXiv preprint arXiv:2605.05503},
308	  year = {2026},
309	}
310	
311	% ===== Vocabulary Diversity =====
312	
313	@inproceedings{curious_decline,
314	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
315	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
316	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
317	  year = {2024},
318	}
319	
320	@inproceedings{writing_diversity,
321	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
322	  author = {Padmakumar, Vishakh and He, He},
323	  booktitle = {Proceedings of the International Conference on Learning Representations},
324	  year = {2024},
325	}
326	
327	@inproceedings{nucleus_sampling,
328	  title = {{The Curious Case of Neural Text Degeneration}},
329	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
330	  booktitle = {Proceedings of the International Conference on Learning Representations},
331	  year = {2020},
332	}
333	
334	@inproceedings{mapping_llm_science,
335	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
336	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
337	  booktitle = {Proceedings of the Conference on Language Modeling},
338	  year = {2024},
339	}
340	
341	@inproceedings{monitoring_ai_review,
342	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
343	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
344	  booktitle = {Proceedings of the International Conference on Machine Learning},
345	  year = {2024},
346	}
347	
348	% ===== Stylometry =====
349	
350	@article{stamatatos_survey,
351	  title = {{A Survey of Modern Authorship Attribution Methods}},
352	  author = {Stamatatos, Efstathios},
353	  journal = {Journal of the American Society for Information Science and Technology},
354	  volume = {60},
355	  number = {3},
356	  pages = {538--556},
357	  year = {2009},
358	}
359	
360	@article{koppel_authorship,
361	  title = {{Computational Methods in Authorship Attribution}},
362	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
363	  journal = {Journal of the American Society for Information Science and Technology},
364	  volume = {60},
365	  number = {1},
366	  pages = {9--26},
367	  year = {2009},
368	}
369	
370	@inproceedings{uchendu_attribution,
371	  title = {{Authorship Attribution for Neural Text Generation}},
372	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
373	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
374	  year = {2020},
375	}
376	
377	@inproceedings{munir_looking_glass,
378	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
379	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
380	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
381	  year = {2021},
382	}
383	
384	% ===== (orphan entries removed: briesch_self_consuming, jovanovic_watermark_stealing, mcgovern_fingerprints) =====
385	
386	% ===== Iterative Generation =====
387	
388	@inproceedings{broken_telephone,
389	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
390	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
391	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
392	  year = {2025},
393	}
394	
395	@article{markovian_chains,
396	  title = {{Markovian Generation Chains in Large Language Models}},
397	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
398	  journal = {arXiv preprint arXiv:2603.11228},
399	  year = {2026},
400	}
401	
402	@inproceedings{self_refine,
403	  title = {{Self-Refine: Iterative Refinement with Self-Feedback}},
404	  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
405	  booktitle = {Advances in Neural Information Processing Systems},
406	  year = {2023},
407	}
408	
409	% ===== Membership Inference =====
410	
411	@inproceedings{min_k_percent,
412	  title = {{Detecting Pretraining Data from Large Language Models}},
413	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
414	  booktitle = {Proceedings of the International Conference on Learning Representations},
415	  year = {2024},
416	}
417	
418	% ===== Survey =====
419	
420	@article{wu_survey_2025,
421	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
422	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
423	  journal = {Computational Linguistics},
424	  publisher = {MIT Press},
425	  year = {2025},
426	}
427	
428	@inproceedings{jawahar_survey,
429	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
430	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
431	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
432	  year = {2020},
433	}
434	
435	% ===== Models =====
436	
437	@inproceedings{pythia,
438	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
439	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
440	  booktitle = {Proceedings of the International Conference on Machine Learning},
441	  year = {2023},
442	}
443	
444	@inproceedings{olmo,
445	  title = {{OLMo: Accelerating the Science of Language Models}},
446	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
447	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
448	  year = {2024},
449	}
450	
451	@article{qwen3,
452	  title = {{Qwen3 Technical Report}},
453	  author = {{Qwen Team}},
454	  journal = {arXiv preprint arXiv:2505.09388},
455	  year = {2025},
456	}
457	
458	@inproceedings{ghostbuster,
459	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
460	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Jurafsky, Dan},
461	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
462	  year = {2024},
463	}
464	
465	@inproceedings{radar,
466	  title = {{RADAR: Robust AI-Text Detection via Adversarial Learning}},
467	  author = {Hu, Xiaomeng and Chen, Pin-Yu and Ho, Tsung-Yi},
468	  booktitle = {Advances in Neural Information Processing Systems},
469	  year = {2023},
470	}
471	
472	% ===== Machine Learning =====
473	
474	@article{gutierrez_ordinal_survey,
475	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
476	  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
477	  journal = {IEEE Transactions on Knowledge and Data Engineering},
478	  volume = {28},
479	  number = {1},
480	  pages = {127--146},
481	  year = {2016},
482	}
483	
484	@article{coral_ordinal,
485	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
486	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
487	  journal = {Pattern Recognition Letters},
488	  volume = {140},
489	  pages = {325--331},
490	  year = {2020},
491	}
492	
493	@inproceedings{frank_hall_ordinal,
494	  title = {{A Simple Approach to Ordinal Classification}},
495	  author = {Frank, Eibe and Hall, Mark},
496	  booktitle = {Proceedings of the European Conference on Machine Learning},
497	  year = {2001},
498	}
499	
500	@article{corn_ordinal,
501	  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
502	  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
503	  journal = {Pattern Analysis and Applications},
504	  volume = {26},
505	  pages = {941--955},
506	  year = {2023},
507	}
508	
509	@inproceedings{xgboost,
510	  title = {{XGBoost: A Scalable Tree Boosting System}},
511	  author = {Chen, Tianqi and Guestrin, Carlos},
512	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
513	  year = {2016},
514	}
515	
516	@article{lakens_equivalence,
517	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
518	  author = {Lakens, Dani{\"e}l},
519	  journal = {Social Psychological and Personality Science},
520	  volume = {8},
521	  number = {4},
522	  pages = {355--362},
523	  year = {2017},
524	}
525	
526	% ===== Generator Model References =====
527	
528	@article{llama3,
529	  title = {{The Llama 3 Herd of Models}},
530	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
531	  journal = {arXiv preprint arXiv:2407.21783},
532	  year = {2024},
533	}
534	
535	@article{mistral7b,
536	  title = {{Mistral 7B}},
537	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
538	  journal = {arXiv preprint arXiv:2310.06825},
539	  year = {2023},
540	}
541	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11c2d502-86b0-41d2-9ff7-e7193b047da8",
  "isSidechain": true,
  "promptId": "d32410c1-13ba-4b64-9c72-537ff0a5ca80",
  "agentId": "a270fc364e5b3772c",
  "type": "user",
  "uuid": "deb9fb78-e8c5-4d50-8ce4-0b3154099c37",
  "sourceToolAssistantUUID": "11c2d502-86b0-41d2-9ff7-e7193b047da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-18T14:16:16.544Z_

Perfect! I found the references.bib file. Let me extract the key detection and analysis papers from it.

Based on the references.bib file, here are the **key empirical/analysis papers on AI-generated text detection** cited in the project:

## Detection Methods

| Paper Key | Title | Venue |
|-----------|-------|-------|
| `detectgpt` | DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | ICML 2023 |
| `gltr` | GLTR: Statistical Detection and Visualization of Generated Text | ACL 2019 (System Demonstrations) |
| `fast_detectgpt` | Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | ICLR 2024 |
| `binoculars` | Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | ICML 2024 |
| `dna_gpt` | DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | ICLR 2024 |
| `intrinsic_dimension` | Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | NeurIPS 2023 |
| `ld_score` | Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection | arXiv 2026 |

## Other Key Analysis/Empirical Papers

| Paper Key | Title | Venue |
|-----------|-------|-------|
| `paraphrase_evades` | Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense | NeurIPS 2023 |
| `detection_possibilities` | Position: On the Possibilities of AI-Generated Text Detection | ICML 2024 |
| `grover` | Defending Against Neural Fake News | NeurIPS 2019 |
| `reliable_detection` | Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | TMLR 2025 |
| `diveye` | Diversity Boosts AI-Generated Text Detection | TMLR 2026 |
| `ghostbuster` | Ghostbuster: Detecting Text Ghostwritten by Large Language Models | ACL 2024 |
| `radar` | RADAR: Robust AI-Text Detection via Adversarial Learning | NeurIPS 2023 |

The paper also cites important related surveys and benchmark papers like the **SemEval-2024 Task 8** on multidomain/multimodel/multilingual machine-generated text detection, and a comprehensive review article **"The Science of Detecting LLM-Generated Text"** (Tang et al., Communications of the ACM 2024).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deb9fb78-e8c5-4d50-8ce4-0b3154099c37",
  "isSidechain": true,
  "agentId": "a270fc364e5b3772c",
  "requestId": "req_011CbABA9h5JXhiUnqefZFQS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b72f62b-84c7-4c6b-8ef0-603b6c9be02d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ee8153a1-2d10-446d-8fa5-c74306b35416",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "typed-enchanting-muffin",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Powy1fUoZrnj9Wjp92XvKb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10780,
      "cache_read_input_tokens": 37349,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 697,
          "cache_read_input_tokens": 37349,
          "cache_creation_input_tokens": 10780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10780,
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
