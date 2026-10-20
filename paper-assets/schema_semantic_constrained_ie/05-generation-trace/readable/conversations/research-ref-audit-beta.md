# research ref audit beta

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 283
- **Recorded user turns:** 0
- **Tool calls:** 141
- **Original source:** `logs/chats/worker_research_ref-audit-beta_20260526T101833.jsonl`
- **Structured JSON:** [`1d397e2fc2f71876bfd3.json`](../../sessions/1d/1d397e2fc2f71876bfd3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

283 recorded events

### Tool call

_source line 1 · 2026-05-26T10:32:10.014449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:32:10.015093+00:00_

1	% ============================================================
2	% Merged authoritative BibTeX references
3	% ============================================================
4	
5	% vLLM — used for GCD-equivalence verification experiment
6	@inproceedings{kwon2023vllm,
7	  title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
8	  author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph and Zhang, Hao and Stoica, Ion},
9	  booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)},
10	  year      = {2023},
11	}
12	
13	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
14	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
15	@inproceedings{synchromesh_iclr2022,
16	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
17	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
18	  booktitle = {International Conference on Learning Representations},
19	  year      = {2022},
20	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
21	}
22	
23	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
24	@inproceedings{mgd_neurips2023,
25	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
26	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
27	  booktitle = {Advances in Neural Information Processing Systems},
28	  volume    = {36},
29	  year      = {2023},
30	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
31	}
32	
33	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
34	@article{pldi2025_type_constrained_codegen,
35	  title     =
…[truncated 33109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:32:10.015309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:32:10.015485+00:00_

1	\documentclass[11pt]{article}
2	
3	\PassOptionsToPackage{table}{xcolor}
4	\usepackage[review]{acl}
5	
6	\usepackage{times}
7	\usepackage{latexsym}
8	\usepackage[T1]{fontenc}
9	\usepackage[utf8]{inputenc}
10	\usepackage{microtype}
11	% \usepackage{inconsolata}  % optional per ACL template; not available in this TeX Live
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{amsmath}
16	\usepackage{amssymb}
17	\usepackage{amsthm}
18	\usepackage{enumitem}
19	\usepackage{pifont}
20	\usepackage{soul}
21	\usepackage{tikz}
22	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Related Work ===
38	\input{section6_related_work}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §5 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §6 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_crossmodel_draft}
56	\input{section5_wikievents_draft}
57	\input{section5_runtime}
58	
59	% === §7 Discussion and Conclusion ===
60	\section{Discussion and Conclusion}
61	\label{sec:discussion}
62	\input{section7_conclusion_compressed}
63	
64	% === Limitations ===
65	\section*{Limitations}
66	
67	Per-triple enforcement creates a DR$\leftrightarrow$CF trade-off; global type consensus during decoding remains future work.
68	Evaluation covers 8B/70B models on two RE and one EE dataset; smaller-model and non-English generalization is untested.
69	Empirical type constraints are derived from training data (9
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:32:10.015700+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:32:10.015847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:32:10.016055+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 1-10",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries with their BibTeX data and citation contexts:\n\n---\n\n**1. kwon2023vllm**\n```\n@inproceedings{kwon2023vllm,\n  title = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n  author = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph and Zhang, Hao and Stoica, Ion},\n  booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)},\n  year = {2023},\n}\n```\nCitation context: Used in section5_scierc_draft.tex L65-66 (vLLM) and section5_runtime.tex L64 (vLLM).\n\n---\n\n**2. synchromesh_iclr2022**\n```\n@inproceedings{synchromesh_iclr2022,\n  title = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},\n  author = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},\n  booktitle = {International Conference on Learning Representations},\n  year = {2022},\n  url = {https://openreview.net/forum?id=KmtVD97J43e}\n}\n```\nCitation context: appendix_related_work.tex L26-28 (Synchromesh description).\n\n---\n\n**3. mgd_neurips2023**\n```\n@inproceedings{mgd_neurips2023,\n  title = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},\n  author = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {36},\n  year = {2023},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}\n}\n```\nCitation context: appendix_related_work.tex L26-28 (MGD description).\n\n---\n\n**4. pldi2025_type_constrained_codegen**\n```\n@article{pldi2025_type_constrained_codegen,\n  title = {Type-Constrained Code Generation with Language Models},\n  author = {M\\\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},\n  journal = {Proceedings of the ACM on Programming Languages},\n  volume = {9},\n  number = {PLDI},\n  year = {2025},\n  doi = {10.1145/3729274},\n  url = {https://dl.acm.org/doi/10.1145/3729274}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\citet{pldi2025_type_constrained_codegen}; appendix_related_work.tex L26-28.\n\n---\n\n**5. roth_yih_2004**\n```\n@inproceedings{roth_yih_2004,\n  title = {A Linear Programming Formulation for Global Inference in Natural Language Tasks},\n  author = {Roth, Dan and Yih, Wen-tau},\n  booktitle = {Proceedings of the Eighth Conference on Computational Natural Language Learning ({CoNLL}-2004) at {HLT}-{NAACL} 2004},\n  pages = {1--8},\n  year = {2004},\n  address = {Boston, Massachusetts, USA},\n  url = {https://aclanthology.org/W04-2401/}\n}\n```\nCitation context: section6_related_work.tex L17 \"ILP constraints\" → \\citet{roth_yih_2004}; appendix_related_work.tex L40.\n\n---\n\n**6. adakgc_emnlp2023**\n```\n@inproceedings{adakgc_emnlp2023,\n  title = {Schema-adaptable Knowledge Graph Construction},\n  author = {Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu},\n  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2023},\n  pages = {6408--6431},\n  year = {2023},\n  url = {https://aclanthology.org/2023.findings-emnlp.425/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (AdaKGC).\n\n---\n\n**7. knowcoder_acl2024**\n```\n@inproceedings{knowcoder_acl2024,\n  title = {{KnowCoder}: Coding Structured Knowledge into {LLMs} for Universal Information Extraction},\n  author = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {8758--8779},\n  year = {2024},\n  address = {Bangkok, Thailand},\n  url = {https://aclanthology.org/2024.acl-long.475/}\n}\n```\nCitation context: section1_introduction_draft.tex L24 \"OntoCoDec is orthogonal to … KnowCoder\" → \\cite{knowcoder_acl2024}; section6_related_work.tex L13 \"training-time internalization\" → \\cite{knowcoder_acl2024}; appendix_related_work.tex L55-60.\n\n---\n\n**8. spires_2024**\n```\n@article{spires_2024,\n  title = {Structured Prompt Interrogation and Recursive Extraction of Semantics ({SPIRES}): A Method for Populating Knowledge Bases Using Zero-shot Learning},\n  author = {Caufield, J. Harry and Hegde, Harshad and Emonet, Vincent and Harris, Nomi L. and Joachimiak, Marcin P. and Matentzoglu, Nicolas and Kim, HyeongSik and Moxon, Sierra and Reese, Justin T. and Haendel, Melissa A. and Robinson, Peter N. and Mungall, Christopher J.},\n  journal = {Bioinformatics},\n  volume = {40},\n  number = {3},\n  pages = {btae104},\n  year = {2024},\n  doi = {10.1093/bioinformatics/btae104},\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{spires_2024}; appendix_related_work.tex L72-77.\n\n---\n\n**9. ontologx_2025**\n```\n@article{ontologx_2025,\n  title = {{OntoLogX}: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models},\n  author = {Cotti, Luca and Drago, Idilio and Rula, Anisa and Bianchini, Devis and Cerutti, Federico},\n  journal = {Advanced Intelligent Systems},\n  year = {2026},\n  doi = {10.1002/aisy.202501381},\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{ontologx_2025}; appendix_related_work.tex L72-77.\nNOTE: cite key says 2025 but year field says 2026. Check which is correct.\n\n---\n\n**10. ekaw2024_ontology_beam**\n```\n@inproceedings{ekaw2024_ontology_beam,\n  title = {Ontology-Constrained Generation of Domain-Specific Clinical Summaries},\n  author = {Mehenni, Gaya and Zouaq, Amal},\n  booktitle = {Knowledge Engineering and Knowledge Management ({EKAW} 2024)},\n  series = {Lecture Notes in Computer Science},\n  volume = {15370},\n  pages = {382--398},\n  year = {2024},\n  publisher = {Springer},\n  doi = {10.1007/978-3-031-77792-9_23}\n}\n```\nCitation context: appendix_related_work.tex L82 (EKAW2024 ontology beam).\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 1-10",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries with their BibTeX data and citation contexts:\n\n---\n\n**1. kwon2023vllm**\n```\n@inproceedings{kwon2023vllm,\n  title = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n  author = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph and Zhang, Hao and Stoica, Ion},\n  booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles (SOSP)},\n  year = {2023},\n}\n```\nCitation context: Used in section5_scierc_draft.tex L65-66 (vLLM) and section5_runtime.tex L64 (vLLM).\n\n---\n\n**2. synchromesh_iclr2022**\n```\n@inproceedings{synchromesh_iclr2022,\n  title = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},\n  author = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},\n  booktitle = {International Conference on Learning Representations},\n  year = {2022},\n  url = {https://openreview.net/forum?id=KmtVD97J43e}\n}\n```\nCitation context: appendix_related_work.tex L26-28 (Synchromesh description).\n\n---\n\n**3. mgd_neurips2023**\n```\n@inproceedings{mgd_neurips2023,\n  title = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},\n  author = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {36},\n  year = {2023},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}\n}\n```\nCitation context: appendix_related_work.tex L26-28 (MGD description).\n\n---\n\n**4. pldi2025_type_constrained_codegen**\n```\n@article{pldi2025_type_constrained_codegen,\n  title = {Type-Constrained Code Generation with Language Models},\n  author = {M\\\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},\n  journal = {Proceedings of the ACM on Programming Languages},\n  volume = {9},\n  number = {PLDI},\n  year = {2025},\n  doi = {10.1145/3729274},\n  url = {https://dl.acm.org/doi/10.1145/3729274}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\citet{pldi2025_type_constrained_codegen}; appendix_related_work.tex L26-28.\n\n---\n\n**5. roth_yih_2004**\n```\n@inproceedings{roth_yih_2004,\n  title = {A Linear Programming Formulation for Global Inference in Natural Language Tasks},\n  author = {Roth, Dan and Yih, Wen-tau},\n  booktitle = {Proceedings of the Eighth Conference on Computational Natural Language Learning ({CoNLL}-2004) at {HLT}-{NAACL} 2004},\n  pages = {1--8},\n  year = {2004},\n  address = {Boston, Massachusetts, USA},\n  url = {https://aclanthology.org/W04-2401/}\n}\n```\nCitation context: section6_related_work.tex L17 \"ILP constraints\" → \\citet{roth_yih_2004}; appendix_related_work.tex L40.\n\n---\n\n**6. adakgc_emnlp2023**\n```\n@inproceedings{adakgc_emnlp2023,\n  title = {Schema-adaptable Knowledge Graph Construction},\n  author = {Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu},\n  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2023},\n  pages = {6408--6431},\n  year = {2023},\n  url = {https://aclanthology.org/2023.findings-emnlp.425/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (AdaKGC).\n\n---\n\n**7. knowcoder_acl2024**\n```\n@inproceedings{knowcoder_acl2024,\n  title = {{KnowCoder}: Coding Structured Knowledge into {LLMs} for Universal Information Extraction},\n  author = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {8758--8779},\n  year = {2024},\n  address = {Bangkok, Thailand},\n  url = {https://aclanthology.org/2024.acl-long.475/}\n}\n```\nCitation context: section1_introduction_draft.tex L24 \"OntoCoDec is orthogonal to … KnowCoder\" → \\cite{knowcoder_acl2024}; section6_related_work.tex L13 \"training-time internalization\" → \\cite{knowcoder_acl2024}; appendix_related_work.tex L55-60.\n\n---\n\n**8. spires_2024**\n```\n@article{spires_2024,\n  title = {Structured Prompt Interrogation and Recursive Extraction of Semantics ({SPIRES}): A Method for Populating Knowledge Bases Using Zero-shot Learning},\n  author = {Caufield, J. Harry and Hegde, Harshad and Emonet, Vincent and Harris, Nomi L. and Joachimiak, Marcin P. and Matentzoglu, Nicolas and Kim, HyeongSik and Moxon, Sierra and Reese, Justin T. and Haendel, Melissa A. and Robinson, Peter N. and Mungall, Christopher J.},\n  journal = {Bioinformatics},\n  volume = {40},\n  number = {3},\n  pages = {btae104},\n  year = {2024},\n  doi = {10.1093/bioinformatics/btae104},\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{spires_2024}; appendix_related_work.tex L72-77.\n\n---\n\n**9. ontologx_2025**\n```\n@article{ontologx_2025,\n  title = {{OntoLogX}: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models},\n  author = {Cotti, Luca and Drago, Idilio and Rula, Anisa and Bianchini, Devis and Cerutti, Federico},\n  journal = {Advanced Intelligent Systems},\n  year = {2026},\n  doi = {10.1002/aisy.202501381},\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{ontologx_2025}; appendix_related_work.tex L72-77.\nNOTE: cite key says 2025 but year field says 2026. Check which is correct.\n\n---\n\n**10. ekaw2024_ontology_beam**\n```\n@inproceedings{ekaw2024_ontology_beam,\n  title = {Ontology-Constrained Generation of Domain-Specific Clinical Summaries},\n  author = {Mehenni, Gaya and Zouaq, Amal},\n  booktitle = {Knowledge Engineering and Knowledge Management ({EKAW} 2024)},\n  series = {Lecture Notes in Computer Science},\n  volume = {15370},\n  pages = {382--398},\n  year = {2024},\n  publisher = {Springer},\n  doi = {10.1007/978-3-031-77792-9_23}\n}\n```\nCitation context: appendix_related_work.tex L82 (EKAW2024 ontology beam).\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:32:10.016471+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:32:10.016621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:32:10.016800+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Efficient Memory Management for Large Language Model Serving with PagedAttention\" Kwon 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Efficient Memory Management for Large Language Model Serving with PagedAttention\" Kwon 2023"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:32:10.016965+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Synchromesh: Reliable Code Generation from Pre-trained Language Models\" Poesia 2022 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Synchromesh: Reliable Code Generation from Pre-trained Language Models\" Poesia 2022 ICLR"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:32:10.017090+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\" Agrawal NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\" Agrawal NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:32:10.017212+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Type-Constrained Code Generation with Language Models\" Mündler PLDI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Type-Constrained Code Generation with Language Models\" Mündler PLDI 2025"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:32:10.017329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Linear Programming Formulation for Global Inference in Natural Language Tasks\" Roth Yih 2004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Linear Programming Formulation for Global Inference in Natural Language Tasks\" Roth Yih 2004"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:32:10.017442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Schema-adaptable Knowledge Graph Construction\" Ye Hongbin EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Schema-adaptable Knowledge Graph Construction\" Ye Hongbin EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:32:10.017554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\" Li Zixuan ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\" Li Zixuan ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:32:10.017664+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Structured Prompt Interrogation and Recursive Extraction of Semantics SPIRES\" Caufield Bioinformatics 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Structured Prompt Interrogation and Recursive Extraction of Semantics SPIRES\" Caufield Bioinformatics 2024"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:32:10.017799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs\" Cotti 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs\" Cotti 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:32:10.017916+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ontology-Constrained Generation of Domain-Specific Clinical Summaries\" Mehenni Zouaq EKAW 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ontology-Constrained Generation of Domain-Specific Clinical Summaries\" Mehenni Zouaq EKAW 2024"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:32:10.018043+00:00_

Web search results for query: ""Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context" Agrawal NeurIPS 2023"

Links: [{"title":"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html"},{"title":"NeurIPS Poster Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context","url":"https://neurips.cc/virtual/2023/poster/70362"},{"title":"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context","url":"https://neurips.cc/media/neurips-2023/Slides/70362.pdf"},{"title":"GitHub - microsoft/monitors4codegen: Code and Data artifact for NeurIPS 2023 paper - \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\". `multispy` is a lsp client library in Python intended to be used to build applications around language servers.","url":"https://github.com/microsoft/monitors4codegen"},{"title":"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/guiding-language-models-of-code-with-global-context-using-monitors/"},{"title":"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context | OpenReview","url":"https://openreview.net/forum?id=qPUbKxKvXq"},{"title":"[PDF] Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Monitor-Guided-Decoding-of-Code-LMs-with-Static-of-Agrawal-Kanade/9b405bcf0c10a220e848eed43573ffc3477e13b8"},{"title":"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context","url":"https://openreview.net/pdf?id=qPUbKxKvXq"},{"title":"monitors4codegen/README.md at main · microsoft/monitors4codegen","url":"https://github.com/microsoft/monitors4codegen/blob/main/README.md"}]

I found comprehensive in
…[truncated 1468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:32:10.018227+00:00_

Web search results for query: ""Efficient Memory Management for Large Language Model Serving with PagedAttention" Kwon 2023"

Links: [{"title":"[2309.06180] Efficient Memory Management for Large Language Model Serving with PagedAttention","url":"https://arxiv.org/abs/2309.06180"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention | Proceedings of the 29th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3600006.3613165"},{"title":"[Paper Note] Efficient Memory Management for Large Language Model Serving with PagedAttention, Woosuk Kwon+, SOSP'23 · Issue #2474 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2474"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention | Request PDF","url":"https://www.researchgate.net/publication/374920067_Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention"},{"title":"Efficient Memory Management for Large Language Model","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/ng_tang_pagedattention.pdf"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention","url":"https://saikatkumardey.com/ml-wiki/sources/pagedattention-vllm"},{"title":"[PDF] Efficient Memory Management for Large Language Model Serving with PagedAttention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Memory-Management-for-Large-Language-with-Kwon-Li/83b90f4a0ae4cc214eb3cc140ccfef9cd99fac05"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention citation","url":"https://duruofei.com/cites/Kwon2023Efficient.html"},{"title":"Paper page - Efficient Memory Management for Large Language Model Serving with PagedAttention","url":"https://huggingface.co/papers/2309.06180"}]

I found the paper you're looking for! Here are the key details:

## Overview

High throughput servin
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T10:32:10.018402+00:00_

Web search results for query: ""Synchromesh: Reliable Code Generation from Pre-trained Language Models" Poesia 2022 ICLR"

Links: [{"title":"[2201.11227] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227"},{"title":"GitHub - kanishkg/synchromesh: Get language models to generate responses in a specific format reliably. Open source implementation of Synchromesh: Reliable code generation from pre-trained language models.","url":"https://github.com/kanishkg/synchromesh"},{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Synchromesh: Reliable code generation from pre-trained language models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/"},{"title":"[2201.11227v1] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227v1"},{"title":"[Quick Review] Synchromesh: Reliable code generation from pre-trained language models","url":"https://liner.com/review/synchromesh-reliable-code-generation-from-pretrained-language-models"},{"title":"Synchromesh: Reliable code generation from pre-trained language models · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/poesia2022synchromesh/"},{"title":"Synchromesh: Reliable code generation from pre-trained language models – Alex Polozov","url":"https://alexpolozov.com/publication/synchromesh/"}]

I found the paper "Synchromesh: Reliable Code Generation from Pre-trained Language Models" by Poesia et al., published at
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:32:10.018555+00:00_

Web search results for query: ""A Linear Programming Formulation for Global Inference in Natural Language Tasks" Roth Yih 2004"

Links: [{"title":"A Linear Programming Formulation for Global Inference in Natural Language Tasks - ACL Anthology","url":"https://aclanthology.org/W04-2401/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=A+linear+programming+formulation+for+global+inference+in+natural+language+tasks&amp=&author=Dan+Roth&amp=&author=Wen-tau+Yih&amp=&publication_year=2004&amp=&pages=1-8"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=D.+Roth+and+W.+Yih.+A+linear+programming+formulation+for+global+inference+in+natural+language+tasks.+In+CoNLL,+2004."},{"title":"A Linear Programming Formulation for Global Inference in Natural Language Tasks - Scott Wen-tau Yih","url":"https://scottyih.org/publication/2004-05-06-0007"},{"title":"A Linear Programming Formulation for Global Inference in Natural Language Tasks","url":"https://www.clips.uantwerpen.be/conll2004/pdf/00108rot.pdf"},{"title":"A Linear Programming Formulation for Global Inference in ...","url":"https://cogcomp.seas.upenn.edu/papers/RothYi04a.pdf"},{"title":"CoNLL ’04 A Linear Programming Formulation for Global Inference in Natural","url":"http://scottyih.org/files/RothYi04.pdf"},{"title":"A Study of Global Inference Algorithms in Multi-document Summarization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-540-71496-5_51"}]

Based on the search results, I found information about this paper:

The paper "A Linear Programming Formulation for Global Inference in Natural Language Tasks" was authored by Dan Roth and Wen-tau Yih and published in 2004 in the Proceedings of the Eighth Conference on Computational Natural Language Learning (CoNLL-2004) at HLT-NAACL 2004, pages 1–8, Boston, Massachusetts, USA.

The paper addresses the problem of finding an optimal global assignment to discrete random variables representing o
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:32:10.018739+00:00_

Web search results for query: ""Type-Constrained Code Generation with Language Models" Mündler PLDI 2025"

Links: [{"title":"Type-Constrained Code Generation with Language Models (PLDI 2025 - PLDI Research Papers) - PLDI 2025","url":"https://pldi25.sigplan.org/details/pldi-2025-papers/25/Type-Constrained-Code-Generation-with-Language-Models"},{"title":"[2504.09246] Type-Constrained Code Generation with Language Models","url":"https://arxiv.org/abs/2504.09246"},{"title":"Type-Constrained Code Generation with Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/muendler2025typeawareconstraint"},{"title":"Type-Constrained Code Generation with Language Models","url":"https://arxiv.org/pdf/2504.09246"},{"title":"[PLDI'25] Type-Constrained Code Generation with Language Models - YouTube","url":"https://www.youtube.com/watch?v=DaE0wRnRil0"},{"title":"Type-Constrained Code Generation with Language Models","url":"https://files.sri.inf.ethz.ch/website/slides/2025TypeConstrainedPresentation.pdf"},{"title":"GitHub - eth-sri/type-constrained-code-generation: Reproduction Package for the paper \"Type-Constrained Code Generation with Language Models\" [PLDI 2025] · GitHub","url":"https://github.com/eth-sri/type-constrained-code-generation"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars","url":"https://arxiv.org/html/2508.10111v1"},{"title":"dblp: Type-Constrained Code Generation with Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2504-09246.html"},{"title":"Type-Constrained Code Generation with Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3729274"}]

I found the paper! Here are the key details about "Type-Constrained Code Generation with Language Models" by Mündler et al., published at PLDI 2025:

## Overview
The paper is authored by Niels Mündler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, and Martin Vechev, and was presented at PLDI 2025 on June 18,
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:32:10.018916+00:00_

Web search results for query: ""KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction" Li Zixuan ACL 2024"

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"[2403.07969] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/abs/2403.07969"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/384207388_KnowCoder_Coding_Structured_Knowledge_into_LLMs_for_Universal_Information_Extraction"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/html/2403.07969v2"},{"title":"GitHub - ICT-GoKnow/KnowCoder: Official Repo of paper \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\". In the paper, we propose KnowCoder, the most powerful large language model so far for universal information extraction.","url":"https://github.com/ICT-GoKnow/KnowCoder"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - Zixuan Li","url":"https://lee-zix.github.io/publications/2024-08-16-ACL/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2b5538e89bfb4cac76acafc1f9f2c9f64/dblp"},{"title":"KnowCoder","url":"https://ict-goknow.github.io/knowcoder/"},{"title":"[PDF] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/3ba0f13d9b24a2dcfdcd861150e33c7d71e6c69e"}]

I found the paper you were looking for! Here are the key details:

## Publication Information
KnowCoder: Coding Structured Knowledge into LLMs for Universal Informat
…[truncated 1496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:32:10.019078+00:00_

Web search results for query: ""Schema-adaptable Knowledge Graph Construction" Ye Hongbin EMNLP 2023"

Links: [{"title":"Schema-adaptable Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.425/"},{"title":"GitHub - zjunlp/AdaKGC: [EMNLP 2023 (Findings)] Schema-adaptable Knowledge Graph Construction","url":"https://github.com/zjunlp/AdaKGC"},{"title":"[2305.08703] Schema-adaptable Knowledge Graph Construction","url":"https://arxiv.org/abs/2305.08703"},{"title":"Schema-adaptable Knowledge Graph Construction","url":"https://aclanthology.org/2023.findings-emnlp.425.pdf"},{"title":"Publication: Schema-adaptable Knowledge Graph Construction. - Reviewerly","url":"https://cs.reviewer.ly/publication/9d14831e-5bbd-4d89-aa6c-70b54ce6b072"},{"title":"Findings - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_findings/"},{"title":"Paper page - Schema-adaptable Knowledge Graph Construction","url":"https://huggingface.co/papers/2305.08703"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"AutoSchemaKG: Autonomous Knowledge Graph Construction through","url":"https://arxiv.org/pdf/2505.23628"}]

I found the paper you're looking for. Here are the results:

## "Schema-adaptable Knowledge Graph Construction" by Ye Hongbin et al., EMNLP 2023

The paper was authored by Hongbin Ye, Honghao Gui, Xin Xu, Xi Chen, Huajun Chen, and Ningyu Zhang, and published in the Findings of the Association for Computational Linguistics: EMNLP 2023.

**Key Information:**
- The paper addresses how conventional Knowledge Graph Construction (KGC) approaches follow a static information extraction paradigm with a closed set of pre-defined schema, which falls short when applied to dynamic scenarios or domains where new types of knowledge emerge.

- The authors built a benchmark by splitting and converting existing datasets based on three principles: horizontal schema expansion, vertical sc
…[truncated 736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:32:10.019227+00:00_

Web search results for query: ""OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs" Cotti 2025 2026"

Links: [{"title":"OntoLogX: Ontology‐Guided Knowledge Graph Extraction From Cybersecurity Logs With Large Language Models - Cotti - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501381"},{"title":"[2510.01409] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409"},{"title":"[2510.01409v1] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409v1"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/html/2510.01409v2"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from","url":"https://arxiv.org/pdf/2510.01409"},{"title":"Semantic Cybersecurity Knowledge Graph (SEPSES CSKG)","url":"https://www.emergentmind.com/topics/semantic-processing-of-security-event-streams-cybersecurity-knowledge-graph-sepses-cskg"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction ...","url":"https://iris.unito.it/retrieve/9c05d22b-f34a-493e-a906-faf6b8af372c/2510.01409v1.pdf"}]

I found the research paper you're looking for. Here are the key details:

**OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs**

OntoLogX is an autonomous Artificial Intelligence (AI) agent that leverages Large Language Models (LLMs) to transform raw logs into ontology-grounded Knowledge Graphs (KGs). The paper is authored by Luca Cotti and three other authors.

**Key Features:**
- OntoLogX integrates a lightweight log ontology with Retrieval Augmented Generation (RAG) and iterative correction steps, ensuring that generated KGs are syntactically and semantically valid.
- OntoLogX is an AI agent for o
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:32:10.019378+00:00_

Web search results for query: ""Ontology-Constrained Generation of Domain-Specific Clinical Summaries" Mehenni Zouaq EKAW 2024"

Links: [{"title":"[2411.15666] Ontology-Constrained Generation of Domain-Specific Clinical Summaries","url":"https://arxiv.org/abs/2411.15666"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries","url":"https://arxiv.org/pdf/2411.15666"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-77792-9_23"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries | Request PDF","url":"https://www.researchgate.net/publication/386062489_Ontology-Constrained_Generation_of_Domain-Specific_Clinical_Summaries"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries | PromptLayer","url":"https://www.promptlayer.com/research-papers/ai-powered-medical-summaries-ontologies-reduce-hallucinations"},{"title":"GitHub - Lama-West/Ontology-based-decoding_EKAW2024","url":"https://github.com/Lama-West/Ontology-based-decoding_EKAW2024"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries - PolyPublie","url":"https://publications.polymtl.ca/67792/"},{"title":"dblp: Amal Zouaq","url":"https://dblp.org/pid/92/4064.html"},{"title":"24th EKAW 2024: Amsterdam, The Netherlands","url":"https://dblp.org/db/conf/ekaw/ekaw2024.html"},{"title":"Generative Ontology: When Structured Knowledge Learns to Create","url":"https://arxiv.org/html/2602.05636"}]

I found the paper! Here's what I found about "Ontology-Constrained Generation of Domain-Specific Clinical Summaries" by Mehenni and Zouaq:

## Paper Overview

The paper "Ontology-Constrained Generation of Domain-Specific Clinical Summaries" by Gaya Mehenni and Amal Zouaq was presented at EKAW 2024 (Knowledge Engineering and Knowledge Management conference).

## Research Focus

The paper addresses how Large Language 
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:32:10.019527+00:00_

Web search results for query: ""Structured Prompt Interrogation and Recursive Extraction of Semantics SPIRES" Caufield Bioinformatics 2024"

Links: [{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/article/40/3/btae104/7612230"},{"title":"[2304.02711] Structured prompt interrogation and recursive extraction of semantics (SPIRES): A method for populating knowledge bases using zero-shot learning","url":"https://arxiv.org/abs/2304.02711"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10924283/"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38383067/"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning","url":"https://escholarship.org/uc/item/7b51j34r"},{"title":"OntoGPT","url":"https://monarch-initiative.github.io/ontogpt/"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning - researchr publication","url":"https://researchr.org/publication/CaufieldHEHJMKMRHRM24"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning (Journal Article) | OSTI.GOV","url":"https://www.osti.gov/biblio/2322444"},{"title":"[2304.02711v1] Structured prompt interrogation and recursive extraction of semantics (SPIRES): A method for populating knowledge bases using zero-shot learning","url":
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:32:10.019723+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 11-20",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**11. scholak2021picard**\n```\n@inproceedings{scholak2021picard,\n  title = {{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},\n  author = {Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  year = {2021},\n  url = {https://aclanthology.org/2021.emnlp-main.779/}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\cite{scholak2021picard}; appendix_related_work.tex L23.\n\n---\n\n**12. olasunkanmi2025relate**\n```\n@article{olasunkanmi2025relate,\n  title = {{RELATE}: Relation Extraction in Biomedical Abstracts with {LLMs} and Ontology Constraints},\n  author = {Olasunkanmi, Olawumi and Satusky, Mathew and Yi, Hong and Bizon, Chris and Lee, Harlin and Ahalt, Stanley},\n  journal = {arXiv preprint arXiv:2509.19057},\n  year = {2025},\n  url = {https://arxiv.org/abs/2509.19057}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (RELATE).\n\n---\n\n**13. zhou2026ontologytools**\n```\n@article{zhou2026ontologytools,\n  title = {Ontology-to-tools compilation for executable semantic constraint enforcement in {LLM} agents},\n  author = {Zhou, Xiaochi and Bulter, Patrick and Yang, Changxuan and Rihm, Simon D. and Angkanaporn, Thitikarn and Akroyd, Jethro and Mosbach, Sebastian and Kraft, Markus},\n  journal = {arXiv preprint arXiv:2602.03439},\n  year = {2026},\n  url = {https://arxiv.org/abs/2602.03439}\n}\n```\nCitation context: appendix_related_work.tex L80 (Zhou2026 ontology tools).\n\n---\n\n**14. eberts2020spert**\n```\n@inproceedings{eberts2020spert,\n  title = {Span-based Joint Entity and Relation Extraction with Transformer Pre-training},\n  author = {Eberts, Markus and Ulges, Adrian},\n  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ({ECAI} 2020)},\n  series = {Frontiers in Artificial Intelligence and Applications},\n  volume = {325},\n  pages = {2006--2013},\n  year = {2020},\n  doi = {10.3233/FAIA200321}\n}\n```\nCitation context: appendix_related_work.tex L55-60 (SpERT).\n\n---\n\n**15. yan2021pfn**\n```\n@inproceedings{yan2021pfn,\n  title = {A Partition Filter Network for Joint Entity and Relation Extraction},\n  author = {Yan, Zhiheng and Zhang, Chong and Fu, Jinlan and Zhang, Qi and Wei, Zhongyu},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages = {185--197},\n  year = {2021},\n  url = {https://aclanthology.org/2021.emnlp-main.17/}\n}\n```\nCitation context: appendix_related_work.tex L55-60 (PFN).\n\n---\n\n**16. zhong2021frustratingly**\n```\n@inproceedings{zhong2021frustratingly,\n  title = {A Frustratingly Easy Approach for Entity and Relation Extraction},\n  author = {Zhong, Zexuan and Chen, Danqi},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages = {50--61},\n  year = {2021},\n  address = {Online},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2021.naacl-main.5}\n}\n```\nCitation context: section3_violation_landscape.tex L14 \"supervised SOTA\" → \\cite{zhong2021frustratingly}; appendix_discussion.tex L191 \"supervised SOTA\" → \\citep{zhong2021frustratingly}.\n\n---\n\n**17. ye2022packed**\n```\n@inproceedings{ye2022packed,\n  title = {Packed Levitated Marker for Entity and Relation Extraction},\n  author = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {4904--4917},\n  year = {2022},\n  address = {Dublin, Ireland},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2022.acl-long.337}\n}\n```\nCitation context: section3_violation_landscape.tex L14 \"supervised SOTA\" → \\cite{ye2022packed}; appendix_discussion.tex L191 → \\citep{ye2022packed}.\n\n---\n\n**18. zhou2026snowballing**\n```\n@article{zhou2026snowballing,\n  title = {From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in {LLM} Reflection},\n  author = {Zhou, Hongxu},\n  journal = {arXiv preprint arXiv:2604.06066},\n  year = {2026},\n  url = {https://arxiv.org/abs/2604.06066}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (Zhou snowballing).\n\n---\n\n**19. dong2025xgrammar**\n```\n@inproceedings{dong2025xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n```\nCitation context: section1_introduction_draft.tex L13 \"Grammar-constrained decoding\" → \\cite{dong2025xgrammar}; section3_method_draft.tex L69 \"JSON Schema compiled via XGrammar\" → \\cite{dong2025xgrammar}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\n**20. willard2023outlines**\n```\n@article{willard2023outlines,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n```\nCitation context: section1_introduction_draft.tex L13 → \\cite{willard2023outlines}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 11-20",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**11. scholak2021picard**\n```\n@inproceedings{scholak2021picard,\n  title = {{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},\n  author = {Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  year = {2021},\n  url = {https://aclanthology.org/2021.emnlp-main.779/}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\cite{scholak2021picard}; appendix_related_work.tex L23.\n\n---\n\n**12. olasunkanmi2025relate**\n```\n@article{olasunkanmi2025relate,\n  title = {{RELATE}: Relation Extraction in Biomedical Abstracts with {LLMs} and Ontology Constraints},\n  author = {Olasunkanmi, Olawumi and Satusky, Mathew and Yi, Hong and Bizon, Chris and Lee, Harlin and Ahalt, Stanley},\n  journal = {arXiv preprint arXiv:2509.19057},\n  year = {2025},\n  url = {https://arxiv.org/abs/2509.19057}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (RELATE).\n\n---\n\n**13. zhou2026ontologytools**\n```\n@article{zhou2026ontologytools,\n  title = {Ontology-to-tools compilation for executable semantic constraint enforcement in {LLM} agents},\n  author = {Zhou, Xiaochi and Bulter, Patrick and Yang, Changxuan and Rihm, Simon D. and Angkanaporn, Thitikarn and Akroyd, Jethro and Mosbach, Sebastian and Kraft, Markus},\n  journal = {arXiv preprint arXiv:2602.03439},\n  year = {2026},\n  url = {https://arxiv.org/abs/2602.03439}\n}\n```\nCitation context: appendix_related_work.tex L80 (Zhou2026 ontology tools).\n\n---\n\n**14. eberts2020spert**\n```\n@inproceedings{eberts2020spert,\n  title = {Span-based Joint Entity and Relation Extraction with Transformer Pre-training},\n  author = {Eberts, Markus and Ulges, Adrian},\n  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ({ECAI} 2020)},\n  series = {Frontiers in Artificial Intelligence and Applications},\n  volume = {325},\n  pages = {2006--2013},\n  year = {2020},\n  doi = {10.3233/FAIA200321}\n}\n```\nCitation context: appendix_related_work.tex L55-60 (SpERT).\n\n---\n\n**15. yan2021pfn**\n```\n@inproceedings{yan2021pfn,\n  title = {A Partition Filter Network for Joint Entity and Relation Extraction},\n  author = {Yan, Zhiheng and Zhang, Chong and Fu, Jinlan and Zhang, Qi and Wei, Zhongyu},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n  pages = {185--197},\n  year = {2021},\n  url = {https://aclanthology.org/2021.emnlp-main.17/}\n}\n```\nCitation context: appendix_related_work.tex L55-60 (PFN).\n\n---\n\n**16. zhong2021frustratingly**\n```\n@inproceedings{zhong2021frustratingly,\n  title = {A Frustratingly Easy Approach for Entity and Relation Extraction},\n  author = {Zhong, Zexuan and Chen, Danqi},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages = {50--61},\n  year = {2021},\n  address = {Online},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2021.naacl-main.5}\n}\n```\nCitation context: section3_violation_landscape.tex L14 \"supervised SOTA\" → \\cite{zhong2021frustratingly}; appendix_discussion.tex L191 \"supervised SOTA\" → \\citep{zhong2021frustratingly}.\n\n---\n\n**17. ye2022packed**\n```\n@inproceedings{ye2022packed,\n  title = {Packed Levitated Marker for Entity and Relation Extraction},\n  author = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {4904--4917},\n  year = {2022},\n  address = {Dublin, Ireland},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2022.acl-long.337}\n}\n```\nCitation context: section3_violation_landscape.tex L14 \"supervised SOTA\" → \\cite{ye2022packed}; appendix_discussion.tex L191 → \\citep{ye2022packed}.\n\n---\n\n**18. zhou2026snowballing**\n```\n@article{zhou2026snowballing,\n  title = {From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in {LLM} Reflection},\n  author = {Zhou, Hongxu},\n  journal = {arXiv preprint arXiv:2604.06066},\n  year = {2026},\n  url = {https://arxiv.org/abs/2604.06066}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (Zhou snowballing).\n\n---\n\n**19. dong2025xgrammar**\n```\n@inproceedings{dong2025xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n```\nCitation context: section1_introduction_draft.tex L13 \"Grammar-constrained decoding\" → \\cite{dong2025xgrammar}; section3_method_draft.tex L69 \"JSON Schema compiled via XGrammar\" → \\cite{dong2025xgrammar}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\n**20. willard2023outlines**\n```\n@article{willard2023outlines,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n```\nCitation context: section1_introduction_draft.tex L13 → \\cite{willard2023outlines}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:32:10.020061+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OntoLogX Cotti Drago Rula Bianchini Cerutti \"Advanced Intelligent Systems\" publication date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OntoLogX Cotti Drago Rula Bianchini Cerutti \"Advanced Intelligent Systems\" publication date 2026"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:32:10.020206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Synchromesh ICLR 2022 authors \"Vu Le\" \"Ashish Tiwari\" \"Gustavo Soares\" \"Christopher Meek\" OR \"Chris Meek\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Synchromesh ICLR 2022 authors \"Vu Le\" \"Ashish Tiwari\" \"Gustavo Soares\" \"Christopher Meek\" OR \"Chris Meek\""
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:32:10.020354+00:00_

Web search results for query: "OntoLogX Cotti Drago Rula Bianchini Cerutti "Advanced Intelligent Systems" publication date 2026"

Links: [{"title":"OntoLogX: Ontology‐Guided Knowledge Graph Extraction From Cybersecurity Logs With Large Language Models - Cotti - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501381"},{"title":"[2510.01409] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409"},{"title":"[2510.01409v1] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409v1"},{"title":"[2509.00081] Enabling Transparent Cyber Threat Intelligence Combining Large Language Models and Domain Ontologies","url":"https://arxiv.org/abs/2509.00081"},{"title":"Advanced Intelligent Systems — Grokipedia","url":"https://grokipedia.com/page/advanced_intelligent_systems"},{"title":"Federico Cerutti - Advanced Networking Systems - UNIBS","url":"https://ans.unibs.it/people/cerutti/"},{"title":"Advanced Computing and Intelligent Technologies by Bianchini, Monica (9789811929793) | Browns Books","url":"https://www.brownsbfs.co.uk/Product/Shaw-Rabindra-Nath/Advanced-Computing-and-Intelligent-Technologies/9789811929793"},{"title":"Intelligent Systems on X: \"🎉 👏 Congratulations to the founders of MachOptima, Sinan Demir, Saadet Baltaci and Mehmet Efe Tiryaki as well as their external support Isabella Bianchini. The team successfully completed Phase 1 and are off to Phase 2 of the @maxplanckpress start-up incubator program, MAX!mize https://t.co/qOO9FE4kLM\" / X","url":"https://x.com/MPI_IS/status/1811030100541878647"},{"title":"Amazon.com: Advanced Computing and Intelligent Technologies: Proceedings of ICACIT 2021 (Lecture Notes in Networks and Systems, 218): 9789811621635: Bianchini, Monica, Piuri, Vincenzo, Das, Sanjoy, Shaw, Rabindra N
…[truncated 727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:32:10.020512+00:00_

Web search results for query: "Synchromesh ICLR 2022 authors "Vu Le" "Ashish Tiwari" "Gustavo Soares" "Christopher Meek" OR "Chris Meek""

Links: [{"title":"[2201.11227] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Synchromesh: Reliable code generation from pre-trained language models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/"},{"title":"[2201.11227v1] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227v1"},{"title":"Ashish Tiwari's Homepage","url":"https://ashishxtiwari.github.io/"},{"title":"[Quick Review] Synchromesh: Reliable code generation from pre-trained language models","url":"https://liner.com/review/synchromesh-reliable-code-generation-from-pretrained-language-models"},{"title":"GitHub - kanishkg/synchromesh: Get language models to generate responses in a specific format reliably. Open source implementation of Synchromesh: Reliable code generation from pre-trained language models.","url":"https://github.com/kanishkg/synchromesh"},{"title":"Computer Science Jan 2022","url":"https://arxiv.org/list/cs/2022-01?skip=3780&show=2000"},{"title":"dblp: Sumit Gulwani","url":"https://dblp.org/pid/g/SumitGulwani.html"},{"title":"Papers with Code - Ashish Tiwari","url":"https://paperswithcode.com/search?q=author:Ashish+Tiwari"}]

Based on the search results, I found information about the Synchromesh ICLR 2022 paper:

The paper "Synchromesh: Reliable code generation from pre-trained language models" was authored by Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiw
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:32:10.020659+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2201.11227 Synchromesh authors list \"Meek, Christopher\" OR \"Meek, Chris\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2201.11227 Synchromesh authors list \"Meek, Christopher\" OR \"Meek, Chris\""
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:32:10.020808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SPIRES Bioinformatics 2024 btae104 volume 40 number 3 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SPIRES Bioinformatics 2024 btae104 volume 40 number 3 authors full list"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:32:10.020959+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:32:10.021074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:32:10.021184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding\" Scholak 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding\" Scholak 2021"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:32:10.021311+00:00_

Web search results for query: ""PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding" Scholak 2021"

Links: [{"title":"[2109.05093] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://arxiv.org/abs/2109.05093"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.779/"},{"title":"GitHub - ServiceNow/picard: PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models. PICARD is a ServiceNow Research project that was started at Element AI. · GitHub","url":"https://github.com/ServiceNow/picard"},{"title":"[PDF] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PICARD:-Parsing-Incrementally-for-Constrained-from-Scholak-Schucher/5fbcfccd3736969d95ed660d8e6962c86b7a9113"},{"title":"PICARD: Parsing Incrementally for Constrained Auto- ...","url":"https://aclanthology.org/2021.emnlp-main.779.pdf"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | Request PDF","url":"https://www.researchgate.net/publication/357120000_PICARD_Parsing_Incrementally_for_Constrained_Auto-Regressive_Decoding_from_Language_Models"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://tscholak.github.io/publications/picard"},{"title":"Picard: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | ServiceNow Research","url":"https://www.servicenow.com/research/publication/torsten-scholak-pica-emnlp2021.html"},{"title":"[2109.05093v1] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://arxiv.org/abs/2109.05093v1"},{"title":"GitHub - isabella232/picard-1: PICARD - Parsing Increme
…[truncated 1389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:32:10.021453+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RELATE: Relation Extraction in Biomedical Abstracts\" Olasunkanmi arXiv 2509.19057"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RELATE: Relation Extraction in Biomedical Abstracts\" Olasunkanmi arXiv 2509.19057"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:32:10.021597+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 21-30",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**21. beurer-kellner2023lmql**\n```\n@inproceedings{beurer-kellner2023lmql,\n  title = {Prompting Is Programming: A Query Language for Large Language Models},\n  author = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},\n  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)},\n  year = {2023},\n  url = {https://doi.org/10.1145/3591300}\n}\n```\nCitation context: section1_introduction_draft.tex L13 \"Grammar-constrained decoding\" → \\cite{beurer-kellner2023lmql}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\n**22. beurer-kellner2024domino**\n```\n@inproceedings{beurer-kellner2024domino,\n  title = {Guiding {LLMs} The Right Way: Fast, Non-Invasive Constrained Generation},\n  author = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  pages = {3658--3673},\n  year = {2024},\n  series = {PMLR},\n  volume = {235},\n  url = {https://proceedings.mlr.press/v235/beurer-kellner24a.html}\n}\n```\nCitation context: appendix_related_work.tex L13 (DOMINO/ASAp).\n\n---\n\n**23. park2024grammar**\n```\n@inproceedings{park2024grammar,\n  title = {Grammar-Aligned Decoding},\n  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.21047}\n}\n```\nCitation context: section6_related_work.tex L8.\n\n---\n\n**24. decao2021genre**\n```\n@inproceedings{decao2021genre,\n  title = {Autoregressive Entity Retrieval},\n  author = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=5k8F6UU39V}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (GENRE).\n\n---\n\n**25. josifoski2022genie**\n```\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {4626--4643},\n  year = {2022},\n  url = {https://aclanthology.org/2022.naacl-main.342/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (GenIE).\n\n---\n\n**26. geng2023gcd**\n```\n@inproceedings{geng2023gcd,\n  title = {Grammar-Constrained Decoding for Structured {NLP} Tasks without Finetuning},\n  author = {Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.674/}\n}\n```\nCitation context: section5_scierc_draft.tex L65 \"GCD ceiling\" → \\cite{geng2023gcd}; section5_runtime.tex L64 \"grammar-only equivalent to GCD\" → \\cite{geng2023gcd}; section6_related_work.tex L17 \"grammar-only\" → \\cite{geng2023gcd}; appendix_related_work.tex L40-45; appendix_discussion.tex L596,650-654,672.\n\n---\n\n**27. lu2021neurologic**\n```\n@inproceedings{lu2021neurologic,\n  title = {{NeuroLogic} Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints},\n  author = {Lu, Ximing and West, Peter and Zellers, Rowan and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {4288--4299},\n  year = {2021},\n  url = {https://aclanthology.org/2021.naacl-main.339/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (NeuroLogic).\n\n---\n\n**28. lu2022uie**\n```\n@inproceedings{lu2022uie,\n  title = {Unified Structure Generation for Universal Information Extraction},\n  author = {Lu, Yaojie and Liu, Qing and Dai, Dai and Xiao, Xinyan and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages = {5755--5772},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.395/}\n}\n```\nCitation context: section1_introduction_draft.tex L15 \"Training-based approaches\" → \\cite{lu2022uie}; section6_related_work.tex L13 \"training-time internalization\" → \\cite{lu2022uie}; appendix_related_work.tex L55-60.\n\n---\n\n**29. sainz2024gollie**\n```\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling},\n  author = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n  booktitle = {The Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://openreview.net/forum?id=Y3wpuxd7u9}\n}\n```\nCitation context: section1_introduction_draft.tex L6/L15/L24 multiple uses; section6_related_work.tex L13; appendix_related_work.tex L55-60; appendix_gollie_comparison.tex L6.\n\n---\n\n**30. li2023codeie**\n```\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {15339--15353},\n  year = {2023},\n  address = {Toronto, Canada},\n  url = {https://aclanthology.org/2023.acl-long.855/}\n}\n```\nCitation context: section1_introduction_draft.tex L6 \"LLMs are increasingly used for IE\" → \\cite{li2023codeie}; appendix_related_work.tex L55-60.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 21-30",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**21. beurer-kellner2023lmql**\n```\n@inproceedings{beurer-kellner2023lmql,\n  title = {Prompting Is Programming: A Query Language for Large Language Models},\n  author = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},\n  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)},\n  year = {2023},\n  url = {https://doi.org/10.1145/3591300}\n}\n```\nCitation context: section1_introduction_draft.tex L13 \"Grammar-constrained decoding\" → \\cite{beurer-kellner2023lmql}; section6_related_work.tex L8; appendix_related_work.tex L9-11.\n\n---\n\n**22. beurer-kellner2024domino**\n```\n@inproceedings{beurer-kellner2024domino,\n  title = {Guiding {LLMs} The Right Way: Fast, Non-Invasive Constrained Generation},\n  author = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  pages = {3658--3673},\n  year = {2024},\n  series = {PMLR},\n  volume = {235},\n  url = {https://proceedings.mlr.press/v235/beurer-kellner24a.html}\n}\n```\nCitation context: appendix_related_work.tex L13 (DOMINO/ASAp).\n\n---\n\n**23. park2024grammar**\n```\n@inproceedings{park2024grammar,\n  title = {Grammar-Aligned Decoding},\n  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.21047}\n}\n```\nCitation context: section6_related_work.tex L8.\n\n---\n\n**24. decao2021genre**\n```\n@inproceedings{decao2021genre,\n  title = {Autoregressive Entity Retrieval},\n  author = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=5k8F6UU39V}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (GENRE).\n\n---\n\n**25. josifoski2022genie**\n```\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {4626--4643},\n  year = {2022},\n  url = {https://aclanthology.org/2022.naacl-main.342/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (GenIE).\n\n---\n\n**26. geng2023gcd**\n```\n@inproceedings{geng2023gcd,\n  title = {Grammar-Constrained Decoding for Structured {NLP} Tasks without Finetuning},\n  author = {Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.674/}\n}\n```\nCitation context: section5_scierc_draft.tex L65 \"GCD ceiling\" → \\cite{geng2023gcd}; section5_runtime.tex L64 \"grammar-only equivalent to GCD\" → \\cite{geng2023gcd}; section6_related_work.tex L17 \"grammar-only\" → \\cite{geng2023gcd}; appendix_related_work.tex L40-45; appendix_discussion.tex L596,650-654,672.\n\n---\n\n**27. lu2021neurologic**\n```\n@inproceedings{lu2021neurologic,\n  title = {{NeuroLogic} Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints},\n  author = {Lu, Ximing and West, Peter and Zellers, Rowan and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {4288--4299},\n  year = {2021},\n  url = {https://aclanthology.org/2021.naacl-main.339/}\n}\n```\nCitation context: appendix_related_work.tex L40-45 (NeuroLogic).\n\n---\n\n**28. lu2022uie**\n```\n@inproceedings{lu2022uie,\n  title = {Unified Structure Generation for Universal Information Extraction},\n  author = {Lu, Yaojie and Liu, Qing and Dai, Dai and Xiao, Xinyan and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages = {5755--5772},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.395/}\n}\n```\nCitation context: section1_introduction_draft.tex L15 \"Training-based approaches\" → \\cite{lu2022uie}; section6_related_work.tex L13 \"training-time internalization\" → \\cite{lu2022uie}; appendix_related_work.tex L55-60.\n\n---\n\n**29. sainz2024gollie**\n```\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling},\n  author = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n  booktitle = {The Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://openreview.net/forum?id=Y3wpuxd7u9}\n}\n```\nCitation context: section1_introduction_draft.tex L6/L15/L24 multiple uses; section6_related_work.tex L13; appendix_related_work.tex L55-60; appendix_gollie_comparison.tex L6.\n\n---\n\n**30. li2023codeie**\n```\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {15339--15353},\n  year = {2023},\n  address = {Toronto, Canada},\n  url = {https://aclanthology.org/2023.acl-long.855/}\n}\n```\nCitation context: section1_introduction_draft.tex L6 \"LLMs are increasingly used for IE\" → \\cite{li2023codeie}; appendix_related_work.tex L55-60.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 43 · 2026-05-26T10:32:10.021879+00:00_

Web search results for query: "SPIRES Bioinformatics 2024 btae104 volume 40 number 3 authors full list"

Links: [{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/article/40/3/btae104/7612230"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning (Journal Article) | OSTI.GOV","url":"https://www.osti.gov/pages/biblio/2322444"},{"title":"https://github.com/monarch-initiative/ontogpt | Ecosyste.ms: Awesome","url":"https://awesome.ecosyste.ms/projects/github.com/monarch-initiative/ontogpt"},{"title":"ontogpt · PyPI","url":"https://pypi.org/project/ontogpt/"},{"title":"Volume 40 Issue 3 | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/issue/40/3"},{"title":"Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38383067/"},{"title":"Oup","url":"https://academic.oup.com/bioinformatics/article-pdf/40/3/btae104/56912794/btae104_supplementary_data.pdf"},{"title":"Volume 40 Issue Supplement_1 | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/issue/40/Supplement_1"},{"title":"Volume 40 Issue 1 | Bioinformatics | Oxford Academic","url":"https://academic.oup.com/bioinformatics/issue/40/1"}]

Based on the search results, I found the full author list for the SPIRES article in Bioinformatics, Volume 40, Issue 3 (March 2024), article btae104:

The authors are: J Harry Caufield, Harshad Hegde, Vincent Emonet, Nomi L Harris, Marcin P Joachimiak, Nicolas Matentzoglu, HyeongSik Kim, Sierra Moxon, Justin T Reese, Melissa A Haendel, Peter N Robinson, and Christopher J Mungall.

The article is titled "S
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T10:32:10.022103+00:00_

Web search results for query: "arxiv 2201.11227 Synchromesh authors list "Meek, Christopher" OR "Meek, Chris""

Links: [{"title":"[2201.11227] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227"},{"title":"[2201.11227v1] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227v1"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Computer Science Jan 2022","url":"https://arxiv.org/list/cs/2022-01?skip=3780&show=2000"},{"title":"Synchromesh: Reliable Code Generation","url":"https://www.emergentmind.com/papers/2201.11227"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2201.05613"},{"title":"[1302.1561] Structure and Parameter Learning for Causal Independence and Causal Interaction Models","url":"https://arxiv.org/abs/1302.1561"},{"title":"Signal Processing authors/titles Dec 2017 (80 skipped)","url":"https://arxiv.org/list/eess.SP/1712?skip=80"},{"title":"Computer Science authors/titles Mar 2011 (100 skipped)","url":"https://arxiv.org/list/cs/1103?show=100&skip=100"},{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"}]

Based on the search results, the authors of arxiv paper 2201.11227 (Synchromesh) are: Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, and Sumit Gulwani.

Yes, Christopher Meek is listed as one of the authors on this paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:32:10.022251+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OntoLogX arXiv 2510.01409 authors \"Luca Cotti\" \"Idilio Drago\" \"Anisa Rula\" \"Devis Bianchini\" \"Federico Cerutti\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OntoLogX arXiv 2510.01409 authors \"Luca Cotti\" \"Idilio Drago\" \"Anisa Rula\" \"Devis Bianchini\" \"Federico Cerutti\""
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:32:10.022377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Oleksandr Polozov\" OR \"Alex Polozov\" Synchromesh ICLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Oleksandr Polozov\" OR \"Alex Polozov\" Synchromesh ICLR 2022"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:32:10.022506+00:00_

Web search results for query: "OntoLogX arXiv 2510.01409 authors "Luca Cotti" "Idilio Drago" "Anisa Rula" "Devis Bianchini" "Federico Cerutti""

Links: [{"title":"[2510.01409v1] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409v1"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/html/2510.01409"},{"title":"OntoLogX: Ontology‐Guided Knowledge Graph Extraction From Cybersecurity Logs With Large Language Models - Cotti - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501381?af=R"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from","url":"https://arxiv.org/pdf/2510.01409"},{"title":"[2510.01409] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409"},{"title":"Enabling Transparent Cyber Threat Intelligence Combining ...","url":"https://arxiv.org/pdf/2509.00081"},{"title":"Enabling Transparent Cyber Threat Intelligence Combining Large Language Models and Domain Ontologies","url":"https://arxiv.org/html/2509.00081"},{"title":"An Investigation on Cyber Security Threats and Security Models | Request PDF","url":"https://www.researchgate.net/publication/282613809_An_Investigation_on_Cyber_Security_Threats_and_Security_Models"}]

I found the paper! Here's information about the arXiv paper 2510.01409:

**Paper Details:**
- **Title:** OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models
- **arXiv ID:** 2510.01409
- **Submission Date:** October 1, 2025
- **Authors:** Luca Cotti, Idilio Drago, Anisa Rula, Devis Bianchini, Federico Cerutti

**Overview:**
OntoLogX is an autonomous AI agent that leverages Large Language Models to transform raw logs into ontology-grounded
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:32:10.022656+00:00_

Web search results for query: ""Oleksandr Polozov" OR "Alex Polozov" Synchromesh ICLR 2022"

Links: [{"title":"Alex Polozov","url":"https://alexpolozov.com/"},{"title":"dblp: Oleksandr Polozov","url":"https://dblp.org/pid/151/3318.html"},{"title":"[Quick Review] Synchromesh: Reliable code generation from pre-trained language models","url":"https://liner.com/review/synchromesh-reliable-code-generation-from-pretrained-language-models"},{"title":"Synchromesh: Reliable code generation from pre-trained language models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Papers with Code - Oleksandr Polozov","url":"https://paperswithcode.com/author/oleksandr-polozov"},{"title":"– Alex Polozov","url":"https://alexpolozov.com/news/"},{"title":"Oleksandr POLOZOV | University of Washington, Seattle | UW | Department of Computer Science and Engineering | Research profile","url":"https://www.researchgate.net/profile/Oleksandr-Polozov"},{"title":"Alex Polozov | OpenReview","url":"https://openreview.net/profile?id=~Alex_Polozov1"}]

Based on the search results, I found relevant information about Oleksandr Polozov and his work on Synchromesh at ICLR 2022:

Alex (Oleksandr) Polozov is a Member of Technical Staff at Reflection AI. He teaches machines to write and analyze source code, builds agents and models to aid developers, and is broadly interested in program synthesis and AI for software engineering.

Synchromesh: Reliable Code Generation from Pre-trained Language Models was published at ICLR 2022 with authors including Alex Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Chris Meek, and Sumit Gulwani.

Synchrom
…[truncated 409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:32:10.022826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"Synchromesh\" KmtVD97J43e authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"Synchromesh\" KmtVD97J43e authors"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:32:10.022957+00:00_

Web search results for query: ""RELATE: Relation Extraction in Biomedical Abstracts" Olasunkanmi arXiv 2509.19057"

Links: [{"title":"[2509.19057] RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/abs/2509.19057"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with","url":"https://arxiv.org/pdf/2509.19057"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/html/2509.19057v1"},{"title":"(PDF) RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://www.researchgate.net/publication/395771672_RELATE_Relation_Extraction_in_Biomedical_Abstracts_with_LLMs_and_Ontology_Constraints"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2509.19057"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints | OpenReview","url":"https://openreview.net/forum?id=gcG8dmAUNh"},{"title":"High-throughput Biomedical Relation Extraction for Semi-Structured Web Articles Empowered by Large Language Models","url":"https://arxiv.org/html/2312.08274v3"},{"title":"[2112.13259v1] Deeper Clinical Document Understanding Using Relation Extraction","url":"https://arxiv.org/abs/2112.13259v1"}]

I found the paper! Here's what I found about it:

RELATE is a three-stage pipeline that maps LLM-extracted relations to standardized ontology predicates using ChemProt and the Biolink Model. The pipeline includes: (1) ontology preprocessing with predicate embeddings, (2) similarity-based retrieval enhanced with SapBERT, and (3) LLM-based reranking with explicit negation handling.

Large language models (LLMs) excel at extracting biomedical relations, yet their outputs lack standardization and alignment with ontologies, limiting KG integration. This approach
…[truncated 634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T10:32:10.023092+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ontology-to-tools compilation\" Zhou Kraft arXiv 2602.03439"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ontology-to-tools compilation\" Zhou Kraft arXiv 2602.03439"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:32:10.023222+00:00_

Web search results for query: ""Ontology-to-tools compilation" Zhou Kraft arXiv 2602.03439"

Links: [{"title":"[2602.03439] Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents","url":"https://arxiv.org/abs/2602.03439"},{"title":"Ontology-to-tools compilation for executable semantic ...","url":"https://arxiv.org/pdf/2602.03439"},{"title":"[2602.00029] Construct, Align, and Reason: Large Ontology Models for Enterprise Knowledge Management","url":"https://arxiv.org/abs/2602.00029"},{"title":"Discovering Conceptual Knowledge with Analytic Ontology Templates for Articulated Objects","url":"https://arxiv.org/html/2409.11702v1"},{"title":"1/19 Ontology Development Kit: a toolkit for building, maintaining, and","url":"https://arxiv.org/pdf/2207.02056"},{"title":"[2602.05636] Generative Ontology: When Structured Knowledge Learns to Create","url":"https://arxiv.org/abs/2602.05636"},{"title":"Ontology-Driven Approach to the Structuring of Information Resources Describing a Subject Domain | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-89296-7_16"},{"title":"OntoAligner: A Comprehensive Modular and Robust Python Toolkit for Ontology Alignment","url":"https://arxiv.org/html/2503.21902v1"}]

I found the paper you're looking for. Here's what the search revealed:

The paper "Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents" was submitted on February 3, 2026 by authors including Xiaochi Zhou and Markus Kraft.

The paper introduces ontology-to-tools compilation as a proof-of-principle mechanism for coupling large language models (LLMs) with formal domain knowledge. Within The World Avatar (TWA), ontological specifications are compiled into executable tool interfaces that LLM-based agents must use to create and modify knowledge graph instances, enforcing semantic constraints during generation rather than through post-hoc validation.

Using metal-organic polyhedra synthes
…[truncated 416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:32:10.023356+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Span-based Joint Entity and Relation Extraction with Transformer Pre-training\" Eberts Ulges ECAI 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Span-based Joint Entity and Relation Extraction with Transformer Pre-training\" Eberts Ulges ECAI 2020"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:32:10.023507+00:00_

Web search results for query: ""Span-based Joint Entity and Relation Extraction with Transformer Pre-training" Eberts Ulges ECAI 2020"

Links: [{"title":"Span-based Joint Entity and Relation Extraction with Transformer Pre-training","url":"https://ecai2020.eu/papers/1283_paper.pdf"},{"title":"IOS Press Ebooks - Span-Based Joint Entity and Relation Extraction with Transformer Pre-Training","url":"https://ebooks.iospress.nl/volumearticle/55116"},{"title":"[1909.07755] Span-based Joint Entity and Relation Extraction with Transformer Pre-training","url":"https://arxiv.org/abs/1909.07755"},{"title":"Span-Based Joint Entity and Relation Extraction with Transformer Pre-Training, 2020","url":"https://journals.sagepub.com/doi/10.3233/FAIA200321"},{"title":"GitHub - lavis-nlp/spert: PyTorch code for SpERT: Span-based Entity and Relation Transformer · GitHub","url":"https://github.com/lavis-nlp/spert"},{"title":"Span-based Joint Entity and Relation Extraction with Transformer Pre-training - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190907755E/abstract"},{"title":"Span-based Joint Entity and Relation Extraction with ...","url":"https://arxiv.org/pdf/1909.07755"},{"title":"Span-based Joint Entity and Relation Extraction with ...","url":"https://aclanthology.org/2020.coling-main.8.pdf"},{"title":"Span-based Joint Entity and Relation Extraction with Transformer Pre-training | Request PDF","url":"https://www.researchgate.net/publication/335880592_Span-based_Joint_Entity_and_Relation_Extraction_with_Transformer_Pre-training"},{"title":"ER-LAC: Span-Based Joint Entity and Relation Extraction Model with Multi-Level Lexical and Attention on Context Features","url":"https://www.mdpi.com/2076-3417/13/18/10538"}]

I found the paper you're looking for. Here's what the search revealed:

"Span-based Joint Entity and Relation Extraction with Transformer Pre-training" is by Markus Eberts and Adrian Ulges, introducing SpERT, an attention model for span-based joint entity and relati
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:32:10.023654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Partition Filter Network for Joint Entity and Relation Extraction\" Yan Zhang Fu EMNLP 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Partition Filter Network for Joint Entity and Relation Extraction\" Yan Zhang Fu EMNLP 2021"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:32:10.023830+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T10:32:10.023947+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:32:10.024059+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Prompting Is Programming: A Query Language for Large Language Models\" Beurer-Kellner PLDI 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Prompting Is Programming: A Query Language for Large Language Models\" Beurer-Kellner PLDI 2023"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:32:10.024187+00:00_

Web search results for query: ""Prompting Is Programming: A Query Language for Large Language Models" Beurer-Kellner PLDI 2023"

Links: [{"title":"Prompting Is Programming: A Query Language for Large Language Models (PLDI 2023 - PLDI Research Papers) - PLDI 2023","url":"https://pldi23.sigplan.org/details/pldi-2023-pldi/81/Prompting-Is-Programming-A-Query-Language-for-Large-Language-Models"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/beurerkellner2023prompting"},{"title":"Prompting Is Programming: A Query Language for Large Language Models","url":"https://www.researchgate.net/publication/371363896_Prompting_Is_Programming_A_Query_Language_for_Large_Language_Models"},{"title":"ETH Library Prompting Is Programming: A Query Language for Large","url":"https://www.research-collection.ethz.ch/server/api/core/bitstreams/9a54d4ba-8d99-47a9-b960-b6f33df0ee1d/content"},{"title":"LMQL as described in Prompting Is Programming: A Query Language for Large Language Models","url":"https://dl.acm.org/do/10.5281/zenodo.7711823/full/"},{"title":"[2212.06094v2] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094v2"}]

I found information about the paper "Prompting Is Programming: A Query Language for Large Language Models" by Beurer-Kellner and colleagues presented at PLDI 2023.

## Overview

The paper was presented at PLDI 2023 by Luca Beurer-Kellner, Marc Fischer, and Martin Vechev, and addresses the chall
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:32:10.024326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\" Beurer-Kellner ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation\" Beurer-Kellner ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:32:10.024457+00:00_

Web search results for query: ""Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation" Beurer-Kellner ICML 2024"

Links: [{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"Guiding LLMs the right way: fast, non-invasive constrained ...","url":"https://dl.acm.org/doi/10.5555/3692070.3692216"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation [Quick Review]","url":"https://liner.com/review/guiding-llms-right-way-fast-noninvasive-constrained-generation"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://proceedings.mlr.press/v235/beurer-kellner24a.html"},{"title":"[PDF] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Guiding-LLMs-The-Right-Way:-Fast,-Non-Invasive-Beurer-Kellner-Fischer/b95ca121a606da32180ab8bb0c0c58bf19b1499b"},{"title":"dblp: Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation.","url":"https://dblp.org/rec/conf/icml/Beurer-Kellner024.html"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/beurerkellner2024domino"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://files.sri.inf.ethz.ch/website/papers/beurerkellner2024domino.pdf"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://openreview.net/pdf?id=pXaEYzrFae"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation"

**Authors:** Luca Beurer-Kellner, Marc Fischer, and Martin Vechev

**Venue:** ICML'24: Proceedings of
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:32:10.024590+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" Park Berg-Kirkpatrick Polikarpova NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" Park Berg-Kirkpatrick Polikarpova NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:32:10.024781+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 31-40",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**31. qi2024adelie**\n```\n@inproceedings{qi2024adelie,\n  title = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n  author = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  address = {Miami, Florida, USA},\n  url = {https://aclanthology.org/2024.emnlp-main.419/}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{qi2024adelie}; appendix_related_work.tex L55-60.\n\n---\n\n**32. zaratiana2024enrico**\n```\n@article{zaratiana2024enrico,\n  title = {{EnriCo}: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction},\n  author = {Zaratiana, Urchade and Tomeh, Nadi and Dauxais, Yann and Holat, Pierre and Charnois, Thierry},\n  journal = {arXiv preprint arXiv:2404.12493},\n  year = {2024},\n  url = {https://arxiv.org/abs/2404.12493}\n}\n```\nCitation context: section6_related_work.tex L18 \"ASP constraints\" → \\cite{zaratiana2024enrico}; appendix_related_work.tex L62.\n\n---\n\n**33. khorshidi2025odke**\n```\n@article{khorshidi2025odke,\n  title = {{ODKE+}: Ontology-Guided Open-Domain Knowledge Extraction with {LLMs}},\n  author = {Khorshidi, Samira and Nikfarjam, Azadeh and Shankar, Suprita and Sang, Yisi and Govind, Yash and Jang, Hyun and Kasgari, Ali and McClimans, Alexis and Soliman, Mohamed and Konda, Vishnu and Fakhry, Ahmed and Qi, Xiaoguang},\n  journal = {arXiv preprint arXiv:2509.04696},\n  year = {2025},\n  url = {https://arxiv.org/abs/2509.04696}\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{khorshidi2025odke}; appendix_related_work.tex L72-77.\n\n---\n\n**34. upadhyay2023openie**\n```\n@inproceedings{upadhyay2023openie,\n  title = {Open Information Extraction with Entity Focused Constraints},\n  author = {Upadhyay, Prajna and Balalau, Oana and Manolescu, Ioana},\n  booktitle = {Findings of the Association for Computational Linguistics: {EACL} 2023},\n  year = {2023},\n  url = {https://aclanthology.org/2023.findings-eacl.95/}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (Upadhyay).\n\n---\n\n**35. regino2025kgcurator**\n```\n@inproceedings{regino2025kgcurator,\n  title = {Can {LLMs} be Knowledge Graph Curators for Validating Triple Insertions?},\n  author = {Regino, Andr{\\'e} Gomes and dos Reis, Julio Cesar},\n  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK}) at {COLING} 2025},\n  pages = {87--99},\n  year = {2025},\n  address = {Abu Dhabi, UAE},\n  url = {https://aclanthology.org/2025.genaik-1.10/}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (Regino).\n\n---\n\n**36. tam2024letmespeak**\n```\n@inproceedings{tam2024letmespeak,\n  title = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},\n  author = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n  pages = {1218--1236},\n  year = {2024},\n  address = {Miami, Florida, US},\n  url = {https://aclanthology.org/2024.emnlp-industry.91/}\n}\n```\nCitation context: section4_composition_draft.tex L28 \"Extraction tasks robust to format constraints\" → \\cite{tam2024letmespeak}; appendix_related_work.tex L92-95 and L97 (Tam).\n\n---\n\n**37. banerjee2025crane**\n```\n@inproceedings{banerjee2025crane,\n  title = {{CRANE}: Reasoning with Constrained {LLM} Generation},\n  author = {Banerjee, Debangshu and Suresh, Tarun and Ugare, Shubham and Misailovic, Sasa and Singh, Gagandeep},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  pages = {2836--2857},\n  year = {2025},\n  url = {https://proceedings.mlr.press/v267/banerjee25a.html}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (CRANE).\n\n---\n\n**38. schall2025hiddencost**\n```\n@inproceedings{schall2025hiddencost,\n  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},\n  author = {Schall, Maximilian and de Melo, Gerard},\n  booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing ({RANLP} 2025)},\n  year = {2025},\n  address = {Varna, Bulgaria},\n  url = {https://aclanthology.org/2025.ranlp-1.124/}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (Schall).\n\n---\n\n**39. cabot2021rebel**\n```\n@inproceedings{cabot2021rebel,\n  title = {{REBEL}: Relation Extraction By End-to-end Language Generation},\n  author = {Huguet Cabot, Pere-Llu{\\'\\i}s and Navigli, Roberto},\n  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},\n  pages = {2370--2381},\n  year = {2021},\n  url = {https://aclanthology.org/2021.findings-emnlp.204/}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{cabot2021rebel}; appendix_related_work.tex L55-60.\n\n---\n\n**40. ugare2024syncode**\n```\n@article{ugare2024syncode,\n  title = {{SynCode}: {LLM} Generation with Grammar Augmentation},\n  author = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://openreview.net/forum?id=HiUZtgAPoH}\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{ugare2024syncode}; appendix_related_work.tex.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 31-40",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**31. qi2024adelie**\n```\n@inproceedings{qi2024adelie,\n  title = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n  author = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  address = {Miami, Florida, USA},\n  url = {https://aclanthology.org/2024.emnlp-main.419/}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{qi2024adelie}; appendix_related_work.tex L55-60.\n\n---\n\n**32. zaratiana2024enrico**\n```\n@article{zaratiana2024enrico,\n  title = {{EnriCo}: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction},\n  author = {Zaratiana, Urchade and Tomeh, Nadi and Dauxais, Yann and Holat, Pierre and Charnois, Thierry},\n  journal = {arXiv preprint arXiv:2404.12493},\n  year = {2024},\n  url = {https://arxiv.org/abs/2404.12493}\n}\n```\nCitation context: section6_related_work.tex L18 \"ASP constraints\" → \\cite{zaratiana2024enrico}; appendix_related_work.tex L62.\n\n---\n\n**33. khorshidi2025odke**\n```\n@article{khorshidi2025odke,\n  title = {{ODKE+}: Ontology-Guided Open-Domain Knowledge Extraction with {LLMs}},\n  author = {Khorshidi, Samira and Nikfarjam, Azadeh and Shankar, Suprita and Sang, Yisi and Govind, Yash and Jang, Hyun and Kasgari, Ali and McClimans, Alexis and Soliman, Mohamed and Konda, Vishnu and Fakhry, Ahmed and Qi, Xiaoguang},\n  journal = {arXiv preprint arXiv:2509.04696},\n  year = {2025},\n  url = {https://arxiv.org/abs/2509.04696}\n}\n```\nCitation context: section6_related_work.tex L17 \"post-hoc\" → \\cite{khorshidi2025odke}; appendix_related_work.tex L72-77.\n\n---\n\n**34. upadhyay2023openie**\n```\n@inproceedings{upadhyay2023openie,\n  title = {Open Information Extraction with Entity Focused Constraints},\n  author = {Upadhyay, Prajna and Balalau, Oana and Manolescu, Ioana},\n  booktitle = {Findings of the Association for Computational Linguistics: {EACL} 2023},\n  year = {2023},\n  url = {https://aclanthology.org/2023.findings-eacl.95/}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (Upadhyay).\n\n---\n\n**35. regino2025kgcurator**\n```\n@inproceedings{regino2025kgcurator,\n  title = {Can {LLMs} be Knowledge Graph Curators for Validating Triple Insertions?},\n  author = {Regino, Andr{\\'e} Gomes and dos Reis, Julio Cesar},\n  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK}) at {COLING} 2025},\n  pages = {87--99},\n  year = {2025},\n  address = {Abu Dhabi, UAE},\n  url = {https://aclanthology.org/2025.genaik-1.10/}\n}\n```\nCitation context: appendix_related_work.tex L72-77 (Regino).\n\n---\n\n**36. tam2024letmespeak**\n```\n@inproceedings{tam2024letmespeak,\n  title = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},\n  author = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n  pages = {1218--1236},\n  year = {2024},\n  address = {Miami, Florida, US},\n  url = {https://aclanthology.org/2024.emnlp-industry.91/}\n}\n```\nCitation context: section4_composition_draft.tex L28 \"Extraction tasks robust to format constraints\" → \\cite{tam2024letmespeak}; appendix_related_work.tex L92-95 and L97 (Tam).\n\n---\n\n**37. banerjee2025crane**\n```\n@inproceedings{banerjee2025crane,\n  title = {{CRANE}: Reasoning with Constrained {LLM} Generation},\n  author = {Banerjee, Debangshu and Suresh, Tarun and Ugare, Shubham and Misailovic, Sasa and Singh, Gagandeep},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  pages = {2836--2857},\n  year = {2025},\n  url = {https://proceedings.mlr.press/v267/banerjee25a.html}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (CRANE).\n\n---\n\n**38. schall2025hiddencost**\n```\n@inproceedings{schall2025hiddencost,\n  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},\n  author = {Schall, Maximilian and de Melo, Gerard},\n  booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing ({RANLP} 2025)},\n  year = {2025},\n  address = {Varna, Bulgaria},\n  url = {https://aclanthology.org/2025.ranlp-1.124/}\n}\n```\nCitation context: appendix_related_work.tex L92-95 (Schall).\n\n---\n\n**39. cabot2021rebel**\n```\n@inproceedings{cabot2021rebel,\n  title = {{REBEL}: Relation Extraction By End-to-end Language Generation},\n  author = {Huguet Cabot, Pere-Llu{\\'\\i}s and Navigli, Roberto},\n  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},\n  pages = {2370--2381},\n  year = {2021},\n  url = {https://aclanthology.org/2021.findings-emnlp.204/}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{cabot2021rebel}; appendix_related_work.tex L55-60.\n\n---\n\n**40. ugare2024syncode**\n```\n@article{ugare2024syncode,\n  title = {{SynCode}: {LLM} Generation with Grammar Augmentation},\n  author = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://openreview.net/forum?id=HiUZtgAPoH}\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{ugare2024syncode}; appendix_related_work.tex.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:32:10.025216+00:00_

Web search results for query: "site:openreview.net "Synchromesh" KmtVD97J43e authors"

Links: [{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"SyncFlow: Toward Temporally Aligned Joint Audio-Video Generation from   Text","url":"https://arxiv.org/pdf/2412.15220"},{"title":"Interpretable Convolutional SyncNet","url":"https://arxiv.org/pdf/2409.00971"},{"title":"SyncMV4D: Synchronized Multi-view Joint Diffusion of Appearance and Motion for Hand-Object Interaction Synthesis","url":"https://arxiv.org/pdf/2511.19319"},{"title":"Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy","url":"https://arxiv.org/pdf/2511.21579"},{"title":"SynCamMaster: Synchronizing Multi-Camera Video Generation from Diverse   Viewpoints","url":"https://arxiv.org/pdf/2412.07760"}]

Based on the search results, I found the paper you were looking for on OpenReview. The paper "Synchromesh" proposes a framework for improving the reliability of pre-trained models for code generation, which comprises Target Similarity Tuning (TST) for semantic example selection and Constrained Semantic Decoding (CSD) for constraining output to valid programs in the target language.

However, the search results display only the abstract and don't include the author names. The paper is available at: https://openreview.net/forum?id=KmtVD97J43e

You can visit that OpenReview page directly to see the complete author information for this paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:32:10.025389+00:00_

Web search results for query: ""A Partition Filter Network for Joint Entity and Relation Extraction" Yan Zhang Fu EMNLP 2021"

Links: [{"title":"A Partition Filter Network for Joint Entity and Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.17/"},{"title":"A Partition Filter Network for Joint Entity and Relation Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210812202Y/abstract"},{"title":"[2108.12202] A Partition Filter Network for Joint Entity and Relation Extraction","url":"https://arxiv.org/abs/2108.12202"},{"title":"GitHub - Coopercoppers/PFN: EMNLP 2021 - A Partition Filter Network for Joint Entity and Relation Extraction · GitHub","url":"https://github.com/Coopercoppers/PFN"},{"title":"[2108.12202v8] A Partition Filter Network for Joint Entity and Relation Extraction","url":"http://arxiv.org/abs/2108.12202v8"},{"title":"(PDF) A Partition Filter Network for Joint Entity and Relation Extraction","url":"https://www.researchgate.net/publication/357119538_A_Partition_Filter_Network_for_Joint_Entity_and_Relation_Extraction"},{"title":"An Improved Partition Filter Network for Entity-Relation Joint Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-19-6142-7_10"},{"title":"Figure 2 from A Partition Filter Network for Joint Entity and Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Partition-Filter-Network-for-Joint-Entity-and-Yan-Zhang/917f4a2da2e5f7b45c1f8170421d36770360b569/figure/2"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** A Partition Filter Network for Joint Entity and Relation Extraction

**Authors:** Zhiheng Yan, Chong Zhang, Jinlan Fu, Qi Zhang, and Zhongyu Wei

**Publication:** Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 185–197, Online and Punta Cana, Dominican Republic

**Main Contribution:** The authors propose a partition filte
…[truncated 498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:32:10.025545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Frustratingly Easy Approach for Entity and Relation Extraction\" Zhong Chen NAACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Frustratingly Easy Approach for Entity and Relation Extraction\" Zhong Chen NAACL 2021"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:32:10.025708+00:00_

Web search results for query: ""A Frustratingly Easy Approach for Entity and Relation Extraction" Zhong Chen NAACL 2021"

Links: [{"title":"A Frustratingly Easy Approach for Entity and Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.5/"},{"title":"A Frustratingly Easy Approach for Entity and Relation ...","url":"https://aclanthology.org/2021.naacl-main.5.pdf"},{"title":"GitHub - princeton-nlp/PURE: [NAACL 2021] A Frustratingly Easy Approach for Entity and Relation Extraction https://arxiv.org/abs/2010.12812","url":"https://github.com/princeton-nlp/PURE"},{"title":"A Frustratingly Easy Approach for Entity and Relation Extraction - Princeton University","url":"https://collaborate.princeton.edu/en/publications/a-frustratingly-easy-approach-for-entity-and-relation-extraction/"},{"title":"A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://www.researchgate.net/publication/352365967_A_Frustratingly_Easy_Approach_for_Entity_and_Relation_Extraction"},{"title":"[2010.12812] A Frustratingly Easy Approach for Entity and Relation Extraction","url":"https://arxiv.org/abs/2010.12812"},{"title":"Easy Approach for Entity & Relation Extraction","url":"https://www.emergentmind.com/papers/2010.12812"}]

I found the paper! Here's what I found about "A Frustratingly Easy Approach for Entity and Relation Extraction" by Zhong and Chen:

**Publication Details:**
The paper was published in the Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 50–61.

**Key Contribution:**
The paper addresses end-to-end relation extraction, which aims to identify named entities and extract relations between them. Most recent work models these two subtasks jointly, either by casting them in one structured prediction framework, or performing multi-task learning through shared representations.

**Main Approach:**
The authors present a simple pipeli
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:32:10.025861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Packed Levitated Marker for Entity and Relation Extraction\" Ye Lin Li Sun ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Packed Levitated Marker for Entity and Relation Extraction\" Ye Lin Li Sun ACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:32:10.026006+00:00_

Web search results for query: ""Packed Levitated Marker for Entity and Relation Extraction" Ye Lin Li Sun ACL 2022"

Links: [{"title":"Packed Levitated Marker for Entity and Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.337/"},{"title":"GitHub - thunlp/PL-Marker: Source code for \"Packed Levitated Marker for Entity and Relation Extraction\" · GitHub","url":"https://github.com/thunlp/PL-Marker"},{"title":"Packed Levitated Marker for Entity and Relation Extraction","url":"https://aclanthology.org/2022.acl-long.337.pdf"},{"title":"Packed Levitated Marker for Entity and Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/361058283_Packed_Levitated_Marker_for_Entity_and_Relation_Extraction"},{"title":"[2109.06067] Packed Levitated Marker for Entity and Relation Extraction","url":"https://arxiv.org/abs/2109.06067"},{"title":"Packed Levitated Marker for Entity and Relation Extraction","url":"https://bibbase.org/network/publication/ye-lin-li-sun-packedlevitatedmarkerforentityandrelationextraction-2022"},{"title":"Packed Levitated Marker for Entity and Relation Extraction - NASA/ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210906067Y/abstract"},{"title":"[2022 ACL]Packed Levitated Marker for Entity and Relation ...","url":"https://www.youtube.com/watch?v=aiS_iNOOUl8"},{"title":"[2109.06067v5] Packed Levitated Marker for Entity and Relation Extraction","url":"https://arxiv.org/abs/2109.06067v5"},{"title":"Papers with Code - Packed Levitated Marker for Entity and Relation Extraction","url":"https://paperswithcode.com/paper/pack-together-entity-and-relation-extraction"}]

I found the paper! Here are the search results for "Packed Levitated Marker for Entity and Relation Extraction":

**Publication Details:**
The paper was authored by Deming Ye, Yankai Lin, Peng Li, and Maosong Sun and published in 2022 as "Packed Levitated Marker for Entity and Relation Extraction." It appeared in the Proceedings of t
…[truncated 1322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:32:10.026149+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"From Hallucination to Structure Snowballing\" \"Alignment Tax\" \"Constrained Decoding\" Zhou arXiv 2604.06066"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"From Hallucination to Structure Snowballing\" \"Alignment Tax\" \"Constrained Decoding\" Zhou arXiv 2604.06066"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:32:10.026285+00:00_

Web search results for query: ""Grammar-Aligned Decoding" Park Berg-Kirkpatrick Polikarpova NeurIPS 2024"

Links: [{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"},{"title":"Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni · Grammar-Aligned Decoding","url":"https://slideslive.com/39028324/grammaraligned-decoding"}]

I found the paper "Grammar-Aligned Decoding" by the authors you mentioned. Here's what I found:

## Overview

The paper is by Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D'Antoni, and was presented at NeurIPS 2024 as part of the Main Conference Track.

## Problem and Solution

Large Language Models (LLMs) struggle with reliably generating highly structured outputs, such as program code, mathematical formulas, or well-formed markup. Constrained decoding approaches mitigate this problem by greedily restricting what tokens an LLM can output at each step to guarantee 
…[truncated 891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:32:10.026430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Autoregressive Entity Retrieval\" De Cao Izacard Riedel Petroni ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Autoregressive Entity Retrieval\" De Cao Izacard Riedel Petroni ICLR 2021"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:32:10.026564+00:00_

Web search results for query: ""Autoregressive Entity Retrieval" De Cao Izacard Riedel Petroni ICLR 2021"

Links: [{"title":"ICLR Spotlight Autoregressive Entity Retrieval","url":"https://iclr.cc/virtual/2021/spotlight/3521"},{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://openreview.net/pdf?id=5k8F6UU39V"},{"title":"Papers with Code - Autoregressive Entity Retrieval","url":"https://paperswithcode.com/paper/autoregressive-entity-retrieval"},{"title":"[PDF] Autoregressive Entity Retrieval | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Autoregressive-Entity-Retrieval-Cao-Izacard/572c12e81319ccd47cc0c637c82efadd03fd05ab"},{"title":"Autoregressive Entity Retrieval - Meta AI","url":"https://ai.meta.com/research/publications/autoregressive-entry-retrieval/"},{"title":"Autoregressive Entity Retrieval - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10167460/"},{"title":"dblp: Autoregressive Entity Retrieval.","url":"https://dblp.org/rec/conf/iclr/CaoI0P21.html"},{"title":"[2010.00904] Autoregressive Entity Retrieval","url":"https://arxiv.org/abs/2010.00904"}]

I found comprehensive information about the paper "Autoregressive Entity Retrieval" by De Cao, Izacard, Riedel, and Petroni from ICLR 2021.

## Overview

The paper is authored by Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni and was published at ICLR 2021.

## Main Contribution

The work addresses the ability to retrieve entities given a query, which is fundamental for knowledge-intensive tasks such as entity linking and open-domain question answering. The paper proposes GENRE (Generative Entity Retrieval), which takes an alternative approach to traditional classification-based methods.

## Key Findings

The research achieved new state-of-the-art or very competitive results on 
…[truncated 588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:32:10.026721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GenIE: Generative Information Extraction\" Josifoski De Cao Peyrard NAACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GenIE: Generative Information Extraction\" Josifoski De Cao Peyrard NAACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:32:10.026864+00:00_

Web search results for query: ""GenIE: Generative Information Extraction" Josifoski De Cao Peyrard NAACL 2022"

Links: [{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"GenIE: Generative Information Extraction","url":"https://aclanthology.org/2022.naacl-main.342.pdf"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"GenIE: Generative Information Extraction","url":"https://infoscience.epfl.ch/entities/publication/ac96118e-64f4-4d05-8461-aa27321afaeb"},{"title":"GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/epfl-dlab/GenIE"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=GenIE:+Generative+information+extraction&amp=&author=Martin+Josifoski&amp=&author=Nicola+De+Cao&amp=&author=Maxime+Peyrard&amp=&author=Fabio+Petroni&amp=&author=Robert+West&amp=&publication_year=2022&amp=&pages=4626-4643&amp=&doi=10.18653/v1/2022.naacl-main.342"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"[2112.08340] GenIE: Generative Information Extraction - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2112.08340"},{"title":"GenIE: Generative Information Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2112.08340"}]

I found comprehensive information about the GenIE paper. Here are the key details:

## Publication Information
GenIE: Generative Information Extraction was published at NAACL 2022 by Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, and Robert West. It appears in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4626–4
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:32:10.027010+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:32:10.027127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:32:10.027239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ADELIE: Aligning Large Language Models on Information Extraction\" Qi 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ADELIE: Aligning Large Language Models on Information Extraction\" Qi 2024"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:32:10.027354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\" Zaratiana 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction\" Zaratiana 2024"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:32:10.027466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\" Khorshidi 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs\" Khorshidi 2025"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:32:10.027578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Open Information Extraction with Entity Focused Constraints\" Upadhyay 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Open Information Extraction with Entity Focused Constraints\" Upadhyay 2023"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T10:32:10.027706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can LLMs be Knowledge Graph Curators for Validating Triple Insertions\" Regino 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can LLMs be Knowledge Graph Curators for Validating Triple Insertions\" Regino 2025"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:32:10.027825+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\" Tam 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models\" Tam 2024"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:32:10.027941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CRANE: Reasoning with Constrained LLM Generation\" Banerjee 2025 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CRANE: Reasoning with Constrained LLM Generation\" Banerjee 2025 ICML"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:32:10.028050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" Schall 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" Schall 2025"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:32:10.028158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"REBEL: Relation Extraction By End-to-end Language Generation\" Cabot Navigli 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"REBEL: Relation Extraction By End-to-end Language Generation\" Cabot Navigli 2021"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:32:10.028265+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SynCode: LLM Generation with Grammar Augmentation\" Ugare 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SynCode: LLM Generation with Grammar Augmentation\" Ugare 2024"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:32:10.028389+00:00_

Web search results for query: ""EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction" Zaratiana 2024"

Links: [{"title":"[2404.12493] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/abs/2404.12493"},{"title":"GitHub - urchade/EnriCo: EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction · GitHub","url":"https://github.com/urchade/enrico"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493v1"},{"title":"Paper page - EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://huggingface.co/papers/2404.12493"},{"title":"[PDF] EnriCo: Enriched Representation and Globally ...","url":"https://www.semanticscholar.org/paper/EnriCo:-Enriched-Representation-and-Globally-for-Zaratiana-Tomeh/5b1e811cd7f22cf5f9a76265ac4837626883df29"},{"title":"urchade (Urchade Zaratiana) · GitHub","url":"https://github.com/urchade"},{"title":"[Literature Review] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://www.themoonlight.io/en/review/enrico-enriched-representation-and-globally-constrained-inference-for-entity-and-relation-extraction"},{"title":"Urchade Zaratiana","url":"https://www.catalyzex.com/author/Urchade%20Zaratiana"},{"title":"Urchade Zaratiana","url":"https://scholar.google.com/citations?user=nQTXsu4AAAAJ&hl=fr"}]

I found the paper! Here are the search results for "EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction" by Zaratiana et al. (2024):

## Overview
EnriCo improves joint entity and relation extraction through attention mechanisms for rich representation and decoding algorithms for coherent output structure, achieving compe
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:32:10.028539+00:00_

Web search results for query: ""ADELIE: Aligning Large Language Models on Information Extraction" Qi 2024"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.419/"},{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub","url":"https://github.com/THU-KEG/ADELIE"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"dblp: ADELIE: Aligning Large Language Models on Information Extraction.","url":"https://dblp.org/rec/journals/corr/abs-2405-05008.html"},{"title":"Paper page - ADELIE: Aligning Large Language Models on Information Extraction","url":"https://huggingface.co/papers/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://paperreading.club/page?id=226238"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"}]

I found comprehensive information about this paper. Here are the results:

## ADELIE: Aligning Large Language Models on Information Extraction

**Publication Details:**
The paper "ADELIE: Aligning Large Language Models on Information Extraction" was authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bi
…[truncated 1256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:32:10.028705+00:00_

Web search results for query: ""Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models" Tam 2024"

Links: [{"title":"[2408.02442] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/abs/2408.02442"},{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.91/"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240802442R/abstract"},{"title":"[PDF] Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let-Me-Speak-Freely-A-Study-On-The-Impact-Of-Format-Tam-Wu/7c394a8b4db70d7424abc300749fff0fe580bdae"},{"title":"[2408.02442v1] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/abs/2408.02442v1"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"},{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. | Request PDF","url":"https://www.researchgate.net/publication/386203559_Let_Me_Speak_Freely_A_Study_On_The_Impact_Of_Format_Restrictions_On_Large_Language_Model_Performance"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/let-me-speak-freely-study-impact-format"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models. | BibSonomy","url":"https
…[truncated 1316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:32:10.028888+00:00_

Web search results for query: ""The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" Schall 2025"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"Constrained Decoding with Speculative Lookaheads","url":"https://aclanthology.org/2025.naacl-long.239.pdf"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"}]

I found the paper you're looking for! "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" by Schall and de Melo was published at RANLP 2025 (the 15th International Conference on Recent Advances in Natural Language Processing).

Here are the key findings from the paper:

The paper examines how Large Language Models excel at generating fluent text, but real-world applications increasingly demand structured outputs like JSON that can be programmatically processed. The research investigates the interaction between task performance and format compliance through comprehensive experiments across 11 models and multiple benchmarks.

**Key discoveries:**

- The authors unco
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:32:10.029062+00:00_

Web search results for query: ""Can LLMs be Knowledge Graph Curators for Validating Triple Insertions" Regino 2025"

Links: [{"title":"Can LLMs be Knowledge Graph Curators for Validating Triple Insertions? - ACL Anthology","url":"https://aclanthology.org/2025.genaik-1.10/"},{"title":"Can LLMs be Knowledge Graph Curators for Validating ...","url":"https://aclanthology.org/2025.genaik-1.10.pdf"},{"title":"Knowledge graph validation by integrating LLMs and human-in-the-loop - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S030645732500086X"},{"title":"Knowledge graph validation by integrating LLMs and human-in-the-loop | Information Processing and Management: an International Journal","url":"https://dl.acm.org/doi/10.1016/j.ipm.2025.104145"},{"title":"COLING 2025 Workshop on Generative AI and Knowledge Graphs (GenAIK)","url":"https://aclanthology.org/2025.genaik-1.pdf"},{"title":"A multi-view validation framework for LLM-generated knowledge graphs of chronic kidney disease - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12689688/"},{"title":"[2411.17388v2] Can LLMs be Good Graph Judger for Knowledge Graph Construction?","url":"https://arxiv.org/abs/2411.17388v2"},{"title":"From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium","url":"https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"}]

I found the paper you're looking for! Here's the information about it:

"Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?" was published by Regino and dos Reis in 2025 in the Proceedings of the Workshop on Generative AI and Knowledge Graphs (GenAIK), pages 87–99, Abu Dhabi, UAE.

The paper addresses how as Knowledge Graphs (KGs) become central to modern applications, automated methods for validating RDF triples before insertion into these graphs are essential. The complexity and scalability challenges in 
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T10:32:10.029221+00:00_

Web search results for query: ""ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs" Khorshidi 2025"

Links: [{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/odke"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"},{"title":"[PDF] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ODKE+:-Ontology-Guided-Open-Domain-Knowledge-with-Khorshidi-Nikfarjam/23991e9d5ab7780527a1753633a7f065c5da4663"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/odke-ontology-guided-open-domain-knowledge-extraction"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs - haebom","url":"https://slashpage.com/haebom/7vgjr4m1nwwwz2dwpy86?lang=en&tl=en"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"}]

I found detailed information about this paper. Here's what the search revealed:

## Overview

ODKE+ is a production-grade system that automatically extracts and ingests millions of open-domain facts from web sources with high precision, addressing the challenge that knowledge graphs are foundational to many AI applications but maintaining their freshness and completeness remains costly.

## System Architecture

ODKE+ combines modular components into a scalable pipeline: (1) the Extraction Initiator detects mi
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T10:32:10.029374+00:00_

Web search results for query: ""Open Information Extraction with Entity Focused Constraints" Upadhyay 2023"

Links: [{"title":"Open Information Extraction with Entity Focused Constraints - ACL Anthology","url":"https://aclanthology.org/2023.findings-eacl.95/"},{"title":"Open Information Extraction with Entity Focused Constraints | Request PDF","url":"https://www.researchgate.net/publication/373810294_Open_Information_Extraction_with_Entity_Focused_Constraints"},{"title":"Open Information Extraction with Entity Focused Constraints - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-03980046v1"},{"title":"Open Information Extraction with Entity Focused Constraints - CNRS - Centre national de la recherche scientifique","url":"https://cnrs.hal.science/hal-03980046/"},{"title":"Open Information Extraction with Entity Focused Constraints - Laboratoire d'informatique de l'X (LIX)","url":"https://pasteur.hal.science/X-LIX/hal-03980046v1"},{"title":"Open Information Extraction with Entity Focused Constraints - Département d'informatique","url":"https://laas.hal.science/X-DEP-INFO/hal-03980046v1"},{"title":"EACL 2023: “Open Information Extraction with Entity Focused Constraints” – CEDAR: Rich Data Analytics at Cloud Scale","url":"https://team.inria.fr/cedar/eacl-2023-open-information-extraction-with-entity-focused-constraints/"},{"title":"GitHub - prajnaupadhyay/openie-with-entities · GitHub","url":"https://github.com/prajnaupadhyay/openie-with-entities"},{"title":"Open Information Extraction with Entity Focused Constraints | Underline","url":"https://underline.io/lecture/71946-open-information-extraction-with-entity-focused-constraints"}]

I found the paper! Here are the search results for "Open Information Extraction with Entity Focused Constraints" by Upadhyay et al. (2023):

## Publication Details

The paper was authored by Prajna Upadhyay, Oana Balalau, and Ioana Manolescu and published in the Findings o
…[truncated 1119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:32:10.029525+00:00_

Web search results for query: ""REBEL: Relation Extraction By End-to-end Language Generation" Cabot Navigli 2021"

Links: [{"title":"REBEL: Relation Extraction By End-to-end Language generation - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.204/"},{"title":"GitHub - Babelscape/rebel: REBEL is a seq2seq model that simplifies Relation Extraction (EMNLP 2021). · GitHub","url":"https://github.com/Babelscape/rebel"},{"title":"REBEL: Relation Extraction By End-to-end Language generation","url":"https://babelscape.com/research/publication/rebel-relation-extraction-by-end-to-end-language-generation"},{"title":"REBEL: Relation Extraction By End-to-end Language generation - ORKG","url":"https://orkg.org/paper/R172701"},{"title":"Babelscape/rebel-large · Hugging Face","url":"https://huggingface.co/Babelscape/rebel-large"},{"title":"(PDF) REBEL: Relation Extraction By End-to-end Language generation","url":"https://www.researchgate.net/publication/357387727_REBEL_Relation_Extraction_By_End-to-end_Language_generation"},{"title":"REBEL: Relation Extraction by End-to-end Language generation","url":"https://www.mendeley.com/catalogue/00c70289-0c2c-3a4e-9653-8d79650131b5/"},{"title":"REBEL: Relation Extraction By End-to-end Language generation","url":"https://ai.updf.com/paper-detail/rebel-relation-extraction-by-end-to-end-language-generation-cabot-navigli-cbc449ea3d410c127db81e37ca6b6387c6d05cdc"},{"title":"REBEL: Relation Extraction By End-to-end Language generation | BibSonomy","url":"https://www.bibsonomy.org/bibtex/4ad7b2e29c3facbc1b59e5e8216720fd"}]

Based on the search results, here's what I found about "REBEL: Relation Extraction By End-to-end Language Generation":

## Overview

REBEL is a seq2seq model based on BART that performs end-to-end relation extraction for more than 200 different relation types. The paper was authored by Pere-Lluís Huguet Cabot and Roberto Navigli and published in the Findings of the Association for Computational Linguistics: EM
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:32:10.029688+00:00_

Web search results for query: ""CRANE: Reasoning with Constrained LLM Generation" Banerjee 2025 ICML"

Links: [{"title":"ICML Poster CRANE: Reasoning with constrained LLM generation","url":"https://icml.cc/virtual/2025/poster/43624"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://proceedings.mlr.press/v267/banerjee25a.html"},{"title":"ICLR CRANE: Reasoning with constrained LLM generation","url":"https://iclr.cc/virtual/2025/36222"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"Improving Procedural Skill Explanations via Constrained Generation: A","url":"https://arxiv.org/pdf/2511.20942"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"dblp: CRANE: Reasoning with constrained LLM generation.","url":"https://dblp.org/rec/journals/corr/abs-2502-09061.html"}]

Based on the search results, I found comprehensive information about the paper "CRANE: Reasoning with Constrained LLM Generation" by Banerjee et al. (2025) published at ICML:

## Overview

CRANE is a constrained decoding algorithm that combines reasoning capabilities with structural correctness.

## Problem Statement

Constrained LLM generation is a promising direction to enforce adherence to formal grammar, but prior works have empirically observed that strict enforcement of formal constraints often diminishes the reasoning capabilities of LLMs.

## Key Contributions

The paper addresses this problem in two ways:

1. **Theoretical Contribution**: The authors provide a theoretical explanation for why constraining LLM outputs to very restrictive grammars that only allow syntactically valid final answers redu
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:32:10.029847+00:00_

Web search results for query: ""SynCode: LLM Generation with Grammar Augmentation" Ugare 2024"

Links: [{"title":"[2403.01632] SynCode: LLM Generation with Grammar Augmentation","url":"https://arxiv.org/abs/2403.01632"},{"title":"[PDF] SynCode: LLM Generation with Grammar Augmentation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCode:-LLM-Generation-with-Grammar-Augmentation-Ugare-Suresh/46a41357eadac1459c81588136c5c053abfeefe4"},{"title":"Improving LLM Code Generation with Grammar Augmentation","url":"https://www.catalyzex.com/paper/improving-llm-code-generation-with-grammar"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Paper Detail","url":"https://deeplearn.org/arxiv/546356/syncode:-llm-generation-with-grammar-augmentation"},{"title":"[2403.01632v1] Improving LLM Code Generation with Grammar Augmentation","url":"https://arxiv.org/abs/2403.01632v1"},{"title":"Paper page - SynCode: LLM Generation with Grammar Augmentation","url":"https://huggingface.co/papers/2403.01632"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"Improving LLM Code Generation with Grammar Augmentation","url":"https://arxiv.org/html/2403.01632v1"},{"title":"Accelerating LLM Code Generation Through Mask Store Streamlining","url":"https://huggingface.co/blog/vivien/grammar-llm-decoding"}]

I found detailed information about SynCode. Here's what the research paper covers:

## Overview

SynCode is a novel framework for efficient and general syntactical decoding of code with large language models (LLMs) that leverages the grammar of a programming language, utilizing an offline-constructed efficient lookup table called DFA mask store based on language grammar terminals.

## Purpose and Challenge Addressed

LLM outputs need to adhere to a specific format for integration with other components in systems, with format ru
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T10:32:10.029989+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCode Ugare \"Transactions on Machine Learning Research\" TMLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCode Ugare \"Transactions on Machine Learning Research\" TMLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:32:10.030108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.04696 ODKE+ submission date September 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.04696 ODKE+ submission date September 2025"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-26T10:32:10.030229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2024.emnlp-industry.91 \"Let Me Speak Freely\" title exact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2024.emnlp-industry.91 \"Let Me Speak Freely\" title exact"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:32:10.030345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EnriCo Zaratiana 2024 published venue conference journal ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EnriCo Zaratiana 2024 published venue conference journal ACL EMNLP"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-26T10:32:10.030464+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE Banerjee 2025 ICML pages authors Debangshu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE Banerjee 2025 ICML pages authors Debangshu"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:32:10.030600+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 41-50",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**41. ugare2025itergen**\n```\n@inproceedings{ugare2025itergen,\n  title = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},\n  author = {Ugare, Shubham and Gumaste, Rohan and Suresh, Tarun and Singh, Gagandeep and Misailovic, Sasa},\n  booktitle = {The Thirteenth International Conference on Learning Representations},\n  year = {2025},\n  url = {https://openreview.net/forum?id=ac93gRzxxV}\n}\n```\nCitation context: section6_related_work.tex L18 \"backtracking\" → \\cite{ugare2025itergen}; appendix_related_work.tex.\n\n---\n\n**42. boostcd2025**\n```\n@inproceedings{boostcd2025,\n  title = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},\n  author = {Sakota, Marija and West, Robert},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://aclanthology.org/2025.emnlp-main.926/}\n}\n```\nCitation context: section6_related_work.tex L17 \"grammar-only\" → \\cite{boostcd2025}; section5_runtime.tex L64 → \\cite{boostcd2025}; appendix_discussion.tex L596,650-654,672.\n\n---\n\n**43. luan2018scierc**\n```\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  pages = {3219--3232},\n  year = {2018},\n  address = {Brussels, Belgium},\n  url = {https://aclanthology.org/D18-1360/}\n}\n```\nCitation context: section3_violation_landscape.tex L8 \"datasets\" → \\cite{luan2018scierc}.\n\n---\n\n**44. yao2019docred**\n```\n@inproceedings{yao2019docred,\n  title = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n  author = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages = {764--777},\n  year = {2019},\n  address = {Florence, Italy},\n  url = {https://aclanthology.org/P19-1074/}\n}\n```\nCitation context: section3_violation_landscape.tex L8 \"datasets\" → \\cite{yao2019docred}.\n\n---\n\n**45. wei2023zeroshot**\n```\n@article{wei2023zeroshot,\n  title = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},\n  author = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},\n  journal = {arXiv preprint arXiv:2302.10205},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.10205}\n}\n```\nCitation context: section1_introduction_draft.tex L6 \"LLMs are increasingly used for IE\" → \\cite{wei2023zeroshot}.\n\n---\n\n**46. qwen2025qwen3**\n```\n@article{qwen2025qwen3,\n  title = {Qwen3 Technical Report},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.09388}\n}\n```\nCitation context: section3_violation_landscape.tex L11 \"model\" → \\cite{qwen2025qwen3}.\n\n---\n\n**47. zheng2024sglang**\n```\n@inproceedings{zheng2024sglang,\n  title = {{SGLang}: Efficient Execution of Structured Language Model Programs},\n  author = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {37},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.07104}\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{zheng2024sglang}.\n\n---\n\n**48. li2021document**\n```\n@inproceedings{li2021document,\n  title = {Document-Level Event Argument Extraction by Conditional Generation},\n  author = {Li, Sha and Ji, Heng and Han, Jiawei},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {894--908},\n  year = {2021},\n  url = {https://aclanthology.org/2021.naacl-main.69/}\n}\n```\nCitation context: appendix_discussion.tex L547 \"WikiEvents\" → \\cite{li2021document}; appendix_wikievents_pilot.tex L6 and L57 → \\cite{li2021document}.\n\n---\n\n**49. guidex2025**\n```\n@inproceedings{guidex2025,\n  author = {De La Fuente, Neil and Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agirre, Eneko},\n  title = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2025.findings-acl.1245/},\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{guidex2025}.\n\n---\n\n**50. jsonschemabench2025**\n```\n@article{jsonschemabench2025,\n  author = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n  title = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n  journal = {arXiv preprint arXiv:2501.10868},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.10868},\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{jsonschemabench2025}.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 41-50",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**41. ugare2025itergen**\n```\n@inproceedings{ugare2025itergen,\n  title = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},\n  author = {Ugare, Shubham and Gumaste, Rohan and Suresh, Tarun and Singh, Gagandeep and Misailovic, Sasa},\n  booktitle = {The Thirteenth International Conference on Learning Representations},\n  year = {2025},\n  url = {https://openreview.net/forum?id=ac93gRzxxV}\n}\n```\nCitation context: section6_related_work.tex L18 \"backtracking\" → \\cite{ugare2025itergen}; appendix_related_work.tex.\n\n---\n\n**42. boostcd2025**\n```\n@inproceedings{boostcd2025,\n  title = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},\n  author = {Sakota, Marija and West, Robert},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://aclanthology.org/2025.emnlp-main.926/}\n}\n```\nCitation context: section6_related_work.tex L17 \"grammar-only\" → \\cite{boostcd2025}; section5_runtime.tex L64 → \\cite{boostcd2025}; appendix_discussion.tex L596,650-654,672.\n\n---\n\n**43. luan2018scierc**\n```\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  pages = {3219--3232},\n  year = {2018},\n  address = {Brussels, Belgium},\n  url = {https://aclanthology.org/D18-1360/}\n}\n```\nCitation context: section3_violation_landscape.tex L8 \"datasets\" → \\cite{luan2018scierc}.\n\n---\n\n**44. yao2019docred**\n```\n@inproceedings{yao2019docred,\n  title = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n  author = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages = {764--777},\n  year = {2019},\n  address = {Florence, Italy},\n  url = {https://aclanthology.org/P19-1074/}\n}\n```\nCitation context: section3_violation_landscape.tex L8 \"datasets\" → \\cite{yao2019docred}.\n\n---\n\n**45. wei2023zeroshot**\n```\n@article{wei2023zeroshot,\n  title = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},\n  author = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},\n  journal = {arXiv preprint arXiv:2302.10205},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.10205}\n}\n```\nCitation context: section1_introduction_draft.tex L6 \"LLMs are increasingly used for IE\" → \\cite{wei2023zeroshot}.\n\n---\n\n**46. qwen2025qwen3**\n```\n@article{qwen2025qwen3,\n  title = {Qwen3 Technical Report},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.09388}\n}\n```\nCitation context: section3_violation_landscape.tex L11 \"model\" → \\cite{qwen2025qwen3}.\n\n---\n\n**47. zheng2024sglang**\n```\n@inproceedings{zheng2024sglang,\n  title = {{SGLang}: Efficient Execution of Structured Language Model Programs},\n  author = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {37},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.07104}\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{zheng2024sglang}.\n\n---\n\n**48. li2021document**\n```\n@inproceedings{li2021document,\n  title = {Document-Level Event Argument Extraction by Conditional Generation},\n  author = {Li, Sha and Ji, Heng and Han, Jiawei},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages = {894--908},\n  year = {2021},\n  url = {https://aclanthology.org/2021.naacl-main.69/}\n}\n```\nCitation context: appendix_discussion.tex L547 \"WikiEvents\" → \\cite{li2021document}; appendix_wikievents_pilot.tex L6 and L57 → \\cite{li2021document}.\n\n---\n\n**49. guidex2025**\n```\n@inproceedings{guidex2025,\n  author = {De La Fuente, Neil and Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agirre, Eneko},\n  title = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  publisher = {Association for Computational Linguistics},\n  url = {https://aclanthology.org/2025.findings-acl.1245/},\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{guidex2025}.\n\n---\n\n**50. jsonschemabench2025**\n```\n@article{jsonschemabench2025,\n  author = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n  title = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n  journal = {arXiv preprint arXiv:2501.10868},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.10868},\n}\n```\nCitation context: section6_related_work.tex L8 → \\cite{jsonschemabench2025}.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:32:10.031009+00:00_

I have enough information now. The arXiv listing (2201.11227) shows "Christopher Meek" as the official author name, which matches the BibTeX. Now let me compile the full verification results.

Here are the verification results for all 10 BibTeX entries:

---

**[kwon2023vllm] ✓**
- 存在性: ✓
- 作者: ✓ (9 authors match: Kwon, Li, Zhuang, Sheng, Zheng, Yu, Gonzalez, Zhang, Stoica)
- 年份: ✓ (2023)
- 标题: ✓ (exact match)
- Venue: ✓ (Proceedings of the 29th Symposium on Operating Systems Principles, SOSP 2023)
- DOI/arXiv: 未提供但可补充 (DOI: 10.1145/3600006.3613165, arXiv: 2309.06180)
- 正文引用: ✓ (vLLM serving engine context is appropriate)
- 备注: 无问题

---

**[synchromesh_iclr2022] ✓**
- 存在性: ✓
- 作者: ✓ (Poesia, Polozov, Le, Tiwari, Soares, Meek, Gulwani -- all match. arXiv uses "Christopher Meek" consistent with BibTeX)
- 年份: ✓ (2022)
- 标题: ✓ (exact match)
- Venue: ✓ (ICLR 2022)
- DOI/arXiv: ✓ (OpenReview URL matches: KmtVD97J43e)
- 正文引用: ✓
- 备注: 无问题

---

**[mgd_neurips2023] ✓**
- 存在性: ✓
- 作者: ✓ (Agrawal, Kanade, Goyal, Lahiri, Rajamani)
- 年份: ✓ (2023)
- 标题: ✓ (exact match)
- Venue: ✓ (NeurIPS 2023, volume 36)
- DOI/arXiv: ✓ (NeurIPS proceedings URL matches)
- 正文引用: ✓
- 备注: 无问题

---

**[pldi2025_type_constrained_codegen] ✓**
- 存在性: ✓
- 作者: ✓ (Mündler, He, Wang, Sen, Song, Vechev)
- 年份: ✓ (2025)
- 标题: ✓ (exact match)
- Venue: ✓ (Proceedings of the ACM on Programming Languages, Volume 9, Number PLDI)
- DOI/arXiv: ✓ (DOI 10.1145/3729274 confirmed via ACM DL)
- 正文引用: ✓
- 备注: 无问题

---

**[roth_yih_2004] ✓**
- 存在性: ✓
- 作者: ✓ (Roth, Dan and Yih, Wen-tau)
- 年份: ✓ (2004)
- 标题: ✓ (exact match)
- Venue: ✓ (CoNLL-2004 at HLT-NAACL 2004, pages 1-8, Boston)
- DOI/arXiv: ✓ (ACL Anthology URL W04-2401 confirmed)
- 正文引用: ✓
- 备注: 无问题

---

**[adakgc_emnlp2023] ✓**
- 存在性: ✓
- 作者: ✓ (Ye, Gui, Xu, Chen Xi, Chen Huajun, Zhang Ningyu)
- 年份: ✓ (2023)
- 标题: ✓ (exact match)
- Venue: ✓ (Findings of EMNLP 2023, pages 6408-6431)
- DOI/arXiv: ✓ (ACL Anthology 2023.findings-emnlp.425 confirmed)
- 正文引用: ✓
- 备注: 无问题

…[truncated 2187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 14
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-26T10:32:10.031192+00:00_

Web search results for query: ""From Hallucination to Structure Snowballing" "Alignment Tax" "Constrained Decoding" Zhou arXiv 2604.06066"

Links: [{"title":"[2604.06066] From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/abs/2604.06066"},{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/html/2604.06066"},{"title":"[2407.00569] Investigating and Mitigating the Multimodal Hallucination Snowballing in Large Vision-Language Models","url":"https://arxiv.org/abs/2407.00569"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603"},{"title":"Visual Multi-Agent System: Mitigating Hallucination Snowballing via Visual Flow","url":"https://arxiv.org/html/2509.21789v2"},{"title":"[2509.21789] Visual Multi-Agent System: Mitigating Hallucination Snowballing via Visual Flow","url":"https://arxiv.org/abs/2509.21789"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.pdf"},{"title":"SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models","url":"https://arxiv.org/html/2601.03500"},{"title":"Investigating and Mitigating the Multimodal Hallucination ...","url":"https://aclanthology.org/2024.acl-long.648.pdf"}]

I found the paper! Here's the information about the research:

The paper addresses how intrinsic self-correction in Large Language Models frequently fails in open-ended reasoning tasks due to "hallucination snowballing," a phenomenon in which models recursively justify early errors during free-text reflection.

The study investigates whether enforcing structured reflection purely through Outlines-based co
…[truncated 792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T10:32:10.031395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"XGrammar: Flexible and Efficient Structured Generation Engine\" Dong Ruan Cai Chen 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"XGrammar: Flexible and Efficient Structured Generation Engine\" Dong Ruan Cai Chen 2025"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T10:32:10.031575+00:00_

Web search results for query: ""XGrammar: Flexible and Efficient Structured Generation Engine" Dong Ruan Cai Chen 2025"

Links: [{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241115100D/abstract"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/551290/xgrammar:-flexible-and-efficient-structured-generation-engine-for-large-language-models"},{"title":"MLSys Poster XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://mlsys.org/virtual/2025/poster/3235"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"[2411.15100v1] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100v1"},{"title":"dblp: XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2411-15100.html"}]

I found comprehensive information about XGrammar. Here are the key findings:

## Overview

XGrammar is a flexible and efficient structured generation engine for large language models wi
…[truncated 1364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T10:32:10.031777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Efficient Guided Generation for Large Language Models\" Willard Louf arXiv 2307.09702"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Efficient Guided Generation for Large Language Models\" Willard Louf arXiv 2307.09702"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:32:10.031937+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\" Geng Josifoski EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\" Geng Josifoski EMNLP 2023"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:32:10.032086+00:00_

Web search results for query: ""Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" Geng Josifoski EMNLP 2023"

Links: [{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.674/"},{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks ...","url":"https://dlab.epfl.ch/people/west/pub/Geng-Josifoski-Peyrard-West_EMNLP-23.pdf"},{"title":"[PDF] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Request PDF","url":"https://www.researchgate.net/publication/376402267_Grammar-Constrained_Decoding_for_Structured_NLP_Tasks_without_Finetuning"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"}]

I found the paper you're looking for! Here are the key details:

**Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning** is authored by Saibo Geng, Martin Josifoski, Maxime Peyrard, and Robert West, published at EMNLP 2023.

The paper was published in the Proceedings of the 2023 Conference on Empirical Methods in N
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:32:10.032237+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\" Lu West Zellers NAACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints\" Lu West Zellers NAACL 2021"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T10:32:10.032375+00:00_

Web search results for query: ""NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints" Lu West Zellers NAACL 2021"

Links: [{"title":"[2010.12884] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints","url":"https://arxiv.org/abs/2010.12884"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.339/"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Request PDF","url":"https://www.researchgate.net/publication/344894390_NeuroLogic_Decoding_Unsupervised_Neural_Text_Generation_with_Predicate_Logic_Constraints"},{"title":"[2010.12884v2] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints","url":"https://arxiv.org/abs/2010.12884v2"},{"title":"[PDF] NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NeuroLogic-Decoding:-(Un)supervised-Neural-Text-Lu-West/2c5bf29079cd958a2bef150077a02a1deb300652"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | DeepAI","url":"https://deepai.org/publication/neurologic-decoding-un-supervised-neural-text-generation-with-predicate-logic-constraints"},{"title":"NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints | Zendy","url":"https://zendy.io/pdf-viewer/2010.12884"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints

**Authors:** Ximing Lu, Peter West, Rowan Zellers, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi

**Publication:** Proceedings of the 2021 Conference of the North American Chapter of the Association for Computation
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-26T10:32:10.032515+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Unified Structure Generation for Universal Information Extraction\" Lu Liu Dai ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Unified Structure Generation for Universal Information Extraction\" Lu Liu Dai ACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:32:10.032649+00:00_

Web search results for query: "CRANE Banerjee 2025 ICML pages authors Debangshu"

Links: [{"title":"Debangshu Banerjee","url":"https://debangshu-banerjee.github.io/"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://proceedings.mlr.press/v267/banerjee25a.html"},{"title":"Debangshu Banerjee's research works | University of Illinois Urbana-Champaign and other places","url":"https://www.researchgate.net/scientific-contributions/Debangshu-Banerjee-2248320619"},{"title":"dblp: Debangshu Banerjee","url":"https://dblp.org/pid/268/6756.html"},{"title":"ICML Outstanding Paper: Interpreting Robustness Proofs of Deep Neural Networks - Debangshu Banerjee, Avaljot Singh, Gagandeep Singh","url":"https://icml.cc/virtual/2023/25697"},{"title":"ICML 2025 Program Committee - Meta Reviewer","url":"https://icml.cc/Conferences/2025/ProgramCommittee"},{"title":"dblp: Debangshu Banerjee 0001","url":"https://dblp.org/pid/268/6756-1.html"},{"title":"[Literature Review] CRANE: Reasoning with constrained LLM generation","url":"https://www.themoonlight.io/en/review/crane-reasoning-with-constrained-llm-generation"},{"title":"(PDF) CRANE: Reasoning with constrained LLM generation","url":"https://www.researchgate.net/publication/388964154_CRANE_Reasoning_with_constrained_LLM_generation"}]

Based on the search results, here's the information about the CRANE paper at ICML 2025:

**Paper Title:** CRANE: Reasoning with constrained LLM generation

**Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, and Gagandeep Singh

**Conference:** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:2836-2857, 2025

**Pages:** 2836-2857

**Abstract:** Code generation, symbolic math reasoning, and other tasks require LLMs to produce outputs that are both syntactically and semantically correct. Constrained LLM generation is a promising direction to enforce adherence to formal grammar, but prior works have empirically observed that strict 
…[truncated 189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:32:10.032957+00:00_

Web search results for query: "EnriCo Zaratiana 2024 published venue conference journal ACL EMNLP"

Links: [{"title":"[2404.12493] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/abs/2404.12493"},{"title":"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.300/"},{"title":"Urchade Zaratiana","url":"https://urchade.github.io/"},{"title":"urchade (Urchade Zaratiana) · GitHub","url":"https://github.com/urchade"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29919"},{"title":"Urchade Zaratiana - ACL Anthology","url":"https://aclanthology.org/people/u/urchade-zaratiana/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/calls/papers/"},{"title":"FI Group at SemEval-2024 Task 8: A Syntactically Motivated Architecture for Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.170/"}]

Based on the search results, I found information about Urchade Zaratiana's 2024 publications. Here are the key findings:

**EnriCo Paper:**
EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction was authored by Urchade Zaratiana and 4 other authors, and was posted on arXiv on April 18, 2024. However, the search results do not show it being published in ACL or EMNLP venues.

**Other 2024 Publications:**
Zaratiana had other publications in 2024:
- GLiNER: Generalist Model for Named Entity Recognition was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024)
- An Autoregressive Text-to-Graph Framework for Joint Entity 
…[truncated 511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:32:10.033138+00:00_

Web search results for query: "arXiv 2509.04696 ODKE+ submission date September 2025"

Links: [{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"[PDF] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ODKE+:-Ontology-Guided-Open-Domain-Knowledge-with-Khorshidi-Nikfarjam/23991e9d5ab7780527a1753633a7f065c5da4663"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=32675&show=500"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3125&show=2000"},{"title":"Populations and Evolution Sep 2025","url":"https://arxiv.org/list/q-bio.PE/2025-09?skip=25&show=250"},{"title":"Computer Science Sep 2025","url":"https://arxiv.org/list/cs/2025-09?skip=7300&show=100"}]

Based on the search results, I found the information you're looking for:

The arXiv paper 2509.04696 titled "ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs" was submitted on September 4, 2025.

ODKE+ is a production-grade system that automatically extracts and ingests millions of open-domain facts from web sources with high precision. The system dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, enabling scalable, type-consistent fact extraction across 195 predicates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:32:10.033290+00:00_

Web search results for query: "SynCode Ugare "Transactions on Machine Learning Research" TMLR 2024"

Links: [{"title":"dblp: Transactions on Machine Learning Research, Volume 2024","url":"https://dblp.org/db/journals/tmlr/tmlr2024.html"},{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"Published in Transactions on Machine Learning Research (05/2025)","url":"https://openreview.net/pdf/3fb997932692936d6eb32d47a91a242487c69ae3.pdf"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"Transactions on Machine Learning Research (TMLR), 2024 Archives - RBC Borealis","url":"https://rbcborealis.com/conferences/transactions-on-machine-learning-research-tmlr-2024/"},{"title":"Transactions on Machine Learning Research (@TmlrOrg) ...","url":"https://x.com/tmlrorg?lang=de"},{"title":"Transactions on Machine Learning Research – Medium","url":"https://medium.com/@TmlrOrg"},{"title":"Transactions on Machine Learning Research (@TmlrOrg) / X","url":"https://twitter.com/tmlrorg?lang=en"},{"title":"Transactions on Machine Learning Research (TMLR)","url":"https://dblp.org/db/journals/tmlr/index.html"}]

Based on the search results, I found information about SynCode and its publication:

SynCode: LLM Generation with Grammar Augmentation was authored by Shubham Ugare and colleagues and published in Transactions on Machine Learning Research. Note that the publication was listed as 2025, rather than 2024.

SynCode is a novel framework for efficient and general syntactical decoding with LLMs that ensures soundness and completeness with respect to context-free grammars (CFGs), effectively retaining valid tokens while filtering out invalid ones. SynCode seamlessly integrates with any language defined by CF
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-26T10:32:10.033442+00:00_

Web search results for query: "aclanthology.org 2024.emnlp-industry.91 "Let Me Speak Freely" title exact"

Links: [{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.91/"},{"title":"Let Me Speak Freely? A Study on the Impact of Format ...","url":"https://aclanthology.org/2024.emnlp-industry.91.pdf"},{"title":"2024.emnlp-industry.0.pdf","url":"https://aclanthology.org/2024.emnlp-industry.0.pdf"},{"title":"Aclanthology","url":"https://aclanthology.org/2024.emnlp-main.146.pdf"},{"title":"Industry Track - EMNLP 2024","url":"https://2024.emnlp.org/program/industry/"},{"title":"Conflicts of Interest in Published NLP Research 2000-2024","url":"https://arxiv.org/pdf/2502.16218"}]

I found the paper you were looking for! Here are the details:

The paper "Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance." was authored by Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, and Yun-Nung Chen and published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track (pages 1218–1236, Miami, Florida, US).

The paper is available at: https://aclanthology.org/2024.emnlp-industry.91/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:32:10.033583+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net SynCode \"HiUZtgAPoH\" TMLR publication date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net SynCode \"HiUZtgAPoH\" TMLR publication date"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:32:10.033730+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Anthology \"Let Me Speak Freely\" EMNLP industry 2024 exact title \"Performance\" vs \"Large Language Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Anthology \"Let Me Speak Freely\" EMNLP industry 2024 exact title \"Performance\" vs \"Large Language Models\""
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:32:10.033856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RANLP 2025 Schall de Melo \"Hidden Cost of Structure\" pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RANLP 2025 Schall de Melo \"Hidden Cost of Structure\" pages"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-26T10:32:10.033982+00:00_

Web search results for query: "RANLP 2025 Schall de Melo "Hidden Cost of Structure" pages"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"Accepted papers","url":"https://ranlp.org/ranlp2025/index.php/accepted-papers/"},{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 1074–1084","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"Recognition Performance of a Structured Language Model","url":"https://arxiv.org/pdf/cs/0001022"},{"title":"Structured Language Modeling for Speech Recognition","url":"https://arxiv.org/pdf/cs/0001023"},{"title":"Discrete Structural Planning for Neural Machine Translation","url":"https://arxiv.org/pdf/1808.04525"},{"title":"Finding Structure in Language Models","url":"https://arxiv.org/pdf/2411.16433"}]

Based on the search results, I found the information about the paper:

"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" by Maximilian Schall and Gerard de Melo was published in the Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing, pages 1074–1084, which took place in Varna, Bulgaria.

The paper was presented at the conference held September 8–10, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:32:10.034128+00:00_

Web search results for query: "ACL Anthology "Let Me Speak Freely" EMNLP industry 2024 exact title "Performance" vs "Large Language Models""

Links: [{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.91/"},{"title":"Let Me Speak Freely? A Study on the Impact of Format ...","url":"https://aclanthology.org/2024.emnlp-industry.91.pdf"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.emnlp-industry.0.pdf"},{"title":"Industry Track - EMNLP 2024","url":"https://2024.emnlp.org/program/industry/"},{"title":"The ACL OCL Corpus: Advancing Open Science in Computational Linguistics","url":"https://arxiv.org/pdf/2305.14996"},{"title":"ACL Anthology Helper: A Tool to Retrieve and Manage Literature from ACL   Anthology","url":"https://arxiv.org/pdf/2310.20467"},{"title":"Revealing Trends in Datasets from the 2022 ACL and EMNLP Conferences","url":"https://arxiv.org/pdf/2404.08666"},{"title":"Exploring the Landscape of Natural Language Processing Research","url":"https://arxiv.org/pdf/2307.10652"}]

Based on the search results, I found the paper you're looking for:

"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance." is published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track.

The exact title includes both components you mentioned:
- **"Let Me Speak Freely?"** (the main title)
- **"A Study On The Impact Of Format Restrictions On Large Language Model Performance."** (the subtitle)

The paper is authored by Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, and Yun-Nung Chen, and it's available on the ACL Anthology at https://aclanthology.org/2024.emnlp-industry.91/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyp
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:32:10.034267+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:32:10.034380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:32:10.034491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\" Ugare ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\" Ugare ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-26T10:32:10.034614+00:00_

Web search results for query: ""IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking" Ugare ICLR 2025"

Links: [{"title":"[2410.07295] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://arxiv.org/abs/2410.07295"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | OpenReview","url":"https://openreview.net/forum?id=ac93gRzxxV"},{"title":"ICLR Poster IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://iclr.cc/virtual/2025/poster/29157"},{"title":"IterGen: Iterative Semantic-aware Structured LLM ...","url":"https://iclr.cc/media/iclr-2025/Slides/29157.pdf"},{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"[Literature Review] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking","url":"https://www.themoonlight.io/en/review/itergen-iterative-semantic-aware-structured-llm-generation-with-backtracking"},{"title":"[PDF] IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/8f918a87d0f1bc090fca1dbdfbc4d06a9dc88a66"},{"title":"Componentization: Decomposing Monolithic LLM Responses into Manipulable Semantic Units","url":"https://arxiv.org/html/2509.08203v1"}]

I found the paper you're looking for. Here's what I found about IterGen:

## Overview

IterGen was presented as a 2025 poster at ICLR by Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, and Sasa Misailovic.

## Purpose and Problem

Large Language Models are widely used for natural language and code generation, but their outputs often suffer from hallucination, toxicity, and incorrect results. Current libraries for structured LLM generation rely on left-to-right decoding without support for backtracking, limiting the ability to correct or refine outputs mid-generation.

## Solution


…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-26T10:32:10.034781+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Combining Constrained and Unconstrained Decoding via Boosting\" Sakota West BoostCD EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Combining Constrained and Unconstrained Decoding via Boosting\" Sakota West BoostCD EMNLP 2025"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-26T10:32:10.034918+00:00_

Web search results for query: ""Combining Constrained and Unconstrained Decoding via Boosting" Sakota West BoostCD EMNLP 2025"

Links: [{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting:","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Constrained Decoding in Sequence Generation","url":"https://www.emergentmind.com/topics/constrained-decoding"}]

I found the paper you're looking for! Here's what I found:

"Combining Constrained and Unconstrained Decoding via Boosting" (BoostCD) is a method that combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice, in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

The key insight is that the mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

The paper demonstrates the power of BoostCD by applying it to closed information extraction. Their model, BoostIE, outperforms prior approaches both in and out of distribution, addressing sever
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:32:10.035060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\" Luan EMNLP 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\" Luan EMNLP 2018"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-26T10:32:10.035211+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify BibTeX entries 51-60",
  "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**51. wang2023instructuie**\n```\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{wang2023instructuie}; appendix_related_work.tex.\n\n---\n\n**52. zhou2024universalner**\n```\n@inproceedings{zhou2024universalner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {The Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://openreview.net/forum?id=r65xfUb76p}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{zhou2024universalner}.\n\n---\n\n**53. wadhwa2023revisiting**\n```\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {15566--15589},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {https://aclanthology.org/2023.acl-long.868}\n}\n```\nCitation context: section6_related_work.tex L13 \"violations persist\" → \\cite{wadhwa2023revisiting}; section3_violation_landscape.tex L13 \"R-F1 range consistent with recent evaluations\" → \\cite{wadhwa2023revisiting}.\n\n---\n\n**54. paolini2021tanl**\n```\n@inproceedings{paolini2021tanl,\n  title = {Structured Prediction as Translation between Augmented Natural Languages},\n  author = {Paolini, Giovanni and Athiwaratkun, Ben and Krone, Jason and Ma, Jie and Achille, Alessandro and Anubhai, Rishita and Nogueira dos Santos, C{\\'\\i}cero and Xiang, Bing and Soatto, Stefano},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=US-TP-xnXI}\n}\n```\nCitation context: section6_related_work.tex L13 → \\cite{paolini2021tanl}; appendix_related_work.tex.\n\n---\n\n**55. fei2022lasuie**\n```\n@inproceedings{fei2022lasuie,\n  title = {{LasUIE}: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model},\n  author = {Fei, Hao and Wu, Shengqiong and Li, Jingye and Li, Bobo and Li, Fei and Qin, Libo and Zhang, Meishan and Zhang, Min and Chua, Tat-Seng},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {35},\n  year = {2022},\n  url = {https://arxiv.org/abs/2304.06248}\n}\n```\nCitation context: section6_related_work.tex L13 → \\cite{fei2022lasuie}; appendix_related_work.tex.\n\n---\n\n**56. riedel2010modeling**\n```\n@inproceedings{riedel2010modeling,\n  title = {Modeling Relations and Their Mentions without Labeled Text},\n  author = {Riedel, Sebastian and Yao, Limin and McCallum, Andrew},\n  booktitle = {Joint European Conference on Machine Learning and Knowledge Discovery in Databases},\n  pages = {148--163},\n  year = {2010},\n  publisher = {Springer}\n}\n```\nCitation context: section6_related_work.tex L17 \"ILP constraints\" → \\citet{riedel2010modeling}; appendix_related_work.tex.\n\n---\n\n**57. anderson2017guided**\n```\n@inproceedings{anderson2017guided,\n  title = {Guided Open Vocabulary Image Captioning with Constrained Beam Search},\n  author = {Anderson, Peter and Fernando, Basura and Johnson, Mark and Gould, Stephen},\n  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},\n  pages = {936--945},\n  year = {2017},\n  publisher = {Association for Computational Linguistics}\n}\n```\nCitation context: section5_runtime.tex L12 \"beam search\" → \\cite{anderson2017guided}.\n\n---\n\n**58. lu2021text2event**\n```\n@inproceedings{lu2021text2event,\n  title = {{Text2Event}: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction},\n  author = {Lu, Yaojie and Lin, Hongyu and Xu, Jin and Han, Xianpei and Tang, Jialong and Li, Annan and Sun, Le and Liao, Meng and Chen, Shaobo},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {2722--2735},\n  year = {2021},\n  publisher = {Association for Computational Linguistics}\n}\n```\nCitation context: appendix_wikievents_pilot.tex L6 \"WikiEvents\" → \\cite{lu2021text2event}.\n\n---\n\n**59. luo2025kgtrie**\n```\n@inproceedings{luo2025kgtrie,\n  title = {Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation for Knowledge-to-Text Generation},\n  author = {Luo, Linhao and Zhao, Zicheng and Haffari, Gholamreza and Li, Yuan-Fang and Gong, Chen and Pan, Shirui},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.13080}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\cite{luo2025kgtrie}.\nNOTE: The cite key says \"kgtrie\" but the title says \"Graph-Constrained Reasoning\" — check if this is the correct paper and whether the cite key is misleading. Also check if the venue is correct (ICML 2025).\n\n---\n\n**60. vukovic2024dialogue**\n```\n@inproceedings{vukovic2024dialogue,\n  title = {Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding},\n  author = {Vukovic, Renato and Arps, David and van Niekerk, Carel and Ruppik, Benjamin Matthias and Lin, Hsien-chin and Heck, Michael and Ga\\v{s}i\\'{c}, Milica},\n  booktitle = {Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue},\n  pages = {370--384},\n  year = {2024},\n  address = {Kyoto, Japan},\n  url = {https://arxiv.org/abs/2408.02361}\n}\n```\nCitation context: section6_related_work.tex L18 \"dialogue RE\" → \\citet{vukovic2024dialogue}; appendix_related_work.tex.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify BibTeX entries 51-60",
    "prompt": "You are verifying 10 BibTeX entries for correctness. For each entry, use WebSearch to verify: (1) paper exists, (2) author names, (3) year, (4) title, (5) venue, (6) DOI/arXiv ID. Search for the paper title in quotes + author surname.\n\nHere are the 10 entries:\n\n---\n\n**51. wang2023instructuie**\n```\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{wang2023instructuie}; appendix_related_work.tex.\n\n---\n\n**52. zhou2024universalner**\n```\n@inproceedings{zhou2024universalner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {The Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://openreview.net/forum?id=r65xfUb76p}\n}\n```\nCitation context: section6_related_work.tex L13 \"training-time internalization\" → \\cite{zhou2024universalner}.\n\n---\n\n**53. wadhwa2023revisiting**\n```\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {15566--15589},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {https://aclanthology.org/2023.acl-long.868}\n}\n```\nCitation context: section6_related_work.tex L13 \"violations persist\" → \\cite{wadhwa2023revisiting}; section3_violation_landscape.tex L13 \"R-F1 range consistent with recent evaluations\" → \\cite{wadhwa2023revisiting}.\n\n---\n\n**54. paolini2021tanl**\n```\n@inproceedings{paolini2021tanl,\n  title = {Structured Prediction as Translation between Augmented Natural Languages},\n  author = {Paolini, Giovanni and Athiwaratkun, Ben and Krone, Jason and Ma, Jie and Achille, Alessandro and Anubhai, Rishita and Nogueira dos Santos, C{\\'\\i}cero and Xiang, Bing and Soatto, Stefano},\n  booktitle = {International Conference on Learning Representations},\n  year = {2021},\n  url = {https://openreview.net/forum?id=US-TP-xnXI}\n}\n```\nCitation context: section6_related_work.tex L13 → \\cite{paolini2021tanl}; appendix_related_work.tex.\n\n---\n\n**55. fei2022lasuie**\n```\n@inproceedings{fei2022lasuie,\n  title = {{LasUIE}: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model},\n  author = {Fei, Hao and Wu, Shengqiong and Li, Jingye and Li, Bobo and Li, Fei and Qin, Libo and Zhang, Meishan and Zhang, Min and Chua, Tat-Seng},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {35},\n  year = {2022},\n  url = {https://arxiv.org/abs/2304.06248}\n}\n```\nCitation context: section6_related_work.tex L13 → \\cite{fei2022lasuie}; appendix_related_work.tex.\n\n---\n\n**56. riedel2010modeling**\n```\n@inproceedings{riedel2010modeling,\n  title = {Modeling Relations and Their Mentions without Labeled Text},\n  author = {Riedel, Sebastian and Yao, Limin and McCallum, Andrew},\n  booktitle = {Joint European Conference on Machine Learning and Knowledge Discovery in Databases},\n  pages = {148--163},\n  year = {2010},\n  publisher = {Springer}\n}\n```\nCitation context: section6_related_work.tex L17 \"ILP constraints\" → \\citet{riedel2010modeling}; appendix_related_work.tex.\n\n---\n\n**57. anderson2017guided**\n```\n@inproceedings{anderson2017guided,\n  title = {Guided Open Vocabulary Image Captioning with Constrained Beam Search},\n  author = {Anderson, Peter and Fernando, Basura and Johnson, Mark and Gould, Stephen},\n  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},\n  pages = {936--945},\n  year = {2017},\n  publisher = {Association for Computational Linguistics}\n}\n```\nCitation context: section5_runtime.tex L12 \"beam search\" → \\cite{anderson2017guided}.\n\n---\n\n**58. lu2021text2event**\n```\n@inproceedings{lu2021text2event,\n  title = {{Text2Event}: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction},\n  author = {Lu, Yaojie and Lin, Hongyu and Xu, Jin and Han, Xianpei and Tang, Jialong and Li, Annan and Sun, Le and Liao, Meng and Chen, Shaobo},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {2722--2735},\n  year = {2021},\n  publisher = {Association for Computational Linguistics}\n}\n```\nCitation context: appendix_wikievents_pilot.tex L6 \"WikiEvents\" → \\cite{lu2021text2event}.\n\n---\n\n**59. luo2025kgtrie**\n```\n@inproceedings{luo2025kgtrie,\n  title = {Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation for Knowledge-to-Text Generation},\n  author = {Luo, Linhao and Zhao, Zicheng and Haffari, Gholamreza and Li, Yuan-Fang and Gong, Chen and Pan, Shirui},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.13080}\n}\n```\nCitation context: section6_related_work.tex L9 \"type systems\" → \\cite{luo2025kgtrie}.\nNOTE: The cite key says \"kgtrie\" but the title says \"Graph-Constrained Reasoning\" — check if this is the correct paper and whether the cite key is misleading. Also check if the venue is correct (ICML 2025).\n\n---\n\n**60. vukovic2024dialogue**\n```\n@inproceedings{vukovic2024dialogue,\n  title = {Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding},\n  author = {Vukovic, Renato and Arps, David and van Niekerk, Carel and Ruppik, Benjamin Matthias and Lin, Hsien-chin and Heck, Michael and Ga\\v{s}i\\'{c}, Milica},\n  booktitle = {Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue},\n  pages = {370--384},\n  year = {2024},\n  address = {Kyoto, Japan},\n  url = {https://arxiv.org/abs/2408.02361}\n}\n```\nCitation context: section6_related_work.tex L18 \"dialogue RE\" → \\citet{vukovic2024dialogue}; appendix_related_work.tex.\n\n---\n\nFor each entry, output in this format:\n```\n[cite_key] ✓ or ✗\n  - 存在性: ✓/✗\n  - 作者: ✓/✗ (note if issue)\n  - 年份: ✓/✗\n  - 标题: ✓/✗\n  - Venue: ✓/✗ (note if issue)\n  - DOI/arXiv: ✓/✗\n  - 正文引用: ✓/✗ (note if issue)\n  - 备注: (any notes)\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:32:10.035477+00:00_

Web search results for query: ""Unified Structure Generation for Universal Information Extraction" Lu Liu Dai ACL 2022"

Links: [{"title":"Unified Structure Generation for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.395/"},{"title":"[2203.12277] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277"},{"title":"[PDF] Unified Structure Generation for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-Structure-Generation-for-Universal-Lu-Liu/5eb9dad01d9b61947d7a9aae6dfff400d20555b9"},{"title":"Unified Structure Generation for Universal Information Extraction | universal-ie.github.io","url":"https://universal-ie.github.io/"},{"title":"Unified Structure Generation for Universal Information ...","url":"https://aclanthology.org/2022.acl-long.395.pdf"},{"title":"GitHub - universal-ie/UIE: Unified Structure Generation for Universal Information Extraction","url":"https://github.com/universal-ie/UIE"},{"title":"[2203.12277v1] Unified Structure Generation for Universal Information Extraction","url":"https://arxiv.org/abs/2203.12277v1"},{"title":"Uniﬁed Structure Generation for Universal Information Extraction","url":"https://arxiv.org/pdf/2203.12277"},{"title":"Paper page - Unified Structure Generation for Universal Information Extraction","url":"https://huggingface.co/papers/2203.12277"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Unified+structure+generation+for+universal+information+extraction&amp=&author=Yaojie+Lu&amp=&author=Qing+Liu&amp=&author=Dai+Dai&amp=&author=Xinyan+Xiao&amp=&author=Hongyu+Lin&amp=&author=Xianpei+Han&amp=&author=Le+Sun&amp=&author=Hua+Wu&amp=&publication_year=2022&amp=&pages=5755-5772&amp=&doi=10.18653/v1/2022.acl-long.395"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Unified Structure Generation for Universal Inform
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-26T10:32:10.035639+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:32:10.035784+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:32:10.035905+00:00_

Web search results for query: "openreview.net SynCode "HiUZtgAPoH" TMLR publication date"

Links: [{"title":"Revision History for SynCode: LLM Generation with ...","url":"https://openreview.net/revisions?id=HiUZtgAPoH"},{"title":"TMLR | OpenReview","url":"https://openreview.net/group?id=TMLR"},{"title":"SynCode: LLM Generation with Grammar Augmentation | OpenReview","url":"https://openreview.net/forum?id=HiUZtgAPoH"},{"title":"TMLR Submission Instructions","url":"https://jmlr.org/tmlr/submissions.html"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"Edit TMLR Group | OpenReview","url":"https://openreview.net/group/edit?id=TMLR"},{"title":"TMLR Expert Reviewers | OpenReview","url":"https://openreview.net/group?id=TMLR/Expert_Reviewers"},{"title":"Submissions | OpenReview","url":"https://openreview.net/submissions?page=21&venue=TMLR"},{"title":"Openreview","url":"https://openreview.net/pdf?id=HiUZtgAPoH"},{"title":"TMLR Submissions | OpenReview","url":"https://openreview.net/submissions?page=111&venue=TMLR"}]

Based on the search results, I found the SynCode paper on OpenReview. SynCode is a framework for LLM generation with grammar augmentation that integrates with languages defined by context-free grammars (CFG), eliminating syntax errors in JSON, Python, Go, and other code generation tasks.

Regarding the publication date, the search result metadata indicates the page was last updated or accessed on November 26, 2024. However, the search results do not contain a specific TMLR publication date for this paper. To find the exact publication date, you would need to visit the OpenReview forum page directly at https://openreview.net/forum?id=HiUZtgAPoH, where that information would be displayed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-26T10:32:10.036082+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\" Sainz García-Ferrero Agerri ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\" Sainz García-Ferrero Agerri ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-26T10:32:10.036258+00:00_

Web search results for query: ""Efficient Guided Generation for Large Language Models" Willard Louf arXiv 2307.09702"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"Efficient Guided Generation for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"}]

I found the paper you're looking for! Here are the key details:

**Title:** Efficient Guided Generation for Large Language Models

**Authors:** Brandon T. Willard and Rémi Louf

**arXiv ID:** 2307.09702

**Publication Date:** July 19, 2023

**Main Contribution:** The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine.

**Key Features:**
- The framework leads to an efficient approach to guiding text generation with regular expressions and context-free gram
…[truncated 676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-26T10:32:10.036414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\" Wang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\" Wang"
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-26T10:32:10.036548+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.19057 RELATE authors \"Mathew Satusky\" OR \"Mathew Satursky\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.19057 RELATE authors \"Mathew Satusky\" OR \"Mathew Satursky\""
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-26T10:32:10.036701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCode TMLR \"Transactions on Machine Learning Research\" 2024 OR 2025 Ugare accepted published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCode TMLR \"Transactions on Machine Learning Research\" 2024 OR 2025 Ugare accepted published"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:32:10.036886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Anthology \"2021.findings-emnlp.204\" REBEL pages Cabot Navigli"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Anthology \"2021.findings-emnlp.204\" REBEL pages Cabot Navigli"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T10:32:10.037039+00:00_

Web search results for query: ""InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction" Wang"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"}]

Based on the search results, I found comprehensive information about this paper:

## InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction

InstructUIE is a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency.

**Key Features:**

The research introduces IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.

**Performan
…[truncated 832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:32:10.037192+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\" Zhou"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\" Zhou"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-26T10:32:10.037336+00:00_

Web search results for query: "SynCode TMLR "Transactions on Machine Learning Research" 2024 OR 2025 Ugare accepted published"

Links: [{"title":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2024","url":"https://dblp.org/db/journals/tmlr/tmlr2024.html"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2025","url":"https://dblp.org/db/journals/tmlr/tmlr2025.html"},{"title":"Transactions on Machine Learning Research on X: \"📣 Heads-up 📣 that TMLR will pause new submissions over the upcoming holiday period from December 2 2024 to January 6 2025 (midnight AoE on both dates). We will resume accepting new submissions on January 7, 2025. Happy Holidays!\" / X","url":"https://x.com/TmlrOrg/status/1861409986196209930"},{"title":"Transactions on Machine Learning Research (@TmlrOrg) ...","url":"https://x.com/tmlrorg?lang=de"},{"title":"Transactions on Machine Learning Research - X","url":"https://x.com/TmlrOrg/status/1904952900620554745"},{"title":"Transactions on Machine Learning Research (TMLR)","url":"https://dblp.org/db/journals/tmlr/index.html"},{"title":"TMLR joins NeurIPS/ICML/ICLR Journal-to-Conference Track | by Transactions on Machine Learning Research | Medium","url":"https://medium.com/@TmlrOrg/tmlr-joins-neurips-icml-iclr-journal-to-conference-track-937a898eab3d"}]

Based on the search results, I found information about SynCode in TMLR:

SynCode is a novel framework for efficient and general syntactical decoding with LLMs, authored by Ugare, Shubham and others, and published in Transactions on Machine Learning Research in 2025. The framework ensures soundness and compl
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:32:10.037510+00:00_

Web search results for query: ""Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction" Luan EMNLP 2018"

Links: [{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/D18-1360/"},{"title":"[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"},{"title":"dblp: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction.","url":"https://dblp.org/rec/conf/emnlp/LuanHOH18.html"},{"title":"[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602"},{"title":"Multi-Task Identification of Entities, Relations, and Coreferencefor Scientific Knowledge Graph Construction","url":"https://nlp.cs.washington.edu/sciIE/"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ORKG","url":"https://orkg.org/paper/R36010"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://www.researchgate.net/publication/334115742_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - Consensus","url":"https://k8s.consensus.app/papers/details/ce11b64546755e678612cfea3b404121/"},{"title":"[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.or
…[truncated 1885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-26T10:32:10.037663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\" Yao ACL 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\" Yao ACL 2019"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-26T10:32:10.037822+00:00_

Web search results for query: ""GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction" Sainz García-Ferrero Agerri ICLR 2024"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO-SHOT ...","url":"https://openreview.net/notes/edits/attachment?id=x345y4wtJb&name=pdf"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"}]

I found the paper! Here are the search results for "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction":

## Overview

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

## Problem Statement

Large Language Models (LLMs) combined with instruction tuning have made significant progress when generalizing to unseen tasks, but they have been less successful in Information Extraction (IE), lagging behind task-specific models. Previous attempts to leverage annotation guidelines have failed, even with the largest models, as they are not able to follow the guidelines out-of-
…[truncated 715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-26T10:32:10.037981+00:00_

Web search results for query: "ACL Anthology "2021.findings-emnlp.204" REBEL pages Cabot Navigli"

Links: [{"title":"REBEL: Relation Extraction By End-to-end Language generation - ACL Anthology","url":"https://aclanthology.org/2021.findings-emnlp.204/"},{"title":"Aclanthology","url":"https://aclanthology.org/2021.findings-emnlp.204.bib"},{"title":"REBEL: Relation Extraction by End... preview & related info | Mendeley","url":"https://www.mendeley.com/catalogue/00c70289-0c2c-3a4e-9653-8d79650131b5/"},{"title":"GitHub - Babelscape/rebel: REBEL is a seq2seq model that simplifies Relation Extraction (EMNLP 2021). · GitHub","url":"https://github.com/Babelscape/rebel"},{"title":"EMNLP 2021","url":"https://aclanthology.org/2021.findings-emnlp.0.pdf"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2021 - ACL Anthology","url":"https://aclanthology.org/volumes/2021.findings-emnlp/"},{"title":"The 2021 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2021/"},{"title":"(PDF) REBEL: Relation Extraction By End-to-end Language generation","url":"https://www.researchgate.net/publication/357387727_REBEL_Relation_Extraction_By_End-to-end_Language_generation"},{"title":"Findings of the Association for Computational Linguistics (2021) - ACL Anthology","url":"https://aclanthology.org/events/findings-2021/"}]

Based on the search results, I found information about the paper you're looking for:

REBEL: Relation Extraction By End-to-end Language generation, by Pere-Lluís Huguet Cabot and Roberto Navigli, appears in the Findings of the Association for Computational Linguistics: EMNLP 2021, pages 2370–2381, Punta Cana, Dominican Republic.

The paper's ACL Anthology entry (2021.findings-emnlp.204) can be found at https://aclanthology.org/2021.findings-emnlp.204/

The paper proposes the use of autoregressive seq2seq models to extract relation triplets from raw text, which is described as cruc
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-26T10:32:10.038136+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\" Li Sun Tang ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\" Li Sun Tang ACL 2023"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:32:10.038272+00:00_

Web search results for query: ""UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition" Zhou"

Links: [{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"UniversalNER: targeted distillation from large language models for open named entity recognition","url":"https://arxiv.org/html/2308.03279v2"},{"title":"UniversalNER","url":"https://universal-ner.github.io/"},{"title":"GitHub - universal-ner/universal-ner · GitHub","url":"https://github.com/universal-ner/universal-ner"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/372961966_UniversalNER_Targeted_Distillation_from_Large_Language_Models_for_Open_Named_Entity_Recognition"},{"title":"[2308.03279v2] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279v2"},{"title":"[PDF] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/76b99439d524ae1813c30edc4bcad487a30a1f8c"},{"title":"universal-ner - Overview","url":"https://github.com/universal-ner"}]

I found the research paper on UniversalNER. Here's what the search results show:

## Overview

UniversalNER is about distilling large language models to demonstrate remarkable generalizability in understanding arbitrary entities and relations. The paper explores targeted distillation with mission-focused instruction tuning to train student models for open information extraction, using named entity recognition (NER) as a case study to show how ChatGPT can be distilled into much smaller UniversalNER models.

## Authors and Affiliation

The paper was authored by Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, an
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-26T10:32:10.038424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:experts.illinois.edu SynCode \"LLM Generation with Grammar Augmentation\" publication date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:experts.illinois.edu SynCode \"LLM Generation with Grammar Augmentation\" publication date"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-26T10:32:10.038552+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp SynCode Ugare TMLR 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp SynCode Ugare TMLR 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T10:32:10.038697+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Revisiting Relation Extraction in the era of Large Language Models\" Wadhwa Amir Wallace ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Revisiting Relation Extraction in the era of Large Language Models\" Wadhwa Amir Wallace ACL 2023"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T10:32:10.038834+00:00_

Web search results for query: "arXiv 2509.19057 RELATE authors "Mathew Satusky" OR "Mathew Satursky""

Links: [{"title":"[2509.19057] RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/abs/2509.19057"},{"title":"(PDF) RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://www.researchgate.net/publication/395771672_RELATE_Relation_Extraction_in_Biomedical_Abstracts_with_LLMs_and_Ontology_Constraints"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2509.19057"},{"title":"Time-series based quantum state discrimination","url":"https://arxiv.org/html/2601.19057"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=4&show=500"},{"title":"Partial Identification of the Average Treatment Effect with Stochastic Counterfactuals and Discordant Twins","url":"https://arxiv.org/html/2407.19057"},{"title":"for Functional Genomics","url":"https://arxiv.org/html/2405.19057"},{"title":"[2407.19057] Partial Identification of the Average Treatment Effect with Stochastic Counterfactuals and Discordant Twins","url":"https://arxiv.org/abs/2407.19057"},{"title":"Alvaro Velasquez","url":"https://sciprofiles.com/profile/author/bkMwQ01EczEybWcrMDZnU1BPM0x0Zz09"},{"title":"[2512.19057] Efficient Personalization of Generative Models via Optimal Experimental Design","url":"https://arxiv.org/abs/2512.19057"}]

Based on the search results, I found the arXiv paper 2509.19057 titled "RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints."

The authors of this paper are: Olawumi Olasunkanmi, Mathew Satusky, Hong Yi, Chris Bizon, Harlin Lee, and Stanley Ahalt.

Note: The arXiv official page (result 1) lists the author's name as "Mathew Satusky," while the ResearchGate page (result 2) shows "Mathew Sat
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-26T10:32:10.038998+00:00_

Web search results for query: ""DocRED: A Large-Scale Document-Level Relation Extraction Dataset" Yao ACL 2019"

Links: [{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"dblp: DocRED: A Large-Scale Document-Level Relation Extraction Dataset.","url":"https://dblp.org/rec/conf/acl/YaoYLHLLLHZS19.html"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"[1906.06127v3] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127v3"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"[Quick Review] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://liner.com/review/docred-largescale-documentlevel-relation-extraction-dataset"}]

I found comprehensive information about the DocRED paper. Here's what the search revealed:

## DocRED: A Large-Scale Document-Level Relation Extraction Dataset

The paper "DocRED: A Large-Scale Document-Level Relation Extraction Dataset" was authored by Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin,
…[truncated 1555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T10:32:10.039282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.19057 RELATE Olasunkanmi author list exact",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.19057 RELATE Olasunkanmi author list exact",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-26T10:32:10.039433+00:00_

Web search results for query: "site:experts.illinois.edu SynCode "LLM Generation with Grammar Augmentation" publication date"

Links: [{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"SynCode: LLM Generation with Grammar Augmentation","url":"https://arxiv.org/pdf/2403.01632"},{"title":"HyGenar: An LLM-Driven Hybrid Genetic Algorithm for Few-Shot Grammar Generation","url":"https://arxiv.org/pdf/2505.16978"},{"title":"IterGen: Iterative Semantic-aware Structured LLM Generation with   Backtracking","url":"https://arxiv.org/pdf/2410.07295"},{"title":"Grammar Prompting for Domain-Specific Language Generation with Large   Language Models","url":"https://arxiv.org/pdf/2305.19234"}]

Based on the search results, the SynCode: LLM Generation with Grammar Augmentation publication is in Transactions on Machine Learning Research, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T10:32:10.039577+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\" Wei arXiv 2302.10205"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT\" Wei arXiv 2302.10205"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T10:32:10.039739+00:00_

Web search results for query: "dblp SynCode Ugare TMLR 2024 2025"

Links: [{"title":"Accepted papers at TMLR on X: \"SynCode: LLM Generation with Grammar Augmentation Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa Misailovic, Gagandeep Singh. Action editor: Ying Wei. https://t.co/tS6qBH16mq #syntax #automaton #serialization\" / X","url":"https://x.com/TmlrPub/status/1951447922060435673"},{"title":"dblp: Shubham Ugare","url":"https://dblp.org/pid/227/3014.html"},{"title":"Shubham Ugare","url":"https://shubhamugare.github.io/"},{"title":"[PDF] SynCode: LLM Generation with Grammar Augmentation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCode:-LLM-Generation-with-Grammar-Augmentation-Ugare-Suresh/46a41357eadac1459c81588136c5c053abfeefe4"},{"title":"GitHub - structuredllm/syncode: Efficient and general syntactical decoding for Large Language Models · GitHub","url":"https://github.com/structuredllm/syncode"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"Transactions on Machine Learning Research (TMLR)","url":"https://dblp.org/db/journals/tmlr/index.html"},{"title":"[2403.01632] SynCode: LLM Generation with Grammar Augmentation","url":"https://arxiv.org/abs/2403.01632"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2024","url":"https://dblp.org/db/journals/tmlr/tmlr2024.html"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2025","url":"https://dblp.org/db/journals/tmlr/tmlr2025.html"}]

Based on the search results, here's what I found:

**SynCode: LLM Generation with Grammar Augmentation** is a paper by Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa Misailovic, and Gagandeep Singh published in Transactions on Machine Learning Research (TMLR) in 2025.

SynCode is a novel framework for efficient and general syntactical decoding with LLMs that ensures soundness and com
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-26T10:32:10.039914+00:00_

Web search results for query: ""Revisiting Relation Extraction in the era of Large Language Models" Wadhwa Amir Wallace ACL 2023"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"[2305.05003] Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/abs/2305.05003"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/html/2305.05003v2"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/372915829_Revisiting_Relation_Extraction_in_the_era_of_Large_Language_Models"},{"title":"dblp: Revisiting Relation Extraction in the era of Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2305-05003.html"}]

I found the paper! Here are the results for your search:

"Revisiting Relation Extraction in the era of Large Language Models" was authored by Somin Wadhwa, Silvio Amir, and Byron Wallace and published at ACL 2
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:32:10.040078+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Structured Prediction as Translation between Augmented Natural Languages\" Paolini ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Structured Prediction as Translation between Augmented Natural Languages\" Paolini ICLR 2021"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T10:32:10.040207+00:00_

Web search results for query: "arxiv 2509.19057 RELATE Olasunkanmi author list exact"

Links: [{"title":"[2509.19057] RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/abs/2509.19057"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=0&show=500"},{"title":"[2504.19057] A correspondence between the Rabi model and an Ising model with long-range interactions","url":"https://arxiv.org/abs/2504.19057"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=25&show=2000"},{"title":"ReLATE: Learning Efficient Sparse Encoding for High-Performance Tensor Decomposition","url":"https://arxiv.org/html/2509.00280v1"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"arXiv:2505.15948v1 [cs.CL] 21 May 2025","url":"https://arxiv.org/pdf/2505.15948"},{"title":"[2509.20604] Numerically exact quantum dynamics with tensor networks: Predicting the decoherence of interacting spin systems","url":"https://arxiv.org/abs/2509.20604"},{"title":"Bridging the Gap Between Ideal and Real-world Evaluation: Benchmarking AI-Generated Image Detection in Challenging Scenarios","url":"https://arxiv.org/html/2509.09172v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1237&show=1000"}]

Based on the search results, the authors of arXiv paper 2509.19057 "RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints" are: Olawumi Olasunkanmi, Mathew Satusky, Hong Yi, Chris Bizon, Harlin Lee, and Stanley Ahalt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T10:32:10.040361+00:00_

Web search results for query: ""CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors" Li Sun Tang ACL 2023"

Links: [{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"CODEIE: Large Code Generation Models are Better Few- ...","url":"https://aclanthology.org/2023.acl-long.855.pdf"},{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"[Quick Review] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://liner.com/review/codeie-large-code-generation-models-are-better-fewshot-information-extractors"},{"title":"CodeIE","url":"https://artpli.github.io/CodeIE/"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"Main Conference - ACL 2023","url":"https://2023.aclweb.org/program/accepted_main_conference/"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors

**Authors:** Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu

**Publication:** Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15339–15353, Toronto, Canada (ACL 2023)

**Main Contribution:** The paper proposes to recast the structured output in the form of code instead of natural l
…[truncated 589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T10:32:10.040511+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/section6_related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/section6_related_work.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T10:32:10.040627+00:00_

artifacts/_project/paper/section6_related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-26T10:32:10.040770+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-26T10:32:10.040929+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/appendix_related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/appendix_related_work.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-26T10:32:10.041053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-26T10:32:10.041163+00:00_

artifacts/_project/paper/appendix_related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T10:32:10.041289+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/section4_composition_draft.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/section4_composition_draft.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T10:32:10.041402+00:00_

artifacts/_project/paper/section4_composition_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-26T10:32:10.041523+00:00_

Web search results for query: ""ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT" Wei arXiv 2302.10205"

Links: [{"title":"[2302.10205] ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/abs/2302.10205"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/pdf/2302.10205"},{"title":"[PDF] Zero-Shot Information Extraction via Chatting with ChatGPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Zero-Shot-Information-Extraction-via-Chatting-with-Wei-Cui/f4cba0db34aa0c389cec267ca1f3ba5255ea2645"},{"title":"GitHub - cocacola-lab/ChatIE: The online version is temporarily unavailable because we cannot afford the key. You can clone and run it locally. Note: we set defaul openai key. If keys exceed plan and are invalid, please tell us. The response speed depends on openai. ( sometimes, the official is too crowded and slow)","url":"https://github.com/cocacola-lab/ChatIE"},{"title":"[2302.10205] Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://ar5iv.labs.arxiv.org/html/2302.10205"},{"title":"[2302.10205v1] Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/abs/2302.10205v1"},{"title":"ChatIE: Zero-Shot Information Extraction | PDF | Linguistics | Human Communication","url":"https://www.scribd.com/document/718695080/2302-10205"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230210205W/abstract"}]

I found the paper you're looking for. Here's what the search revealed:

ChatIE transforms the zero-shot IE task into a multi-turn question-answering problem with a two-stage framework. The framework was evaluated on three IE tasks: entity-relation triple extract, named entity recognition, and event extraction.

Empirical results on six datasets across two languages show that ChatIE achieves impressive performance 
…[truncated 609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-26T10:32:10.041686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LMQL PLDI 2023 \"Proceedings of the ACM on Programming Languages\" OR \"SIGPLAN\" Beurer-Kellner venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LMQL PLDI 2023 \"Proceedings of the ACM on Programming Languages\" OR \"SIGPLAN\" Beurer-Kellner venue"
  }
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-26T10:32:10.041822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:32:10.041947+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.19057",
  "prompt": "List the exact author names of this paper, preserving exact spelling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.19057",
    "prompt": "List the exact author names of this paper, preserving exact spelling"
  }
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-26T10:32:10.042074+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen3 Technical Report\" Qwen Team arXiv 2505.09388"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen3 Technical Report\" Qwen Team arXiv 2505.09388"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-26T10:32:10.042207+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	Grammar-constrained decoding restricts each token to a mask derived from a target grammar.
8	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SGLang~\cite{zheng2024sglang}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} compile JSON Schemas into pushdown automata for structural enforcement, but are limited to context-free constraints and cannot enforce cross-field semantic rules that depend on previously generated field values.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; KG-Trie~\cite{luo2025kgtrie} applies trie-based KG constraints for knowledge-to-text generation.
10	OntoCoDec fills this gap with a stateful semantic layer whose entity registry is populated dynamically during generation.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, and others~\cite{guidex2025,josifoski2022genie,paolini2021tanl,cabot2021rebel,wang2023instructuie,qi2024adelie,fei2022lasuie,lu2022uie,zhou2024universalner} encode ontology structure via training-time internalization, learning schema preferences but without runtime guarantees: violations persist at 0.5--2\% even after fine-tuning~\cite{wadhwa2023revisiting}.
14	OntoCoDec provides orthogonal runtime enforcement composable with these systems, including GoLLIE itself (Appendix~\ref{app:gollie-comparison}).
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via integer linear programming (ILP); post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation but discards up to 74\%
…[truncated 586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-26T10:32:10.042351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T10:32:10.042515+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 20065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-26T10:32:10.042665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-26T10:32:10.042831+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	% ──────────────────────────────────────────
4	%  Figure: Composition Interaction
5	% ──────────────────────────────────────────
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig_composition_interaction.pdf}
9	\caption{Non-additive layer interaction on SciERC (Qwen3-8B, zero-shot). Grammar-only and semantic-only achieve 3\% and 24\% DR reduction; their composition yields 94\%, 3.5$\times$ the additive prediction.}
10	\label{fig:composition-interaction}
11	\end{figure}
12	
13	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
14	The final mask is their conjunction:
15	%
16	\begin{equation}\label{eq:composition}
17	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
18	\end{equation}
19	%
20	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
21	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
22	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
23	
24	\paragraph{Grammar-First Fallback.}
25	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
26	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
27	Structural integrity is a hard constraint; type violations are soft errors dete
…[truncated 2729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-26T10:32:10.042969+00:00_

# Authors of RELATE Paper

Based on the document, the exact author names are:

1. Olawumi Olasunkanmi
2. Mathew Satusky
3. Hong Yi
4. Chris Bizon
5. Harlin Lee
6. Stanley Ahalt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-26T10:32:10.043094+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03439",
  "prompt": "List the exact author names of this paper, preserving exact spelling. Also note the submission date/year."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.03439",
    "prompt": "List the exact author names of this paper, preserving exact spelling. Also note the submission date/year."
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-26T10:32:10.043234+00:00_

Web search results for query: ""Structured Prediction as Translation between Augmented Natural Languages" Paolini ICLR 2021"

Links: [{"title":"[2101.05779] Structured Prediction as Translation between Augmented Natural Languages","url":"https://arxiv.org/abs/2101.05779"},{"title":"(PDF) Structured Prediction as Translation between Augmented Natural Languages","url":"https://www.researchgate.net/publication/348487215_Structured_Prediction_as_Translation_between_Augmented_Natural_Languages"},{"title":"Structured Prediction as Translation between Augmented Natural Languages","url":"https://papertalk.org/papertalks/29196"},{"title":"ICLR 2021 Structured Prediction as Translation between Augmented Natural Languages Spotlight","url":"https://iclr.cc/virtual/2021/spotlight/3411"},{"title":"[PDF] Structured Prediction as Translation between Augmented Natural Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Structured-Prediction-as-Translation-between-Paolini-Athiwaratkun/1cb3f6d545b68db3e7fc6055dcf44099c3ac4672"},{"title":"Structured Prediction as Translation between Augmented Natural Languages. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1097610122eed846abd2cbc09bd0bd96a"},{"title":"Structured prediction as translation between augmented natural languages - Amazon Science","url":"https://www.amazon.science/publications/structured-prediction-as-translation-between-augmented-natural-languages"},{"title":"Structured Prediction as Translation between Augmented Natural Languages | OpenReview","url":"https://openreview.net/forum?id=US-TP-xnXI"},{"title":"GitHub - amazon-science/tanl: Structured Prediction as Translation between Augmented Natural Languages · GitHub","url":"https://github.com/amazon-science/tanl"}]

I found the paper! Here are the key details:

**Paper:** "Structured Prediction as Translation between Augmented Natural Languages" by Giovanni Paolini, Ben Athiwaratkun, Jason Krone, Jie Ma, Alessandro Achille, Rishita Anubhai, Cicer
…[truncated 1350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-26T10:32:10.043383+00:00_

Web search results for query: ""Qwen3 Technical Report" Qwen Team arXiv 2505.09388"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"},{"title":"Qwen3 Technical Report | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.09388v1"},{"title":"Qwen3 Technical Report (arXiv:2505.09388v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2505.09388v1"}]

I found the Qwen3 Technical Report (arXiv:2505.09388) by the Qwen Team. Here's a summary of the key findings:

## Overview
Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities.

## Model Architecture
The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

## Key Innovations
A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, which eliminates the need to switch between different models and enables dynamic mode switching based on user queries or chat templates.

Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, ther
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-26T10:32:10.043522+00:00_

# Paper Authors and Submission Date

**Authors (exact spelling):**
1. Xiaochi Zhou
2. Patrick Bulter
3. Changxuan Yang
4. Simon D. Rihm
5. Thitikarn Angkanaporn
6. Jethro Akroyd
7. Sebastian Mosbach
8. Markus Kraft

**Submission Date:** February 3, 2026

The paper was "Submitted on 3 Feb 2026" with the arXiv identifier 2602.03439.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-26T10:32:10.043657+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SGLang: Efficient Execution of Structured Language Model Programs\" Zheng NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SGLang: Efficient Execution of Structured Language Model Programs\" Zheng NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-26T10:32:10.043808+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06066",
  "prompt": "List the exact author names and submission date of this paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.06066",
    "prompt": "List the exact author names and submission date of this paper"
  }
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-26T10:32:10.043935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model\" Fei NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model\" Fei NeurIPS 2022"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-26T10:32:10.044081+00:00_

Web search results for query: "LMQL PLDI 2023 "Proceedings of the ACM on Programming Languages" OR "SIGPLAN" Beurer-Kellner venue"

Links: [{"title":"Research | LMQL","url":"https://lmql.ai/research/index.html"},{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/10.1145/3591300"},{"title":"A new form of human-computer interaction | ETH Zurich","url":"https://ethz.ch/en/news-and-events/eth-news/news/2023/04/a-new-form-of-human-computer-interaction.html"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"Prompting Is Programming: A Query Language for Large Language Models (PLDI 2023 - PLDI Research Papers) - PLDI 2023","url":"https://pldi23.sigplan.org/details/pldi-2023-pldi/81/Prompting-Is-Programming-A-Query-Language-for-Large-Language-Models"},{"title":"GitHub - lmql-lang/lmql: A query language for programming (large) language models. · GitHub","url":"https://github.com/lmql-lang/lmql"},{"title":"Better Steering LLM Agents with LMQL | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/better-steering-LLM-agents-with-LMQL.html"},{"title":"Luca Beurer-Kellner - PLDI 2023","url":"https://pldi23.sigplan.org/profile/lucabeurerkellner"},{"title":"A new form of human-computer interaction - Technology Org","url":"https://www.technology.org/2023/05/04/new-form-of-human-computer-interaction/"}]

Based on the search results, I found the information about the LMQL paper:

LMQL was presented at the 44th ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI 2023) in Orlando, Florida by Luca Beurer-Kellner, Marc Fischer, and Martin Vechev.

The paper titled "Prompting Is Programming: A Query Language for Large Lan
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T10:32:10.044227+00:00_

# Paper Details

**Author Name:** Hongxu Zhou

**Submission Date:** Tue, 7 Apr 2026 16:47:37 UTC

The paper is titled "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection" and was submitted to arXiv under identifier 2604.06066 in the Computation and Language category.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-26T10:32:10.044360+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GENRE \"Autoregressive Entity Retrieval\" De Cao author list order ICLR 2021 dblp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GENRE \"Autoregressive Entity Retrieval\" De Cao author list order ICLR 2021 dblp"
  }
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-26T10:32:10.044487+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.emnlp-main.779/",
  "prompt": "List the exact author names and full venue details for this PICARD paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.emnlp-main.779/",
    "prompt": "List the exact author names and full venue details for this PICARD paper"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-26T10:32:10.044624+00:00_

Web search results for query: ""SGLang: Efficient Execution of Structured Language Model Programs" Zheng NeurIPS 2024"

Links: [{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html"},{"title":"NeurIPS Poster SGLang: Efficient Execution of Structured Language Model Programs","url":"https://neurips.cc/virtual/2024/poster/94872"},{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"Sglang: Efficient execution of structured language model programs | Stanford MAST Lab","url":"https://mast.stanford.edu/pubs/sglang_efficient_execution_of_structured_language_model_programs/"},{"title":"SGLang: Efficient Execution of Structured Language Model ...","url":"http://theory.stanford.edu/~barrett/pubs/ZYX+24-abstract.html"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | OpenReview","url":"https://openreview.net/forum?id=VqkAKQibpq"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/html/2312.07104v2"},{"title":"SGLang: Efficient Execution of Structured Language Model Programs | Request PDF","url":"https://www.researchgate.net/publication/397203117_SGLang_Efficient_Execution_of_Structured_Language_Model_Programs"},{"title":"NeurIPS Poster SGLang: Efficient Execution of Structured Language Model Programs","url":"https://nips.cc/virtual/2024/poster/94872"},{"title":"[PDF] SGLang: Efficient Execution of Structured Language Model Programs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SGLang:-Efficient-Execution-of-Structured-Language-Zheng-Yin/eb95c327260725498404eb43ec370d419b8d92c7"}]

Based on the search results, here's what I found about "SGLang: Efficient Execution of Structured Language Model Programs":

## Overview

SGLang is a system for efficien
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-26T10:32:10.044798+00:00_

Web search results for query: "GENRE "Autoregressive Entity Retrieval" De Cao author list order ICLR 2021 dblp"

Links: [{"title":"ICLR Spotlight Autoregressive Entity Retrieval","url":"https://iclr.cc/virtual/2021/spotlight/3521"},{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://openreview.net/pdf?id=5k8F6UU39V"},{"title":"Autoregressive Entity Retrieval - Meta AI","url":"https://ai.meta.com/research/publications/autoregressive-entry-retrieval/"},{"title":"dblp: Autoregressive Entity Retrieval.","url":"https://dblp.org/rec/conf/iclr/CaoI0P21.html"},{"title":"Nicola De Cao –","url":"https://nicola-decao.github.io/Nicola_De_Cao_CV.pdf"},{"title":"dblp: Nicola De Cao","url":"https://dblp.org/pid/218/6626.html"},{"title":"Autoregressive Entity Retrieval - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10167460/"},{"title":"[2010.00904] Autoregressive Entity Retrieval","url":"https://arxiv.org/abs/2010.00904"},{"title":"(PDF) Autoregressive Entity Retrieval","url":"https://www.researchgate.net/publication/344468840_Autoregressive_Entity_Retrieval"}]

Based on the search results, here is the author list for the "Autoregressive Entity Retrieval" paper published at ICLR 2021:

The authors are: Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni.

This is also confirmed by the official ICLR 2021 publication, which lists the authors as Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-26T10:32:10.044988+00:00_

# PICARD Paper Details

**Authors:**
1. Torsten Scholak
2. Nathan Schucher
3. Dzmitry Bahdanau

**Venue Details:**
- Conference: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing"
- Month and Year: November 2021
- Location: Online and Punta Cana, Dominican Republic
- Publisher: Association for Computational Linguistics
- Pages: 9895–9901
- DOI: 10.18653/v1/2021.emnlp-main.779

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-26T10:32:10.045135+00:00_

Web search results for query: ""LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model" Fei NeurIPS 2022"

Links: [{"title":"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/63943ee9fe347f3d95892cf87d9a42e6-Abstract-Conference.html"},{"title":"Unifying Information Extraction with Latent Adaptive ...","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf"},{"title":"[2304.06248] LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model","url":"https://arxiv.org/abs/2304.06248"},{"title":"GitHub - ChocoWu/LasUIE: Universal Information Extraction, codes for the NeurIPS-2022 paper: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model. · GitHub","url":"https://github.com/ChocoWu/LasUIE"},{"title":"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model","url":"https://haofei.vip/LasUIE-page/"},{"title":"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model","url":"https://papers.nips.cc/paper_files/paper/2022/hash/63943ee9fe347f3d95892cf87d9a42e6-Abstract-Conference.html"},{"title":"LasUIE: Unifying Information Extraction with Latent ...","url":"https://openreview.net/pdf?id=a8qX5RG36jd"},{"title":"LasUIE: Unifying Information Extraction with Latent ...","url":"https://arxiv.org/pdf/2304.06248"},{"title":"LasUIE: Unifying Information Extraction with Latent Adaptive ...","url":"https://haofei.vip/LasUIE-page/static/media/poster_landscape_NIPS22_LasUIE.pdf"},{"title":"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model | OpenReview","url":"https://openreview.net/forum?id=a8qX5RG36jd"}]

I found the paper you're s
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-26T10:32:10.045294+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Document-Level Event Argument Extraction by Conditional Generation\" Li Ji Han NAACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Document-Level Event Argument Extraction by Conditional Generation\" Li Ji Han NAACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-26T10:32:10.045431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE ICLR 2024 authors \"Lopez de Lacalle\" \"German Rigau\" \"Eneko Agirre\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE ICLR 2024 authors \"Lopez de Lacalle\" \"German Rigau\" \"Eneko Agirre\" full author list"
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-26T10:32:10.045560+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ebooks.iospress.nl/volumearticle/55116",
  "prompt": "What are the exact page numbers for the SpERT paper by Eberts and Ulges? What is the DOI?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ebooks.iospress.nl/volumearticle/55116",
    "prompt": "What are the exact page numbers for the SpERT paper by Eberts and Ulges? What is the DOI?"
  }
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-26T10:32:10.045707+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Modeling Relations and Their Mentions without Labeled Text\" Riedel Yao McCallum ECML 2010"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Modeling Relations and Their Mentions without Labeled Text\" Riedel Yao McCallum ECML 2010"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-26T10:32:10.045833+00:00_

Based on the webpage content provided:

The SpERT paper by Markus Eberts and Adrian Ulges appears on **pages 2006-2013** and has the DOI **10.3233/FAIA200321**. The article is published in Volume 325 of the "Frontiers in Artificial Intelligence and Applications" series, specifically in the ECAI 2020 conference proceedings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T10:32:10.045968+00:00_

Web search results for query: ""Document-Level Event Argument Extraction by Conditional Generation" Li Ji Han NAACL 2021"

Links: [{"title":"Document-Level Event Argument Extraction by Conditional Generation - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.69/"},{"title":"[2104.05919] Document-Level Event Argument Extraction by Conditional Generation","url":"https://arxiv.org/abs/2104.05919"},{"title":"[PDF] Document-Level Event Argument Extraction by Conditional Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Document-Level-Event-Argument-Extraction-by-Li-Ji/2a15f541a8216782a7579f01f56762448e48b582"},{"title":"Document-Level Event Argument Extraction by Conditional Generation | Request PDF","url":"https://www.researchgate.net/publication/352365501_Document-Level_Event_Argument_Extraction_by_Conditional_Generation"},{"title":"Document-Level Event Argument Extraction by Conditional ...","url":"https://aclanthology.org/2021.naacl-main.69.pdf"},{"title":"Document-Level Event Argument Extraction by Conditional Generation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/document-level-event-argument-extraction-by-conditional-generatio"},{"title":"dblp: Document-Level Event Argument Extraction by Conditional Generation.","url":"https://dblp.org/rec/conf/naacl/LiJH21.html"},{"title":"EIGP: document-level event argument extraction with information enhancement generated based on prompts | Knowledge and Information Systems","url":"https://dl.acm.org/doi/10.1007/s10115-024-02213-4"}]

I found the paper! Here are the key details:

**Title:** Document-Level Event Argument Extraction by Conditional Generation

**Authors:** Sha Li, Heng Ji, and Jiawei Han

**Publication:** Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 894–908, Online

**Key Contributions:**
- Event extraction has long been treated as a sentence-l
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-26T10:32:10.046125+00:00_

Web search results for query: "GoLLIE ICLR 2024 authors "Lopez de Lacalle" "German Rigau" "Eneko Agirre" full author list"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"dblp: BibTeX records: Eneko Agirre","url":"https://dblp.org/pid/a/EnekoAgirre.html?view=bibtex&param=0"},{"title":"dblp: Oier Lopez de Lacalle","url":"https://dblp.org/pid/11/4461.html"},{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/gollie"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"dblp: Iker García-Ferrero","url":"https://dblp.org/pid/305/9880.html"}]

Based on the search results, here is the full author list for the GoLLIE paper published at ICLR 2024:

The authors are: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre from HiTZ Basque Center for Language Technology - Ixa NLP Group at the University of the Basque Country (UPV/EHU).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-26T10:32:10.046269+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.15100",
  "prompt": "List the exact author names. Also confirm: was this paper published at MLSys 2025? What year was it first submitted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.15100",
    "prompt": "List the exact author names. Also confirm: was this paper published at MLSys 2025? What year was it first submitted?"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-26T10:32:10.046389+00:00_

# Author Names and Publication Details

**Exact Author Names:**
1. Yixin Dong
2. Charlie F. Ruan
3. Yaxing Cai
4. Ruihang Lai
5. Ziyi Xu
6. Yilong Zhao
7. Tianqi Chen

**MLSys 2025 Publication:**
Yes, the paper indicates "MLSys '25" in the Comments section, confirming it was published at MLSys 2025.

**Initial Submission Year:**
The paper was first submitted in 2024, specifically on "Fri, 22 Nov 2024" according to the submission history.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-26T10:32:10.046519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\" De La Fuente Sainz ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\" De La Fuente Sainz ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-26T10:32:10.046647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DOMINO Beurer-Kellner ICML 2024 PMLR volume 235 pages 3658"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DOMINO Beurer-Kellner ICML 2024 PMLR volume 235 pages 3658"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-26T10:32:10.046798+00:00_

Web search results for query: ""Modeling Relations and Their Mentions without Labeled Text" Riedel Yao McCallum ECML 2010"

Links: [{"title":"[PDF] Modeling Relations and Their Mentions without Labeled Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-Relations-and-Their-Mentions-without-Text-Riedel-Yao/e7e7b9a731678bf0494fe29cbebb42a822224cc6"},{"title":"Modeling Relations and Their Mentions without Labeled Text | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-15939-8_10"},{"title":"(PDF) Modeling Relations and Their Mentions without Labeled Text","url":"https://www.researchgate.net/publication/220698997_Modeling_Relations_and_Their_Mentions_without_Labeled_Text"},{"title":"Modeling Relations and Their Mentions Without Labeled Text","url":"https://research.amanote.com/publication/0JSC2HMBKQvf0Bhi_EHb/modeling-relations-and-their-mentions-without-labeled-text"},{"title":"Modeling relations and their mentions without labeled text | BibSonomy","url":"https://www.bibsonomy.org/bibtex/202c0f5e7cab88d6ec38b6bb8e43e2a7f/jil"},{"title":"Modeling Relations and Their Mentions without Labeled Text | UCL NLP","url":"https://nlp.cs.ucl.ac.uk/publications/2010-07-11-modeling-relations-and-their-mentions-without-labeled-text/"},{"title":"Modeling relations and their mentions without labeled text | Proceedings of the 2010 European conference on Machine learning and knowledge discovery in databases: Part III","url":"https://dl.acm.org/doi/10.5555/1889788.1889799"},{"title":"2010 ModelingRelationsandtheirMentio - GM-RKB - Gabor Melli","url":"https://www.gabormelli.com/RKB/2010_ModelingRelationsandtheirMentio"}]

I found the paper! Here's the information about "Modeling Relations and Their Mentions without Labeled Text":

"Modeling Relations and Their Mentions without Labeled Text" is a 2010 paper by Sebastian Riedel, Limin Yao, and Andrew McCallum published in the Proceedings of the European Conference on Machine Learnin
…[truncated 727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-26T10:32:10.046953+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.emnlp-main.17/",
  "prompt": "List the exact author names, pages, and DOI for this PFN paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.emnlp-main.17/",
    "prompt": "List the exact author names, pages, and DOI for this PFN paper"
  }
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-26T10:32:10.047083+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Guided Open Vocabulary Image Captioning with Constrained Beam Search\" Anderson Fernando Johnson Gould EMNLP 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Guided Open Vocabulary Image Captioning with Constrained Beam Search\" Anderson Fernando Johnson Gould EMNLP 2017"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-26T10:32:10.047213+00:00_

Web search results for query: ""GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction" De La Fuente Sainz ACL 2025"

Links: [{"title":"[2506.00649] GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/abs/2506.00649"},{"title":"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1245/"},{"title":"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/html/2506.00649"},{"title":"GUIDEX – ACL Findings 2025","url":"https://neilus03.github.io/guidex.com/"},{"title":"GitHub - Neilus03/GUIDEX: GUIDEX official repo","url":"https://github.com/Neilus03/GUIDEX"},{"title":"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://openreview.net/pdf?id=OBJSRNVYS5"}]

I found comprehensive information about GUIDEX. Here's a summary of the paper:

## GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction

GUIDEX is a novel method authored by Neil De La Fuente, Oscar Sainz, Iker García-Ferrero, and Eneko Agirre that automatically defines domain-specific schemas, infers guidelines, and generates synthetically labeled instances, allowing for better out-of-domain generalization.

**Problem Addressed:**
Information Extraction systems are traditionally domain-specific, requiring costly adaptation involving expert schema design, data annotation, and model training. While Large Language Models have shown promise in zero-shot IE, performance degrades significantly in unseen domains where label definitions differ.

**Key Results:**
Fine-tuning Llama 3.1 with GUIDEX sets a new state-of-the-art across seven zero-shot Named Entity Recognition benchmarks, with models trained with GUIDEX gaining up to 7 F1 points over previous methods without human-labeled data, and nearly 2 F1 points higher when combined with it.

**Public
…[truncated 367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-26T10:32:10.047369+00:00_

Web search results for query: "DOMINO Beurer-Kellner ICML 2024 PMLR volume 235 pages 3658"

Links: [{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://proceedings.mlr.press/v235/beurer-kellner24a.html"},{"title":"GitHub - mlresearch/v235: Proceedings of ICML 2024 · GitHub","url":"https://github.com/mlresearch/v235"},{"title":"Proceedings of Machine Learning Research | Proceedings of the 41st International Conference on Machine Learning Held in Vienna, Austria on 21-27 July 2024 Published as Volume 235 by the Proceedings of Machine Learning Research on 08 July 2024. Volume Edited by: Ruslan Salakhutdinov Zico Kolter Katherine Heller Adrian Weller Nuria Oliver Jonathan Scarlett Felix Berkenkamp Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v235/"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://media.icml.cc/Conferences/ICML2024/Styles/example_paper.pdf"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation [Quick Review]","url":"https://liner.com/review/guiding-llms-right-way-fast-noninvasive-constrained-generation"},{"title":"dblp: ICML 2024","url":"https://dblp.org/db/conf/icml/icml2024.html"},{"title":"41st International Conference on Machine Learning, ICML 2024. Proceedings","url":"https://publica.fraunhofer.de/entities/mainwork/8e9a6cef-56a8-4a21-9aca-e0c79629bd1f"},{"title":"Position: Application-Driven Innovation in Machine Learning","url":"https://openreview.net/pdf?id=xEB2oF3vvb"},{"title":"[2403.06988] Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/abs/2403.06988"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and
…[truncated 1024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-26T10:32:10.047519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\" Geng Cooper arXiv 2501.10868"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models\" Geng Cooper arXiv 2501.10868"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-26T10:32:10.047641+00:00_

# PFN Paper Details

**Authors:**
Zhiheng Yan, Chong Zhang, Jinlan Fu, Qi Zhang, and Zhongyu Wei

**Pages:**
185–197

**DOI:**
10.18653/v1/2021.emnlp-main.17

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-26T10:32:10.047857+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dl.acm.org 10.1145/3591300 LMQL \"Proceedings of the ACM on Programming Languages\" PLDI venue journal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dl.acm.org 10.1145/3591300 LMQL \"Proceedings of the ACM on Programming Languages\" PLDI venue journal"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-26T10:32:10.048153+00:00_

Now I have all the information needed. Let me compile the verification results.

Here are the verification results for all 10 BibTeX entries:

---

```
[qi2024adelie] ✓
  - 存在性: ✓
  - 作者: ✓ (Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li — matches ACL Anthology)
  - 年份: ✓ (2024)
  - 标题: ✓ (ADELIE: Aligning Large Language Models on Information Extraction)
  - Venue: ✓ (Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Miami, Florida, USA)
  - DOI/arXiv: ✓ (URL https://aclanthology.org/2024.emnlp-main.419/ correct; also arXiv 2405.05008)
  - 正文引用: ✓ (section6_related_work.tex L13 "training-time internalization" context correct; appendix_related_work.tex L59 context correct)
  - 备注: 无问题
```

```
[zaratiana2024enrico] ✓
  - 存在性: ✓
  - 作者: ✓ (Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois)
  - 年份: ✓ (2024, arXiv preprint April 2024)
  - 标题: ✓ (EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction)
  - Venue: ✓ (arXiv preprint arXiv:2404.12493 — paper appears to remain an arXiv preprint without a formal conference/journal publication, so @article with journal={arXiv preprint} is appropriate)
  - DOI/arXiv: ✓ (https://arxiv.org/abs/2404.12493)
  - 正文引用: ✓ (section6_related_work.tex L18 "ASP constraints" context correct; appendix_related_work.tex L62 context correct)
  - 备注: 无问题
```

```
[khorshidi2025odke] ✓
  - 存在性: ✓
  - 作者: ✓ (Samira Khorshidi, Azadeh Nikfarjam, and others — author list matches arXiv/Semantic Scholar)
  - 年份: ✓ (2025, submitted to arXiv September 2025)
  - 标题: ✓ (ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs)
  - Venue: ✓ (arXiv preprint arXiv:2509.04696)
  - DOI/arXiv: ✓ (https://arxiv.org/abs/2509.04696)
  - 正文引用: ✓ (section6_related_work.tex L17 "post-hoc" context correct; appendix_related_work.tex L72 context correct)
  - 备注: 无问题
```

```
[upadhyay2023openie] ✓
  - 存在性: ✓
  - 作者: ✓ (Prajna Upadhyay, Oa
…[truncated 4820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T10:32:10.048339+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2021.naacl-main.5/",
  "prompt": "List the exact author names, pages, venue, and DOI for this paper by Zhong and Chen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2021.naacl-main.5/",
    "prompt": "List the exact author names, pages, venue, and DOI for this paper by Zhong and Chen"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-26T10:32:10.048489+00:00_

Web search results for query: ""Guided Open Vocabulary Image Captioning with Constrained Beam Search" Anderson Fernando Johnson Gould EMNLP 2017"

Links: [{"title":"Guided Open Vocabulary Image Captioning with Constrained Beam Search - ACL Anthology","url":"https://aclanthology.org/D17-1098/"},{"title":"[1612.00576] Guided Open Vocabulary Image Captioning with Constrained Beam Search","url":"https://arxiv.org/abs/1612.00576"},{"title":"Guided Open Vocabulary Image Captioning with Constrained Beam Search","url":"https://users.cecs.anu.edu.au/~sgould/papers/emnlp17-constrained-beam-search.pdf"},{"title":"(PDF) Guided Open Vocabulary Image Captioning with Constrained Beam Search","url":"https://www.researchgate.net/publication/322582680_Guided_Open_Vocabulary_Image_Captioning_with_Constrained_Beam_Search"},{"title":"[PDF] Guided Open Vocabulary Image Captioning with Constrained Beam Search | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Guided-Open-Vocabulary-Image-Captioning-with-Beam-Anderson-Fernando/086fa2fe3ee2a5b805aeaf9fbfe59ee8157dad5c"},{"title":"[PDF] Partially-Supervised Image Captioning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Partially-Supervised-Image-Captioning-Anderson-Gould/ceabd7ff28ce2d501511da998252aeb938adc98b"},{"title":"[PDF] nocaps: novel object captioning at scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/nocaps:-novel-object-captioning-at-scale-Agrawal-Desai/8b55402ffee2734bfc7d5d7595500916e1ef04e8"},{"title":"AMT evaluations of generated (Base+Syn) ImageNet captions versus human... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/AMT-evaluations-of-generated-Base-Syn-ImageNet-captions-versus-human-captions-by_fig1_322582680"}]

I found the paper you're looking for. Here are the key details:

"Guided Open Vocabulary Image Captioning with Constrained Beam Search" was published at EMNLP 2017 by Peter Anderson, Basura Fernando, Mark Johnson, and Stephen Gould
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-26T10:32:10.048652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction\" Lu Lin Xu ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction\" Lu Lin Xu ACL 2021"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-26T10:32:10.048849+00:00_

Web search results for query: ""JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models" Geng Cooper arXiv 2501.10868"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868v3"},{"title":"[Literature Review] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://www.themoonlight.io/en/review/jsonschemabench-a-rigorous-benchmark-of-structured-outputs-for-language-models"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"},{"title":"Generating Structured Outputs from Language Models","url":"https://nathanrchn.com/p/jsb"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs","url":"https://openreview.net/pdf/37c07f3099276aeb5fc23dcf5cbffa38b4405820.pdf"}]

I found the paper you're looking for! Here's information about it:

**JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models**

The paper is by Saibo Geng and 8 other authors. Note: The search results show the lead author is Saibo Geng, not "Geng Cooper" as mentioned in your query.

**Overview:**

Reliably generating structured outputs has become a critical capability for modern language model applications, with constrained decoding emerging as the dominant technology for enforcing structured outputs during generation. Despite its growing adoption, little has been done with the systematic evaluation of the behaviors and performance of constrained decoding.

**The Benchmark:**

JSONSchemaBench is a collection of 
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-26T10:32:10.049003+00:00_

# Paper Details: Zhong and Chen

**Authors:** "Zexuan Zhong and Danqi Chen"

**Pages:** 50–61

**Venue:** "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies"

**DOI:** "10.18653/v1/2021.naacl-main.5"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-26T10:32:10.049147+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BoostCD Sakota West EMNLP 2025 ACL Anthology 2025.emnlp-main.926"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BoostCD Sakota West EMNLP 2025 ACL Anthology 2025.emnlp-main.926"
  }
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-26T10:32:10.049284+00:00_

Web search results for query: ""Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction" Lu Lin Xu ACL 2021"

Links: [{"title":"GitHub - luyaojie/Text2Event: Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://github.com/luyaojie/Text2Event"},{"title":"[2106.09232] Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://arxiv.org/abs/2106.09232"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"[2106.09232] Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://ar5iv.labs.arxiv.org/html/2106.09232"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction | DeepAI","url":"https://deepai.org/publication/text2event-controllable-sequence-to-structure-generation-for-end-to-end-event-extraction"},{"title":"(PDF) Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://www.researchgate.net/publication/352506703_Text2Event_Controllable_Sequence-to-Structure_Generation_for_End-to-end_Event_Extraction"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction | Request PDF","url":"https://www.researchgate.net/publication/353486186_Text2Event_Controllable_Sequence-to-Structure_Generation_for_End-to-end_Event_Extraction"},{"title":"Text2Event/README.md at main · luyaojie/Text2Event","url":"https://github.com/luyaojie/Text2Event/blob/main/README.md"}]

I found the paper you're looking for! Here's what I found:

**Paper Information:**

"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction" was authored by Yaojie Lu, Hongyu Lin, Jin Xu, Xianpei Han, Jialong Tang, Annan Li, Le Sun, Meng Liao, and S
…[truncated 949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-26T10:32:10.049434+00:00_

Web search results for query: "dl.acm.org 10.1145/3591300 LMQL "Proceedings of the ACM on Programming Languages" PLDI venue journal"

Links: [{"title":"Prompting Is Programming: A Query Language for Large Language Models | Proceedings of the ACM on Programming Languages","url":"https://dl.acm.org/doi/abs/10.1145/3591300"},{"title":"[PDF] Prompting Is Programming: A Query Language for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prompting-Is-Programming:-A-Query-Language-for-Beurer-Kellner-Fischer/c2329c685f11efa25c562f97be71ff03103423fd"},{"title":"Prompting Is Programming: A Query Language for Large Language Models 1","url":"https://arxiv.org/pdf/2212.06094"},{"title":"ITERGEN: ITERATIVE SEMANTIC-AWARE STRUCTURED ...","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"ETH Library Prompting Is Programming: A Query Language for Large","url":"https://www.research-collection.ethz.ch/server/api/core/bitstreams/9a54d4ba-8d99-47a9-b960-b6f33df0ee1d/content"},{"title":"GitHub - eth-sri/lmql: A language for constraint-guided and efficient LLM programming. · GitHub","url":"https://github.com/eth-sri/lmql"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://ar5iv.labs.arxiv.org/html/2212.06094"},{"title":"[2212.06094] Prompting Is Programming: A Query Language for Large Language Models","url":"https://arxiv.org/abs/2212.06094"}]

Based on the search results, here's the information about the paper with DOI 10.1145/3591300:

The paper introduces LMQL (Language Model Query Language), which leverages constraints and control flow from language model prompts to generate efficient inference procedures. 

The paper was published in Proc. ACM Program. Lang., Vol. 7, No. PLDI, Article 186 in June 2023.

The paper is titled "Prompting Is Programming: A Query Language for Large Language Models" and was authored by Luca Beurer-Kellner, Marc Fischer, and Martin T. Vechev.

The work p
…[truncated 541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-26T10:32:10.049595+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation\" Luo Zhao Haffari ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation\" Luo Zhao Haffari ICML 2025"
  }
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-26T10:32:10.049783+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclanthology.org/2022.acl-long.337/",
  "prompt": "List the exact author names, pages, venue, location, publisher, and DOI for this PL-Marker paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclanthology.org/2022.acl-long.337/",
    "prompt": "List the exact author names, pages, venue, location, publisher, and DOI for this PL-Marker paper"
  }
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-26T10:32:10.049932+00:00_

# PL-Marker Paper Details

**Authors:** Deming Ye, Yankai Lin, Peng Li, Maosong Sun

**Pages:** 4904–4917

**Venue:** ACL (Annual Meeting of the Association for Computational Linguistics)

**Location:** Dublin, Ireland

**Publisher:** Association for Computational Linguistics

**DOI:** 10.18653/v1/2022.acl-long.337

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-26T10:32:10.050069+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick Polikarpova D'Antoni author list NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Grammar-Aligned Decoding\" Park Wang Berg-Kirkpatrick Polikarpova D'Antoni author list NeurIPS 2024"
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-26T10:32:10.050206+00:00_

Web search results for query: ""Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation" Luo Zhao Haffari ICML 2025"

Links: [{"title":"ICML Poster Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://icml.cc/virtual/2025/poster/45868"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Fr7kH2SFq7"},{"title":"Graph-constrained reasoning: Faithful reasoning on knowledge graphs with large language models","url":"https://bibbase.org/network/publication/luo-zhao-gong-haffari-pan-graphconstrainedreasoningfaithfulreasoningonknowledgegraphswithlargelanguagemodels-2025"},{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"GitHub - RManLuo/graph-constrained-reasoning: Official Implementation of ICML 2025 Paper: \"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models\". · GitHub","url":"https://github.com/RManLuo/graph-constrained-reasoning"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080v2"},{"title":"‪Graph-constrained reasoning: Faithful reasoning on knowledge graphs with large language models‬","url":"https://scholar.google.com/citations?citation_for_view=RO46HpcAAAAJ%3A7PzlFSSx8tAC&hl=en&user=RO46HpcAAAAJ&view_op=view_citation"},{"title":"FiDeLiS: Faithful Reasoning in Large Language Models for ...","url":"https://aclanthology.org/2025.findings-acl.436.pdf"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on","url":"https://icml.cc/media/icml-2025/Slides/45868.pdf"},{"title":"Graph-constrained Reasoning: Faithful ...","url":"https://www.summarizepaper.com/en/arxiv-id/2410.13080v1/"}]

I found the paper you're looking for! Her
…[truncated 1197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-26T10:32:10.050361+00:00_

Web search results for query: ""Grammar-Aligned Decoding" Park Wang Berg-Kirkpatrick Polikarpova D'Antoni author list NeurIPS 2024"

Links: [{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"Grammar-Aligned Decoding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240521047P/abstract"},{"title":"Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni · Grammar-Aligned Decoding","url":"https://slideslive.com/39028324/grammaraligned-decoding"}]

Based on the search results, here is the complete author list for the "Grammar-Aligned Decoding" paper from NeurIPS 2024:

Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, Loris D'Antoni

The paper was published at Advances in Neural Information Processing Systems 37 (NeurIPS 2024) Main Conference Track. The authors are affiliated with University of Wisconsin-Madison and University of California San Diego.


REMINDER: You MUST include the so
…[truncated 67 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-26T10:32:10.050513+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MLSys 2025 official proceedings name \"Proceedings of Machine Learning and Systems\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MLSys 2025 official proceedings name \"Proceedings of Machine Learning and Systems\""
  }
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-26T10:32:10.050645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\" Vukovic Arps SIGDIAL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\" Vukovic Arps SIGDIAL 2024"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-26T10:32:10.050836+00:00_

Web search results for query: ""Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" Vukovic Arps SIGDIAL 2024"

Links: [{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding - ACL Anthology","url":"https://aclanthology.org/2024.sigdial-1.33/"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/pdf/2408.02361"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=95&show=2000"},{"title":"Renato Vukovic","url":"https://renatovukovic.github.io/"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://www.paperreading.club/page?id=244596"},{"title":"dblp: David Arps","url":"https://dblp.org/pid/219/5595.html"},{"title":"Main program – SIGDIAL 2024","url":"https://2024.sigdial.org/main-program/"}]

I found the paper you're looking for! Here are the details:

**Paper:** Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-chin Lin, Michael Heck, and Milica Gasic

**Publication:** Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 370–384, Kyoto, Japan, 2024

**Overview:** State-of-the-art task-oriented dialogue systems typically rely on task-specific ontologies for fulfilling user queries. The majority of task-oriented dialogue data, such as customer service recordings, comes without ontology and annotation. Such ontologies are normally built manually, limiting the application of specialised systems.

**Approach:** The authors adapt Chain-of-Thought (CoT) decoding, recently developed for reasoning problems, to generative relation extraction. T
…[truncated 303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-26T10:32:10.051018+00:00_

Web search results for query: "BoostCD Sakota West EMNLP 2025 ACL Anthology 2025.emnlp-main.926"

Links: [{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"LIDDIA: Language-based Intelligent Drug Discovery Agent - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.603/"},{"title":"ACL Anthology - Google Groups","url":"https://groups.google.com/g/acl-anthology"},{"title":"Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.96/"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.0/"}]

I found references to EMNLP 2025 and author names including Sakota and West from a 2023 publication, but the search didn't return the specific paper you're looking for (2025.emnlp-main.926). Let me search more specifically for that paper ID.

Links: [{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2025 (@emnlpmeeting) / X","url":"https://x.com/emnlpmeeting?lang=en"},{
…[truncated 4115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-26T10:32:10.051176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UniversalNER Zhou Wenxuan ICLR 2024 openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UniversalNER Zhou Wenxuan ICLR 2024 openreview"
  }
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-26T10:32:10.051308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org/2025.emnlp-main.926 Sakota authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org/2025.emnlp-main.926 Sakota authors full list"
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-26T10:32:10.051439+00:00_

Web search results for query: "MLSys 2025 official proceedings name "Proceedings of Machine Learning and Systems""

Links: [{"title":"Proceedings of Machine Learning and Systems 7","url":"https://proceedings.mlsys.org/paper_files/paper/2025"},{"title":"List of Proceedings","url":"https://proceedings.mlsys.org/"},{"title":"2026 Conference","url":"https://mlsys.org/"},{"title":"2025 Conference","url":"https://mlsys.org/Conferences/2025"},{"title":"MLSys 2025 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/mlsys-2025"},{"title":"Context Parallelism for Scalable Million-Token Inference","url":"https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html"},{"title":"Conference on Machine Learning and Systems (MLSys)","url":"https://dblp.org/db/conf/mlsys/index.html"},{"title":"Proceedings of Machine Learning and Systems 6","url":"https://proceedings.mlsys.org/book/2024"}]

Based on the search results, the official name of the MLSys 2025 proceedings is "Proceedings of Machine Learning and Systems 7". This is confirmed across multiple sources, including the official proceedings portal and academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:32:10.051584+00:00_

Web search results for query: "UniversalNER Zhou Wenxuan ICLR 2024 openreview"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=r65xfUb76p"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | OpenReview","url":"https://openreview.net/forum?id=r65xfUb76p"},{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/universalner-targeted-distillation-from-large-language-models-for-open-named-entity-recognition/"},{"title":"Wenxuan Zhou","url":"https://openreview.net/profile?id=~Wenxuan_Zhou2"},{"title":"Wenxuan Zhou | OpenReview","url":"https://openreview.net/profile?id=~Wenxuan_Zhou1"},{"title":"Wenxuan Zhou 周文轩","url":"https://wzhouad.github.io/"},{"title":"ICLR 2024 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2024%2FConference"},{"title":"ICLR 2024 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2024"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230803279Z/abstract"}]

I found relevant information about the UniversalNER paper by Zhou Wenxuan et al. that was published at ICLR 2024. Here are the key details:

## Paper Overview

The paper shows how ChatGPT can be distilled into much smaller UniversalNER models for open NER using targeted distillation with mission-focused instruction tuning. 

## Key Contributions

The authors assembled the largest NER benchmark to date, comprising 43 datasets across 9 diverse domains such as biomedicine, programming, social media, law, finance.

The method successfully distills C
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-26T10:32:10.051791+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2410.13080 \"Graph-constrained Reasoning\" authors Luo Zhao Li Yuan-Fang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2410.13080 \"Graph-constrained Reasoning\" authors Luo Zhao Li Yuan-Fang"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-26T10:32:10.051963+00:00_

Web search results for query: "arXiv 2410.13080 "Graph-constrained Reasoning" authors Luo Zhao Li Yuan-Fang"

Links: [{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080"},{"title":"[2410.13080v1] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080v1"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2410.13080"},{"title":"Graph-constrained Reasoning: Faithful ...","url":"https://www.summarizepaper.com/en/arxiv-id/2410.13080v1/"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241013080L/abstract"},{"title":"GRAPH-CONSTRAINED REASONING: FAITHFUL REA-","url":"https://arxiv.org/pdf/2410.13080v1"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://proceedings.mlr.press/v267/luo25t.html"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models

**arXiv ID:** 2410.13080

**Authors:** Linhao Luo, Zicheng Zhao, Gholamreza Haffari, Yuan-Fang Li, Chen Gong, Shirui Pan

**Key Contribution:** The paper introduces graph-constrained reasoning (GCR), a novel framework that bridges structured knowledge in KGs with unstructured reasoning in LLMs. To elimin
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-26T10:32:10.052185+00:00_

Now I have all the information needed for a comprehensive verification. Here are the results:

---

**[beurer-kellner2023lmql] ✗**
- 存在性: ✓
- 作者: ✓ (Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✗ — BibTeX 写的是 `booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)}`，但实际发表在 **Proceedings of the ACM on Programming Languages (PACMPL), Vol. 7, No. PLDI, Article 186**。PLDI 论文自 2018 年起发表在 PACMPL 期刊而非独立会议论文集。如果使用 `@inproceedings` 且写 booktitle，当前写法可接受为简称惯例（许多 BibTeX 都这样引），但严格来说应为 `@article` 类型，journal = {Proc. ACM Program. Lang.}`, volume = {7}, number = {PLDI}`。**建议保留现状**，因为这是社区广泛使用的简写方式。
- DOI/arXiv: ✓ (DOI 10.1145/3591300 正确)
- 正文引用: ✓
- 备注: venue 类型可选择性修正为 `@article`，但当前写法在 NLP 社区中常见且可接受。

**[beurer-kellner2024domino] ✓**
- 存在性: ✓
- 作者: ✓ (Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ICML 2024, PMLR volume 235)
- DOI/arXiv: ✓ (URL https://proceedings.mlr.press/v235/beurer-kellner24a.html 正确)
- 正文引用: ✓
- 备注: pages 3658--3673 经 PMLR 官方确认正确。

**[park2024grammar] ✓**
- 存在性: ✓
- 作者: ✓ (Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (NeurIPS 2024)
- DOI/arXiv: ✓ (arXiv 2405.21047 正确)
- 正文引用: ✓
- 备注: 无问题。

**[decao2021genre] ✓**
- 存在性: ✓
- 作者: ✓ (De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio)
- 年份: ✓ (2021)
- 标题: ✓
- Venue: ✓ (ICLR 2021)
- DOI/arXiv: ✓ (OpenReview ID 5k8F6UU39V 正确)
- 正文引用: ✓
- 备注: 无问题。

**[josifoski2022genie] ✓**
- 存在性: ✓
- 作者: ✓ (Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert)
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (NAACL 2022)
- DOI/arXiv: ✓ (ACL Anthology 2022.naacl-main.342 正确)
- 正文引用: ✓
- 备注: pages 4626--4643 经确认正确。

**[geng2023gcd] ✓**
- 存在性: ✓
- 作者: ✓ (Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert)
- 年份: ✓ (2023)
- 标题: ✓
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-26T10:32:10.052355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Text2Event Lu Yaojie ACL 2021 authors list aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Text2Event Lu Yaojie ACL 2021 authors list aclanthology"
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-26T10:32:10.052509+00:00_

Web search results for query: "aclanthology.org/2025.emnlp-main.926 Sakota authors full list"

Links: [{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"LIDDIA: Language-based Intelligent Drug Discovery Agent - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.603/"},{"title":"Metadata correction for 2025.emnlp-main.1025 · Issue #8017 · acl-org/acl-anthology","url":"https://github.com/acl-org/acl-anthology/issues/8017"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.0/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"}]

The search results don't contain specific information about paper 2025.emnlp-main.926 or "Sakota" authors. Let me try a more direct search for that specific paper ID.

Links: [{"title":"EMNLP 2025 Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2025-paper-list/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Eighteen papers by CSE researchers at EMNLP 2025","url":"https://cse.engin.umich.edu/stories/eighteen-papers-by-cse-researchers-at-emnlp-2025"},{"title":"Most Influential EMNLP Papers (2025-09 Version) – Paper Digest","url":"https://www.pape
…[truncated 3815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-26T10:32:10.052662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Marija Sakota\" BoostCD BoostIE EPFL information extraction constrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Marija Sakota\" BoostCD BoostIE EPFL information extraction constrained decoding"
  }
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-26T10:32:10.052926+00:00_

Now I have all the verification data. Here is the complete report:

---

```
[scholak2021picard] ✓
  - 存在性: ✓
  - 作者: ✓ (Torsten Scholak, Nathan Schucher, Dzmitry Bahdanau — 完全匹配)
  - 年份: ✓ (2021)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing)
  - DOI/arXiv: ✓ (URL https://aclanthology.org/2021.emnlp-main.779/ 正确；DOI 为 10.18653/v1/2021.emnlp-main.779，BibTeX 未列出但不算错)
  - 正文引用: ✓ (section6_related_work.tex, appendix_related_work.tex 引用语境合理)
  - 备注: 无问题
```

```
[olasunkanmi2025relate] ✓
  - 存在性: ✓
  - 作者: ✓ (Olawumi Olasunkanmi, Mathew Satusky, Hong Yi, Chris Bizon, Harlin Lee, Stanley Ahalt — 完全匹配)
  - 年份: ✓ (arXiv 提交于 2025 年 9 月)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (arXiv preprint arXiv:2509.19057)
  - DOI/arXiv: ✓ (arXiv:2509.19057 正确)
  - 正文引用: ✓
  - 备注: 无问题
```

```
[zhou2026ontologytools] ✓
  - 存在性: ✓
  - 作者: ✓ (Xiaochi Zhou, Patrick Bulter, Changxuan Yang, Simon D. Rihm, Thitikarn Angkanaporn, Jethro Akroyd, Sebastian Mosbach, Markus Kraft — 完全匹配)
  - 年份: ✓ (2026，提交于 2026-02-03)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (arXiv preprint arXiv:2602.03439)
  - DOI/arXiv: ✓ (arXiv:2602.03439 正确)
  - 正文引用: ✓
  - 备注: 无问题
```

```
[eberts2020spert] ✓
  - 存在性: ✓
  - 作者: ✓ (Markus Eberts, Adrian Ulges)
  - 年份: ✓ (2020)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (ECAI 2020, Frontiers in Artificial Intelligence and Applications, Volume 325, pages 2006–2013)
  - DOI/arXiv: ✓ (DOI: 10.3233/FAIA200321 正确)
  - 正文引用: ✓
  - 备注: 无问题
```

```
[yan2021pfn] ✓
  - 存在性: ✓
  - 作者: ✓ (Zhiheng Yan, Chong Zhang, Jinlan Fu, Qi Zhang, Zhongyu Wei — 完全匹配)
  - 年份: ✓ (2021)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (EMNLP 2021, pages 185–197)
  - DOI/arXiv: ✓ (ACL Anthology URL 正确)
  - 正文引用: ✓
  - 备注: 无问题
```

```
[zhong2021frustratingly] ✓
  - 存在性: ✓
  - 作者: ✓ (Zexuan Zhong, Danqi Chen)
  - 年份: ✓ (2021)
  - 标题: ✓ (完全匹配)
  - Venue: ✓ (NAACL-HLT 2021, pages 50–61)
  - DOI/arXiv: ✓ (ACL Anthology URL 正确)
  - 正文引用: ✓ (section3 "supervised SOTA" 和 appendix_discussion 
…[truncated 1710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 33
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-26T10:32:10.053107+00:00_

Web search results for query: "Text2Event Lu Yaojie ACL 2021 authors list aclanthology"

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"Yaojie Lu - ACL Anthology","url":"https://aclanthology.org/people/y/yaojie-lu/"},{"title":"TEXT2EVENT: Controllable Sequence-to-Structure ...","url":"https://aclanthology.org/2021.acl-long.217.pdf"},{"title":"GitHub - luyaojie/Text2Event: Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://github.com/luyaojie/Text2Event"},{"title":"ACL-IJCNLP 2021","url":"https://2021.aclweb.org/program/accept/"},{"title":"From Discourse to Narrative: Knowledge Projection for Event Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.60/"},{"title":"Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 - ACL Anthology","url":"https://aclanthology.org/volumes/2021.findings-acl/"},{"title":"Instructions for ACL-IJCNLP 2021 Proceedings","url":"https://arxiv.org/html/2411.05088v1"}]

Based on the search results, here is the authors list for the Text2Event paper from ACL 2021:

The authors of "Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction" (ACL-IJCNLP 2021) are: Yaojie Lu, Hongyu Lin, Jin Xu, Xianpei Han, Jialong Tang, Annan Li, Le Sun, Meng Liao, and Shaoyi Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-26T10:32:10.053263+00:00_

Web search results for query: ""Marija Sakota" BoostCD BoostIE EPFL information extraction constrained decoding"

Links: [{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"Marija Sakota — People - EPFL","url":"https://people.epfl.ch/marija.sakota?lang=en"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"dblp: Marija Sakota","url":"https://dblp.org/pid/255/5704.html"},{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Marija Šakota – PhD @ EPFL","url":"https://ch.linkedin.com/in/marija-%C5%A1akota-13264797"},{"title":"dblp: Robert West 0001","url":"https://dblp.org/pid/20/7441-1.html"},{"title":"EPFL Data Science & AI Lab (dlab) · GitHub","url":"https://github.com/epfl-dlab"},{"title":"Marija Sakota - PhD student, EPFL","url":"https://openreview.net/profile?id=~Marija_Sakota1"}]

I found comprehensive information about Marija Sakota's work on BoostCD and BoostIE. Here's what the search results reveal:

## About Marija Sakota

Marija Šakota is a researcher at EPFL (École polytechnique fédérale de Lausanne) in Lausanne, Switzerland. She is a PhD student at EPFL (2020-2025) under the supervision of Robert West.

## BoostCD and BoostIE Research

Boosted Constrained Decoding (BoostCD) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the tw
…[truncated 996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-26T10:32:10.053420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"2021.acl-long.217\" Text2Event authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"2021.acl-long.217\" Text2Event authors"
  }
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-26T10:32:10.053552+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2302.10205 ChatIE Wei Cui Cheng Wang Zhang full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2302.10205 ChatIE Wei Cui Cheng Wang Zhang full author list"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T10:32:10.053695+00:00_

Web search results for query: "arxiv 2302.10205 ChatIE Wei Cui Cheng Wang Zhang full author list"

Links: [{"title":"[2302.10205] ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/abs/2302.10205"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/html/2302.10205"},{"title":"[2302.10205v1] Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/abs/2302.10205v1"},{"title":"arXiv:2302.10205v2 [cs.CL] 27 May 2024","url":"https://arxiv.org/pdf/2302.10205"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230210205W/abstract"},{"title":"Triple-based Factual Correctness Evaluation of AI-Generated Summaries - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405896325027892"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=1525&show=2000"},{"title":"Computer Science Jan 2025","url":"https://arxiv.org/list/cs/2025-01?skip=1025&show=2000"},{"title":"Computer Vision and Pattern Recognition Mar 2025","url":"https://arxiv.org/list/cs.CV/2025-03?skip=1200&show=2000"},{"title":"YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal   Information Extraction","url":"https://arxiv.org/pdf/2312.15548"}]

Based on the search results, the full author list for arxiv paper 2302.10205 (ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT) is: Xiang Wei, Xingyu Cui, Ning Cheng, Xiaobin Wang, Xin Zhang, Shen Huang, Pengjun Xie, Jinan Xu, Yufeng Chen, Meishan Zhang, Yong Jiang, and Wenjuan Han.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-26T10:32:10.053843+00:00_

Web search results for query: "site:aclanthology.org "2021.acl-long.217" Text2Event authors"

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"EventNarrative: A large-scale Event-centric Dataset for Knowledge   Graph-to-Text Generation","url":"https://arxiv.org/pdf/2111.00276"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end   Event Extraction","url":"https://arxiv.org/pdf/2106.09232"},{"title":"Event Extraction: A Survey","url":"https://arxiv.org/pdf/2210.03419"},{"title":"EventPlus: A Temporal Event Understanding Pipeline","url":"https://arxiv.org/pdf/2101.04922"}]

Based on the search results, the authors of Text2Event (paper 2021.acl-long.217) are Yaojie Lu, Hongyu Lin, Jin Xu, Xianpei Han, Jialong Tang, Annan Li, Le Sun, Meng Liao, and Shaoyi Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-26T10:32:10.053979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2312.07104 SGLang full author list Zheng Yin Xie Sun Huang Yu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2312.07104 SGLang full author list Zheng Yin Xie Sun Huang Yu"
  }
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-26T10:32:10.054107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Riedel \"Modeling Relations and Their Mentions without Labeled Text\" pages 148 163 ECML PKDD Springer 2010"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Riedel \"Modeling Relations and Their Mentions without Labeled Text\" pages 148 163 ECML PKDD Springer 2010"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-26T10:32:10.054227+00:00_

Web search results for query: "arxiv 2312.07104 SGLang full author list Zheng Yin Xie Sun Huang Yu"

Links: [{"title":"[2312.07104] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104"},{"title":"SGLang. Efficient Execution of Structured Language Model Programs;Zheng Et Al;ArXiv 2312.07104;2023","url":"https://www.scribd.com/document/905870039/SGLang-Efficient-Execution-of-Structured-Language-Model-Programs-Zheng-Et-Al-ArXiv-2312-07104-2023"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2312.07104v1","url":"https://www.summarizepaper.com/en/arxiv-id/2312.07104v1/"},{"title":"[2312.07104v2] SGLang: Efficient Execution of Structured Language Model Programs","url":"https://arxiv.org/abs/2312.07104v2"},{"title":"[2312.07104v1] Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/abs/2312.07104v1"}]

Based on the search results, the full author list for arXiv paper 2312.07104 (SGLang) is: Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph E. Gonzalez, Clark Barrett, and Ying Sheng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-26T10:32:10.054366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2501.10868 JSONSchemaBench full author list Geng Cooper Moskal Jenkins"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2501.10868 JSONSchemaBench full author list Geng Cooper Moskal Jenkins"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-26T10:32:10.054515+00:00_

Web search results for query: "Riedel "Modeling Relations and Their Mentions without Labeled Text" pages 148 163 ECML PKDD Springer 2010"

Links: [{"title":"Modeling Relations and Their Mentions without Labeled Text | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-15939-8_10"},{"title":"(PDF) Modeling Relations and Their Mentions without Labeled Text","url":"https://www.researchgate.net/publication/220698997_Modeling_Relations_and_Their_Mentions_without_Labeled_Text"},{"title":"Modeling Relations and Their Mentions without Labeled Text. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/ef2a9b14adb9048601312b439a3523d6"},{"title":"[PDF] Modeling Relations and Their Mentions without Labeled Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-Relations-and-Their-Mentions-without-Text-Riedel-Yao/e7e7b9a731678bf0494fe29cbebb42a822224cc6"},{"title":"Modeling Relations and Their Mentions without Labeled Text | UCL NLP","url":"https://nlp.cs.ucl.ac.uk/publications/2010-07-11-modeling-relations-and-their-mentions-without-labeled-text/"},{"title":"Modeling Relations and Their Mentions Without Labeled Text","url":"https://research.amanote.com/publication/0JSC2HMBKQvf0Bhi_EHb/modeling-relations-and-their-mentions-without-labeled-text"},{"title":"Deep Distant Supervision: Learning Statistical Relational Models for Weak Supervision in Natural Language Extraction | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-319-41706-6_18"},{"title":"REET: Joint Relation Extraction and Entity Typing via Multi-task Learning | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-32233-5_26"},{"title":"Relation Extraction from the Web Using Distant Supervision | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-13704-9_3"}]

I found the paper you're looking for. The paper "Modeling Relations and Their Mentions without Labeled Text" by Riedel, S., Yao, L., and Mc
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-26T10:32:10.054785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.13080 \"Graph-constrained Reasoning\" exact title \"Knowledge Graph Rationale Generation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.13080 \"Graph-constrained Reasoning\" exact title \"Knowledge Graph Rationale Generation\""
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-26T10:32:10.055008+00:00_

Web search results for query: "arxiv 2501.10868 JSONSchemaBench full author list Geng Cooper Moskal Jenkins"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"epfl-dlab/JSONSchemaBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868"},{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"},{"title":"epfl-dlab/JSONSchemaBench · Add paper link and GitHub link, specify task category and license","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench/discussions/2/files"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2501.10868"},{"title":"(PDF) Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://www.researchgate.net/publication/388231978_Generating_Structured_Outputs_from_Language_Models_Benchmark_and_Studies"}]

Based on the search results, the full author list for arxiv 2501.10868 (JSONSchemaBench) is: Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, and Harsha Nori.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-26T10:32:10.055246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ChatIE \"Zero-Shot Information Extraction\" Wei 2023 published venue conference journal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ChatIE \"Zero-Shot Information Extraction\" Wei 2023 published venue conference journal"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-26T10:32:10.055453+00:00_

Web search results for query: "arxiv 2410.13080 "Graph-constrained Reasoning" exact title "Knowledge Graph Rationale Generation""

Links: [{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080v1"},{"title":"Graph-constrained Reasoning: Faithful ...","url":"https://www.summarizepaper.com/en/arxiv-id/2410.13080v1/"},{"title":"[2410.13080v1] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080v1"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.13080"},{"title":"GRAPH-CONSTRAINED REASONING: FAITHFUL REA-","url":"https://arxiv.org/pdf/2410.13080v1"},{"title":"Paper page - Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://huggingface.co/papers/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://www.emergentmind.com/papers/2410.13080"}]

I found the paper arxiv 2410.13080! Here are the search results:

**Title:** Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models

**Authors:** Linhao Luo, Zicheng Zhao, Chen Gong, Gholamreza Haffari, Shirui Pan

**Submission Date:** October 16, 2024

**Overview:** The work introduces graph-constrained reasoning (GCR), a novel framework that bridges structured knowledge in KGs with unstructured reasoning in LLMs. GCR ensures fait
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-26T10:32:10.055705+00:00_

Web search results for query: "ChatIE "Zero-Shot Information Extraction" Wei 2023 published venue conference journal"

Links: [{"title":"[2302.10205] ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/abs/2302.10205"},{"title":"[PDF] Zero-Shot Information Extraction via Chatting with ChatGPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Zero-Shot-Information-Extraction-via-Chatting-with-Wei-Cui/f4cba0db34aa0c389cec267ca1f3ba5255ea2645"},{"title":"Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://www.researchgate.net/publication/368688168_Zero-Shot_Information_Extraction_via_Chatting_with_ChatGPT"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT","url":"https://arxiv.org/html/2302.10205v2"},{"title":"GitHub - cocacola-lab/ChatIE: The online version is temporarily unavailable because we cannot afford the key. You can clone and run it locally. Note: we set defaul openai key. If keys exceed plan and are invalid, please tell us. The response speed depends on openai. ( sometimes, the official is too crowded and slow) · GitHub","url":"https://github.com/cocacola-lab/chatie"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/chatie-zero-shot-information-extraction-via-chatting"},{"title":"ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT | alphaXiv","url":"https://www.alphaxiv.org/abs/2302.10205"},{"title":"ChatIE- Zero-Shot Information Extraction via Chatting With ChatGPT","url":"https://www.scribd.com/document/888484398/ChatIE-Zero-Shot-Information-Extraction-via-Chatting-With-ChatGPT"}]

Based on the search results, here's what I found about ChatIE:

**Paper Details:**
ChatIE was published in arXiv.org on February 20, 2023. The paper is titled "Zero-Shot Information Extraction via Chatting with ChatGPT" and the authors include Xiang Wei and X
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-26T10:32:10.055951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICML 2025 \"Graph-constrained Reasoning\" Luo Zhao authors \"Yuan-Fang Li\" proceedings.mlr.press"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICML 2025 \"Graph-constrained Reasoning\" Luo Zhao authors \"Yuan-Fang Li\" proceedings.mlr.press"
  }
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-26T10:32:10.056153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2021.naacl-main.69 \"Document-Level Event Argument Extraction\" venue proceedings title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2021.naacl-main.69 \"Document-Level Event Argument Extraction\" venue proceedings title"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-26T10:32:10.056344+00:00_

Web search results for query: "aclanthology.org 2021.naacl-main.69 "Document-Level Event Argument Extraction" venue proceedings title"

Links: [{"title":"Document-Level Event Argument Extraction by Conditional Generation - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.69/"},{"title":"EIGP: document-level event argument extraction with information enhancement generated based on prompts | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-024-02213-4"},{"title":"DL_EventExtractionPapers/Category/Doc-EE.md at master · carrie0307/DL_EventExtractionPapers","url":"https://github.com/carrie0307/DL_EventExtractionPapers/blob/master/Category/Doc-EE.md"},{"title":"DuEE-Fin: A Large-Scale Dataset for Document-Level Event Extraction | Natural Language Processing and Chinese Computing","url":"https://dl.acm.org/doi/10.1007/978-3-031-17120-8_14"},{"title":"Event Time Extraction and Propagation via Graph Attention Networks - ACL Anthology","url":"https://aclanthology.org/2021.naacl-main.6/"},{"title":"Document-Level Event Argument Extraction by Leveraging Redundant Information and Closed Boundary Loss - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.222/"}]

Based on the search results, here is the information for the paper at aclanthology.org 2021.naacl-main.69:

**Title:** Document-Level Event Argument Extraction by Conditional Generation

**Authors:** Li, Sha; Ji, Heng; Han, Jiawei

**Venue:** Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies

**Publication Details:** June 2021, Online, Association for Computational Linguistics, pages 894-908


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-26T10:32:10.056561+00:00_

Web search results for query: "ICML 2025 "Graph-constrained Reasoning" Luo Zhao authors "Yuan-Fang Li" proceedings.mlr.press"

Links: [{"title":"ICML Poster Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://icml.cc/virtual/2025/poster/45868"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Fr7kH2SFq7"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on","url":"https://icml.cc/media/icml-2025/Slides/45868.pdf"},{"title":"Linhao Luo","url":"https://rmanluo.github.io/"},{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"Integrating Large Language Models and Knowledge Graphs for Next-level AGI","url":"https://www.cs.emory.edu/~jyang71/files/klm-tutorial.pdf"},{"title":"ICML 2025 Thursday 07/17","url":"https://icml.cc/virtual/2025/day/7/17"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080"}]

I found information about the paper you're looking for. Here are the key details:

Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models is an ICML 2025 paper authored by Linhao Luo, Zicheng Zhao, Gholamreza Haffari, Yuan-Fang Li, Chen Gong, and Shirui Pan.

The work introduces graph-constrained reasoning (GCR), a novel framework that bridges structured knowledge in knowledge graphs with unstructured reasoning in LLMs, designed to eliminate hallucinations and ensure faithful KG-grounded reasoning.

The paper is available at:
- ICML official website (icml.cc)
- arXiv (arxiv.org/abs/2410.13080)
- OpenReview

Note: The author name appears as "Linhao Luo" (not "Luo Zhao" as in your query), and "Yuan-Fang Li" is indeed one of the co-authors.


REMINDER: Y
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-26T10:32:10.056806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"2021.acl-long.217\" \"Shaobo Chen\" OR \"Shaoyi Chen\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"2021.acl-long.217\" \"Shaobo Chen\" OR \"Shaoyi Chen\""
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-26T10:32:10.057031+00:00_

Web search results for query: "site:aclanthology.org "2021.acl-long.217" "Shaobo Chen" OR "Shaoyi Chen""

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"TEXT2EVENT: Controllable Sequence-to-Structure ...","url":"https://aclanthology.org/2021.acl-long.217.pdf"},{"title":"ACL 2024 The 62nd Annual Meeting of the Association for","url":"https://aclanthology.org/2024.acl-short.0.pdf"},{"title":"2021.acl-long.0.pdf","url":"https://aclanthology.org/2021.acl-long.0.pdf"},{"title":"Shaoyi Huang - ACL Anthology","url":"https://aclanthology.org/people/shaoyi-huang/"},{"title":"Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 - ACL Anthology","url":"https://aclanthology.org/volumes/2021.findings-acl/"},{"title":"Sparse Progressive Distillation: Resolving Overfitting under Pretrain-and-Finetune Paradigm - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.16/"},{"title":"59th Annual Meeting of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/events/acl-2021/"},{"title":"ACL 2022 The 60th Annual Meeting of the Association for ...","url":"https://aclanthology.org/2022.acl-long.0.pdf"}]

Based on the search results, I found the paper you're looking for:

The paper with ID 2021.acl-long.217 is titled "Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction" and includes Shaoyi Chen as one of the authors. 

The full author list is: Yaojie Lu, Hongyu Lin, Jin Xu, Xianpei Han, Jialong Tang, Annan Li, Le Sun, Meng Liao, and Shaoyi Chen, with Shaoyi Chen affiliated with the Data Quality Team at WeChat, Tencent Inc., China.

The paper was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Paper
…[truncated 131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-26T10:32:10.057261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org/2021.acl-long.217 Text2Event pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org/2021.acl-long.217 Text2Event pages"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-26T10:32:10.057457+00:00_

Web search results for query: "aclanthology.org/2021.acl-long.217 Text2Event pages"

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"GitHub - luyaojie/Text2Event: Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://github.com/luyaojie/Text2Event"},{"title":"Aclanthology","url":"https://aclanthology.org/2023.acl-long.584.pdf"},{"title":"ACL Anthology - Google Groups","url":"https://groups.google.com/g/acl-anthology"},{"title":"Two Decades of the ACL Anthology: Development, Impact, and Open Challenges","url":"https://people.cs.georgetown.edu/nschneid/p/aclanth.pdf"},{"title":"Findings of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/findings/"},{"title":"Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations - ACL Anthology","url":"https://aclanthology.org/volumes/2021.acl-demo/"},{"title":"Instructions for ACL-IJCNLP 2021 Proceedings","url":"https://arxiv.org/html/2411.05088v1"}]

Based on the search results, I found the paper you're looking for:

Text2Event is a sequence-to-structure generation paradigm that can directly extract events from the text in an end-to-end manner. The approach includes a sequence-to-structure network for unified event extraction, a constrained decoding algorithm for event knowledge injection during inference, and a curriculum learning algorithm for efficient model learning.

The paper "Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction" was published by Lu et al. in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processi
…[truncated 383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-26T10:32:10.057797+00:00_

Now I have all the information needed. Let me compile the verification results.

Here are the verification results for all 10 BibTeX entries:

---

```
[ugare2025itergen] ✓
  - 存在性: ✓
  - 作者: ✓ (Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, Sasa Misailovic — all confirmed)
  - 年份: ✓ (2025, ICLR 2025)
  - 标题: ✓ (IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking)
  - Venue: ✓ (The Thirteenth International Conference on Learning Representations = ICLR 2025)
  - DOI/arXiv: ✓ (OpenReview URL https://openreview.net/forum?id=ac93gRzxxV confirmed; also arXiv 2410.07295)
  - 正文引用: ✓ (backtracking context is appropriate)
  - 备注: 无问题
```

```
[boostcd2025] ✓
  - 存在性: ✓
  - 作者: ✓ (Marija Sakota, Robert West — confirmed at EPFL)
  - 年份: ✓ (2025, EMNLP 2025)
  - 标题: ✓
  - Venue: ✓ (Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, ACL Anthology 2025.emnlp-main.926 confirmed)
  - DOI/arXiv: ✓ (ACL Anthology URL confirmed; also arXiv 2506.14901)
  - 正文引用: ✓ (grammar-only / constrained decoding context is appropriate)
  - 备注: 作者姓名 Sakota 实际带变音符号 Šakota，BibTeX 中未标注但不影响渲染，可接受
```

```
[luan2018scierc] ✓
  - 存在性: ✓
  - 作者: ✓ (Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi — all confirmed)
  - 年份: ✓ (2018)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2018, Brussels, Belgium, pages 3219-3232 — all confirmed via ACL Anthology D18-1360)
  - DOI/arXiv: ✓ (https://aclanthology.org/D18-1360/ confirmed)
  - 正文引用: ✓ (SciERC dataset context is appropriate)
  - 备注: 无问题
```

```
[yao2019docred] ✓
  - 存在性: ✓
  - 作者: ✓ (Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, Maosong Sun — all confirmed)
  - 年份: ✓ (2019)
  - 标题: ✓
  - Venue: ✓ (ACL 2019, Florence, Italy, pages 764-777 — all confirmed via ACL Anthology P19-1074)
  - DOI/arXiv: ✓ (https://aclanthology.org/P19-1074/ confirmed)
  - 正文引用: ✓ (dataset context is appropriate)
  - 备注: 无问题
```

```
[wei2023zeroshot] ✓
  - 存在性:
…[truncated 3341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-26T10:32:10.058150+00:00_

Now I have all the information needed. Here is the complete verification report:

---

**[51. wang2023instructuie] ✓**
- 存在性: ✓
- 作者: ✓ — Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du — matches
- 年份: ✓ (2023)
- 标题: ✓ "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction"
- Venue: ✓ arXiv preprint arXiv:2304.08085
- DOI/arXiv: ✓ arXiv:2304.08085
- 正文引用: ✓ — training-time internalization context is appropriate
- 备注: 无问题

---

**[52. zhou2024universalner] ✓**
- 存在性: ✓
- 作者: ✓ — Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon
- 年份: ✓ (2024, published at ICLR 2024)
- 标题: ✓ "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition"
- Venue: ✓ — The Twelfth International Conference on Learning Representations (ICLR 2024). OpenReview link confirmed: `https://openreview.net/forum?id=r65xfUb76p`
- DOI/arXiv: ✓ (arXiv:2308.03279; OpenReview ID r65xfUb76p)
- 正文引用: ✓ — training-time internalization context is appropriate
- 备注: 无问题

---

**[53. wadhwa2023revisiting] ✓**
- 存在性: ✓
- 作者: ✓ — Somin Wadhwa, Silvio Amir, Byron Wallace
- 年份: ✓ (2023)
- 标题: ✓ "Revisiting Relation Extraction in the era of Large Language Models"
- Venue: ✓ — Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15566–15589
- DOI/arXiv: ✓ — DOI: 10.18653/v1/2023.acl-long.868, URL: https://aclanthology.org/2023.acl-long.868
- 正文引用: ✓ — "violations persist" and "R-F1 range consistent with recent evaluations" contexts are appropriate
- 备注: 无问题

---

**[54. paolini2021tanl] ✓**
- 存在性: ✓
- 作者: ✓ — Giovanni Paolini, Ben Athiwaratkun, Jason Krone, Jie Ma, Alessandro Achille, Rishita Anubhai, Cicero Nogueira dos Santos, Bing Xiang, Stefano Soatto
- 年份: ✓ (2021)
- 标题: ✓ "Structured Prediction as Translation between Augmented Natural Languages"
- Venue: ✓ — Internat
…[truncated 4712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "Agent",
  "elapsed_ms": 22
}
```

</details>

---

### Tool call

_source line 273 · 2026-05-26T10:32:10.058447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Text2Event\" \"Controllable Sequence-to-Structure\" Lu Yaojie ACL 2021 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Text2Event\" \"Controllable Sequence-to-Structure\" Lu Yaojie ACL 2021 authors"
  }
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-26T10:32:10.058608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Graph-Constrained Reasoning\" Luo Linhao arXiv 2410.13080 title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Graph-Constrained Reasoning\" Luo Linhao arXiv 2410.13080 title"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-26T10:32:10.058814+00:00_

Web search results for query: ""Text2Event" "Controllable Sequence-to-Structure" Lu Yaojie ACL 2021 authors"

Links: [{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.217/"},{"title":"GitHub - luyaojie/Text2Event: Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://github.com/luyaojie/Text2Event"},{"title":"[2106.09232] Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction","url":"https://arxiv.org/abs/2106.09232"},{"title":"TEXT2EVENT: Controllable Sequence-to-Structure ...","url":"https://aclanthology.org/2021.acl-long.217.pdf"},{"title":"[PDF] Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Text2Event:-Controllable-Sequence-to-Structure-for-Lu-Lin/a0c78661e4a5278c65cefc5b4fdef669dcae7e17"},{"title":"Text2Event/README.md at main · luyaojie/Text2Event","url":"https://github.com/luyaojie/Text2Event/blob/main/README.md"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction | Request PDF","url":"https://www.researchgate.net/publication/353486186_Text2Event_Controllable_Sequence-to-Structure_Generation_for_End-to-end_Event_Extraction"},{"title":"Paper note ACL 2021|text2event: controllable sequence to structure generation for end-to-end event extract","url":"https://copyfuture.com/blogs-details/202202111902123547"},{"title":"Text2Event: Controllable Sequence-to-Structure Generation for End-to-end Event Extraction | Papers With Code","url":"https://paperswithcode.com/paper/text2event-controllable-sequence-to-structure"},{"title":"Yaojie Lu's Homepage","url":"https://luyaojie.github.io/"}]

Based on the search results, here is the information about the "Text2Event: Controllable Sequence-to-Structure Generation for End-t
…[truncated 776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-26T10:32:10.058995+00:00_

Web search results for query: ""Graph-Constrained Reasoning" Luo Linhao arXiv 2410.13080 title"

Links: [{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080v1"},{"title":"[2410.13080v1] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080v1"},{"title":"Paper page - Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://huggingface.co/papers/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful ...","url":"https://www.summarizepaper.com/en/arxiv-id/2410.13080v1/"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2410.13080"},{"title":"[PDF] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Graph-constrained-Reasoning:-Faithful-Reasoning-on-Luo-Zhao/9ef5f1c54f254589541ae63c33408ea1d3ad899a"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://www.emergentmind.com/papers/2410.13080"}]

Based on the search results, here is the information about the paper:

**Title:** Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models

**Authors:** Linhao Luo, Zicheng Zhao, Chen Gong, Gholamreza Haffari, and Shirui Pan

**ArXiv ID:** 2410.13080

**Key Contribution:** The work introdu
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 277 · 2026-05-26T10:32:10.059194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2410.13080 \"Graph-constrained Reasoning\" full author list \"Yuan-Fang Li\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2410.13080 \"Graph-constrained Reasoning\" full author list \"Yuan-Fang Li\""
  }
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-26T10:32:10.059338+00:00_

Web search results for query: "arXiv 2410.13080 "Graph-constrained Reasoning" full author list "Yuan-Fang Li""

Links: [{"title":"[2410.13080] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/html/2410.13080v1"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2410.13080"},{"title":"Graph-constrained Reasoning: Faithful ...","url":"https://www.summarizepaper.com/en/arxiv-id/2410.13080v1/"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241013080L/abstract"},{"title":"Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.13080"},{"title":"[2410.13080v1] Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models","url":"https://arxiv.org/abs/2410.13080v1"},{"title":"GRAPH-CONSTRAINED REASONING: FAITHFUL REA-","url":"https://arxiv.org/pdf/2410.13080v1"},{"title":"Integrating Large Language Models and Knowledge Graphs for Next-level AGI","url":"https://www.cs.emory.edu/~jyang71/files/klm-tutorial.pdf"}]

Based on the search results, I found the full author list for arXiv paper 2410.13080 "Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models":

The authors are: Linhao Luo, Zicheng Zhao, Gholamreza Haffari, Yuan-Fang Li, Chen Gong, and Shirui Pan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 279 · 2026-05-26T10:32:10.059525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Let Me Speak Freely\" Tam \"Format Restrictions\" ACL Anthology EMNLP 2024 industry title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Let Me Speak Freely\" Tam \"Format Restrictions\" ACL Anthology EMNLP 2024 industry title"
  }
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-26T10:32:10.059655+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynCode \"LLM Generation with Grammar Augmentation\" TMLR Ugare year accepted 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynCode \"LLM Generation with Grammar Augmentation\" TMLR Ugare year accepted 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-26T10:32:10.059846+00:00_

Web search results for query: ""Let Me Speak Freely" Tam "Format Restrictions" ACL Anthology EMNLP 2024 industry title"

Links: [{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.91/"},{"title":"Let Me Speak Freely? A Study on the Impact of Format ...","url":"https://aclanthology.org/2024.emnlp-industry.91.pdf"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.emnlp-industry.0.pdf"},{"title":"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance. | Request PDF","url":"https://www.researchgate.net/publication/386203559_Let_Me_Speak_Freely_A_Study_On_The_Impact_Of_Format_Restrictions_On_Large_Language_Model_Performance"},{"title":"[2408.02442] Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/abs/2408.02442"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"}]

Based on the search results, I found the paper you're looking for:

"Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance." The authors are Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, and Yun-Nung Chen.

The paper was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track, pages 1218–1236, Miami, Florida, US.

The paper is available in the ACL Anthology at: https://aclanthology.org/2024.emnlp-industry.91/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 282 · 2026-05-26T10:32:10.060026+00:00_

Web search results for query: "SynCode "LLM Generation with Grammar Augmentation" TMLR Ugare year accepted 2024 2025"

Links: [{"title":"[2403.01632] SynCode: LLM Generation with Grammar Augmentation","url":"https://arxiv.org/abs/2403.01632"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/syncode-llm-generation-with-grammar-augmentation/"},{"title":"[PDF] SynCode: LLM Generation with Grammar Augmentation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SynCode:-LLM-Generation-with-Grammar-Augmentation-Ugare-Suresh/46a41357eadac1459c81588136c5c053abfeefe4"},{"title":"SynCode: LLM Generation with Grammar Augmentation | OpenReview","url":"https://openreview.net/forum?id=HiUZtgAPoH"},{"title":"GitHub - structuredllm/syncode: Efficient and general syntactical decoding for Large Language Models · GitHub","url":"https://github.com/structuredllm/syncode"},{"title":"Accepted papers at TMLR on X: \"SynCode: LLM Generation with Grammar Augmentation Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa Misailovic, Gagandeep Singh. Action editor: Ying Wei. https://t.co/tS6qBH16mq #syntax #automaton #serialization\" / X","url":"https://x.com/TmlrPub/status/1951447922060435673"},{"title":"Shubham Ugare | publications","url":"https://shubhamugare.github.io/publications/"},{"title":"Paper page - SynCode: LLM Generation with Grammar Augmentation","url":"https://huggingface.co/papers/2403.01632"},{"title":"SynCode: LLM Generation with Grammar Augmentation - Paper Detail","url":"https://deeplearn.org/arxiv/546356/syncode:-llm-generation-with-grammar-augmentation"},{"title":"[2403.01632v1] Improving LLM Code Generation with Grammar Augmentation","url":"https://arxiv.org/abs/2403.01632v1"}]

Based on the search results, here's what I found about the SynCode paper:

**Paper Details:**
- **Title:** SynCode: LLM Generation with Grammar Augmentation by Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa 
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-beta_20260526T101833",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 283 · 2026-05-26T10:32:10.060318+00:00_

All verifications complete. Here is the full audit report for all 60 BibTeX entries.

---

## 全量引用正确性审计报告（Worker B）

### 逐条核对结果

```
[kwon2023vllm] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (SOSP 2023)
  - DOI/arXiv: ✓ (可补充 arXiv:2309.06180)
  - 正文引用: ✓
  - 备注: 无问题

[synchromesh_iclr2022] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2022)
  - 标题: ✓
  - Venue: ✓ (ICLR 2022)
  - DOI/arXiv: ✓ (OpenReview KmtVD97J43e)
  - 正文引用: ✓
  - 备注: 无问题

[mgd_neurips2023] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (NeurIPS 2023, vol.36)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[pldi2025_type_constrained_codegen] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (PACMPL vol.9 PLDI)
  - DOI/arXiv: ✓ (DOI 10.1145/3729274)
  - 正文引用: ✓
  - 备注: 无问题

[roth_yih_2004] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2004)
  - 标题: ✓
  - Venue: ✓ (CoNLL-2004 at HLT-NAACL)
  - DOI/arXiv: ✓ (ACL Anthology W04-2401)
  - 正文引用: ✓
  - 备注: 无问题

[adakgc_emnlp2023] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (Findings of EMNLP 2023)
  - DOI/arXiv: ✓ (ACL Anthology 2023.findings-emnlp.425)
  - 正文引用: ✓
  - 备注: 无问题

[knowcoder_acl2024] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (ACL 2024 Long Papers)
  - DOI/arXiv: ✓ (ACL Anthology 2024.acl-long.475)
  - 正文引用: ✓
  - 备注: 无问题

[spires_2024] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (Bioinformatics, vol.40 no.3)
  - DOI/arXiv: ✓ (DOI 10.1093/bioinformatics/btae104)
  - 正文引用: ✓
  - 备注: 无问题

[ontologx_2025] ✗ (轻微)
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (year=2026 对应期刊正式发表日期正确)
  - 标题: ✓
  - Venue: ✓ (Advanced Intelligent Systems)
  - DOI/arXiv: ✓ (DOI 10.1002/aisy.202501381)
  - 正文引用: ✓
  - 备注: cite key "ontologx_2025" 与 year=2026 不一致。建议统一。

[ekaw2024_ontology_beam] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (EKAW 2024, LNCS 15370)
  - DOI/arXiv: ✓ (DOI 10.1007/978-3-031-77792-9_23)
  - 正文引用: ✓
  - 备注: 无问题

[scholak2021picard] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2021)
  - DOI/arXiv: ✓ (ACL Anthology 2021.emnlp-main.779)
  - 正文引用: ✓
  - 备注: 无问题

[olasunkanmi2025relate] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (arXiv:2509.19057)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[zhou2026ontologytools] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2026)
  - 标题: ✓
  - Venue: ✓ (arXiv:2602.03439)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[eberts2020spert] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2020)
  - 标题: ✓
  - Venue: ✓ (ECAI 2020, FAIA vol.325)
  - DOI/arXiv: ✓ (DOI 10.3233/FAIA200321)
  - 正文引用: ✓
  - 备注: 无问题

[yan2021pfn] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2021)
  - DOI/arXiv: ✓ (ACL Anthology 2021.emnlp-main.17)
  - 正文引用: ✓
  - 备注: 无问题

[zhong2021frustratingly] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (NAACL 2021)
  - DOI/arXiv: ✓ (ACL Anthology 2021.naacl-main.5)
  - 正文引用: ✓
  - 备注: 无问题

[ye2022packed] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2022)
  - 标题: ✓
  - Venue: ✓ (ACL 2022 Long Papers)
  - DOI/arXiv: ✓ (ACL Anthology 2022.acl-long.337)
  - 正文引用: ✓
  - 备注: 无问题

[zhou2026snowballing] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2026)
  - 标题: ✓
  - Venue: ✓ (arXiv:2604.06066)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[dong2025xgrammar] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (MLSys 2025，缺卷号但可接受)
  - DOI/arXiv: ✓ (arXiv:2411.15100)
  - 正文引用: ✓
  - 备注: 无问题

[willard2023outlines] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (arXiv:2307.09702)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[beurer-kellner2023lmql] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (PLDI 2023; 严格说应为 @article PACMPL，但 @inproceedings 写法在社区中普遍接受)
  - DOI/arXiv: ✓ (DOI 10.1145/3591300)
  - 正文引用: ✓
  - 备注: 无问题

[beurer-kellner2024domino] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (ICML 2024, PMLR vol.235)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[park2024grammar] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (NeurIPS 2024)
  - DOI/arXiv: ✓ (arXiv:2405.21047)
  - 正文引用: ✓
  - 备注: 无问题

[decao2021genre] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (ICLR 2021)
  - DOI/arXiv: ✓ (OpenReview 5k8F6UU39V)
  - 正文引用: ✓
  - 备注: 无问题

[josifoski2022genie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2022)
  - 标题: ✓
  - Venue: ✓ (NAACL 2022)
  - DOI/arXiv: ✓ (ACL Anthology 2022.naacl-main.342)
  - 正文引用: ✓
  - 备注: 无问题

[geng2023gcd] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2023)
  - DOI/arXiv: ✓ (ACL Anthology 2023.emnlp-main.674)
  - 正文引用: ✓
  - 备注: 无问题

[lu2021neurologic] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (NAACL 2021)
  - DOI/arXiv: ✓ (ACL Anthology 2021.naacl-main.339)
  - 正文引用: ✓
  - 备注: 无问题

[lu2022uie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2022)
  - 标题: ✓
  - Venue: ✓ (ACL 2022)
  - DOI/arXiv: ✓ (ACL Anthology 2022.acl-long.395)
  - 正文引用: ✓
  - 备注: 无问题

[sainz2024gollie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (ICLR 2024)
  - DOI/arXiv: ✓ (OpenReview Y3wpuxd7u9)
  - 正文引用: ✓
  - 备注: 无问题

[li2023codeie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (ACL 2023 Long Papers)
  - DOI/arXiv: ✓ (ACL Anthology 2023.acl-long.855)
  - 正文引用: ✓
  - 备注: 无问题

[qi2024adelie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2024)
  - DOI/arXiv: ✓ (ACL Anthology 2024.emnlp-main.419)
  - 正文引用: ✓
  - 备注: 无问题

[zaratiana2024enrico] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (arXiv:2404.12493)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[khorshidi2025odke] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (arXiv:2509.04696)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[upadhyay2023openie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (Findings of EACL 2023)
  - DOI/arXiv: ✓ (ACL Anthology 2023.findings-eacl.95)
  - 正文引用: ✓
  - 备注: 无问题

[regino2025kgcurator] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (GenAIK Workshop at COLING 2025)
  - DOI/arXiv: ✓ (ACL Anthology 2025.genaik-1.10)
  - 正文引用: ✓
  - 备注: 无问题

[tam2024letmespeak] ✗
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✗ — BibTeX 用 arXiv 标题 "...on Performance of Large Language Models"，
    ACL Anthology 正式版标题为 "...On Large Language Model Performance."
  - Venue: ✓ (EMNLP 2024 Industry Track)
  - DOI/arXiv: ✓ (ACL Anthology 2024.emnlp-industry.91)
  - 正文引用: ✓
  - 备注: 应以 ACL Anthology 正式版标题为准

[banerjee2025crane] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (ICML 2025, PMLR vol.267)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[schall2025hiddencost] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (RANLP 2025)
  - DOI/arXiv: ✓ (ACL Anthology 2025.ranlp-1.124)
  - 正文引用: ✓
  - 备注: 可补充 pages={1074--1084}

[cabot2021rebel] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (Findings of EMNLP 2021)
  - DOI/arXiv: ✓ (ACL Anthology 2021.findings-emnlp.204)
  - 正文引用: ✓
  - 备注: 无问题

[ugare2024syncode] ✗
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✗ — TMLR accepted 2025-06-16，应为 year={2025}
  - 标题: ✓
  - Venue: ✓ (TMLR)
  - DOI/arXiv: ✓ (OpenReview HiUZtgAPoH)
  - 正文引用: ✓
  - 备注: year 从 2024 改为 2025

[ugare2025itergen] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (ICLR 2025)
  - DOI/arXiv: ✓ (OpenReview ac93gRzxxV)
  - 正文引用: ✓
  - 备注: 无问题

[boostcd2025] ✓
  - 存在性: ✓
  - 作者: ✓ (Sakota 实际带变音 Šakota，BibTeX 未标但可接受)
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2025)
  - DOI/arXiv: ✓ (ACL Anthology 2025.emnlp-main.926)
  - 正文引用: ✓
  - 备注: 无问题

[luan2018scierc] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2018)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2018)
  - DOI/arXiv: ✓ (ACL Anthology D18-1360)
  - 正文引用: ✓
  - 备注: 无问题

[yao2019docred] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2019)
  - 标题: ✓
  - Venue: ✓ (ACL 2019)
  - DOI/arXiv: ✓ (ACL Anthology P19-1074)
  - 正文引用: ✓
  - 备注: 无问题

[wei2023zeroshot] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (arXiv:2302.10205)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[qwen2025qwen3] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (arXiv:2505.09388)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[zheng2024sglang] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (NeurIPS 2024, vol.37)
  - DOI/arXiv: ✓ (arXiv:2312.07104)
  - 正文引用: ✓
  - 备注: 无问题

[li2021document] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (NAACL 2021; booktitle 末尾多了 "(NAACL)" 但可接受)
  - DOI/arXiv: ✓ (ACL Anthology 2021.naacl-main.69)
  - 正文引用: ✓
  - 备注: 无问题

[guidex2025] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (Findings of ACL 2025)
  - DOI/arXiv: ✓ (ACL Anthology 2025.findings-acl.1245)
  - 正文引用: ✓
  - 备注: 无问题

[jsonschemabench2025] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2025)
  - 标题: ✓
  - Venue: ✓ (arXiv:2501.10868)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[wang2023instructuie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (arXiv:2304.08085)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[zhou2024universalner] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (ICLR 2024)
  - DOI/arXiv: ✓ (OpenReview r65xfUb76p)
  - 正文引用: ✓
  - 备注: 无问题

[wadhwa2023revisiting] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2023)
  - 标题: ✓
  - Venue: ✓ (ACL 2023 Long Papers)
  - DOI/arXiv: ✓ (DOI 10.18653/v1/2023.acl-long.868)
  - 正文引用: ✓
  - 备注: 无问题

[paolini2021tanl] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (ICLR 2021)
  - DOI/arXiv: ✓ (OpenReview US-TP-xnXI)
  - 正文引用: ✓
  - 备注: 无问题

[fei2022lasuie] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2022)
  - 标题: ✓
  - Venue: ✓ (NeurIPS 2022, vol.35)
  - DOI/arXiv: ✓ (arXiv:2304.06248)
  - 正文引用: ✓
  - 备注: 无问题

[riedel2010modeling] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2010)
  - 标题: ✓
  - Venue: ✓ (ECML PKDD 2010)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[anderson2017guided] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2017)
  - 标题: ✓
  - Venue: ✓ (EMNLP 2017)
  - DOI/arXiv: ✓
  - 正文引用: ✓
  - 备注: 无问题

[lu2021text2event] ✗✗ (严重)
  - 存在性: ✓
  - 作者: ✗ — 末位作者 "Shaobo Chen" 实为 "Shaoyi Chen"
  - 年份: ✓ (2021)
  - 标题: ✓
  - Venue: ✓ (ACL-IJCNLP 2021)
  - DOI/arXiv: ✗ — 页码错误：BibTeX 写 2722–2735，实际为 2795–2806
  - 正文引用: ✓
  - 备注: 两处必须修正

[luo2025kgtrie] ✗✗ (严重)
  - 存在性: ✓
  - 作者: ✓ (6人均正确)
  - 年份: ✓ (2025)
  - 标题: ✗✗ — 副标题完全错误！
    BibTeX: "...Faithful Knowledge Graph Rationale Generation for Knowledge-to-Text Generation"
    实际: "...Faithful Reasoning on Knowledge Graphs with Large Language Models"
  - Venue: ✓ (ICML 2025)
  - DOI/arXiv: ✓ (arXiv:2410.13080)
  - 正文引用: ✓
  - 备注: 标题必须修正

[vukovic2024dialogue] ✓
  - 存在性: ✓
  - 作者: ✓
  - 年份: ✓ (2024)
  - 标题: ✓
  - Venue: ✓ (SIGDIAL 2024)
  - DOI/arXiv: ✓ (arXiv:2408.02361)
  - 正文引用: ✓
  - 备注: 无问题
```

---

### 汇总

| 类别 | 数量 | 条目 |
|------|------|------|
| **确认无误** | **55** | 其余所有 |
| **必须修正** | **3** | luo2025kgtrie, lu2021text2event, ugare2024syncode |
| **建议修正** | **2** | tam2024letmespeak, ontologx_2025 |

### 必须修正的 3 条（按严重程度排序）

**1. `luo2025kgtrie` — 标题副标题完全错误（hallucinated subtitle）**
- 当前: `"Graph-Constrained Reasoning: Faithful Knowledge Graph Rationale Generation for Knowledge-to-Text Generation"`
- 正确: `"Graph-Constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models"`
- 来源: [arXiv:2410.13080](https://arxiv.org/abs/2410.13080)

**2. `lu2021text2event` — 作者名拼写错误 + 页码错误**
- 作者: `Shaobo Chen` → `Shaoyi Chen`
- 页码: `2722--2735` → `2795--2806`
- 来源: [ACL Anthology 2021.acl-long.217](https://aclanthology.org/2021.acl-long.217/)

**3. `ugare2024syncode` — 年份错误**
- 当前: `year = {2024}`
- 正确: `year = {2025}` (TMLR accepted 2025-06-16)
- 来源: [TMLR 官方推文](https://x.com/TmlrPub/status/1951447922060435673)

### 建议修正的 2 条

**4. `tam2024letmespeak` — 标题与 ACL Anthology 正式版不一致**
- BibTeX 用 arXiv 版标题: `"...on Performance of Large Language Models"`
- ACL Anthology 正式版: `"...On Large Language Model Performance."`
- 建议以正式发表版为准: [ACL Anthology](https://aclanthology.org/2024.emnlp-industry.91/)

**5. `ontologx_2025` — cite key 与 year 字段不一致**
- cite key 写 `ontologx_2025`，但 `year = {2026}`（对应期刊正式发表）
- 建议统一：改 cite key 为 `ontologx_2026` 或改 year 为 `2025`（引 arXiv 版）

---

**总计 60 条：55 条确认无误，3 条必须修正，2 条建议修正。无虚构论文（hallucinated paper）。所有 60 篇论文均真实存在。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-beta_20260526T101833"
}
```

</details>

---
