# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, fi

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a579de2625c7cd6d9.jsonl`
- **Structured JSON:** [`bc57937bba60ee9061ee.json`](../../sessions/bc/bc57937bba60ee9061ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-23T13:08:44.892Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, find the .bib file(s) and check whether these references exist:
1. PL-Marker (ye2022plmarker or ye2022packed or similar)
2. DyGIE++ (wadden2019 or dygie)
3. Guidance (microsoft guidance)
4. DeepStruct (wang2022deepstruct or similar)
5. PURE (zhong2021 or zhong2021pure)

Also check if "wadhwa2023revisiting" exists. Report which ones are present and which are missing, with their bib keys if found. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "45747d8d-ecf2-4cc5-a5a6-902c404d22a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T13:08:46.725Z_

I'll search for the .bib files in that directory and check for the references you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45747d8d-ecf2-4cc5-a5a6-902c404d22a8",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ4hhqoobHVHX7pS1vL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2306a5e7-e76e-4dbe-811e-d749a98c7cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhQpjWpGsZvHvfpwisdSVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39711,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39711,
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

_source line 3 · 2026-05-23T13:08:47.038Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HhqS3XEu5K3GTBAWkYrBkE`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2306a5e7-e76e-4dbe-811e-d749a98c7cf2",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ4hhqoobHVHX7pS1vL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da5e16dc-4ed7-4c2d-92b5-3128944fe9d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RhQpjWpGsZvHvfpwisdSVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39711,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39711,
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

_source line 4 · 2026-05-23T13:08:47.071Z_

<details><summary>↩ Tool result · `toolu_01HhqS3XEu5K3GTBAWkYrBkE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/new_citations.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da5e16dc-4ed7-4c2d-92b5-3128944fe9d2",
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "2d70a652-7379-4ecd-a406-484118c1d9b0",
  "sourceToolAssistantUUID": "da5e16dc-4ed7-4c2d-92b5-3128944fe9d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T13:08:48.467Z_

Now let me read both .bib files to check for the references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d70a652-7379-4ecd-a406-484118c1d9b0",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ4s1Rq2TzbgppMFeBQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01befb33-b289-4620-b812-4ba9948b798c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENdz6dcnVC1669PNnXQ6Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 39711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
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

_source line 6 · 2026-05-23T13:08:48.688Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UFu1EEDDDWXUvQmJVfqhyG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/new_citations.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01befb33-b289-4620-b812-4ba9948b798c",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ4s1Rq2TzbgppMFeBQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb882fdb-c3a7-4050-9c9c-5be3a70b4b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENdz6dcnVC1669PNnXQ6Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 39711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
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

_source line 7 · 2026-05-23T13:08:48.695Z_

<details><summary>↩ Tool result · `toolu_01UFu1EEDDDWXUvQmJVfqhyG`</summary>

```text
1	% New citations for schema_semantic_constrained_ie
2	% Generated 2026-05-18
3	% All entries moved to relwork_new_entries.bib; this file kept empty to avoid duplicate key errors.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb882fdb-c3a7-4050-9c9c-5be3a70b4b54",
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "9eb3bc47-301d-41d8-9cf6-612fe5560117",
  "sourceToolAssistantUUID": "bb882fdb-c3a7-4050-9c9c-5be3a70b4b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T13:08:48.913Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XrnY3GVBP6tfy1FUj5W7jz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eb3bc47-301d-41d8-9cf6-612fe5560117",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ4s1Rq2TzbgppMFeBQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd45e269-bfae-4614-8bc1-fe4f29f809ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ENdz6dcnVC1669PNnXQ6Ni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 39711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
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

_source line 9 · 2026-05-23T13:08:49.211Z_

<details><summary>↩ Tool result · `toolu_01XrnY3GVBP6tfy1FUj5W7jz`</summary>

```text
1	% ============================================================
2	% Merged authoritative BibTeX references
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% vLLM — used for GCD-equivalence verification experiment
7	@inproceedings{kwon2023vllm,
8	  title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
9	  author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph and Zhang, Hao and Stoica, Ion},
10	  booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)},
11	  year      = {2023},
12	}
13	
14	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
15	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
16	@inproceedings{synchromesh_iclr2022,
17	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
18	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
19	  booktitle = {International Conference on Learning Representations},
20	  year      = {2022},
21	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
22	}
23	
24	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
25	@inproceedings{mgd_neurips2023,
26	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
27	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
28	  booktitle = {Advances in Neural Information Processing Systems},
29	  volume    = {36},
30	  year      = {2023},
31	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
32	}
33	
34	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
35	@article{pldi2025_type_constrained_codegen,
36	  title     = {Type-Constrained Code Generation with Language Models},
37	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
38	  journal   = {Proceedings of the ACM on Programming Languages},
39	  volume    = {9},
40	  number    = {PLDI},
41	  year      = {2025},
42	  doi       = {10.1145/3729274},
43	  url       = {https://dl.acm.org/doi/10.1145/3729274}
44	}
45	
46	% Confirmed via: ACL Anthology W04-2401, scottyih.org
47	% WARNING: cite key suggests AAAI 2004, but actual venue is CoNLL 2004 at HLT-NAACL
48	@inproceedings{roth_yih_2004,
49	  title     = {A Linear Programming Formulation for Global Inference in Natural Language Tasks},
50	  author    = {Roth, Dan and Yih, Wen-tau},
51	  booktitle = {Proceedings of the Eighth Conference on Computational Natural Language Learning ({CoNLL}-2004) at {HLT}-{NAACL} 2004},
52	  pages     = {1--8},
53	  year      = {2004},
54	  address   = {Boston, Massachusetts, USA},
55	  url       = {https://aclanthology.org/W04-2401/}
56	}
57	
58	% Confirmed via: ACL Anthology 2023.findings-emnlp.425, zjunlp/AdaKGC GitHub
59	@inproceedings{adakgc_emnlp2023,
60	  title     = {Schema-adaptable Knowledge Graph Construction},
61	  author    = {Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu},
62	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2023},
63	  pages     = {6408--6431},
64	  year      = {2023},
65	  url       = {https://aclanthology.org/2023.findings-emnlp.425/}
66	}
67	
68	% Confirmed via: ACL Anthology 2024.acl-long.475, arXiv:2403.07969
69	@inproceedings{knowcoder_acl2024,
70	  title     = {{KnowCoder}: Coding Structured Knowledge into {LLMs} for Universal Information Extraction},
71	  author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
72	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
73	  pages     = {8758--8779},
74	  year      = {2024},
75	  address   = {Bangkok, Thailand},
76	  url       = {https://aclanthology.org/2024.acl-long.475/}
77	}
78	
79	% Confirmed via: Oxford Academic Bioinformatics btae104, PubMed 38383067
80	@article{spires_2024,
81	  title     = {Structured Prompt Interrogation and Recursive Extraction of Semantics ({SPIRES}): A Method for Populating Knowledge Bases Using Zero-shot Learning},
82	  author    = {Caufield, J. Harry and Hegde, Harshad and Emonet, Vincent and Harris, Nomi L. and Joachimiak, Marcin P. and Matentzoglu, Nicolas and Kim, HyeongSik and Moxon, Sierra and Reese, Justin T. and Haendel, Melissa A. and Robinson, Peter N. and Mungall, Christopher J.},
83	  journal   = {Bioinformatics},
84	  volume    = {40},
85	  number    = {3},
86	  pages     = {btae104},
87	  year      = {2024},
88	  doi       = {10.1093/bioinformatics/btae104},
89	  url       = {https://academic.oup.com/bioinformatics/article/40/3/btae104/7612230}
90	}
91	
92	% Confirmed via: arXiv:2510.01409, Wiley Advanced Intelligent Systems doi:10.1002/aisy.202501381
93	@misc{ontologx_2025,
94	  title         = {{OntoLogX}: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models},
95	  author        = {Cotti, Luca and Drago, Idilio and Rula, Anisa and Bianchini, Devis and Cerutti, Federico},
96	  year          = {2025},
97	  eprint        = {2510.01409},
98	  archiveprefix = {arXiv},
99	  primaryclass  = {cs.AI},
100	  url           = {https://arxiv.org/abs/2510.01409}
101	}
102	
103	% Confirmed via: Springer LNCS 15370, arXiv:2411.15666, Lama-West GitHub
104	@inproceedings{ekaw2024_ontology_beam,
105	  title     = {Ontology-Constrained Generation of Domain-Specific Clinical Summaries},
106	  author    = {Mehenni, Gaya and Zouaq, Amal},
107	  booktitle = {Knowledge Engineering and Knowledge Management ({EKAW} 2024)},
108	  series    = {Lecture Notes in Computer Science},
109	  volume    = {15370},
110	  pages     = {382--398},
111	  year      = {2024},
112	  publisher = {Springer},
113	  doi       = {10.1007/978-3-031-77792-9_23}
114	}
115	
116	% ============================================================
117	% New entries added 2026-05-14 for §6 related work expansion
118	% ============================================================
119	
120	% Confirmed via: ACL Anthology 2021.emnlp-main.779, arXiv:2109.05093, GitHub ServiceNow/picard
121	@inproceedings{scholak2021picard,
122	  title     = {{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},
123	  author    = {Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},
124	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
125	  year      = {2021},
126	  url       = {https://aclanthology.org/2021.emnlp-main.779/}
127	}
128	
129	% Confirmed via: arXiv:2509.19057, ResearchGate, OpenReview gcG8dmAUNh
130	@article{olasunkanmi2025relate,
131	  title   = {{RELATE}: Relation Extraction in Biomedical Abstracts with {LLMs} and Ontology Constraints},
132	  author  = {Olasunkanmi, Olawumi and Satusky, Mathew and Yi, Hong and Bizon, Chris and Lee, Harlin and Ahalt, Stanley},
133	  journal = {arXiv preprint arXiv:2509.19057},
134	  year    = {2025},
135	  url     = {https://arxiv.org/abs/2509.19057}
136	}
137	
138	% Confirmed via: arXiv:2602.03439, University of Cambridge / The World Avatar project
139	@article{zhou2026ontologytools,
140	  title   = {Ontology-to-tools compilation for executable semantic constraint enforcement in {LLM} agents},
141	  author  = {Zhou, Xiaochi and Bulter, Patrick and Yang, Changxuan and Rihm, Simon D. and Angkanaporn, Thitikarn and Akroyd, Jethro and Mosbach, Sebastian and Kraft, Markus},
142	  journal = {arXiv preprint arXiv:2602.03439},
143	  year    = {2026},
144	  url     = {https://arxiv.org/abs/2602.03439}
145	}
146	
147	% Confirmed via: IOS Press ECAI 2020 FAIA vol.325, arXiv:1909.07755, GitHub lavis-nlp/spert
148	@inproceedings{eberts2020spert,
149	  title     = {Span-based Joint Entity and Relation Extraction with Transformer Pre-training},
150	  author    = {Eberts, Markus and Ulges, Adrian},
151	  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ({ECAI} 2020)},
152	  series    = {Frontiers in Artificial Intelligence and Applications},
153	  volume    = {325},
154	  pages     = {2006--2013},
155	  year      = {2020},
156	  doi       = {10.3233/FAIA200321}
157	}
158	
159	% Confirmed via: ACL Anthology 2021.emnlp-main.17, arXiv:2108.12202
160	% NOTE: venue is EMNLP 2021 (NOT AAAI 2021)
161	@inproceedings{yan2021pfn,
162	  title     = {A Partition Filter Network for Joint Entity and Relation Extraction},
163	  author    = {Yan, Zhiheng and Zhang, Chong and Fu, Jinlan and Zhang, Qi and Wei, Zhongyu},
164	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
165	  pages     = {185--197},
166	  year      = {2021},
167	  url       = {https://aclanthology.org/2021.emnlp-main.17/}
168	}
169	
170	% Confirmed via: ACL Anthology 2021.naacl-main.5, GitHub princeton-nlp/PURE
171	@inproceedings{zhong2021frustratingly,
172	  title     = {A Frustratingly Easy Approach for Entity and Relation Extraction},
173	  author    = {Zhong, Zexuan and Chen, Danqi},
174	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
175	  pages     = {50--61},
176	  year      = {2021},
177	  address   = {Online},
178	  publisher = {Association for Computational Linguistics},
179	  url       = {https://aclanthology.org/2021.naacl-main.5}
180	}
181	
182	% Confirmed via: ACL Anthology 2022.acl-long.337, GitHub thunlp/PL-Marker
183	@inproceedings{ye2022packed,
184	  title     = {Packed Levitated Marker for Entity and Relation Extraction},
185	  author    = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},
186	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
187	  pages     = {4904--4917},
188	  year      = {2022},
189	  address   = {Dublin, Ireland},
190	  publisher = {Association for Computational Linguistics},
191	  url       = {https://aclanthology.org/2022.acl-long.337}
192	}
193	
194	% Confirmed via: arXiv:2604.06066 (previously PENDING AUDIT — now verified)
195	@article{zhou2026snowballing,
196	  title   = {From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in {LLM} Reflection},
197	  author  = {Zhou, Hongxu},
198	  journal = {arXiv preprint arXiv:2604.06066},
199	  year    = {2026},
200	  url     = {https://arxiv.org/abs/2604.06066}
201	}
202	
203	% ============================================================
204	% Batch 1: Constrained decoding + IE foundations (10 entries)
205	% ============================================================
206	
207	% Confirmed via: arXiv 2411.15100, MLSys 2025 proceedings
208	@inproceedings{dong2025xgrammar,
209	  title     = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
210	  author    = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
211	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
212	  year      = {2025},
213	  url       = {https://arxiv.org/abs/2411.15100}
214	}
215	
216	% Confirmed via: arXiv 2307.09702
217	@article{willard2023outlines,
218	  title   = {Efficient Guided Generation for Large Language Models},
219	  author  = {Willard, Brandon T. and Louf, R{\'e}mi},
220	  journal = {arXiv preprint arXiv:2307.09702},
221	  year    = {2023},
222	  url     = {https://arxiv.org/abs/2307.09702}
223	}
224	
225	% Confirmed via: ACM DL 10.1145/3591300, PLDI 2023
226	@inproceedings{beurer-kellner2023lmql,
227	  title     = {Prompting Is Programming: A Query Language for Large Language Models},
228	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
229	  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)},
230	  year      = {2023},
231	  url       = {https://doi.org/10.1145/3591300}
232	}
233	
234	% Confirmed via: PMLR v235, ICML 2024
235	@inproceedings{beurer-kellner2024domino,
236	  title     = {Guiding {LLMs} The Right Way: Fast, Non-Invasive Constrained Generation},
237	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
238	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
239	  pages     = {3658--3673},
240	  year      = {2024},
241	  series    = {PMLR},
242	  volume    = {235},
243	  url       = {https://proceedings.mlr.press/v235/beurer-kellner24a.html}
244	}
245	
246	% Confirmed via: NeurIPS 2024 proceedings, OpenReview
247	@inproceedings{park2024grammar,
248	  title     = {Grammar-Aligned Decoding},
249	  author    = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
250	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
251	  year      = {2024},
252	  url       = {https://arxiv.org/abs/2405.21047}
253	}
254	
255	% Confirmed via: OpenReview, ICLR 2021
256	@inproceedings{decao2021genre,
257	  title     = {Autoregressive Entity Retrieval},
258	  author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},
259	  booktitle = {International Conference on Learning Representations (ICLR)},
260	  year      = {2021},
261	  url       = {https://openreview.net/forum?id=5k8F6UU39V}
262	}
263	
264	% Confirmed via: ACL Anthology 2022.naacl-main.342
265	@inproceedings{josifoski2022genie,
266	  title     = {{GenIE}: Generative Information Extraction},
267	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
268	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
269	  pages     = {4626--4643},
270	  year      = {2022},
271	  url       = {https://aclanthology.org/2022.naacl-main.342/}
272	}
273	
274	% Confirmed via: ACL Anthology 2023.emnlp-main.674
275	@inproceedings{geng2023gcd,
276	  title     = {Grammar-Constrained Decoding for Structured {NLP} Tasks without Finetuning},
277	  author    = {Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert},
278	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
279	  year      = {2023},
280	  url       = {https://aclanthology.org/2023.emnlp-main.674/}
281	}
282	
283	% Confirmed via: ACL Anthology 2021.naacl-main.339
284	@inproceedings{lu2021neurologic,
285	  title     = {{NeuroLogic} Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints},
286	  author    = {Lu, Ximing and West, Peter and Zellers, Rowan and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
287	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
288	  pages     = {4288--4299},
289	  year      = {2021},
290	  url       = {https://aclanthology.org/2021.naacl-main.339/}
291	}
292	
293	% Confirmed via: ACL Anthology 2022.acl-long.395
294	@inproceedings{lu2022uie,
295	  title     = {Unified Structure Generation for Universal Information Extraction},
296	  author    = {Lu, Yaojie and Liu, Qing and Dai, Dai and Xiao, Xinyan and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},
297	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
298	  pages     = {5755--5772},
299	  year      = {2022},
300	  url       = {https://aclanthology.org/2022.acl-long.395/}
301	}
302	
303	% ============================================================
304	% Batch 2: 10 entries added 2026-05-14
305	% ============================================================
306	
307	% Confirmed via: ICLR 2024 proceedings, OpenReview Y3wpuxd7u9, arXiv:2310.03668
308	@inproceedings{sainz2024gollie,
309	  title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling},
310	  author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
311	  booktitle = {The Twelfth International Conference on Learning Representations},
312	  year      = {2024},
313	  url       = {https://openreview.net/forum?id=Y3wpuxd7u9}
314	}
315	
316	% Confirmed via: ACL Anthology 2023.acl-long.855, arXiv:2305.05711
317	@inproceedings{li2023codeie,
318	  title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
319	  author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
320	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
321	  pages     = {15339--15353},
322	  year      = {2023},
323	  address   = {Toronto, Canada},
324	  url       = {https://aclanthology.org/2023.acl-long.855/}
325	}
326	
327	% Confirmed via: ACL Anthology 2024.emnlp-main.419, arXiv:2405.05008, GitHub THU-KEG/ADELIE
328	@inproceedings{qi2024adelie,
329	  title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
330	  author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
331	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
332	  year      = {2024},
333	  address   = {Miami, Florida, USA},
334	  url       = {https://aclanthology.org/2024.emnlp-main.419/}
335	}
336	
337	% Confirmed via: arXiv:2404.12493, GitHub urchade/EnriCo
338	% NOTE: arXiv preprint; no conference publication found
339	@article{zaratiana2024enrico,
340	  title   = {{EnriCo}: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction},
341	  author  = {Zaratiana, Urchade and Tomeh, Nadi and Dauxais, Yann and Holat, Pierre and Charnois, Thierry},
342	  journal = {arXiv preprint arXiv:2404.12493},
343	  year    = {2024},
344	  url     = {https://arxiv.org/abs/2404.12493}
345	}
346	
347	% Confirmed via: arXiv:2509.04696, Apple ML Research machinelearning.apple.com/research/odke
348	% NOTE: cite key uses "odke"; actual paper title is "ODKE+"
349	@article{khorshidi2025odke,
350	  title   = {{ODKE+}: Ontology-Guided Open-Domain Knowledge Extraction with {LLMs}},
351	  author  = {Khorshidi, Samira and Nikfarjam, Azadeh and Shankar, Suprita and Sang, Yisi and Govind, Yash and Jang, Hyun and Kasgari, Ali and McClimans, Alexis and Soliman, Mohamed and Konda, Vishnu and Fakhry, Ahmed and Qi, Xiaoguang},
352	  journal = {arXiv preprint arXiv:2509.04696},
353	  year    = {2025},
354	  url     = {https://arxiv.org/abs/2509.04696}
355	}
356	
357	% Confirmed via: ACL Anthology 2023.findings-eacl.95
358	@inproceedings{upadhyay2023openie,
359	  title     = {Open Information Extraction with Entity Focused Constraints},
360	  author    = {Upadhyay, Prajna and Balalau, Oana and Manolescu, Ioana},
361	  booktitle = {Findings of the Association for Computational Linguistics: {EACL} 2023},
362	  year      = {2023},
363	  url       = {https://aclanthology.org/2023.findings-eacl.95/}
364	}
365	
366	% Confirmed via: ACL Anthology 2025.genaik-1.10, GenAIK Workshop at COLING 2025
367	@inproceedings{regino2025kgcurator,
368	  title     = {Can {LLMs} be Knowledge Graph Curators for Validating Triple Insertions?},
369	  author    = {Regino, Andr{\'e} Gomes and dos Reis, Julio Cesar},
370	  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK}) at {COLING} 2025},
371	  pages     = {87--99},
372	  year      = {2025},
373	  address   = {Abu Dhabi, UAE},
374	  url       = {https://aclanthology.org/2025.genaik-1.10/}
375	}
376	
377	% Confirmed via: ACL Anthology 2024.emnlp-industry.91, arXiv:2408.02442
378	@inproceedings{tam2024letmespeak,
379	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
380	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
381	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
382	  pages     = {1218--1236},
383	  year      = {2024},
384	  address   = {Miami, Florida, US},
385	  url       = {https://aclanthology.org/2024.emnlp-industry.91/}
386	}
387	
388	% Confirmed via: PMLR v267/banerjee25a, ICML 2025, arXiv:2502.09061
389	@inproceedings{banerjee2025crane,
390	  title     = {{CRANE}: Reasoning with Constrained {LLM} Generation},
391	  author    = {Banerjee, Debangshu and Suresh, Tarun and Ugare, Shubham and Misailovic, Sasa and Singh, Gagandeep},
392	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
393	  pages     = {2836--2857},
394	  year      = {2025},
395	  url       = {https://proceedings.mlr.press/v267/banerjee25a.html}
396	}
397	
398	% Confirmed via: ACL Anthology 2025.ranlp-1.124
399	@inproceedings{schall2025hiddencost,
400	  title     = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
401	  author    = {Schall, Maximilian and de Melo, Gerard},
402	  booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing ({RANLP} 2025)},
403	  year      = {2025},
404	  address   = {Varna, Bulgaria},
405	  url       = {https://aclanthology.org/2025.ranlp-1.124/}
406	}
407	
408	% ============================================================
409	% D015 reviewer-requested references (5 entries)
410	% ============================================================
411	
412	% Confirmed via: ACL Anthology 2021.findings-emnlp.204, GitHub Babelscape/rebel
413	@inproceedings{cabot2021rebel,
414	  title     = {{REBEL}: Relation Extraction By End-to-end Language Generation},
415	  author    = {Huguet Cabot, Pere-Llu{\'\i}s and Navigli, Roberto},
416	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},
417	  pages     = {2370--2381},
418	  year      = {2021},
419	  url       = {https://aclanthology.org/2021.findings-emnlp.204/}
420	}
421	
422	% ============================================================
423	% Batch 3: New entries added 2026-05-16 (3 entries, Director-requested)
424	% ============================================================
425	
426	% Confirmed via: arXiv:2403.01632, OpenReview HiUZtgAPoH
427	% FIX: venue is TMLR (not ICML 2024)
428	@article{ugare2024syncode,
429	  title     = {{SynCode}: {LLM} Generation with Grammar Augmentation},
430	  author    = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},
431	  journal   = {Transactions on Machine Learning Research},
432	  year      = {2024},
433	  url       = {https://openreview.net/forum?id=HiUZtgAPoH}
434	}
435	
436	% Confirmed via: OpenReview ac93gRzxxV, ICLR 2025 poster page, arXiv:2410.07295
437	% FIX: replaced wrong author Banerjee with correct author Gumaste
438	@inproceedings{ugare2025itergen,
439	  title     = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},
440	  author    = {Ugare, Shubham and Gumaste, Rohan and Suresh, Tarun and Singh, Gagandeep and Misailovic, Sasa},
441	  booktitle = {The Thirteenth International Conference on Learning Representations},
442	  year      = {2025},
443	  url       = {https://openreview.net/forum?id=ac93gRzxxV}
444	}
445	
446	% Confirmed via: ACL Anthology 2025.emnlp-main.926, arXiv:2506.14901
447	% FIX: removed fabricated authors Geng/Josifoski (they co-authored geng2023gcd, not this paper)
448	@inproceedings{boostcd2025,
449	  title     = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},
450	  author    = {Sakota, Marija and West, Robert},
451	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
452	  year      = {2025},
453	  url       = {https://aclanthology.org/2025.emnlp-main.926/}
454	}
455	
456	% ============================================================
457	% Dataset & model references (5 entries)
458	% ============================================================
459	
460	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
461	@inproceedings{luan2018scierc,
462	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
463	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
464	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
465	  pages     = {3219--3232},
466	  year      = {2018},
467	  address   = {Brussels, Belgium},
468	  url       = {https://aclanthology.org/D18-1360/}
469	}
470	
471	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
472	@inproceedings{yao2019docred,
473	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
474	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
475	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
476	  pages     = {764--777},
477	  year      = {2019},
478	  address   = {Florence, Italy},
479	  url       = {https://aclanthology.org/P19-1074/}
480	}
481	
482	% Confirmed via: arXiv:2302.10205, Semantic Scholar
483	@article{wei2023zeroshot,
484	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
485	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
486	  journal = {arXiv preprint arXiv:2302.10205},
487	  year    = {2023},
488	  url     = {https://arxiv.org/abs/2302.10205}
489	}
490	
491	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
492	@article{qwen2025qwen3,
493	  title   = {Qwen3 Technical Report},
494	  author  = {{Qwen Team}},
495	  journal = {arXiv preprint arXiv:2505.09388},
496	  year    = {2025},
497	  url     = {https://arxiv.org/abs/2505.09388}
498	}
499	
500	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
501	@inproceedings{zheng2024sglang,
502	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
503	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
504	  booktitle = {Advances in Neural Information Processing Systems},
505	  volume    = {37},
506	  year      = {2024},
507	  url       = {https://arxiv.org/abs/2312.07104}
508	}
509	
510	% Confirmed via: ACL Anthology 2021.naacl-main.69
511	@inproceedings{li2021document,
512	  title     = {Document-Level Event Argument Extraction by Conditional Generation},
513	  author    = {Li, Sha and Ji, Heng and Han, Jiawei},
514	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
515	  pages     = {894--908},
516	  year      = {2021},
517	  url       = {https://aclanthology.org/2021.naacl-main.69/}
518	}
519	
520	% ============================================================
521	% New citations added 2026-05-18 (literature freshness check)
522	% ============================================================
523	
524	% grammar_aligned_2024 removed: duplicate of park2024grammar (same paper)
525	
526	@article{formattax2026,
527	    author    = {Ivan Yee Lee and Loris D'Antoni and Taylor Berg-Kirkpatrick},
528	    title     = {The Format Tax},
529	    journal   = {arXiv preprint arXiv:2604.03616},
530	    year      = {2026},
531	    url       = {https://arxiv.org/abs/2604.03616},
532	}
533	
534	@article{dccd2026,
535	    author    = {Avinash Reddy and Thayne T. Walker and James S. Ide and Amrit Singh Bedi},
536	    title     = {Draft-Conditioned Constrained Decoding for Structured Generation in {LLMs}},
537	    journal   = {arXiv preprint arXiv:2603.03305},
538	    year      = {2026},
539	    url       = {https://arxiv.org/abs/2603.03305},
540	}
541	
542	% Confirmed via: arXiv:2601.07525
543	@article{nguyen2026thinking,
544	    author    = {Nguyen, Ngoc Trinh Hung and Silva, Alonso and Zumot, Laith and Tupikina, Liubov and Aghasaryan, Armen and Alam, Mehwish},
545	    title     = {Thinking Before Constraining: A Unified Decoding Framework for Large Language Models},
546	    journal   = {arXiv preprint arXiv:2601.07525},
547	    year      = {2026},
548	    url       = {https://arxiv.org/abs/2601.07525},
549	}
550	
551	@inproceedings{guidex2025,
552	    author    = {Neil De La Fuente and Oscar Sainz and Iker Garc{\'\i}a-Ferrero and Eneko Agirre},
553	    title     = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
554	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
555	    year      = {2025},
556	    publisher = {Association for Computational Linguistics},
557	    url       = {https://aclanthology.org/2025.findings-acl.1245/},
558	}
559	
560	@article{jsonschemabench2025,
561	    author    = {Saibo Geng and Hudson Cooper and Micha{\l} Moskal and Samuel Jenkins and Julian Berman and Nathan Ranchin and Robert West and Eric Horvitz and Harsha Nori},
562	    title     = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
563	    journal   = {arXiv preprint arXiv:2501.10868},
564	    year      = {2025},
565	    url       = {https://arxiv.org/abs/2501.10868},
566	}
567	
568	% ============================================================
569	% Round 9 SF6 references (5 entries)
570	% ============================================================
571	
572	% Confirmed via: arXiv:2304.08085
573	@article{wang2023instructuie,
574	  title     = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
575	  author    = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
576	  journal   = {arXiv preprint arXiv:2304.08085},
577	  year      = {2023},
578	  url       = {https://arxiv.org/abs/2304.08085}
579	}
580	
581	% Confirmed via: ACL Anthology 2022.findings-acl.67
582	@inproceedings{wang2022deepstruct,
583	  title     = {{DeepStruct}: Pretraining of Language Models for Structure Prediction},
584	  author    = {Wang, Chenguang and Liu, Xiao and Chen, Zui and Hong, Haoyun and Tang, Jie and Song, Dawn},
585	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
586	  pages     = {803--823},
587	  year      = {2022},
588	  doi       = {10.18653/v1/2022.findings-acl.67},
589	  url       = {https://aclanthology.org/2022.findings-acl.67}
590	}
591	
592	% Confirmed via: OpenReview r65xfUb76p, ICLR 2024
593	@inproceedings{zhou2024universalner,
594	  title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
595	  author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
596	  booktitle = {The Twelfth International Conference on Learning Representations},
597	  year      = {2024},
598	  url       = {https://openreview.net/forum?id=r65xfUb76p}
599	}
600	
601	% Confirmed via: AAAI 2023 proceedings, doi:10.1609/aaai.v37i11.26563
602	@inproceedings{lou2023usm,
603	  title     = {Universal Information Extraction as Unified Semantic Matching},
604	  author    = {Lou, Jie and Lu, Yaojie and Dai, Dai and Jia, Wei and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},
605	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
606	  volume    = {37},
607	  number    = {11},
608	  pages     = {13318--13326},
609	  year      = {2023},
610	  doi       = {10.1609/aaai.v37i11.26563},
611	  url       = {https://ojs.aaai.org/index.php/AAAI/article/view/26563}
612	}
613	
614	% Confirmed via: ACL Anthology 2023.acl-long.868
615	@inproceedings{wadhwa2023revisiting,
616	  title     = {Revisiting Relation Extraction in the era of Large Language Models},
617	  author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
618	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
619	  pages     = {15566--15589},
620	  year      = {2023},
621	  doi       = {10.18653/v1/2023.acl-long.868},
622	  url       = {https://aclanthology.org/2023.acl-long.868}
623	}
624	
625	% ============================================================
626	% R12 reviewer-requested references
627	% ============================================================
628	
629	% ============================================================
630	% R13 SF5 references (F1 anchoring)
631	% ============================================================
632	
633	
634	% Confirmed via: OpenReview US-TP-xnXI, arXiv:2101.05779, amazon-science/tanl GitHub
635	@inproceedings{paolini2021tanl,
636	  title     = {Structured Prediction as Translation between Augmented Natural Languages},
637	  author    = {Paolini, Giovanni and Athiwaratkun, Ben and Krone, Jason and Ma, Jie and Achille, Alessandro and Anubhai, Rishita and Nogueira dos Santos, C{\'\i}cero and Xiang, Bing and Soatto, Stefano},
638	  booktitle = {International Conference on Learning Representations},
639	  year      = {2021},
640	  url       = {https://openreview.net/forum?id=US-TP-xnXI}
641	}
642	
643	% ============================================================
644	% R12 reviewer-requested references
645	% ============================================================
646	
647	% Confirmed via: NeurIPS 2022 proceedings, arXiv:2304.06248
648	@inproceedings{fei2022lasuie,
649	  title     = {{LasUIE}: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model},
650	  author    = {Fei, Hao and Wu, Shengqiong and Li, Jingye and Li, Bobo and Li, Fei and Qin, Libo and Zhang, Meishan and Zhang, Min and Chua, Tat-Seng},
651	  booktitle = {Advances in Neural Information Processing Systems},
652	  volume    = {35},
653	  year      = {2022},
654	  url       = {https://arxiv.org/abs/2304.06248}
655	}
656	
657	% Confirmed via: ACL Anthology, EMNLP-CoNLL 2010 (originally 2009 workshop)
658	@inproceedings{riedel2010modeling,
659	  title     = {Modeling Relations and Their Mentions without Labeled Text},
660	  author    = {Riedel, Sebastian and Yao, Limin and McCallum, Andrew},
661	  booktitle = {Joint European Conference on Machine Learning and Knowledge Discovery in Databases},
662	  pages     = {148--163},
663	  year      = {2010},
664	  publisher = {Springer}
665	}
666	
667	% Confirmed via: CVPR 2017 proceedings
668	@inproceedings{anderson2017guided,
669	  title     = {Guided Open Vocabulary Image Captioning with Constrained Beam Search},
670	  author    = {Anderson, Peter and Fernando, Basura and Johnson, Mark and Gould, Stephen},
671	  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
672	  pages     = {936--945},
673	  year      = {2017},
674	  publisher = {Association for Computational Linguistics}
675	}
676	
677	% R21 additions
678	
679	@inproceedings{lu2021text2event,
680	  title     = {{Text2Event}: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction},
681	  author    = {Lu, Yaojie and Lin, Hongyu and Xu, Jin and Han, Xianpei and Tang, Jialong and Li, Annan and Sun, Le and Liao, Meng and Chen, Shaobo},
682	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
683	  pages     = {2722--2735},
684	  year      = {2021},
685	  publisher = {Association for Computational Linguistics}
686	}
687	
688	@inproceedings{huang2024lookahead,
689	  title     = {Lookahead Planning for Improved Constrained Decoding},
690	  author    = {Huang, Hanwen and Chen, Niansu and de Melo, Gerard},
691	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
692	  year      = {2024},
693	  publisher = {Association for Computational Linguistics}
694	}
695	
696	
697	
698	% R24 additions
699	
700	@article{luo2025kgtrie,
701	  title     = {{KG-Trie}: Knowledge Graph Enhanced Constrained Decoding for Faithful Knowledge-to-Text Generation},
702	  author    = {Luo, Yifan and others},
703	  journal   = {arXiv preprint arXiv:2410.13080},
704	  year      = {2025},
705	  note      = {ICML 2025}
706	}
707	
708	@article{vukovic2024dialogue,
709	  title     = {Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding},
710	  author    = {Vukovic, Renato and others},
711	  journal   = {arXiv preprint arXiv:2408.02361},
712	  year      = {2024}
713	}
714	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd45e269-bfae-4614-8bc1-fe4f29f809ab",
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "1830ac80-22bc-4603-966e-820fd858129c",
  "sourceToolAssistantUUID": "dd45e269-bfae-4614-8bc1-fe4f29f809ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-23T13:08:50.751Z_

Now let me search for references to "microsoft guidance" to see if there's a Guidance entry:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1830ac80-22bc-4603-966e-820fd858129c",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ52BqNP3HfKtK4oMXP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7e0b28c-fd14-4a96-a1ed-85b09db5cc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AKpaJPEn8GEL1MHCu5r2sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14206,
      "cache_read_input_tokens": 40758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14206,
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

_source line 11 · 2026-05-23T13:08:52.178Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019LMtx1zpv3vkdrheo1dvZy`</summary>

```json
{
  "pattern": "guidance|microsoft.*guidance|lmql|outlines",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e0b28c-fd14-4a96-a1ed-85b09db5cc46",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ52BqNP3HfKtK4oMXP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe6412f3-0556-4862-b877-5a552e5d7790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AKpaJPEn8GEL1MHCu5r2sx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14206,
      "cache_read_input_tokens": 40758,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14206
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 166,
          "cache_read_input_tokens": 40758,
          "cache_creation_input_tokens": 14206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14206,
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

_source line 12 · 2026-05-23T13:08:52.194Z_

<details><summary>↩ Tool result · `toolu_019LMtx1zpv3vkdrheo1dvZy`</summary>

```text
217:@article{willard2023outlines,
226:@inproceedings{beurer-kellner2023lmql,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe6412f3-0556-4862-b877-5a552e5d7790",
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "f24f0645-688e-45ab-acdb-ab37dbdef22f",
  "sourceToolAssistantUUID": "fe6412f3-0556-4862-b877-5a552e5d7790",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T13:08:53.469Z_

Now let me search for DyGIE++ specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f24f0645-688e-45ab-acdb-ab37dbdef22f",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ5Es5g6BUQrHzCofJx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b2107d3-bd08-4be8-94c1-d91af0756186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015bvQdff5PvWvfQuHTzU3Cc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 54964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 211,
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

_source line 14 · 2026-05-23T13:08:53.902Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01K54A9yKeRx8Teck4kD6fEP`</summary>

```json
{
  "pattern": "dygie|wadden2019|DyGIE",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b2107d3-bd08-4be8-94c1-d91af0756186",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ5Es5g6BUQrHzCofJx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60364889-2b58-4937-963b-1f44c91ffde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015bvQdff5PvWvfQuHTzU3Cc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 54964,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 159,
          "cache_read_input_tokens": 54964,
          "cache_creation_input_tokens": 211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 211,
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

_source line 15 · 2026-05-23T13:08:53.912Z_

<details><summary>↩ Tool result · `toolu_01K54A9yKeRx8Teck4kD6fEP`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60364889-2b58-4937-963b-1f44c91ffde3",
  "isSidechain": true,
  "promptId": "f90c706a-5752-4cb1-a803-d1c2313c7907",
  "agentId": "a579de2625c7cd6d9",
  "type": "user",
  "uuid": "80552cf4-e7b9-4a4a-a193-5590b94586f8",
  "sourceToolAssistantUUID": "60364889-2b58-4937-963b-1f44c91ffde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T13:09:00.773Z_

Based on my thorough search of the two .bib files in the paper directory, here are my findings:

**PRESENT REFERENCES:**

1. **PL-Marker** - PRESENT
   - Bib key: `ye2022packed`
   - Title: "Packed Levitated Marker for Entity and Relation Extraction"
   - Found at line 183-192

2. **PURE** - PRESENT
   - Bib key: `zhong2021frustratingly`
   - Title: "A Frustratingly Easy Approach for Entity and Relation Extraction"
   - Found at line 171-180

3. **DeepStruct** - PRESENT
   - Bib key: `wang2022deepstruct`
   - Title: "DeepStruct: Pretraining of Language Models for Structure Prediction"
   - Found at line 582-590

4. **wadhwa2023revisiting** - PRESENT
   - Bib key: `wadhwa2023revisiting`
   - Title: "Revisiting Relation Extraction in the era of Large Language Models"
   - Found at line 615-623

**MISSING REFERENCES:**

1. **DyGIE++** (wadden2019 or dygie) - NOT FOUND
   - No entries matching "dygie", "wadden2019", or similar variants

2. **Guidance (microsoft guidance)** - NOT FOUND (with caveat)
   - While there is no explicit "Guidance" entry by Microsoft, the file contains related constrained decoding libraries:
     - `willard2023outlines` (line 217-223) - "Efficient Guided Generation for Large Language Models" 
     - `beurer-kellner2023lmql` (line 226-232) - "Prompting Is Programming: A Query Language for Large Language Models"
   - However, there is NO specific Microsoft Guidance/guidance library entry

**Summary:** 4 out of 6 target references are present (PL-Marker, PURE, DeepStruct, and wadhwa2023revisiting). Missing are DyGIE++ and the Microsoft Guidance library entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80552cf4-e7b9-4a4a-a193-5590b94586f8",
  "isSidechain": true,
  "agentId": "a579de2625c7cd6d9",
  "requestId": "req_011CbKZ5NQWMCiAUSUWhwAPX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77ca736a-e777-4505-b300-fdc930e67af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "65a387df-0d96-4ba9-b6d6-f7bd8f2d0f36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-conjuring-cocke",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DNoeXygixKpyw9zZPkfsVj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 174,
      "cache_read_input_tokens": 55175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 174,
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
