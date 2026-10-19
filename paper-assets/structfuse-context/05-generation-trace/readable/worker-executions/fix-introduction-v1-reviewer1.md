# fix introduction v1 reviewer1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_fix_introduction-v1-reviewer1_20260515T085237.log`
- **Structured JSON:** [`b3ad15973eb66e7dcaba.json`](../../sessions/b3/b3ad15973eb66e7dcaba.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
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
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "e854ea68-d9f4-4723-ace6-675f25010cce",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
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
    "resetsAt": 1778836200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1f76f583-cfea-4406-baf5-2612bb3289f6",
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two files and searching for the SWE-bench paper info in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "a56614ba-141e-4024-ad58-66cf7cd4fd69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDRF4HEWwnHjzNsiCHjHGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11543,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11543
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Read · `toolu_01R17rwL9nv8u8jNhu76epDs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "a7e3cae0-92ec-43fd-8eb9-85e9f161664f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDRF4HEWwnHjzNsiCHjHGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11543,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11543
      },
      "output_tokens": 27,
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

_source line 6 · 2026-05-15T08:52:50.021Z_

<details><summary>↩ Tool result · `toolu_01R17rwL9nv8u8jNhu76epDs`</summary>

```text
1	# 1. Introduction
2	
3	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
4	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
5	These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
6	Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
7	Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.
8	
9	In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
10	DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
11	These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
12	In the code domain, however, the picture is less clear.
13	CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''
14	This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?
15	
16	We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.
17	This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.
18	We operationalize this insight using CodeQL \cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.
19	Crucially, this structure-grounded mining is a \emph{training-time} intervention only, incurring zero additional inference cost.
20	This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \cite{liu2025codexgraph}, RANGER \cite{shah2025ranger}, and RepoGraph \cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.
21	
22	Our systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.
23	First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{lozhkov2024starcoder2} \textit{(pilot: 2 encoders $\times$ 3 strategies; M2 seed 43: full-scale replication)}.
24	This establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.
25	Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\ 0.80), respond differently to structural negatives.
26	We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.
27	
28	Our contributions are as follows:
29	
30	1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\% timeout rate, 78\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.
31	
32	2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.
33	
34	3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "b5744412-310b-4c13-ad2f-8f0e4e7acdc4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_016VMHFftigVaP6JsY16uCLY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "81711c99-e6a2-4bf8-9a9f-b625f61ad909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDRF4HEWwnHjzNsiCHjHGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11543,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11543
      },
      "output_tokens": 27,
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

_source line 8 · 2026-05-15T08:52:51.353Z_

<details><summary>↩ Tool result · `toolu_016VMHFftigVaP6JsY16uCLY`</summary>

```text
1	% =============================================================================
2	% Section 2.1: Code Retrieval Methods
3	% =============================================================================
4	
5	@article{robertson2009bm25,
6	  title={The Probabilistic Relevance Framework: {BM25} and Beyond},
7	  author={Robertson, Stephen and Zaragoza, Hugo},
8	  journal={Foundations and Trends in Information Retrieval},
9	  volume={3},
10	  number={4},
11	  pages={333--389},
12	  year={2009},
13	  publisher={Now Publishers}
14	}
15	
16	@inproceedings{karpukhin2020dpr,
17	  title={Dense Passage Retrieval for Open-Domain Question Answering},
18	  author={Karpukhin, Vladimir and O{\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},
19	  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
20	  pages={6769--6781},
21	  year={2020}
22	}
23	
24	@article{reddy2025swerank,
25	  title={{SweRank}: Software Issue Localization with Code Ranking},
26	  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},
27	  journal={arXiv preprint arXiv:2505.07849},
28	  year={2025}
29	}
30	
31	@inproceedings{xie2025swefixer,
32	  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},
33	  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},
34	  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
35	  pages={1123--1139},
36	  year={2025}
37	}
38	
39	@inproceedings{chen2025locagent,
40	  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},
41	  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},
42	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
43	  pages={8697--8727},
44	  year={2025}
45	}
46	
47	@article{shah2025ranger,
48	  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},
49	  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},
50	  journal={arXiv preprint arXiv:2509.25257},
51	  year={2025}
52	}
53	
54	@inproceedings{liu2025codexgraph,
55	  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},
56	  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},
57	  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
58	  pages={142--160},
59	  year={2025}
60	}
61	
62	@inproceedings{ouyang2025repograph,
63	  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},
64	  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},
65	  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
66	  year={2025}
67	}
68	
69	@inproceedings{liu2024graphcoder,
70	  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},
71	  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},
72	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
73	  year={2024}
74	}
75	
76	@article{seddik2026arise,
77	  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},
78	  author={Seddik, Shahd and Fard, Fatemeh},
79	  journal={arXiv preprint arXiv:2605.03117},
80	  year={2026}
81	}
82	
83	% =============================================================================
84	% Section 2.2: Pre-trained Code Representations and Contrastive Learning
85	% =============================================================================
86	
87	@inproceedings{feng2020codebert,
88	  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},
89	  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
90	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
91	  pages={1536--1547},
92	  year={2020}
93	}
94	
95	@inproceedings{guo2021graphcodebert,
96	  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},
97	  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
98	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
99	  year={2021}
100	}
101	
102	@inproceedings{guo2022unixcoder,
103	  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},
104	  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
105	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
106	  pages={7212--7225},
107	  year={2022}
108	}
109	
110	@inproceedings{alon2019code2vec,
111	  title={code2vec: Learning Distributed Representations of Code},
112	  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},
113	  booktitle={Proceedings of the ACM on Programming Languages (POPL)},
114	  volume={3},
115	  pages={1--29},
116	  year={2019}
117	}
118	
119	@inproceedings{zhang2024codesage,
120	  title={Code Representation Learning At Scale},
121	  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},
122	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
123	  year={2024}
124	}
125	
126	@inproceedings{reimers2019sentencebert,
127	  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
128	  author={Reimers, Nils and Gurevych, Iryna},
129	  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
130	  pages={3982--3992},
131	  year={2019}
132	}
133	
134	@inproceedings{jain2021contracode,
135	  title={Contrastive Code Representation Learning},
136	  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},
137	  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
138	  pages={5954--5971},
139	  year={2021}
140	}
141	
142	@inproceedings{li2022coderetriever,
143	  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},
144	  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
145	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
146	  pages={2898--2910},
147	  year={2022}
148	}
149	
150	@inproceedings{li2022scoder,
151	  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},
152	  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
153	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},
154	  year={2022}
155	}
156	
157	@inproceedings{ding2022programcontrasts,
158	  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},
159	  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},
160	  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
161	  pages={6300--6312},
162	  year={2022}
163	}
164	
165	@inproceedings{bui2021infercode,
166	  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},
167	  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},
168	  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},
169	  pages={1186--1197},
170	  year={2021}
171	}
172	
173	@article{lozhkov2024starcoder2,
174	  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},
175	  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},
176	  journal={arXiv preprint arXiv:2402.19173},
177	  year={2024}
178	}
179	
180	@article{hui2024qwen25coder,
181	  title={{Qwen2.5-Coder} Technical Report},
182	  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},
183	  journal={arXiv preprint arXiv:2409.12186},
184	  year={2024}
185	}
186	
187	% =============================================================================
188	% Section 2.3: Hard Negative Mining
189	% =============================================================================
190	
191	@inproceedings{chen2020simclr,
192	  title={A Simple Framework for Contrastive Learning of Visual Representations},
193	  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
194	  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},
195	  pages={1597--1607},
196	  year={2020}
197	}
198	
199	@inproceedings{xiong2021ance,
200	  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},
201	  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},
202	  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},
203	  year={2021}
204	}
205	
206	@inproceedings{zhan2021star,
207	  title={Optimizing Dense Retrieval Model Training with Hard Negatives},
208	  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},
209	  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
210	  pages={1503--1512},
211	  year={2021}
212	}
213	
214	@inproceedings{qu2021rocketqa,
215	  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},
216	  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},
217	  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},
218	  pages={5835--5847},
219	  year={2021}
220	}
221	
222	@inproceedings{zeng2022cldrd,
223	  title={Curriculum Learning for Dense Retrieval Distillation},
224	  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},
225	  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
226	  pages={1979--1983},
227	  year={2022}
228	}
229	
230	@article{fan2025cocohanere,
231	  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
232	  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},
233	  journal={ACM Transactions on Software Engineering and Methodology},
234	  volume={34},
235	  number={3},
236	  year={2025},
237	  publisher={ACM}
238	}
239	
240	% =============================================================================
241	% Section 2.4: Code Structure Analysis
242	% =============================================================================
243	
244	@article{ferrante1987pdg,
245	  title={The Program Dependence Graph and Its Use in Optimization},
246	  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},
247	  journal={ACM Transactions on Programming Languages and Systems},
248	  volume={9},
249	  number={3},
250	  pages={319--349},
251	  year={1987},
252	  publisher={ACM}
253	}
254	
255	@inproceedings{yamaguchi2014cpg,
256	  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},
257	  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},
258	  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\&P)},
259	  pages={590--604},
260	  year={2014},
261	  publisher={IEEE}
262	}
263	
264	@inproceedings{avgustinov2016ql,
265	  title={{QL}: Object-oriented Queries on Relational Data},
266	  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\"a}fer, Max},
267	  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},
268	  series={LIPIcs},
269	  volume={56},
270	  pages={2:1--2:25},
271	  year={2016}
272	}
273	
274	% =============================================================================
275	% Supplement: New citations added 2026-05-15
276	% =============================================================================
277	
278	@article{wang2021syncobert,
279	  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},
280	  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},
281	  journal={arXiv preprint arXiv:2108.04556},
282	  year={2021}
283	}
284	
285	@inproceedings{liu2023contrabert,
286	  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},
287	  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},
288	  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},
289	  pages={2476--2487},
290	  year={2023}
291	}
292	
293	@inproceedings{he2023capstone,
294	  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},
295	  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},
296	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
297	  pages={10531--10541},
298	  year={2023}
299	}
300	
301	@inproceedings{ding2023crosscodeeval,
302	  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},
303	  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},
304	  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},
305	  year={2023}
306	}
307	
308	@inproceedings{cummins2021programl,
309	  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},
310	  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},
311	  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},
312	  pages={2244--2253},
313	  year={2021},
314	  publisher={PMLR}
315	}
316	
317	@inproceedings{huang2021cosqa,
318	  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},
319	  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},
320	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
321	  pages={5690--5700},
322	  year={2021}
323	}
324	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "77c76eb9-c7c5-41ac-8c98-42913602c8fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}\n",
      "numLines": 324,
      "startLine": 1,
      "totalLines": 324
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ba4rhmwgMLV1TDBWV2o1hG`</summary>

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
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "2e3234cf-75eb-4f99-9efa-27b71c853d2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDRF4HEWwnHjzNsiCHjHGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11543,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11543
      },
      "output_tokens": 27,
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

_source line 10 · 2026-05-15T08:52:51.391Z_

<details><summary>↩ Tool result · `toolu_01Ba4rhmwgMLV1TDBWV2o1hG`</summary>

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
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "c4cb8ebb-09c7-436c-b9b9-f449b9c5503e",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files read. Let me search for the SWE-bench paper info to confirm the citation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "5589cbb1-e6be-4dc9-bc7a-6d55d31eadfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iBq5h2sjXFZxqjU9NtZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8236,
      "cache_read_input_tokens": 23384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8236
      },
      "output_tokens": 22,
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q58sJaagFvHcTK1m1cN4uh`</summary>

```json
{
  "query": "Jimenez SWE-bench Can Language Models Resolve Real-World GitHub Issues ICLR 2024",
  "allowed_domains": [
    "openreview.net",
    "arxiv.org",
    "dblp.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "4f8881af-56b6-449c-bee4-f53adfaf3b19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iBq5h2sjXFZxqjU9NtZNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8236,
      "cache_read_input_tokens": 23384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8236
      },
      "output_tokens": 22,
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

_source line 13 · 2026-05-15T08:53:02.514Z_

<details><summary>↩ Tool result · `toolu_01Q58sJaagFvHcTK1m1cN4uh`</summary>

```text
Web search results for query: "Jimenez SWE-bench Can Language Models Resolve Real-World GitHub Issues ICLR 2024"

Links: [{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"SWE-bench: Can Language Models Resolve Real-world Github Issues? | OpenReview","url":"https://openreview.net/forum?id=VTF8yNQM66"},{"title":"dblp: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://dblp.org/rec/journals/corr/abs-2310-06770.html"},{"title":"[2310.06770v3] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770v3"},{"title":"Presented at ICLR 2025 Workshop on Foundation Models in the Wild. AUTOMATED","url":"https://openreview.net/pdf?id=KzKuI0s2Op"},{"title":"[2310.06770v1] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770v1"},{"title":"MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue ReSolution Wei Tao","url":"https://arxiv.org/pdf/2403.17927"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://ar5iv.labs.arxiv.org/html/2310.06770"},{"title":"The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason","url":"https://arxiv.org/html/2506.12286v3"}]

Based on the search results, I found detailed information about the SWE-bench paper by Jimenez et al. from ICLR 2024:

## SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

The paper "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" was published as a conference paper at ICLR 2024 and was authored by Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan from Princeton University, Princeton Language and Intelligence, and the University of Chicago.

### Overview

The paper introduces SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories.

Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. The revised codebase is then evaluated using the repository's testing framework.

### Key Contributions

SWE-bench offers several advantages over existing LM programming benchmarks, including a realistic setting that utilizes user-submitted issues and solutions, diverse inputs featuring unique code problems from 12 repositories, a robust framework for execution-based evaluation, and the ability to continuously update the benchmark with new instances, requiring minimal human intervention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "5084293b-defb-43d5-b803-939f796de663",
  "tool_use_result": {
    "query": "Jimenez SWE-bench Can Language Models Resolve Real-World GitHub Issues ICLR 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_011xaLHNXMo9oUcd66NLjWtn",
        "content": [
          {
            "title": "[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
            "url": "https://arxiv.org/abs/2310.06770"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 SWE-BENCH:",
            "url": "https://arxiv.org/pdf/2310.06770"
          },
          {
            "title": "SWE-bench: Can Language Models Resolve Real-world Github Issues? | OpenReview",
            "url": "https://openreview.net/forum?id=VTF8yNQM66"
          },
          {
            "title": "dblp: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
            "url": "https://dblp.org/rec/journals/corr/abs-2310-06770.html"
          },
          {
            "title": "[2310.06770v3] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
            "url": "https://arxiv.org/abs/2310.06770v3"
          },
          {
            "title": "Presented at ICLR 2025 Workshop on Foundation Models in the Wild. AUTOMATED",
            "url": "https://openreview.net/pdf?id=KzKuI0s2Op"
          },
          {
            "title": "[2310.06770v1] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
            "url": "https://arxiv.org/abs/2310.06770v1"
          },
          {
            "title": "MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue ReSolution Wei Tao",
            "url": "https://arxiv.org/pdf/2403.17927"
          },
          {
            "title": "[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
            "url": "https://ar5iv.labs.arxiv.org/html/2310.06770"
          },
          {
            "title": "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason",
            "url": "https://arxiv.org/html/2506.12286v3"
          }
        ]
      },
      "Based on the search results, I found detailed information about the SWE-bench paper by Jimenez et al. from ICLR 2024:\n\n## SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\n\nThe paper \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\" was published as a conference paper at ICLR 2024 and was authored by Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan from Princeton University, Princeton Language and Intelligence, and the University of Chicago.\n\n### Overview\n\nThe paper introduces SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories.\n\nGiven a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. The revised codebase is then evaluated using the repository's testing framework.\n\n### Key Contributions\n\nSWE-bench offers several advantages over existing LM programming benchmarks, including a realistic setting that utilizes user-submitted issues and solutions, diverse inputs featuring unique code problems from 12 repositories, a robust framework for execution-based evaluation, and the ability to continuously update the benchmark with new instances, requiring minimal human intervention."
    ],
    "durationSeconds": 6.251409830000001
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the confirmed info. The authors are Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. Published at ICLR 2024.

Now let me apply all 6 fixes. Let me plan the edits:

**Fix 1**: Add bib entry for jimenez2024swebench to references.bib

**Fix 2**: "four negative mining strategies" → "three negative mining strategies (random, embedding-distance, and dataflow-aware)". 

I need to remove BM25 mentions throughout. On line 22, I'll change "four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware" to just the three strategies. For line 18, I need to check if the BM25 reference is part of the dataflow methodology description or a separate strategy mention—it seems to be describing how the dataflow approach works, so I should clarify that part carefully. Looking at the key distinction here—"突然出现" means these mentions need to stand out as abrupt introductions rather than integral parts of a strategy's description. In P4, BM25 is listed as one of four separate strategies, which clearly needs to be removed since we're consolidating the approach. But in P3, the BM25 reference is embedded within how the dataflow-aware method actually works, so it's describing implementation rather than introducing a new strategy.

I should change the P3 mention to something more neutral like "lexical similarity" to avoid confusion now that BM25 isn't a standalone strategy anymore. Then I need to update the contribution statements—both line 30 and line 32—to reflect that we're working with three strategies instead of four, and remove the explicit BM25 reference from the list. I need to reconsider the BM25 mention on line 18—while BM25 as a standalone mining strategy hasn't been trained, it's being used as a component within the dataflow-aware approach to rank files by lexical similarity, so I'll swap "BM25 similarity" for "lexical similarity" to avoid confusion. Then I need to update the strategy counts from four to three across lines 22 and 32, and replace the specific performance numbers on line 23 with placeholders since those results aren't finalized. I'm checking which phrases need to be updated—looking for exact matches of "zero additional computational cost" or "zero additional cost" throughout the document. Line 23 has an exact match, line 24 has a variant with "zero-cost baseline," and line 30 mentions "zero inference cost" which is close but not identical. Line 19's "zero additional inference cost" is similar but uses "inference" instead of "computational," so I need to determine if that counts as a match for the replacement task. I need to be more careful about which phrases actually match the task requirements. "Zero additional inference cost" isn't one of the exact phrases I'm supposed to replace, so I'll leave that alone. For line 23, "zero additional computational cost" is a direct match, so I'll change it to "negligible additional cost compared to random sampling." Line 24's "zero-cost baseline" needs updating to something like "strong low-cost baseline." Let me continue identifying the remaining instances that need revision. I'm planning out the edits to the introduction file carefully, making sure each old_string is unique so the replacements don't overlap. Starting with the BM25 terminology fix on line 18, then adjusting the negative mining strategies to remove BM25 from the list on line 22, and finally tackling the larger sentence on line 23 that needs multiple corrections about computational cost and the experimental results. I'm working through some edits to the paper text. For the baseline description, I need to clarify that embedding-distance mining doesn't require gradient computation—that's the key advantage. And I'm also reconsidering the contribution statement to focus on three core mining strategies rather than four, since BM25 might not be as central to the main narrative. I need to reorder the contributions to prioritize the systematic comparison as the main finding, move the pipeline to second place with updated language about inference cost, and position the representation geometry analysis third. Let me work through all the edits systematically to finalize the paper. Finishing the contributions section...

I need to update the encoder names in contribution 2 to reflect that StarCoder2 validation is still in progress, so I'll mention both encoders but note the ongoing validation work rather than listing them as fully complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "a1147ee9-f938-499e-b453-b8daddca64cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QChyGZo51DtMoy9h3omHJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 31620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1032
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

_source line 15_

SWE-bench 论文信息已确认。开始执行 6 项修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "8e20f43c-1bfc-4062-8fed-627bd90f661a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QChyGZo51DtMoy9h3omHJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 31620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1032
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01Sye7n67Dsz5yPEoH6BE4tS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
  "old_string": "then select negatives from structurally unreachable files ranked by BM25 similarity.",
  "new_string": "then select negatives from structurally unreachable files ranked by lexical similarity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "959d1007-a56e-40e5-98b6-5ceb3d9f0ede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QChyGZo51DtMoy9h3omHJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 31620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1032
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

_source line 17 · 2026-05-15T08:54:31.350Z_

<details><summary>↩ Tool result · `toolu_01Sye7n67Dsz5yPEoH6BE4tS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "96ed3093-72fe-494b-a6c8-abcbb60aecba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
    "oldString": "then select negatives from structurally unreachable files ranked by BM25 similarity.",
    "newString": "then select negatives from structurally unreachable files ranked by lexical similarity.",
    "originalFile": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " ",
          " We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.",
          " This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.",
          "-We operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by BM25 similarity.",
          "+We operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.",
          " Crucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.",
          " This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ha3BUdjeASPAot4ZA6NkAi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
  "old_string": "Our systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.",
  "new_string": "Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "b60d4c58-8336-49f2-afb8-2cc279223753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yXrp1tUG6jcJuQ2omKC2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 32652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4402
      },
      "output_tokens": 67,
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

_source line 19 · 2026-05-15T08:54:35.067Z_

<details><summary>↩ Tool result · `toolu_01Ha3BUdjeASPAot4ZA6NkAi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "e5d16de7-a29b-46d8-a11d-29f7c9c01040",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
    "oldString": "Our systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.",
    "newString": "Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.",
    "originalFile": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " Crucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.",
          " This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.",
          " ",
          "-Our systematic comparison of four negative mining strategies---random, embedding-distance, BM25, and dataflow-aware---across two decoder-only encoders yields the following findings.",
          "+Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.",
          " First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.",
          " This establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.",
          " Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01VVt8KARB9M6wGJ65CqP739`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
  "old_string": "First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.",
  "new_string": "First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "2d2beb5e-44bd-4823-99c8-3bb534361790",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnFCAfcKqup8hdxRoDYk4T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 37054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
      },
      "output_tokens": 72,
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

_source line 21 · 2026-05-15T08:54:40.578Z_

<details><summary>↩ Tool result · `toolu_01VVt8KARB9M6wGJ65CqP739`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "9b070761-b47c-4f74-beb4-76beb762eb20",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
    "oldString": "First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.",
    "newString": "First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.",
    "originalFile": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.\nThis establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 8,
        "newStart": 20,
        "newLines": 8,
        "lines": [
          " This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.",
          " ",
          " Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.",
          "-First, simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, with gains of +1.6--2.0 percentage points (pp) Recall@1 in pilot experiments and +0.52pp (best-by-R@1) / +0.82pp (mean fixed-checkpoint) in full-scale training with seed 43, across both Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{lozhkov2024starcoder2} \\textit{(pilot: 2 encoders $\\times$ 3 strategies; M2 seed 43: full-scale replication)}.",
          "-This establishes embedding-distance mining as a strong zero-cost baseline for future work on more sophisticated strategies.",
          "+First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete",
          "+This establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.",
          " Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.",
          " We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01W9dKqdZwzWQLzQWjuAX9VP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
  "old_string": "1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.",
  "new_string": "1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.\n\n3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "a45648cd-1235-449f-b618-1ddcd82290dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y5wuWgqjXnfmqBid7W8wp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 37329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 535
      },
      "output_tokens": 72,
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

_source line 23 · 2026-05-15T08:54:48.209Z_

<details><summary>↩ Tool result · `toolu_01W9dKqdZwzWQLzQWjuAX9VP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "d80567f8-def5-44c3-93c2-ec487fe9535e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
    "oldString": "1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.",
    "newString": "1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.\n\n3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.",
    "originalFile": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.\n\n2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
    "structuredPatch": [
      {
        "oldStart": 27,
        "oldLines": 8,
        "newStart": 27,
        "newLines": 8,
        "lines": [
          " ",
          " Our contributions are as follows:",
          " ",
          "-1. **A practical pipeline for structure-grounded hard negative mining** using CodeQL inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives at zero inference cost.",
          "+1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.",
          " ",
          "-2. **A systematic comparison of four negative mining strategies** (random, embedding-distance, BM25, dataflow-aware) across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.",
          "+2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.",
          " ",
          "-3. **An analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.",
          "+3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 24_

Now add the SWE-bench bib entry to references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "b7de03ed-d578-480f-bb9a-5d5923da2cad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKut3cJ7Bed7ucGeK4oN8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 37864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01EqW4QsKDWaGxNyUrMnEcU5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "old_string": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================",
  "new_string": "% =============================================================================\n% Section 1: Introduction\n% =============================================================================\n\n@inproceedings{jimenez2024swebench,\n  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},\n  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% ============================================================================="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "b5e96226-b0b1-48b7-a998-d675fe0b605b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKut3cJ7Bed7ucGeK4oN8f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 37864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 26 · 2026-05-15T08:54:54.669Z_

<details><summary>↩ Tool result · `toolu_01EqW4QsKDWaGxNyUrMnEcU5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "42d6fd61-14bf-46e2-af80-d962f15fc6ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
    "oldString": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================",
    "newString": "% =============================================================================\n% Section 1: Introduction\n% =============================================================================\n\n@inproceedings{jimenez2024swebench,\n  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},\n  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================",
    "originalFile": "% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},\n  number={4},\n  pages={333--389},\n  year={2009},\n  publisher={Now Publishers}\n}\n\n@inproceedings{karpukhin2020dpr,\n  title={Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Karpukhin, Vladimir and O{\\u{g}}uz, Barlas and Min, Sewon and Lewis, Patrick and Wu, Ledell and Edunov, Sergey and Chen, Danqi and Yih, Wen-tau},\n  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={6769--6781},\n  year={2020}\n}\n\n@article{reddy2025swerank,\n  title={{SweRank}: Software Issue Localization with Code Ranking},\n  author={Gangi Reddy, Revanth and Suresh, Tarun and Doo, JaeHyeok and Liu, Ye and Nguyen, Xuan Phi and Zhou, Yingbo and Yavuz, Semih and Xiong, Caiming and Ji, Heng and Joty, Shafiq},\n  journal={arXiv preprint arXiv:2505.07849},\n  year={2025}\n}\n\n@inproceedings{xie2025swefixer,\n  title={{SWE-Fixer}: Training Open-Source {LLM}s for Effective and Efficient {GitHub} Issue Resolution},\n  author={Xie, Chengxing and Li, Bowen and Gao, Chang and Du, He and Lam, Wai and Zou, Difan and Chen, Kai},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  pages={1123--1139},\n  year={2025}\n}\n\n@inproceedings{chen2025locagent,\n  title={{LocAgent}: Graph-Guided {LLM} Agents for Code Localization},\n  author={Chen, Zhaoling and Tang, Robert and Deng, Gangda and Wu, Fang and Wu, Jialong and Jiang, Zhiwei and Prasanna, Viktor and Cohan, Arman and Wang, Xingyao},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={8697--8727},\n  year={2025}\n}\n\n@article{shah2025ranger,\n  title={{RANGER}: Repository-Level Agent for Graph-Enhanced Retrieval},\n  author={Shah, Pratik and Ghosh, Rajat and Singhal, Aryan and Dutta, Debojyoti},\n  journal={arXiv preprint arXiv:2509.25257},\n  year={2025}\n}\n\n@inproceedings{liu2025codexgraph,\n  title={{CodexGraph}: Bridging Large Language Models and Code Repositories via Code Graph Databases},\n  author={Liu, Xiangyan and Lan, Bo and Hu, Zhiyuan and Liu, Yang and Zhang, Zhicheng and Wang, Fei and Shieh, Michael Qizhe and Zhou, Wenmeng},\n  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages={142--160},\n  year={2025}\n}\n\n@inproceedings{ouyang2025repograph,\n  title={{RepoGraph}: Enhancing {AI} Software Engineering with Repository-level Code Graph},\n  author={Ouyang, Siru and Yu, Wenhao and Ma, Kaixin and Xiao, Zilin and Zhang, Zhihan and Jia, Mengzhao and Han, Jiawei and Zhang, Hongming and Yu, Dong},\n  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{liu2024graphcoder,\n  title={{GraphCoder}: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model},\n  author={Liu, Wei and Hu, Ailun and Li, Yixuan and Li, Yichen and Liu, Haoyu and Yang, Leyi},\n  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},\n  year={2024}\n}\n\n@article{seddik2026arise,\n  title={{ARISE}: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair},\n  author={Seddik, Shahd and Fard, Fatemeh},\n  journal={arXiv preprint arXiv:2605.03117},\n  year={2026}\n}\n\n% =============================================================================\n% Section 2.2: Pre-trained Code Representations and Contrastive Learning\n% =============================================================================\n\n@inproceedings{feng2020codebert,\n  title={{CodeBERT}: A Pre-Trained Model for Programming and Natural Languages},\n  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},\n  pages={1536--1547},\n  year={2020}\n}\n\n@inproceedings{guo2021graphcodebert,\n  title={{GraphCodeBERT}: Pre-training Code Representations with Data Flow},\n  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shuai Kim and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{guo2022unixcoder,\n  title={{UniXcoder}: Unified Cross-Modal Pre-training for Code Representation},\n  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={7212--7225},\n  year={2022}\n}\n\n@inproceedings{alon2019code2vec,\n  title={code2vec: Learning Distributed Representations of Code},\n  author={Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},\n  booktitle={Proceedings of the ACM on Programming Languages (POPL)},\n  volume={3},\n  pages={1--29},\n  year={2019}\n}\n\n@inproceedings{zhang2024codesage,\n  title={Code Representation Learning At Scale},\n  author={Zhang, Dejiao and Ahmad, Wasi Uddin and Tan, Ming and Ding, Hantian and Nallapati, Ramesh and Roth, Dan and Ma, Xiaofei and Xiang, Bing},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{reimers2019sentencebert,\n  title={Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n  author={Reimers, Nils and Gurevych, Iryna},\n  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={3982--3992},\n  year={2019}\n}\n\n@inproceedings{jain2021contracode,\n  title={Contrastive Code Representation Learning},\n  author={Jain, Paras and Jain, Ajil and Zhang, Tianjun and Abbeel, Pieter and Gonzalez, Joseph and Stoica, Ion},\n  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={5954--5971},\n  year={2021}\n}\n\n@inproceedings{li2022coderetriever,\n  title={{CodeRetriever}: A Large Scale Contrastive Pre-Training Method for Code Search},\n  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={2898--2910},\n  year={2022}\n}\n\n@inproceedings{li2022scoder,\n  title={Soft-Labeled Contrastive Pre-training for Function-level Code Representation},\n  author={Li, Xiaonan and Guo, Daya and Gong, Yeyun and Lin, Yun and Shen, Yelong and Qiu, Xipeng and Jiang, Daxin and Chen, Weizhu and Duan, Nan},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year={2022}\n}\n\n@inproceedings{ding2022programcontrasts,\n  title={Towards Learning (Dis)-Similarity of Source Code from Program Contrasts},\n  author={Ding, Yangruibo and Buratti, Luca and Pujar, Saurabh and Morari, Alessandro and Ray, Baishakhi and Parthasarathy, Saikat},\n  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={6300--6312},\n  year={2022}\n}\n\n@inproceedings{bui2021infercode,\n  title={{InferCode}: Self-Supervised Learning of Code Representations by Predicting Subtrees},\n  author={Bui, Nghi D. Q. and Yu, Yijun and Jiang, Lingxiao},\n  booktitle={Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={1186--1197},\n  year={2021}\n}\n\n@article{lozhkov2024starcoder2,\n  title={{StarCoder} 2 and {The Stack} v2: The Next Generation},\n  author={Lozhkov, Anton and Li, Raymond and Ben Allal, Loubna and Cassano, Federico and Lamy-Poirier, Joel and Tazi, Nouamane and Tang, Ao and Pykhtar, Dmytro and Liu, Jiawei and Wei, Yuxiang and others},\n  journal={arXiv preprint arXiv:2402.19173},\n  year={2024}\n}\n\n@article{hui2024qwen25coder,\n  title={{Qwen2.5-Coder} Technical Report},\n  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Lu, Keming and Dang, Kai and Fan, Yang and Zhang, Yichang and Yang, An and Men, Rui and Huang, Fei and Zheng, Bo and others},\n  journal={arXiv preprint arXiv:2409.12186},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.3: Hard Negative Mining\n% =============================================================================\n\n@inproceedings{chen2020simclr,\n  title={A Simple Framework for Contrastive Learning of Visual Representations},\n  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},\n  booktitle={Proceedings of the 37th International Conference on Machine Learning (ICML)},\n  pages={1597--1607},\n  year={2020}\n}\n\n@inproceedings{xiong2021ance,\n  title={Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval},\n  author={Xiong, Lee and Xiong, Chenyan and Li, Ye and Tang, Kwok-Fung and Liu, Jialin and Bennett, Paul and Ahmed, Junaid and Overwijk, Arnold},\n  booktitle={Proceedings of the Ninth International Conference on Learning Representations (ICLR)},\n  year={2021}\n}\n\n@inproceedings{zhan2021star,\n  title={Optimizing Dense Retrieval Model Training with Hard Negatives},\n  author={Zhan, Jingtao and Mao, Jiaxin and Liu, Yiqun and Guo, Jiafeng and Zhang, Min and Ma, Shaoping},\n  booktitle={Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1503--1512},\n  year={2021}\n}\n\n@inproceedings{qu2021rocketqa,\n  title={{RocketQA}: An Optimized Training Approach to Dense Passage Retrieval for Open-Domain Question Answering},\n  author={Qu, Yingqi and Ding, Yuchen and Liu, Jing and Liu, Kai and Ren, Ruiyang and Zhao, Wayne Xin and Dong, Daxiang and Wu, Hua and Wang, Haifeng},\n  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT)},\n  pages={5835--5847},\n  year={2021}\n}\n\n@inproceedings{zeng2022cldrd,\n  title={Curriculum Learning for Dense Retrieval Distillation},\n  author={Zeng, Hansi and Zamani, Hamed and Vinay, Vishwa},\n  booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages={1979--1983},\n  year={2022}\n}\n\n@article{fan2025cocohanere,\n  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},\n  author={Fan, Ye and Li, Chuanyi and Ge, Jidong and Huang, LiGuo and Luo, Bin},\n  journal={ACM Transactions on Software Engineering and Methodology},\n  volume={34},\n  number={3},\n  year={2025},\n  publisher={ACM}\n}\n\n% =============================================================================\n% Section 2.4: Code Structure Analysis\n% =============================================================================\n\n@article{ferrante1987pdg,\n  title={The Program Dependence Graph and Its Use in Optimization},\n  author={Ferrante, Jeanne and Ottenstein, Karl J. and Warren, Joe D.},\n  journal={ACM Transactions on Programming Languages and Systems},\n  volume={9},\n  number={3},\n  pages={319--349},\n  year={1987},\n  publisher={ACM}\n}\n\n@inproceedings{yamaguchi2014cpg,\n  title={Modeling and Discovering Vulnerabilities with Code Property Graphs},\n  author={Yamaguchi, Fabian and Golde, Nico and Arp, Daniel and Rieck, Konrad},\n  booktitle={Proceedings of the 2014 IEEE Symposium on Security and Privacy (S\\&P)},\n  pages={590--604},\n  year={2014},\n  publisher={IEEE}\n}\n\n@inproceedings{avgustinov2016ql,\n  title={{QL}: Object-oriented Queries on Relational Data},\n  author={Avgustinov, Pavel and de Moor, Oege and Jones, Michael Peyton and Sch{\\\"a}fer, Max},\n  booktitle={30th European Conference on Object-Oriented Programming (ECOOP)},\n  series={LIPIcs},\n  volume={56},\n  pages={2:1--2:25},\n  year={2016}\n}\n\n% =============================================================================\n% Supplement: New citations added 2026-05-15\n% =============================================================================\n\n@article{wang2021syncobert,\n  title={{SynCoBERT}: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation},\n  author={Wang, Xin and Wang, Yasheng and Mi, Fei and Zhou, Pingyi and Wan, Yao and Liu, Xiao and Li, Li and Wu, Hao and Liu, Jin and Jiang, Xin},\n  journal={arXiv preprint arXiv:2108.04556},\n  year={2021}\n}\n\n@inproceedings{liu2023contrabert,\n  title={{ContraBERT}: Enhancing Code Pre-trained Models via Contrastive Learning},\n  author={Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng, Guozhu and Liu, Yang},\n  booktitle={Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE)},\n  pages={2476--2487},\n  year={2023}\n}\n\n@inproceedings{he2023capstone,\n  title={{CAPSTONE}: Curriculum Sampling for Dense Retrieval with Document Expansion},\n  author={He, Xingwei and Gong, Yeyun and Jin, A-Long and Zhang, Hang and Dong, Anlei and Jiao, Jian and Yiu, Siu Ming and Duan, Nan},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages={10531--10541},\n  year={2023}\n}\n\n@inproceedings{ding2023crosscodeeval,\n  title={{CrossCodeEval}: A Diverse and Multilingual Benchmark for Cross-File Code Completion},\n  author={Ding, Yangruibo and Wang, Zijian and Ahmad, Wasi Uddin and Ding, Hantian and Tan, Ming and Jain, Nihal and Ramanathan, Murali Krishna and Nallapati, Ramesh and Bhatia, Parminder and Roth, Dan and Xiang, Bing},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{cummins2021programl,\n  title={{ProGraML}: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations},\n  author={Cummins, Chris and Fisches, Zacharias V. and Ben-Nun, Tal and Hoefler, Torsten and O'Boyle, Michael F. P. and Leather, Hugh},\n  booktitle={Proceedings of the 38th International Conference on Machine Learning (ICML)},\n  pages={2244--2253},\n  year={2021},\n  publisher={PMLR}\n}\n\n@inproceedings{huang2021cosqa,\n  title={{CoSQA}: 20,000+ Web Queries for Code Search and Question Answering},\n  author={Huang, Junjie and Tang, Duyu and Shou, Linjun and Gong, Ming and Xu, Ke and Jiang, Daxin and Zhou, Ming and Duan, Nan},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages={5690--5700},\n  year={2021}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 4,
        "newStart": 1,
        "newLines": 15,
        "lines": [
          " % =============================================================================",
          "+% Section 1: Introduction",
          "+% =============================================================================",
          "+",
          "+@inproceedings{jimenez2024swebench,",
          "+  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},",
          "+  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},",
          "+  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},",
          "+  year={2024}",
          "+}",
          "+",
          "+% =============================================================================",
          " % Section 2.1: Code Retrieval Methods",
          " % =============================================================================",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 27_

验证两个文件的最终状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "08615c5d-ace4-4d97-b4f7-47389b2c27a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcDoceT53fCM3VpLta6ouu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 38569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_013e5zSfXWESwRRyrkecN6wr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "46cfbb36-4294-4ccb-9a90-55d18c16fd21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcDoceT53fCM3VpLta6ouu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 38569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 29 · 2026-05-15T08:54:57.778Z_

<details><summary>↩ Tool result · `toolu_013e5zSfXWESwRRyrkecN6wr`</summary>

```text
1	# 1. Introduction
2	
3	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
4	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
5	These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
6	Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
7	Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.
8	
9	In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
10	DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
11	These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
12	In the code domain, however, the picture is less clear.
13	CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''
14	This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?
15	
16	We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.
17	This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.
18	We operationalize this insight using CodeQL \cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.
19	Crucially, this structure-grounded mining is a \emph{training-time} intervention only, incurring zero additional inference cost.
20	This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \cite{liu2025codexgraph}, RANGER \cite{shah2025ranger}, and RepoGraph \cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.
21	
22	Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.
23	First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\% CI: [a, b]) on Qwen2.5-Coder-3B \cite{hui2024qwen25coder} (with StarCoder2-3B \cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete
24	This establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.
25	Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\ 0.80), respond differently to structural negatives.
26	We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.
27	
28	Our contributions are as follows:
29	
30	1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.
31	
32	2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\% timeout rate, 78\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.
33	
34	3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "1ba37bff-3f38-419f-8e85-fce2f553484a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.\n\n3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01CWSXCfGP28QdP4iVPeGoWW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "e4bda4ff-8cbe-48a6-89a9-8d05ceeaf8b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcDoceT53fCM3VpLta6ouu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 38569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 31 · 2026-05-15T08:54:58.097Z_

<details><summary>↩ Tool result · `toolu_01CWSXCfGP28QdP4iVPeGoWW`</summary>

```text
1	% =============================================================================
2	% Section 1: Introduction
3	% =============================================================================
4	
5	@inproceedings{jimenez2024swebench,
6	  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},
7	  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},
8	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
9	  year={2024}
10	}
11	
12	% =============================================================================
13	% Section 2.1: Code Retrieval Methods
14	% =============================================================================
15	
16	@article{robertson2009bm25,
17	  title={The Probabilistic Relevance Framework: {BM25} and Beyond},
18	  author={Robertson, Stephen and Zaragoza, Hugo},
19	  journal={Foundations and Trends in Information Retrieval},
20	  volume={3},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "64003109-b516-40d9-b04f-e31bf45ab121",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/references.bib",
      "content": "% =============================================================================\n% Section 1: Introduction\n% =============================================================================\n\n@inproceedings{jimenez2024swebench,\n  title={{SWE-bench}: Can Language Models Resolve Real-World {GitHub} Issues?},\n  author={Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% =============================================================================\n% Section 2.1: Code Retrieval Methods\n% =============================================================================\n\n@article{robertson2009bm25,\n  title={The Probabilistic Relevance Framework: {BM25} and Beyond},\n  author={Robertson, Stephen and Zaragoza, Hugo},\n  journal={Foundations and Trends in Information Retrieval},\n  volume={3},",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 335
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

6 项修正全部完成，验证通过：

| # | 修正 | 状态 |
|---|------|------|
| 1 | `jimenez2024swebench` bib entry | 已添加（ICLR 2024, 7 位作者） |
| 2 | BM25 策略删除 | four→three，contribution 列表已去除 BM25，P3 "BM25 similarity"→"lexical similarity" |
| 3 | 数字→placeholder | `+X.X pp across N random seeds (95% CI: [a, b])` + TODO 注释 |
| 4 | encoder claim | "on Qwen2.5-Coder-3B (with StarCoder2-3B validation in progress)" |
| 5 | Contribution 重排 | 1=systematic comparison, 2=CodeQL pipeline, 3=preliminary mechanistic analysis |
| 6 | zero cost 措辞 | P4→"negligible additional cost"，baseline→"requiring no gradient computation"，contributions→"without requiring gradient computation" |

注：P3 line 19 的 "zero additional inference cost" 保留未改——该处描述的是 training-time intervention 不增加推理开销，语义准确且与任务指定的 "zero additional computational cost" 不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "uuid": "29999307-8e43-49d6-a43d-7dd5898c5043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163Npxhr8eankbrJDUeyshx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1924,
      "cache_read_input_tokens": 39089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1924
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

_source line 33_

6 项修正全部完成，验证通过：

| # | 修正 | 状态 |
|---|------|------|
| 1 | `jimenez2024swebench` bib entry | 已添加（ICLR 2024, 7 位作者） |
| 2 | BM25 策略删除 | four→three，contribution 列表已去除 BM25，P3 "BM25 similarity"→"lexical similarity" |
| 3 | 数字→placeholder | `+X.X pp across N random seeds (95% CI: [a, b])` + TODO 注释 |
| 4 | encoder claim | "on Qwen2.5-Coder-3B (with StarCoder2-3B validation in progress)" |
| 5 | Contribution 重排 | 1=systematic comparison, 2=CodeQL pipeline, 3=preliminary mechanistic analysis |
| 6 | zero cost 措辞 | P4→"negligible additional cost"，baseline→"requiring no gradient computation"，contributions→"without requiring gradient computation" |

注：P3 line 19 的 "zero additional inference cost" 保留未改——该处描述的是 training-time intervention 不增加推理开销，语义准确且与任务指定的 "zero additional computational cost" 不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 140856,
  "duration_api_ms": 141823,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "6f04bf75-7636-41e5-81ea-4cdfa3ce5f6b",
  "total_cost_usd": 0.531644,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 29172,
    "cache_read_input_tokens": 289402,
    "output_tokens": 6971,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29172,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 349,
        "cache_read_input_tokens": 39089,
        "cache_creation_input_tokens": 1924,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1924
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 17868,
      "outputTokens": 482,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.030278,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 6971,
      "cacheReadInputTokens": 289402,
      "cacheCreationInputTokens": 29172,
      "webSearchRequests": 0,
      "costUSD": 0.501366,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "01976334-f6e3-46c3-a48d-670524a9802b"
}
```

</details>

---
