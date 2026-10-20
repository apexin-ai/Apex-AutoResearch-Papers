# Research conversation: Search across the paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/p

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8ac91885028ee045.jsonl`
- **Structured JSON:** [`6767caf15e7fe0c57965.json`](../../sessions/67/6767caf15e7fe0c57965.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-15T10:12:17.943Z_

Search across the paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ for references to "Krishna", "Sadasivan", and "Wei Hao" (or "Hao 2025"). Also check references.bib for these entries. I need to know if these 3 citations already exist in the bibliography or are genuinely missing. Report the exact bib keys if found, or confirm they are absent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "9dd4c6af-7cb4-4bae-81f1-c51b40b0c133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T10:12:19.414Z_

I'll search the paper files and bibliography for those author references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dd4c6af-7cb4-4bae-81f1-c51b40b0c133",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B8y2pQFG4jT8KuauM8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88b620e2-fe95-4b06-bf65-720c24579c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0132hrn7yGJSNwPPi9rsKG9W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20718,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20718,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 3 · 2026-05-15T10:12:19.771Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SUnXqFzpBQiB2mirDS2xG6`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b620e2-fe95-4b06-bf65-720c24579c55",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B8y2pQFG4jT8KuauM8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35e33aa2-6fa9-422f-acce-7e881a46fdce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0132hrn7yGJSNwPPi9rsKG9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20718,
      "cache_read_input_tokens": 0,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20718,
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

### Tool call

_source line 4 · 2026-05-15T10:12:19.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZW1hudRAxt9KLmiSYAqHk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e33aa2-6fa9-422f-acce-7e881a46fdce",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B8y2pQFG4jT8KuauM8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cd503391-6ec7-4d76-8390-0e5ec0555585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0132hrn7yGJSNwPPi9rsKG9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20718,
      "cache_read_input_tokens": 0,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20718,
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

_source line 5 · 2026-05-15T10:12:19.793Z_

<details><summary>↩ Tool result · `toolu_01SUnXqFzpBQiB2mirDS2xG6`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig2_auc_decay.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig3_transfer_heatmap.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig2_auc_decay.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig3_transfer_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_s1_auc_decay_ci.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.fls
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/pipeline.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/pipeline.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.blg
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/_pdf_images/main_p6.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e33aa2-6fa9-422f-acce-7e881a46fdce",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "555ab71a-0658-41b4-9772-bc1c6a415f1c",
  "sourceToolAssistantUUID": "35e33aa2-6fa9-422f-acce-7e881a46fdce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T10:12:19.799Z_

<details><summary>↩ Tool result · `toolu_01TZW1hudRAxt9KLmiSYAqHk`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-14
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{shi2025generalization,
31	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
32	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
33	  booktitle={Advances in NeurIPS},
34	  year={2025},
35	  url={https://arxiv.org/abs/2509.16499}
36	}
37	
38	@inproceedings{mitchell2023detectgpt,
39	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
40	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
41	  booktitle={Proceedings of ICML},
42	  year={2023}
43	}
44	
45	% === Should-Cite ===
46	
47	@article{basani2026diveye,
48	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
49	  author={Basani, Advik Raj and Chen, Pin-Yu},
50	  journal={Transactions on Machine Learning Research},
51	  year={2026},
52	  url={https://arxiv.org/abs/2509.18880}
53	}
54	
55	@inproceedings{amin2025escaping,
56	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
57	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
58	  booktitle={Advances in NeurIPS},
59	  year={2025},
60	  url={https://arxiv.org/abs/2502.08924}
61	}
62	
63	@inproceedings{zawalski2026codec,
64	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
65	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
66	  booktitle={Proceedings of ICLR},
67	  year={2026},
68	  url={https://arxiv.org/abs/2510.27055}
69	}
70	
71	@article{gambetta2025surplexity,
72	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},
73	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
74	  journal={arXiv preprint arXiv:2410.12341},
75	  year={2025},
76	  url={https://arxiv.org/abs/2410.12341}
77	}
78	
79	@inproceedings{zhang2024minkpp,
80	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
81	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
82	  booktitle={Proceedings of EMNLP},
83	  year={2024}
84	}
85	
86	@article{shumailov2024collapse,
87	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
88	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
89	  journal={Nature},
90	  volume={631},
91	  pages={755--759},
92	  year={2024}
93	}
94	
95	@inproceedings{alemohammad2024selfconsuming,
96	  title={Self-Consuming Generative Models Go {MAD}},
97	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},
98	  booktitle={Proceedings of ICLR},
99	  year={2024}
100	}
101	
102	@article{kaplan2020scaling,
103	  title={Scaling Laws for Neural Language Models},
104	  author={Kaplan, Jared and McCandlish, Sam and Henighan, Tom and Brown, Tom B. and Chess, Benjamin and Child, Rewon and Gray, Scott and Radford, Alec and Wu, Jeffrey and Amodei, Dario},
105	  journal={arXiv preprint arXiv:2001.08361},
106	  year={2020}
107	}
108	
109	@inproceedings{dohmatob2024model,
110	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
111	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
112	  booktitle={Proceedings of ICML},
113	  year={2024}
114	}
115	
116	@inproceedings{xie2023dsir,
117	  title={Data Selection with Importance Resampling},
118	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
119	  booktitle={Proceedings of ICML},
120	  year={2023}
121	}
122	
123	@inproceedings{tirumala2023d4,
124	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
125	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
126	  booktitle={Advances in NeurIPS},
127	  year={2023}
128	}
129	
130	@inproceedings{xie2023doremi,
131	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
132	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
133	  booktitle={Advances in NeurIPS},
134	  year={2023}
135	}
136	
137	@inproceedings{kirchenbauer2023watermark,
138	  title={A Watermark for Large Language Models},
139	  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
140	  booktitle={Proceedings of ICML},
141	  year={2023}
142	}
143	
144	@inproceedings{gehrmann2019gltr,
145	  title={{GLTR}: Statistical Detection and Visualization of Generated Text},
146	  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
147	  booktitle={Proceedings of ACL: System Demonstrations},
148	  year={2019}
149	}
150	
151	@inproceedings{hans2024binoculars,
152	  title={Spotting {LLMs} With Binoculars},
153	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
154	  booktitle={Proceedings of ICML},
155	  year={2024}
156	}
157	
158	@article{cao2020coral,
159	  title={Rank consistent ordinal regression for neural networks with application to age estimation},
160	  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
161	  journal={Pattern Recognition Letters},
162	  volume={140},
163	  pages={325--331},
164	  year={2020}
165	}
166	
167	@inproceedings{zellers2019grover,
168	  title={Defending Against Neural Fake News},
169	  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
170	  booktitle={Advances in NeurIPS},
171	  year={2019}
172	}
173	
174	@inproceedings{ippolito2020detection,
175	  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},
176	  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},
177	  booktitle={Proceedings of ACL},
178	  year={2020}
179	}
180	
181	% === Probing Classifiers ===
182	
183	@inproceedings{alain2017understanding,
184	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
185	  author={Alain, Guillaume and Bengio, Yoshua},
186	  booktitle={ICLR Workshop},
187	  year={2017}
188	}
189	
190	@inproceedings{conneau2018probing,
191	  title={What You Can Cram into a Single \$\&!\#* Vector: Probing Sentence Embeddings for Linguistic Properties},
192	  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\"\i}c and Baroni, Marco},
193	  booktitle={Proceedings of ACL},
194	  year={2018}
195	}
196	
197	@article{belinkov2022probing,
198	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
199	  author={Belinkov, Yonatan},
200	  journal={Computational Linguistics},
201	  volume={48},
202	  number={1},
203	  pages={207--219},
204	  year={2022}
205	}
206	
207	% === Model Collapse Avoidability ===
208	
209	@article{gerstgrasser2024inevitable,
210	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
211	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
212	  journal={arXiv preprint arXiv:2404.01413},
213	  year={2024},
214	  url={https://arxiv.org/abs/2404.01413}
215	}
216	
217	% === Ordinal Classification (additional) ===
218	
219	@inproceedings{dohmatob2025strong,
220	  title={Strong Model Collapse},
221	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
222	  booktitle={Proceedings of ICLR},
223	  year={2025},
224	  url={https://arxiv.org/abs/2410.04840}
225	}
226	
227	@inproceedings{feng2025beyond,
228	  title={Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},
229	  author={Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia},
230	  booktitle={Proceedings of ICLR},
231	  year={2025},
232	  url={https://arxiv.org/abs/2406.07515}
233	}
234	
235	@inproceedings{bao2024fast,
236	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
237	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
238	  booktitle={Proceedings of ICLR},
239	  year={2024},
240	  url={https://arxiv.org/abs/2310.05130}
241	}
242	
243	@inproceedings{frank2001ordinal,
244	  title={A Simple Approach to Ordinal Classification},
245	  author={Frank, Eibe and Hall, Mark},
246	  booktitle={Proceedings of ECML},
247	  pages={145--156},
248	  year={2001}
249	}
250	
251	% === New entries (added 2026-05-14) ===
252	
253	@inproceedings{cheng2025beyond,
254	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
255	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
256	  booktitle={Proceedings of the ACM Web Conference (WWW)},
257	  year={2025},
258	  url={https://arxiv.org/abs/2410.14259}
259	}
260	
261	@article{yi2025escaping,
262	  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
263	  author={Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
264	  journal={arXiv preprint arXiv:2510.16657},
265	  year={2025},
266	  url={https://arxiv.org/abs/2510.16657}
267	}
268	
269	@article{mehta2025beyond,
270	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
271	  author={Mehta, Sushant},
272	  journal={arXiv preprint arXiv:2511.17602},
273	  year={2025},
274	  url={https://arxiv.org/abs/2511.17602}
275	}
276	
277	% === AI-Generated Content Prevalence ===
278	
279	@inproceedings{sun2025aigt,
280	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
281	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
282	  booktitle={Proceedings of ACL},
283	  year={2025},
284	  url={https://arxiv.org/abs/2412.18148}
285	}
286	
287	@article{spennemann2025quantifying,
288	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
289	  author={Spennemann, Dirk H. R.},
290	  journal={arXiv preprint arXiv:2504.08755},
291	  year={2025},
292	  url={https://arxiv.org/abs/2504.08755}
293	}
294	
295	% === Continual Pretraining ===
296	
297	@inproceedings{gupta2023continual,
298	  title={Continual Pre-Training of Large Language Models: How to (re)warm your model?},
299	  author={Gupta, Kshitij and Th{\'e}rien, Benjamin and Ibrahim, Adam and Richter, Mats L. and Anthony, Quentin and Belilovsky, Eugene and Rish, Irina and Lesort, Timoth{\'e}e},
300	  booktitle={Proceedings of ICML},
301	  year={2023},
302	  url={https://arxiv.org/abs/2308.04014}
303	}
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd503391-6ec7-4d76-8390-0e5ec0555585",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "3528cd87-3446-4d9e-a3f6-bed07936f858",
  "sourceToolAssistantUUID": "cd503391-6ec7-4d76-8390-0e5ec0555585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T10:12:21.328Z_

Now let me search for these author names in the paper .tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3528cd87-3446-4d9e-a3f6-bed07936f858",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B96yosADW4LresnBxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afd48563-ac57-4ad6-a90f-a1e8bc3f32bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015ySCofBE6xjU8mZd6TPyig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7707,
      "cache_read_input_tokens": 20718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7707,
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

_source line 8 · 2026-05-15T10:12:22.443Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CRYE5d72QCnJww9QFNVVex`</summary>

```json
{
  "pattern": "Krishna|Sadasivan|Wei Hao|Hao 2025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afd48563-ac57-4ad6-a90f-a1e8bc3f32bd",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B96yosADW4LresnBxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a417ad36-fc98-4de4-87c1-318788bed416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015ySCofBE6xjU8mZd6TPyig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7707,
      "cache_read_input_tokens": 20718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7707,
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

_source line 9 · 2026-05-15T10:12:22.536Z_

<details><summary>↩ Tool result · `toolu_01CRYE5d72QCnJww9QFNVVex`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a417ad36-fc98-4de4-87c1-318788bed416",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "29aa3f99-4780-45dc-a417-ddf96e93b131",
  "sourceToolAssistantUUID": "a417ad36-fc98-4de4-87c1-318788bed416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T10:12:22.833Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014aGkTzaK1JZFTCm6kKi6EN`</summary>

```json
{
  "pattern": "krishna|sadasivan|wei.hao|hao2025",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29aa3f99-4780-45dc-a417-ddf96e93b131",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B96yosADW4LresnBxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce5de130-bf65-49a7-8800-9119e1417d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015ySCofBE6xjU8mZd6TPyig",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7707,
      "cache_read_input_tokens": 20718,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 274,
          "cache_read_input_tokens": 20718,
          "cache_creation_input_tokens": 7707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7707,
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

_source line 11 · 2026-05-15T10:12:22.852Z_

<details><summary>↩ Tool result · `toolu_014aGkTzaK1JZFTCm6kKi6EN`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce5de130-bf65-49a7-8800-9119e1417d02",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "4a3cef7d-7d7a-4f0d-aec6-6636d18577ea",
  "sourceToolAssistantUUID": "ce5de130-bf65-49a7-8800-9119e1417d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T10:12:24.128Z_

Let me search the main .tex files individually to check all content sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a3cef7d-7d7a-4f0d-aec6-6636d18577ea",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9L4cWeFkvYmWmw5Jy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "706ada34-3415-4c74-a734-11628e54a6b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5S6twnrsWWCL2dPmGHN3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 28425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 341,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 13 · 2026-05-15T10:12:24.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SFKPt9RLDZftwhud55iPiH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "706ada34-3415-4c74-a734-11628e54a6b1",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9L4cWeFkvYmWmw5Jy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1bc3e941-230b-43d3-8285-b51e6b740bcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5S6twnrsWWCL2dPmGHN3Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 28425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 341,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 14 · 2026-05-15T10:12:24.381Z_

<details><summary>↩ Tool result · `toolu_01SFKPt9RLDZftwhud55iPiH`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\newcommand{\Kstar}{{K^*}}
19	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
20	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
21	\newcommand{\auc}{\text{AUC}}
22	\newcommand{\jsd}{\text{JSD}}
23	
24	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\begin{abstract}
33	% D025: web contamination prevalence context
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations, with recent estimates suggesting that 10--40\% of content on some platforms is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kempirical$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kempirical=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield $\auc$ above $\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\% accuracy across continuation-mode generators, with binary (0-vs-1) $\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Neural probing yields $\Kempirical^{\text{neural}}=3$ for Qwen-continuation but $\Kempirical^{\text{neural}}=2$ for Pythia and OLMo, confirming $\Kempirical=2$ as a representation-independent lower bound while revealing model-dependent additional discriminability. Frontier LLMs achieve ${\sim}88\%$ binary detection but only ${\sim}33\%$ five-class depth accuracy---below our OBD classifier's 38.6\%---confirming depth estimation as a non-trivial task requiring specialized features. % D025: C3 adjusted from independent claim to supporting validation
35	Our findings motivate a three-tier taxonomy (human / generation-1 / generation-2+) for depth-aware data curation; $\Kempirical=2$ correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit---binary filtering at the $\Kempirical$ boundary ($0.5941$ MMLU) outperforms both graduated depth weighting and surprisal-based selection ($0.5894$), establishing $\Kempirical$ as an actionable curation guideline.
36	\end{abstract}
37	
38	% === Section 1: Introduction ===
39	\input{introduction}
40	
41	% === Section 2: Related Work ===
42	\input{related_work}
43	
44	% === Section 3: Method ===
45	\input{method}
46	
47	% === Section 4: Experiments ===
48	\input{experiments_c1}
49	
50	% === Section 5: K*-Aware Data Filtering ===
51	\input{experiments_c3}
52	
53	% === Section 6: Discussion ===
54	\input{discussion}
55	
56	% === Section 7: Conclusion ===
57	\input{conclusion}
58	
59	\bibliography{references}
60	
61	\input{appendix}
62	\input{appendix_extended}
63	
64	\end{document}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bc3e941-230b-43d3-8285-b51e6b740bcb",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "dfaf24a9-5f1f-4270-9990-623bdbb77680",
  "sourceToolAssistantUUID": "1bc3e941-230b-43d3-8285-b51e6b740bcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T10:12:24.913Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgcVWfKcavAGTNh47gJ3h5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfaf24a9-5f1f-4270-9990-623bdbb77680",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9L4cWeFkvYmWmw5Jy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fcaed080-245e-4949-81dc-f3bd051e00ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5S6twnrsWWCL2dPmGHN3Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 28425,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 248,
          "cache_read_input_tokens": 28425,
          "cache_creation_input_tokens": 341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 341,
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

_source line 16 · 2026-05-15T10:12:24.921Z_

<details><summary>↩ Tool result · `toolu_01FgcVWfKcavAGTNh47gJ3h5`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
8	
9	The gap cuts across three communities.
10	Binary detection methods~\cite{basani2026diveye, zhang2024minkpp, zawalski2026codec} produce no depth estimate.
11	The model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} characterizes recursive degradation at the macro level but provides no per-text depth estimation tool.
12	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
13	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
14	
15	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
16	We empirically measure $\Kempirical$---the maximum depth at which a classifier reliably distinguishes adjacent generations---using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
17	We operationalize $\Kempirical$ as the deepest $k$ where the bootstrap 95\% CI for pairwise $\auc_{k,k+1}$ exceeds $\theta = 0.60$.
18	
19	Our primary contribution is a systematic empirical characterization of $\Kempirical$:
20	\begin{enumerate}[label=(\alph*),nosep]
21	  \item \textbf{$\Kempirical = 2$} across 4 model-mode configurations and 4 decoding strategies (8 conditions), with all 1v2 CI lower bounds exceeding $\theta$ and all 2v3 CI upper bounds below $\theta$ (permutation $p \leq 0.002$).
22	  \item \textbf{Cross-model transfer}: 80--92\% accuracy retention across continuation-mode generators; 0v1 $\auc > 0.96$ across all pairs.
23	  \item \textbf{Feature degradation consistency}: Spearman $\rho \geq 0.85$ on single-feature rankings across continuation-mode models, with surprisal-variance features dominating.
24	  \item \textbf{Generation mode}: rewrite yields higher 1v2 $\auc$ ($+$8.4\,pp) but transfers poorly (61--63\% vs.\ 80--92\%).
25	\end{enumerate}
26	
27	\noindent As a secondary contribution, $\Kempirical = 2$ correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit: graduated filtering at its best ($\alpha{=}0.9$, MMLU $0.5892$) still falls short of binary-ours ($0.5941$), and surprisal-based selection ($0.5894$) likewise fails to improve (Section~\ref{sec:filtering}).
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcaed080-245e-4949-81dc-f3bd051e00ce",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "7dfbdc6e-64c1-4f1e-93a5-09f44beb966a",
  "sourceToolAssistantUUID": "fcaed080-245e-4949-81dc-f3bd051e00ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T10:12:24.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SbRRkKCDakbqJukriTJhLV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dfbdc6e-64c1-4f1e-93a5-09f44beb966a",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9L4cWeFkvYmWmw5Jy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e768a25f-e03b-437c-9bf3-ed673aa1cac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V5S6twnrsWWCL2dPmGHN3Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 28425,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 248,
          "cache_read_input_tokens": 28425,
          "cache_creation_input_tokens": 341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 341,
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

_source line 18 · 2026-05-15T10:12:24.943Z_

<details><summary>↩ Tool result · `toolu_01SbRRkKCDakbqJukriTJhLV`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse.}
5	Shumailov et al.~\cite{shumailov2024collapse} showed that iterative training on model outputs causes irreversible tail-distribution degradation.
6	Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for tail probability loss.
7	Schaeffer et al.~\cite{schaeffer2025position} organized the literature into eight definitions; our $\Kstar$ aligns with their Family~B (D4: collapsing variance, D6: mode entanglement).
8	Kazdan et al.~\cite{kazdan2025collapse} distinguished replace and accumulate regimes; our prompt-chain operates in the replace regime, making $\Kempirical = 2$ a conservative lower bound.
9	These works characterize macro dynamics but provide no per-text depth estimation tools.
10	
11	\paragraph{Binary Synthetic Text Detection.}
12	Detection methods---DetectGPT~\cite{mitchell2023detectgpt}, Fast-DetectGPT~\citep{bao2024fast}, Binoculars~\cite{hans2024binoculars}, DivEye~\cite{basani2026diveye}, Min-K\%++~\cite{zhang2024minkpp}, CoDeC~\cite{zawalski2026codec}---achieve strong human-vs.-machine separation but produce no depth estimate.
13	DivEye's surprisal diversity features overlap with our \texttt{surp\_*} subset, but optimize for binary detection rather than ordinal depth discrimination.
14	Recent work moves beyond binary labels along other axes: collaboration degree~\cite{cheng2025beyond} and contamination type hierarchies~\cite{mehta2025beyond}, but neither addresses recursive generation depth.
15	
16	\paragraph{Data Selection.}
17	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} improve corpus quality through distribution matching but ignore recursive depth.
18	Drayson et al.~\cite{drayson2025} combined binary detection with stratified importance resampling---a special case of our framework when $\Kstar = 1$.
19	Feng et al.~\cite{feng2025beyond} showed external verification can prevent collapse; our $\Kstar$ can inform such verifiers by delineating the depth frontier below which quality discrimination remains feasible.
20	
21	\paragraph{Ordinal Classification and Probing.}
22	Ordinal regression~\cite{frank2001ordinal, cao2020coral} exploits label ordering but has not been applied to synthetic text depth.
23	Our OBD head follows Frank \& Hall's binary decomposition principle.
24	Probing classifiers~\cite{alain2017understanding, conneau2018probing, belinkov2022probing} analyze pretrained representations; our neural probe follows this protocol with a controlled-capacity MLP on frozen embeddings.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e768a25f-e03b-437c-9bf3-ed673aa1cac7",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "b8b6a6b9-26e7-4cb9-aa45-7f68fa43940b",
  "sourceToolAssistantUUID": "e768a25f-e03b-437c-9bf3-ed673aa1cac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T10:12:26.193Z_

Let me check the other section files as well:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b6a6b9-26e7-4cb9-aa45-7f68fa43940b",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9V1sUcoJ1E5RU4nTU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12c27a5f-443a-47a3-a2c7-a6d54f90dc16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0158MPpAhTayQarag32Cs8wL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 20 · 2026-05-15T10:12:26.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_014eUbpwmuht56w6wmLc7WSE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12c27a5f-443a-47a3-a2c7-a6d54f90dc16",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9V1sUcoJ1E5RU4nTU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54518f71-7fed-46d9-a0de-7673a047bbf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0158MPpAhTayQarag32Cs8wL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 21 · 2026-05-15T10:12:26.984Z_

<details><summary>↩ Tool result · `toolu_014eUbpwmuht56w6wmLc7WSE`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k : \text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\theta = 0.60$ is justified by the permutation null distribution (95th percentile $< 0.55$ across all configurations; bootstrap: 1{,}000 resamples).
25	
26	\subsection{Features and Classifier}
27	\label{sec:features}
28	
29	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
30	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
31	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
32	
33	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
34	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
35	
36	\subsection{Experimental Setup}
37	\label{sec:experimental_setup}
38	
39	We evaluate four configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Pythia-1.4B and OLMo-1B (continuation).
40	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
41	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
42	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
43	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Experimental configurations.}
49	\label{tab:setup}
50	\begin{tabular}{llcc}
51	\toprule
52	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
53	\midrule
54	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
55	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
56	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
57	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54518f71-7fed-46d9-a0de-7673a047bbf4",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "bf4ab3bc-8ab2-4784-937c-dedcc3e919f9",
  "sourceToolAssistantUUID": "54518f71-7fed-46d9-a0de-7673a047bbf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T10:12:27.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GQEKHFC5Z7d5QuHPTGATUg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf4ab3bc-8ab2-4784-937c-dedcc3e919f9",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9V1sUcoJ1E5RU4nTU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79e5716f-7622-45d1-bb7f-2e3d2f2cef59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0158MPpAhTayQarag32Cs8wL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
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

_source line 23 · 2026-05-15T10:12:27.130Z_

<details><summary>↩ Tool result · `toolu_01GQEKHFC5Z7d5QuHPTGATUg`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Interpretation.}
5	The consistency of $\Kempirical = 2$ across all 8 tested configurations indicates that the two-step information bottleneck is a structural feature of autoregressive generation at the $\leq$1.5B scale.
6	The feature degradation analysis provides mechanistic evidence: surprisal-variance features degrade in a shared order across model families (Spearman $\rho \geq 0.85$), suggesting that each generation step smooths the token-level surprisal landscape in a model-independent fashion.
7	Cross-model neural probing reveals that $\Kempirical^{\text{neural}} = 3$ for Qwen-continuation but $\Kempirical^{\text{neural}} = 2$ for Pythia and OLMo; the Qwen elevation likely reflects self-familiarity artifacts in instruction-tuned embeddings rather than a universal signal, so $\Ktheory \geq 3$ can only be claimed for Qwen representations (Appendix~\ref{sec:extended_neural_probe}).
8	Extended theoretical discussion, including connections to model collapse theory and scale considerations, appears in Appendix~\ref{sec:extended_discussion}.
9	
10	\paragraph{Practical implications.}
11	The implied three-tier taxonomy (human / generation-1 / generation-2+) requires no per-model or per-decoding-strategy calibration.
12	Cross-model transfer (80--92\% accuracy retention; Section~\ref{sec:transfer}) enables deployment without generator-specific retraining.
13	Our filtering experiments (Section~\ref{sec:filtering}) show that binary filtering at the $\Kempirical{=}2$ boundary is the most effective strategy among those tested; graduated strategies offer no additional benefit.
14	Frontier LLMs achieve ${\sim}88\%$ binary detection but only ${\sim}33\%$ five-class depth accuracy (below OBD's 38.6\%), confirming that depth estimation requires specialized features (Appendix~\ref{sec:extended_llm}).
15	
16	\paragraph{Limitations.}
17	Our findings are bounded by (1)~model scale ($\leq$1.5B), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ shifts from 3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; our conclusions are conditioned on $\theta{=}0.60$), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.15\,pp), (7)~the 15D feature set yields an operational lower bound ($\Ktheory$ may be strictly higher), and (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal.
18	Detailed limitation analysis appears in Appendix~\ref{sec:extended_limitations}.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79e5716f-7622-45d1-bb7f-2e3d2f2cef59",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "f4abca60-fe4e-4354-a32c-4194fea93183",
  "sourceToolAssistantUUID": "79e5716f-7622-45d1-bb7f-2e3d2f2cef59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T10:12:27.413Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G72FPerzsy96ATfiPDMDXX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4abca60-fe4e-4354-a32c-4194fea93183",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9V1sUcoJ1E5RU4nTU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5fdc1cbd-249e-424a-adc5-45ce9191a3e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0158MPpAhTayQarag32Cs8wL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28766,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 259,
          "cache_read_input_tokens": 28766,
          "cache_creation_input_tokens": 3391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3391,
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

_source line 25 · 2026-05-15T10:12:27.423Z_

<details><summary>↩ Tool result · `toolu_01G72FPerzsy96ATfiPDMDXX`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	  \centering
6	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
7	  \caption{Pairwise $\auc$ decay curves for four model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
8	  \label{fig:s1_auc_decay_ci}
9	\end{figure}
10	
11	\section{Supplementary Tables}
12	
13	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
14	\begin{table*}[t]
15	  \centering
16	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
17	  \label{tab:s1_transfer}
18	  \begin{tabular}{lcccc}
19	    \toprule
20	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
21	    \cmidrule(lr){2-5}
22	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
23	    \midrule
24	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
25	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
26	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
27	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
28	    \bottomrule
29	  \end{tabular}
30	  \vspace{4pt}
31	
32	  \footnotesize
33	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
34	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
35	\end{table*}
36	
37	%%% Table S2: Decoding Ablation AUC (exp-003)
38	\begin{table*}[t]
39	  \centering
40	  \caption{Pairwise AUC across depth pairs for four decoding configurations. The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$: pairs above this line are reliably separable ($\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings across decoding configurations.}
41	  \label{tab:s2_decoding}
42	  \begin{tabular}{lcccc}
43	    \toprule
44	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
45	    \midrule
46	    0 vs.\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\
47	    1 vs.\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\
48	    \cmidrule(lr){1-5}
49	    2 vs.\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\
50	    3 vs.\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\
51	    4 vs.\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\
52	    \midrule
53	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
54	    \midrule
55	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
56	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
57	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
58	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
59	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
60	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
61	    \bottomrule
62	  \end{tabular}
63	\end{table*}
64	
65	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
66	\begin{table*}[t]
67	  \centering
68	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
69	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
70	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
71	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
72	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
73	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
74	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
75	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.}
76	  \label{tab:s3_llm_zeroshot}
77	
78	  \vspace{0.5em}
79	  \begin{subtable}{0.48\textwidth}
80	    \centering
81	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
82	    \label{tab:s3a_gpt55}
83	    \small
84	    \begin{tabular}{lcccccc}
85	      \toprule
86	      & \multicolumn{5}{c}{Predicted Depth} & \\
87	      \cmidrule(lr){2-6}
88	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
89	      \midrule
90	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
91	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
92	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
93	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
94	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
95	      \bottomrule
96	    \end{tabular}
97	  \end{subtable}
98	  \hfill
99	  \begin{subtable}{0.48\textwidth}
100	    \centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fdc1cbd-249e-424a-adc5-45ce9191a3e2",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "fb8deb47-950b-4752-878f-b8bb6cf8280a",
  "sourceToolAssistantUUID": "5fdc1cbd-249e-424a-adc5-45ce9191a3e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T10:12:31.236Z_

Now let me do a comprehensive search in the bibliography file for variations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb8deb47-950b-4752-878f-b8bb6cf8280a",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9fg4uTADpawvsysv9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce5a315d-4ec4-4176-84c7-ea9526a2cfec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lm97qFzYXgriNNykS9oQ6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5177,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5177,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 27 · 2026-05-15T10:12:32.176Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NXxALpgbb2DWs94jZpJpij`</summary>

```json
{
  "pattern": "@\\w+\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce5a315d-4ec4-4176-84c7-ea9526a2cfec",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4B9fg4uTADpawvsysv9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52fe58de-69a3-4f7c-8551-b8cb8cdfc33f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lm97qFzYXgriNNykS9oQ6i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5177,
      "cache_read_input_tokens": 32157,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 144,
          "cache_read_input_tokens": 32157,
          "cache_creation_input_tokens": 5177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5177,
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

_source line 28 · 2026-05-15T10:12:32.194Z_

<details><summary>↩ Tool result · `toolu_01NXxALpgbb2DWs94jZpJpij`</summary>

```text
6:@inproceedings{drayson2025,
14:@inproceedings{schaeffer2025position,
22:@inproceedings{kazdan2025collapse,
30:@inproceedings{shi2025generalization,
38:@inproceedings{mitchell2023detectgpt,
47:@article{basani2026diveye,
55:@inproceedings{amin2025escaping,
63:@inproceedings{zawalski2026codec,
71:@article{gambetta2025surplexity,
79:@inproceedings{zhang2024minkpp,
86:@article{shumailov2024collapse,
95:@inproceedings{alemohammad2024selfconsuming,
102:@article{kaplan2020scaling,
109:@inproceedings{dohmatob2024model,
116:@inproceedings{xie2023dsir,
123:@inproceedings{tirumala2023d4,
130:@inproceedings{xie2023doremi,
137:@inproceedings{kirchenbauer2023watermark,
144:@inproceedings{gehrmann2019gltr,
151:@inproceedings{hans2024binoculars,
158:@article{cao2020coral,
167:@inproceedings{zellers2019grover,
174:@inproceedings{ippolito2020detection,
183:@inproceedings{alain2017understanding,
190:@inproceedings{conneau2018probing,
197:@article{belinkov2022probing,
209:@article{gerstgrasser2024inevitable,
219:@inproceedings{dohmatob2025strong,
227:@inproceedings{feng2025beyond,
235:@inproceedings{bao2024fast,
243:@inproceedings{frank2001ordinal,
253:@inproceedings{cheng2025beyond,
261:@article{yi2025escaping,
269:@article{mehta2025beyond,
279:@inproceedings{sun2025aigt,
287:@article{spennemann2025quantifying,
297:@inproceedings{gupta2023continual,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52fe58de-69a3-4f7c-8551-b8cb8cdfc33f",
  "isSidechain": true,
  "promptId": "44c21223-413f-4250-b24e-c80a5feb1f36",
  "agentId": "a8ac91885028ee045",
  "type": "user",
  "uuid": "edbf7d19-442d-42a6-848b-8098fca6d9bd",
  "sourceToolAssistantUUID": "52fe58de-69a3-4f7c-8551-b8cb8cdfc33f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T10:12:37.781Z_

Based on my comprehensive search across the paper files and bibliography, here are my findings:

## Summary of Citation Search Results

I searched all paper files (introduction.tex, related_work.tex, method.tex, discussion.tex, appendix.tex, and main.tex) plus the complete references.bib file for the three authors/citations you specified:

**Status: All three citations are ABSENT from the bibliography and the paper files.**

1. **Krishna** - No matches found in any paper section or in references.bib
2. **Sadasivan** - No matches found in any paper section or in references.bib
3. **Wei Hao** or **Hao 2025** - No matches found in any paper section or in references.bib

The references.bib file contains 37 entries total (ranging from 2017-2026), with key citations like:
- drayson2025
- schaeffer2025position
- kazdan2025collapse
- shi2025generalization
- mitchell2023detectgpt
- basani2026diveye
- And 31 others

None of these bib keys correspond to authors Krishna, Sadasivan, or Wei Hao. Therefore, these three citations are **genuinely missing** from the bibliography and are not currently referenced anywhere in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edbf7d19-442d-42a6-848b-8098fca6d9bd",
  "isSidechain": true,
  "agentId": "a8ac91885028ee045",
  "requestId": "req_011Cb4BA22RzgJqpFetnjgtQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c315dc26-770c-480a-9338-021945e4f851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "92a9857b-9182-409f-acb8-dd1f4819436d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "memoized-stirring-shamir",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3R1DMERWAPV5ZPhnjVdpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 37334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 719,
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
