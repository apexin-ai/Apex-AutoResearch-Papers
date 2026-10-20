# Research conversation: Find and read the literature_map.yaml file in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5e9cd0794a11f600.jsonl`
- **Structured JSON:** [`69f2404734914dcd6db3.json`](../../sessions/69/69f2404734914dcd6db3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-19T19:02:55.116Z_

Find and read the literature_map.yaml file in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/. Also find the add_to_literature_map function - search for it in /home/ubuntu/agent-ml-research/ and /home/ubuntu/.agent-ml-research-idea_gen_0509_2/. Report the full path to literature_map.yaml, its current contents (especially any existing "Linear Recurrent Models" cluster), and the exact import path and signature for add_to_literature_map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e6b9f9c-391a-42e2-a12a-c7c861397b6a",
  "agentId": "a5e9cd0794a11f600",
  "type": "user",
  "uuid": "3221305f-fe28-436c-b334-3022e75e8cad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T19:02:56.826Z_

I'll help you find and analyze the literature_map.yaml file and locate the add_to_literature_map function. Let me search for these.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3221305f-fe28-436c-b334-3022e75e8cad",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqV7iCdbXqxif8jmHU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7e8f33b-a20e-400e-92a5-f8bba5acc288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJQHc5u59FCVgK67udEbiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27753,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27753,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 3 · 2026-05-19T19:02:57.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_017jPnTVH7MST5XNyuBaLLSB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7e8f33b-a20e-400e-92a5-f8bba5acc288",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqV7iCdbXqxif8jmHU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0dd79e9-724d-4af2-b204-91e00a19fd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJQHc5u59FCVgK67udEbiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27753,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27753,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-19T19:02:57.161Z_

<details><summary>↩ Tool result · `toolu_017jPnTVH7MST5XNyuBaLLSB`</summary>

```text
1	# Literature Map for entrainment_gated_ft
2	# Populated via WebSearch verification (S2 API unavailable 2026-05-19)
3	
4	clusters:
5	  - cluster_name: "Hybrid Architectures"
6	    target_count: 7
7	    papers:
8	      - bibtex_key: wang2025hybrid
9	        title: "Scaling Laws for Hybrid Language Models"
10	        authors: "Wang, Junxiong and others"
11	        year: 2025
12	        venue: "arXiv:2507.06457"
13	        category: "Hybrid Architectures"
14	        verified: true
15	        doi: ""
16	        url: "https://arxiv.org/abs/2507.06457"
17	        relevance: "Primary data source — 72-model zoo of hybrid recurrent-attention architectures"
18	      - bibtex_key: lieber2024jamba
19	        title: "Jamba: A Hybrid Transformer-Mamba Language Model"
20	        authors: "Lieber, Opher and others"
21	        year: 2024
22	        venue: "arXiv:2403.19887"
23	        category: "Hybrid Architectures"
24	        verified: true
25	        doi: ""
26	        url: "https://arxiv.org/abs/2403.19887"
27	        relevance: "First production-scale hybrid interleaving Transformer and Mamba layers with MoE; key design reference for attention-ratio choices"
28	      - bibtex_key: peng2024eagle
29	        title: "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence"
30	        authors: "Peng, Bo and others"
31	        year: 2024
32	        venue: "arXiv:2404.05892"
33	        category: "Hybrid Architectures"
34	        verified: true
35	        doi: ""
36	        url: "https://arxiv.org/abs/2404.05892"
37	        relevance: "RWKV-5/6 with matrix-valued states and dynamic recurrence; pure-recurrent baseline in the hybrid architecture spectrum"
38	      - bibtex_key: de2024griffin
39	        title: "Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models"
40	        authors: "De, Soham and others"
41	        year: 2024
42	        venue: "arXiv:2402.19427"
43	        category: "Hybrid Architectures"
44	        verified: true
45	        doi: ""
46	        url: "https://arxiv.org/abs/2402.19427"
47	        relevance: "Proposes Hawk (pure RNN) and Griffin (gated linear recurrence + local attention); matches Llama-2 with 6x fewer tokens"
48	      - bibtex_key: dao2024mamba2
49	        title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
50	        authors: "Dao, Tri and Gu, Albert"
51	        year: 2024
52	        venue: "ICML 2024"
53	        category: "Hybrid Architectures"
54	        verified: true
55	        doi: ""
56	        url: "https://arxiv.org/abs/2405.21060"
57	        relevance: "Establishes SSD framework unifying SSMs and attention; Mamba-2 core layer used in many hybrid designs"
58	      - bibtex_key: botev2024recurrentgemma
59	        title: "RecurrentGemma: Moving Past Transformers for Efficient Open Language Models"
60	        authors: "Botev, Aleksandar and others"
61	        year: 2024
62	        venue: "arXiv:2404.07839"
63	        category: "Hybrid Architectures"
64	        verified: true
65	        doi: ""
66	        url: "https://arxiv.org/abs/2404.07839"
67	        relevance: "Open-weight Griffin-based model combining linear recurrence with local sliding-window attention; directly comparable to hybrid zoo models"
68	      - bibtex_key: dong2024hymba
69	        title: "Hymba: A Hybrid-head Architecture for Small Language Models"
70	        authors: "Dong, Xin and others"
71	        year: 2024
72	        venue: "arXiv:2411.13676"
73	        category: "Hybrid Architectures"
74	        verified: true
75	        doi: ""
76	        url: "https://arxiv.org/abs/2411.13676"
77	        relevance: "Intra-layer head-wise hybrid mixing attention and SSM heads; contrasts with inter-layer hybrid designs like Jamba/Griffin"
78	
79	  - cluster_name: "Linear Recurrent Models"
80	    target_count: 6
81	    papers:
82	      - bibtex_key: gu2024mamba
83	        title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
84	        authors: "Gu, Albert and Dao, Tri"
85	        year: 2024
86	        venue: "arXiv:2312.00752"
87	        category: "Linear Recurrent Models"
88	        verified: true
89	        doi: ""
90	        url: "https://arxiv.org/abs/2312.00752"
91	        relevance: "Selective SSM foundation — Mamba architecture; base for Mamba-2 and many hybrid designs in our study"
92	      - bibtex_key: sun2023retnet
93	        title: "Retentive Network: A Successor to Transformer for Large Language Models"
94	        authors: "Sun, Yutao and Dong, Li and Huang, Shaohan and Ma, Shuming and Xia, Yuqing and Xue, Jilong and Wang, Jianyong and Wei, Furu"
95	        year: 2023
96	        venue: "arXiv:2307.08621"
97	        category: "Linear Recurrent Models"
98	        verified: true
99	        doi: ""
100	        url: "https://arxiv.org/abs/2307.08621"
101	        relevance: "RetNet — one of three base architectures in our study; retention mechanism with parallel/recurrent/chunkwise paradigms"
102	      - bibtex_key: qin2024hgrn2
103	        title: "HGRN2: Gated Linear RNNs with State Expansion"
104	        authors: "Qin, Zhen and others"
105	        year: 2024
106	        venue: "arXiv:2404.07904"
107	        category: "Linear Recurrent Models"
108	        verified: true
109	        doi: ""
110	        url: "https://arxiv.org/abs/2404.07904"
111	        relevance: "HGRN2 — one of three base architectures in our study; outer-product state expansion for gated linear RNNs"
112	      - bibtex_key: yang2024gateddeltanet
113	        title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
114	        authors: "Yang, Songlin and Kautz, Jan and Hatamizadeh, Ali"
115	        year: 2024
116	        venue: "arXiv:2412.06464"
117	        category: "Linear Recurrent Models"
118	        verified: true
119	        doi: ""
120	        url: "https://arxiv.org/abs/2412.06464"
121	        relevance: "GatedDeltaNet — one of three base architectures in our study; combines gating with delta update rule"
122	      - bibtex_key: gu2022s4
123	        title: "Efficiently Modeling Long Sequences with Structured State Spaces"
124	        authors: "Gu, Albert and Goel, Karan and Ré, Christopher"
125	        year: 2022
126	        venue: "ICLR 2022"
127	        category: "Linear Recurrent Models"
128	        verified: true
129	        doi: ""
130	        url: "https://arxiv.org/abs/2111.00396"
131	        relevance: "S4 — foundational structured state space model; established SSM paradigm that led to Mamba and subsequent architectures"
132	      - bibtex_key: katharopoulos2020transformers
133	        title: "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention"
134	        authors: "Katharopoulos, Angelos and Vyas, Apoorv and Pappas, Nikolaos and Fleuret, François"
135	        year: 2020
136	        venue: "ICML 2020"
137	        category: "Linear Recurrent Models"
138	        verified: true
139	        doi: ""
140	        url: "https://arxiv.org/abs/2006.16236"
141	        relevance: "Linear attention as RNN — establishes theoretical bridge between attention and recurrence; foundational for gated linear attention variants"
142	
143	  - cluster_name: "Underspecification and Model Agreement"
144	    target_count: 5
145	    papers:
146	      - bibtex_key: damour2022underspecification
147	        title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
148	        authors: "D'Amour, Alexander and Heller, Katherine and Moldovan, Dan and others"
149	        year: 2022
150	        venue: "JMLR"
151	        category: "Underspecification and Model Agreement"
152	        verified: true
153	        doi: ""
154	        url: ""
155	        relevance: "Framing anchor — defines underspecification; our finding is a specific instance"
156	      - bibtex_key: mccoy2020berts
157	        title: "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance"
158	        authors: "McCoy, R. Thomas and Min, Junghyun and Linzen, Tal"
159	        year: 2020
160	        venue: "NeurIPS 2020"
161	        category: "Underspecification and Model Agreement"
162	        verified: true
163	        doi: ""
164	        url: "https://arxiv.org/abs/1911.02969"
165	        relevance: "Per-example divergence in fine-tuned BERTs — direct precedent for our finding that similar aggregate performance masks per-example disagreement"
166	      - bibtex_key: fort2019deep
167	        title: "Deep Ensembles: A Loss Landscape Perspective"
168	        authors: "Fort, Stanislav and Hu, Huiyi and Lakshminarayanan, Balaji"
169	        year: 2019
170	        venue: "arXiv:1912.02757"
171	        category: "Underspecification and Model Agreement"
172	        verified: true
173	        doi: ""
174	        url: "https://arxiv.org/abs/1912.02757"
175	        relevance: "Loss landscape analysis showing diverse solutions in weight space; supports our observation that architectures find different per-example solutions"
176	      - bibtex_key: kornblith2019similarity
177	        title: "Similarity of Neural Network Representations Revisited"
178	        authors: "Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey"
179	        year: 2019
180	        venue: "ICML 2019"
181	        category: "Underspecification and Model Agreement"
182	        verified: true
183	        doi: ""
184	        url: "https://arxiv.org/abs/1905.00414"
185	        relevance: "CKA — centered kernel alignment for measuring representational similarity; methodological context for cross-architecture comparison"
186	      - bibtex_key: koh2021wilds
187	        title: "WILDS: A Benchmark for In-the-Wild Distribution Shift"
188	        authors: "Koh, Pang Wei and Sagawa, Shiori and Marklund, Henrik and others"
189	        year: 2021
190	        venue: "ICML 2021"
191	        category: "Underspecification and Model Agreement"
192	        verified: true
193	        doi: ""
194	        url: "https://arxiv.org/abs/2012.07421"
195	        relevance: "Benchmark for distribution shift; complements underspecification framework by providing empirical evidence of model disagreement under shift"
196	
197	  - cluster_name: "Ensemble Diversity"
198	    target_count: 3
199	    papers:
200	      - bibtex_key: krogh1994ensembles
201	        title: "Neural Network Ensembles, Cross Validation, and Active Learning"
202	        authors: "Krogh, Anders and Vedelsby, Jesper"
203	        year: 1994
204	        venue: "NeurIPS 1994"
205	        category: "Ensemble Diversity"
206	        verified: true
207	        doi: ""
208	        url: ""
209	        relevance: "Foundational ensemble diversity-accuracy decomposition; ambiguity = variance of ensemble members; our Jaccard metric measures analogous per-example disagreement"
210	      - bibtex_key: kuncheva2003measures
211	        title: "Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy"
212	        authors: "Kuncheva, Ludmila I. and Whitaker, Christopher J."
213	        year: 2003
214	        venue: "Machine Learning"
215	        category: "Ensemble Diversity"
216	        verified: true
217	        doi: ""
218	        url: ""
219	        relevance: "Systematic evaluation of 10 diversity measures for classifier ensembles; Jaccard-like pairwise measures directly relevant to our per-example analysis"
220	      - bibtex_key: lakshminarayanan2017simple
221	        title: "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
222	        authors: "Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles"
223	        year: 2017
224	        venue: "NeurIPS 2017"
225	        category: "Ensemble Diversity"
226	        verified: true
227	        doi: ""
228	        url: "https://arxiv.org/abs/1612.01474"
229	        relevance: "Deep ensemble methodology; random initialization suffices for diversity — parallels our observation that different architectures produce diverse per-example behaviors"
230	
231	  - cluster_name: "Dataset Cartography and Per-Example Analysis"
232	    target_count: 4
233	    papers:
234	      - bibtex_key: swayamdipta2020dataset
235	        title: "Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics"
236	        authors: "Swayamdipta, Swabha and Schwartz, Roy and Lourie, Nicholas and Wang, Yizhong and Hajishirzi, Hannaneh and Smith, Noah A. and Choi, Yejin"
237	        year: 2020
238	        venue: "EMNLP 2020"
239	        category: "Dataset Cartography and Per-Example Analysis"
240	        verified: true
241	        doi: ""
242	        url: "https://arxiv.org/abs/2009.10795"
243	        relevance: "Per-example characterization via training dynamics (confidence, variability); our helped/hurt decomposition is analogous per-example analysis across architectures rather than epochs"
244	      - bibtex_key: rodriguez2021evaluation
245	        title: "Evaluation Examples are Not Equally Informative: How Should That Change NLP Leaderboards?"
246	        authors: "Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan"
247	        year: 2021
248	        venue: "ACL 2021"
249	        category: "Dataset Cartography and Per-Example Analysis"
250	        verified: true
251	        doi: ""
252	        url: "https://aclanthology.org/2021.acl-long.346"
253	        relevance: "IRT-based per-example difficulty modeling for NLP; demonstrates that evaluation examples have latent properties — our helped/hurt analysis reveals similar per-example structure"
254	      - bibtex_key: ethayarajh2022understanding
255	        title: "Understanding Dataset Difficulty with V-Usable Information"
256	        authors: "Ethayarajh, Kawin and Choi, Yejin and Swayamdipta, Swabha"
257	        year: 2022
258	        venue: "ICML 2022"
259	        category: "Dataset Cartography and Per-Example Analysis"
260	        verified: true
261	        doi: ""
262	        url: "https://arxiv.org/abs/2110.08420"
263	        relevance: "V-usable information framework for per-example difficulty; extends dataset cartography to information-theoretic characterization"
264	      - bibtex_key: pleiss2020identifying
265	        title: "Identifying Mislabeled Data using the Area Under the Margin Ranking"
266	        authors: "Pleiss, Geoff and Zhang, Tianyi and Elenberg, Ethan and Weinberger, Kilian Q."
267	        year: 2020
268	        venue: "NeurIPS 2020"
269	        category: "Dataset Cartography and Per-Example Analysis"
270	        verified: true
271	        doi: ""
272	        url: "https://arxiv.org/abs/2001.10528"
273	        relevance: "Per-example margin ranking for data quality; complementary per-example analysis method to our helped/hurt decomposition"
274	
275	  - cluster_name: "Attention Interpretability"
276	    target_count: 4
277	    papers:
278	      - bibtex_key: jain2019attention
279	        title: "Attention is not Explanation"
280	        authors: "Jain, Sarthak and Wallace, Byron C."
281	        year: 2019
282	        venue: "NAACL 2019"
283	        category: "Attention Interpretability"
284	        verified: true
285	        doi: ""
286	        url: "https://arxiv.org/abs/1902.10186"
287	        relevance: "Caution against interpreting attention as explanation; relevant to our attention weight analysis which we frame as descriptive characterization, not causal"
288	      - bibtex_key: clark2019what
289	        title: "What Does BERT Look At? An Analysis of BERT's Attention"
290	        authors: "Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D."
291	        year: 2019
292	        venue: "BlackboxNLP Workshop, ACL 2019"
293	        category: "Attention Interpretability"
294	        verified: true
295	        doi: ""
296	        url: "https://arxiv.org/abs/1906.04341"
297	        relevance: "Descriptive attention pattern analysis in BERT; methodological precedent for our cross-architecture attention cosine similarity analysis"
298	      - bibtex_key: olsson2022induction
299	        title: "In-context Learning and Induction Heads"
300	        authors: "Olsson, Catherine and Elhage, Nelson and Nanda, Neel and others"
301	        year: 2022
302	        venue: "arXiv:2209.11895"
303	        category: "Attention Interpretability"
304	        verified: true
305	        doi: ""
306	        url: "https://arxiv.org/abs/2209.11895"
307	        relevance: "Induction heads as mechanistic circuit for in-context learning; relevant to understanding what hybrid attention layers learn"
308	      - bibtex_key: wiegreffe2019attention
309	        title: "Attention is not not Explanation"
310	        authors: "Wiegreffe, Sarah and Pinter, Yuval"
311	        year: 2019
312	        venue: "EMNLP 2019"
313	        category: "Attention Interpretability"
314	        verified: true
315	        doi: ""
316	        url: "https://arxiv.org/abs/1908.04626"
317	        relevance: "Response to Jain & Wallace showing attention can provide useful signal under certain conditions; contextualizes our cautious descriptive framing"
318	
319	  - cluster_name: "Benchmarks and Evaluation"
320	    target_count: 3
321	    papers:
322	      - bibtex_key: paperno2016lambada
323	        title: "The LAMBADA Dataset: Word Prediction Requiring a Broad Discourse Context"
324	        authors: "Paperno, Denis and Kruszewski, Germán and Lazaridou, Angeliki and others"
325	        year: 2016
326	        venue: "ACL 2016"
327	        category: "Benchmarks and Evaluation"
328	        verified: true
329	        doi: ""
330	        url: ""
331	        relevance: "Primary benchmark — LAMBADA is the sole convergence benchmark in our study"
332	      - bibtex_key: gao2024lmeval
333	        title: "A Framework for Few-Shot Language Model Evaluation"
334	        authors: "Gao, Leo and Tow, Jonathan and Abbasi, Baber and Biderman, Stella and others"
335	        year: 2024
336	        venue: "Zenodo (v0.4.3)"
337	        category: "Benchmarks and Evaluation"
338	        verified: true
339	        doi: "10.5281/zenodo.12608602"
340	        url: "https://github.com/EleutherAI/lm-evaluation-harness"
341	        relevance: "lm-evaluation-harness — evaluation framework used by Wang et al. (2025) model zoo and our benchmark evaluations"
342	      - bibtex_key: clark2018arc
343	        title: "Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge"
344	        authors: "Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind"
345	        year: 2018
346	        venue: "arXiv:1803.05457"
347	        category: "Benchmarks and Evaluation"
348	        verified: true
349	        doi: ""
350	        url: "https://arxiv.org/abs/1803.05457"
351	        relevance: "ARC benchmark — ARC-Easy and ARC-Challenge are two of our 10 evaluation benchmarks"
352	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0dd79e9-724d-4af2-b204-91e00a19fd6d",
  "isSidechain": true,
  "promptId": "1e6b9f9c-391a-42e2-a12a-c7c861397b6a",
  "agentId": "a5e9cd0794a11f600",
  "type": "user",
  "uuid": "c54ce7dc-1129-4979-b228-784e7c695c5a",
  "sourceToolAssistantUUID": "b0dd79e9-724d-4af2-b204-91e00a19fd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T19:02:57.256Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016okBqbxpHykEm3dhRVrWHD`</summary>

```json
{
  "pattern": "def add_to_literature_map",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c54ce7dc-1129-4979-b228-784e7c695c5a",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqV7iCdbXqxif8jmHU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe44b9bc-de18-4904-b932-fbb2a0f3eac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJQHc5u59FCVgK67udEbiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27753,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27753,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 6 · 2026-05-19T19:02:57.468Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0199ZmqJ6aHwUFDGKbxMtaVT`</summary>

```json
{
  "pattern": "def add_to_literature_map",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe44b9bc-de18-4904-b932-fbb2a0f3eac5",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqV7iCdbXqxif8jmHU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98e6721c-fcc9-4cc9-a5d9-e14df03ccc51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJQHc5u59FCVgK67udEbiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27753,
      "cache_read_input_tokens": 0,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27753
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 266,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27753,
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

_source line 7 · 2026-05-19T19:02:58.130Z_

<details><summary>↩ Tool result · `toolu_016okBqbxpHykEm3dhRVrWHD`</summary>

```text
Found 1 file
/home/ubuntu/agent-ml-research/core/tools/literature.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe44b9bc-de18-4904-b932-fbb2a0f3eac5",
  "isSidechain": true,
  "promptId": "1e6b9f9c-391a-42e2-a12a-c7c861397b6a",
  "agentId": "a5e9cd0794a11f600",
  "type": "user",
  "uuid": "06c64b48-ba40-4206-b780-2cd80c670bfa",
  "sourceToolAssistantUUID": "fe44b9bc-de18-4904-b932-fbb2a0f3eac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T19:03:01.726Z_

<details><summary>↩ Tool result · `toolu_0199ZmqJ6aHwUFDGKbxMtaVT`</summary>

```text
Found 2 files
logs/workers/worker_paper_research_lit_cluster_2_linear_recurrent_20260519T184333.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/logs/chats/feishu_group_oc_16f4cc04d259f364091fe7b4addd7912_paper_agent.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98e6721c-fcc9-4cc9-a5d9-e14df03ccc51",
  "isSidechain": true,
  "promptId": "1e6b9f9c-391a-42e2-a12a-c7c861397b6a",
  "agentId": "a5e9cd0794a11f600",
  "type": "user",
  "uuid": "6242e278-d793-4236-a006-22936eda6cce",
  "sourceToolAssistantUUID": "98e6721c-fcc9-4cc9-a5d9-e14df03ccc51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T19:03:03.821Z_

Great! Now let me read the literature.py file to get the exact function signature and imports:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6242e278-d793-4236-a006-22936eda6cce",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqyLr1xtX95gfLYgZE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "191d9b50-3103-402f-9b32-8831cdd51d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WQzwKHxnRfnN1SLN7SNhkC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7357,
      "cache_read_input_tokens": 27753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7357,
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

_source line 10 · 2026-05-19T19:03:04.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EFFZK96BAUdecQdnWVxdBM`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/literature.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191d9b50-3103-402f-9b32-8831cdd51d5f",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSqyLr1xtX95gfLYgZE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a3d7e7bb-55ee-4989-a0bd-2e8f791656e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WQzwKHxnRfnN1SLN7SNhkC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7357,
      "cache_read_input_tokens": 27753,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7357
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 91,
          "cache_read_input_tokens": 27753,
          "cache_creation_input_tokens": 7357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7357,
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

_source line 11 · 2026-05-19T19:03:04.262Z_

<details><summary>↩ Tool result · `toolu_01EFFZK96BAUdecQdnWVxdBM`</summary>

```text
1	"""Literature map — persistent, cross-stage knowledge base of papers.
2	
3	The literature_map.yaml is the single source of truth for papers a project
4	accumulates across the Idea → Research → Writing → Review pipeline. Each
5	entry is verified (or marked unverified) and carries enough metadata to
6	generate BibTeX entries and to drive Related Work / citation gap-fill in
7	the Paper Agent's writing pipeline.
8	
9	Two scopes:
10	
11	  - Project-level: ``projects/{project}/literature_map.yaml``
12	      Used during Research and Writing phases.
13	
14	  - Global (Idea phase): ``{WORKSPACE_ROOT}/literature_map.yaml``
15	      Used before a project exists. Each entry carries ``source_idea_id`` so
16	      multiple ideas can coexist. On project creation, matching entries are
17	      seeded into the project map.
18	
19	Design notes:
20	
21	  - Read paths support modes (summary / category:X / competitors / unverified
22	    / bib / full) so day-to-day reads stay token-cheap even when the map has
23	    grown to 40-60 papers.
24	
25	  - Writes hold an exclusive flock + use atomic temp→rename, modeled on
26	    ``core/tools/registry.py`` so the file never tears under concurrent
27	    Worker writes.
28	
29	  - Dedup happens on add: DOI exact match wins; otherwise normalized title
30	    match. Existing entries are merged (new fields fill empty existing
31	    fields) rather than overwritten.
32	"""
33	
34	from __future__ import annotations
35	
36	import fcntl
37	import logging
38	import os
39	import re
40	import tempfile
41	import unicodedata
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import paths as _paths
48	from core.tools.result import ToolResult
49	
50	logger = logging.getLogger(__name__)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Constants
55	# ---------------------------------------------------------------------------
56	
57	# Roles a paper can play relative to the project. Used by Related Work drafting
58	# (foundation papers anchor narratives; direct-competitor papers must be cited).
59	VALID_ROLES: frozenset[str] = frozenset(
60	    {"foundation", "direct-competitor", "method-component", "evaluation", "background"}
61	)
62	
63	# Modes for read_literature_map — keep token usage proportional to need.
64	VALID_READ_MODES: frozenset[str] = frozenset(
65	    {"summary", "competitors", "unverified", "bib", "full"}
66	)
67	
68	# Fields kept in summary mode (skips long fields like abstract, relevance).
69	_SUMMARY_FIELDS: tuple[str, ...] = (
70	    "title", "year", "venue", "category", "role", "verified", "bibtex_key",
71	)
72	
73	
74	# ---------------------------------------------------------------------------
75	# Path resolution
76	# ---------------------------------------------------------------------------
77	
78	def get_literature_map_path(project: str | None = None) -> Path:
79	    """Resolve the literature_map.yaml path.
80	
81	    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
82	    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
83	    """
84	    if project:
85	        p = _paths.resolve_project_file(project, "literature_map.yaml")
86	        p.parent.mkdir(parents=True, exist_ok=True)
87	        return p
88	    return _paths.global_literature_map_path()
89	
90	
91	# ---------------------------------------------------------------------------
92	# Atomic file I/O — modeled on registry._read_modify_write_registry
93	# ---------------------------------------------------------------------------
94	
95	def _empty_map() -> dict:
96	    return {
97	        "meta": {"last_updated": None, "total_papers": 0},
98	        "categories": [],
99	        "papers": {},
100	    }
101	
102	
103	def _read_map(path: Path) -> dict:
104	    """Read literature_map.yaml without a lock (atomic single-syscall read).
105	
106	    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
107	    Writers use exclusive flock + atomic rename so readers always see a
108	    consistent snapshot.
109	    """
110	    if not path.exists():
111	        return _empty_map()
112	    try:
113	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
114	    except Exception:
115	        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
116	        return _empty_map()
117	    if isinstance(data, list):
118	        data = {"papers": data, "meta": {}, "categories": []}
119	    elif not isinstance(data, dict):
120	        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
121	        return _empty_map()
122	    data.setdefault("meta", {})
123	    data["meta"].setdefault("last_updated", None)
124	    data["meta"].setdefault("total_papers", 0)
125	    data.setdefault("categories", [])
126	    data.setdefault("papers", {})
127	    return data
128	
129	
130	def _read_modify_write(path: Path, modifier) -> dict:
131	    """Read, apply ``modifier(data)`` in place, atomically write back.
132	
133	    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
134	    swaps the inode and would invalidate locks held on it).
135	    """
136	    path.parent.mkdir(parents=True, exist_ok=True)
137	    lock_path = path.with_suffix(".lock")
138	
139	    with open(lock_path, "a+") as lock_f:
140	        fcntl.flock(lock_f, fcntl.LOCK_EX)
141	        try:
142	            data = _read_map(path)
143	            modifier(data)
144	            data["meta"]["total_papers"] = len(data.get("papers", {}))
145	            data["meta"]["last_updated"] = _paths.now_iso()
146	
147	            fd, tmp_path = tempfile.mkstemp(
148	                dir=str(path.parent), prefix=".literature_", suffix=".tmp"
149	            )
150	            try:
151	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
152	                    yaml.dump(
153	                        data, tmp_f,
154	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
155	                    )
156	                    tmp_f.flush()
157	                    os.fsync(tmp_f.fileno())
158	                os.replace(tmp_path, str(path))
159	            except Exception:
160	                if os.path.exists(tmp_path):
161	                    os.unlink(tmp_path)
162	                raise
163	        finally:
164	            fcntl.flock(lock_f, fcntl.LOCK_UN)
165	
166	    return data
167	
168	
169	# ---------------------------------------------------------------------------
170	# Normalization & dedup
171	# ---------------------------------------------------------------------------
172	
173	_PUNCT_RE = re.compile(r"[^\w\s]")
174	_WS_RE = re.compile(r"\s+")
175	
176	
177	def _normalize_title(title: str) -> str:
178	    """Lowercase, strip diacritics + punctuation, collapse whitespace.
179	
180	    Used for fuzzy dedup when two records describe the same paper with
181	    slightly different titles (smart quotes, hyphens, capitalization).
182	    """
183	    if not title:
184	        return ""
185	    s = unicodedata.normalize("NFKD", title)
186	    s = "".join(c for c in s if not unicodedata.combining(c))
187	    s = s.lower()
188	    s = _PUNCT_RE.sub(" ", s)
189	    s = _WS_RE.sub(" ", s).strip()
190	    return s
191	
192	
193	def _normalize_doi(doi: str) -> str:
194	    """Lowercase DOI, strip common prefixes."""
195	    if not doi:
196	        return ""
197	    s = doi.strip().lower()
198	    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
199	        if s.startswith(prefix):
200	            s = s[len(prefix):]
201	            break
202	    return s.strip()
203	
204	
205	def _slugify(s: str, max_len: int = 24) -> str:
206	    """First-word slug — lowercase, alnum only, truncated."""
207	    s = unicodedata.normalize("NFKD", s or "")
208	    s = "".join(c for c in s if not unicodedata.combining(c))
209	    s = re.sub(r"[^a-zA-Z0-9]+", "", s.split()[0] if s.split() else "")
210	    return s.lower()[:max_len]
211	
212	
213	def _generate_bibtex_key(paper: dict) -> str:
214	    """Generate a bibtex key like ``vaswani2017attention``.
215	
216	    Uses the first author's surname + year + the first significant word of
217	    the title. Falls back to ``paper_{hash}`` if metadata is missing.
218	    """
219	    authors = paper.get("authors") or []
220	    first_author = ""
221	    if authors:
222	        raw = authors[0]
223	        if isinstance(raw, str):
224	            # Could be "Vaswani, A." or "Ashish Vaswani"
225	            if "," in raw:
226	                first_author = raw.split(",", 1)[0].strip()
227	            else:
228	                first_author = raw.strip().split()[-1] if raw.strip() else ""
229	    surname = _slugify(first_author)
230	
231	    year = paper.get("year") or ""
232	    year_part = str(year) if year else ""
233	
234	    title = paper.get("title") or ""
235	    # Skip stop words for the title slug
236	    stop = {"a", "an", "the", "on", "in", "of", "for", "and", "or", "is", "to"}
237	    words = [w for w in re.split(r"\W+", title.lower()) if w and w not in stop]
238	    word = _slugify(words[0]) if words else ""
239	
240	    key = f"{surname}{year_part}{word}"
241	    if not key.strip():
242	        import hashlib
243	        h = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
244	        key = f"paper_{h}"
245	    return key
246	
247	
248	def _find_existing_key(papers: dict, candidate: dict) -> str | None:
249	    """Find a matching paper key in ``papers`` for the candidate dict.
250	
251	    Match order: DOI exact (normalized) → normalized title.
252	    Returns the existing key or None.
253	
254	    bibtex_key collisions are NOT treated as dedup signal — two different
255	    papers can share a naive bibtex_key (e.g. same first author + year), and
256	    we handle that with a suffix at insert time. Real dedup must be content
257	    based.
258	    """
259	    cand_doi = _normalize_doi(candidate.get("doi", ""))
260	    cand_title = _normalize_title(candidate.get("title", ""))
261	
262	    for key, entry in papers.items():
263	        if cand_doi:
264	            entry_doi = _normalize_doi(entry.get("doi", ""))
265	            if entry_doi and entry_doi == cand_doi:
266	                return key
267	        if cand_title:
268	            entry_title = _normalize_title(entry.get("title", ""))
269	            if entry_title and entry_title == cand_title:
270	                return key
271	    return None
272	
273	
274	def _merge_paper(existing: dict, new: dict) -> dict:
275	    """Merge new fields into existing — only fill empty slots, never overwrite.
276	
277	    Verified=True wins over False (a later verification cannot un-verify).
278	    """
279	    merged = dict(existing)
280	    for k, v in new.items():
281	        if v is None or v == "" or v == []:
282	            continue
283	        if k == "verified":
284	            merged["verified"] = bool(existing.get("verified")) or bool(v)
285	            continue
286	        if not merged.get(k):
287	            merged[k] = v
288	    return merged
289	
290	
291	# ---------------------------------------------------------------------------
292	# Public API
293	# ---------------------------------------------------------------------------
294	
295	def read_literature_map(
296	    project: str | None = None,
297	    mode: str = "summary",
298	) -> ToolResult:
299	    """Read the literature map with mode-controlled verbosity.
300	
301	    Args:
302	        project: Project name — None reads the global (idea-phase) map.
303	        mode:
304	          - "summary"        → categories + per-paper {title, year, venue,
305	                                category, role, verified, bibtex_key}
306	          - "category:&lt;key>" → full entries in the named category
307	          - "competitors"    → full entries with role=direct-competitor
308	          - "unverified"     → full entries with verified=False
309	          - "bib"            → list of bibtex_key strings (for citation lookups)
310	          - "full"           → everything (use sparingly — token-heavy)
311	
312	    Returns:
313	        ToolResult.data = {
314	            "categories": [...],
315	            "papers": {key: {...}, ...},
316	            "meta": {"last_updated", "total_papers"},
317	            "mode": &lt;effective mode>,
318	        }
319	    """
320	    path = get_literature_map_path(project)
321	    data = _read_map(path)
322	    papers: dict = data.get("papers", {})
323	    categories: list = data.get("categories", [])
324	
325	    # Category-scoped read: "category:&lt;key>"
326	    if mode.startswith("category:"):
327	        cat_key = mode.split(":", 1)[1].strip()
328	        filtered = {k: v for k, v in papers.items() if v.get("category") == cat_key}
329	        return ToolResult(success=True, data={
330	            "categories": [c for c in categories if c.get("key") == cat_key],
331	            "papers": filtered,
332	            "meta": data.get("meta", {}),
333	            "mode": mode,
334	        })
335	
336	    if mode not in VALID_READ_MODES:
337	        return ToolResult(
338	            success=False,
339	            error=(
340	                f"Unknown mode '{mode}'. Valid: {sorted(VALID_READ_MODES)} "
341	                "or 'category:&lt;key>'."
342	            ),
343	        )
344	
345	    if mode == "summary":
346	        compact = {
347	            k: {f: v.get(f) for f in _SUMMARY_FIELDS if f in v}
348	            for k, v in papers.items()
349	        }
350	        return ToolResult(success=True, data={
351	            "categories": categories,
352	            "papers": compact,
353	            "meta": data.get("meta", {}),
354	            "mode": mode,
355	        })
356	
357	    if mode == "competitors":
358	        filtered = {k: v for k, v in papers.items() if v.get("role") == "direct-competitor"}
359	        return ToolResult(success=True, data={
360	            "categories": categories,
361	            "papers": filtered,
362	            "meta": data.get("meta", {}),
363	            "mode": mode,
364	        })
365	
366	    if mode == "unverified":
367	        filtered = {k: v for k, v in papers.items() if not v.get("verified")}
368	        return ToolResult(success=True, data={
369	            "categories": categories,
370	            "papers": filtered,
371	            "meta": data.get("meta", {}),
372	            "mode": mode,
373	        })
374	
375	    if mode == "bib":
376	        keys = [v.get("bibtex_key") or k for k, v in papers.items()]
377	        return ToolResult(success=True, data={
378	            "bibtex_keys": keys,
379	            "meta": data.get("meta", {}),
380	            "mode": mode,
381	        })
382	
383	    # mode == "full"
384	    return ToolResult(success=True, data={
385	        "categories": categories,
386	        "papers": papers,
387	        "meta": data.get("meta", {}),
388	        "mode": mode,
389	    })
390	
391	
392	def add_to_literature_map(
393	    project: str | None = None,
394	    papers: Iterable[dict] | None = None,
395	    added_by: str = "",
396	) -> ToolResult:
397	    """Add (or merge) one or more papers into the literature map.
398	
399	    Dedup: DOI exact (normalized) → normalized title → bibtex_key collision.
400	    Existing entries are merged field-by-field, never overwritten.
401	
402	    Args:
403	        project: Project name — None writes to the global (idea-phase) map.
404	        papers: Iterable of paper dicts. Recognized fields:
405	                title, authors (list[str]), year, venue, url, doi,
406	                bibtex_key, category, role, relevance, abstract,
407	                semantic_scholar_id, source_idea_id, verified.
408	                Missing bibtex_key is auto-generated.
409	        added_by: Free-form tag for provenance ("paper-research",
410	                  "idea-generator", "user", etc.). Recorded on new entries.
411	
412	    Returns:
413	        ToolResult.data = {
414	            "added": [keys],            # newly inserted
415	            "merged": [keys],           # matched existing, fields merged
416	            "rejected": [{title, reason}],
417	            "total_papers": N,
418	        }
419	    """
420	    if not papers:
421	        return ToolResult(
422	            success=False, error="No papers provided.",
423	        )
424	
425	    paper_list = list(papers)
426	    added: list[str] = []
427	    merged: list[str] = []
428	    rejected: list[dict] = []
429	    now = _paths.now_iso()
430	
431	    def _apply(data: dict) -> None:
432	        existing = data.setdefault("papers", {})
433	        for cand in paper_list:
434	            if not isinstance(cand, dict):
435	                rejected.append({"title": str(cand), "reason": "not a dict"})
436	                continue
437	            title = (cand.get("title") or "").strip()
438	            if not title:
439	                rejected.append({"title": "", "reason": "missing title"})
440	                continue
441	            if cand.get("role") and cand["role"] not in VALID_ROLES:
442	                rejected.append({
443	                    "title": title,
444	                    "reason": f"invalid role '{cand['role']}', valid: {sorted(VALID_ROLES)}",
445	                })
446	                continue
447	
448	            existing_key = _find_existing_key(existing, cand)
449	            if existing_key:
450	                # Merge — fill empty fields, keep verified=True if either is True
451	                existing[existing_key] = _merge_paper(existing[existing_key], cand)
452	                merged.append(existing_key)
453	                continue
454	
455	            # New entry — assign a bibtex_key if missing, dedupe within file
456	            key = cand.get("bibtex_key") or _generate_bibtex_key(cand)
457	            base_key = key
458	            suffix = 1
459	            while key in existing:
460	                suffix += 1
461	                key = f"{base_key}_{suffix}"
462	
463	            entry = {
464	                "title": title,
465	                "authors": cand.get("authors") or [],
466	                "year": cand.get("year"),
467	                "venue": cand.get("venue") or "",
468	                "url": cand.get("url") or "",
469	                "doi": cand.get("doi") or "",
470	                "bibtex_key": key,
471	                "category": cand.get("category") or "",
472	                "role": cand.get("role") or "",
473	                "relevance": cand.get("relevance") or "",
474	                "abstract": cand.get("abstract") or "",
475	                "semantic_scholar_id": cand.get("semantic_scholar_id") or "",
476	                "verified": bool(cand.get("verified", False)),
477	                "added_by": cand.get("added_by") or added_by or "",
478	                "added_at": cand.get("added_at") or now,
479	            }
480	            # Optional source_idea_id (global map only) — keep if present
481	            if cand.get("source_idea_id"):
482	                entry["source_idea_id"] = cand["source_idea_id"]
483	
484	            existing[key] = entry
485	            added.append(key)
486	
487	    data = _read_modify_write(get_literature_map_path(project), _apply)
488	
489	    return ToolResult(success=True, data={
490	        "added": added,
491	        "merged": merged,
492	        "rejected": rejected,
493	        "total_papers": data["meta"]["total_papers"],
494	    })
495	
496	
497	def update_literature_category(
498	    paper_key: str,
499	    project: str | None = None,
500	    category: str | None = None,
501	    role: str | None = None,
502	    relevance: str | None = None,
503	    verified: bool | None = None,
504	) -> ToolResult:
505	    """Update a single paper's classification fields.
506	
507	    Only the fields you pass are changed — others are left intact. This is
508	    the preferred path for "re-classify this paper after reading it" or
509	    "mark verified=true after OpenAlex check" — it's smaller than rewriting
510	    the whole entry via add_to_literature_map.
511	
512	    Args:
513	        paper_key: The YAML key of the paper (e.g. "vaswani2017attention").
514	        project: Project name — None updates the global map.
515	        category: New category key (must match a categories[].key, or empty).
516	        role: New role (must be in VALID_ROLES, or empty to clear).
517	        relevance: One-line relevance description.
518	        verified: Mark verified/unverified (e.g. after OpenAlex check).
519	
520	    Returns:
521	        ToolResult.data = {"paper_key", "updated_fields": {...}}
522	        ToolResult.error if paper_key not found or role/category invalid.
523	    """
524	    if role is not None and role and role not in VALID_ROLES:
525	        return ToolResult(
526	            success=False,
527	            error=f"invalid role '{role}', valid: {sorted(VALID_ROLES)}",
528	        )
529	
530	    updated: dict[str, Any] = {}
531	    not_found = {"miss": False}
532	
533	    def _apply(data: dict) -> None:
534	        papers = data.setdefault("papers", {})
535	        if paper_key not in papers:
536	            not_found["miss"] = True
537	            return
538	        entry = papers[paper_key]
539	        if category is not None:
540	            entry["category"] = category
541	            updated["category"] = category
542	        if role is not None:
543	            entry["role"] = role
544	            updated["role"] = role
545	        if relevance is not None:
546	            entry["relevance"] = relevance
547	            updated["relevance"] = relevance
548	        if verified is not None:
549	            entry["verified"] = bool(verified)
550	            updated["verified"] = bool(verified)
551	
552	    _read_modify_write(get_literature_map_path(project), _apply)
553	
554	    if not_found["miss"]:
555	        return ToolResult(
556	            success=False,
557	            error=f"paper_key '{paper_key}' not found in literature_map",
558	        )
559	    return ToolResult(success=True, data={
560	        "paper_key": paper_key,
561	        "updated_fields": updated,
562	    })
563	
564	
565	def upsert_category(
566	    project: str | None = None,
567	    key: str = "",
568	    name: str = "",
569	    narrative: str = "",
570	) -> ToolResult:
571	    """Add or update a category entry in the categories[] list.
572	
573	    Categories define the Related Work subsection structure. A paper's
574	    ``category`` field references one of these by ``key``.
575	
576	    Args:
577	        project: Project name — None edits the global map.
578	        key: Category slug (e.g. "attention_mechanisms"). Required.
579	        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
580	        narrative: One-line description of the category's narrative arc.
581	
582	    Returns:
583	        ToolResult.data = {"key", "action": "added"|"updated"}.
584	    """
585	    if not key:
586	        return ToolResult(success=False, error="key is required")
587	
588	    state = {"action": "added"}
589	
590	    def _apply(data: dict) -> None:
591	        cats = data.setdefault("categories", [])
592	        for c in cats:
593	            if c.get("key") == key:
594	                if name:
595	                    c["name"] = name
596	                if narrative:
597	                    c["narrative"] = narrative
598	                state["action"] = "updated"
599	                return
600	        cats.append({"key": key, "name": name or key, "narrative": narrative})
601	
602	    _read_modify_write(get_literature_map_path(project), _apply)
603	    return ToolResult(success=True, data={"key": key, "action": state["action"]})
604	
605	
606	def seed_literature_map(
607	    project: str,
608	    seed_papers: Iterable[dict],
609	    source_idea_id: str = "",
610	) -> ToolResult:
611	    """Bulk-seed a new project's literature_map from an idea's accumulated papers.
612	
613	    Called by the idea→project bootstrap hook. Each seed paper is added with
614	    ``added_by="idea_generator"`` so downstream consumers can distinguish
615	    seed papers from those discovered during research.
616	
617	    Args:
618	        project: Project name (required — seeding without a project is the
619	                 global map case, handled by add_to_literature_map directly).
620	        seed_papers: Iterable of paper dicts (same schema as add_to_literature_map).
621	        source_idea_id: Idea ID these papers came from. Stamped on entries so
622	                        a future "re-seed from idea" can find them.
623	
624	    Returns:
625	        Same shape as add_to_literature_map.
626	    """
627	    if not project:
628	        return ToolResult(success=False, error="project is required for seed_literature_map")
629	
630	    seeds = []
631	    for p in seed_papers:
632	        if not isinstance(p, dict):
633	            continue
634	        p2 = dict(p)
635	        if source_idea_id:
636	            p2.setdefault("source_idea_id", source_idea_id)
637	        seeds.append(p2)
638	
639	    return add_to_literature_map(
640	        project=project, papers=seeds, added_by="idea_generator",
641	    )
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3d7e7bb-55ee-4989-a0bd-2e8f791656e7",
  "isSidechain": true,
  "promptId": "1e6b9f9c-391a-42e2-a12a-c7c861397b6a",
  "agentId": "a5e9cd0794a11f600",
  "type": "user",
  "uuid": "35b8e6e2-d050-4978-a831-6028e2e4c340",
  "sourceToolAssistantUUID": "a3d7e7bb-55ee-4989-a0bd-2e8f791656e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T19:03:12.843Z_

Perfect! I have all the information you requested. Here's my comprehensive report:

## Summary

**Full path to literature_map.yaml:**
```
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml
```

## Current Contents of literature_map.yaml

The file contains 6 major clusters with a total of 33 papers. Here's the "Linear Recurrent Models" cluster specifically:

**Linear Recurrent Models cluster** (target_count: 6 papers):
1. **gu2024mamba** - "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (2024)
2. **sun2023retnet** - "Retentive Network: A Successor to Transformer for Large Language Models" (2023)
3. **qin2024hgrn2** - "HGRN2: Gated Linear RNNs with State Expansion" (2024)
4. **yang2024gateddeltanet** - "Gated Delta Networks: Improving Mamba2 with Delta Rule" (2024)
5. **gu2022s4** - "Efficiently Modeling Long Sequences with Structured State Spaces" (2022)
6. **katharopoulos2020transformers** - "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention" (2020)

All other clusters in the file are:
- Hybrid Architectures (7 papers)
- Underspecification and Model Agreement (5 papers)
- Ensemble Diversity (3 papers)
- Dataset Cartography and Per-Example Analysis (4 papers)
- Attention Interpretability (4 papers)
- Benchmarks and Evaluation (3 papers)

## add_to_literature_map Function Details

**Import path:**
```
from core.tools.literature import add_to_literature_map
```

**Function signature:**
```python
def add_to_literature_map(
    project: str | None = None,
    papers: Iterable[dict] | None = None,
    added_by: str = "",
) -> ToolResult:
```

**Key parameters:**
- `project`: Project name (None for global/idea-phase map)
- `papers`: Iterable of paper dicts with recognized fields: title, authors (list[str]), year, venue, url, doi, bibtex_key, category, role, relevance, abstract, semantic_scholar_id, source_idea_id, verified
- `added_by`: Free-form provenance tag ("paper-research", "idea-generator", "user", etc.)

**Return value:**
Returns `ToolResult` with `.data` containing:
- `"added"`: list of newly inserted paper keys
- `"merged"`: list of keys for papers matched and merged
- `"rejected"`: list of dicts with title and rejection reason
- `"total_papers"`: total count in the map

**Location:** `/home/ubuntu/agent-ml-research/core/tools/literature.py` (lines 392-494)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b8e6e2-d050-4978-a831-6028e2e4c340",
  "isSidechain": true,
  "agentId": "a5e9cd0794a11f600",
  "requestId": "req_011CbCSrAADtMKUidaz3DPTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ead911c8-65d2-418f-9a7d-647f9c76958c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "d1595ce1-31fd-40bf-b819-8ad600c5e518",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015gYKnkmnY7ooR8wqKx4abU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7860,
      "cache_read_input_tokens": 35110,
      "output_tokens": 748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 748,
          "cache_read_input_tokens": 35110,
          "cache_creation_input_tokens": 7860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7860,
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
