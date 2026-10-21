# research literature survey v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_research_literature_survey_v2_20260515T161104.log`
- **Structured JSON:** [`e76d843320d7b1831071.json`](../../sessions/e7/e76d843320d7b1831071.json)

## Before a recorded user message

91 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
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
  "uuid": "bb3715a1-ee40-4d3d-9b94-61778bf6f21b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778875200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9c43a32d-b276-4227-92c9-ac60e2e8b1c3",
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing references survey file, then search for the missing author information and new papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "66f737e2-7a24-4f4c-a092-b10b3422f216",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qtnWsrBvjAbmiwtCAaSnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 28,
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

_source line 5_

先读取现有文件，然后并行搜索缺失的作者信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d0f0574d-eec4-43b7-b4c7-140fe370692b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qtnWsrBvjAbmiwtCAaSnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 28,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01QhyDEPrkhCwecn2B2YN3v8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1d3084c3-3dba-4529-b0f7-6dd80b87918e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qtnWsrBvjAbmiwtCAaSnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11918,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11918
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-15T16:11:18.126Z_

<details><summary>↩ Tool result · `toolu_01QhyDEPrkhCwecn2B2YN3v8`</summary>

```text
1	# References Survey for Schema-DAG-Extraction
2	
3	> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)
4	
5	## Required References (14)
6	
7	### 1. LLM-PEE
8	- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction
9	- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
10	- **Venue**: EMNLP 2025 (Main)
11	- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/
12	- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.
13	- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.
14	
15	### 2. GoLLIE
16	- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction
17	- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre
18	- **Venue**: ICLR 2024
19	- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9
20	- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.
21	- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.
22	
23	### 3. GLiNER
24	- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer
25	- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois
26	- **Venue**: NAACL 2024
27	- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/
28	- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.
29	- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.
30	
31	### 4. IEPile
32	- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus
33	- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen
34	- **Venue**: ACL 2024 (Short)
35	- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/
36	- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.
37	- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.
38	
39	### 5. CrossAgentIE
40	- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction
41	- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang
42	- **Venue**: ACL 2025 Findings
43	- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG
44	- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.
45	- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.
46	
47	### 6. InstructUIE
48	- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction
49	- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du
50	- **Venue**: arXiv 2023 (preprint)
51	- **arXiv/DOI**: arXiv:2304.08085
52	- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.
53	- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.
54	
55	### 7. KGGen
56	- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models
57	- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo
58	- **Venue**: NeurIPS 2025
59	- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi
60	- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.
61	- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.
62	
63	### 8. Ethayarajh (2019) — Contextual Anisotropy
64	- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings
65	- **Authors**: Kawin Ethayarajh
66	- **Venue**: EMNLP-IJCNLP 2019
67	- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/
68	- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.
69	- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.
70	
71	### 9. Gao et al. (2019) — Representation Degeneration
72	- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models
73	- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu
74	- **Venue**: ICLR 2019
75	- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm
76	- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.
77	- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.
78	
79	### 10. LLM4IE Survey
80	- **Full title**: Large Language Models for Generative Information Extraction: A Survey
81	- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen
82	- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024
83	- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y
84	- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.
85	- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.
86	
87	### 11. UniNER
88	- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition
89	- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon
90	- **Venue**: ICLR 2024
91	- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p
92	- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.
93	- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.
94	
95	### 12. CMAS-NER
96	- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition
97	- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren
98	- **Venue**: TheWebConf (WWW) 2025
99	- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923
100	- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.
101	- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.
102	
103	### 13. KnowCoder
104	- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction
105	- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
106	- **Venue**: ACL 2024 (Long)
107	- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/
108	- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.
109	- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.
110	
111	### 14. Lost in the Middle
112	- **Full title**: Lost in the Middle: How Language Models Use Long Contexts
113	- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
114	- **Venue**: TACL 2024, vol. 12, pp. 157-173
115	- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638
116	- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.
117	- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.
118	
119	---
120	
121	## Additional References (7)
122	
123	### 15. CodeIE
124	- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors
125	- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu
126	- **Venue**: ACL 2023 (Long)
127	- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/
128	- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.
129	- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.
130	
131	### 16. ADELIE
132	- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction
133	- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li
134	- **Venue**: EMNLP 2024 (Main)
135	- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/
136	- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.
137	- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.
138	
139	### 17. Decompose, Enrich, and Extract! (DEE)
140	- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs
141	- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li
142	- **Venue**: IEEE ICTAI 2024
143	- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/
144	- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.
145	- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.
146	
147	### 18. OneKE
148	- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System
149	- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen
150	- **Venue**: WWW 2025 (Companion)
151	- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189
152	- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.
153	- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.
154	
155	### 19. Schema as Parameterized Tools (SPT)
156	- **Full title**: Schema as Parameterized Tools for Universal Information Extraction
157	- **Authors**: (arXiv 2025)
158	- **Venue**: arXiv preprint, June 2025
159	- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa
160	- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.
161	- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.
162	
163	### 20. PARSE
164	- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction
165	- **Authors**: (Amazon Science, 2025)
166	- **Venue**: arXiv preprint, October 2025
167	- **arXiv/DOI**: arXiv:2510.08623
168	- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.
169	- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.
170	
171	### 21. Familiarity: Zero-Shot NER Label Shift
172	- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data
173	- **Authors**: (arXiv, December 2024)
174	- **arXiv/DOI**: arXiv:2412.10121
175	- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.
176	- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.
177	
178	---
179	
180	## Summary Statistics
181	- Total references found: **14/14 required + 7 additional = 21 total**
182	- Not found: None — all 14 required papers verified via web search
183	- Coverage by relation type:
184	  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)
185	  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)
186	  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "9f9e3c70-6682-460b-8349-749fdbc9d6b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
      "content": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: (arXiv 2025)\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: (Amazon Science, 2025)\n- **Venue**: arXiv preprint, October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
      "numLines": 187,
      "startLine": 1,
      "totalLines": 187
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wn12wRaNQ8fPDjTRTk5R3E`</summary>

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
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "3b44e909-daeb-4ffa-a7c7-fc8c84039bbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SB7NfYcAE1yEGnSuDgakXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5978,
      "cache_read_input_tokens": 23759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5978
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

_source line 9 · 2026-05-15T16:11:20.279Z_

<details><summary>↩ Tool result · `toolu_01Wn12wRaNQ8fPDjTRTk5R3E`</summary>

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
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d9513ce9-e989-438a-aa8d-16ae773ef62f",
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

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the three incomplete citations in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "42a217d0-6532-4bae-a5e0-cfe87a25da00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6D5dusguNiNBV9d542TW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 29737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 18,
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

_source line 11_

并行搜索 3 篇不完整引用的作者信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "01e14457-4692-4809-b34e-6436355123ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6D5dusguNiNBV9d542TW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 29737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FSTntdDX6PDx94bVNfhqdz`</summary>

```json
{
  "query": "Schema as Parameterized Tools Universal Information Extraction arXiv 2506.01276 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "81c23059-f428-447d-ac6d-ee144e36f351",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6D5dusguNiNBV9d542TW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 29737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
      },
      "output_tokens": 18,
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

_source line 13 · 2026-05-15T16:11:27.646Z_

<details><summary>↩ Tool result · `toolu_01FSTntdDX6PDx94bVNfhqdz`</summary>

```text
Web search results for query: "Schema as Parameterized Tools Universal Information Extraction arXiv 2506.01276 authors"

Links: [{"title":"[2506.01276] Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/abs/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information ...","url":"https://arxiv.org/pdf/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/html/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction | OpenReview","url":"https://openreview.net/forum?id=r1QGqAOBxa"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://openreview.net/pdf?id=yoPtjKVtoX"},{"title":"[Literature Review] Schema as Parameterized Tools for Universal Information Extraction","url":"https://www.themoonlight.io/en/review/schema-as-parameterized-tools-for-universal-information-extraction"},{"title":"Schema-Driven Information Extraction from Heterogeneous Tables","url":"https://arxiv.org/html/2305.14336v3"},{"title":"[2301.03282] Universal Information Extraction as Unified Semantic Matching","url":"https://arxiv.org/abs/2301.03282"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/html/2403.07969v2"},{"title":"[2304.14770] RexUIE: A Recursive Method with Explicit Schema Instructor for Universal Information Extraction","url":"https://arxiv.org/abs/2304.14770"}]

Based on the search results, the authors of arXiv paper 2506.01276 "Schema as Parameterized Tools for Universal Information Extraction" are Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, and Yong Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "bfdbb827-fa45-4e1a-b43e-b5f16e18e991",
  "tool_use_result": {
    "query": "Schema as Parameterized Tools Universal Information Extraction arXiv 2506.01276 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GUoXam8mdgMDbU4U5Ufm9y",
        "content": [
          {
            "title": "[2506.01276] Schema as Parameterized Tools for Universal Information Extraction",
            "url": "https://arxiv.org/abs/2506.01276"
          },
          {
            "title": "Schema as Parameterized Tools for Universal Information ...",
            "url": "https://arxiv.org/pdf/2506.01276"
          },
          {
            "title": "Schema as Parameterized Tools for Universal Information Extraction",
            "url": "https://arxiv.org/html/2506.01276"
          },
          {
            "title": "Schema as Parameterized Tools for Universal Information Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=r1QGqAOBxa"
          },
          {
            "title": "Schema as Parameterized Tools for Universal Information Extraction",
            "url": "https://openreview.net/pdf?id=yoPtjKVtoX"
          },
          {
            "title": "[Literature Review] Schema as Parameterized Tools for Universal Information Extraction",
            "url": "https://www.themoonlight.io/en/review/schema-as-parameterized-tools-for-universal-information-extraction"
          },
          {
            "title": "Schema-Driven Information Extraction from Heterogeneous Tables",
            "url": "https://arxiv.org/html/2305.14336v3"
          },
          {
            "title": "[2301.03282] Universal Information Extraction as Unified Semantic Matching",
            "url": "https://arxiv.org/abs/2301.03282"
          },
          {
            "title": "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction",
            "url": "https://arxiv.org/html/2403.07969v2"
          },
          {
            "title": "[2304.14770] RexUIE: A Recursive Method with Explicit Schema Instructor for Universal Information Extraction",
            "url": "https://arxiv.org/abs/2304.14770"
          }
        ]
      },
      "Based on the search results, the authors of arXiv paper 2506.01276 \"Schema as Parameterized Tools for Universal Information Extraction\" are Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, and Yong Liu."
    ],
    "durationSeconds": 3.8840931550000004
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CqLtrzsUnvtvGTthaVSx1E`</summary>

```json
{
  "query": "PARSE LLM Driven Schema Optimization Entity Extraction arXiv 2510.08623 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "e6a966c7-8893-4558-8dcf-4e9471f3fb45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MCiuGHd3bnWZfrevAPa9Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 30339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dn2Pr7iVv7eVecwwYX3S3W`</summary>

```json
{
  "query": "Familiarity Better Evaluation Zero-Shot Named Entity Recognition arXiv 2412.10121 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d52ad390-7579-4d22-9d3e-eab662a52c57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MCiuGHd3bnWZfrevAPa9Br",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 30339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
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

_source line 16 · 2026-05-15T16:11:34.022Z_

<details><summary>↩ Tool result · `toolu_01CqLtrzsUnvtvGTthaVSx1E`</summary>

```text
Web search results for query: "PARSE LLM Driven Schema Optimization Entity Extraction arXiv 2510.08623 authors"

Links: [{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"(PDF) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://www.researchgate.net/publication/396458126_PARSE_LLM_Driven_Schema_Optimization_for_Reliable_Entity_Extraction"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13775&show=25"},{"title":"PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science","url":"https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3600&show=250"},{"title":"LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://ribbitribbit.co/paper/arxiv.2510.08623-PARSE-LLM-Driven-Schema-Optimization-for-Reliable-Entity"},{"title":"Machine Learning","url":"https://web3.arxiv.org/list/cs.LG/recent?skip=175&show=100"},{"title":"Bytez","url":"https://bytez.com/docs/arxiv/2510.08623/paper"},{"title":"Parse: LLM Driven Schema Optimization for Reliable Entity Extraction | Hacker News","url":"https://news.ycombinator.com/item?id=45683970"}]

Based on the search results, here are the authors of the arXiv paper 2510.08623 "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction":

The authors are Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, and Promod Yenigalla. 

The paper was submitted for the EMNLP 2025 Industry Track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "9a162f6d-4648-427d-912c-63ee9e1572e5",
  "tool_use_result": {
    "query": "PARSE LLM Driven Schema Optimization Entity Extraction arXiv 2510.08623 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AUUwDkvCua3FP7LNHx4UXh",
        "content": [
          {
            "title": "[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://arxiv.org/abs/2510.08623"
          },
          {
            "title": "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://arxiv.org/html/2510.08623v1"
          },
          {
            "title": "(PDF) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://www.researchgate.net/publication/396458126_PARSE_LLM_Driven_Schema_Optimization_for_Reliable_Entity_Extraction"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=13775&show=25"
          },
          {
            "title": "PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science",
            "url": "https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=3600&show=250"
          },
          {
            "title": "LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://ribbitribbit.co/paper/arxiv.2510.08623-PARSE-LLM-Driven-Schema-Optimization-for-Reliable-Entity"
          },
          {
            "title": "Machine Learning",
            "url": "https://web3.arxiv.org/list/cs.LG/recent?skip=175&show=100"
          },
          {
            "title": "Bytez",
            "url": "https://bytez.com/docs/arxiv/2510.08623/paper"
          },
          {
            "title": "Parse: LLM Driven Schema Optimization for Reliable Entity Extraction | Hacker News",
            "url": "https://news.ycombinator.com/item?id=45683970"
          }
        ]
      },
      "Based on the search results, here are the authors of the arXiv paper 2510.08623 \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\":\n\nThe authors are Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, and Promod Yenigalla. \n\nThe paper was submitted for the EMNLP 2025 Industry Track."
    ],
    "durationSeconds": 3.4514138810000006
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T16:11:36.433Z_

<details><summary>↩ Tool result · `toolu_01Dn2Pr7iVv7eVecwwYX3S3W`</summary>

```text
Web search results for query: "Familiarity Better Evaluation Zero-Shot Named Entity Recognition arXiv 2412.10121 authors"

Links: [{"title":"[2412.10121] Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/abs/2412.10121"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/html/2412.10121v1"},{"title":"(PDF) Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://www.researchgate.net/publication/387078555_Familiarity_Better_Evaluation_of_Zero-Shot_Named_Entity_Recognition_by_Quantifying_Label_Shifts_in_Synthetic_Training_Data"},{"title":"GitHub - flairNLP/familiarity: Label shift estimation for transfer difficulty with Familiarity.","url":"https://github.com/flairNLP/familiarity"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.37/"},{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models","url":"https://arxiv.org/html/2311.08921v3"},{"title":"llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models","url":"https://arxiv.org/html/2406.04528v1"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"[2407.04629] Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework","url":"https://arxiv.org/abs/2407.04629"},{"title":"Improving Few-Shot Named Entity Recognition with Causal ...","url":"https://ieeexplore.ieee.org/iel8/8254253/10778131/10742264.pdf"}]

The authors of arXiv paper 2412.10121 "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data" are Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, and Alan Akbik.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "a96efc7b-99c1-4400-979a-c45139b61537",
  "tool_use_result": {
    "query": "Familiarity Better Evaluation Zero-Shot Named Entity Recognition arXiv 2412.10121 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LezetU2r1B1RoptaDUhNvF",
        "content": [
          {
            "title": "[2412.10121] Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data",
            "url": "https://arxiv.org/abs/2412.10121"
          },
          {
            "title": "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data",
            "url": "https://arxiv.org/html/2412.10121v1"
          },
          {
            "title": "(PDF) Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data",
            "url": "https://www.researchgate.net/publication/387078555_Familiarity_Better_Evaluation_of_Zero-Shot_Named_Entity_Recognition_by_Quantifying_Label_Shifts_in_Synthetic_Training_Data"
          },
          {
            "title": "GitHub - flairNLP/familiarity: Label shift estimation for transfer difficulty with Familiarity.",
            "url": "https://github.com/flairNLP/familiarity"
          },
          {
            "title": "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data - ACL Anthology",
            "url": "https://aclanthology.org/2025.naacl-long.37/"
          },
          {
            "title": "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models",
            "url": "https://arxiv.org/html/2311.08921v3"
          },
          {
            "title": "llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models",
            "url": "https://arxiv.org/html/2406.04528v1"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "[2407.04629] Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework",
            "url": "https://arxiv.org/abs/2407.04629"
          },
          {
            "title": "Improving Few-Shot Named Entity Recognition with Causal ...",
            "url": "https://ieeexplore.ieee.org/iel8/8254253/10778131/10742264.pdf"
          }
        ]
      },
      "The authors of arXiv paper 2412.10121 \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\" are Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, and Alan Akbik."
    ],
    "durationSeconds": 4.987481609999999
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all three author lists:
1. SPT (#19): Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu
2. PARSE (#20): Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
3. Familiarity (#21): Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik

Let me also check venues more carefully. 

I've confirmed the venues: SPT appeared on OpenReview, PARSE was submitted to EMNLP 2025's Industry Track, and Familiarity was published at NAACL 2025. Now I need to search for 8-10 papers across all four directions in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "0a05c8ca-a152-473b-a930-c295d737638d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 19_

3 篇作者信息已找到。现在并行搜索 4 个方向的论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "083ba884-58e0-44e8-bab0-9eb4ec61e4ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TvKGiLQ9E7oifLQjAZ8kMY`</summary>

```json
{
  "query": "GENRE autoregressive entity linking constrained generation De Cao 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "59542be0-d7e3-48bb-840d-fded70be376a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TqwqkxnA7VYr64atBunaaz`</summary>

```json
{
  "query": "structured decoding constrained generation named entity recognition information extraction 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "80e478b1-dd7d-425c-b195-b2f3fd80c906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AegdMAhtPAnbpHE9D5ZP3J`</summary>

```json
{
  "query": "label noise named entity recognition annotation disagreement NER evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "b2fb63ec-e4ae-4337-95bb-1cb7bb03e46d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KKFSG4rPTcq5KKvmcHBJfX`</summary>

```json
{
  "query": "fine-grained entity typing label ambiguity type confusion hierarchy 2019 2020 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "cbd9357e-c0a3-472f-827d-dbb35af50851",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9jd1zkRKtuPiZsDNXXun4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 31007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 24 · 2026-05-15T16:11:50.565Z_

<details><summary>↩ Tool result · `toolu_01TvKGiLQ9E7oifLQjAZ8kMY`</summary>

```text
Web search results for query: "GENRE autoregressive entity linking constrained generation De Cao 2021"

Links: [{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://openreview.net/pdf?id=5k8F6UU39V"},{"title":"Multilingual Autoregressive Entity Linking | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00460/110051/Multilingual-Autoregressive-Entity-Linking"},{"title":"Highly Parallel Autoregressive Entity Linking with ...","url":"https://aclanthology.org/2021.emnlp-main.604.pdf"},{"title":"[2010.00904] Autoregressive Entity Retrieval","url":"https://arxiv.org/abs/2010.00904"},{"title":"[2103.12528] Multilingual Autoregressive Entity Linking","url":"https://arxiv.org/abs/2103.12528"},{"title":"[2112.08340] GenIE: Generative Information Extraction - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2112.08340"},{"title":"Highly Parallel Autoregressive Entity Linking with Discriminative Correction - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.604/"},{"title":"ICLR Spotlight Autoregressive Entity Retrieval","url":"https://iclr.cc/virtual/2021/spotlight/3521"},{"title":"Highly Parallel Autoregressive Entity Linking with Discriminative Correction | Request PDF","url":"https://www.researchgate.net/publication/357122777_Highly_Parallel_Autoregressive_Entity_Linking_with_Discriminative_Correction"}]

Based on the search results, here's what I found about GENRE:

## Overview

GENRE (Generative ENtity REtrieval) is a system for autoregressive entity retrieval implemented in PyTorch. It is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion and conditioned on the context.

## Key Technical Approach

GENRE uses a sequence-to-sequence approach to entity retrieval based on fine-tuned BART architecture. The core innovation is how it handles constrained generation: GENRE performs retrieval by generating the unique entity name conditioned on the input text using constrained beam search to only generate valid identifiers.

## Constrained Generation Strategy

To solve the problem of generating invalid entity names, GENRE employs a constrained decoding strategy that forces each generated name to be in a predefined candidate set. More specifically, this constraint is defined in terms of a prefix tree (trie).

## Key Advantages

The autoregressive formulation directly captures relations between context and entity name, effectively cross encoding both; the memory footprint is greatly reduced because the parameters scale with vocabulary size, not entity count; and the softmax loss is computed without subsampling negative data.

The paper was published at ICLR 2021 with authors Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d1a079b1-e7ba-484e-8b3e-16f40948f6b4",
  "tool_use_result": {
    "query": "GENRE autoregressive entity linking constrained generation De Cao 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_016zLJ8kU916kEHUVu25bjS2",
        "content": [
          {
            "title": "GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub",
            "url": "https://github.com/facebookresearch/GENRE"
          },
          {
            "title": "Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL",
            "url": "https://openreview.net/pdf?id=5k8F6UU39V"
          },
          {
            "title": "Multilingual Autoregressive Entity Linking | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00460/110051/Multilingual-Autoregressive-Entity-Linking"
          },
          {
            "title": "Highly Parallel Autoregressive Entity Linking with ...",
            "url": "https://aclanthology.org/2021.emnlp-main.604.pdf"
          },
          {
            "title": "[2010.00904] Autoregressive Entity Retrieval",
            "url": "https://arxiv.org/abs/2010.00904"
          },
          {
            "title": "[2103.12528] Multilingual Autoregressive Entity Linking",
            "url": "https://arxiv.org/abs/2103.12528"
          },
          {
            "title": "[2112.08340] GenIE: Generative Information Extraction - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/2112.08340"
          },
          {
            "title": "Highly Parallel Autoregressive Entity Linking with Discriminative Correction - ACL Anthology",
            "url": "https://aclanthology.org/2021.emnlp-main.604/"
          },
          {
            "title": "ICLR Spotlight Autoregressive Entity Retrieval",
            "url": "https://iclr.cc/virtual/2021/spotlight/3521"
          },
          {
            "title": "Highly Parallel Autoregressive Entity Linking with Discriminative Correction | Request PDF",
            "url": "https://www.researchgate.net/publication/357122777_Highly_Parallel_Autoregressive_Entity_Linking_with_Discriminative_Correction"
          }
        ]
      },
      "Based on the search results, here's what I found about GENRE:\n\n## Overview\n\nGENRE (Generative ENtity REtrieval) is a system for autoregressive entity retrieval implemented in PyTorch. It is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion and conditioned on the context.\n\n## Key Technical Approach\n\nGENRE uses a sequence-to-sequence approach to entity retrieval based on fine-tuned BART architecture. The core innovation is how it handles constrained generation: GENRE performs retrieval by generating the unique entity name conditioned on the input text using constrained beam search to only generate valid identifiers.\n\n## Constrained Generation Strategy\n\nTo solve the problem of generating invalid entity names, GENRE employs a constrained decoding strategy that forces each generated name to be in a predefined candidate set. More specifically, this constraint is defined in terms of a prefix tree (trie).\n\n## Key Advantages\n\nThe autoregressive formulation directly captures relations between context and entity name, effectively cross encoding both; the memory footprint is greatly reduced because the parameters scale with vocabulary size, not entity count; and the softmax loss is computed without subsampling negative data.\n\nThe paper was published at ICLR 2021 with authors Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni."
    ],
    "durationSeconds": 7.109990338000003
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T16:11:53.376Z_

<details><summary>↩ Tool result · `toolu_01AegdMAhtPAnbpHE9D5ZP3J`</summary>

```text
Web search results for query: "label noise named entity recognition annotation disagreement NER evaluation"

Links: [{"title":"NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition","url":"https://arxiv.org/html/2405.07609v1"},{"title":"[2405.07609] NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition","url":"https://arxiv.org/abs/2405.07609"},{"title":"Named Entity Recognition: Entity Types, BIO Tagging & Evaluation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/named-entity-recognition-ner-tutorial"},{"title":"NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1011/"},{"title":"DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition","url":"https://arxiv.org/html/2604.15866"},{"title":"A review of named entity recognition: from learning ...","url":"https://sentic.net/named-entity-recognition.pdf"},{"title":"SANTA: Separate Strategies for Inaccurate and Incomplete Annotation Noise in Distantly-Supervised Named Entity Recognition","url":"https://arxiv.org/html/2305.04076"},{"title":"Evaluating NLP for Named Entity Recognition, Part 2: Annotating and Scoring | Babel Street","url":"https://www.babelstreet.com/blog/evaluating-nlp-annotating-evaluation-data-and-scoring-results"},{"title":"Named Entity Recognition · Prodigy · An annotation tool for AI, Machine Learning & NLP","url":"https://prodi.gy/docs/named-entity-recognition"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"}]

Here are the search results for your query on label noise, named entity recognition, annotation disagreement, and NER evaluation:

## Key Findings:

**Label Noise in NER:**
Available training data for named entity recognition (NER) often contains a significant percentage of incorrect labels for entity types and entity boundaries, and such label noise poses challenges for supervised learning and may significantly deteriorate model quality.

**Types of Noise:**
NoiseBench introduces an NER benchmark consisting of clean training data corrupted with 6 types of real noise, including expert errors, crowdsourcing errors, automatic annotation errors and LLM errors.

**Annotation Disagreement:**
Label noise can result from incorrect or inconsistent gold annotations, such as when "Smith" is annotated as PER in 90% of training examples but O in 10% because annotators disagreed about whether to tag common surnames without first names. Inter-annotator disagreement during corpus construction propagates into the training data, and when two annotators choose different boundaries for the same span, a model trained on their combined labels learns an inconsistent mapping.

**Real vs. Simulated Noise:**
Approaches are typically evaluated using simulated noise where labels in a clean dataset are automatically corrupted, but this leads to unrealistic noise that is far easier to handle than real noise caused by human error or semi-automatic annotation.

**Existing Datasets:**
Other NER datasets have also been found to contain a share of incorrect labels, with Ontonotes4 estimated around 8% and WNUT-17 around 18%.

The search results show active research in addressing label noise challenges through benchmarking and noise-robust learning approaches for NER systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "43828dd1-3378-4d92-ae22-f46087feea33",
  "tool_use_result": {
    "query": "label noise named entity recognition annotation disagreement NER evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KNUADruwnfdgHhAGHQePXT",
        "content": [
          {
            "title": "NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition",
            "url": "https://arxiv.org/html/2405.07609v1"
          },
          {
            "title": "[2405.07609] NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition",
            "url": "https://arxiv.org/abs/2405.07609"
          },
          {
            "title": "Named Entity Recognition: Entity Types, BIO Tagging & Evaluation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/named-entity-recognition-ner-tutorial"
          },
          {
            "title": "NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.1011/"
          },
          {
            "title": "DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition",
            "url": "https://arxiv.org/html/2604.15866"
          },
          {
            "title": "A review of named entity recognition: from learning ...",
            "url": "https://sentic.net/named-entity-recognition.pdf"
          },
          {
            "title": "SANTA: Separate Strategies for Inaccurate and Incomplete Annotation Noise in Distantly-Supervised Named Entity Recognition",
            "url": "https://arxiv.org/html/2305.04076"
          },
          {
            "title": "Evaluating NLP for Named Entity Recognition, Part 2: Annotating and Scoring | Babel Street",
            "url": "https://www.babelstreet.com/blog/evaluating-nlp-annotating-evaluation-data-and-scoring-results"
          },
          {
            "title": "Named Entity Recognition · Prodigy · An annotation tool for AI, Machine Learning & NLP",
            "url": "https://prodi.gy/docs/named-entity-recognition"
          },
          {
            "title": "A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11321-8"
          }
        ]
      },
      "Here are the search results for your query on label noise, named entity recognition, annotation disagreement, and NER evaluation:\n\n## Key Findings:\n\n**Label Noise in NER:**\nAvailable training data for named entity recognition (NER) often contains a significant percentage of incorrect labels for entity types and entity boundaries, and such label noise poses challenges for supervised learning and may significantly deteriorate model quality.\n\n**Types of Noise:**\nNoiseBench introduces an NER benchmark consisting of clean training data corrupted with 6 types of real noise, including expert errors, crowdsourcing errors, automatic annotation errors and LLM errors.\n\n**Annotation Disagreement:**\nLabel noise can result from incorrect or inconsistent gold annotations, such as when \"Smith\" is annotated as PER in 90% of training examples but O in 10% because annotators disagreed about whether to tag common surnames without first names. Inter-annotator disagreement during corpus construction propagates into the training data, and when two annotators choose different boundaries for the same span, a model trained on their combined labels learns an inconsistent mapping.\n\n**Real vs. Simulated Noise:**\nApproaches are typically evaluated using simulated noise where labels in a clean dataset are automatically corrupted, but this leads to unrealistic noise that is far easier to handle than real noise caused by human error or semi-automatic annotation.\n\n**Existing Datasets:**\nOther NER datasets have also been found to contain a share of incorrect labels, with Ontonotes4 estimated around 8% and WNUT-17 around 18%.\n\nThe search results show active research in addressing label noise challenges through benchmarking and noise-robust learning approaches for NER systems."
    ],
    "durationSeconds": 8.514989471000002
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T16:11:54.060Z_

<details><summary>↩ Tool result · `toolu_01KKFSG4rPTcq5KKvmcHBJfX`</summary>

```text
Web search results for query: "fine-grained entity typing label ambiguity type confusion hierarchy 2019 2020 2021"

Links: [{"title":"Fine-grained Entity Typing via Label Reasoning","url":"https://aclanthology.org/2021.emnlp-main.378.pdf"},{"title":"AFET: Automatic Fine-Grained Entity Typing by Hierarchical Partial-Label Embedding | Request PDF","url":"https://www.researchgate.net/publication/311990778_AFET_Automatic_Fine-Grained_Entity_Typing_by_Hierarchical_Partial-Label_Embedding"},{"title":"Seed-Guided Fine-Grained Entity Typing in Science and Engineering Domains","url":"https://arxiv.org/html/2401.13129v2"},{"title":"Fine-grained Entity Typing via Label Reasoning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.378/"},{"title":"Fine-grained Entity Typing through Increased Discourse Context and Adaptive Classification Thresholds","url":"https://www.emergentmind.com/papers/1804.08000"},{"title":"[2109.05744] Fine-grained Entity Typing via Label Reasoning","url":"https://arxiv.org/abs/2109.05744"},{"title":"Ontology Enrichment for Effective Fine-grained Entity Typing","url":"https://arxiv.org/html/2310.07795"},{"title":"Fine-grained Entity Typing via Label Reasoning - ORKG","url":"https://orkg.org/paper/R604350"},{"title":"Fine-grained Entity Typing without Knowledge Base","url":"https://aclanthology.org/2021.emnlp-main.431.pdf"},{"title":"Fine-Grained Entity Typing with a Type Taxonomy","url":"https://www.massey.ac.nz/~rwang/publications/22-TKDE-Wang.pdf"}]

The web search has returned relevant results on fine-grained entity typing research from the 2019-2021 period. Here are the key findings:

## Key Research Papers and Topics

Conventional entity typing approaches are based on independent classification paradigms, which make them difficult to recognize inter-dependent, long-tailed and fine-grained entity types, but the implicitly entailed extrinsic and intrinsic dependencies between labels can provide critical knowledge to tackle these challenges.

### Label Reasoning Approach (2021)

A Label Reasoning Network (LRN) was proposed that sequentially reasons fine-grained entity labels by discovering and exploiting label dependencies knowledge, utilizing an auto-regressive network to conduct deductive reasoning and a bipartite attribute graph to conduct inductive reasoning between labels.

### Key Challenges in the Field

Most works focus on learning what a certain type looks like, but few works have gone further to directly model the differences between types, that is, let models know the extent that one type is different from others, which is more effective to distinguish among similar fine-grained types.

A key challenge is how to deal with hierarchical ontology.

### Addressing Noisy Data and Hierarchies

Some researchers have focused on obtaining more labeled data through distant supervision, while others had focused on how to reduce noises in automatically labeled data.

Most existing ontology structures lack rich supporting information and even contain ambiguous relations, making them ineffective in guiding fine-grained entity typing, and as the ontology layer goes deeper and entity types become more fine-grained, language models face increasing challenges in distinguishing between these types due to their subtle semantic differences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "7556ed2d-2926-4321-8c87-30b7df2f2f42",
  "tool_use_result": {
    "query": "fine-grained entity typing label ambiguity type confusion hierarchy 2019 2020 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_011HkxDquPyK8oKmzqTEgPSf",
        "content": [
          {
            "title": "Fine-grained Entity Typing via Label Reasoning",
            "url": "https://aclanthology.org/2021.emnlp-main.378.pdf"
          },
          {
            "title": "AFET: Automatic Fine-Grained Entity Typing by Hierarchical Partial-Label Embedding | Request PDF",
            "url": "https://www.researchgate.net/publication/311990778_AFET_Automatic_Fine-Grained_Entity_Typing_by_Hierarchical_Partial-Label_Embedding"
          },
          {
            "title": "Seed-Guided Fine-Grained Entity Typing in Science and Engineering Domains",
            "url": "https://arxiv.org/html/2401.13129v2"
          },
          {
            "title": "Fine-grained Entity Typing via Label Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2021.emnlp-main.378/"
          },
          {
            "title": "Fine-grained Entity Typing through Increased Discourse Context and Adaptive Classification Thresholds",
            "url": "https://www.emergentmind.com/papers/1804.08000"
          },
          {
            "title": "[2109.05744] Fine-grained Entity Typing via Label Reasoning",
            "url": "https://arxiv.org/abs/2109.05744"
          },
          {
            "title": "Ontology Enrichment for Effective Fine-grained Entity Typing",
            "url": "https://arxiv.org/html/2310.07795"
          },
          {
            "title": "Fine-grained Entity Typing via Label Reasoning - ORKG",
            "url": "https://orkg.org/paper/R604350"
          },
          {
            "title": "Fine-grained Entity Typing without Knowledge Base",
            "url": "https://aclanthology.org/2021.emnlp-main.431.pdf"
          },
          {
            "title": "Fine-Grained Entity Typing with a Type Taxonomy",
            "url": "https://www.massey.ac.nz/~rwang/publications/22-TKDE-Wang.pdf"
          }
        ]
      },
      "The web search has returned relevant results on fine-grained entity typing research from the 2019-2021 period. Here are the key findings:\n\n## Key Research Papers and Topics\n\nConventional entity typing approaches are based on independent classification paradigms, which make them difficult to recognize inter-dependent, long-tailed and fine-grained entity types, but the implicitly entailed extrinsic and intrinsic dependencies between labels can provide critical knowledge to tackle these challenges.\n\n### Label Reasoning Approach (2021)\n\nA Label Reasoning Network (LRN) was proposed that sequentially reasons fine-grained entity labels by discovering and exploiting label dependencies knowledge, utilizing an auto-regressive network to conduct deductive reasoning and a bipartite attribute graph to conduct inductive reasoning between labels.\n\n### Key Challenges in the Field\n\nMost works focus on learning what a certain type looks like, but few works have gone further to directly model the differences between types, that is, let models know the extent that one type is different from others, which is more effective to distinguish among similar fine-grained types.\n\nA key challenge is how to deal with hierarchical ontology.\n\n### Addressing Noisy Data and Hierarchies\n\nSome researchers have focused on obtaining more labeled data through distant supervision, while others had focused on how to reduce noises in automatically labeled data.\n\nMost existing ontology structures lack rich supporting information and even contain ambiguous relations, making them ineffective in guiding fine-grained entity typing, and as the ontology layer goes deeper and entity types become more fine-grained, language models face increasing challenges in distinguishing between these types due to their subtle semantic differences."
    ],
    "durationSeconds": 8.373050595999993
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T16:11:56.054Z_

<details><summary>↩ Tool result · `toolu_01TqwqkxnA7VYr64atBunaaz`</summary>

```text
Web search results for query: "structured decoding constrained generation named entity recognition information extraction 2023 2024"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"[2308.07791] Informed Named Entity Recognition Decoding for Generative Language Models","url":"https://arxiv.org/abs/2308.07791"},{"title":"INFORMED NAMED ENTITY RECOGNITION DECODING FOR GENERATIVE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2308.07791"},{"title":"ProgGen: Generating Named Entity Recognition Datasets Step-by-step with Self-Reflexive Large Language Models","url":"https://arxiv.org/html/2403.11103v1"},{"title":"Generative Information Extraction","url":"https://www.emergentmind.com/topics/generative-information-extraction"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Informed Named Entity Recognition Decoding for Generative Language Models | Request PDF","url":"https://www.researchgate.net/publication/388095476_Informed_Named_Entity_Recognition_Decoding_for_Generative_Language_Models"},{"title":"Informed Named Entity Recognition Decoding for Generative Language Models","url":"https://www.emergentmind.com/papers/2308.07791"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"}]

I've performed a web search on your query about structured decoding, constrained generation, named entity recognition, and information extraction from 2023-2024. Here are the key findings:

## Recent Research on Constrained Decoding and Information Extraction

Recent work has tested the benefits of grammar-constrained decoding in NLP settings, with particular investigation into its impact on structured information extraction tasks in low-resource settings.

### Named Entity Recognition with Generative Models

A notable approach called Informed Named Entity Recognition Decoding (iNERD) treats named entity recognition as a generative process, leveraging language understanding capabilities of recent generative models and employing an informed decoding scheme that incorporates constraints into open-ended text generation to improve performance and eliminate hallucination risks.

### Constrained Decoding Techniques

Constrained decoding approaches use constrained beam search or prefix-tokens to force valid outputs, such as restricting to valid schema fields, entity names, or relation types.

### Dataset Generation for NER

Recent methods leverage the self-reflexive capabilities of LLMs to progressively synthesize NER datasets through a sequential multi-step process, as opposed to traditional approaches that directly generate synthetic datasets.

### Broader Information Extraction Landscape

Unified generative frameworks like LasUIE and compositional prompt frameworks integrate NER, relation extraction, event extraction, and semantic role labeling into a single generative model.

The search results reveal an active research area focusing on ensuring that generative models produce valid, well-formed outputs through various decoding constraints and structured generation techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "b9caf724-1ac1-44a8-894f-1c7b3e2add5b",
  "tool_use_result": {
    "query": "structured decoding constrained generation named entity recognition information extraction 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WKpGJXxHKQhNxpRKQ7DRPD",
        "content": [
          {
            "title": "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"
          },
          {
            "title": "Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"
          },
          {
            "title": "[2308.07791] Informed Named Entity Recognition Decoding for Generative Language Models",
            "url": "https://arxiv.org/abs/2308.07791"
          },
          {
            "title": "INFORMED NAMED ENTITY RECOGNITION DECODING FOR GENERATIVE LANGUAGE MODELS",
            "url": "https://arxiv.org/pdf/2308.07791"
          },
          {
            "title": "ProgGen: Generating Named Entity Recognition Datasets Step-by-step with Self-Reflexive Large Language Models",
            "url": "https://arxiv.org/html/2403.11103v1"
          },
          {
            "title": "Generative Information Extraction",
            "url": "https://www.emergentmind.com/topics/generative-information-extraction"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for Generative Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/388095476_Informed_Named_Entity_Recognition_Decoding_for_Generative_Language_Models"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for Generative Language Models",
            "url": "https://www.emergentmind.com/papers/2308.07791"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          }
        ]
      },
      "I've performed a web search on your query about structured decoding, constrained generation, named entity recognition, and information extraction from 2023-2024. Here are the key findings:\n\n## Recent Research on Constrained Decoding and Information Extraction\n\nRecent work has tested the benefits of grammar-constrained decoding in NLP settings, with particular investigation into its impact on structured information extraction tasks in low-resource settings.\n\n### Named Entity Recognition with Generative Models\n\nA notable approach called Informed Named Entity Recognition Decoding (iNERD) treats named entity recognition as a generative process, leveraging language understanding capabilities of recent generative models and employing an informed decoding scheme that incorporates constraints into open-ended text generation to improve performance and eliminate hallucination risks.\n\n### Constrained Decoding Techniques\n\nConstrained decoding approaches use constrained beam search or prefix-tokens to force valid outputs, such as restricting to valid schema fields, entity names, or relation types.\n\n### Dataset Generation for NER\n\nRecent methods leverage the self-reflexive capabilities of LLMs to progressively synthesize NER datasets through a sequential multi-step process, as opposed to traditional approaches that directly generate synthetic datasets.\n\n### Broader Information Extraction Landscape\n\nUnified generative frameworks like LasUIE and compositional prompt frameworks integrate NER, relation extraction, event extraction, and semantic role labeling into a single generative model.\n\nThe search results reveal an active research area focusing on ensuring that generative models produce valid, well-formed outputs through various decoding constraints and structured generation techniques."
    ],
    "durationSeconds": 11.723663505999998
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Good, I have results for directions A and B. Let me now search for directions C and D, and also search for more specific papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "3579d8df-df92-493a-a42b-9adf42b45d6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 29_

继续搜索方向 C 和 D，以及一些具体论文的详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "caca6ab4-3a9e-4883-a95f-b7d7f2d9c712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zmjTokmRfQyFb9yV7qvzA`</summary>

```json
{
  "query": "span-level evaluation NER partial matching F1 entity evaluation metrics survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "3557936d-c149-4220-a271-d8d120ae3d78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fdp9dN7NAxGdxN6j7MHn5`</summary>

```json
{
  "query": "LLM calibration confidence estimation 2024 language model calibration survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "c1fdbaf9-a97e-4a1a-bac4-18e35ff21f48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y1ahWkrEgSXFnTGxqZHTRj`</summary>

```json
{
  "query": "NoiseBench benchmarking impact real label noise named entity recognition 2405.07609 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "3c7e8e15-b6a5-44f7-9c2e-990955307661",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QDmHSDHixdwjoZp7MvMHEx`</summary>

```json
{
  "query": "iNERD informed named entity recognition decoding generative language models 2308.07791 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "898e44dc-6b1d-4fe0-82e9-2a863128cbca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgSgc9SxSpc11yJ1WFaoJz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1840,
      "cache_creation_input_tokens": 2401,
      "cache_read_input_tokens": 32507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2401
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

_source line 34 · 2026-05-15T16:12:07.113Z_

<details><summary>↩ Tool result · `toolu_01Y1ahWkrEgSXFnTGxqZHTRj`</summary>

```text
Web search results for query: "NoiseBench benchmarking impact real label noise named entity recognition 2405.07609 authors venue"

Links: [{"title":"[2405.07609] NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition","url":"https://arxiv.org/abs/2405.07609"},{"title":"NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition","url":"https://arxiv.org/html/2405.07609v1"},{"title":"GitHub - elenamer/NoiseBench: An NER benchmark for learning with label noise","url":"https://github.com/elenamer/NoiseBench"},{"title":"NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1011/"},{"title":"NoiseBench - Alan Akbik","url":"https://alanakbik.github.io/research/noisebench"},{"title":"Label Convergence: Defining an Upper Performance Bound in Object Recognition through Contradictory Annotations","url":"https://arxiv.org/html/2409.09412v1"},{"title":"RobustFT: Robust Supervised Fine-tuning for Large Language Models under Noisy Response","url":"https://arxiv.org/html/2412.14922v1"},{"title":"[2510.16211] Benchmarking noisy label detection methods","url":"https://arxiv.org/abs/2510.16211"},{"title":"Computer Science May 2024","url":"https://arxiv.org/list/cs/2024-05?skip=2980&show=2000"},{"title":"FNBench: Benchmarking Robust Federated Learning against Noisy Labels","url":"https://arxiv.org/html/2505.06684"}]

Based on the search results, here's the information about the NoiseBench paper:

**Authors:** Elena Merdjanovska, Ansar Aynetdinov, and Alan Akbik

**Venue:** The 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)

**Overview:** NoiseBench is an NER benchmark consisting of clean training data corrupted with 6 types of real noise, including expert errors, crowdsourcing errors, automatic annotation errors and LLM errors.

**Key Findings:** Real noise is significantly more challenging than simulated noise, and current state-of-the-art models for noise-robust learning fall far short of their theoretically achievable upper bound. Additionally, during training, real noise is memorized immediately, whereas memorization of simulated noise is delayed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "ade6c140-bc0f-40f4-9dbb-e4ea83bcafa1",
  "tool_use_result": {
    "query": "NoiseBench benchmarking impact real label noise named entity recognition 2405.07609 authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XugrQjoZ6ziT9eAMdWJRTS",
        "content": [
          {
            "title": "[2405.07609] NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition",
            "url": "https://arxiv.org/abs/2405.07609"
          },
          {
            "title": "NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition",
            "url": "https://arxiv.org/html/2405.07609v1"
          },
          {
            "title": "GitHub - elenamer/NoiseBench: An NER benchmark for learning with label noise",
            "url": "https://github.com/elenamer/NoiseBench"
          },
          {
            "title": "NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.1011/"
          },
          {
            "title": "NoiseBench - Alan Akbik",
            "url": "https://alanakbik.github.io/research/noisebench"
          },
          {
            "title": "Label Convergence: Defining an Upper Performance Bound in Object Recognition through Contradictory Annotations",
            "url": "https://arxiv.org/html/2409.09412v1"
          },
          {
            "title": "RobustFT: Robust Supervised Fine-tuning for Large Language Models under Noisy Response",
            "url": "https://arxiv.org/html/2412.14922v1"
          },
          {
            "title": "[2510.16211] Benchmarking noisy label detection methods",
            "url": "https://arxiv.org/abs/2510.16211"
          },
          {
            "title": "Computer Science May 2024",
            "url": "https://arxiv.org/list/cs/2024-05?skip=2980&show=2000"
          },
          {
            "title": "FNBench: Benchmarking Robust Federated Learning against Noisy Labels",
            "url": "https://arxiv.org/html/2505.06684"
          }
        ]
      },
      "Based on the search results, here's the information about the NoiseBench paper:\n\n**Authors:** Elena Merdjanovska, Ansar Aynetdinov, and Alan Akbik\n\n**Venue:** The 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)\n\n**Overview:** NoiseBench is an NER benchmark consisting of clean training data corrupted with 6 types of real noise, including expert errors, crowdsourcing errors, automatic annotation errors and LLM errors.\n\n**Key Findings:** Real noise is significantly more challenging than simulated noise, and current state-of-the-art models for noise-robust learning fall far short of their theoretically achievable upper bound. Additionally, during training, real noise is memorized immediately, whereas memorization of simulated noise is delayed."
    ],
    "durationSeconds": 5.041437243000001
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T16:12:07.405Z_

<details><summary>↩ Tool result · `toolu_01QDmHSDHixdwjoZp7MvMHEx`</summary>

```text
Web search results for query: "iNERD informed named entity recognition decoding generative language models 2308.07791 authors venue"

Links: [{"title":"[2308.07791] Informed Named Entity Recognition Decoding for Generative Language Models","url":"https://arxiv.org/abs/2308.07791"},{"title":"INFORMED NAMED ENTITY RECOGNITION DECODING FOR GENERATIVE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2308.07791"},{"title":"Paper page - Informed Named Entity Recognition Decoding for Generative Language Models","url":"https://huggingface.co/papers/2308.07791"},{"title":"Informed Named Entity Recognition Decoding for Generative Language Models | Request PDF","url":"https://www.researchgate.net/publication/373142130_Informed_Named_Entity_Recognition_Decoding_for_Generative_Language_Models"},{"title":"Informed Named Entity Recognition Decoding for Generative Language Models","url":"https://www.emergentmind.com/papers/2308.07791"},{"title":"[PDF] Informed Named Entity Recognition Decoding for Generative Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Informed-Named-Entity-Recognition-Decoding-for-Deu%C3%9Fer-Hillebrand/3958152c43888a0a9461de2b952df4a39491442b"},{"title":"Informed Named Entity Recognition Decoding for Generative Language Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10825603/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Named+Entity+Recognition"},{"title":"Informed Named Entity Recognition Decoding for ...","url":"https://www.computer.org/csdl/proceedings-article/bigdata/2024/10825603/23ykHmHZhsI"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"}]

Based on the search results, here's the information about the iNERD paper:

**Paper:** Informed Named Entity Recognition Decoding (iNERD) treats named entity recognition as a generative process.

**Authors:** Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, and Rafet Sifa

**Venue:** The paper was submitted to arXiv on August 15, 2023. The paper has also been published at the IEEE Big Data conference (as indicated by the IEEE Xplore listing showing it as document 10825603 from 2024).

The paper proposes an informed decoding scheme incorporating the restricted nature of information extraction into open-ended text generation, improving performance and eliminating any risk of hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "12c35352-2ab7-459c-8ff8-74ed08ef1fc2",
  "tool_use_result": {
    "query": "iNERD informed named entity recognition decoding generative language models 2308.07791 authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MdrrsDuf9L4ZUZsPF2WqY7",
        "content": [
          {
            "title": "[2308.07791] Informed Named Entity Recognition Decoding for Generative Language Models",
            "url": "https://arxiv.org/abs/2308.07791"
          },
          {
            "title": "INFORMED NAMED ENTITY RECOGNITION DECODING FOR GENERATIVE LANGUAGE MODELS",
            "url": "https://arxiv.org/pdf/2308.07791"
          },
          {
            "title": "Paper page - Informed Named Entity Recognition Decoding for Generative Language Models",
            "url": "https://huggingface.co/papers/2308.07791"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for Generative Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/373142130_Informed_Named_Entity_Recognition_Decoding_for_Generative_Language_Models"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for Generative Language Models",
            "url": "https://www.emergentmind.com/papers/2308.07791"
          },
          {
            "title": "[PDF] Informed Named Entity Recognition Decoding for Generative Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Informed-Named-Entity-Recognition-Decoding-for-Deu%C3%9Fer-Hillebrand/3958152c43888a0a9461de2b952df4a39491442b"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for Generative Language Models | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10825603/"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Named+Entity+Recognition"
          },
          {
            "title": "Informed Named Entity Recognition Decoding for ...",
            "url": "https://www.computer.org/csdl/proceedings-article/bigdata/2024/10825603/23ykHmHZhsI"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          }
        ]
      },
      "Based on the search results, here's the information about the iNERD paper:\n\n**Paper:** Informed Named Entity Recognition Decoding (iNERD) treats named entity recognition as a generative process.\n\n**Authors:** Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, and Rafet Sifa\n\n**Venue:** The paper was submitted to arXiv on August 15, 2023. The paper has also been published at the IEEE Big Data conference (as indicated by the IEEE Xplore listing showing it as document 10825603 from 2024).\n\nThe paper proposes an informed decoding scheme incorporating the restricted nature of information extraction into open-ended text generation, improving performance and eliminating any risk of hallucinations."
    ],
    "durationSeconds": 4.495450585999999
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T16:12:08.071Z_

<details><summary>↩ Tool result · `toolu_015fdp9dN7NAxGdxN6j7MHn5`</summary>

```text
Web search results for query: "LLM calibration confidence estimation 2024 language model calibration survey"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298"},{"title":"A Survey of Confidence Estimation and Calibration in ...","url":"https://aclanthology.org/2024.naacl-long.366.pdf"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/html/2311.08298v2"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2","url":"https://dl.acm.org/doi/10.1145/3711896.3736569"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Uncertainty Quantification and Confidence Calibration in Large","url":"https://xiao0o0o.github.io/2025KDD_tutorial/survey.pdf"},{"title":"Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"},{"title":"A study of calibration as a measurement of trustworthiness of large language models in biomedical natural language processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/"}]

Based on the search results, I found comprehensive information about LLM calibration and confidence estimation from 2024 research. Here are the key findings:

## Main Survey Paper

A comprehensive survey titled "A Survey of Confidence Estimation and Calibration in Large Language Models" was published by Geng et al. at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) in Mexico City.

## Key Challenges and Findings

Large language models can be unreliable due to factual errors in their generations, and assessing their confidence and calibrating them across different tasks can help mitigate risks and enable LLMs to produce better generations.

Research on confidence and calibration reveals frequent misalignment between confidence and accuracy, which is a critical challenge in deploying LLMs reliably.

## Calibration Issues

When models are asked to express self-knowledge numerically, the reports tend to collapse: verbalized confidence clusters in high ranges, in multiples of five, and systematically misaligns with internal token probabilities.

## Research Scope

The survey outlines the challenges and summarizes recent technical advancements for LLM confidence estimation and calibration, discussing their applications and suggesting promising directions for future work.

The research indicates that while LLMs show promise, improving their calibration and confidence estimation remains an important open problem for safe and trustworthy deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "9af8005b-469c-4374-9ee5-465fb1f1ed19",
  "tool_use_result": {
    "query": "LLM calibration confidence estimation 2024 language model calibration survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V4zgiasP1U71dsakgrLuWr",
        "content": [
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.366/"
          },
          {
            "title": "[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2311.08298"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in ...",
            "url": "https://aclanthology.org/2024.naacl-long.366.pdf"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2311.08298v2"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2",
            "url": "https://dl.acm.org/doi/10.1145/3711896.3736569"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large",
            "url": "https://xiao0o0o.github.io/2025KDD_tutorial/survey.pdf"
          },
          {
            "title": "Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"
          },
          {
            "title": "A study of calibration as a measurement of trustworthiness of large language models in biomedical natural language processing - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about LLM calibration and confidence estimation from 2024 research. Here are the key findings:\n\n## Main Survey Paper\n\nA comprehensive survey titled \"A Survey of Confidence Estimation and Calibration in Large Language Models\" was published by Geng et al. at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL) in Mexico City.\n\n## Key Challenges and Findings\n\nLarge language models can be unreliable due to factual errors in their generations, and assessing their confidence and calibrating them across different tasks can help mitigate risks and enable LLMs to produce better generations.\n\nResearch on confidence and calibration reveals frequent misalignment between confidence and accuracy, which is a critical challenge in deploying LLMs reliably.\n\n## Calibration Issues\n\nWhen models are asked to express self-knowledge numerically, the reports tend to collapse: verbalized confidence clusters in high ranges, in multiples of five, and systematically misaligns with internal token probabilities.\n\n## Research Scope\n\nThe survey outlines the challenges and summarizes recent technical advancements for LLM confidence estimation and calibration, discussing their applications and suggesting promising directions for future work.\n\nThe research indicates that while LLMs show promise, improving their calibration and confidence estimation remains an important open problem for safe and trustworthy deployment."
    ],
    "durationSeconds": 7.3523104079999975
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T16:12:10.828Z_

<details><summary>↩ Tool result · `toolu_015zmjTokmRfQyFb9yV7qvzA`</summary>

```text
Web search results for query: "span-level evaluation NER partial matching F1 entity evaluation metrics survey"

Links: [{"title":"Named-Entity evaluation metrics based on entity-level","url":"https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"},{"title":"GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13","url":"https://github.com/MantisAI/nervaluate"},{"title":"nervaluate · PyPI","url":"https://pypi.org/project/nervaluate/"},{"title":"Exact Match and F1: Precision Metrics for NLP Evaluation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/exact-match-f1-nlp-evaluation-metrics"},{"title":"F1 Score for NER: A Metric To Evaluate Precision And Recall","url":"https://thatware.co/f1-score-for-ner/"},{"title":"nervaluate — The Ultimate way for Benchmarking NER Models","url":"https://rumn.medium.com/nervaluate-the-ultimate-way-for-benchmarking-ner-models-b29e83fbae95"},{"title":"GitHub - jantrienes/nereval: Evaluation script for named entity recognition (NER) systems based on entity-level F1 score. · GitHub","url":"https://github.com/jantrienes/nereval"},{"title":"Custom NER evaluation metrics - Foundry Tools | Microsoft Learn","url":"https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/concepts/evaluation-metrics"},{"title":"Sequence Labeling Metrics | huggingface/evaluate | DeepWiki","url":"https://deepwiki.com/huggingface/evaluate/5.3-sequence-labeling-metrics"},{"title":"Class level metrics | Snorkel AI","url":"https://docs.snorkel.ai/docs/25.3/user-guide/analysis/class-level-metrics/"}]

Based on the web search results, here's a comprehensive overview of span-level evaluation, NER partial matching, F1 metrics, and entity evaluation:

## Span-Level Evaluation in NER

In NER, the task is to identify spans of text that correspond to entities of specified types, and evaluation requires not just that the tokens overlap but that the entity boundaries match the reference annotation. Most production NER systems prioritize span-level F1, as it aligns with real usage requirements.

## Exact vs. Partial Matching

Exact span match requires that the predicted entity span exactly matches the reference span in both position and type. If the reference annotates "General Electric" as an ORGANIZATION and the model predicts "Electric" as an ORGANIZATION, the prediction receives zero credit under exact span evaluation, even though it identified the right entity type and the right sub-span. This strict protocol is used in the CoNLL-2003 shared task evaluation and is essentially Exact Match adapted to the span level.

Token-level F1 computes precision and recall at the level of individual entity tokens, giving partial credit for spans that overlap but do not perfectly align. However, the NLP community has not fully standardized whether "partial match" in NER means token-level overlap (any shared tokens count) or span-level overlap (the predicted span must start or end at the same position as the reference).

## Entity Evaluation Metrics and F1

Nervaluate is a module for evaluating Named Entity Recognition (NER) models as defined in the SemEval 2013 - 9.1 task. The evaluation metrics output by nervaluate go beyond a simple token/tag based schema, and consider different scenarios based on whether all the tokens that belong to a named entity were classified or not, and also whether the correct entity type was assigned.

Different evaluation methods include Strict, Exact, Partial, and Type Evaluation. Each method offers unique insights into model performance, considering factors such as exact matches, partial overlaps, missing entities, correctness of entity types, etc.

Partial matching calculations use: Precision = (COR + 0.5 × PAR) / ACT and Recall = (COR + 0.5 × PAR)/POS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "aa7ced84-07d0-4b4a-bc75-90e17d74a323",
  "tool_use_result": {
    "query": "span-level evaluation NER partial matching F1 entity evaluation metrics survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EKrkEbykCVSqBjuBrKv5nz",
        "content": [
          {
            "title": "Named-Entity evaluation metrics based on entity-level",
            "url": "https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"
          },
          {
            "title": "GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13",
            "url": "https://github.com/MantisAI/nervaluate"
          },
          {
            "title": "nervaluate · PyPI",
            "url": "https://pypi.org/project/nervaluate/"
          },
          {
            "title": "Exact Match and F1: Precision Metrics for NLP Evaluation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/exact-match-f1-nlp-evaluation-metrics"
          },
          {
            "title": "F1 Score for NER: A Metric To Evaluate Precision And Recall",
            "url": "https://thatware.co/f1-score-for-ner/"
          },
          {
            "title": "nervaluate — The Ultimate way for Benchmarking NER Models",
            "url": "https://rumn.medium.com/nervaluate-the-ultimate-way-for-benchmarking-ner-models-b29e83fbae95"
          },
          {
            "title": "GitHub - jantrienes/nereval: Evaluation script for named entity recognition (NER) systems based on entity-level F1 score. · GitHub",
            "url": "https://github.com/jantrienes/nereval"
          },
          {
            "title": "Custom NER evaluation metrics - Foundry Tools | Microsoft Learn",
            "url": "https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/concepts/evaluation-metrics"
          },
          {
            "title": "Sequence Labeling Metrics | huggingface/evaluate | DeepWiki",
            "url": "https://deepwiki.com/huggingface/evaluate/5.3-sequence-labeling-metrics"
          },
          {
            "title": "Class level metrics | Snorkel AI",
            "url": "https://docs.snorkel.ai/docs/25.3/user-guide/analysis/class-level-metrics/"
          }
        ]
      },
      "Based on the web search results, here's a comprehensive overview of span-level evaluation, NER partial matching, F1 metrics, and entity evaluation:\n\n## Span-Level Evaluation in NER\n\nIn NER, the task is to identify spans of text that correspond to entities of specified types, and evaluation requires not just that the tokens overlap but that the entity boundaries match the reference annotation. Most production NER systems prioritize span-level F1, as it aligns with real usage requirements.\n\n## Exact vs. Partial Matching\n\nExact span match requires that the predicted entity span exactly matches the reference span in both position and type. If the reference annotates \"General Electric\" as an ORGANIZATION and the model predicts \"Electric\" as an ORGANIZATION, the prediction receives zero credit under exact span evaluation, even though it identified the right entity type and the right sub-span. This strict protocol is used in the CoNLL-2003 shared task evaluation and is essentially Exact Match adapted to the span level.\n\nToken-level F1 computes precision and recall at the level of individual entity tokens, giving partial credit for spans that overlap but do not perfectly align. However, the NLP community has not fully standardized whether \"partial match\" in NER means token-level overlap (any shared tokens count) or span-level overlap (the predicted span must start or end at the same position as the reference).\n\n## Entity Evaluation Metrics and F1\n\nNervaluate is a module for evaluating Named Entity Recognition (NER) models as defined in the SemEval 2013 - 9.1 task. The evaluation metrics output by nervaluate go beyond a simple token/tag based schema, and consider different scenarios based on whether all the tokens that belong to a named entity were classified or not, and also whether the correct entity type was assigned.\n\nDifferent evaluation methods include Strict, Exact, Partial, and Type Evaluation. Each method offers unique insights into model performance, considering factors such as exact matches, partial overlaps, missing entities, correctness of entity types, etc.\n\nPartial matching calculations use: Precision = (COR + 0.5 × PAR) / ACT and Recall = (COR + 0.5 × PAR)/POS."
    ],
    "durationSeconds": 10.642059938
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Good, let me continue searching for more specific papers in the remaining directions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "f879b222-bc63-4d39-b42f-2ede2efb417c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 39_

继续搜索更多具体论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "303c10ae-94db-4a4a-82cb-48639339b7ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S3zFcHE4TnN2JfYAZxeoe1`</summary>

```json
{
  "query": "fine-grained entity typing label reasoning EMNLP 2021 2109.05744 authors Qian Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1ca86228-e482-424d-bbca-e593fccd9056",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014mgDzKo5KYPFMP5f7U8Paq`</summary>

```json
{
  "query": "SemEval 2013 task 9.1 evaluation named entities partial matching metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "f5940bde-8e3a-433b-81ba-976495aa7aa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X8Nicr2PpzqyRQdBrLYFHB`</summary>

```json
{
  "query": "\"confidence estimation\" \"named entity recognition\" OR \"information extraction\" LLM calibration 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "cce498fb-a98e-436e-9240-4a0d00076741",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9kYPWtcMir3yTKz3s33uk`</summary>

```json
{
  "query": "grammar constrained decoding structured information extraction clinical 2024 1406857 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "841ff5e4-f62a-419f-956f-b286b9c85853",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPfFnuo3EVxwkyMF899QA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2322,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 34908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 44 · 2026-05-15T16:12:22.448Z_

<details><summary>↩ Tool result · `toolu_01K9kYPWtcMir3yTKz3s33uk`</summary>

```text
Web search results for query: "grammar constrained decoding structured information extraction clinical 2024 1406857 authors"

Links: [{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"GitHub - ag-sc/Clinical-Trial-IE-GCD: Artifact \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\"","url":"https://github.com/ag-sc/clinical-trial-ie-gcd"},{"title":"ag-sc/Clinical-Trial-IE-GCD: v1.1","url":"https://zenodo.org/records/14615186"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://pubmed.ncbi.nlm.nih.gov/39839970/"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://www.semanticscholar.org/paper/Grammar-constrained-decoding-for-structured-with-to-Schmidt-Cimiano/f15284effc8bf54035953b20422ebe8aed7a9b58"},{"title":"https://www.frontiersin.org/journals/artificial-intelligence/articles/ ...","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/xml"},{"title":"Ontology-Constrained Generation of Domain-Specific Clinical Summaries","url":"https://arxiv.org/pdf/2411.15666"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"}]

I found the paper you're searching for! Here's the information about the article:

**Title:** Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts

**Authors:** David M. Schmidt and Philipp Cimiano

**Publication Details:** Published in Frontiers in Artificial Intelligence, Volume 7, 2025, DOI: 10.3389/frai.2024.1406857

**Affiliation:** Both authors are from the Center for Cognitive Interaction Technology (CITEC), Technical Faculty, Bielefeld University, Germany

**Main Focus:** The paper experimentally investigates the impact of a grammar-constrained decoding approach on the well-formedness and correctness of the output of structured information extraction models.

The research is available on Frontiers in Artificial Intelligence and has associated artifacts on GitHub and Zenodo for reproducibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "2179d103-2959-4dc8-9a56-bc0e91561bc6",
  "tool_use_result": {
    "query": "grammar constrained decoding structured information extraction clinical 2024 1406857 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QgpXZR6FrHxbFLWSCerqai",
        "content": [
          {
            "title": "Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"
          },
          {
            "title": "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"
          },
          {
            "title": "Grammar-constrained decoding for structured information ...",
            "url": "https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"
          },
          {
            "title": "GitHub - ag-sc/Clinical-Trial-IE-GCD: Artifact \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\"",
            "url": "https://github.com/ag-sc/clinical-trial-ie-gcd"
          },
          {
            "title": "ag-sc/Clinical-Trial-IE-GCD: v1.1",
            "url": "https://zenodo.org/records/14615186"
          },
          {
            "title": "Grammar-constrained decoding for structured information ...",
            "url": "https://pubmed.ncbi.nlm.nih.gov/39839970/"
          },
          {
            "title": "Grammar-constrained decoding for structured information ...",
            "url": "https://www.semanticscholar.org/paper/Grammar-constrained-decoding-for-structured-with-to-Schmidt-Cimiano/f15284effc8bf54035953b20422ebe8aed7a9b58"
          },
          {
            "title": "https://www.frontiersin.org/journals/artificial-intelligence/articles/ ...",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/xml"
          },
          {
            "title": "Ontology-Constrained Generation of Domain-Specific Clinical Summaries",
            "url": "https://arxiv.org/pdf/2411.15666"
          },
          {
            "title": "The Hidden Cost of Structure: How Constrained Decoding ...",
            "url": "https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"
          }
        ]
      },
      "I found the paper you're searching for! Here's the information about the article:\n\n**Title:** Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\n\n**Authors:** David M. Schmidt and Philipp Cimiano\n\n**Publication Details:** Published in Frontiers in Artificial Intelligence, Volume 7, 2025, DOI: 10.3389/frai.2024.1406857\n\n**Affiliation:** Both authors are from the Center for Cognitive Interaction Technology (CITEC), Technical Faculty, Bielefeld University, Germany\n\n**Main Focus:** The paper experimentally investigates the impact of a grammar-constrained decoding approach on the well-formedness and correctness of the output of structured information extraction models.\n\nThe research is available on Frontiers in Artificial Intelligence and has associated artifacts on GitHub and Zenodo for reproducibility."
    ],
    "durationSeconds": 5.237147412999999
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T16:12:22.838Z_

<details><summary>↩ Tool result · `toolu_01S3zFcHE4TnN2JfYAZxeoe1`</summary>

```text
Web search results for query: "fine-grained entity typing label reasoning EMNLP 2021 2109.05744 authors Qian Li"

Links: [{"title":"[2109.05744] Fine-grained Entity Typing via Label Reasoning","url":"https://arxiv.org/abs/2109.05744"},{"title":"Fine-grained Entity Typing via Label Reasoning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.378/"},{"title":"Fine-grained Entity Typing via Label Reasoning","url":"https://aclanthology.org/2021.emnlp-main.378.pdf"},{"title":"GitHub - loriqing/Label-Reasoning-Network: code for \"Fine-grained Entity Typing via Label Reasoning\" EMNLP2021","url":"https://github.com/loriqing/Label-Reasoning-Network"},{"title":"Few-Shot Fine-Grained Entity Typing with Automatic Label Interpretation and Instance Generation | Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining","url":"https://dl.acm.org/doi/10.1145/3534678.3539443"},{"title":"Fine-grained Entity Typing without Knowledge Base - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.431/"},{"title":"Fine-grained Entity Typing via Label Reasoning - ORKG","url":"https://orkg.org/paper/R604350"},{"title":"Automatic noisy label correction for fine-grained entity typing","url":"https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=8756&context=sis_research"},{"title":"Few-Shot Fine-Grained Entity Typing with Automatic Label ...","url":"https://par.nsf.gov/servlets/purl/10387471"},{"title":"Seed-Guided Fine-Grained Entity Typing in Science and Engineering Domains","url":"https://arxiv.org/html/2401.13129v2"}]

Based on the search results, I found information about the paper with arxiv ID 2109.05744. Here are the key details:

## Paper Information

**Title:** Fine-grained Entity Typing via Label Reasoning

**Authors:** Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, and Hua Wu

**Publication:** Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 4611–4622, Online and Punta Cana, Dominican Republic (EMNLP 2021)

**ArXiv Submission:** September 13, 2021

## Overview

Conventional entity typing approaches are based on independent classification paradigms, which make them difficult to recognize inter-dependent, long-tailed and fine-grained entity types. The paper argues that the implicitly entailed extrinsic and intrinsic dependencies between labels can provide critical knowledge to tackle these challenges.

## Proposed Approach

The paper proposes Label Reasoning Network (LRN), which sequentially reasons fine-grained entity labels by discovering and exploiting label dependencies knowledge entailed in the data. Specifically, LRN utilizes an auto-regressive network to conduct deductive reasoning and a bipartite attribute graph to conduct inductive reasoning between labels, which can effectively model, learn and reason complex label dependencies in a sequence-to-set, end-to-end manner.

## Results

Experiments show that LRN achieves the state-of-the-art performance on standard ultra fine-grained entity typing benchmarks, and can also resolve the long tail label problem effectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "5a6d0959-5903-4caa-9a30-6ef545a22906",
  "tool_use_result": {
    "query": "fine-grained entity typing label reasoning EMNLP 2021 2109.05744 authors Qian Li",
    "results": [
      {
        "tool_use_id": "srvtoolu_01754rWeuQYtkaWPUsuHz4Zr",
        "content": [
          {
            "title": "[2109.05744] Fine-grained Entity Typing via Label Reasoning",
            "url": "https://arxiv.org/abs/2109.05744"
          },
          {
            "title": "Fine-grained Entity Typing via Label Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2021.emnlp-main.378/"
          },
          {
            "title": "Fine-grained Entity Typing via Label Reasoning",
            "url": "https://aclanthology.org/2021.emnlp-main.378.pdf"
          },
          {
            "title": "GitHub - loriqing/Label-Reasoning-Network: code for \"Fine-grained Entity Typing via Label Reasoning\" EMNLP2021",
            "url": "https://github.com/loriqing/Label-Reasoning-Network"
          },
          {
            "title": "Few-Shot Fine-Grained Entity Typing with Automatic Label Interpretation and Instance Generation | Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
            "url": "https://dl.acm.org/doi/10.1145/3534678.3539443"
          },
          {
            "title": "Fine-grained Entity Typing without Knowledge Base - ACL Anthology",
            "url": "https://aclanthology.org/2021.emnlp-main.431/"
          },
          {
            "title": "Fine-grained Entity Typing via Label Reasoning - ORKG",
            "url": "https://orkg.org/paper/R604350"
          },
          {
            "title": "Automatic noisy label correction for fine-grained entity typing",
            "url": "https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=8756&context=sis_research"
          },
          {
            "title": "Few-Shot Fine-Grained Entity Typing with Automatic Label ...",
            "url": "https://par.nsf.gov/servlets/purl/10387471"
          },
          {
            "title": "Seed-Guided Fine-Grained Entity Typing in Science and Engineering Domains",
            "url": "https://arxiv.org/html/2401.13129v2"
          }
        ]
      },
      "Based on the search results, I found information about the paper with arxiv ID 2109.05744. Here are the key details:\n\n## Paper Information\n\n**Title:** Fine-grained Entity Typing via Label Reasoning\n\n**Authors:** Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, and Hua Wu\n\n**Publication:** Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 4611–4622, Online and Punta Cana, Dominican Republic (EMNLP 2021)\n\n**ArXiv Submission:** September 13, 2021\n\n## Overview\n\nConventional entity typing approaches are based on independent classification paradigms, which make them difficult to recognize inter-dependent, long-tailed and fine-grained entity types. The paper argues that the implicitly entailed extrinsic and intrinsic dependencies between labels can provide critical knowledge to tackle these challenges.\n\n## Proposed Approach\n\nThe paper proposes Label Reasoning Network (LRN), which sequentially reasons fine-grained entity labels by discovering and exploiting label dependencies knowledge entailed in the data. Specifically, LRN utilizes an auto-regressive network to conduct deductive reasoning and a bipartite attribute graph to conduct inductive reasoning between labels, which can effectively model, learn and reason complex label dependencies in a sequence-to-set, end-to-end manner.\n\n## Results\n\nExperiments show that LRN achieves the state-of-the-art performance on standard ultra fine-grained entity typing benchmarks, and can also resolve the long tail label problem effectively."
    ],
    "durationSeconds": 8.166565035000007
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T16:12:22.992Z_

<details><summary>↩ Tool result · `toolu_014mgDzKo5KYPFMP5f7U8Paq`</summary>

```text
Web search results for query: "SemEval 2013 task 9.1 evaluation named entities partial matching metrics"

Links: [{"title":"GitHub - davidsbatista/NER-Evaluation: An implementation of a full named-entity evaluation metrics based on SemEval'13 Task 9 - not at tag/token level but considering all the tokens that are part of the named-entity","url":"https://github.com/davidsbatista/NER-Evaluation"},{"title":"GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13","url":"https://github.com/MantisAI/nervaluate"},{"title":"Client Challenge","url":"https://pypi.org/project/eval4ner/"},{"title":"nervaluate · PyPI","url":"https://pypi.org/project/nervaluate/"},{"title":"Named-Entity evaluation metrics based on entity-level","url":"https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"},{"title":"Named Entity Recognition for Norwegian","url":"https://www.duo.uio.no/bitstream/handle/10852/81384/master-thesis.pdf?sequence=1&isAllowed=y"},{"title":"What are some metrics for Named Entity Recognition? — AI Practitioner Handbook","url":"https://aisingapore.github.io/ai-practitioner-handbook/book/6-modelling/ner-metrics.html"},{"title":"Semeval-2013 task 9: Extraction of drug-drug interactions from biomedical texts (ddiextraction 2013) | Request PDF","url":"https://www.researchgate.net/publication/284650486_Semeval-2013_task_9_Extraction_of_drug-drug_interactions_from_biomedical_texts_ddiextraction_2013"},{"title":"Ychai","url":"https://ychai.uk/notes/2018/11/21/NLP/NER/Evaluation-metrics-of-Name-Entity-Recognition-systems/"},{"title":"SemEval-2013 Task 9 : Extraction of Drug- ...","url":"https://aclanthology.org/S13-2056.pdf"}]

Based on the search results, here's what I found about SemEval 2013 Task 9.1 evaluation metrics for named entities with partial matching:

## Overview

The SemEval 2013 - 9.1 task defines evaluation metrics for Named Entity Recognition (NER) models. The evaluation metrics go beyond a simple token/tag based schema, and consider different scenarios based on whether all the tokens that belong to a named entity were classified or not, and also whether the correct entity type was assigned.

## Evaluation Schemes

The SemEval'13 introduced four different ways to measure precision/recall/f1-score results based on the metrics defined by MUC. There are 4 options of measuring the overall performance, which differ in terms of what is considered to be correct, incorrect, partial, missed and spurious predictions, and specifically indicate the correctness of the full named-entities with respect to their boundaries and entity classes.

## Partial Matching Metrics

For partial matches, Precision = (COR + 0.5 × PAR) / ACT and Recall = (COR + 0.5 × PAR)/POS. This formula gives partial matches a 0.5 weight in the calculation.

## Stringency Levels

In general, partial will be the most lenient evaluation, while strict will be the most stringent evaluation. The scores for type and exact will usually fall in between.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "859c9fc0-30e5-425d-a621-388e087055a4",
  "tool_use_result": {
    "query": "SemEval 2013 task 9.1 evaluation named entities partial matching metrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pem4JxENKaeMFsQE11Xyip",
        "content": [
          {
            "title": "GitHub - davidsbatista/NER-Evaluation: An implementation of a full named-entity evaluation metrics based on SemEval'13 Task 9 - not at tag/token level but considering all the tokens that are part of the named-entity",
            "url": "https://github.com/davidsbatista/NER-Evaluation"
          },
          {
            "title": "GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13",
            "url": "https://github.com/MantisAI/nervaluate"
          },
          {
            "title": "Client Challenge",
            "url": "https://pypi.org/project/eval4ner/"
          },
          {
            "title": "nervaluate · PyPI",
            "url": "https://pypi.org/project/nervaluate/"
          },
          {
            "title": "Named-Entity evaluation metrics based on entity-level",
            "url": "https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"
          },
          {
            "title": "Named Entity Recognition for Norwegian",
            "url": "https://www.duo.uio.no/bitstream/handle/10852/81384/master-thesis.pdf?sequence=1&isAllowed=y"
          },
          {
            "title": "What are some metrics for Named Entity Recognition? — AI Practitioner Handbook",
            "url": "https://aisingapore.github.io/ai-practitioner-handbook/book/6-modelling/ner-metrics.html"
          },
          {
            "title": "Semeval-2013 task 9: Extraction of drug-drug interactions from biomedical texts (ddiextraction 2013) | Request PDF",
            "url": "https://www.researchgate.net/publication/284650486_Semeval-2013_task_9_Extraction_of_drug-drug_interactions_from_biomedical_texts_ddiextraction_2013"
          },
          {
            "title": "Ychai",
            "url": "https://ychai.uk/notes/2018/11/21/NLP/NER/Evaluation-metrics-of-Name-Entity-Recognition-systems/"
          },
          {
            "title": "SemEval-2013 Task 9 : Extraction of Drug- ...",
            "url": "https://aclanthology.org/S13-2056.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about SemEval 2013 Task 9.1 evaluation metrics for named entities with partial matching:\n\n## Overview\n\nThe SemEval 2013 - 9.1 task defines evaluation metrics for Named Entity Recognition (NER) models. The evaluation metrics go beyond a simple token/tag based schema, and consider different scenarios based on whether all the tokens that belong to a named entity were classified or not, and also whether the correct entity type was assigned.\n\n## Evaluation Schemes\n\nThe SemEval'13 introduced four different ways to measure precision/recall/f1-score results based on the metrics defined by MUC. There are 4 options of measuring the overall performance, which differ in terms of what is considered to be correct, incorrect, partial, missed and spurious predictions, and specifically indicate the correctness of the full named-entities with respect to their boundaries and entity classes.\n\n## Partial Matching Metrics\n\nFor partial matches, Precision = (COR + 0.5 × PAR) / ACT and Recall = (COR + 0.5 × PAR)/POS. This formula gives partial matches a 0.5 weight in the calculation.\n\n## Stringency Levels\n\nIn general, partial will be the most lenient evaluation, while strict will be the most stringent evaluation. The scores for type and exact will usually fall in between."
    ],
    "durationSeconds": 7.234831132999999
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T16:12:23.983Z_

<details><summary>↩ Tool result · `toolu_01X8Nicr2PpzqyRQdBrLYFHB`</summary>

```text
Web search results for query: ""confidence estimation" "named entity recognition" OR "information extraction" LLM calibration 2024 2025"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty","url":"https://arxiv.org/html/2402.10573v3"},{"title":"A Survey of Confidence Estimation and Calibration in ...","url":"https://aclanthology.org/2024.naacl-long.366.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"Efficient medical NER with limited data: Enhancing LLM performance through annotation guidelines - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1386505625004472"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2","url":"https://dl.acm.org/doi/10.1145/3711896.3736569"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"Fact-and-Reflection (FaR) Improves Confidence ...","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2024-far.pdf"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"}]

I've performed the web search for your query on confidence estimation, named entity recognition, information extraction, and LLM calibration. Here are the key findings:

## Major Findings

**Recent Comprehensive Survey (2024):**
A 2024 survey outlines the challenges and summarizes recent technical advancements for LLM confidence estimation and calibration, covering their applications and promising directions for future work.

**Named Entity Recognition with Confidence Estimation:**
LinkNER uses multiple uncertainty estimation techniques including Confidence, Entropy, Monte-Carlo Dropout, and Evidential-based learning for named entity recognition tasks. LinkNER enhances NER task performance, notably surpassing SOTA models in robustness tests.

**Information Extraction Applications:**
In generative information extraction, researchers have utilized LLMs to correct low-confidence results and to calibrate results.

**Uncertainty Quantification in Medical Domain (2025):**
Uncertainty quantification has been studied in NLP tasks such as sentiment analysis, machine translation, and named entity recognition, with work beginning from the seminal research of Guo et al. (2017).

**Calibration Challenges:**
In practice, the alignment between a model's confidence and its actual accuracy matters.

The search results show active research in 2024-2025 on integrating confidence estimation with both NER and information extraction tasks, with particular emphasis on proper calibration of LLM predictions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "0300e2a0-bfeb-4b2b-8deb-fb35396f761b",
  "tool_use_result": {
    "query": "\"confidence estimation\" \"named entity recognition\" OR \"information extraction\" LLM calibration 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JzkQKNessuyHDeQtuFeQvq",
        "content": [
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.366/"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
            "url": "https://arxiv.org/html/2402.10573v3"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in ...",
            "url": "https://aclanthology.org/2024.naacl-long.366.pdf"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"
          },
          {
            "title": "Benchmarking LLM Uncertainty and Calibration with ...",
            "url": "https://aclanthology.org/2026.eacl-long.106.pdf"
          },
          {
            "title": "Efficient medical NER with limited data: Enhancing LLM performance through annotation guidelines - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1386505625004472"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2",
            "url": "https://dl.acm.org/doi/10.1145/3711896.3736569"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"
          },
          {
            "title": "Fact-and-Reflection (FaR) Improves Confidence ...",
            "url": "https://www.cs.cmu.edu/~sherryw/assets/pubs/2024-far.pdf"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          }
        ]
      },
      "I've performed the web search for your query on confidence estimation, named entity recognition, information extraction, and LLM calibration. Here are the key findings:\n\n## Major Findings\n\n**Recent Comprehensive Survey (2024):**\nA 2024 survey outlines the challenges and summarizes recent technical advancements for LLM confidence estimation and calibration, covering their applications and promising directions for future work.\n\n**Named Entity Recognition with Confidence Estimation:**\nLinkNER uses multiple uncertainty estimation techniques including Confidence, Entropy, Monte-Carlo Dropout, and Evidential-based learning for named entity recognition tasks. LinkNER enhances NER task performance, notably surpassing SOTA models in robustness tests.\n\n**Information Extraction Applications:**\nIn generative information extraction, researchers have utilized LLMs to correct low-confidence results and to calibrate results.\n\n**Uncertainty Quantification in Medical Domain (2025):**\nUncertainty quantification has been studied in NLP tasks such as sentiment analysis, machine translation, and named entity recognition, with work beginning from the seminal research of Guo et al. (2017).\n\n**Calibration Challenges:**\nIn practice, the alignment between a model's confidence and its actual accuracy matters.\n\nThe search results show active research in 2024-2025 on integrating confidence estimation with both NER and information extraction tasks, with particular emphasis on proper calibration of LLM predictions."
    ],
    "durationSeconds": 7.437149319000004
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for more papers in the remaining directions. I need:
- Direction A: I have GENRE (De Cao et al., ICLR 2021) and iNERD (Deußer et al., IEEE BigData 2024). Let me search for one more on structured output/constrained decoding for IE.
- Direction B: I have NoiseBench (Merdjanovska et al., EMNLP 2024) and Fine-grained Entity Typing via Label Reasoning (Qing Liu et al., EMNLP 2021). Let me look for one more on annotation disagreement / label ambiguity.


- Direction C: I need to find papers on IE evaluation methodology beyond SemEval 2013 task 9, so I'm looking for evaluation survey papers.
- Direction D: I have the Geng et al. survey (NAACL 2024) and need to find LinkNER plus another paper on confidence estimation for NER/IE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "89ebac32-515e-4277-a903-86a14a7b6b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 49_

继续搜索剩余方向的论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "6b232bb3-e887-464e-bebf-786d2f0b95a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QPgTNotkULiCdnw23tithg`</summary>

```json
{
  "query": "LinkNER linking local named entity recognition large language models uncertainty 2402.10573 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1cf08eb3-bf67-4f62-998e-0f7b1690cb98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 51_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGuqSBdiQumrFsseBRJYCc`</summary>

```json
{
  "query": "\"survey confidence estimation calibration large language models\" Geng NAACL 2024 2311.08298 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "5771393f-8979-43c7-bf71-6206ef2803ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAei3mGqXQjkVYHkDS2oyr`</summary>

```json
{
  "query": "GENRE autoregressive entity retrieval De Cao Izacard Riedel Petroni ICLR 2021 arXiv 2010.00904"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "417abc1a-4175-4b9d-9477-3194958d3808",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 53_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01See8zVJArbLpX95EaAWrTs`</summary>

```json
{
  "query": "entity evaluation SemEval MUC named entity recognition evaluation metrics survey paper 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d4170c87-67e9-4ce1-95a2-e2418767597c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cw8JHNwfnbtxMEEeLnyPaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 843,
      "cache_creation_input_tokens": 5469,
      "cache_read_input_tokens": 38136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5469
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

_source line 54 · 2026-05-15T16:12:39.333Z_

<details><summary>↩ Tool result · `toolu_01KGuqSBdiQumrFsseBRJYCc`</summary>

```text
Web search results for query: ""survey confidence estimation calibration large language models" Geng NAACL 2024 2311.08298 authors"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.366/"},{"title":"[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298"},{"title":"A Survey of Confidence Estimation and Calibration in ...","url":"https://aclanthology.org/2024.naacl-long.366.pdf"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/html/2311.08298v2"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2311.08298v2"},{"title":"[PDF] A Survey of Confidence Estimation and Calibration in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Confidence-Estimation-and-Calibration-Geng-Cai/6aa6003c7d7b3d275ae981aa6200014968c32430"},{"title":"[2311.08298v2] A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://arxiv.org/abs/2311.08298v2"},{"title":"A Survey of Language Model Confidence Estimation and Calibration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-of-Language-Model-Confidence-Estimation-Geng-Cai/1ebc475ae96503eb2e9aa0b5904564c85b834a96"},{"title":"A Survey of Confidence Estimation and Calibration ...","url":"https://lingo.iitgn.ac.in/nlpexplorer/paper/2024.naacl-long.366"}]

I found the paper you're looking for! Here's the information about the survey:

## Paper Details

**Title:** A Survey of Confidence Estimation and Calibration in Large Language Models

**Authors:** Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych

**Venue:** Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024), pages 6577–6595, Mexico City, Mexico

**ArXiv ID:** 2311.08298 (v2 submitted March 25, 2024)

## Paper Overview

The survey addresses how large language models (LLMs) have demonstrated remarkable capabilities but can be unreliable due to factual errors in their generations. Assessing their confidence and calibrating them across different tasks can help mitigate risks and enable LLMs to produce better generations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "30b6d979-d4b5-4929-be39-e55cda657ffa",
  "tool_use_result": {
    "query": "\"survey confidence estimation calibration large language models\" Geng NAACL 2024 2311.08298 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RMqLReDDHVub5PJaAkF7mk",
        "content": [
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.366/"
          },
          {
            "title": "[2311.08298] A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2311.08298"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in ...",
            "url": "https://aclanthology.org/2024.naacl-long.366.pdf"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2311.08298v2"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2311.08298v2"
          },
          {
            "title": "[PDF] A Survey of Confidence Estimation and Calibration in Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-Survey-of-Confidence-Estimation-and-Calibration-Geng-Cai/6aa6003c7d7b3d275ae981aa6200014968c32430"
          },
          {
            "title": "[2311.08298v2] A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2311.08298v2"
          },
          {
            "title": "A Survey of Language Model Confidence Estimation and Calibration | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-Survey-of-Language-Model-Confidence-Estimation-Geng-Cai/1ebc475ae96503eb2e9aa0b5904564c85b834a96"
          },
          {
            "title": "A Survey of Confidence Estimation and Calibration ...",
            "url": "https://lingo.iitgn.ac.in/nlpexplorer/paper/2024.naacl-long.366"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about the survey:\n\n## Paper Details\n\n**Title:** A Survey of Confidence Estimation and Calibration in Large Language Models\n\n**Authors:** Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych\n\n**Venue:** Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024), pages 6577–6595, Mexico City, Mexico\n\n**ArXiv ID:** 2311.08298 (v2 submitted March 25, 2024)\n\n## Paper Overview\n\nThe survey addresses how large language models (LLMs) have demonstrated remarkable capabilities but can be unreliable due to factual errors in their generations. Assessing their confidence and calibrating them across different tasks can help mitigate risks and enable LLMs to produce better generations."
    ],
    "durationSeconds": 4.726727532000004
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T16:12:39.431Z_

<details><summary>↩ Tool result · `toolu_01QPgTNotkULiCdnw23tithg`</summary>

```text
Web search results for query: "LinkNER linking local named entity recognition large language models uncertainty 2402.10573 authors venue"

Links: [{"title":"[2402.10573] LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty","url":"https://arxiv.org/abs/2402.10573"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty","url":"https://arxiv.org/html/2402.10573"},{"title":"LinkNER: Linking Local Named Entity Recognition Models ...","url":"https://arxiv.org/pdf/2402.10573"},{"title":"GitHub - zhzhengit/LinkNER: Repo for LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty","url":"https://github.com/zhzhengit/LinkNER"},{"title":"LinkNER: Linking Local Named Entity Recognition Models ...","url":"https://www.alphaxiv.org/overview/2402.10573v3"},{"title":"[Literature Review] LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty","url":"https://www.themoonlight.io/en/review/linkner-linking-local-named-entity-recognition-models-to-large-language-models-using-uncertainty"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | OpenReview","url":"https://openreview.net/forum?id=9fkOcX5dGT"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645414"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Request PDF","url":"https://www.researchgate.net/publication/380539010_LinkNER_Linking_Local_Named_Entity_Recognition_Models_to_Large_Language_Models_using_Uncertainty"},{"title":"(PDF) Deploying large language models for discourse studies: An exploration of automated analysis of media attitudes","url":"https://www.researchgate.net/publication/387868230_Deploying_large_language_models_for_discourse_studies_An_exploration_of_automated_analysis_of_media_attitudes"}]

Based on the search results, here is the information about the LinkNER paper (arXiv:2402.10573):

## Authors
The authors are Zhen Zhang, Yuhua Zhao, Hang Gao, and Mengting Hu.

## Venue
The paper was published in the Proceedings of the ACM Web Conference 2024 (WWW '24) held May 13–17, 2024 in Singapore.

## Paper Overview
LinkNER proposes a framework that combines small fine-tuned models with LLMs and an uncertainty-based linking strategy called RDC that enables fine-tuned models to complement black-box LLMs, achieving better performance.

The work addresses the limitation that fine-tuned NER models perform poorly on unseen entity recognition, while LLMs like GPT-4 possess extensive external knowledge, but lack specialty for NER tasks.

LinkNER enhances NER task performance, notably surpassing SOTA models in robustness tests.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "ba094ba0-96a1-4eca-bc91-8d802200faea",
  "tool_use_result": {
    "query": "LinkNER linking local named entity recognition large language models uncertainty 2402.10573 authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SrrUz88eoYcD8esbJMk3Pi",
        "content": [
          {
            "title": "[2402.10573] LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
            "url": "https://arxiv.org/abs/2402.10573"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
            "url": "https://arxiv.org/html/2402.10573"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models ...",
            "url": "https://arxiv.org/pdf/2402.10573"
          },
          {
            "title": "GitHub - zhzhengit/LinkNER: Repo for LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
            "url": "https://github.com/zhzhengit/LinkNER"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models ...",
            "url": "https://www.alphaxiv.org/overview/2402.10573v3"
          },
          {
            "title": "[Literature Review] LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
            "url": "https://www.themoonlight.io/en/review/linkner-linking-local-named-entity-recognition-models-to-large-language-models-using-uncertainty"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | OpenReview",
            "url": "https://openreview.net/forum?id=9fkOcX5dGT"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024",
            "url": "https://dl.acm.org/doi/10.1145/3589334.3645414"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Request PDF",
            "url": "https://www.researchgate.net/publication/380539010_LinkNER_Linking_Local_Named_Entity_Recognition_Models_to_Large_Language_Models_using_Uncertainty"
          },
          {
            "title": "(PDF) Deploying large language models for discourse studies: An exploration of automated analysis of media attitudes",
            "url": "https://www.researchgate.net/publication/387868230_Deploying_large_language_models_for_discourse_studies_An_exploration_of_automated_analysis_of_media_attitudes"
          }
        ]
      },
      "Based on the search results, here is the information about the LinkNER paper (arXiv:2402.10573):\n\n## Authors\nThe authors are Zhen Zhang, Yuhua Zhao, Hang Gao, and Mengting Hu.\n\n## Venue\nThe paper was published in the Proceedings of the ACM Web Conference 2024 (WWW '24) held May 13–17, 2024 in Singapore.\n\n## Paper Overview\nLinkNER proposes a framework that combines small fine-tuned models with LLMs and an uncertainty-based linking strategy called RDC that enables fine-tuned models to complement black-box LLMs, achieving better performance.\n\nThe work addresses the limitation that fine-tuned NER models perform poorly on unseen entity recognition, while LLMs like GPT-4 possess extensive external knowledge, but lack specialty for NER tasks.\n\nLinkNER enhances NER task performance, notably surpassing SOTA models in robustness tests."
    ],
    "durationSeconds": 5.783727067000014
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T16:12:43.383Z_

<details><summary>↩ Tool result · `toolu_01QAei3mGqXQjkVYHkDS2oyr`</summary>

```text
Web search results for query: "GENRE autoregressive entity retrieval De Cao Izacard Riedel Petroni ICLR 2021 arXiv 2010.00904"

Links: [{"title":"Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL","url":"https://openreview.net/pdf?id=5k8F6UU39V"},{"title":"GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub","url":"https://github.com/facebookresearch/GENRE"},{"title":"Autoregressive Entity Retrieval - AI at Meta","url":"https://ai.meta.com/research/publications/autoregressive-entry-retrieval/"},{"title":"Papers with Code - Autoregressive Entity Retrieval","url":"https://paperswithcode.com/paper/autoregressive-entity-retrieval"},{"title":"(PDF) Autoregressive Entity Retrieval","url":"https://www.researchgate.net/publication/344468840_Autoregressive_Entity_Retrieval"},{"title":"Track: Oral Session 4","url":"https://iclr.cc/virtual/2021/session/4331"},{"title":"ICLR Spotlight Autoregressive Entity Retrieval","url":"https://iclr.cc/virtual/2021/spotlight/3521"},{"title":"Autoregressive Entity Retrieval - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201000904D/abstract"},{"title":"Autoregressive Entity Retrieval | OpenReview","url":"https://openreview.net/forum?id=5k8F6UU39V"},{"title":"[PDF] Autoregressive Entity Retrieval | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Autoregressive-Entity-Retrieval-Cao-Izacard/572c12e81319ccd47cc0c637c82efadd03fd05ab"}]

I found comprehensive information about GENRE. Here are the key findings:

## Overview

GENRE is an autoregressive entity retrieval system by Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni, published at ICLR 2021. The paper is identified with arXiv ID 2010.00904.

## Key Innovation

GENRE is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion and conditioned on the context.

## Technical Advantages

The autoregressive formulation allows direct capture of relations between context and entity name, effectively cross encoding both; the memory footprint is greatly reduced because the parameters scale with vocabulary size, not entity count; and the exact softmax loss can be efficiently computed without subsampling negative data.

## Performance and Results

The system was tested with more than 20 datasets on entity disambiguation, end-to-end entity linking and document retrieval tasks, achieving new state-of-the-art or very competitive results while using a tiny fraction of the memory footprint of competing systems. Compared with recent models, GENRE requires substantially less memory (∼20 times smaller footprint on average).

## Availability

Code and pre-trained models are available at https://github.com/facebookresearch/GENRE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "8be6ce55-bd88-4897-985d-78be6bf6f520",
  "tool_use_result": {
    "query": "GENRE autoregressive entity retrieval De Cao Izacard Riedel Petroni ICLR 2021 arXiv 2010.00904",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FrcooGymsMdCFSmuzspXAt",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2021 AUTOREGRESSIVE ENTITY RETRIEVAL",
            "url": "https://openreview.net/pdf?id=5k8F6UU39V"
          },
          {
            "title": "GitHub - facebookresearch/GENRE: Autoregressive Entity Retrieval · GitHub",
            "url": "https://github.com/facebookresearch/GENRE"
          },
          {
            "title": "Autoregressive Entity Retrieval - AI at Meta",
            "url": "https://ai.meta.com/research/publications/autoregressive-entry-retrieval/"
          },
          {
            "title": "Papers with Code - Autoregressive Entity Retrieval",
            "url": "https://paperswithcode.com/paper/autoregressive-entity-retrieval"
          },
          {
            "title": "(PDF) Autoregressive Entity Retrieval",
            "url": "https://www.researchgate.net/publication/344468840_Autoregressive_Entity_Retrieval"
          },
          {
            "title": "Track: Oral Session 4",
            "url": "https://iclr.cc/virtual/2021/session/4331"
          },
          {
            "title": "ICLR Spotlight Autoregressive Entity Retrieval",
            "url": "https://iclr.cc/virtual/2021/spotlight/3521"
          },
          {
            "title": "Autoregressive Entity Retrieval - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv201000904D/abstract"
          },
          {
            "title": "Autoregressive Entity Retrieval | OpenReview",
            "url": "https://openreview.net/forum?id=5k8F6UU39V"
          },
          {
            "title": "[PDF] Autoregressive Entity Retrieval | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Autoregressive-Entity-Retrieval-Cao-Izacard/572c12e81319ccd47cc0c637c82efadd03fd05ab"
          }
        ]
      },
      "I found comprehensive information about GENRE. Here are the key findings:\n\n## Overview\n\nGENRE is an autoregressive entity retrieval system by Nicola De Cao, Gautier Izacard, Sebastian Riedel, and Fabio Petroni, published at ICLR 2021. The paper is identified with arXiv ID 2010.00904.\n\n## Key Innovation\n\nGENRE is the first system that retrieves entities by generating their unique names, left to right, token-by-token in an autoregressive fashion and conditioned on the context.\n\n## Technical Advantages\n\nThe autoregressive formulation allows direct capture of relations between context and entity name, effectively cross encoding both; the memory footprint is greatly reduced because the parameters scale with vocabulary size, not entity count; and the exact softmax loss can be efficiently computed without subsampling negative data.\n\n## Performance and Results\n\nThe system was tested with more than 20 datasets on entity disambiguation, end-to-end entity linking and document retrieval tasks, achieving new state-of-the-art or very competitive results while using a tiny fraction of the memory footprint of competing systems. Compared with recent models, GENRE requires substantially less memory (∼20 times smaller footprint on average).\n\n## Availability\n\nCode and pre-trained models are available at https://github.com/facebookresearch/GENRE."
    ],
    "durationSeconds": 6.834647090999992
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T16:12:43.561Z_

<details><summary>↩ Tool result · `toolu_01See8zVJArbLpX95EaAWrTs`</summary>

```text
Web search results for query: "entity evaluation SemEval MUC named entity recognition evaluation metrics survey paper 2023 2024"

Links: [{"title":"GitHub - davidsbatista/NER-Evaluation: An implementation of a full named-entity evaluation metrics based on SemEval'13 Task 9 - not at tag/token level but considering all the tokens that are part of the named-entity","url":"https://github.com/davidsbatista/NER-Evaluation"},{"title":"What are some metrics for Named Entity Recognition? — AI Practitioner Handbook","url":"https://aisingapore.github.io/ai-practitioner-handbook/book/6-modelling/ner-metrics.html"},{"title":"Named-Entity evaluation metrics based on entity-level","url":"https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"},{"title":"GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13","url":"https://github.com/MantisAI/nervaluate"},{"title":"SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ACL Anthology","url":"https://aclanthology.org/2023.semeval-1.310/"},{"title":"A survey on Named Entity Recognition — datasets, tools, and methodologies - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949719123000146"},{"title":"GitHub - cyk1337/eval4ner: [PyPI] NER MUC evaluation toolkit in Python · GitHub","url":"https://github.com/cyk1337/eval4ner"},{"title":"SemEval 2023 Task 2: MultiCoNER II&lt;/br>&lt;b>Multi&lt;/b>lingual &lt;b>Co&lt;/b>mplex &lt;b>N&lt;/b>amed &lt;b>E&lt;/b>ntity &lt;b>R&lt;/b>ecognition","url":"https://multiconer.github.io/paper"},{"title":"Everything you need to know about Named Entity Recognition! | by Uma Gunturi | Medium","url":"https://umagunturi789.medium.com/everything-you-need-to-know-about-named-entity-recognition-2a136f38c08f"},{"title":"[2305.06586] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)","url":"https://arxiv.org/abs/2305.06586"}]

I've completed the web search for your query about entity evaluation, SemEval, MUC, and named entity recognition evaluation metrics. Here are the key findings:

## Evaluation Metrics Overview

The SemEval scheme is built off the Message Understanding Conference (MUC) scheme. The SemEval'13 introduced four different ways to measure precision/recall/f1-score results based on the metrics defined by MUC.

## SemEval-2023 NER Task

One of the most prominent recent NER evaluation efforts is SemEval-2023 Task 2 on Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2), which focused on methods to identify complex fine-grained named entities across 12 languages, in both monolingual and multilingual scenarios, as well as noisy settings. It attracted 842 submissions from 47 teams, and 34 teams submitted system papers.

## Evaluation Metrics Categories

In the SemEval scheme, there are 4 options of measuring the overall performance, which differ in terms of what is considered to be correct, incorrect, partial, missed and spurious predictions, and specifically indicate the correctness of the full named-entities with respect to their boundaries and entity classes.

## NER Survey Resources

A survey on Named Entity Recognition covers datasets, tools, and methodologies, with references to MUC-7 named entity task definitions.

The search results show active research in this area with recent SemEval tasks and comprehensive survey materials available on NER evaluation metrics and methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "58f44350-fa5f-4e81-b912-d0eafdcb153c",
  "tool_use_result": {
    "query": "entity evaluation SemEval MUC named entity recognition evaluation metrics survey paper 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YAz7KBu8D4NMEfaHeoyoHm",
        "content": [
          {
            "title": "GitHub - davidsbatista/NER-Evaluation: An implementation of a full named-entity evaluation metrics based on SemEval'13 Task 9 - not at tag/token level but considering all the tokens that are part of the named-entity",
            "url": "https://github.com/davidsbatista/NER-Evaluation"
          },
          {
            "title": "What are some metrics for Named Entity Recognition? — AI Practitioner Handbook",
            "url": "https://aisingapore.github.io/ai-practitioner-handbook/book/6-modelling/ner-metrics.html"
          },
          {
            "title": "Named-Entity evaluation metrics based on entity-level",
            "url": "https://www.davidsbatista.net/blog/2018/05/09/Named_Entity_Evaluation/"
          },
          {
            "title": "GitHub - MantisAI/nervaluate: Full named-entity (i.e., not tag/token) evaluation metrics based on SemEval’13",
            "url": "https://github.com/MantisAI/nervaluate"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ACL Anthology",
            "url": "https://aclanthology.org/2023.semeval-1.310/"
          },
          {
            "title": "A survey on Named Entity Recognition — datasets, tools, and methodologies - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2949719123000146"
          },
          {
            "title": "GitHub - cyk1337/eval4ner: [PyPI] NER MUC evaluation toolkit in Python · GitHub",
            "url": "https://github.com/cyk1337/eval4ner"
          },
          {
            "title": "SemEval 2023 Task 2: MultiCoNER II&lt;/br>&lt;b>Multi&lt;/b>lingual &lt;b>Co&lt;/b>mplex &lt;b>N&lt;/b>amed &lt;b>E&lt;/b>ntity &lt;b>R&lt;/b>ecognition",
            "url": "https://multiconer.github.io/paper"
          },
          {
            "title": "Everything you need to know about Named Entity Recognition! | by Uma Gunturi | Medium",
            "url": "https://umagunturi789.medium.com/everything-you-need-to-know-about-named-entity-recognition-2a136f38c08f"
          },
          {
            "title": "[2305.06586] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)",
            "url": "https://arxiv.org/abs/2305.06586"
          }
        ]
      },
      "I've completed the web search for your query about entity evaluation, SemEval, MUC, and named entity recognition evaluation metrics. Here are the key findings:\n\n## Evaluation Metrics Overview\n\nThe SemEval scheme is built off the Message Understanding Conference (MUC) scheme. The SemEval'13 introduced four different ways to measure precision/recall/f1-score results based on the metrics defined by MUC.\n\n## SemEval-2023 NER Task\n\nOne of the most prominent recent NER evaluation efforts is SemEval-2023 Task 2 on Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2), which focused on methods to identify complex fine-grained named entities across 12 languages, in both monolingual and multilingual scenarios, as well as noisy settings. It attracted 842 submissions from 47 teams, and 34 teams submitted system papers.\n\n## Evaluation Metrics Categories\n\nIn the SemEval scheme, there are 4 options of measuring the overall performance, which differ in terms of what is considered to be correct, incorrect, partial, missed and spurious predictions, and specifically indicate the correctness of the full named-entities with respect to their boundaries and entity classes.\n\n## NER Survey Resources\n\nA survey on Named Entity Recognition covers datasets, tools, and methodologies, with references to MUC-7 named entity task definitions.\n\nThe search results show active research in this area with recent SemEval tasks and comprehensive survey materials available on NER evaluation metrics and methodologies."
    ],
    "durationSeconds": 6.677461259999997
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
I need a few more papers. Let me search for:
1. A specific IE evaluation paper (not just SemEval task) - maybe the Fu et al. evaluation paper or something similar
2. Another paper for direction B (annotation disagreement)
3. Maybe one more for direction D

Let me search for more papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d277933f-8450-4d03-8342-625de80f892d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hz3nX8S9vxe7JA6MfvAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 43605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4983
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

_source line 59_

搜索更多具体论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d76ad7df-fff3-490a-8465-02d4249a5367",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hz3nX8S9vxe7JA6MfvAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 43605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4983
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSdgoZoqb1t6ut5BjbFPBm`</summary>

```json
{
  "query": "\"rethinking evaluation\" \"named entity recognition\" OR \"information extraction\" evaluation limitations 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "a753f073-cb4a-4345-b013-e64caf69bdab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hz3nX8S9vxe7JA6MfvAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 43605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4983
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

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XvdpWHDuJ9Fz6XVSk2kSdJ`</summary>

```json
{
  "query": "annotation disagreement NER inter-annotator agreement label consistency named entity 2020 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "791a7b76-28f7-4b10-9e90-b49df6ce185c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hz3nX8S9vxe7JA6MfvAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 43605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4983
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

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XsfWoYe8jgs8sozyHE3MpJ`</summary>

```json
{
  "query": "Fact-and-Reflection FaR confidence calibration LLM NLP 2024 arXiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "4c9adc9e-9e7c-48ca-b5f7-2784b42fd086",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hz3nX8S9vxe7JA6MfvAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4983,
      "cache_read_input_tokens": 43605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4983
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

_source line 63 · 2026-05-15T16:12:54.975Z_

<details><summary>↩ Tool result · `toolu_01MSdgoZoqb1t6ut5BjbFPBm`</summary>

```text
Web search results for query: ""rethinking evaluation" "named entity recognition" OR "information extraction" evaluation limitations 2024 2025"

Links: [{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"A survey on recent advances in Named Entity Recognition","url":"https://arxiv.org/html/2401.10825v1"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"A review of named entity recognition: from learning ...","url":"https://sentic.net/named-entity-recognition.pdf"},{"title":"A multi-level feature enhancement framework for named entity recognition in power system texts | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-32884-0"},{"title":"JMIR AI - Exploring Named Entity Recognition Potential and the Value of Tailored Natural Language Processing Pipelines for Radiology, Pathology, and Progress Notes in Clinical Decision Support: Quantitative Study","url":"https://ai.jmir.org/2025/1/e59251/"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"A review of named entity recognition: from learning methods to ...","url":"https://researchonline.jcu.edu.au/86126/1/s10462-025-11321-8.pdf"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"}]

I've completed the web search for your query about "rethinking evaluation" in named entity recognition and information extraction. Here are the key findings:

## Key Results Found:

**Recent Surveys and Reviews (2024-2025):**
- A 2024-2025 review of NER found that pre-trained NER models are limited in their ability to model new entities and disambiguate their context.
- A recent survey examined graph- and transformer-based methods including LLMs and evaluated the performance of main NER implementations on a variety of datasets with differing characteristics, providing a deep comparison of algorithms.

**Evaluation and Benchmark Issues:**
- A 2024 study developed a new benchmark dataset called Noisebench for evaluating NER, which covers different types of noise in labels such as expert errors and automatic annotation errors.

**Rethinking Evaluation in Generative Information Extraction:**
- "GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models" appears to be an active research direction addressing evaluation limitations in the context of LLMs.

**LLM Limitations for IE:**
- LLMs have several disadvantages including the requirement for a large training dataset for pretraining, high computational costs and problems of bias and hallucination.

The search results indicate an active research area focusing on reconsidering how to evaluate NER and information extraction systems, particularly as these tasks move into the era of generative models and large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "192525e3-a377-420f-8e00-f2e86faca843",
  "tool_use_result": {
    "query": "\"rethinking evaluation\" \"named entity recognition\" OR \"information extraction\" evaluation limitations 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012x7CXGSUYfQh4G6nQqFTWk",
        "content": [
          {
            "title": "A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11321-8"
          },
          {
            "title": "A survey on recent advances in Named Entity Recognition",
            "url": "https://arxiv.org/html/2401.10825v1"
          },
          {
            "title": "Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study",
            "url": "https://arxiv.org/html/2401.10825v3"
          },
          {
            "title": "A review of named entity recognition: from learning ...",
            "url": "https://sentic.net/named-entity-recognition.pdf"
          },
          {
            "title": "A multi-level feature enhancement framework for named entity recognition in power system texts | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-32884-0"
          },
          {
            "title": "JMIR AI - Exploring Named Entity Recognition Potential and the Value of Tailored Natural Language Processing Pipelines for Radiology, Pathology, and Progress Notes in Clinical Decision Support: Quantitative Study",
            "url": "https://ai.jmir.org/2025/1/e59251/"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          },
          {
            "title": "A review of named entity recognition: from learning methods to ...",
            "url": "https://researchonline.jcu.edu.au/86126/1/s10462-025-11321-8.pdf"
          },
          {
            "title": "GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction",
            "url": "https://github.com/zjunlp/Low-resource-KEPapers"
          }
        ]
      },
      "I've completed the web search for your query about \"rethinking evaluation\" in named entity recognition and information extraction. Here are the key findings:\n\n## Key Results Found:\n\n**Recent Surveys and Reviews (2024-2025):**\n- A 2024-2025 review of NER found that pre-trained NER models are limited in their ability to model new entities and disambiguate their context.\n- A recent survey examined graph- and transformer-based methods including LLMs and evaluated the performance of main NER implementations on a variety of datasets with differing characteristics, providing a deep comparison of algorithms.\n\n**Evaluation and Benchmark Issues:**\n- A 2024 study developed a new benchmark dataset called Noisebench for evaluating NER, which covers different types of noise in labels such as expert errors and automatic annotation errors.\n\n**Rethinking Evaluation in Generative Information Extraction:**\n- \"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\" appears to be an active research direction addressing evaluation limitations in the context of LLMs.\n\n**LLM Limitations for IE:**\n- LLMs have several disadvantages including the requirement for a large training dataset for pretraining, high computational costs and problems of bias and hallucination.\n\nThe search results indicate an active research area focusing on reconsidering how to evaluate NER and information extraction systems, particularly as these tasks move into the era of generative models and large language models."
    ],
    "durationSeconds": 7.027206634999995
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T16:12:56.823Z_

<details><summary>↩ Tool result · `toolu_01XsfWoYe8jgs8sozyHE3MpJ`</summary>

```text
Web search results for query: "Fact-and-Reflection FaR confidence calibration LLM NLP 2024 arXiv authors"

Links: [{"title":"[2402.17124] Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models","url":"https://arxiv.org/abs/2402.17124"},{"title":"Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models","url":"https://arxiv.org/html/2402.17124v1"},{"title":"Fact-and-Reflection (FaR) Improves Confidence ...","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2024-far.pdf"},{"title":"Benchmarking Uncertainty Calibration in Large Language Model Long-Form Question Answering","url":"https://arxiv.org/html/2602.00279v1"},{"title":"Factuality of Large Language Models in the Year 2024","url":"https://arxiv.org/html/2402.02420v2"},{"title":"Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.515/"},{"title":"Reasoning Helps Surface Self-Confidence Signals in LLMs","url":"https://arxiv.org/pdf/2505.23845"},{"title":"Preprint 2026 FACT-CHECKING WITH LARGE LANGUAGE MODELS","url":"https://www.arxiv.org/pdf/2601.02574"},{"title":"Factual Confidence of LLMs: on Reliability and Robustness of Current Estimators","url":"https://arxiv.org/html/2406.13415v1"},{"title":"Fact-Checking with Large Language Models via Probabilistic Certainty and Consistency","url":"https://arxiv.org/html/2601.02574"}]

Based on the search results, here's what I found about the Fact-and-Reflection (FaR) paper:

## Paper Details

Fact-and-Reflection (FaR) prompting improves LLM calibration in two steps: first, it elicits the known "facts" that are relevant to the input prompt from the LLM, and then it asks the model to "reflect" over them to generate the final answer.

## Authors

The authors are Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, and Jianshu Chen.

## Publication Details

The paper was published in the Findings of the Association for Computational Linguistics: ACL 2024 in August 2024, in Bangkok, Thailand. The arXiv version is 2402.17124, with the initial submission on February 27, 2024.

## Key Results

The paper shows that FaR prompting achieves significantly better calibration, lowering the Expected Calibration Error by 23.5% on multi-purpose QA tasks. Additionally, FaR prompting elicits the capability of verbally expressing concerns in less confident scenarios, which helps trigger retrieval augmentation for solving harder instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "acf61f8c-e7ab-4ea9-9f29-2ae27f6a228d",
  "tool_use_result": {
    "query": "Fact-and-Reflection FaR confidence calibration LLM NLP 2024 arXiv authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01So9uF7dnAYxUNZHTqYEjfd",
        "content": [
          {
            "title": "[2402.17124] Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models",
            "url": "https://arxiv.org/abs/2402.17124"
          },
          {
            "title": "Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models",
            "url": "https://arxiv.org/html/2402.17124v1"
          },
          {
            "title": "Fact-and-Reflection (FaR) Improves Confidence ...",
            "url": "https://www.cs.cmu.edu/~sherryw/assets/pubs/2024-far.pdf"
          },
          {
            "title": "Benchmarking Uncertainty Calibration in Large Language Model Long-Form Question Answering",
            "url": "https://arxiv.org/html/2602.00279v1"
          },
          {
            "title": "Factuality of Large Language Models in the Year 2024",
            "url": "https://arxiv.org/html/2402.02420v2"
          },
          {
            "title": "Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-acl.515/"
          },
          {
            "title": "Reasoning Helps Surface Self-Confidence Signals in LLMs",
            "url": "https://arxiv.org/pdf/2505.23845"
          },
          {
            "title": "Preprint 2026 FACT-CHECKING WITH LARGE LANGUAGE MODELS",
            "url": "https://www.arxiv.org/pdf/2601.02574"
          },
          {
            "title": "Factual Confidence of LLMs: on Reliability and Robustness of Current Estimators",
            "url": "https://arxiv.org/html/2406.13415v1"
          },
          {
            "title": "Fact-Checking with Large Language Models via Probabilistic Certainty and Consistency",
            "url": "https://arxiv.org/html/2601.02574"
          }
        ]
      },
      "Based on the search results, here's what I found about the Fact-and-Reflection (FaR) paper:\n\n## Paper Details\n\nFact-and-Reflection (FaR) prompting improves LLM calibration in two steps: first, it elicits the known \"facts\" that are relevant to the input prompt from the LLM, and then it asks the model to \"reflect\" over them to generate the final answer.\n\n## Authors\n\nThe authors are Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, and Jianshu Chen.\n\n## Publication Details\n\nThe paper was published in the Findings of the Association for Computational Linguistics: ACL 2024 in August 2024, in Bangkok, Thailand. The arXiv version is 2402.17124, with the initial submission on February 27, 2024.\n\n## Key Results\n\nThe paper shows that FaR prompting achieves significantly better calibration, lowering the Expected Calibration Error by 23.5% on multi-purpose QA tasks. Additionally, FaR prompting elicits the capability of verbally expressing concerns in less confident scenarios, which helps trigger retrieval augmentation for solving harder instances."
    ],
    "durationSeconds": 7.5450836500000005
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-15T16:12:56.889Z_

<details><summary>↩ Tool result · `toolu_01XvdpWHDuJ9Fz6XVSk2kSdJ`</summary>

```text
Web search results for query: "annotation disagreement NER inter-annotator agreement label consistency named entity 2020 2021 2022"

Links: [{"title":"DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition","url":"https://arxiv.org/html/2604.15866v1"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Annotation Metrics · Prodigy · An annotation tool for AI, Machine Learning & NLP","url":"https://prodi.gy/docs/metrics"},{"title":"Inter-Annotator Agreement: a key metric in Labeling","url":"https://www.innovatiana.com/en/post/inter-annotator-agreement"},{"title":"The Ultimate Guide to Annotation Schemes","url":"https://www.numberanalytics.com/blog/ultimate-guide-to-annotation-schemes"},{"title":"Measuring Annotator Agreement Generally across Complex Structured, Multi-object, and Free-text Annotation Tasks","url":"https://dl.acm.org/doi/fullHtml/10.1145/3485447.3512242"},{"title":"GitHub - ml-for-nlp/annotator-agreement: Inter-annotator agreement tutorial. Technique: Cohen's Kappa. · GitHub","url":"https://github.com/ml-for-nlp/annotator-agreement"},{"title":"Annotating Named Entities in Consumer Health Questions","url":"https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub9349.pdf"},{"title":"Cohen, Fleiss & Krippendorff: IAA Metrics & Implementation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/inter-annotator-agreement-kappa-alpha-reliability"},{"title":"Inter-Annotator Agreement in Multi-Annotator Labeling Explained - Rise Data Labs Blog","url":"https://risedatalabs.com/blog/inter-annotator-agreement"}]

I've completed a web search on annotation disagreement, inter-annotator agreement, label consistency, and NER (Named Entity Recognition). Here are the key findings:

## Recent Research and Frameworks

DiZiNER is a framework that simulates pilot annotation using LLMs as both annotators and supervisors for zero-shot Named Entity Recognition. Multiple heterogeneous open-source LLMs act as annotators labeling shared texts, and a supervisor LLM analyzes and categorizes inter-model disagreements to refine both common and model-specific instructions.

## Inter-Annotator Agreement Metrics

As annotation and evaluation tasks continue to expand from categorical labeling to segmentation and subjective judgment, measuring agreement between annotators has become increasingly more complex, with papers outlining how inter-annotator agreement (IAA) has been conceptualized and applied across NLP and related disciplines.

For NER specifically, in named entity recognition tasks where annotators highlight spans corresponding to entities, a common approach is to treat one annotator's annotations as a predicted set of spans and another's as the gold set, then compute precision, recall, and F1 score between them.

For token-based annotations, notably NER but any other span based annotations, the recommended metric is the average pairwise F1 score.

## Sources of Disagreement

When annotators systematically disagree on entity boundaries in NER or on whether a statement constitutes a "hallucination," the annotation guidelines need clarification. Disagreement patterns reveal different problems: isolated disagreements indicate attention errors, category-level disagreements indicate unclear guidelines, and persistent expert disagreement indicates genuine task ambiguity.

## Practical Applications

For machine learning, the danger is not disagreement itself but unmeasured disagreement, as models trained on single-annotator labels silently learn individual quirks and biases that surface as brittle behavior, poor generalization, and fairness issues when deployed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "e061f2a7-f5ea-4f8f-92d5-4723321d84f3",
  "tool_use_result": {
    "query": "annotation disagreement NER inter-annotator agreement label consistency named entity 2020 2021 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_015EEsdSMpHaduTUYYpLSN2Q",
        "content": [
          {
            "title": "DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition",
            "url": "https://arxiv.org/html/2604.15866v1"
          },
          {
            "title": "Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation",
            "url": "https://arxiv.org/html/2603.06865"
          },
          {
            "title": "Annotation Metrics · Prodigy · An annotation tool for AI, Machine Learning & NLP",
            "url": "https://prodi.gy/docs/metrics"
          },
          {
            "title": "Inter-Annotator Agreement: a key metric in Labeling",
            "url": "https://www.innovatiana.com/en/post/inter-annotator-agreement"
          },
          {
            "title": "The Ultimate Guide to Annotation Schemes",
            "url": "https://www.numberanalytics.com/blog/ultimate-guide-to-annotation-schemes"
          },
          {
            "title": "Measuring Annotator Agreement Generally across Complex Structured, Multi-object, and Free-text Annotation Tasks",
            "url": "https://dl.acm.org/doi/fullHtml/10.1145/3485447.3512242"
          },
          {
            "title": "GitHub - ml-for-nlp/annotator-agreement: Inter-annotator agreement tutorial. Technique: Cohen's Kappa. · GitHub",
            "url": "https://github.com/ml-for-nlp/annotator-agreement"
          },
          {
            "title": "Annotating Named Entities in Consumer Health Questions",
            "url": "https://lhncbc.nlm.nih.gov/LHC-publications/PDF/pub9349.pdf"
          },
          {
            "title": "Cohen, Fleiss & Krippendorff: IAA Metrics & Implementation - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/inter-annotator-agreement-kappa-alpha-reliability"
          },
          {
            "title": "Inter-Annotator Agreement in Multi-Annotator Labeling Explained - Rise Data Labs Blog",
            "url": "https://risedatalabs.com/blog/inter-annotator-agreement"
          }
        ]
      },
      "I've completed a web search on annotation disagreement, inter-annotator agreement, label consistency, and NER (Named Entity Recognition). Here are the key findings:\n\n## Recent Research and Frameworks\n\nDiZiNER is a framework that simulates pilot annotation using LLMs as both annotators and supervisors for zero-shot Named Entity Recognition. Multiple heterogeneous open-source LLMs act as annotators labeling shared texts, and a supervisor LLM analyzes and categorizes inter-model disagreements to refine both common and model-specific instructions.\n\n## Inter-Annotator Agreement Metrics\n\nAs annotation and evaluation tasks continue to expand from categorical labeling to segmentation and subjective judgment, measuring agreement between annotators has become increasingly more complex, with papers outlining how inter-annotator agreement (IAA) has been conceptualized and applied across NLP and related disciplines.\n\nFor NER specifically, in named entity recognition tasks where annotators highlight spans corresponding to entities, a common approach is to treat one annotator's annotations as a predicted set of spans and another's as the gold set, then compute precision, recall, and F1 score between them.\n\nFor token-based annotations, notably NER but any other span based annotations, the recommended metric is the average pairwise F1 score.\n\n## Sources of Disagreement\n\nWhen annotators systematically disagree on entity boundaries in NER or on whether a statement constitutes a \"hallucination,\" the annotation guidelines need clarification. Disagreement patterns reveal different problems: isolated disagreements indicate attention errors, category-level disagreements indicate unclear guidelines, and persistent expert disagreement indicates genuine task ambiguity.\n\n## Practical Applications\n\nFor machine learning, the danger is not disagreement itself but unmeasured disagreement, as models trained on single-annotator labels silently learn individual quirks and biases that surface as brittle behavior, poor generalization, and fairness issues when deployed."
    ],
    "durationSeconds": 8.443967470000004
  }
}
```

</details>

---

### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for a couple more papers. I need:
- Direction C: I need a specific evaluation paper. Let me search for "GenRES rethinking evaluation generative relation extraction" mentioned earlier.
- Direction B: I could use the NoiseBench paper (found), and the Fine-grained Entity Typing via Label Reasoning paper. Let me also look for one more on label noise or type confusion in NER.

Let me also check if I have enough papers now. Let me count:
- Direction A (Structured decoding / constrained generation): GENRE (De Cao et al., ICLR 2021), iNERD (Deußer et al., IEEE BigData 2024)


- Direction B (Classical label ambiguity / type confusion): NoiseBench (Merdjanovska et al., EMNLP 2024), Fine-grained Entity Typing via Label Reasoning (Liu et al., EMNLP 2021)
- Direction C (Evaluation methodology for IE): Need specific papers
- Direction D (LLM calibration): Geng et al. survey (NAACL 2024), FaR (Zhao et al., ACL Findings 2024)

I have 6 papers so far and need to reach 8-10. I should search for the GenRES paper for direction C and find at least one more evaluation methodology paper to round out that category. I'm realizing LinkNER fits well for direction D since it addresses uncertainty in NER. Let me search for GenRES and maybe one more evaluation-focused paper to round out my list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1d04c989-b882-442a-81a3-656a866ff9f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEvFwDMZnudxTg6GmiFKmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 830,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 48588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2182
      },
      "output_tokens": 9,
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

_source line 67_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ZAWNJ37wqUBudSD493FuJ`</summary>

```json
{
  "query": "GenRES rethinking evaluation generative relation extraction large language models 2024 arXiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "c35a73a2-d474-4a2c-a19a-08528252667c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEvFwDMZnudxTg6GmiFKmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 830,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 48588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2182
      },
      "output_tokens": 9,
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

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TRkXJf61YoikaDZcajBAML`</summary>

```json
{
  "query": "MultiCoNER fine-grained multilingual named entity recognition SemEval 2023 task 2 arXiv 2305.06586 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "daf980d5-dfe0-458a-b89e-6de20f566587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEvFwDMZnudxTg6GmiFKmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 830,
      "cache_creation_input_tokens": 2182,
      "cache_read_input_tokens": 48588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2182
      },
      "output_tokens": 9,
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

_source line 69 · 2026-05-15T16:13:16.390Z_

<details><summary>↩ Tool result · `toolu_01TRkXJf61YoikaDZcajBAML`</summary>

```text
Web search results for query: "MultiCoNER fine-grained multilingual named entity recognition SemEval 2023 task 2 arXiv 2305.06586 authors"

Links: [{"title":"[2305.06586] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)","url":"https://arxiv.org/abs/2305.06586"},{"title":"SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230506586F/abstract"},{"title":"[2305.06586v1] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)","url":"https://arxiv.org/abs/2305.06586v1"},{"title":"[PDF] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/3c1a75628e571ced2071810411677571b2457134"},{"title":"SemEval 2023 Task 2: MultiCoNER II&lt;/br>&lt;b>Multi&lt;/b>lingual &lt;b>Co&lt;/b>mplex &lt;b>N&lt;/b>amed &lt;b>E&lt;/b>ntity &lt;b>R&lt;/b>ecognition","url":"https://multiconer.github.io/"},{"title":"SemEval-2023 Task 2: Fine-grained Multilingual Named Entity","url":"https://arxiv.org/pdf/2305.06586"},{"title":"SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ACL Anthology","url":"https://aclanthology.org/2023.semeval-1.310/"},{"title":"(PDF) SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) (2023) | Besnik Fetahu | 40 Citations","url":"https://scispace.com/papers/semeval-2023-task-2-fine-grained-multilingual-named-entity-1gku9651gb"},{"title":"SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) | Request PDF","url":"https://www.researchgate.net/publication/372917258_SemEval-2023_Task_2_Fine-grained_Multilingual_Named_Entity_Recognition_MultiCoNER_2"},{"title":"SemEval-2023 Task 2: Fine-grained multilingual named entity recognition (MultiCoNER 2) - Amazon Science","url":"https://www.amazon.science/publications/semeval-2023-task-2-fine-grained-multilingual-named-entity-recognition-multiconer-2"}]

Based on the search results, I found information about the arXiv paper 2305.06586 on MultiCoNER fine-grained multilingual named entity recognition for SemEval 2023 Task 2.

The authors of this paper are Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, and Shervin Malmasi.

The paper presents the findings of SemEval-2023 Task 2 on Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2), focusing on methods to identify complex fine-grained named entities (like WRITTENWORK, VEHICLE, MUSICALGRP) across 12 languages, in both monolingual and multilingual scenarios, as well as noisy settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "87e4403d-77f8-42fb-b00f-43e68fed1351",
  "tool_use_result": {
    "query": "MultiCoNER fine-grained multilingual named entity recognition SemEval 2023 task 2 arXiv 2305.06586 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01No2yRPi737CASK7qdMih7c",
        "content": [
          {
            "title": "[2305.06586] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)",
            "url": "https://arxiv.org/abs/2305.06586"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230506586F/abstract"
          },
          {
            "title": "[2305.06586v1] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)",
            "url": "https://arxiv.org/abs/2305.06586v1"
          },
          {
            "title": "[PDF] SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/3c1a75628e571ced2071810411677571b2457134"
          },
          {
            "title": "SemEval 2023 Task 2: MultiCoNER II&lt;/br>&lt;b>Multi&lt;/b>lingual &lt;b>Co&lt;/b>mplex &lt;b>N&lt;/b>amed &lt;b>E&lt;/b>ntity &lt;b>R&lt;/b>ecognition",
            "url": "https://multiconer.github.io/"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained Multilingual Named Entity",
            "url": "https://arxiv.org/pdf/2305.06586"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) - ACL Anthology",
            "url": "https://aclanthology.org/2023.semeval-1.310/"
          },
          {
            "title": "(PDF) SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) (2023) | Besnik Fetahu | 40 Citations",
            "url": "https://scispace.com/papers/semeval-2023-task-2-fine-grained-multilingual-named-entity-1gku9651gb"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2) | Request PDF",
            "url": "https://www.researchgate.net/publication/372917258_SemEval-2023_Task_2_Fine-grained_Multilingual_Named_Entity_Recognition_MultiCoNER_2"
          },
          {
            "title": "SemEval-2023 Task 2: Fine-grained multilingual named entity recognition (MultiCoNER 2) - Amazon Science",
            "url": "https://www.amazon.science/publications/semeval-2023-task-2-fine-grained-multilingual-named-entity-recognition-multiconer-2"
          }
        ]
      },
      "Based on the search results, I found information about the arXiv paper 2305.06586 on MultiCoNER fine-grained multilingual named entity recognition for SemEval 2023 Task 2.\n\nThe authors of this paper are Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, and Shervin Malmasi.\n\nThe paper presents the findings of SemEval-2023 Task 2 on Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2), focusing on methods to identify complex fine-grained named entities (like WRITTENWORK, VEHICLE, MUSICALGRP) across 12 languages, in both monolingual and multilingual scenarios, as well as noisy settings."
    ],
    "durationSeconds": 4.2478705809999955
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T16:13:26.373Z_

<details><summary>↩ Tool result · `toolu_012ZAWNJ37wqUBudSD493FuJ`</summary>

```text
Web search results for query: "GenRES rethinking evaluation generative relation extraction large language models 2024 arXiv authors"

Links: [{"title":"[2402.10744] GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models","url":"https://arxiv.org/abs/2402.10744"},{"title":"GENRES: Rethinking Evaluation for Generative Relation Extraction in the","url":"https://arxiv.org/pdf/2402.10744"},{"title":"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.155/"},{"title":"GENRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/genres-rethinking-evaluation-for-generative-relation-extraction-i/"},{"title":"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models","url":"https://www.emergentmind.com/papers/2402.10744"},{"title":"Rethinking Evaluation for Generative Relation Extraction in ...","url":"https://aclanthology.org/2024.naacl-long.155.pdf"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"1 Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://arxiv.org/pdf/2312.10997"}]

Based on the search results, here's the information about the GenRES paper:

## GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models

**Authors:** Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, and Jiawei Han

**Publication Details:** The paper was published in 2024 in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024), pages 2820–2837, Mexico City, Mexico

**arXiv Information:** The preprint was submitted on February 16, 2024 (arXiv:2402.10744)

**Summary:** Traditional relation extraction (RE) metrics like precision and recall fall short in evaluating generative relation extraction (GRE) methods because these metrics rely on exact matching with human-annotated reference relations, while GRE methods often produce diverse and semantically accurate relations that differ from the references. To address this gap, the authors introduce GenRES for a multi-dimensional assessment in terms of topic similarity, uniqueness, granularity, factualness, and completeness of the GRE results


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "98441fa9-a7fc-4ad3-b713-25395d7623f5",
  "tool_use_result": {
    "query": "GenRES rethinking evaluation generative relation extraction large language models 2024 arXiv authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jy24EQM7xvJ3rptmH2j2Ts",
        "content": [
          {
            "title": "[2402.10744] GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models",
            "url": "https://arxiv.org/abs/2402.10744"
          },
          {
            "title": "GENRES: Rethinking Evaluation for Generative Relation Extraction in the",
            "url": "https://arxiv.org/pdf/2402.10744"
          },
          {
            "title": "GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.155/"
          },
          {
            "title": "GENRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/genres-rethinking-evaluation-for-generative-relation-extraction-i/"
          },
          {
            "title": "GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models",
            "url": "https://www.emergentmind.com/papers/2402.10744"
          },
          {
            "title": "Rethinking Evaluation for Generative Relation Extraction in ...",
            "url": "https://aclanthology.org/2024.naacl-long.155.pdf"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "Large Language Models for Generative Information Extraction: A Survey",
            "url": "https://arxiv.org/html/2312.17617v3"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "1 Retrieval-Augmented Generation for Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2312.10997"
          }
        ]
      },
      "Based on the search results, here's the information about the GenRES paper:\n\n## GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\n\n**Authors:** Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, and Jiawei Han\n\n**Publication Details:** The paper was published in 2024 in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024), pages 2820–2837, Mexico City, Mexico\n\n**arXiv Information:** The preprint was submitted on February 16, 2024 (arXiv:2402.10744)\n\n**Summary:** Traditional relation extraction (RE) metrics like precision and recall fall short in evaluating generative relation extraction (GRE) methods because these metrics rely on exact matching with human-annotated reference relations, while GRE methods often produce diverse and semantically accurate relations that differ from the references. To address this gap, the authors introduce GenRES for a multi-dimensional assessment in terms of topic similarity, uniqueness, granularity, factualness, and completeness of the GRE results"
    ],
    "durationSeconds": 14.304051960000011
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough papers. Let me compile my list:

### Part 1: Fix incomplete citations
1. **#19 SPT**: Authors = Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu
2. **#20 PARSE**: Authors = Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla. Venue = EMNLP 2025 Industry Track (submitted). Let me keep arXiv 2025 for now.


3. **#21 Familiarity**: Authors = Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik. Venue = NAACL 2025.

### Part 2: New papers (8-10)

Now I'm looking at structured decoding and constrained generation approaches for information extraction. I'll add GENRE from De Cao et al. at ICLR 2021 and iNERD from Deußer et al. published in IEEE.

For classical label ambiguity issues, there's NoiseBench from Merdjanovska et al. at EMNLP 2024 and the fine-grained entity typing work by Liu et al. from EMNLP 2021.

On evaluation methodology, I'm considering GenRES from Jiang et al. at NAACL 2024 and MultiCoNER 2 from the SemEval-2023 Task 2.

For LLM calibration and confidence estimation, I have the Geng et al. survey from NAACL 2024, FaR by Zhao et al. in ACL Findings 2024, and optionally LinkNER from Zhang et al. at WWW 2024.

That gives me 9 papers total, which fits the 8-10 requirement with 2-3 per direction. I should include LinkNER to reach 10 and have a solid buffer. Let me also verify that grammar-constrained decoding paper by Schmidt and Cimiano from Frontiers in AI 2025, though it might be too specialized for this survey.

Now I need to update the file with corrected author information for papers #19 and #20, then add the remaining 9 new papers and recalculate the summary statistics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "ac10d3c9-5e8f-42b6-9fc1-55b423aea9bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fj27cywLteH1kcJBivvKiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 50770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2528
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

_source line 72_

所有信息已收集完毕。现在更新文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "89b3584c-8a93-4dcb-8a1a-c5a81c7a23f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fj27cywLteH1kcJBivvKiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 50770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2528
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

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_017JzeGutmja8vjbSoiqV3Mg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "old_string": "- **Authors**: (arXiv 2025)\n- **Venue**: arXiv preprint, June 2025",
  "new_string": "- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "a827d1c3-a978-481a-9491-d93f67f94009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fj27cywLteH1kcJBivvKiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 50770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2528
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

_source line 74 · 2026-05-15T16:13:53.420Z_

<details><summary>↩ Tool result · `toolu_017JzeGutmja8vjbSoiqV3Mg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "40c4c401-35f7-4410-9356-b2839e6d505f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
    "oldString": "- **Authors**: (arXiv 2025)\n- **Venue**: arXiv preprint, June 2025",
    "newString": "- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025",
    "originalFile": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: (arXiv 2025)\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: (Amazon Science, 2025)\n- **Venue**: arXiv preprint, October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
    "structuredPatch": [
      {
        "oldStart": 154,
        "oldLines": 7,
        "newStart": 154,
        "newLines": 7,
        "lines": [
          " ",
          " ### 19. Schema as Parameterized Tools (SPT)",
          " - **Full title**: Schema as Parameterized Tools for Universal Information Extraction",
          "-- **Authors**: (arXiv 2025)",
          "+- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu",
          " - **Venue**: arXiv preprint, June 2025",
          " - **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa",
          " - **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters."
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01Kojq6qzhnW9DjresWmHSb1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "old_string": "- **Authors**: (Amazon Science, 2025)\n- **Venue**: arXiv preprint, October 2025",
  "new_string": "- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1448428c-308e-4f76-96ee-2f20c49b84a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrM42v279TXgV7YMzPaz5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2371,
      "cache_read_input_tokens": 53298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2371
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

_source line 76 · 2026-05-15T16:13:56.735Z_

<details><summary>↩ Tool result · `toolu_01Kojq6qzhnW9DjresWmHSb1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "77e6ef9f-3c48-4ba7-b909-7cc864daccf6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
    "oldString": "- **Authors**: (Amazon Science, 2025)\n- **Venue**: arXiv preprint, October 2025",
    "newString": "- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025",
    "originalFile": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: (Amazon Science, 2025)\n- **Venue**: arXiv preprint, October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
    "structuredPatch": [
      {
        "oldStart": 162,
        "oldLines": 8,
        "newStart": 162,
        "newLines": 8,
        "lines": [
          " ",
          " ### 20. PARSE",
          " - **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
          "-- **Authors**: (Amazon Science, 2025)",
          "-- **Venue**: arXiv preprint, October 2025",
          "+- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla",
          "+- **Venue**: arXiv preprint (Amazon Science), October 2025",
          " - **arXiv/DOI**: arXiv:2510.08623",
          " - **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.",
          " - **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level."
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

_source line 77_

<details open><summary>🔧 Tool call — Edit · `toolu_015uuNi94ZUjFsYfh8Gknnfv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "old_string": "- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121",
  "new_string": "- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "8ed1234f-2c3e-4aa1-a37e-9e181381ee37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E5PMxrzW2R995F6YY5iirn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 55669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 281
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

_source line 78 · 2026-05-15T16:14:00.725Z_

<details><summary>↩ Tool result · `toolu_015uuNi94ZUjFsYfh8Gknnfv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "d8434dfe-63f1-48ce-93f9-56ec3c74256b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
    "oldString": "- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121",
    "newString": "- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/",
    "originalFile": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: (arXiv, December 2024)\n- **arXiv/DOI**: arXiv:2412.10121\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
    "structuredPatch": [
      {
        "oldStart": 170,
        "oldLines": 8,
        "newStart": 170,
        "newLines": 9,
        "lines": [
          " ",
          " ### 21. Familiarity: Zero-Shot NER Label Shift",
          " - **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data",
          "-- **Authors**: (arXiv, December 2024)",
          "-- **arXiv/DOI**: arXiv:2412.10121",
          "+- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik",
          "+- **Venue**: NAACL 2025",
          "+- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/",
          " - **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.",
          " - **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.",
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

_source line 79_

Now I need to remove the duplicate venue line that was left behind from #21. Let me check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "5e3451d7-72d4-406f-874e-3ac78084430e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHxDXqkrBHZcSS7kJrGu74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 55950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 321
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

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_01ViC2SgvY8RBYY46vwkiMak`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "offset": 170,
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
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "3587bfc3-2527-45ad-946e-1f9263471dce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHxDXqkrBHZcSS7kJrGu74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 55950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 321
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

_source line 81 · 2026-05-15T16:14:03.493Z_

<details><summary>↩ Tool result · `toolu_01ViC2SgvY8RBYY46vwkiMak`</summary>

```text
170	
171	### 21. Familiarity: Zero-Shot NER Label Shift
172	- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data
173	- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik
174	- **Venue**: NAACL 2025
175	- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/
176	- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.
177	- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.
178	
179	---
180	
181	## Summary Statistics
182	- Total references found: **14/14 required + 7 additional = 21 total**
183	- Not found: None — all 14 required papers verified via web search
184	- Coverage by relation type:
185	  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)
186	  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)
187	  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)
188	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "04ea27ff-54a6-4635-bd87-17203ac02fec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
      "content": "\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
      "numLines": 19,
      "startLine": 170,
      "totalLines": 188
    }
  }
}
```

</details>

---

### Assistant

_source line 82_

Good, the format is clean. Now I'll add the 9 new papers and update the summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "36ef831a-68fd-4f9b-9a52-c1fe34c8a91a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5YJkWhzjygzSdqZ5JZvrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 56271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
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

_source line 83_

<details open><summary>🔧 Tool call — Edit · `toolu_019L55TBZNiHHxEM9ZNe6Q67`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "old_string": "---\n\n## Summary Statistics",
  "new_string": "---\n\n## Direction A: Structured Decoding / Constrained Generation for IE (2)\n\n### 22. GENRE — Autoregressive Entity Retrieval\n- **Full title**: Autoregressive Entity Retrieval\n- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni\n- **Venue**: ICLR 2021\n- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V\n- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.\n- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.\n\n### 23. iNERD — Informed NER Decoding\n- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models\n- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa\n- **Venue**: IEEE BigData 2024\n- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/\n- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.\n- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.\n\n---\n\n## Direction B: Classical Label Ambiguity / Type Confusion (2)\n\n### 24. NoiseBench\n- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition\n- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik\n- **Venue**: EMNLP 2024\n- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/\n- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.\n- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.\n\n### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing\n- **Full title**: Fine-grained Entity Typing via Label Reasoning\n- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu\n- **Venue**: EMNLP 2021\n- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/\n- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.\n- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.\n\n---\n\n## Direction C: Evaluation Methodology for IE (2)\n\n### 26. GenRES — Rethinking Evaluation for Generative RE\n- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\n- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/\n- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.\n- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.\n\n### 27. MultiCoNER 2 (SemEval-2023 Task 2)\n- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)\n- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi\n- **Venue**: SemEval 2023 (co-located with ACL 2023)\n- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/\n- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.\n- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.\n\n---\n\n## Direction D: LLM Calibration / Confidence Estimation (3)\n\n### 28. LLM Confidence & Calibration Survey\n- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models\n- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/\n- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.\n- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.\n\n### 29. FaR — Fact-and-Reflection Prompting for Calibration\n- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models\n- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen\n- **Venue**: ACL 2024 Findings\n- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/\n- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.\n- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.\n\n### 30. LinkNER — Uncertainty-based NER with LLMs\n- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\n- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu\n- **Venue**: WWW 2024\n- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414\n- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.\n- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.\n\n---\n\n## Summary Statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "bb2d2f4a-647e-4e9f-b776-284ad62ac96c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5YJkWhzjygzSdqZ5JZvrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 56271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
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

_source line 84 · 2026-05-15T16:14:57.592Z_

<details><summary>↩ Tool result · `toolu_019L55TBZNiHHxEM9ZNe6Q67`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "dfdb30a7-1f20-4ce9-9724-d3113d903a88",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
    "oldString": "---\n\n## Summary Statistics",
    "newString": "---\n\n## Direction A: Structured Decoding / Constrained Generation for IE (2)\n\n### 22. GENRE — Autoregressive Entity Retrieval\n- **Full title**: Autoregressive Entity Retrieval\n- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni\n- **Venue**: ICLR 2021\n- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V\n- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.\n- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.\n\n### 23. iNERD — Informed NER Decoding\n- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models\n- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa\n- **Venue**: IEEE BigData 2024\n- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/\n- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.\n- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.\n\n---\n\n## Direction B: Classical Label Ambiguity / Type Confusion (2)\n\n### 24. NoiseBench\n- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition\n- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik\n- **Venue**: EMNLP 2024\n- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/\n- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.\n- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.\n\n### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing\n- **Full title**: Fine-grained Entity Typing via Label Reasoning\n- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu\n- **Venue**: EMNLP 2021\n- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/\n- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.\n- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.\n\n---\n\n## Direction C: Evaluation Methodology for IE (2)\n\n### 26. GenRES — Rethinking Evaluation for Generative RE\n- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\n- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/\n- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.\n- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.\n\n### 27. MultiCoNER 2 (SemEval-2023 Task 2)\n- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)\n- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi\n- **Venue**: SemEval 2023 (co-located with ACL 2023)\n- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/\n- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.\n- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.\n\n---\n\n## Direction D: LLM Calibration / Confidence Estimation (3)\n\n### 28. LLM Confidence & Calibration Survey\n- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models\n- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/\n- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.\n- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.\n\n### 29. FaR — Fact-and-Reflection Prompting for Calibration\n- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models\n- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen\n- **Venue**: ACL 2024 Findings\n- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/\n- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.\n- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.\n\n### 30. LinkNER — Uncertainty-based NER with LLMs\n- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\n- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu\n- **Venue**: WWW 2024\n- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414\n- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.\n- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.\n\n---\n\n## Summary Statistics",
    "originalFile": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
    "structuredPatch": [
      {
        "oldStart": 178,
        "oldLines": 6,
        "newStart": 178,
        "newLines": 94,
        "lines": [
          " ",
          " ---",
          " ",
          "+## Direction A: Structured Decoding / Constrained Generation for IE (2)",
          "+",
          "+### 22. GENRE — Autoregressive Entity Retrieval",
          "+- **Full title**: Autoregressive Entity Retrieval",
          "+- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni",
          "+- **Venue**: ICLR 2021",
          "+- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V",
          "+- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.",
          "+- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.",
          "+",
          "+### 23. iNERD — Informed NER Decoding",
          "+- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models",
          "+- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa",
          "+- **Venue**: IEEE BigData 2024",
          "+- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/",
          "+- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.",
          "+- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.",
          "+",
          "+---",
          "+",
          "+## Direction B: Classical Label Ambiguity / Type Confusion (2)",
          "+",
          "+### 24. NoiseBench",
          "+- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition",
          "+- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik",
          "+- **Venue**: EMNLP 2024",
          "+- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/",
          "+- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.",
          "+- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.",
          "+",
          "+### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing",
          "+- **Full title**: Fine-grained Entity Typing via Label Reasoning",
          "+- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu",
          "+- **Venue**: EMNLP 2021",
          "+- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/",
          "+- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.",
          "+- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.",
          "+",
          "+---",
          "+",
          "+## Direction C: Evaluation Methodology for IE (2)",
          "+",
          "+### 26. GenRES — Rethinking Evaluation for Generative RE",
          "+- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models",
          "+- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han",
          "+- **Venue**: NAACL 2024",
          "+- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/",
          "+- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.",
          "+- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.",
          "+",
          "+### 27. MultiCoNER 2 (SemEval-2023 Task 2)",
          "+- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)",
          "+- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi",
          "+- **Venue**: SemEval 2023 (co-located with ACL 2023)",
          "+- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/",
          "+- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.",
          "+- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.",
          "+",
          "+---",
          "+",
          "+## Direction D: LLM Calibration / Confidence Estimation (3)",
          "+",
          "+### 28. LLM Confidence & Calibration Survey",
          "+- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models",
          "+- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych",
          "+- **Venue**: NAACL 2024",
          "+- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/",
          "+- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.",
          "+- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.",
          "+",
          "+### 29. FaR — Fact-and-Reflection Prompting for Calibration",
          "+- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models",
          "+- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen",
          "+- **Venue**: ACL 2024 Findings",
          "+- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/",
          "+- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.",
          "+- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.",
          "+",
          "+### 30. LinkNER — Uncertainty-based NER with LLMs",
          "+- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty",
          "+- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu",
          "+- **Venue**: WWW 2024",
          "+- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414",
          "+- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.",
          "+- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.",
          "+",
          "+---",
          "+",
          " ## Summary Statistics",
          " - Total references found: **14/14 required + 7 additional = 21 total**",
          " - Not found: None — all 14 required papers verified via web search"
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_014D1BSXXXQvV5JgSvvXhfWn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "old_string": "## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)",
  "new_string": "## Summary Statistics\n- Total references: **14 required + 7 additional + 9 newly added = 30 total**\n- Not found: None — all papers verified via web search\n- Coverage by direction:\n  - **A. Structured decoding / constrained generation**: #22 GENRE, #23 iNERD\n  - **B. Classical label ambiguity / type confusion**: #24 NoiseBench, #25 LRN\n  - **C. Evaluation methodology for IE**: #26 GenRES, #27 MultiCoNER 2\n  - **D. LLM calibration / confidence estimation**: #28 Geng survey, #29 FaR, #30 LinkNER\n- Coverage by relation type:\n  - **Support** (validates our claims): #1, #4, #5, #8, #9, #11, #12, #14, #17, #21, #24, #25, #27, #30 (14 papers)\n  - **Complement** (orthogonal methods): #2, #6, #7, #10, #13, #15, #18, #19, #20, #22, #23, #26, #28, #29 (14 papers)\n  - **Contrast** (alternative approaches): #3, #16 (2 papers)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "711c42a6-be4b-480d-9376-43c809bdd008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbQaJv6XrwGyYJwoBHbnEn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 56975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 73,
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

_source line 86 · 2026-05-15T16:15:11.529Z_

<details><summary>↩ Tool result · `toolu_014D1BSXXXQvV5JgSvvXhfWn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "69a3a8ea-b580-42e8-a1e8-431a9f3dd76f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
    "oldString": "## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)",
    "newString": "## Summary Statistics\n- Total references: **14 required + 7 additional + 9 newly added = 30 total**\n- Not found: None — all papers verified via web search\n- Coverage by direction:\n  - **A. Structured decoding / constrained generation**: #22 GENRE, #23 iNERD\n  - **B. Classical label ambiguity / type confusion**: #24 NoiseBench, #25 LRN\n  - **C. Evaluation methodology for IE**: #26 GenRES, #27 MultiCoNER 2\n  - **D. LLM calibration / confidence estimation**: #28 Geng survey, #29 FaR, #30 LinkNER\n- Coverage by relation type:\n  - **Support** (validates our claims): #1, #4, #5, #8, #9, #11, #12, #14, #17, #21, #24, #25, #27, #30 (14 papers)\n  - **Complement** (orthogonal methods): #2, #6, #7, #10, #13, #15, #18, #19, #20, #22, #23, #26, #28, #29 (14 papers)\n  - **Contrast** (alternative approaches): #3, #16 (2 papers)",
    "originalFile": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Direction A: Structured Decoding / Constrained Generation for IE (2)\n\n### 22. GENRE — Autoregressive Entity Retrieval\n- **Full title**: Autoregressive Entity Retrieval\n- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni\n- **Venue**: ICLR 2021\n- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V\n- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.\n- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.\n\n### 23. iNERD — Informed NER Decoding\n- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models\n- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa\n- **Venue**: IEEE BigData 2024\n- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/\n- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.\n- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.\n\n---\n\n## Direction B: Classical Label Ambiguity / Type Confusion (2)\n\n### 24. NoiseBench\n- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition\n- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik\n- **Venue**: EMNLP 2024\n- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/\n- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.\n- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.\n\n### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing\n- **Full title**: Fine-grained Entity Typing via Label Reasoning\n- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu\n- **Venue**: EMNLP 2021\n- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/\n- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.\n- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.\n\n---\n\n## Direction C: Evaluation Methodology for IE (2)\n\n### 26. GenRES — Rethinking Evaluation for Generative RE\n- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\n- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/\n- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.\n- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.\n\n### 27. MultiCoNER 2 (SemEval-2023 Task 2)\n- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)\n- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi\n- **Venue**: SemEval 2023 (co-located with ACL 2023)\n- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/\n- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.\n- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.\n\n---\n\n## Direction D: LLM Calibration / Confidence Estimation (3)\n\n### 28. LLM Confidence & Calibration Survey\n- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models\n- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/\n- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.\n- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.\n\n### 29. FaR — Fact-and-Reflection Prompting for Calibration\n- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models\n- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen\n- **Venue**: ACL 2024 Findings\n- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/\n- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.\n- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.\n\n### 30. LinkNER — Uncertainty-based NER with LLMs\n- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\n- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu\n- **Venue**: WWW 2024\n- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414\n- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.\n- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.\n\n---\n\n## Summary Statistics\n- Total references found: **14/14 required + 7 additional = 21 total**\n- Not found: None — all 14 required papers verified via web search\n- Coverage by relation type:\n  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)\n  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)\n  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)\n",
    "structuredPatch": [
      {
        "oldStart": 267,
        "oldLines": 9,
        "newStart": 267,
        "newLines": 14,
        "lines": [
          " ---",
          " ",
          " ## Summary Statistics",
          "-- Total references found: **14/14 required + 7 additional = 21 total**",
          "-- Not found: None — all 14 required papers verified via web search",
          "+- Total references: **14 required + 7 additional + 9 newly added = 30 total**",
          "+- Not found: None — all papers verified via web search",
          "+- Coverage by direction:",
          "+  - **A. Structured decoding / constrained generation**: #22 GENRE, #23 iNERD",
          "+  - **B. Classical label ambiguity / type confusion**: #24 NoiseBench, #25 LRN",
          "+  - **C. Evaluation methodology for IE**: #26 GenRES, #27 MultiCoNER 2",
          "+  - **D. LLM calibration / confidence estimation**: #28 Geng survey, #29 FaR, #30 LinkNER",
          " - Coverage by relation type:",
          "-  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)",
          "-  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)",
          "-  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)",
          "+  - **Support** (validates our claims): #1, #4, #5, #8, #9, #11, #12, #14, #17, #21, #24, #25, #27, #30 (14 papers)",
          "+  - **Complement** (orthogonal methods): #2, #6, #7, #10, #13, #15, #18, #19, #20, #22, #23, #26, #28, #29 (14 papers)",
          "+  - **Contrast** (alternative approaches): #3, #16 (2 papers)"
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

_source line 87_

验证最终文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "ee7e71b1-90a7-4ee7-a507-044736665686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6bsVEUNMVR9a5w8HPwq3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 59534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 774
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

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_01EVSvc9Rz4CPKPFBvc4X3sP`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md && grep -c \"^### \" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
  "description": "Count lines and paper entries in the updated file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "33c0ecb1-cfe7-4ffe-a0aa-b33647207c94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6bsVEUNMVR9a5w8HPwq3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 59534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 774
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

_source line 89 · 2026-05-15T16:15:14.784Z_

<details><summary>↩ Tool result · `toolu_01EVSvc9Rz4CPKPFBvc4X3sP`</summary>

```text
280 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md
30
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "69906a67-ba0c-459f-8f8a-ac1848ff0f58",
  "tool_use_result": {
    "stdout": "280 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md\n30",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 90_

完成。文件已更新，共 30 篇论文：

**Part 1 — 修复 3 篇不完整引用：**
- #19 SPT: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu
- #20 PARSE: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
- #21 Familiarity: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik（同时更新 venue 为 NAACL 2025）

**Part 2 — 新增 9 篇论文（#22-#30）：**

| 方向 | 编号 | 论文 | Venue |
|------|------|------|-------|
| A. Structured decoding | #22 | GENRE (De Cao et al.) | ICLR 2021 |
| A. Structured decoding | #23 | iNERD (Deußer et al.) | IEEE BigData 2024 |
| B. Label ambiguity | #24 | NoiseBench (Merdjanovska et al.) | EMNLP 2024 |
| B. Label ambiguity | #25 | LRN (Liu et al.) | EMNLP 2021 |
| C. Evaluation | #26 | GenRES (Jiang et al.) | NAACL 2024 |
| C. Evaluation | #27 | MultiCoNER 2 (Fetahu et al.) | SemEval 2023 |
| D. Calibration | #28 | LLM Calibration Survey (Geng et al.) | NAACL 2024 |
| D. Calibration | #29 | FaR (Zhao et al.) | ACL Findings 2024 |
| D. Calibration | #30 | LinkNER (Zhang et al.) | WWW 2024 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "uuid": "1afabb52-b650-441d-accc-4f11ba758003",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugap4bkQiMRU4EfRM9iAi4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 60308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 91_

完成。文件已更新，共 30 篇论文：

**Part 1 — 修复 3 篇不完整引用：**
- #19 SPT: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu
- #20 PARSE: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
- #21 Familiarity: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik（同时更新 venue 为 NAACL 2025）

**Part 2 — 新增 9 篇论文（#22-#30）：**

| 方向 | 编号 | 论文 | Venue |
|------|------|------|-------|
| A. Structured decoding | #22 | GENRE (De Cao et al.) | ICLR 2021 |
| A. Structured decoding | #23 | iNERD (Deußer et al.) | IEEE BigData 2024 |
| B. Label ambiguity | #24 | NoiseBench (Merdjanovska et al.) | EMNLP 2024 |
| B. Label ambiguity | #25 | LRN (Liu et al.) | EMNLP 2021 |
| C. Evaluation | #26 | GenRES (Jiang et al.) | NAACL 2024 |
| C. Evaluation | #27 | MultiCoNER 2 (Fetahu et al.) | SemEval 2023 |
| D. Calibration | #28 | LLM Calibration Survey (Geng et al.) | NAACL 2024 |
| D. Calibration | #29 | FaR (Zhao et al.) | ACL Findings 2024 |
| D. Calibration | #30 | LinkNER (Zhang et al.) | WWW 2024 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 251434,
  "duration_api_ms": 359574,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "61e80c54-ca06-4aaf-bbbb-5bb810912999",
  "total_cost_usd": 1.6589287500000003,
  "usage": {
    "input_tokens": 6839,
    "cache_creation_input_tokens": 48787,
    "cache_read_input_tokens": 773202,
    "output_tokens": 9004,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48787,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 539,
        "cache_read_input_tokens": 60308,
        "cache_creation_input_tokens": 320,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 320
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 417364,
      "outputTokens": 10150,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 24,
      "costUSD": 0.7081139999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6839,
      "outputTokens": 9004,
      "cacheReadInputTokens": 773202,
      "cacheCreationInputTokens": 48787,
      "webSearchRequests": 0,
      "costUSD": 0.9508147499999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "850b6cab-5ae5-43be-8077-dd429506f30f"
}
```

</details>

---
