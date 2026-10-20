# Research conversation: I need to check specific BibTeX entries in the paper's .bib file(s) for the gen-depth-fingerprint project. Find the bib 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aed4146fa26bdbdd0.jsonl`
- **Structured JSON:** [`a8a5aef87a86a8d608c2.json`](../../sessions/a8/a8a5aef87a86a8d608c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-24T15:04:43.771Z_

I need to check specific BibTeX entries in the paper's .bib file(s) for the gen-depth-fingerprint project. Find the bib file and extract the entries for these 16 citation keys:

Ghost citations (6): detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost

Inconsistent info (10): cohen1988statistical, paraphrase_evades, intrinsic_dim_detection, self_consuming_mad, dsir, nucleus_sampling, qwen3, gutierrez_ordinal_survey, diaz_soft_labels_ordinal, llama3

Search in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ for .bib files, then extract each of these entries showing the full entry (title, author, year, venue/journal, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ee622ec2-5cbd-444b-9510-61af72dbc84a",
  "agentId": "aed4146fa26bdbdd0",
  "type": "user",
  "uuid": "8b66f4c4-9ca9-499f-84a3-38acf7a96a15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T15:04:46.378Z_

I'll help you find and extract the BibTeX entries from the paper's .bib file. Let me start by searching for .bib files in the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b66f4c4-9ca9-499f-84a3-38acf7a96a15",
  "isSidechain": true,
  "agentId": "aed4146fa26bdbdd0",
  "requestId": "req_011CbMbibFgzRtYFTk3a4tTp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4f6cf17-efec-4a52-8e42-c421135506f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018vMrcrWmC2UAEB1bPyvuMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39735,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39735,
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

_source line 3 · 2026-05-24T15:04:46.536Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017Uvx4TZ63YTgeLVyViRTaN`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f6cf17-efec-4a52-8e42-c421135506f2",
  "isSidechain": true,
  "agentId": "aed4146fa26bdbdd0",
  "requestId": "req_011CbMbibFgzRtYFTk3a4tTp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9407cdbd-37c5-4982-8d78-059a6fe11044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018vMrcrWmC2UAEB1bPyvuMn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39735,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39735,
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

_source line 4 · 2026-05-24T15:04:46.553Z_

<details><summary>↩ Tool result · `toolu_017Uvx4TZ63YTgeLVyViRTaN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9407cdbd-37c5-4982-8d78-059a6fe11044",
  "isSidechain": true,
  "promptId": "ee622ec2-5cbd-444b-9510-61af72dbc84a",
  "agentId": "aed4146fa26bdbdd0",
  "type": "user",
  "uuid": "3c6dddf7-31f4-4c7f-aeaa-78ceeb33ef4f",
  "sourceToolAssistantUUID": "9407cdbd-37c5-4982-8d78-059a6fe11044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T15:04:53.784Z_

Good! I found the bib file at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib`. Now let me read it and extract the entries for all 16 citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c6dddf7-31f4-4c7f-aeaa-78ceeb33ef4f",
  "isSidechain": true,
  "agentId": "aed4146fa26bdbdd0",
  "requestId": "req_011CbMbj3YjoUoo1JKwvdRuQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9416404a-dc87-4b21-b069-5f63e2118a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MZEZqz87rWgrkdYbx6LBwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 39735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1007,
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

_source line 6 · 2026-05-24T15:04:54.024Z_

<details open><summary>🔧 Tool call — Read · `toolu_014mXVnDqu4wHmsKRJ2HUCAt`</summary>

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
  "parentUuid": "9416404a-dc87-4b21-b069-5f63e2118a54",
  "isSidechain": true,
  "agentId": "aed4146fa26bdbdd0",
  "requestId": "req_011CbMbj3YjoUoo1JKwvdRuQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ce8a69d-bca3-4529-886d-064bb2fd2ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MZEZqz87rWgrkdYbx6LBwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 39735,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 154,
          "cache_read_input_tokens": 39735,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1007,
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

_source line 7 · 2026-05-24T15:04:54.310Z_

<details><summary>↩ Tool result · `toolu_014mXVnDqu4wHmsKRJ2HUCAt`</summary>

```text
1	% ===== Data Provenance / Contamination =====
2	
3	% ===== Statistics =====
4	
5	@book{cohen1988statistical,
6	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
7	  author = {Cohen, Jacob},
8	  edition = {2nd},
9	  publisher = {Lawrence Erlbaum Associates},
10	  year = {1988},
11	}
12	
13	% ===== Detection =====
14	
15	@inproceedings{detectgpt,
16	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
17	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
18	  booktitle = {Proceedings of the International Conference on Machine Learning},
19	  year = {2023},
20	}
21	
22	@inproceedings{gltr,
23	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
24	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
25	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
26	  year = {2019},
27	}
28	
29	@inproceedings{dna_gpt,
30	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
31	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
32	  booktitle = {Proceedings of the International Conference on Learning Representations},
33	  year = {2024},
34	}
35	
36	@inproceedings{binoculars,
37	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
38	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
39	  booktitle = {Proceedings of the International Conference on Machine Learning},
40	  year = {2024},
41	}
42	
43	@inproceedings{fast_detectgpt,
44	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
45	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
46	  booktitle = {Proceedings of the International Conference on Learning Representations},
47	  year = {2024},
48	}
49	
50	@article{ld_score,
51	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
52	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
53	  journal = {arXiv preprint arXiv:2605.01647},
54	  year = {2026},
55	}
56	
57	@inproceedings{diveye,
58	  title = {{Diversity Boosts AI-Generated Text Detection}},
59	  author = {Basani, Advik Raj and Chen, Pin-Yu},
60	  booktitle = {Proceedings of the International Conference on Learning Representations},
61	  year = {2026},
62	  eprint = {2509.18880},
63	  archiveprefix = {arXiv},
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
95	@inproceedings{intrinsic_dim_detection,
96	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
97	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2023},
100	}
101	
102	@inproceedings{seqxgpt,
103	  title = {{SeqXGPT: Sentence-Level AI-Generated Text Detection}},
104	  author = {Wang, Pengyu and Li, Linyang and Ren, Ke and Jiang, Botian and Zhang, Dong and Qiu, Xipeng},
105	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
106	  year = {2023},
107	}
108	
109	@inproceedings{grover,
110	  title = {{Defending Against Neural Fake News}},
111	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
112	  booktitle = {Advances in Neural Information Processing Systems},
113	  year = {2019},
114	}
115	
116	@article{release_strategies,
117	  title = {{Release Strategies and the Social Impacts of Language Models}},
118	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
119	  journal = {arXiv preprint arXiv:1908.09203},
120	  year = {2019},
121	}
122	
123	@inproceedings{beyond_binary,
124	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
125	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
126	  booktitle = {Proceedings of the ACM Web Conference},
127	  year = {2025},
128	}
129	
130	@inproceedings{semeval2024_task8,
131	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
132	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
133	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
134	  year = {2024},
135	}
136	
137	% ===== Model Collapse =====
138	
139	@inproceedings{self_consuming_mad,
140	  title = {{Self-Consuming Generative Models Go MAD}},
141	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
142	  booktitle = {Proceedings of the International Conference on Learning Representations},
143	  year = {2024},
144	}
145	
146	@article{curse_of_recursion,
147	  title = {{AI models collapse when trained on recursively generated data}},
148	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
149	  journal = {Nature},
150	  volume = {631},
151	  pages = {755--759},
152	  year = {2024},
153	}
154	
155	@inproceedings{dohmatob_tale_of_tails,
156	  title = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
157	  author = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Fran\c{c}ois and Kempe, Julia},
158	  booktitle = {Proceedings of the International Conference on Machine Learning},
159	  year = {2024},
160	}
161	
162	@inproceedings{strong_model_collapse,
163	  title = {{Strong Model Collapse}},
164	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
165	  booktitle = {Proceedings of the International Conference on Learning Representations},
166	  year = {2025},
167	}
168	
169	@inproceedings{model_collapse_avoidable,
170	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
171	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
172	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
173	  year = {2024},
174	}
175	
176	@article{schaeffer_collapse_position,
177	  title = {{Position: Model Collapse Does Not Mean What You Think}},
178	  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
179	  journal = {arXiv preprint arXiv:2503.03150},
180	  year = {2025},
181	}
182	
183	@inproceedings{seddik_synthetic_data,
184	  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
185	  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
186	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
187	  year = {2024},
188	}
189	
190	% ===== Fine-tuning =====
191	
192	@inproceedings{qlora,
193	  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
194	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
195	  booktitle = {Advances in Neural Information Processing Systems},
196	  year = {2023},
197	}
198	
199	% ===== Data Quality =====
200	
201	@inproceedings{dsir,
202	  title = {{Data Selection for Language Models via Importance Resampling}},
203	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
204	  booktitle = {Advances in Neural Information Processing Systems},
205	  year = {2023},
206	}
207	
208	@inproceedings{qurating,
209	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
210	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
211	  booktitle = {Proceedings of the International Conference on Machine Learning},
212	  year = {2024},
213	}
214	
215	@inproceedings{ccnet,
216	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
217	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
218	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
219	  year = {2020},
220	}
221	
222	% ===== Watermarking =====
223	
224	@inproceedings{watermark_llm,
225	  title = {{A Watermark for Large Language Models}},
226	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
227	  booktitle = {Proceedings of the International Conference on Machine Learning},
228	  year = {2023},
229	}
230	
231	@article{synthid_text,
232	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
233	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
234	  journal = {Nature},
235	  volume = {634},
236	  pages = {818--823},
237	  year = {2024},
238	}
239	
240	@misc{aaronson_watermark,
241	  title = {{Watermarking GPT Outputs}},
242	  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
243	  year = {2022},
244	  note = {Blog post},
245	  url = {https://scottaaronson.blog/?p=6823},
246	}
247	
248	@article{chainwash,
249	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
250	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
251	  journal = {arXiv preprint arXiv:2605.05503},
252	  year = {2026},
253	}
254	
255	% ===== Vocabulary Diversity =====
256	
257	@inproceedings{curious_decline,
258	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
259	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
260	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
261	  year = {2024},
262	}
263	
264	@inproceedings{writing_diversity,
265	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
266	  author = {Padmakumar, Vishakh and He, He},
267	  booktitle = {Proceedings of the International Conference on Learning Representations},
268	  year = {2024},
269	}
270	
271	@inproceedings{nucleus_sampling,
272	  title = {{The Curious Case of Neural Text Degeneration}},
273	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
274	  booktitle = {Proceedings of the International Conference on Learning Representations},
275	  year = {2020},
276	}
277	
278	@inproceedings{welleck_unlikelihood,
279	  title = {{Neural Text Generation with Unlikelihood Training}},
280	  author = {Welleck, Sean and Kulikov, Ilia and Roller, Stephen and Dinan, Emily and Cho, Kyunghyun and Weston, Jason},
281	  booktitle = {Proceedings of the International Conference on Learning Representations},
282	  year = {2020},
283	}
284	
285	% ===== Stylometry =====
286	
287	@article{stamatatos_survey,
288	  title = {{A Survey of Modern Authorship Attribution Methods}},
289	  author = {Stamatatos, Efstathios},
290	  journal = {Journal of the American Society for Information Science and Technology},
291	  volume = {60},
292	  number = {3},
293	  pages = {538--556},
294	  year = {2009},
295	}
296	
297	@article{koppel_authorship,
298	  title = {{Computational Methods in Authorship Attribution}},
299	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
300	  journal = {Journal of the American Society for Information Science and Technology},
301	  volume = {60},
302	  number = {1},
303	  pages = {9--26},
304	  year = {2009},
305	}
306	
307	@inproceedings{uchendu_attribution,
308	  title = {{Authorship Attribution for Neural Text Generation}},
309	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
310	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
311	  year = {2020},
312	}
313	
314	@inproceedings{munir_looking_glass,
315	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
316	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
317	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
318	  year = {2021},
319	}
320	
321	@article{briesch_self_consuming,
322	  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
323	  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
324	  journal = {arXiv preprint arXiv:2311.16822},
325	  year = {2023},
326	}
327	
328	% ===== Iterative Generation =====
329	
330	@inproceedings{broken_telephone,
331	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
332	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
333	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
334	  year = {2025},
335	}
336	
337	@article{markovian_chains,
338	  title = {{Markovian Generation Chains in Large Language Models}},
339	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
340	  journal = {arXiv preprint arXiv:2603.11228},
341	  year = {2026},
342	}
343	
344	@inproceedings{attractor_cycles,
345	  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},
346	  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
347	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
348	  year = {2025},
349	  eprint = {2502.15208},
350	  archiveprefix = {arXiv},
351	}
352	
353	% ===== Membership Inference =====
354	
355	@inproceedings{min_k_percent,
356	  title = {{Detecting Pretraining Data from Large Language Models}},
357	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
358	  booktitle = {Proceedings of the International Conference on Learning Representations},
359	  year = {2024},
360	}
361	
362	@article{koike_mia_detection,
363	  title = {{Machine Text Detectors are Membership Inference Attacks}},
364	  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},
365	  journal = {arXiv preprint arXiv:2510.19492},
366	  year = {2025},
367	}
368	
369	% ===== Survey =====
370	
371	@article{wu_survey_2025,
372	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
373	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
374	  journal = {Computational Linguistics},
375	  publisher = {MIT Press},
376	  year = {2025},
377	}
378	
379	@inproceedings{jawahar_survey,
380	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
381	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
382	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
383	  year = {2020},
384	}
385	
386	% ===== Models =====
387	
388	@inproceedings{pythia,
389	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
390	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
391	  booktitle = {Proceedings of the International Conference on Machine Learning},
392	  year = {2023},
393	}
394	
395	@inproceedings{olmo,
396	  title = {{OLMo: Accelerating the Science of Language Models}},
397	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
398	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
399	  year = {2024},
400	}
401	
402	@article{qwen3,
403	  title = {{Qwen3 Technical Report}},
404	  author = {{Qwen Team}},
405	  journal = {arXiv preprint arXiv:2505.09388},
406	  year = {2025},
407	}
408	
409	@inproceedings{ghostbuster,
410	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
411	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
412	  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
413	  year = {2024},
414	}
415	
416	@article{two_birds,
417	  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},
418	  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},
419	  journal = {arXiv preprint arXiv:2508.14190},
420	  year = {2025},
421	}
422	
423	@inproceedings{beyond_final_actor,
424	  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},
425	  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},
426	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
427	  year = {2026},
428	}
429	
430	% ===== Machine Learning =====
431	
432	@article{gutierrez_ordinal_survey,
433	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
434	  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
435	  journal = {IEEE Transactions on Knowledge and Data Engineering},
436	  volume = {28},
437	  number = {1},
438	  pages = {127--146},
439	  year = {2016},
440	}
441	
442	@article{coral_ordinal,
443	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
444	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
445	  journal = {Pattern Recognition Letters},
446	  volume = {140},
447	  pages = {325--331},
448	  year = {2020},
449	}
450	
451	@inproceedings{frank_hall_ordinal,
452	  title = {{A Simple Approach to Ordinal Classification}},
453	  author = {Frank, Eibe and Hall, Mark},
454	  booktitle = {Proceedings of the European Conference on Machine Learning},
455	  year = {2001},
456	}
457	
458	@article{corn_ordinal,
459	  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
460	  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
461	  journal = {Pattern Analysis and Applications},
462	  volume = {26},
463	  pages = {941--955},
464	  year = {2023},
465	}
466	
467	@inproceedings{diaz_soft_labels_ordinal,
468	  title = {{Soft Labels for Ordinal Regression}},
469	  author = {Diaz, Raul and Marathe, Amit},
470	  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
471	  year = {2019},
472	}
473	
474	@inproceedings{kasa_ordinality_nlp,
475	  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
476	  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
477	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
478	  year = {2024},
479	}
480	
481	@inproceedings{xgboost,
482	  title = {{XGBoost: A Scalable Tree Boosting System}},
483	  author = {Chen, Tianqi and Guestrin, Carlos},
484	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
485	  year = {2016},
486	}
487	
488	@article{lakens_equivalence,
489	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
490	  author = {Lakens, Dani{\"e}l},
491	  journal = {Social Psychological and Personality Science},
492	  volume = {8},
493	  number = {4},
494	  pages = {355--362},
495	  year = {2017},
496	}
497	
498	% ===== Generator Model References =====
499	
500	@article{llama3,
501	  title = {{The Llama 3 Herd of Models}},
502	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
503	  journal = {arXiv preprint arXiv:2407.21783},
504	  year = {2024},
505	}
506	
507	@article{mistral7b,
508	  title = {{Mistral 7B}},
509	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
510	  journal = {arXiv preprint arXiv:2310.06825},
511	  year = {2023},
512	}
513	
514	@article{strobl_conditional_2008,
515	  title = {Conditional Variable Importance for Random Forests},
516	  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},
517	  journal = {BMC Bioinformatics},
518	  volume = {9},
519	  pages = {307},
520	  year = {2008},
521	}
522	
523	% --- Entries from Paper Agent (docs/paper) ---
524	
525	@inproceedings{dolma,
526	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
527	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
528	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
529	  year = {2024},
530	}
531	
532	
533	@inproceedings{fineweb,
534	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
535	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
536	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
537	  year = {2024},
538	}
539	
540	
541	@inproceedings{mapping_llm_science,
542	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
543	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
544	  booktitle = {Proceedings of the Conference on Language Modeling},
545	  year = {2024},
546	}
547	
548	
549	@inproceedings{monitoring_ai_review,
550	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
551	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
552	  booktitle = {Proceedings of the International Conference on Machine Learning},
553	  year = {2024},
554	}
555	
556	% ===== Stylometry =====
557	
558	
559	
560	@inproceedings{raid,
561	  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
562	  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
563	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
564	  year = {2024},
565	  address = {Bangkok, Thailand},
566	  publisher = {Association for Computational Linguistics},
567	  pages = {12463--12492},
568	}
569	
570	% ===== Spectral / Frequency-domain Detection =====
571	
572	@article{xu_spectrum_detection,
573	  title = {{Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood}},
574	  author = {Xu, Yang and Wang, Yu and An, Hao and Liu, Zhichen and Li, Yongyuan},
575	  journal = {arXiv preprint arXiv:2406.19874},
576	  year = {2024},
577	}
578	
579	% ===== Distribution Quality =====
580	
581	@inproceedings{mauve,
582	  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},
583	  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},
584	  booktitle = {Advances in Neural Information Processing Systems},
585	  year = {2021},
586	}
587	
588	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ce8a69d-bca3-4529-886d-064bb2fd2ae3",
  "isSidechain": true,
  "promptId": "ee622ec2-5cbd-444b-9510-61af72dbc84a",
  "agentId": "aed4146fa26bdbdd0",
  "type": "user",
  "uuid": "f7cb9322-5b23-4786-83cb-046b842d9edf",
  "sourceToolAssistantUUID": "2ce8a69d-bca3-4529-886d-064bb2fd2ae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T15:05:13.237Z_

Perfect! I found the references.bib file and have extracted all 16 citation entries. Here are the results:

## Ghost Citations (6 entries)

**1. detectgpt** (lines 15-20)
```
@inproceedings{detectgpt,
  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
  booktitle = {Proceedings of the International Conference on Machine Learning},
  year = {2023},
}
```

**2. reliable_detection** (lines 73-79)
```
@article{reliable_detection,
  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
  journal = {Transactions on Machine Learning Research},
  year = {2025},
  url = {https://openreview.net/forum?id=OOgsAZdFOt},
}
```

**3. detection_possibilities** (lines 88-93)
```
@inproceedings{detection_possibilities,
  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
  booktitle = {Proceedings of the International Conference on Machine Learning},
  year = {2024},
}
```

**4. aaronson_watermark** (lines 240-246)
```
@misc{aaronson_watermark,
  title = {{Watermarking GPT Outputs}},
  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
  year = {2022},
  note = {Blog post},
  url = {https://scottaaronson.blog/?p=6823},
}
```

**5. pythia** (lines 388-393)
```
@inproceedings{pythia,
  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
  booktitle = {Proceedings of the International Conference on Machine Learning},
  year = {2023},
}
```

**6. xgboost** (lines 481-486)
```
@inproceedings{xgboost,
  title = {{XGBoost: A Scalable Tree Boosting System}},
  author = {Chen, Tianqi and Guestrin, Carlos},
  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
  year = {2016},
}
```

## Inconsistent Info (10 entries)

**7. cohen1988statistical** (lines 5-11)
```
@book{cohen1988statistical,
  title = {{Statistical Power Analysis for the Behavioral Sciences}},
  author = {Cohen, Jacob},
  edition = {2nd},
  publisher = {Lawrence Erlbaum Associates},
  year = {1988},
}
```

**8. paraphrase_evades** (lines 81-86)
```
@inproceedings{paraphrase_evades,
  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023},
}
```

**9. intrinsic_dim_detection** (lines 95-100)
```
@inproceedings{intrinsic_dim_detection,
  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023},
}
```

**10. self_consuming_mad** (lines 139-144)
```
@inproceedings{self_consuming_mad,
  title = {{Self-Consuming Generative Models Go MAD}},
  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
  booktitle = {Proceedings of the International Conference on Learning Representations},
  year = {2024},
}
```

**11. dsir** (lines 201-206)
```
@inproceedings{dsir,
  title = {{Data Selection for Language Models via Importance Resampling}},
  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023},
}
```

**12. nucleus_sampling** (lines 271-276)
```
@inproceedings{nucleus_sampling,
  title = {{The Curious Case of Neural Text Degeneration}},
  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
  booktitle = {Proceedings of the International Conference on Learning Representations},
  year = {2020},
}
```

**13. qwen3** (lines 402-407)
```
@article{qwen3,
  title = {{Qwen3 Technical Report}},
  author = {{Qwen Team}},
  journal = {arXiv preprint arXiv:2505.09388},
  year = {2025},
}
```

**14. gutierrez_ordinal_survey** (lines 432-440)
```
@article{gutierrez_ordinal_survey,
  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
  journal = {IEEE Transactions on Knowledge and Data Engineering},
  volume = {28},
  number = {1},
  pages = {127--146},
  year = {2016},
}
```

**15. diaz_soft_labels_ordinal** (lines 467-472)
```
@inproceedings{diaz_soft_labels_ordinal,
  title = {{Soft Labels for Ordinal Regression}},
  author = {Diaz, Raul and Marathe, Amit},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year = {2019},
}
```

**16. llama3** (lines 500-505)
```
@article{llama3,
  title = {{The Llama 3 Herd of Models}},
  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
  journal = {arXiv preprint arXiv:2407.21783},
  year = {2024},
}
```

All 16 citation keys are present in the references.bib file with complete entry information including authors, titles, publication venues, and years.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cb9322-5b23-4786-83cb-046b842d9edf",
  "isSidechain": true,
  "agentId": "aed4146fa26bdbdd0",
  "requestId": "req_011CbMbjN3UrPuYeaRdLzoSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8ae37bd-13cf-4c52-91c1-778315897965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "6f13698d-9bb4-4f2e-acbc-2759ff5b5bb1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-noodling-llama",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TpreyZPLXgidK5Nj3AjCgi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10812,
      "cache_read_input_tokens": 40742,
      "output_tokens": 2226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10812
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2226,
          "cache_read_input_tokens": 40742,
          "cache_creation_input_tokens": 10812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10812,
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
