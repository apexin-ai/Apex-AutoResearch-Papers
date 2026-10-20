# Research conversation: Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations: 1. /home/ubuntu/.agent-ml

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a98d970ec9e66bf2e.jsonl`
- **Structured JSON:** [`6da123f0630f9aa3d2b5.json`](../../sessions/6d/6da123f0630f9aa3d2b5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-14T03:06:10.747Z_

Search for experiment_plan.yaml in the project contamcal-irt-calibration. Try these locations:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml
3. Glob for **/experiment_plan.yaml under /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/

If found, read the full file and report its complete contents. I need to see all experiment definitions, their priorities, dependencies, and which claims they support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "84f1430a-2700-4c92-98d9-897a25c45b73",
  "agentId": "a98d970ec9e66bf2e",
  "type": "user",
  "uuid": "93af2009-dd1e-4150-ac97-d7332ae40614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T03:06:12.005Z_

I'll search for the experiment_plan.yaml file in the specified locations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93af2009-dd1e-4150-ac97-d7332ae40614",
  "isSidechain": true,
  "agentId": "a98d970ec9e66bf2e",
  "requestId": "req_011Cb1iqPJnffJijhYcZi8Dh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c5825b4-8e92-4b14-bea1-eca2139d9f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

_source line 3 · 2026-05-14T03:06:12.253Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Hf1hNZYsLSHoxJ5Qgy2sH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c5825b4-8e92-4b14-bea1-eca2139d9f97",
  "isSidechain": true,
  "agentId": "a98d970ec9e66bf2e",
  "requestId": "req_011Cb1iqPJnffJijhYcZi8Dh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6ad47f5-6d21-48aa-9cb5-183cc9859b78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

### Tool result

_source line 4 · 2026-05-14T03:06:12.293Z_

<details><summary>↩ Tool result · `toolu_013Hf1hNZYsLSHoxJ5Qgy2sH`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: 1
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	    registry_id: exp_001_sft_d100_15B_v2
33	    # Multi-run experiment; related registry entries:
34	    # exp_001_sft_injection, exp_001_sft_0pct_05B (DONE), exp_001_sft_0pct_15B (DONE),
35	    # exp_001_sft_0pct_3B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123,
36	    # exp_001_sft_0pct_3B_s123, exp_001_sft_d100_05B (DONE), exp_001_sft_d005_05B (DONE),
37	    # exp_001_eval_* (various)
38	
39	  - id: exp-002
40	    name: stage1_signal_pipeline
41	    claim: 2
42	    description: >
43	      Compute 4 detection signals on all contaminated + clean models from exp-001:
44	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
45	      (b) Min-K%++ membership inference,
46	      (c) ConStat performance gap (original vs paraphrased items),
47	      (d) Self-Critique entropy collapse.
48	      Output: per-model-item exposure scores for each signal.
49	    priority: P0
50	    gpu_budget_hours: 20
51	    deps: [exp-001]
52	
53	  - id: exp-003
54	    name: rrf_aggregation_ablation
55	    claim: 2
56	    description: >
57	      RRF fusion of 4 signals into composite per-item exposure score.
58	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
59	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
60	      injection robustness check (inject FP at rates matching Duan et al. 2024).
61	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
62	    priority: P0
63	    gpu_budget_hours: 2
64	    deps: [exp-002]
65	
66	  - id: exp-004
67	    name: simulation_identifiability_sweep
68	    claim: 1
69	    also_supports: [3]
70	    description: >
71	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
72	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
73	      model count (20, 50, 100, 200) ×
74	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
75	      exposure type (binary, continuous).
76	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
77	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
78	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
79	      "cannot distinguish no contamination from moderate contamination."
80	      N_items=300 fixed (per MVP finding).
81	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
82	      — prior × N_models dimensions already in sweep grid. Growing Pains
83	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
84	      vs informative prior from pre-estimated item parameters.
85	      Also includes Fisher Information matrix analysis: derive approximate
86	      analytical relationship between signal AUC, N_models, and γ
87	      recoverability. Distinguish structural identifiability (parameters
88	      uniquely determined) from practical identifiability (estimation
89	      quality sufficient for decisions). Provides theoretical grounding
90	      for the empirical AUC ≥ 0.70 threshold.
91	    priority: P0
92	    gpu_budget_hours: 0
93	    deps: []
94	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
95	    registry_id: exp_004_sim_sweep
96	    # Related: mvp_sim_4pl_gamma (DONE/success), mvp_sim_confounding (DONE/success)
97	
98	  - id: exp-005
99	    name: noise_propagation_analysis
100	    claim: 3
101	    description: >
102	      Two parts:
103	      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure
104	      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true
105	      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
106	      This propagates Stage 1 uncertainty into posteriors automatically.
107	      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.
108	      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched
109	      levels, re-fit standard model, measure CI widening for γ and θ.
110	      Both parts inform whether measurement error model closes the coverage gap.
111	    priority: P0
112	    gpu_budget_hours: 0
113	    deps: [exp-002, exp-004]
114	    note: CPU only
115	    registry_id: exp_005_noise_prop_v2
116	    # Related: exp_005_noise_prop (v1, DONE/failed — sigma_e=0 bug)
117	
118	  - id: exp-006
119	    name: irt_calibration_and_baselines
120	    claim: 1
121	    also_supports: [3]
122	    description: >
123	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
124	      PRIMARY: per-benchmark fitting with benchmark-specific γ_k — this is
125	      the natural parameterization when IRT is fitted per-benchmark (each
126	      benchmark's model has its own γ_k). ABLATION: joint fitting across
127	      benchmarks with shared global γ (stronger assumption, tests whether
128	      contamination effect is homogeneous across benchmarks). Report both.
129	      Per-benchmark fitting (not joint) is the default to reduce local
130	      independence violation scope. Posterior predictive checks on item-level residual
131	      correlations to assess local independence empirically.
132	      Compute calibrated scores via exposure=0 counterfactual with CIs.
133	      Compare against 7 baselines:
134	      (0) Raw — no adjustment (anchor),
135	      (1) remove-and-rescore (drop flagged items),
136	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
137	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
138	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
139	      (5) Emperor's mitigation: rephrasing + option shuffling,
140	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
141	          producing adjusted accuracy; must include or reviewers will reject.
142	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
143	      Kendall τ, dose-response monotonicity.
144	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
145	    priority: P0
146	    gpu_budget_hours: 8
147	    deps: [exp-003]
148	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
149	    seeds: 3
150	
151	  # ============================================================
152	  # P1: Important — run if time/GPU permit
153	  # ============================================================
154	
155	  - id: exp-015
156	    name: sft_d100_qc_only
157	    claim: 1
158	    description: >
159	      100% dosage SFT using only QC-pass paraphrases (7547/16697 items).
160	      Isolates noisy vs clean contamination confound identified by reviewer.
161	      D012 decision. Compare calibration metrics against exp-001 d100 (all
162	      paraphrases) to quantify effect of noisy contamination on IRT estimates.
163	    priority: P1
164	    gpu_budget_hours: 5
165	    deps: [exp-001]
166	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
167	    models: [Qwen2.5-0.5B]
168	    seeds: 1
169	    status: planned
170	    registry_id: exp_001_sft_d100_qc_only
171	    data_script: exp001/prepare_qc_only_data.py
172	
173	  - id: exp-007
174	    name: scale_bridging_7b
175	    claim: 1
176	    description: >
177	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
178	      Validates calibration accuracy scales to larger models.
179	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
180	    priority: P1
181	    gpu_budget_hours: 30
182	    deps: [exp-001]
183	
184	  - id: exp-008
185	    name: signal_survival_analysis
186	    claim: 2
187	    description: >
188	      Systematic evaluation of detection signal reliability across training regimes.
189	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
190	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
191	      degrade post-RL (per fragility paper arXiv 2510.02386).
192	      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified
193	      this as the most genuinely novel finding).
194	    priority: P0
195	    gpu_budget_hours: 10
196	    deps: [exp-002]
197	
198	  - id: exp-014
199	    name: multi_family_validation
200	    claim: 1
201	    description: >
202	      Controlled SFT injection on at least one non-Qwen model family
203	      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).
204	      Validates that identifiability boundaries and calibration accuracy
205	      generalize beyond Qwen2.5. Addresses Dream reviewer concern about
206	      single model family limiting generalizability (flagged [M][W]).
207	    priority: P1
208	    gpu_budget_hours: 15
209	    deps: [exp-001]
210	
211	  - id: exp-009
212	    name: rl_observational_case_study
213	    claim: 2
214	    also_supports: [3]
215	    description: >
216	      Apply Self-Critique + available signals to existing RL-trained models:
217	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
218	      Fit IRT with appropriately wider CIs. Expected regret quantification:
219	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
220	      selection. Framed as observational — directional external validity,
221	      not full quantitative validation. Near-zero γ check on known-clean
222	      benchmark (specificity test).
223	    priority: P1
224	    gpu_budget_hours: 15
225	    deps: [exp-006, exp-008]
226	
227	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
228	  # Prior × N_models dimensions already covered in the sweep grid.
229	
230	  # ============================================================
231	  # P2: Bonus — adds breadth if resources allow
232	  # ============================================================
233	
234	  - id: exp-012
235	    name: observational_72b
236	    claim: 1
237	    description: >
238	      Qwen2.5-72B observational analysis (inference only, no SFT).
239	      Extends ecological validity to frontier model scale.
240	    priority: P2
241	    gpu_budget_hours: 15
242	    deps: [exp-006]
243	
244	  - id: exp-013
245	    name: closed_weight_2signal_mode
246	    claim: 2
247	    description: >
248	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
249	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
250	      calibration accuracy gap.
251	    priority: P2
252	    gpu_budget_hours: 5
253	    deps: [exp-003]
254	
255	# ============================================================
256	# GPU Budget Summary
257	# ============================================================
258	gpu_budget:
259	  P0_hours: 90
260	  P1_hours: 60
261	  P2_hours: 20
262	  buffer_hours: 30
263	  total_hours: 200
264	  note: >
265	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
266	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
267	    Requires 2-4× H100/A100-80G for parallel SFT runs.
268	    EMNLP 2026 ARR May 25 sprint (12 days from May 13):
269	    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)
270	    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized
271	    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule
272	
273	# Multi-seed protocol:
274	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
275	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
276	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
277	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6ad47f5-6d21-48aa-9cb5-183cc9859b78",
  "isSidechain": true,
  "promptId": "84f1430a-2700-4c92-98d9-897a25c45b73",
  "agentId": "a98d970ec9e66bf2e",
  "type": "user",
  "uuid": "ee6ae1d5-677a-4f64-ae45-502a98a5f520",
  "sourceToolAssistantUUID": "a6ad47f5-6d21-48aa-9cb5-183cc9859b78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T03:06:12.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KzmThguKe1C3UkL62g4Q4E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/knowledge/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee6ae1d5-677a-4f64-ae45-502a98a5f520",
  "isSidechain": true,
  "agentId": "a98d970ec9e66bf2e",
  "requestId": "req_011Cb1iqPJnffJijhYcZi8Dh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7fd0bff1-5a19-40c7-a983-9f0e6dde4c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19283,
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

### Tool result

_source line 6 · 2026-05-14T03:06:12.696Z_

<details><summary>↩ Tool result · reported error · `toolu_01KzmThguKe1C3UkL62g4Q4E`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fd0bff1-5a19-40c7-a983-9f0e6dde4c4d",
  "isSidechain": true,
  "promptId": "84f1430a-2700-4c92-98d9-897a25c45b73",
  "agentId": "a98d970ec9e66bf2e",
  "type": "user",
  "uuid": "ae0060dc-b367-4a67-9bb0-919ad2026c58",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.",
  "sourceToolAssistantUUID": "7fd0bff1-5a19-40c7-a983-9f0e6dde4c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T03:06:12.817Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JyYTsZcPXgcMX956buq1Jf`</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "pattern": "**/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae0060dc-b367-4a67-9bb0-919ad2026c58",
  "isSidechain": true,
  "agentId": "a98d970ec9e66bf2e",
  "requestId": "req_011Cb1iqPJnffJijhYcZi8Dh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2136241-0011-419c-9c77-3e5dbb2cdaf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011nANMCro3weDPgn8nH8P7Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19283,
      "cache_read_input_tokens": 0,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19283,
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

_source line 8 · 2026-05-14T03:06:12.971Z_

<details><summary>↩ Tool result · `toolu_01JyYTsZcPXgcMX956buq1Jf`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2136241-0011-419c-9c77-3e5dbb2cdaf6",
  "isSidechain": true,
  "promptId": "84f1430a-2700-4c92-98d9-897a25c45b73",
  "agentId": "a98d970ec9e66bf2e",
  "type": "user",
  "uuid": "be10e567-eb28-4777-9dd3-dcffbcd7f6dc",
  "sourceToolAssistantUUID": "d2136241-0011-419c-9c77-3e5dbb2cdaf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T03:06:31.369Z_

Perfect! I found the file. Here is the complete contents of the experiment_plan.yaml file:

## Summary

The **experiment_plan.yaml** file defines the complete experimental roadmap for the ContamCal IRT Calibration project. It contains 13 experiments organized by priority level, with clear mappings to core claims in the paper.

## Experiment Definitions by Priority

### P0: Core Experiments (Must Complete)
Must-run experiments required for submission:

1. **exp-001: controlled_sft_injection** (→ Claim 1)
   - SFT contamination injection on 3 Qwen2.5 models (0.5B/1.5B/3B) at 5 dosage levels (0%, 5%, 25%, 50%, 100%)
   - 15 SFT runs total, 3 seeds each for statistics
   - 50 GPU hours, uses strong LLM paraphrasing with high semantic similarity (>0.85 cosine) and low lexical overlap (BLEU <0.3)
   - Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval

2. **exp-002: stage1_signal_pipeline** (→ Claim 2, deps: exp-001)
   - Compute 4 detection signals: embedding-based semantic retrieval, Min-K%++, ConStat, Self-Critique entropy
   - Produces per-model-item exposure scores
   - 20 GPU hours

3. **exp-003: rrf_aggregation_ablation** (→ Claim 2, deps: exp-002)
   - RRF fusion of 4 signals with ablations: RRF vs equal-weight, single-signal only, calibration-based variants
   - Tests degraded 2-signal mode (ConStat + Self-Critique) for closed-weight
   - 2 GPU hours

4. **exp-004: simulation_identifiability_sweep** (→ Claim 1, also supports Claim 3)
   - Synthetic data sweep: AUC (0.55-0.90) × model count (20-200) × prior strength × exposure type
   - 144 conditions, 10 seeds each
   - CPU only, establishes minimum AUC threshold (≥0.70 recommended)
   - Includes Fisher Information analysis for theoretical grounding
   - Subsumes prior exp-010 and exp-011

5. **exp-005: noise_propagation_analysis** (→ Claim 3, deps: exp-002, exp-004)
   - Measurement error model: treat exposure as noisy observation
   - Two parts: primary measurement model + post-hoc noise injection
   - CPU only, compares coverage vs point-estimate baseline

6. **exp-006: irt_calibration_and_baselines** (→ Claim 1, also supports Claim 3, deps: exp-003)
   - Fit 4PL+γ IRT with per-benchmark γ_k (primary) and joint global γ (ablation)
   - Compare against 7 baselines (raw, remove-rescore, 2PL, vanilla 4PL, linear regression, Emperor's, DCR fuzzy)
   - Evaluate 5 metrics: MAE, coverage (50%/80%/95%), sharpness, Kendall τ, monotonicity
   - 8 GPU hours, 3 seeds matched to exp-001

8. **exp-008: signal_survival_analysis** (→ Claim 2, deps: exp-002)
   - 4 signals × 4 training regimes heatmap (base, SFT-clean, SFT-contaminated, RL-post-trained)
   - Validates Self-Critique reliability across regimes
   - 10 GPU hours, elevated to core contribution

### P1: Important (Run if Time/GPU Permit)

7. **exp-007: scale_bridging_7b** (→ Claim 1, deps: exp-001)
   - Qwen2.5-7B SFT injection at 5 dosages, validates scaling to larger models
   - 30 GPU hours

9. **exp-009: rl_observational_case_study** (→ Claim 2, also supports Claim 3, deps: exp-006, exp-008)
   - Apply Self-Critique + signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1)
   - Observational frame for external validity
   - 15 GPU hours

14. **exp-014: multi_family_validation** (→ Claim 1, deps: exp-001)
   - SFT injection on non-Qwen model (Llama-3.2-1B or Pythia-1.4B) at 3 dosages
   - Validates generalizability across model families
   - 15 GPU hours

15. **exp-015: sft_d100_qc_only** (→ Claim 1, deps: exp-001)
   - 100% dosage using only QC-pass paraphrases (7547/16697 items)
   - Isolates noisy vs clean contamination confound
   - 5 GPU hours, 1 seed on Qwen2.5-0.5B

### P2: Bonus (Resource Permitting)

12. **exp-012: observational_72b** (→ Claim 1, deps: exp-006)
   - Qwen2.5-72B observational analysis (inference only)
   - 15 GPU hours

13. **exp-013: closed_weight_2signal_mode** (→ Claim 2, deps: exp-003)
   - Degraded 2-signal mode for closed-weight models
   - 5 GPU hours

## GPU Budget Summary
- P0: 90 hours
- P1: 60 hours
- P2: 20 hours
- Buffer: 30 hours
- **Total: 200 hours**

Timeline note: EMNLP 2026 ARR May 25 sprint (12 days from May 13):
- With 4× H100: P0 in ~4 days, P1 in ~3 days (fits deadline)
- With 2× H100: P0 in ~7 days, P1 in ~4 days (tight but feasible)

## Dependencies Graph
- exp-001 (SFT injection) → foundation
- exp-002 (signals) depends on exp-001
- exp-003 (RRF) depends on exp-002
- exp-006 (IRT calibration) depends on exp-003
- exp-004 (simulation) is independent
- exp-005 (noise) depends on exp-002 and exp-004
- exp-008, exp-009, exp-014, exp-015 depend on exp-001/002/003
- exp-007, exp-009, exp-012 form a secondary tier

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be10e567-eb28-4777-9dd3-dcffbcd7f6dc",
  "isSidechain": true,
  "agentId": "a98d970ec9e66bf2e",
  "requestId": "req_011Cb1iqYtFSdchksRH8hRPf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31272b17-f57a-4983-a739-1058e5b47159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "db3cbd2f-05b2-4fca-84f4-22e20f10b90f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017uhPRkrHam8w2JubTFBrEK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5658,
      "cache_read_input_tokens": 19283,
      "output_tokens": 1693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1693,
          "cache_read_input_tokens": 19283,
          "cache_creation_input_tokens": 5658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5658,
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
