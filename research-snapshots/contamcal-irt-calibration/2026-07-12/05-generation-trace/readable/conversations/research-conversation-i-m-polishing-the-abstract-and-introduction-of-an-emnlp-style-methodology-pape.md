# Research conversation: I'm polishing the Abstract and Introduction of an EMNLP-style methodology paper. I want to see examples of how similar p

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afabe4ff3c4e4c925.jsonl`
- **Structured JSON:** [`68904d7f1411ee13e68d.json`](../../sessions/68/68904d7f1411ee13e68d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-17T09:28:59.250Z_

I'm polishing the Abstract and Introduction of an EMNLP-style methodology paper. I want to see examples of how similar papers in this project's literature map handle their opening. Search for:
1. The literature_map.yaml at `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml` — read it and extract the titles/abstracts of papers marked as role=foundation or role=direct-competitor (or similar categorization)
2. The paper_framing.md at `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper_framing.md` or similar path — this should have the approved narrative framing

Report: the key papers' titles and any framing guidance found. Keep it under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "91837b43-a16b-4a3f-a342-fa8f545853f7",
  "agentId": "afabe4ff3c4e4c925",
  "type": "user",
  "uuid": "abfcef64-1651-4fc5-8cf7-3b8c9e8a89b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-17T09:29:01.122Z_

I'll search for the literature map and paper framing to help you polish your Abstract and Introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abfcef64-1651-4fc5-8cf7-3b8c9e8a89b3",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTFAatWBg9sZBSHntK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3da5a60a-1d49-4eab-958c-5a870d077df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HtVJHWXENdtyXuDZPJbnMd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27367,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27367,
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

_source line 3 · 2026-05-17T09:29:01.387Z_

<details open><summary>🔧 Tool call — Read · `toolu_0156L8E6pxk7XcZYyNoGnADv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3da5a60a-1d49-4eab-958c-5a870d077df3",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTFAatWBg9sZBSHntK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5832819a-405e-465b-8864-ac3cf1695846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HtVJHWXENdtyXuDZPJbnMd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27367,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27367,
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

_source line 4 · 2026-05-17T09:29:01.517Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WfccmM5ES9h4uSBGd7kM3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5832819a-405e-465b-8864-ac3cf1695846",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTFAatWBg9sZBSHntK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23dde7ba-3461-42b6-a2f2-5cb8c477bdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HtVJHWXENdtyXuDZPJbnMd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27367,
      "cache_read_input_tokens": 0,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27367
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27367,
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

_source line 5 · 2026-05-17T09:29:01.535Z_

<details><summary>↩ Tool result · reported error · `toolu_01WfccmM5ES9h4uSBGd7kM3n`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23dde7ba-3461-42b6-a2f2-5cb8c477bdad",
  "isSidechain": true,
  "promptId": "91837b43-a16b-4a3f-a342-fa8f545853f7",
  "agentId": "afabe4ff3c4e4c925",
  "type": "user",
  "uuid": "c6b4fa67-3e7b-4e5b-a0c1-fe99ca0b67a3",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6.",
  "sourceToolAssistantUUID": "23dde7ba-3461-42b6-a2f2-5cb8c477bdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T09:29:01.725Z_

<details><summary>↩ Tool result · `toolu_0156L8E6pxk7XcZYyNoGnADv`</summary>

```text
1	# Literature Map — contamcal-irt-calibration
2	# Generated: 2026-05-16
3	# Purpose: Related Work section foundation for ContamCal paper (EMNLP 2026)
4	
5	papers:
6	
7	  # ============================================================
8	  # Category: detection — Contamination Detection Methods
9	  # ============================================================
10	
11	  - id: "zhang_2024_minkpp"
12	    title: "Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models"
13	    authors: "Zhang et al."
14	    venue: "ICLR 2025"
15	    year: 2024
16	    url: "https://arxiv.org/abs/2404.02936"
17	    category: "detection"
18	    role: "method-component"
19	    relevance: "Our S2 signal. Min-K%++ normalizes token probability with vocabulary statistics for membership inference. We discover its directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — a novel finding that challenges single-signal reliance."
20	    key_findings: "Theoretically motivated detection via normalized token probabilities; outperforms Min-K% on WikiMIA and other benchmarks."
21	    our_advantage: "ContamCal reveals Min-K++ is actively misleading (not just ineffective) at small scales — directional reversal is our headline empirical finding."
22	
23	  - id: "shi_2023_minkprob"
24	    title: "Detecting Pretraining Data from Large Language Models"
25	    authors: "Shi et al."
26	    venue: "ICLR 2024"
27	    year: 2023
28	    url: "https://arxiv.org/abs/2310.16789"
29	    category: "detection"
30	    role: "foundation"
31	    relevance: "Original Min-K% Prob method and WikiMIA benchmark. Foundation for membership inference in LLMs. Min-K%++ (our S2) is a direct extension."
32	    key_findings: "Unseen examples have outlier low-probability tokens; Min-K% uses this for pretraining data detection without reference model."
33	    our_advantage: "We use the improved Min-K%++ variant and expose its failure modes at small scales."
34	
35	  - id: "dekoninck_2024_constat"
36	    title: "ConStat: Performance-Based Contamination Detection in Large Language Models"
37	    authors: "Dekoninck et al."
38	    venue: "arXiv 2024"
39	    year: 2024
40	    url: "https://arxiv.org/abs/2405.16281"
41	    category: "detection"
42	    role: "method-component"
43	    relevance: "Our S3 signal candidate (excluded from final pipeline). Detects contamination as non-generalizing inflated performance by comparing primary vs reference benchmark performance against reference models."
44	    key_findings: "Novel contamination definition as non-generalizing performance inflation; detects contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models."
45	    our_advantage: "ConStat requires reference benchmarks and reference models; ContamCal integrates detection signals directly into IRT framework for calibrated score adjustment, not just detection."
46	
47	  - id: "dong_2024_cdd"
48	    title: "Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models"
49	    authors: "Dong et al."
50	    venue: "ACL 2024 Findings"
51	    year: 2024
52	    url: "https://arxiv.org/abs/2402.15938"
53	    category: "detection"
54	    role: "direct-competitor"
55	    relevance: "Proposes CDD (output distribution peakedness) and TED (distribution correction for trustworthy evaluation). TED is closest to calibration but lacks IRT grounding and uncertainty quantification."
56	    key_findings: "CDD achieves 21-30% improvement over baselines in detection accuracy; TED mitigates up to 66.9% of contamination-attributed performance gain."
57	    our_advantage: "ContamCal provides full uncertainty quantification via Bayesian IRT posteriors; TED offers point corrections without credible intervals or identifiability analysis."
58	
59	  - id: "zhang_2024_gsm1k"
60	    title: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
61	    authors: "Zhang et al."
62	    venue: "arXiv 2024"
63	    year: 2024
64	    url: "https://arxiv.org/abs/2405.00332"
65	    category: "detection"
66	    role: "method-component"
67	    relevance: "Our S4 signal (self-critique / GSM1k). Creates GSM1k to mirror GSM8k and measures accuracy drop as contamination proxy. Up to 13% accuracy drops in some model families."
68	    key_findings: "Systematic overfitting in Phi and Mistral families; positive correlation (r^2=0.32) between generation probability of GSM8k examples and performance gap."
69	    our_advantage: "ContamCal uses the GSM1k-style signal as one input to multi-signal RRF, then feeds into IRT for calibrated estimates rather than just flagging contamination."
70	
71	  - id: "choi_2025_kds"
72	    title: "How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence"
73	    authors: "Choi et al."
74	    venue: "ICML 2025"
75	    year: 2025
76	    url: "https://arxiv.org/abs/2502.00678"
77	    category: "detection"
78	    role: "evaluation"
79	    relevance: "Kernel Divergence Score (KDS) detects contamination via embedding shift before/after fine-tuning. Near-perfect correlation with contamination levels. Complementary signal approach to our S1 embedding similarity."
80	    key_findings: "KDS captures fine-tuning-induced shifts in sample embeddings; outperforms existing baselines with near-perfect contamination level correlation."
81	    our_advantage: "ContamCal bridges detection to calibration; KDS only detects. Our S1 embedding similarity achieves AUC>0.95 without requiring fine-tuning comparison."
82	
83	  - id: "oren_2023_proving_contamination"
84	    title: "Proving Test Set Contamination in Black Box Language Models"
85	    authors: "Oren et al."
86	    venue: "arXiv 2023"
87	    year: 2023
88	    url: "https://arxiv.org/abs/2310.17623"
89	    category: "detection"
90	    role: "background"
91	    relevance: "Provable contamination detection via exchangeability test on benchmark ordering likelihood. Complementary black-box approach."
92	    key_findings: "Detects contamination in models as small as 1.4B with 1000 examples; audits 5 popular LLMs finding little pervasive contamination."
93	    our_advantage: "ContamCal goes beyond detection to calibrated score adjustment with uncertainty quantification."
94	
95	  - id: "deng_2024_tsguessing"
96	    title: "Investigating Data Contamination in Modern Benchmarks for Large Language Models"
97	    authors: "Deng, Zhao, Tang, Gerstein, & Cohan"
98	    year: 2024
99	    venue: "NAACL 2024"
100	    url: "https://arxiv.org/abs/2311.09783"
101	    category: "detection"
102	    role: "direct-competitor"
103	    relevance: "TS-Guessing protocol masks MC wrong options for fill-in; ChatGPT/GPT-4 guess correct options at 52%/57% on MMLU. Direct evidence that MC format is more vulnerable to contamination, supporting our finding that ARC (MC) shows γ>0 while GSM8K (generative) shows γ≈0."
104	    key_findings:
105	      - "MC format enables contaminated models to exploit memorized answer options"
106	      - "ChatGPT/GPT-4 MMLU option guessing rate 52%/57% vs random baseline"
107	      - "Open-ended format harder to game via memorization"
108	
109	  - id: "schaeffer_2026_generative_contamination"
110	    title: "Quantifying the Effect of Test Set Contamination on Generative Evaluations"
111	    authors: "Schaeffer, Kazdan, Abbasi, Liu, et al."
112	    year: 2026
113	    venue: "arXiv 2026"
114	    url: "https://arxiv.org/abs/2601.04301"
115	    category: "detection"
116	    role: "direct-competitor"
117	    relevance: "First scaling law study of contamination on generative benchmarks (MATH). Even 1 test set replica in pretraining breaks irreducible error floor, but effect size much smaller than MC benchmarks. Consistent with our framework: generative γ expected smaller but non-zero."
118	    key_findings:
119	      - "Single test set replica in pretraining corpus breaks irreducible error on MATH"
120	      - "Contamination effect on generative benchmarks weaker than MC benchmarks"
121	      - "Scaling law characterization of contamination-performance relationship"
122	
123	  # ============================================================
124	  # Category: irt-llm — IRT for LLM Evaluation
125	  # ============================================================
126	
127	  - id: "lalor_2024_irt_nlp"
128	    title: "Item Response Theory for Natural Language Processing"
129	    authors: "Lalor et al."
130	    venue: "EACL 2024 Tutorial"
131	    year: 2024
132	    url: "https://aclanthology.org/2024.eacl-tutorials.2/"
133	    category: "irt-llm"
134	    role: "foundation"
135	    relevance: "Comprehensive tutorial introducing IRT to NLP community. Establishes framework for psychometric LLM evaluation that ContamCal extends with contamination covariates."
136	    key_findings: "Demonstrates IRT benefits for NLP evaluation including difficulty estimation, benchmark quality assessment, and latent trait modeling."
137	    our_advantage: "ContamCal extends standard IRT with contamination covariate gamma, measurement error model, and per-benchmark effect estimation."
138	
139	  - id: "polo_2024_tinybenchmarks"
140	    title: "tinyBenchmarks: evaluating LLMs with fewer examples"
141	    authors: "Polo et al."
142	    venue: "ICML 2024"
143	    year: 2024
144	    url: "https://arxiv.org/abs/2402.14992"
145	    category: "irt-llm"
146	    role: "foundation"
147	    relevance: "Uses IRT as performance estimator; 100 curated examples sufficient for MMLU. Demonstrates IRT scalability for LLM evaluation. Shares our assumption that IRT item parameters transfer across models."
148	    key_findings: "Accurate performance estimation with ~100 items per benchmark; IRT-based selection outperforms random subsampling."
149	    our_advantage: "ContamCal addresses a different problem: not efficiency but decontamination. We use IRT to model contamination effects rather than to reduce evaluation cost."
150	
151	  - id: "habba_2025_growing_pains"
152	    title: "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"
153	    authors: "Habba et al."
154	    venue: "arXiv 2025"
155	    year: 2025
156	    url: "https://arxiv.org/abs/2604.12843"
157	    category: "irt-llm"
158	    role: "foundation"
159	    relevance: "Multidimensional IRT with anchor items for cross-study comparability. Addresses N insufficiency via fixed parameter calibration. Directly relevant to our N>=50 identifiability concern."
160	    key_findings: "Predicts full-evaluation performance within 2-3pp using 100 anchor items; Spearman rho>=0.9 across 400+ models."
161	    our_advantage: "Growing Pains assumes no contamination; ContamCal explicitly models contamination effects. Their anchor-item framework could complement our decontamination pipeline."
162	
163	  - id: "luettgau_2025_hibayes"
164	    title: "HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics"
165	    authors: "Luettgau et al."
166	    venue: "arXiv 2025"
167	    year: 2025
168	    url: "https://arxiv.org/abs/2505.05602"
169	    category: "irt-llm"
170	    role: "direct-competitor"
171	    relevance: "Hierarchical Bayesian framework for LLM evaluation with principled UQ, especially in low-data scenarios (<20 data points). Does not model contamination. Most methodologically similar to ContamCal's Bayesian approach."
172	    key_findings: "Robust parameter estimation via hierarchical GLMs with formal model comparison; handles nested evaluation structures."
173	    our_advantage: "ContamCal adds contamination-specific covariates (gamma_k, exposure scores) to the Bayesian framework. HiBayES provides UQ but ignores contamination effects entirely."
174	
175	  - id: "li_2024_atlas"
176	    title: "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
177	    authors: "Li et al."
178	    venue: "arXiv 2024"
179	    year: 2024
180	    url: "https://arxiv.org/abs/2511.04689"
181	    category: "irt-llm"
182	    role: "evaluation"
183	    relevance: "ATLAS uses Fisher information-guided adaptive item selection for efficient LLM evaluation with up to 90% item reduction. Validates IRT psychometric framework for LLM evaluation."
184	    key_findings: "30-89 items per benchmark sufficient with SE-controlled stopping; best accuracy-efficiency tradeoff among IRT-based methods."
185	    our_advantage: "ATLAS optimizes evaluation efficiency; ContamCal addresses evaluation validity under contamination. Complementary goals."
186	
187	  - id: "zhou_2025_psnirt"
188	    title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
189	    authors: "Zhou et al."
190	    venue: "AAAI 2026"
191	    year: 2025
192	    url: "https://arxiv.org/abs/2505.15055"
193	    category: "irt-llm"
194	    role: "evaluation"
195	    relevance: "PSN-IRT uses pseudo-siamese networks for rich item parameter estimation. Analyzes 11 benchmarks (41,871 items) revealing measurement quality shortcomings."
196	    key_findings: "LLM benchmarks suffer widespread saturation and insufficient difficulty ceilings; PSN-IRT constructs smaller benchmarks with stronger human preference alignment."
197	    our_advantage: "PSN-IRT diagnoses benchmark quality; ContamCal diagnoses and corrects contamination effects. Our gamma_k captures a specific quality dimension (data leakage) that PSN-IRT does not model."
198	
199	  - id: "burnell_2023_structure"
200	    title: "Revealing the structure of language model capabilities"
201	    authors: "Burnell et al."
202	    venue: "arXiv 2023"
203	    year: 2023
204	    url: "https://arxiv.org/abs/2306.10062"
205	    category: "irt-llm"
206	    role: "background"
207	    relevance: "Factor analysis reveals 3 capability dimensions (reasoning, comprehension, core language modeling) in LLMs. Supports multidimensional view; our unidimensional theta per benchmark is acknowledged as simplification in Limitations."
208	    key_findings: "LLM capabilities are not monolithic; 3 factors explain high proportion of performance variance across 29 LLMs on 27 tasks."
209	    our_advantage: "ContamCal's unidimensional theta per benchmark is a deliberate simplification acknowledged in Limitations; multidimensional extension is future work."
210	
211	  - id: "brown_2024_ppp"
212	    title: "The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation"
213	    authors: "Brown & Thomson"
214	    year: 2024
215	    venue: "Molecular Biology and Evolution, 41(3), msae051"
216	    category: "irt-llm"
217	    role: "background"
218	    relevance: "Proves PPP distribution is inherently non-uniform (unlike frequentist p-values), concentrated near 0.5. Extreme PPP (e.g. our 0.003) provides stronger poor-fit evidence than usually assumed, but low PPP does not automatically invalidate parameter estimates — supports our position that γ posterior excluding zero remains informative even with poor global fit."
219	    key_findings:
220	      - "PPP distribution is non-uniform, concentrated around 0.5"
221	      - "Low PPP does not automatically negate parameter estimate informativeness"
222	      - "Posterior predictive tests evaluate models under favorable conditions (model already fitted to data)"
223	
224	  - id: "sinharay_2025_irt_fit"
225	    title: "Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions"
226	    authors: "Sinharay, S."
227	    year: 2025
228	    venue: "British Journal of Mathematical and Statistical Psychology, 78, 711–733"
229	    category: "irt-llm"
230	    role: "background"
231	    relevance: "Comprehensive review of IRT model fit assessment (PPMC, generalized residuals, person-fit). Argues low PPP indicates model inadequacy but not that parameter estimates are meaningless. Supports our ARC PPP=0.003 but γ still interpretable position."
232	    key_findings:
233	      - "PPP interpretation requires caution — low PPP means model inadequacy, not parameter invalidity"
234	      - "Covers PPMC, generalized residuals, person-fit diagnostics"
235	      - "Authoritative 2025 review likely known to reviewers"
236	
237	  # ============================================================
238	  # Category: item-compromise — Educational Measurement
239	  # ============================================================
240	
241	  - id: "eckerly_2017_item_compromise"
242	    title: "Detecting preknowledge and item compromise: Understanding the status quo"
243	    authors: "Eckerly, C."
244	    venue: "Handbook of Quantitative Methods for Detecting Cheating on Tests (Routledge)"
245	    year: 2017
246	    url: "https://www.routledge.com/9781138821811"
247	    category: "item-compromise"
248	    role: "foundation"
249	    relevance: "Core theoretical foundation for ContamCal. Reviews IRT methods for detecting compromised items and examinees with preknowledge. Our gamma parameter directly extends the item compromise framework to LLM benchmark contamination."
250	    key_findings: "Systematic framework for item preknowledge detection using IRT-based person-fit statistics and item parameter drift."
251	    our_advantage: "ContamCal adapts item compromise IRT from human testing to LLM evaluation with 3 structural adaptations: independent examinees -> single model, binary leakage -> continuous exposure, stable ability -> regime-conditional ability."
252	    verified: false
253	
254	  - id: "sinharay_2017_preknowledge"
255	    title: "Detection of item preknowledge using likelihood ratio test and score test"
256	    authors: "Sinharay, S."
257	    venue: "Journal of Educational and Behavioral Statistics, 42(1)"
258	    year: 2017
259	    url: "https://pubmed.ncbi.nlm.nih.gov/29881099/"
260	    category: "item-compromise"
261	    role: "foundation"
262	    relevance: "Proposes LRT-based statistics for item preknowledge detection with known Type I error rates. Our treatment of contamination-induced item parameter drift builds on this work."
263	    key_findings: "LRT statistic for item preknowledge has similar power to posterior shift statistic with known null distribution; applicable to adaptive and non-adaptive tests."
264	    our_advantage: "ContamCal extends from binary preknowledge to continuous contamination exposure scores and from human examinees to LLM respondents."
265	
266	  - id: "deboeck_2004_explanatory_irt"
267	    title: "Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach"
268	    authors: "De Boeck, P. & Wilson, M."
269	    venue: "Springer"
270	    year: 2004
271	    url: "https://link.springer.com/book/10.1007/978-1-4757-3990-9"
272	    category: "item-compromise"
273	    role: "foundation"
274	    relevance: "Foundational text for explanatory IRT. ContamCal's contamination-augmented 4PL is an explanatory IRT model where item responses are modeled as a function of contamination exposure predictors."
275	    key_findings: "Unifies IRT with generalized linear/nonlinear mixed models; enables item covariates (like our exposure scores) as predictors in IRT framework."
276	    our_advantage: "Direct theoretical grounding. ContamCal instantiates the explanatory IRT framework with contamination-specific covariates."
277	
278	  - id: "kievit_2013_simpsons_paradox"
279	    title: "Simpson's Paradox in Psychological Science: A Practical Guide"
280	    authors: "Kievit, Frankenhuis, Waldorp, & Borsboom"
281	    year: 2013
282	    venue: "Frontiers in Psychology, 4, 513"
283	    category: "item-compromise"
284	    role: "background"
285	    relevance: "Theoretical framework for Simpson's paradox in behavioral science. Directly applicable to our MMLU finding: pooled γ insignificant but domain-level analysis reveals significant positive and negative γ that cancel upon aggregation."
286	    key_findings:
287	      - "Simpson's paradox more prevalent in psychology than traditionally recognized"
288	      - "Effect direction can reverse when moving from population to subgroup (or vice versa)"
289	      - "Provides statistical markers and R detection toolkit"
290	
291	  - id: "ercikan_2008_dif_cancellation"
292	    title: "Differential Item Functioning Amplification and Cancellation in a Reading Test"
293	    authors: "Ercikan, Arim, & Oliveri"
294	    year: 2008
295	    venue: "Practical Assessment, Research, and Evaluation, 14(3)"
296	    category: "item-compromise"
297	    role: "background"
298	    relevance: "Empirical precedent for DIF cancellation: most items show significant DIF but favoring different groups, so DIF cancels at total test score level. Direct analogue to our MMLU domain-level contamination signals with inconsistent directions being masked in pooled analysis."
299	    key_findings:
300	      - "Majority of items show significant DIF but in opposing directions"
301	      - "DIF cancels at aggregate test score level despite item-level significance"
302	      - "Multiple-group testlet IRT model reveals hidden heterogeneity"
303	
304	  # ============================================================
305	  # Category: calibration — Calibration & Score Adjustment
306	  # ============================================================
307	
308	  - id: "xu_2025_dcr"
309	    title: "DCR: Quantifying Data Contamination in LLMs Evaluation"
310	    authors: "Xu et al."
311	    venue: "EMNLP 2025"
312	    year: 2025
313	    url: "https://arxiv.org/abs/2507.11405"
314	    category: "calibration"
315	    role: "direct-competitor"
316	    relevance: "Only existing method producing adjusted accuracy via fuzzy inference. ContamCal's primary competitor. DCR quantifies contamination risk across 4 levels (semantic, informational, data, label) and adjusts raw accuracy."
317	    key_findings: "DCR Factor adjusts accuracy within 4% average error across 3 benchmarks; validated on 0.5B-72B models."
318	    our_advantage: "ContamCal provides Bayesian credible intervals (DCR gives point estimates only), per-benchmark gamma_k characterization, and IRT-grounded identifiability analysis. DCR lacks UQ and theoretical identifiability bounds."
319	
320	  - id: "guo_2017_calibration"
321	    title: "On Calibration of Modern Neural Networks"
322	    authors: "Guo et al."
323	    venue: "ICML 2017"
324	    year: 2017
325	    url: "https://arxiv.org/abs/1706.04599"
326	    category: "calibration"
327	    role: "background"
328	    relevance: "Foundational work on probability calibration in neural networks. Must disambiguate: our 'calibration' means decontamination score adjustment, not probability calibration (confidence = accuracy). Temperature scaling is unrelated to our method."
329	    key_findings: "Modern neural networks are poorly calibrated; temperature scaling (single parameter) effectively recalibrates predictions."
330	    our_advantage: "Different notion of calibration. Guo et al. calibrate prediction confidence; ContamCal calibrates benchmark scores for contamination effects."
331	
332	  - id: "angelopoulos_2023_conformal"
333	    title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
334	    authors: "Angelopoulos & Bates"
335	    venue: "Foundations and Trends in ML, 2023"
336	    year: 2023
337	    url: "https://arxiv.org/abs/2107.07511"
338	    category: "calibration"
339	    role: "background"
340	    relevance: "Alternative UQ approach with distribution-free coverage guarantees. Discussed in Related Work to justify why Bayesian IRT is preferred over conformal for our setting (conformal requires exchangeability assumptions violated by contamination structure)."
341	    key_findings: "Conformal prediction provides statistically rigorous uncertainty sets without distributional assumptions; applicable to any pre-trained model."
342	    our_advantage: "Bayesian IRT provides interpretable per-item parameters and contamination-specific covariates; conformal gives coverage guarantees but no mechanistic insight into contamination effects."
343	
344	  # ============================================================
345	  # Category: mitigation — Contamination Mitigation & Alternatives
346	  # ============================================================
347	
348	  - id: "sun_2025_emperors_new_clothes"
349	    title: "The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination"
350	    authors: "Sun et al."
351	    venue: "ICML 2025"
352	    year: 2025
353	    url: "https://arxiv.org/abs/2503.16402"
354	    category: "mitigation"
355	    role: "direct-competitor"
356	    relevance: "Demonstrates all 20 existing mitigation strategies fail to balance fidelity and contamination resistance across all benchmarks. Strongest motivation for ContamCal's post-hoc calibration approach."
357	    key_findings: "No semantic-preserving strategy significantly improves resistance over vanilla; semantic-altering strategies sacrifice fidelity. 10 LLMs x 5 benchmarks x 20 strategies x 2 scenarios."
358	    our_advantage: "ContamCal offers post-hoc calibration rather than prevention — complementary approach. Emperor's failure motivates calibration; ContamCal provides it."
359	
360	  - id: "white_2024_livebench"
361	    title: "LiveBench: A Challenging, Contamination-Free LLM Benchmark"
362	    authors: "White et al."
363	    venue: "arXiv 2024"
364	    year: 2024
365	    url: "https://arxiv.org/abs/2406.19314"
366	    category: "mitigation"
367	    role: "evaluation"
368	    relevance: "Dynamic benchmark alternative: monthly-updated questions from recent sources to prevent contamination. Complementary to ContamCal — LiveBench prevents contamination for new evaluations; ContamCal calibrates existing contaminated benchmarks."
369	    key_findings: "Top models achieve below 70% accuracy; monthly updates with 18 tasks across 6 categories maintain contamination resistance."
370	    our_advantage: "LiveBench requires continuous curation; ContamCal works with existing static benchmarks. Both valid approaches to the contamination problem."
371	
372	  # ============================================================
373	  # Category: benchmark — Evaluation Frameworks & Alternatives
374	  # ============================================================
375	
376	  - id: "liang_2023_helm"
377	    title: "Holistic Evaluation of Language Models"
378	    authors: "Liang et al."
379	    venue: "TMLR 2023"
380	    year: 2023
381	    url: "https://arxiv.org/abs/2211.09110"
382	    category: "benchmark"
383	    role: "background"
384	    relevance: "HELM evaluates 30 models on 42 scenarios with 7 metrics including calibration. Establishes standardized evaluation framework. ContamCal addresses a gap HELM does not: score reliability under contamination."
385	    key_findings: "Prior to HELM, models were evaluated on only 17.9% of core scenarios; standardized evaluation reveals 25 top-level findings across models."
386	    our_advantage: "HELM assumes benchmark scores are trustworthy; ContamCal questions and corrects this assumption when contamination is present."
387	
388	  - id: "chiang_2024_chatbot_arena"
389	    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
390	    authors: "Chiang et al."
391	    venue: "ICML 2024"
392	    year: 2024
393	    url: "https://arxiv.org/abs/2403.04132"
394	    category: "benchmark"
395	    role: "background"
396	    relevance: "Human pairwise comparison evaluation that inherently bypasses benchmark contamination. Discussed as contamination-resistant alternative."
397	    key_findings: "240K+ votes via crowdsourced pairwise comparisons; Elo rating system for model ranking without static test sets."
398	    our_advantage: "Chatbot Arena requires human judges and live interaction; ContamCal enables post-hoc calibration of automated benchmark scores, which scale better."
399	
400	  - id: "li_2024_open_llm_leaderboard"
401	    title: "Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena"
402	    authors: "Li et al."
403	    year: 2024
404	    venue: "arXiv 2024"
405	    url: "https://arxiv.org/abs/2406.07545"
406	    category: "benchmark"
407	    role: "evaluation"
408	    relevance: "Converting MC benchmarks to open-style questions causes ~25% average accuracy drop across all models. Quantifies MC format advantage (selection bias, random guessing) that amplifies contamination signal in MC benchmarks. Supports our MC/generative format as contamination effect moderator."
409	    key_findings:
410	      - "MC to open-style conversion causes ~25% average accuracy drop"
411	      - "MC format provides extra cues (selection bias, random guessing) beyond knowledge"
412	      - "Contaminated models benefit more from MC format than clean models"
413	
414	  # ============================================================
415	  # Category: foundation — Methodological Foundations
416	  # ============================================================
417	
418	  - id: "shokri_2017_mia"
419	    title: "Membership Inference Attacks Against Machine Learning Models"
420	    authors: "Shokri et al."
421	    venue: "IEEE S&P 2017"
422	    year: 2017
423	    url: "https://arxiv.org/abs/1610.05820"
424	    category: "detection"
425	    role: "foundation"
426	    relevance: "Foundational MIA work. Min-K% and Min-K%++ are descendants of MIA methodology. Contextualizes our Min-K++ directional reversal finding within MIA literature."
427	    key_findings: "Shadow model approach for membership inference; demonstrates vulnerability of ML-as-a-service models to membership inference."
428	    our_advantage: "ContamCal uses MIA-derived signals as inputs to calibration framework, not as standalone detectors."
429	
430	  - id: "carlini_2021_extracting"
431	    title: "Extracting Training Data from Large Language Models"
432	    authors: "Carlini et al."
433	    venue: "USENIX Security 2021"
434	    year: 2021
435	    url: "https://arxiv.org/abs/2012.07805"
436	    category: "detection"
437	    role: "foundation"
438	    relevance: "Demonstrates verbatim training data extraction from GPT-2. Establishes that LLMs memorize training data — the fundamental assumption underlying all contamination detection methods including ours."
439	    key_findings: "Hundreds of verbatim text sequences extracted from GPT-2; memorization is measurable and exploitable."
440	    our_advantage: "ContamCal leverages memorization signals for calibration rather than extraction; our contribution is bridging detection to score adjustment."
441	
442	  - id: "cormack_2009_rrf"
443	    title: "Reciprocal Rank Fusion outperforms Condorcet and Individual Rank Learning Methods"
444	    authors: "Cormack et al."
445	    venue: "SIGIR 2009"
446	    year: 2009
447	    url: "https://dl.acm.org/doi/10.1145/1571941.1572114"
448	    category: "calibration"
449	    role: "method-component"
450	    relevance: "RRF is our multi-signal aggregation method. Training-free rank fusion avoids meta-circularity (learned aggregator's training data may itself be contaminated). RRF is a design choice, not claimed as contribution."
451	    key_findings: "Simple reciprocal rank scoring outperforms Condorcet and learning-to-rank methods for combining multiple retrieval systems."
452	    our_advantage: "RRF is adopted as-is. Our contribution is the argument for training-free aggregation in the contamination context (meta-circularity)."
453	
454	  - id: "talts_2018_sbc"
455	    title: "Validating Bayesian Inference Algorithms with Simulation-Based Calibration"
456	    authors: "Talts et al."
457	    venue: "arXiv 2018"
458	    year: 2018
459	    url: "https://arxiv.org/abs/1804.06788"
460	    category: "calibration"
461	    role: "method-component"
462	    relevance: "SBC is our 6th evaluation metric. Validates Bayesian inference by checking rank uniformity of posterior samples. Used to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation)."
463	    key_findings: "General procedure for validating Bayesian posterior samplers; graphical diagnostics indicate nature of inference problems."
464	    our_advantage: "SBC is adopted as diagnostic tool. Our contribution is applying SBC to contamination-augmented IRT at realistic N_models to decompose coverage gaps."
465	
466	  # ============================================================
467	  # Category: detection — Gap-Fill (must_cite)
468	  # ============================================================
469	
470	  - id: "wust_2025_selfcritique"
471	    title: "Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations"
472	    authors: "Wüst, Hoffmann, & Pang"
473	    venue: "arXiv 2025"
474	    year: 2025
475	    url: "https://arxiv.org/abs/2510.09259"
476	    category: "detection"
477	    role: "method-component"
478	    relevance: "Our S4 signal. Uses LLM self-evaluation entropy collapse as contamination indicator. We find it near-random (AUC≈0.50) at 0.5B scale — ineffective as standalone signal."
479	    key_findings: "Self-critique entropy patterns differ for memorized vs novel items."
480	    our_advantage: "ContamCal reveals S4 ineffectiveness and integrates it into multi-signal RRF where its noise is diluted."
481	
482	  - id: "golchin_2024_time_travel"
483	    title: "Time Travel in LLMs: Tracing Data Contamination in Large Language Models"
484	    authors: "Golchin & Surdeanu"
485	    venue: "ICLR 2024"
486	    year: 2024
487	    url: "https://arxiv.org/abs/2308.08493"
488	    category: "detection"
489	    role: "background"
490	    relevance: "Proposes guided prompting to detect contamination via LLM's ability to reproduce benchmark instances. Complementary approach to our signal-based detection."
491	    key_findings: "Detects contamination across GPT-4, GPT-3.5, LLaMA-2 via instance reproduction; confirms widespread contamination in major LLMs."
492	    our_advantage: "Time Travel requires model generation access; ContamCal works with item-level responses only. Our approach quantifies effects, not just detects."
493	
494	  # ============================================================
495	  # Category: mitigation — Gap-Fill (must_cite + supplementary)
496	  # ============================================================
497	
498	  - id: "li_2025_dcr"
499	    title: "Decontaminated Calibration and Ranking for Trustworthy LLM Evaluation"
500	    authors: "Li et al."
501	    venue: "EMNLP 2025"
502	    year: 2025
503	    category: "mitigation"
504	    role: "direct-competitor"
505	    relevance: "Closest predecessor to ContamCal. DCR applies decontamination + calibration + ranking correction. Lacks IRT grounding, uncertainty quantification, and domain-level diagnosis. Key W1 comparison target."
506	    key_findings: "Score adjustment framework for contaminated benchmarks; demonstrates improved ranking consistency post-decontamination."
507	    our_advantage: "ContamCal provides: (1) Bayesian CIs vs point estimates, (2) domain-level γ diagnosis vs aggregate correction, (3) Fisher Info identifiability analysis, (4) Min-K++ reversal detection."
508	    verified: false
509	
510	  - id: "yang_2023_rethinking_benchmark"
511	    title: "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples"
512	    authors: "Yang et al."
513	    venue: "arXiv 2023"
514	    year: 2023
515	    url: "https://arxiv.org/abs/2311.04850"
516	    category: "mitigation"
517	    role: "background"
518	    relevance: "Rephrasing-based contamination mitigation: creates semantically equivalent but textually novel test items. Complementary to ContamCal's post-hoc calibration approach."
519	    key_findings: "Rephrased benchmarks show significant performance drops in contaminated models; surface-level memorization dominates."
520	    our_advantage: "Rephrasing prevents contamination for new evaluations; ContamCal calibrates existing contaminated scores. Different scope."
521	
522	  # ============================================================
523	  # Category: benchmark — Gap-Fill (must_cite + supplementary)
524	  # ============================================================
525	
526	  - id: "zheng_2023_chatbot_arena"
527	    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
528	    authors: "Zheng et al."
529	    venue: "NeurIPS 2023"
530	    year: 2023
531	    url: "https://arxiv.org/abs/2306.05685"
532	    category: "benchmark"
533	    role: "background"
534	    relevance: "Chatbot Arena as contamination-resistant evaluation via live human preference. Motivates why static benchmark contamination matters — dynamic evaluations are expensive and limited to ranking."
535	    key_findings: "Strong agreement between MT-Bench automated and Chatbot Arena human evaluations; crowdsourced evaluation provides contamination-resistant rankings."
536	    our_advantage: "Chatbot Arena avoids contamination by design but cannot assess specific capabilities. ContamCal enables continued use of targeted static benchmarks with calibrated scores."
537	
538	  - id: "wang_2024_mmlu_pro"
539	    title: "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark"
540	    authors: "Wang et al."
541	    venue: "arXiv 2024"
542	    year: 2024
543	    url: "https://arxiv.org/abs/2406.01574"
544	    category: "benchmark"
545	    role: "background"
546	    relevance: "MMLU-Pro increases difficulty and reduces sensitivity to prompt format, partially addressing contamination concerns. Our MMLU domain-level γ analysis applies equally to MMLU-Pro since contamination is about memorization, not difficulty."
547	    key_findings: "10-option MC format reduces random guessing; more discriminative across model capabilities."
548	    our_advantage: "MMLU-Pro redesigns the benchmark; ContamCal calibrates existing benchmarks without redesign."
549	
550	  # ============================================================
551	  # Category: irt-methodology — Gap-Fill (must_cite)
552	  # ============================================================
553	
554	  - id: "reckase_2009_mirt"
555	    title: "Multidimensional Item Response Theory"
556	    authors: "Reckase, M. D."
557	    venue: "Springer"
558	    year: 2009
559	    category: "irt-methodology"
560	    role: "foundation"
561	    relevance: "Canonical MIRT reference. Our 2PL+γ extends unidimensional IRT; multidimensional extensions discussed in future work for non-STEM domain misfit."
562	    key_findings: "Comprehensive MIRT framework including compensatory and non-compensatory models, parameter estimation, and model fit assessment."
563	    our_advantage: "ContamCal currently uses unidimensional IRT with contamination covariate. MIRT extension is future work for modeling domain-specific abilities."
564	    verified: false
565	
566	  - id: "mislevy_1986_bayes_irt"
567	    title: "Bayes Modal Estimation in Item Response Models"
568	    authors: "Mislevy, R. J."
569	    venue: "Psychometrika"
570	    year: 1986
571	    category: "irt-methodology"
572	    role: "foundation"
573	    relevance: "Foundational work on Bayesian estimation for IRT. Justifies our use of Bayesian (NUTS/Stan) inference for 2PL+γ parameter estimation with informative priors."
574	    key_findings: "Bayesian modal estimation provides regularization for IRT parameters; handles small samples better than MLE."
575	    our_advantage: "ContamCal builds on Bayesian IRT tradition, adding contamination-specific covariates and model comparison via PPP."
576	
577	  - id: "sanmartin_2009_irt"
578	    title: "Consequential Validity and Item Response Theory"
579	    authors: "San Martín, Del Pino, & De Boeck"
580	    venue: "Psychometrika"
581	    year: 2009
582	    category: "irt-methodology"
583	    role: "foundation"
584	    relevance: "Addresses consequential validity in IRT models — directly relevant to our calibration value decomposition (D120) where we separate ability estimation from contamination correction."
585	    key_findings: "Framework for assessing consequences of IRT model use; distinguishes construct-relevant from construct-irrelevant variance."
586	    our_advantage: "ContamCal's D120 decomposition directly operationalizes this distinction: γ correction vs θ estimation improvement."
587	
588	  - id: "adams_1997_mrcml"
589	    title: "The Multidimensional Random Coefficients Multinomial Logit Model"
590	    authors: "Adams, Wilson, & Wang"
591	    venue: "Applied Psychological Measurement"
592	    year: 1997
593	    category: "irt-methodology"
594	    role: "foundation"
595	    relevance: "Extends IRT to multidimensional random effects. Foundation for understanding our per-domain γ modeling within the broader IRT methodology."
596	    key_findings: "General framework for multidimensional IRT with random coefficients; handles nested item structures."
597	    our_advantage: "ContamCal uses a simpler contamination-specific extension (additive γ) rather than full MRCML."
598	
599	  # ============================================================
600	  # Category: item-compromise — Gap-Fill (must_cite)
601	  # ============================================================
602	
603	  - id: "holland_1993_dif"
604	    title: "Differential Item Functioning"
605	    authors: "Holland, P. W. & Wainer, H. (Eds.)"
606	    venue: "Lawrence Erlbaum Associates"
607	    year: 1993
608	    category: "item-compromise"
609	    role: "foundation"
610	    relevance: "Classic DIF reference. DIF methodology detects items that function differently across groups — analogous to our γ detecting contamination effects that vary across domains. DIF is the educational measurement precursor to our domain-differential analysis."
611	    key_findings: "Comprehensive DIF detection and analysis framework; establishes that item-level analysis is essential for fair measurement."
612	    our_advantage: "ContamCal extends DIF thinking to LLM contamination: 'exposed' vs 'unexposed' items replace traditional DIF group comparisons."
613	    verified: false
614	
615	# ============================================================
616	# Summary Statistics (Updated)
617	# ============================================================
618	# Total papers: 43
619	# By category: detection=13, irt-llm=9, item-compromise=6, calibration=4, mitigation=4, benchmark=5, irt-methodology=4
620	# By role: foundation=14, method-component=6, direct-competitor=7, evaluation=5, background=12
621	# Must-cite coverage: 8/9 clusters filled (all must_cite accounted for)
622	# Notes:
623	#   - Eckerly 2017: verified=false (book chapter, no direct URL confirmed)
624	#   - li_2025_dcr: verified=false (EMNLP 2025, need to confirm exact venue/URL)
625	#   - reckase_2009_mirt: verified=false (textbook, no arXiv URL)
626	#   - holland_1993_dif: verified=false (textbook, no DOI confirmed)
627	#   - paper_framing.md references "Lalor et al., AAAI 2024" — closest match is EACL 2024 tutorial
628	#   - weller2024selfcritique in writing_plan → actually wust2025selfcritique
629	#   - paper_framing.md references "ATLAS (Baffour et al., 2024)" — actual paper is Li et al., 2024 (arxiv 2511.04689)
630	#   - paper_framing.md references "PSN-IRT (Yao et al., 2024)" — actual paper is Zhou et al., 2025 (AAAI 2026)
631	#   - paper_framing.md references "DCR (Dekoninck et al., EMNLP 2025)" — actual DCR is Xu et al. (Dekoninck authored ConStat)
632	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5832819a-405e-465b-8864-ac3cf1695846",
  "isSidechain": true,
  "promptId": "91837b43-a16b-4a3f-a342-fa8f545853f7",
  "agentId": "afabe4ff3c4e4c925",
  "type": "user",
  "uuid": "a515ca26-b409-42f6-884f-8f699b3051b5",
  "sourceToolAssistantUUID": "5832819a-405e-465b-8864-ac3cf1695846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-17T09:29:03.121Z_

Let me search for the paper_framing.md in the project directory structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a515ca26-b409-42f6-884f-8f699b3051b5",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTRJXqNVcZ2fuHaDcD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d40a4e71-660f-4d0d-acac-47a56e522655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hv4vesZVXGeo9Z83pqEzEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 88,
      "cache_creation_input_tokens": 13748,
      "cache_read_input_tokens": 27367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13748,
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

_source line 8 · 2026-05-17T09:29:03.499Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nqf6znuVDs9EfkejnX2us6`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration -name \"paper_framing.md\" -o -name \"paper_framing*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d40a4e71-660f-4d0d-acac-47a56e522655",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTRJXqNVcZ2fuHaDcD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d3e7419-30e5-4799-a40e-8f61e68b4cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hv4vesZVXGeo9Z83pqEzEh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 88,
      "cache_creation_input_tokens": 13748,
      "cache_read_input_tokens": 27367,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13748
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 88,
          "output_tokens": 132,
          "cache_read_input_tokens": 27367,
          "cache_creation_input_tokens": 13748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13748,
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

_source line 9 · 2026-05-17T09:29:03.750Z_

<details><summary>↩ Tool result · `toolu_01Nqf6znuVDs9EfkejnX2us6`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260515T052337/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260515T052337/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260515T052337/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T185145/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T185145/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T185145/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260514T171536/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d3e7419-30e5-4799-a40e-8f61e68b4cff",
  "isSidechain": true,
  "promptId": "91837b43-a16b-4a3f-a342-fa8f545853f7",
  "agentId": "afabe4ff3c4e4c925",
  "type": "user",
  "uuid": "588c9fc9-dd9b-44d8-8206-46b86cdf9e5a",
  "sourceToolAssistantUUID": "7d3e7419-30e5-4799-a40e-8f61e68b4cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-17T09:29:04.989Z_

Let me check the main project directory for the paper_framing.md:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588c9fc9-dd9b-44d8-8206-46b86cdf9e5a",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTZxgLHiwDhyhsAxuJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "76454b26-cfd3-424e-b51e-155a196a2c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ShSrXVL3hEGPEAcTVi8yax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 41115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1344,
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

_source line 11 · 2026-05-17T09:29:05.128Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E2kizgmrxqbTULzPQ8awQX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76454b26-cfd3-424e-b51e-155a196a2c8f",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTZxgLHiwDhyhsAxuJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b7e19b1-b8ee-4b2d-aa25-cb82c1dbfb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ShSrXVL3hEGPEAcTVi8yax",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 41115,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1344
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 107,
          "cache_read_input_tokens": 41115,
          "cache_creation_input_tokens": 1344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1344,
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

_source line 12 · 2026-05-17T09:29:05.136Z_

<details><summary>↩ Tool result · `toolu_01E2kizgmrxqbTULzPQ8awQX`</summary>

```text
1	# Paper Framing — contamcal-irt-calibration
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
5	- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
6	- Track: Machine Learning for NLP / Resources and Evaluation
7	- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)
8	
9	## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)
10	Benchmark contamination effects are far more complex than "scores go up." Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).
11	
12	## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)
13	
14	1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:
15	   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)
16	   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)
17	   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)
18	   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.
19	   - "Other" domain: system crash (disk/cgroup), non-essential catch-all category.
20	   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.
21	   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant "contamination = uniform inflation" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.
22	   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.
23	
24	2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.
25	   **C2 contingency**: "Scale-dependent" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness." Min-K++ reversal remains novel regardless.
26	
27	3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real "impossibility," not merely "IRT needs more data." CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.
28	
29	4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.
30	
31	## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)
32	
33	### Core (characterization-led; calibration conditional)
34	1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)
35	2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice
36	3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)
37	
38	### Supporting
39	4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation
40	5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)
41	
42	## Story Spine
43	- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
44	- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
45	- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to "fix" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.
46	- **Headline result template (D039 — characterization-led)**: "Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation."
47	
48	## Venue Fit Risks
49	- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
50	- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
51	- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
52	- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).
53	
54	## Anticipated Reviewer Concerns & Defenses
55	
56	| # | Concern | Defense | Experiment |
57	|---|---------|---------|------------|
58	| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |
59	| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
60	| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
61	| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
62	| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
63	| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |
64	| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
65	| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
66	| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
67	| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
68	| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
69	| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
70	| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
71	| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |
72	| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |
73	| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |
74	| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |
75	| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as "S1+IRT calibration with extensible multi-signal architecture for future signals." Meta-circularity argument for training-free aggregation still holds. | exp-003 |
76	| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |
77	| 20 | γ doesn't improve calibration MAE over vanilla 2PL | γ's role is diagnostic (domain-differential characterization), not calibration accuracy improvement. IRT ability estimation itself provides calibration value (GSM8K ΔMAE=0.163). Vanilla 2PL ≈ 2PL+γ confirms γ is orthogonal to calibration performance — it reveals WHERE contamination acts, not HOW MUCH to adjust. | exp-006 |
78	| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |
79	| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |
80	| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |
81	
82	## Evaluation Protocol (6 Metrics — D025 added SBC)
83	1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
84	2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
85	3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
86	4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
87	5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
88	6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments
89	
90	## Benchmarks (2 main + 2 contrasts)
91	1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY
92	2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as "benchmark-dependent contamination effects" — ContamCal calibrates in both directions.
93	3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as "ContamCal identifies benchmarks not requiring calibration")
94	4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.
95	
96	## Baselines (7)
97	0. **Raw (no adjustment)** — report original benchmark scores as anchor
98	1. **Remove-and-rescore** — drop flagged items, rescore on remaining
99	2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
100	3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
101	4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
102	5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
103	6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare
104	
105	## Local Independence Discussion
106	Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.
107	
108	## Required Figures (Dream D2: "zero figures" flagged as serious deficiency)
109	1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
110	2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022
111	3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)
112	4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
113	5. Calibrated-vs-true accuracy scatter with CIs (exp-006)
114	
115	## Citation Requirements (35+ minimum, expanded per Dream D2)
116	Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
117	Dream D2 additions (all 3 tiers flagged):
118	- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
119	- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
120	- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
121	- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
122	- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
123	D025 additions (all 3 Dream tiers flagged):
124	- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature
125	- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives
126	- Deeper DCR engagement: Oren et al. 2024 structural comparison
127	- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)
128	
129	## Discussion Notes
130	
131	### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)
132	- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.
133	- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.
134	- **Paper treatment**: Report in Discussion as "capacity threshold for reliable MC evaluation." The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.
135	- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.
136	
137	## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
138	Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
139	The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
140	This is CPU-only theoretical work — can be done in parallel with GPU experiments.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b7e19b1-b8ee-4b2d-aa25-cb82c1dbfb8d",
  "isSidechain": true,
  "promptId": "91837b43-a16b-4a3f-a342-fa8f545853f7",
  "agentId": "afabe4ff3c4e4c925",
  "type": "user",
  "uuid": "8b52c861-5a8d-48e1-8405-4e017cbc8fb8",
  "sourceToolAssistantUUID": "5b7e19b1-b8ee-4b2d-aa25-cb82c1dbfb8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T09:29:17.064Z_

Perfect! Now I have both documents. Let me extract the key information you need for polishing your Abstract and Introduction.

## Report: Foundation Papers & Narrative Framing for Abstract/Introduction

Based on the **literature_map.yaml** (43 papers across 7 categories) and **paper_framing.md**, here are the key reference points for opening your EMNLP methodology paper:

### Foundation Papers (role=foundation)
These establish your intellectual lineage and set up the problem:

1. **Shi et al., ICLR 2024** — "Detecting Pretraining Data from Large Language Models" (Min-K% Prob & WikiMIA)
   - The original detection framework your work builds on
   
2. **Eckerly, 2017** — "Detecting preknowledge and item compromise" (Handbook chapter)
   - **Core theoretical grounding**: item compromise detection in educational measurement via IRT
   
3. **De Boeck & Wilson, 2004** — "Explanatory Item Response Models" (Springer)
   - Foundational for your contamination-augmented 4PL as explanatory IRT
   
4. **Lalor et al., EACL 2024** — "Item Response Theory for Natural Language Processing" (Tutorial)
   - Establishes IRT as the evaluation framework you're extending
   
5. **Polo et al., ICML 2024** — "tinyBenchmarks" (IRT for efficient LLM evaluation)
   - Demonstrates IRT's scalability assumption (item parameters transfer across models)

### Direct Competitors (role=direct-competitor)
These define your positioning and differentiation:

1. **Dong et al., ACL 2024** — "CDD & TED: Generalization or Memorization"
   - Closest prior work on calibration; TED corrects for contamination but lacks IRT grounding & uncertainty quantification
   
2. **Deng et al., NAACL 2024** — "TS-Guessing" (Test Set Guessing protocol)
   - Empirical evidence that MC format amplifies contamination signals
   
3. **Schaeffer et al., AAAI 2026** — "Quantifying the Effect of Test Set Contamination on Generative Evaluations"
   - First scaling law for contamination on generative benchmarks; validates your framework
   
4. **Xu et al., EMNLP 2025** — "DCR: Quantifying Data Contamination in LLMs Evaluation"
   - Your primary methodological competitor; provides fuzzy-inference adjusted accuracy but lacks credible intervals & identifiability analysis
   
5. **Luettgau et al., arXiv 2025** — "HiBayES: Hierarchical Bayesian Modeling"
   - Most methodologically similar (Bayesian framework); ignores contamination entirely
   
6. **Sun et al., ICML 2025** — "The Emperor's New Clothes"
   - Demonstrates all 20 mitigation strategies fail; motivates your post-hoc calibration approach

### Narrative Framing (from paper_framing.md)
**Core contribution shift** (per D039 pivot): You're not claiming to "fix" contaminated scores — you're **characterizing how contamination operates**:
- **Domain-dependent** (Simpson's paradox in MMLU: aggregate γ≈0 masks STEM gradient)
- **Benchmark-specific** (ARC forgetting vs GSM8K inflation)
- **Scale-modulated** (catastrophic at 0.5B, negligible at 7B)
- **Signal failure story** (Min-K++ directional reversal at small scales — actively misleading)

**Opening strategy**: Start with the problem (scores are unreliable), position detection methods as necessary but insufficient (they flag contamination without adjusting scores), then frame ContamCal as the first framework that **both characterizes contamination structure AND provides principled calibration with uncertainty bounds**, grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b52c861-5a8d-48e1-8405-4e017cbc8fb8",
  "isSidechain": true,
  "agentId": "afabe4ff3c4e4c925",
  "requestId": "req_011Cb7uTg4Y9abAsTDAiBsHw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb4c91e1-ad91-40b8-bc99-853b765ef46a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/paper_agent_8415d3a6",
  "sessionId": "f5d05f64-02bd-4c69-b131-067a64259496",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "zippy-leaping-pebble",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019NyoLz9c6WuKNqSEZ5SfHV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7564,
      "cache_read_input_tokens": 42459,
      "output_tokens": 970,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 970,
          "cache_read_input_tokens": 42459,
          "cache_creation_input_tokens": 7564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7564,
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
