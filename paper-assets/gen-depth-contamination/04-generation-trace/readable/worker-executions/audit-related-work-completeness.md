# audit related work completeness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_audit_related_work_completeness_20260514T021616.log`
- **Structured JSON:** [`e8f21ed2724fd832be33.json`](../../sessions/e8/e8f21ed2724fd832be33.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
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
  "uuid": "b5da37ae-109e-4329-b654-f9a36b6374ac",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778742600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6d5ad634-27b9-49be-bb2f-30ffbc89f9b3",
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the related_work.tex and references.bib files to conduct the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "73947c33-5f56-4303-818a-045c7d65af41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXejwQV5r84Kz8HgmvXq33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11654,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11654
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01Gy7vxZFb6TyQcFRZKMp5GW`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "ad516dd2-d805-4308-9d03-64471945a138",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXejwQV5r84Kz8HgmvXq33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11654,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11654
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

_source line 6 · 2026-05-14T02:16:27.336Z_

<details><summary>↩ Tool result · `toolu_01Gy7vxZFb6TyQcFRZKMp5GW`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
10	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
11	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
12	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
13	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
14	These works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.
15	
16	\paragraph{Binary Synthetic Text Detection.}
17	Distinguishing machine-generated from human-written text is a well-studied binary classification problem.
18	Zellers et al.~\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.
19	Recent zero-shot methods have narrowed the gap: Mitchell et al.~\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.
20	DivEye~\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\%++~\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.
21	CoDeC~\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.
22	
23	All these methods produce binary outputs and do not distinguish generational depth.
24	The connection to membership inference is instructive: Min-K\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.
25	A further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.
26	Binary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.
27	
28	\paragraph{Data Selection and Curation.}
29	Principled data selection methods improve training corpus quality through distribution matching and deduplication.
30	DSIR~\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.
31	D4~\cite{tirumala2024d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\cite{xie2024doremi} learns domain weights via a proxy model to optimize downstream performance.
32	These methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.
33	
34	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.
35	Their approach is a special case of our graduated filtering framework: when $\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.
36	We generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$).
37	Amin et al.~\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\Kempirical$ may remain practically useful.
38	Gambetta et al.~\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.
39	
40	\paragraph{Watermarking and Provenance.}
41	An alternative approach embeds identifiers at generation time.
42	Kirchenbauer et al.~\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.
43	Watermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.
44	The two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "dbab4f60-6373-438d-b4a8-de4a2b55626c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model Collapse and Recursive Generation.}\nTraining on model-generated data can cause progressive distribution shift known as \\emph{model collapse}.\nShumailov et al.~\\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nSchaeffer et al.~\\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.\nOur $\\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.\nKazdan et al.~\\cite{kazdan2025collapse} distinguished \\emph{replace} and \\emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.\nOur prompt-chain protocol operates in the replace regime, so $\\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\\Kstar$.\nShi et al.~\\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.\nThese works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.\n\n\\paragraph{Binary Synthetic Text Detection.}\nDistinguishing machine-generated from human-written text is a well-studied binary classification problem.\nZellers et al.~\\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.\nRecent zero-shot methods have narrowed the gap: Mitchell et al.~\\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.\nDivEye~\\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\\%++~\\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.\nCoDeC~\\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.\n\nAll these methods produce binary outputs and do not distinguish generational depth.\nThe connection to membership inference is instructive: Min-K\\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.\nA further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.\nBinary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.\n\n\\paragraph{Data Selection and Curation.}\nPrincipled data selection methods improve training corpus quality through distribution matching and deduplication.\nDSIR~\\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.\nD4~\\cite{tirumala2024d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\\cite{xie2024doremi} learns domain weights via a proxy model to optimize downstream performance.\nThese methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.\n\nThe closest prior work is Drayson et al.~\\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.\nTheir approach is a special case of our graduated filtering framework: when $\\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.\nWe generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\\geq 3$).\nAmin et al.~\\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\\Kempirical$ may remain practically useful.\nGambetta et al.~\\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.\n\n\\paragraph{Watermarking and Provenance.}\nAn alternative approach embeds identifiers at generation time.\nKirchenbauer et al.~\\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.\nWatermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.\nThe two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01ErAD2VjqxQyGyaGjhmDDoL`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "e91dfcf4-2c89-4b23-b584-23f8fb7b0614",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXejwQV5r84Kz8HgmvXq33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11654,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11654
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

_source line 8 · 2026-05-14T02:16:27.441Z_

<details><summary>↩ Tool result · `toolu_01ErAD2VjqxQyGyaGjhmDDoL`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — PENDING formal verification via verify_references
3	% NOTE: All entries require online verification before final submission
4	
5	% === Must-Cite ===
6	
7	@inproceedings{drayson2025,
8	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
9	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
10	  booktitle={Proceedings of EMNLP},
11	  year={2025},
12	  url={https://arxiv.org/abs/2502.15654}
13	}
14	
15	@inproceedings{schaeffer2025position,
16	  title={Position: Model Collapse Does Not Mean What You Think},
17	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
18	  booktitle={Proceedings of ICML},
19	  year={2025},
20	  url={https://arxiv.org/abs/2503.03150}
21	}
22	
23	@inproceedings{kazdan2025collapse,
24	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
25	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
26	  booktitle={Proceedings of ICML},
27	  year={2025},
28	  url={https://arxiv.org/abs/2410.16713}
29	}
30	
31	@inproceedings{shi2025generalization,
32	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
33	  author={Shi, Shiliang and Wu, Qiong and Zhang, Zhen and Zhang, Jing and Tao, Dacheng and Qu, Xiangyang},
34	  booktitle={Advances in NeurIPS},
35	  year={2025},
36	  note={Spotlight},
37	  url={https://arxiv.org/abs/2509.16499}
38	}
39	
40	@inproceedings{mitchell2023detectgpt,
41	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
42	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
43	  booktitle={Proceedings of ICML},
44	  year={2023}
45	}
46	
47	% === Should-Cite ===
48	
49	@article{basani2026diveye,
50	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
51	  author={Basani, Yash and Chen, Liyan},
52	  journal={Transactions on Machine Learning Research},
53	  year={2026},
54	  url={https://arxiv.org/abs/2509.18880}
55	}
56	
57	@inproceedings{amin2025escaping,
58	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
59	  author={Amin, Kareem and others},
60	  booktitle={Advances in NeurIPS},
61	  year={2025},
62	  url={https://arxiv.org/abs/2502.08924}
63	}
64	
65	@inproceedings{zawalski2026codec,
66	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
67	  author={Zawalski, Kacper and others},
68	  booktitle={Proceedings of ICLR},
69	  year={2026},
70	  url={https://arxiv.org/abs/2510.27055}
71	}
72	
73	@article{gambetta2025surplexity,
74	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},
75	  author={Gambetta, Lorenzo and others},
76	  journal={arXiv preprint arXiv:2410.12341},
77	  year={2025},
78	  url={https://arxiv.org/abs/2410.12341}
79	}
80	
81	@inproceedings{zhang2024minkpp,
82	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
83	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
84	  booktitle={Proceedings of EMNLP},
85	  year={2024}
86	}
87	
88	@article{shumailov2024collapse,
89	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
90	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
91	  journal={Nature},
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
102	@inproceedings{dohmatob2024model,
103	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
104	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
105	  booktitle={Proceedings of ICML},
106	  year={2024}
107	}
108	
109	@inproceedings{xie2023dsir,
110	  title={Data Selection with Importance Resampling},
111	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
112	  booktitle={Proceedings of ICML},
113	  year={2023}
114	}
115	
116	@inproceedings{tirumala2024d4,
117	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
118	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
119	  booktitle={Advances in NeurIPS},
120	  year={2023}
121	}
122	
123	@inproceedings{xie2024doremi,
124	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
125	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
126	  booktitle={Advances in NeurIPS},
127	  year={2023}
128	}
129	
130	@inproceedings{kirchenbauer2023watermark,
131	  title={A Watermark for Large Language Models},
132	  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
133	  booktitle={Proceedings of ICML},
134	  year={2023}
135	}
136	
137	@inproceedings{zellers2019grover,
138	  title={Defending Against Neural Fake News},
139	  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
140	  booktitle={Advances in NeurIPS},
141	  year={2019}
142	}
143	
144	@inproceedings{ippolito2020detection,
145	  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},
146	  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},
147	  booktitle={Proceedings of ACL},
148	  year={2020}
149	}
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "6e1c7a04-cf90-4901-9523-76f93e4153bb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — PENDING formal verification via verify_references\n% NOTE: All entries require online verification before final submission\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{shi2025generalization,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Shiliang and Wu, Qiong and Zhang, Zhen and Zhang, Jing and Tao, Dacheng and Qu, Xiangyang},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  note={Spotlight},\n  url={https://arxiv.org/abs/2509.16499}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Yash and Chen, Liyan},\n  journal={Transactions on Machine Learning Research},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and others},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  url={https://arxiv.org/abs/2502.08924}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Kacper and others},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@article{gambetta2025surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},\n  author={Gambetta, Lorenzo and others},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12341}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection with Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{tirumala2024d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{xie2024doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title={A Watermark for Large Language Models},\n  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{zellers2019grover,\n  title={Defending Against Neural Fake News},\n  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle={Advances in NeurIPS},\n  year={2019}\n}\n\n@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 150
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the related work systematically against all the check items.

## 1. Key Baseline Method Coverage

### Binary AI text detection:
- **DivEye (Basani 2026)**: ✅ Cited in line 20, bib entry exists
- **Binoculars (Hans et al. 2024)**: ❌ NOT cited
- **DetectGPT (Mitchell et al. 2023)**: ✅ Cited in line 19, bib entry exists


- **Min-K%++ (Zhang 2024)**: ✅ Cited in line 20, bib entry exists
- **CoDeC (Zawalski 2026)**: ✅ Cited in line 21, bib entry exists
- **GLTR (Gehrmann et al. 2019)**: ❌ NOT cited

### Model collapse:
- **Shumailov et al. 2024 (Nature)**: ✅ Cited in line 6
- **Alemohammad et al. 2024 (self-consuming)**: ✅ Cited in line 7
- **Dohmatob et al. 2024 (scaling)**: Still checking coverage...

### Data selection/filtering:
- **DSIR (Xie et al. 2023)**: ✅ Cited in line 30
- **D4 (Tirumala et al. 2024)**: ✅ Cited in line 31
- **DoReMi (Xie et al. 2024)**: ✅ Cited in line 31

### Recursive contamination:
- **Drayson et al. 2025**: ✅ Cited in line 34

### Ordinal classification:
- ❌ No ordinal regression baselines cited (e.g., CORAL, ordinal regression methods)

Now I'm looking at what related work might be missing, particularly around data contamination detection methods.

The paper doesn't address detecting pretraining data in LLMs or benchmark contamination specifically — works like Shi et al. and Golchin & Surdeanu are absent, though this is somewhat tangential to the main focus. Text quality filtering approaches like CCNet, RedPajama, and FineWeb aren't discussed either. Watermarking is covered through Kirchenbauer et al., though other recent approaches like Christ et al. and Zhao et al. could strengthen that section. Statistical fingerprinting of LLM outputs isn't explicitly covered as a topic.

Now I'm checking the citations for authenticity. The basani2026diveye reference points to an arXiv ID from September 2025 with a TMLR 2026 publication, which seems plausible but worth verifying given the future date. The zawalski2026codec citation also appears to be from 2026, and I'm examining whether these are legitimate references or potentially fabricated.

For shi2025generalization, the arXiv ID from September 2025 aligns with a NeurIPS 2025 Spotlight paper, and while Dacheng Tao is a recognized researcher, I should flag the other authors for verification. I'm also noticing a discrepancy with tirumala2024d4, which is listed as 2023 in the bibliography but cited differently.

Actually, looking closer at the timeline: Tirumala's D4 paper was published at NeurIPS 2023, so the bib year is correct despite the task description saying 2024. Similarly, xie2024doremi has a key/year mismatch—the bib shows 2023, which is when DoReMi actually appeared at NeurIPS. For zhang2024minkpp, the task just references "Zhang 2024" without specifying which author or full context, so I should note that Jingyang Zhang is the first author on Min-K%++.

The most concerning citations are the ones with very high arXiv numbers that don't align with their claimed dates—shi2025generalization with arXiv:2509.16499 and basani2026diveye with arXiv:2509.18880 both need verification. zawalski2026codec's arXiv:2510.27055 is similarly suspicious. gambetta2025surplexity at least has an October 2024 timestamp that's more plausible, though "surplexity" as a term could go either way.

I'm also noticing year mismatches in the bibliography where the citation keys don't align with the actual year fields—tirumala2024d4 and xie2024doremi both claim 2024 in their keys but list 2023 in the metadata.

Looking at the related work structure, each of the four main sections has a clear gap statement, which is good. But there's a notable absence of any discussion around ordinal classification, which seems like it should be covered given the paper's focus.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "6d1ab825-abc6-4852-ae91-bab079ba8c98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSNUhSKsQKBaVKd1mX7HDm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4156,
      "cache_read_input_tokens": 23495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4156
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

## Related Work 审查报告

---

### 1. 关键 baseline 覆盖情况

| 方法 | 状态 | 备注 |
|------|------|------|
| DivEye (Basani 2026) | ✅ | line 20 |
| **Binoculars (Hans et al. 2024)** | ❌ 缺失 | 重要 zero-shot 检测方法，与 DetectGPT/Min-K%++ 同级 |
| DetectGPT (Mitchell et al. 2023) | ✅ | line 19 |
| Min-K%++ (Zhang 2024) | ✅ | line 20 |
| CoDeC (Zawalski 2026) | ✅ | line 21 |
| **GLTR (Gehrmann et al. 2019)** | ❌ 缺失 | 早期 statistical detection 开创工作，作为 detection 历史线应提及 |
| Shumailov et al. 2024 (Nature) | ✅ | line 6 |
| Alemohammad et al. 2024 | ✅ | line 7 |
| Dohmatob et al. 2024 | ✅ | line 8 |
| Schaeffer et al. 2025 | ✅ | line 9 |
| DSIR (Xie et al. 2023) | ✅ | line 30 |
| D4 (Tirumala et al. 2023) | ✅ | line 31 |
| DoReMi (Xie et al. 2023) | ✅ | line 31 |
| Drayson et al. 2025 | ✅ | line 34，定位准确 |
| **Ordinal classification baselines** | ❌ 缺失 | 无任何 ordinal regression 引用（见下） |

---

### 2. 潜在遗漏的重要相关工作

**高优先级（建议补充）：**

1. **Binoculars (Hans et al., 2024)** — 用两个 LLM 的 cross-perplexity 比值做 zero-shot 检测，是当前 binary detection 的 SOTA 之一。Binary detection 段落列了 DetectGPT/DivEye/Min-K%++/CoDeC 但漏了 Binoculars，不合理。

2. **GLTR (Gehrmann et al., 2019)** — 基于 token-level 统计（top-k 分布）的早期检测方法，是 statistical fingerprinting 的奠基工作。与论文使用 surprisal 特征的方法论直接相关。

3. **Ordinal regression/classification methods** — 论文将 depth estimation 建模为 ordinal 问题，但 related work 完全没有提及 ordinal classification 文献（如 CORAL [Cao et al. 2020]、ordinal regression 经典方法）。建议加一小段说明为什么 ordinal 建模合适，以及现有 ordinal 方法在此场景的局限。

**中优先级（视篇幅考虑）：**

4. **Benchmark contamination detection** — Shi et al. "Detecting Pretraining Data from Large Language Models" (2023), Golchin & Surdeanu "Time Travel in LLMs" (2024) 等。与本文的 "contamination" 概念有语义重叠，读者可能期望看到区分说明。

5. **Text quality filtering for pretraining** — CCNet (Wenzek et al. 2020)、RefinedWeb (Penedo et al. 2023)、FineWeb。Data Selection 段落只覆盖了 distribution-matching 类方法，heuristic quality filtering 这条线缺失。这些方法与 depth-aware curation 是替代方案关系。

6. **Fast-DetectGPT (Bao et al. 2024)** — DetectGPT 的加速版本，已成为常用 baseline。

**低优先级（可不加）：**

7. **Watermarking 扩展** — 当前只引了 Kirchenbauer 2023 一篇，作为一个独立段落稍薄。但如果篇幅紧张，一篇代表性引用够了。

8. **Information-theoretic analysis** — 与论文方法论关联不够直接，可省略。

---

### 3. 引用真实性抽查

**需验证的可疑引用（2025-2026）：**

| 引用 | 可疑点 | 风险级别 |
|------|--------|---------|
| `shi2025generalization` arXiv:2509.16499 | arXiv ID 为 2509.16499（2025 年 9 月），NeurIPS 2025 Spotlight。作者含 Dacheng Tao（真实知名学者），但其余作者组合需验证 | 中 |
| `basani2026diveye` arXiv:2509.18880 | TMLR 2026 发表。"Yash Basani" 不是该领域常见作者名，需验证 | 中 |
| `zawalski2026codec` arXiv:2510.27055 | ICLR 2026。使用了 `{others}` 省略作者列表，需补全并验证 | 中 |
| `gambetta2025surplexity` arXiv:2410.12341 | "Surplexity" 是自造术语，arXiv ID (2410) 对应 2024 年 10 月，相对可查 | 低-中 |

**bib 文件格式问题：**

- `tirumala2024d4`：bib key 含 "2024" 但 `year={2023}`，NeurIPS 2023 — 年份字段正确但 key 误导
- `xie2024doremi`：同上，key 含 "2024" 但 `year={2023}` — NeurIPS 2023
- `zawalski2026codec` 和 `amin2025escaping`：作者字段用 `{others}` 偷懒，最终提交前必须补全完整作者列表

**bib 文件头部声明（line 2-3）明确标注 "PENDING formal verification"** — 说明团队自身也意识到需要验证。建议在提交前用 Semantic Scholar API 或手动逐条核实所有 2025-2026 引用。

---

### 4. 结构完整性

**当前结构（4 段）：**
1. Model Collapse and Recursive Generation ✅
2. Binary Synthetic Text Detection ✅
3. Data Selection and Curation ✅
4. Watermarking and Provenance ✅

**Gap statement 检查：**
- ¶1 line 14: "do not provide tools for per-text generational depth estimation" ✅
- ¶2 lines 23-26: "produce binary outputs and do not distinguish generational depth" ✅
- ¶3 lines 35-36: "We generalize this binary formulation to ordinal depth estimation" ✅
- ¶4 lines 43-44: "watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings" ✅

每段结尾的 gap statement 都清晰地指向本文贡献，叙事逻辑通顺。

**结构性缺陷：**

- **缺少 Ordinal Classification 段落**：论文核心贡献是将 binary 问题升级为 ordinal 问题，但 related work 没有任何 ordinal regression/classification 文献。这是一个明显的结构缺口——reviewer 几乎一定会问 "why ordinal and not standard multi-class?"。建议在 Binary Detection 和 Data Selection 之间插入一段，讨论 ordinal 方法及其在 NLP 中的应用。

- **Binary Detection 段落偏长**（lines 17-26, ~10 行正文）：包含了方法枚举 + 限制分析 + membership inference 联系 + false positive 讨论。可以考虑将 false positive / self-refinement 讨论移到 introduction 或 discussion。

---

### 改进建议清单

| 优先级 | 建议 |
|--------|------|
| **P0** | 补充 Binoculars (Hans et al. 2024) 到 Binary Detection 段 |
| **P0** | 新增 Ordinal Classification 段落（~5-8 行），引用 CORAL 等经典方法 |
| **P0** | 验证所有 2025-2026 引用的真实性（bib 文件自己也标了 PENDING） |
| **P1** | 补充 GLTR (Gehrmann et al. 2019) 作为 statistical detection 起源 |
| **P1** | 补全 `zawalski2026codec` 和 `amin2025escaping` 的完整作者列表 |
| **P1** | 修正 `tirumala2024d4` 和 `xie2024doremi` 的 bib key 与 year 不一致 |
| **P2** | Data Selection 段补充 heuristic quality filtering 线（CCNet/RefinedWeb） |
| **P2** | 考虑加一句区分 benchmark contamination detection 与本文的 generational contamination |
| **P2** | 补充 Fast-DetectGPT 到 Binary Detection 段 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "uuid": "42c7e2f1-4673-4377-b74f-f45dd42d8b35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSNUhSKsQKBaVKd1mX7HDm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4156,
      "cache_read_input_tokens": 23495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4156
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

_source line 11_

## Related Work 审查报告

---

### 1. 关键 baseline 覆盖情况

| 方法 | 状态 | 备注 |
|------|------|------|
| DivEye (Basani 2026) | ✅ | line 20 |
| **Binoculars (Hans et al. 2024)** | ❌ 缺失 | 重要 zero-shot 检测方法，与 DetectGPT/Min-K%++ 同级 |
| DetectGPT (Mitchell et al. 2023) | ✅ | line 19 |
| Min-K%++ (Zhang 2024) | ✅ | line 20 |
| CoDeC (Zawalski 2026) | ✅ | line 21 |
| **GLTR (Gehrmann et al. 2019)** | ❌ 缺失 | 早期 statistical detection 开创工作，作为 detection 历史线应提及 |
| Shumailov et al. 2024 (Nature) | ✅ | line 6 |
| Alemohammad et al. 2024 | ✅ | line 7 |
| Dohmatob et al. 2024 | ✅ | line 8 |
| Schaeffer et al. 2025 | ✅ | line 9 |
| DSIR (Xie et al. 2023) | ✅ | line 30 |
| D4 (Tirumala et al. 2023) | ✅ | line 31 |
| DoReMi (Xie et al. 2023) | ✅ | line 31 |
| Drayson et al. 2025 | ✅ | line 34，定位准确 |
| **Ordinal classification baselines** | ❌ 缺失 | 无任何 ordinal regression 引用（见下） |

---

### 2. 潜在遗漏的重要相关工作

**高优先级（建议补充）：**

1. **Binoculars (Hans et al., 2024)** — 用两个 LLM 的 cross-perplexity 比值做 zero-shot 检测，是当前 binary detection 的 SOTA 之一。Binary detection 段落列了 DetectGPT/DivEye/Min-K%++/CoDeC 但漏了 Binoculars，不合理。

2. **GLTR (Gehrmann et al., 2019)** — 基于 token-level 统计（top-k 分布）的早期检测方法，是 statistical fingerprinting 的奠基工作。与论文使用 surprisal 特征的方法论直接相关。

3. **Ordinal regression/classification methods** — 论文将 depth estimation 建模为 ordinal 问题，但 related work 完全没有提及 ordinal classification 文献（如 CORAL [Cao et al. 2020]、ordinal regression 经典方法）。建议加一小段说明为什么 ordinal 建模合适，以及现有 ordinal 方法在此场景的局限。

**中优先级（视篇幅考虑）：**

4. **Benchmark contamination detection** — Shi et al. "Detecting Pretraining Data from Large Language Models" (2023), Golchin & Surdeanu "Time Travel in LLMs" (2024) 等。与本文的 "contamination" 概念有语义重叠，读者可能期望看到区分说明。

5. **Text quality filtering for pretraining** — CCNet (Wenzek et al. 2020)、RefinedWeb (Penedo et al. 2023)、FineWeb。Data Selection 段落只覆盖了 distribution-matching 类方法，heuristic quality filtering 这条线缺失。这些方法与 depth-aware curation 是替代方案关系。

6. **Fast-DetectGPT (Bao et al. 2024)** — DetectGPT 的加速版本，已成为常用 baseline。

**低优先级（可不加）：**

7. **Watermarking 扩展** — 当前只引了 Kirchenbauer 2023 一篇，作为一个独立段落稍薄。但如果篇幅紧张，一篇代表性引用够了。

8. **Information-theoretic analysis** — 与论文方法论关联不够直接，可省略。

---

### 3. 引用真实性抽查

**需验证的可疑引用（2025-2026）：**

| 引用 | 可疑点 | 风险级别 |
|------|--------|---------|
| `shi2025generalization` arXiv:2509.16499 | arXiv ID 为 2509.16499（2025 年 9 月），NeurIPS 2025 Spotlight。作者含 Dacheng Tao（真实知名学者），但其余作者组合需验证 | 中 |
| `basani2026diveye` arXiv:2509.18880 | TMLR 2026 发表。"Yash Basani" 不是该领域常见作者名，需验证 | 中 |
| `zawalski2026codec` arXiv:2510.27055 | ICLR 2026。使用了 `{others}` 省略作者列表，需补全并验证 | 中 |
| `gambetta2025surplexity` arXiv:2410.12341 | "Surplexity" 是自造术语，arXiv ID (2410) 对应 2024 年 10 月，相对可查 | 低-中 |

**bib 文件格式问题：**

- `tirumala2024d4`：bib key 含 "2024" 但 `year={2023}`，NeurIPS 2023 — 年份字段正确但 key 误导
- `xie2024doremi`：同上，key 含 "2024" 但 `year={2023}` — NeurIPS 2023
- `zawalski2026codec` 和 `amin2025escaping`：作者字段用 `{others}` 偷懒，最终提交前必须补全完整作者列表

**bib 文件头部声明（line 2-3）明确标注 "PENDING formal verification"** — 说明团队自身也意识到需要验证。建议在提交前用 Semantic Scholar API 或手动逐条核实所有 2025-2026 引用。

---

### 4. 结构完整性

**当前结构（4 段）：**
1. Model Collapse and Recursive Generation ✅
2. Binary Synthetic Text Detection ✅
3. Data Selection and Curation ✅
4. Watermarking and Provenance ✅

**Gap statement 检查：**
- ¶1 line 14: "do not provide tools for per-text generational depth estimation" ✅
- ¶2 lines 23-26: "produce binary outputs and do not distinguish generational depth" ✅
- ¶3 lines 35-36: "We generalize this binary formulation to ordinal depth estimation" ✅
- ¶4 lines 43-44: "watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings" ✅

每段结尾的 gap statement 都清晰地指向本文贡献，叙事逻辑通顺。

**结构性缺陷：**

- **缺少 Ordinal Classification 段落**：论文核心贡献是将 binary 问题升级为 ordinal 问题，但 related work 没有任何 ordinal regression/classification 文献。这是一个明显的结构缺口——reviewer 几乎一定会问 "why ordinal and not standard multi-class?"。建议在 Binary Detection 和 Data Selection 之间插入一段，讨论 ordinal 方法及其在 NLP 中的应用。

- **Binary Detection 段落偏长**（lines 17-26, ~10 行正文）：包含了方法枚举 + 限制分析 + membership inference 联系 + false positive 讨论。可以考虑将 false positive / self-refinement 讨论移到 introduction 或 discussion。

---

### 改进建议清单

| 优先级 | 建议 |
|--------|------|
| **P0** | 补充 Binoculars (Hans et al. 2024) 到 Binary Detection 段 |
| **P0** | 新增 Ordinal Classification 段落（~5-8 行），引用 CORAL 等经典方法 |
| **P0** | 验证所有 2025-2026 引用的真实性（bib 文件自己也标了 PENDING） |
| **P1** | 补充 GLTR (Gehrmann et al. 2019) 作为 statistical detection 起源 |
| **P1** | 补全 `zawalski2026codec` 和 `amin2025escaping` 的完整作者列表 |
| **P1** | 修正 `tirumala2024d4` 和 `xie2024doremi` 的 bib key 与 year 不一致 |
| **P2** | Data Selection 段补充 heuristic quality filtering 线（CCNet/RefinedWeb） |
| **P2** | 考虑加一句区分 benchmark contamination detection 与本文的 generational contamination |
| **P2** | 补充 Fast-DetectGPT 到 Binary Detection 段 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 83645,
  "duration_api_ms": 84514,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "3821aa19-5666-4636-bd3d-9d35c3af77c8",
  "total_cost_usd": 0.23267549999999998,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 15810,
    "cache_read_input_tokens": 35336,
    "output_tokens": 4583,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15810,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4385,
        "cache_read_input_tokens": 23495,
        "cache_creation_input_tokens": 4156,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4156
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1520,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0016,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 4583,
      "cacheReadInputTokens": 35336,
      "cacheCreationInputTokens": 15810,
      "webSearchRequests": 0,
      "costUSD": 0.2310755,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "98bc4827-1f92-47c4-8edf-b367c26a2db1"
}
```

</details>

---
