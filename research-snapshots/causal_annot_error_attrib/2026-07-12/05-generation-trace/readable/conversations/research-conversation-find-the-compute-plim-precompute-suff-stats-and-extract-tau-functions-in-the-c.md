# Research conversation: Find the `compute_plim`, `precompute_suff_stats`, and `extract_tau` functions in the codebase under /home/ubuntu/.agent-

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6dcd171d346aa1b5.jsonl`
- **Structured JSON:** [`89ed03a44dfef5795191.json`](../../sessions/89/89ed03a44dfef5795191.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-22T11:30:18.216Z_

Find the `compute_plim`, `precompute_suff_stats`, and `extract_tau` functions in the codebase under /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/. These are referenced as `plan_006.compute_plim` etc. in compute_all_tasks.py, which imports from a file called `plan_006_asv_empirical.py`. Find where these functions are defined - they might be in a different location or filename. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "eb62d8d9-9d63-4a06-98c0-aaa1437626d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T11:30:19.535Z_

I'll help you find these functions in the codebase. Let me start by exploring the structure and locating the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb62d8d9-9d63-4a06-98c0-aaa1437626d8",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkP72RjQtv7J86RYzX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ef0d5b3-1437-4d8f-9261-5c3b37baff42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014YMavYRQggQzAuDpkStjqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17884,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17884,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-22T11:30:19.673Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0157DGLbCn4rhDHDNqX38XUu`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ef0d5b3-1437-4d8f-9261-5c3b37baff42",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkP72RjQtv7J86RYzX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88350ea3-b2a7-40b6-9eea-cfc6cd504f12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014YMavYRQggQzAuDpkStjqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17884,
      "cache_read_input_tokens": 0,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17884,
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

_source line 4 · 2026-05-22T11:30:19.928Z_

<details><summary>↩ Tool result · `toolu_0157DGLbCn4rhDHDNqX38XUu`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_010_ppi_empirical_validation.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig1.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig7.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig2.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_diagnostic_plots.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig3.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig4.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_008_binarization_collapse.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/intermediate/case_study_analysis.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_confounding_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/annotate_frontier.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/prepare_data.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/compute_results.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan012_case_study/case_study_analysis.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88350ea3-b2a7-40b6-9eea-cfc6cd504f12",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "02f5eda7-384d-4089-a480-0aedcebd6308",
  "sourceToolAssistantUUID": "88350ea3-b2a7-40b6-9eea-cfc6cd504f12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T11:30:21.144Z_

Now let me look at the compute_all_tasks.py file to understand the import structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02f5eda7-384d-4089-a480-0aedcebd6308",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkWHsTJenysTD2WQGH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d086f7a-b020-45bd-a4e3-804a3565b26f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CPXp756EbVRJat74a8vjYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 17884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1817,
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

_source line 6 · 2026-05-22T11:30:21.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vq7auNiQ8ej7wkzGN3KY2h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d086f7a-b020-45bd-a4e3-804a3565b26f",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkWHsTJenysTD2WQGH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e2fd649-d176-485f-9c24-46d860612b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CPXp756EbVRJat74a8vjYX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 17884,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1817
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 111,
          "cache_read_input_tokens": 17884,
          "cache_creation_input_tokens": 1817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1817,
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

_source line 7 · 2026-05-22T11:30:21.677Z_

<details><summary>↩ Tool result · `toolu_01Vq7auNiQ8ej7wkzGN3KY2h`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Three computational tasks for the causal annotation error attribution paper.
4	
5	Task 1: Theory-Empirical MAPE (extend existing humaid-only to all 18 valid configs)
6	Task 2: PPI++ Empirical Validation (simulate gold labels, apply PPI++ correction)
7	Task 3: Dirichlet Subspace Overlay (regenerated with improved styling)
8	
9	Author: auto-generated for paper artifacts
10	"""
11	
12	import json
13	import sys
14	import time
15	import numpy as np
16	from pathlib import Path
17	from collections import defaultdict
18	
19	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
20	sys.path.insert(0, str(PROJ))
21	
22	# Import the plan_006 module for DGP generators matching the paper's setup
23	import importlib.util
24	spec = importlib.util.spec_from_file_location(
25	    "plan_006",
26	    str(PROJ / "plan_006_asv_empirical.py")
27	)
28	plan_006 = importlib.util.module_from_spec(spec)
29	spec.loader.exec_module(plan_006)
30	
31	from annot_sensitivity.correction import correct_ppi, correct_naive_plugin, correct_mla
32	from annot_sensitivity.utils import misclassify
33	
34	# ============================================================================
35	# Common data loading
36	# ============================================================================
37	
38	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
39	              'mbias', 'iv', 'frontdoor']
40	HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}
41	
42	
43	def load_all_data():
44	    """Load confusion matrices and bias records for all 18 valid configs."""
45	    # Load humaid confusion matrices (full 10x10)
46	    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
47	        plan006 = json.load(f)
48	    humaid_cms = {k: np.array(v) for k, v in plan006["confusion_matrices"].items()}
49	    bias_records = plan006["biases"]
50	
51	    # Load filter info
52	    with open(PROJ / "artifacts/plan006_full_filtered_stats.json") as f:
53	        filter_data = json.load(f)
54	    zero_configs = set(filter_data["zero_configs"])
55	
56	    # Valid humaid configs (8 of 9, excluding qwen3_few-shot-5)
57	    humaid_valid = {k: humaid_cms[k] for k in humaid_cms if k not in zero_configs}
58	
59	    # Build bias lookup for humaid
60	    bias_lookup = {}
61	    for b in bias_records:
62	        ck = f"{b['dataset']}_{b['model']}_{b['prompt']}"
63	        if ck not in zero_configs and b.get('bias') is not None:
64	            bias_lookup[(ck, b['topology'])] = b
65	
66	    # VAST confusion matrices: we only have per-class recall (diagonal).
67	    # For VAST we need to construct approximate confusion matrices from the
68	    # diagonal data. The VAST per-class recall gives us C_kk for each class.
69	    # We distribute off-diagonal mass uniformly (best available approximation).
70	    vast_per_class_recall = filter_data["filtered_stats"]["vast_per_class_recall"]
71	    vast_cms = {}
72	    for key, diag in vast_per_class_recall.items():
73	        # key format: "vast_llama4_zero-shot"
74	        config_key = key  # already has "vast_" prefix
75	        K = 3
76	        C = np.zeros((K, K))
77	        for i in range(K):
78	            C[i, i] = diag[i]
79	            off_diag_mass = 1.0 - diag[i]
80	            for j in range(K):
81	                if j != i:
82	                    C[j, i] = off_diag_mass / (K - 1)
83	        vast_cms[config_key] = C
84	
85	    # CivilComments: we have trace/macro_recall from filtered_stats
86	    # For K=2, trace = C[0,0] + C[1,1], macro_recall = trace/2
87	    # We use the CC diagonal values from gen_fig7.py (extracted from the pipeline)
88	    civil_diag = {
89	        "civil_comments_qwen2.5-7b_zero-shot":  [0.7481536189069424, 0.684931506849315],
90	        "civil_comments_qwen2.5-7b_few-shot-3": [0.6787296898079763, 0.7808219178082192],
91	        "civil_comments_qwen2.5-7b_few-shot-5": [0.7370753323485968, 0.7602739726027398],
92	    }
93	    civil_cms = {}
94	    for key, diag in civil_diag.items():
95	        K = 2
96	        C = np.zeros((K, K))
97	        C[0, 0] = diag[0]
98	        C[1, 1] = diag[1]
99	        C[1, 0] = 1.0 - diag[0]
100	        C[0, 1] = 1.0 - diag[1]
101	        civil_cms[key] = C
102	
103	    # Merge all confusion matrices
104	    all_cms = {}
105	    all_cms.update(humaid_valid)
106	    all_cms.update(vast_cms)
107	    all_cms.update(civil_cms)
108	
109	    # Config metadata
110	    config_meta = {}
111	    for k, C in all_cms.items():
112	        parts = k.split("_", 1)
113	        dataset = parts[0]
114	        if dataset == "civil":
115	            dataset = "civil_comments"
116	            model_prompt = k[len("civil_comments_"):]
117	        elif dataset == "vast":
118	            model_prompt = k[len("vast_"):]
119	        else:
120	            model_prompt = k[len("humaid_"):]
121	        K = C.shape[0]
122	        config_meta[k] = {
123	            "dataset": dataset,
124	            "model_prompt": model_prompt,
125	            "K": K,
126	            "min_diag": float(np.min(np.diag(C))),
127	            "trace": float(np.trace(C)),
128	            "macro_recall": float(np.trace(C) / K),
129	        }
130	
131	    return all_cms, config_meta, bias_lookup, filter_data
132	
133	
134	# ============================================================================
135	# Task 1: Theory-Empirical MAPE
136	# ============================================================================
137	
138	def task1_mape(all_cms, config_meta, bias_lookup):
139	    """Compute MAPE between analytical plim bias and finite-sample MC bias."""
140	    print("=" * 80)
141	    print("TASK 1: Theory-Empirical MAPE")
142	    print("=" * 80)
143	    t0 = time.time()
144	
145	    N_MC = 200
146	    N_SAMPLES = 10_000
147	
148	    # Precompute sufficient stats and tau_true for each K
149	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
150	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
151	    suff_stats = {}
152	    tau_true_cache = {}
153	
154	    for K in Ks_used:
155	        for topo in TOPOLOGIES:
156	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
157	            suff_stats[(K, topo)] = st
158	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
159	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
160	            print(f"  K={K:>2} {topo:<12} tau_true={tau_true_cache[(K, topo)]:.6f}")
161	
162	    per_config = {}
163	    per_topology = defaultdict(list)
164	    grand_records = []
165	
166	    for config_key, C in sorted(all_cms.items()):
167	        meta = config_meta[config_key]
168	        K = meta["K"]
169	        params = params_by_K[K]
170	        per_config[config_key] = {}
171	        print(f"\n[{config_key}] K={K}, min_diag={meta['min_diag']:.4f}")
172	
173	        for topo in TOPOLOGIES:
174	            tau_true = tau_true_cache[(K, topo)]
175	            st = suff_stats[(K, topo)]
176	
177	            # Compute analytical plim (theory bias)
178	            plim_C = plan_006.compute_plim(C, st, K)
179	            tau_biased = plan_006.extract_tau(plim_C, topo)
180	            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
181	                continue
182	            theory_bias = tau_biased - tau_true
183	
184	            # MC empirical bias
185	            tau_hats = []
186	            for mc_i in range(N_MC):
187	                seed = (hash(config_key + topo) & 0xFFFFFFFF) + mc_i * 7919
188	                try:
189	                    rng = np.random.default_rng(seed)
190	                    first_var, Y, A = plan_006.GEN_FNS[topo](K, N_SAMPLES,
191	                                                              params[topo], rng)
192	                    A_star = plan_006.generate_Astar(A, C, rng)
193	
194	                    if topo == 'iv':
195	                        Z = first_var
196	                        W, _ = plan_006.wald_estimator(Z, Y, A_star, k=1)
197	                        if np.isfinite(W):
198	                            tau_hats.append(float(W))
199	                    elif topo == 'exposure':
200	                        beta, _ = plan_006.ols_no_T(Y, A_star, K)
201	                        if len(beta) > 1 and np.isfinite(beta[1]):
202	                            tau_hats.append(float(beta[1]))
203	                    else:
204	                        T = first_var
205	                        beta, _ = plan_006.ols_with_dummies(Y, T, A_star, K)
206	                        if np.isfinite(beta[1]):
207	                            tau_hats.append(float(beta[1]))
208	                except Exception:
209	                    continue
210	
211	            if len(tau_hats) < N_MC // 2:
212	                print(f"  {topo:<12} MC FAILED ({len(tau_hats)}/{N_MC})")
213	                continue
214	
215	            tau_mean = float(np.mean(tau_hats))
216	            tau_se = float(np.std(tau_hats, ddof=1) / np.sqrt(len(tau_hats)))
217	            mc_bias = tau_mean - tau_true
218	
219	            if abs(theory_bias) > 1e-12:
220	                ape = abs(theory_bias - mc_bias) / abs(theory_bias)
221	            else:
222	                ape = float('nan')
223	
224	            entry = {
225	                'theory_bias': float(theory_bias),
226	                'mc_bias': float(mc_bias),
227	                'mc_tau_mean': tau_mean,
228	                'mc_tau_se': tau_se,
229	                'tau_true': float(tau_true),
230	                'tau_biased_plim': float(tau_biased),
231	                'abs_pct_error': float(ape) if np.isfinite(ape) else None,
232	                'n_mc_used': len(tau_hats),
233	            }
234	            per_config[config_key][topo] = entry
235	            if np.isfinite(ape):
236	                per_topology[topo].append(ape)
237	                grand_records.append(ape)
238	            print(f"  {topo:<12} theory={theory_bias:+.5f}  MC={mc_bias:+.5f}  "
239	                  f"APE={ape:.3%}")
240	
241	    # Aggregate
242	    per_topology_summary = {}
243	    for topo in TOPOLOGIES:
244	        apes = per_topology.get(topo, [])
245	        finite = [a for a in apes if np.isfinite(a)]
246	        per_topology_summary[topo] = {
247	            'mape': float(np.mean(finite)) if finite else None,
248	            'median_ape': float(np.median(finite)) if finite else None,
249	            'max_ape': float(np.max(finite)) if finite else None,
250	            'n': len(finite),
251	        }
252	
253	    grand_mape = float(np.mean(grand_records)) if grand_records else None
254	
255	    output = {
256	        'meta': {
257	            'n_mc': N_MC,
258	            'n_samples': N_SAMPLES,
259	            'scope': f'All {len(all_cms)} valid configs (K=2,3,10)',
260	            'n_valid_configs': len(all_cms),
261	            'n_scenarios_total': len(grand_records),
262	            'topologies': TOPOLOGIES,
263	            'note': (
264	                'VAST and CivilComments use approximate confusion matrices '
265	                '(diagonal from per-class recall, off-diagonal uniform). '
266	                'HumAID uses full empirical confusion matrices.'
267	            ),
268	        },
269	        'grand_mape': grand_mape,
270	        'per_topology': per_topology_summary,
271	        'per_config': per_config,
272	    }
273	
274	    out_path = PROJ / "artifacts/theory_empirical_mape.json"
275	    out_path.write_text(json.dumps(output, indent=2))
276	    print(f"\n=== Task 1 DONE in {time.time()-t0:.1f}s ===")
277	    print(f"Grand MAPE: {grand_mape:.4%}" if grand_mape else "Grand MAPE: N/A")
278	    print(f"Written: {out_path}")
279	
280	    # LaTeX snippet
281	    latex = r"""% Theory-Empirical MAPE (auto-generated)
282	% Grand MAPE across """ + f"{len(grand_records)} scenarios: {grand_mape:.2%}" + r"""
283	\begin{table}[h]\centering\small
284	\caption{Theory vs.\ MC MAPE per topology}
285	\begin{tabular}{lrrr}
286	\toprule
287	Topology & MAPE (\%) & Median APE (\%) & $n$ \\
288	\midrule
289	"""
290	    for topo in TOPOLOGIES:
291	        s = per_topology_summary[topo]
292	        if s['mape'] is not None:
293	            latex += f"{topo} & {100*s['mape']:.2f} & {100*s['median_ape']:.2f} & {s['n']} \\\\\n"
294	    latex += r"""\midrule
295	Grand & """ + f"{100*grand_mape:.2f}" + r""" & -- & """ + f"{len(grand_records)}" + r""" \\
296	\bottomrule
297	\end{tabular}
298	\end{table}
299	"""
300	    latex_path = PROJ / "artifacts/theory_empirical_mape_table.tex"
301	    latex_path.write_text(latex)
302	    print(f"LaTeX: {latex_path}")
303	
304	    return output
305	
306	
307	# ============================================================================
308	# Task 2: PPI++ Empirical Validation
309	# ============================================================================
310	
311	def task2_ppi(all_cms, config_meta):
312	    """PPI++ empirical validation on all configs x topologies."""
313	    print("\n" + "=" * 80)
314	    print("TASK 2: PPI++ Empirical Validation")
315	    print("=" * 80)
316	    t0 = time.time()
317	
318	    N_SAMPLES = 10_000
319	    N_MC = 50  # fewer MC reps since PPI++ itself has internal bootstrap
320	    GOLD_FRACTION = 0.1
321	
322	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
323	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
324	    suff_stats = {}
325	    tau_true_cache = {}
326	
327	    for K in Ks_used:
328	        for topo in TOPOLOGIES:
329	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
330	            suff_stats[(K, topo)] = st
331	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
332	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
333	
334	    results = {}
335	    summary_by_topo = defaultdict(list)
336	    summary_by_K = defaultdict(list)
337	
338	    for config_key, C in sorted(all_cms.items()):
339	        meta = config_meta[config_key]
340	        K = meta["K"]
341	        params = params_by_K[K]
342	        results[config_key] = {}
343	        print(f"\n[{config_key}] K={K}")
344	
345	        for topo in TOPOLOGIES:
346	            tau_true = tau_true_cache[(K, topo)]
347	            st = suff_stats[(K, topo)]
348	
349	            # Skip IV for PPI++ (PPI++ requires OLS, IV uses Wald estimator)
350	            if topo == 'iv':
351	                # For IV, compute theoretical C^{-1} correction effectiveness instead
352	                cond = np.linalg.cond(C)
353	                try:
354	                    C_inv = np.linalg.inv(C)
355	                    # Theoretical: tau_corrected = RF / (C^{-1} C @ FS)[1] = RF / FS[1] = tau_true
356	                    # So C^{-1} correction should theoretically give 100% bias reduction for IV
357	                    # But this is the Wald estimator - C^{-1} on the first stage only
358	                    plim_C = plan_006.compute_plim(C, st, K)
359	                    tau_biased = plan_006.extract_tau(plim_C, topo)
360	                    bias_biased = tau_biased - tau_true
361	                    # C^{-1} correction of first stage: effective C becomes I
362	                    tau_corrected = tau_true  # theoretical perfect correction
363	                    results[config_key][topo] = {
364	                        'method': 'theoretical_Cinv',
365	                        'tau_true': float(tau_true),
366	                        'tau_biased': float(tau_biased),
367	                        'tau_corrected': float(tau_corrected),
368	                        'bias_biased': float(bias_biased),
369	                        'bias_corrected': 0.0,
370	                        'bias_reduction_pct': 100.0 if abs(bias_biased) > 1e-12 else 0.0,
371	                        'cond_C': float(cond),
372	                        'note': 'IV topology: theoretical C^{-1} correction = perfect (by construction)',
373	                    }
374	                    summary_by_topo[topo].append(100.0)
375	                    summary_by_K[K].append(100.0)
376	                except np.linalg.LinAlgError:
377	                    results[config_key][topo] = {'method': 'failed', 'note': 'C not invertible'}
378	                print(f"  {topo:<12} [IV theoretical] bias_reduction=100.0%")
379	                continue
380	
381	            # For non-IV topologies: simulate PPI++ correction
382	            biased_taus = []
383	            ppi_taus = []
384	            naive_plugin_taus = []
385	
386	            for mc_i in range(N_MC):
387	                seed = (hash(config_key + topo + "ppi") & 0xFFFFFFFF) + mc_i * 3571
388	                rng = np.random.default_rng(seed)
389	
390	                try:
391	                    first_var, Y, A = plan_006.GEN_FNS[topo](K, N_SAMPLES,
392	                                                              params[topo], rng)
393	                    A_star = plan_006.generate_Astar(A, C, rng)
394	
395	                    # Build design matrix
396	                    N = len(Y)
397	                    if topo == 'exposure':
398	                        X_other = np.ones((N, 1))
399	                        tau_idx = 1
400	                    else:
401	                        T = first_var
402	                        X_other = np.column_stack([np.ones(N), T])
403	                        tau_idx = 1  # treatment coefficient
404	
405	                    # Gold labels: select GOLD_FRACTION of data
406	                    n_gold = max(int(N * GOLD_FRACTION), 50)
407	                    gold_idx = rng.choice(N, size=n_gold, replace=False)
408	                    gold_mask = np.zeros(N, dtype=bool)
409	                    gold_mask[gold_idx] = True
410	
411	                    # Biased estimate (using A*)
412	                    D_star = np.zeros((N, K - 1))
413	                    for k_idx in range(1, K):
414	                        D_star[:, k_idx - 1] = (A_star == k_idx).astype(float)
415	                    X_biased = np.column_stack([X_other, D_star])
416	                    try:
417	                        beta_biased = np.linalg.lstsq(X_biased, Y, rcond=None)[0]
418	                        biased_taus.append(float(beta_biased[tau_idx]))
419	                    except Exception:
420	                        continue
421	
422	                    # PPI++ correction
423	                    tau_ppi, se_ppi, success = correct_ppi(
424	                        X_other, Y, A_star, A, gold_mask,
425	                        tau_idx=tau_idx, rng=rng
426	                    )
427	                    if success and np.isfinite(tau_ppi):
428	                        ppi_taus.append(float(tau_ppi))
429	
430	                    # Naive plugin (C^{-1}) correction for comparison
431	                    tau_np, se_np, success_np = correct_naive_plugin(
432	                        X_other, Y, A_star, C, tau_idx=tau_idx
433	                    )
434	                    if success_np and np.isfinite(tau_np):
435	                        naive_plugin_taus.append(float(tau_np))
436	
437	                except Exception:
438	                    continue
439	
440	            if len(biased_taus) < N_MC // 4 or len(ppi_taus) < N_MC // 4:
441	                print(f"  {topo:<12} FAILED (biased={len(biased_taus)}, "
442	                      f"ppi={len(ppi_taus)})")
443	                results[config_key][topo] = {
444	                    'method': 'mc_failed',
445	                    'n_biased': len(biased_taus),
446	                    'n_ppi': len(ppi_taus),
447	                }
448	                continue
449	
450	            mean_biased = float(np.mean(biased_taus))
451	            mean_ppi = float(np.mean(ppi_taus))
452	            bias_biased = mean_biased - tau_true
453	            bias_ppi = mean_ppi - tau_true
454	
455	            if abs(bias_biased) > 1e-12:
456	                reduction_pct = 100.0 * (1.0 - abs(bias_ppi) / abs(bias_biased))
457	            else:
458	                reduction_pct = 0.0
459	
460	            # Naive plugin results
461	            mean_naive = float(np.mean(naive_plugin_taus)) if naive_plugin_taus else float('nan')
462	            bias_naive = mean_naive - tau_true if np.isfinite(mean_naive) else float('nan')
463	            if abs(bias_biased) > 1e-12 and np.isfinite(bias_naive):
464	                naive_reduction = 100.0 * (1.0 - abs(bias_naive) / abs(bias_biased))
465	            else:
466	                naive_reduction = float('nan')
467	
468	            entry = {
469	                'method': 'ppi_mc',
470	                'tau_true': float(tau_true),
471	                'tau_biased_mean': mean_biased,
472	                'tau_ppi_mean': mean_ppi,
473	                'tau_naive_mean': mean_naive,
474	                'bias_biased': float(bias_biased),
475	                'bias_ppi': float(bias_ppi),
476	                'bias_naive': float(bias_naive),
477	                'bias_reduction_pct': float(reduction_pct),
478	                'naive_reduction_pct': float(naive_reduction) if np.isfinite(naive_reduction) else None,
479	                'n_mc_biased': len(biased_taus),
480	                'n_mc_ppi': len(ppi_taus),
481	                'n_mc_naive': len(naive_plugin_taus),
482	                'gold_fraction': GOLD_FRACTION,
483	            }
484	            results[config_key][topo] = entry
485	            summary_by_topo[topo].append(reduction_pct)
486	            summary_by_K[K].append(reduction_pct)
487	            print(f"  {topo:<12} bias_biased={bias_biased:+.5f} bias_ppi={bias_ppi:+.5f} "
488	                  f"reduction={reduction_pct:.1f}%")
489	
490	    # Aggregate summaries
491	    topo_summary = {}
492	    for topo in TOPOLOGIES:
493	        vals = summary_by_topo.get(topo, [])
494	        if vals:
495	            topo_summary[topo] = {
496	                'mean_reduction_pct': float(np.mean(vals)),
497	                'median_reduction_pct': float(np.median(vals)),
498	                'min_reduction_pct': float(np.min(vals)),
499	                'max_reduction_pct': float(np.max(vals)),
500	                'n': len(vals),
501	            }
502	
503	    k_summary = {}
504	    for K in sorted(summary_by_K.keys()):
505	        vals = summary_by_K[K]
506	        if vals:
507	            k_summary[str(K)] = {
508	                'mean_reduction_pct': float(np.mean(vals)),
509	                'median_reduction_pct': float(np.median(vals)),
510	                'n': len(vals),
511	            }
512	
513	    all_reductions = []
514	    for topo_vals in summary_by_topo.values():
515	        all_reductions.extend(topo_vals)
516	    grand_mean_reduction = float(np.mean(all_reductions)) if all_reductions else None
517	
518	    output = {
519	        'meta': {
520	            'n_mc': N_MC,
521	            'n_samples': N_SAMPLES,
522	            'gold_fraction': GOLD_FRACTION,
523	            'n_configs': len(all_cms),
524	            'n_topologies': len(TOPOLOGIES),
525	            'correction_methods': ['ppi++', 'naive_plugin (C^{-1})', 'theoretical_Cinv (IV only)'],
526	            'note': (
527	                'PPI++ uses 10% gold labels. For IV topology, theoretical C^{-1} correction '
528	                'is used (100% by construction). Naive plugin shown for comparison. '
529	                'VAST/CC use approximate confusion matrices (diagonal + uniform off-diagonal).'
530	            ),
531	        },
532	        'grand_mean_bias_reduction_pct': grand_mean_reduction,
533	        'per_topology': topo_summary,
534	        'per_K': k_summary,
535	        'per_config': results,
536	    }
537	
538	    out_path = PROJ / "artifacts/ppi_empirical_validation.json"
539	    out_path.write_text(json.dumps(output, indent=2))
540	    print(f"\n=== Task 2 DONE in {time.time()-t0:.1f}s ===")
541	    print(f"Grand mean bias reduction: {grand_mean_reduction:.1f}%"
542	          if grand_mean_reduction else "N/A")
543	    print(f"Written: {out_path}")
544	
545	    # LaTeX snippet
546	    latex = r"""% PPI++ Bias Reduction (auto-generated)
547	\begin{table}[h]\centering\small
548	\caption{PPI++ bias reduction by topology (""" + f"{GOLD_FRACTION:.0%} gold labels" + r""")}
549	\begin{tabular}{lrrrr}
550	\toprule
551	Topology & Mean (\%) & Median (\%) & Min (\%) & $n$ \\
552	\midrule
553	"""
554	    for topo in TOPOLOGIES:
555	        s = topo_summary.get(topo)
556	        if s:
557	            latex += (f"{topo} & {s['mean_reduction_pct']:.1f} & "
558	                      f"{s['median_reduction_pct']:.1f} & "
559	                      f"{s['min_reduction_pct']:.1f} & {s['n']} \\\\\n")
560	    latex += r"""\midrule
561	Grand & """ + f"{grand_mean_reduction:.1f}" + r""" & -- & -- & """ + f"{len(all_reductions)}" + r""" \\
562	\bottomrule
563	\end{tabular}
564	\end{table}
565	"""
566	    latex_path = PROJ / "artifacts/ppi_empirical_validation_table.tex"
567	    latex_path.write_text(latex)
568	    print(f"LaTeX: {latex_path}")
569	
570	    return output
571	
572	
573	# ============================================================================
574	# Task 3: Dirichlet Subspace Overlay Visualization
575	# ============================================================================
576	
577	def task3_dirichlet_overlay(all_cms, config_meta):
578	    """Create fig7 with improved styling and all 18 configs."""
579	    print("\n" + "=" * 80)
580	    print("TASK 3: Dirichlet Subspace Overlay Visualization")
581	    print("=" * 80)
582	
583	    try:
584	        import matplotlib
585	        matplotlib.use("Agg")
586	        import matplotlib.pyplot as plt
587	        import matplotlib.patheffects as pe
588	    except ImportError:
589	        print("ERROR: matplotlib not available")
590	        return
591	
592	    try:
593	        from scipy.interpolate import PchipInterpolator
594	    except ImportError:
595	        print("WARNING: scipy not available, using linear interpolation")
596	        PchipInterpolator = None
597	
598	    # Load theoretical data
599	    EXPOSURE_THEORY = {
600	        "diag_thresh":    [0.0, 0.5, 0.7, 0.9],
601	        "violation_rate": [0.850, 0.325, 0.137, 0.119],
602	        "sign_flip_rate": [0.834, 0.216, 0.021, 0.000],
603	    }
604	
605	    with open(PROJ / "artifacts/iv_dirichlet_subspace_results.json") as f:
606	        iv_raw = json.load(f)
607	    IV_THEORY = {
608	        "diag_thresh":    [],
609	        "violation_rate": [],
610	        "sign_flip_rate": [],
611	    }
612	    for t in ("0.0", "0.5", "0.7", "0.9"):
613	        IV_THEORY["diag_thresh"].append(float(t))
614	        IV_THEORY["violation_rate"].append(iv_raw["thresholds"][t]["violation_rate"])
615	        IV_THEORY["sign_flip_rate"].append(iv_raw["thresholds"][t]["sign_flip_rate"])
616	
617	    # Style
618	    plt.rcParams.update({
619	        "font.family": "serif",
620	        "font.serif": ["Times New Roman", "DejaVu Serif", "Times"],
621	        "font.size": 9,
622	        "axes.titlesize": 10,
623	        "axes.labelsize": 9,
624	        "xtick.labelsize": 8,
625	        "ytick.labelsize": 8,
626	        "legend.fontsize": 7,
627	        "figure.dpi": 300,
628	        "savefig.dpi": 300,
629	        "savefig.bbox": "tight",
630	        "savefig.pad_inches": 0.05,
631	        "axes.spines.top": False,
632	        "axes.spines.right": False,
633	        "lines.linewidth": 1.4,
634	        "mathtext.fontset": "stix",
635	    })
636	
637	    # Marker / color encoding
638	    DATASET_MARKERS = {
639	        "humaid":         {"marker": "o", "size": 40},
640	        "vast":           {"marker": "s", "size": 40},
641	        "civil_comments": {"marker": "^", "size": 50},
642	    }
643	    MODEL_COLORS = {
644	        "llama4":     "#E31A1C",   # red
645	        "qwen3":      "#1F78B4",   # blue
646	        "deepseek":   "#33A02C",   # green
647	        "qwen2.5-7b": "#FF7F00",   # orange
648	    }
649	
650	    # Build config list
651	    configs = []
652	    for key, C in all_cms.items():
653	        meta = config_meta[key]
654	        model = meta["model_prompt"].split("_")[0]
655	        # Handle "qwen2.5-7b" model name
656	        if "qwen2.5" in meta["model_prompt"]:
657	            model = "qwen2.5-7b"
658	            prompt = meta["model_prompt"].replace("qwen2.5-7b_", "")
659	        else:
660	            prompt = meta["model_prompt"][len(model)+1:]
661	        configs.append({
662	            "key": key,
663	            "dataset": meta["dataset"],
664	            "model": model,
665	            "prompt": prompt,
666	            "K": meta["K"],
667	            "min_diag": meta["min_diag"],
668	        })
669	
670	    def smooth_curve(xs, ys, n=200):
671	        xs = np.asarray(xs, dtype=float)
672	        ys = np.asarray(ys, dtype=float)
673	        xx = np.linspace(0.0, 1.0, n)
674	        if PchipInterpolator is not None:
675	            interp = PchipInterpolator(xs, ys, extrapolate=False)
676	            yy = interp(xx)
677	            yy[xx < xs[0]] = ys[0]
678	            yy[xx > xs[-1]] = ys[-1]
679	        else:
680	            yy = np.interp(xx, xs, ys)
681	        return xx, yy
682	
683	    def interp_at(x, xs, ys):
684	        xs = np.asarray(xs, dtype=float)
685	        ys = np.asarray(ys, dtype=float)
686	        if x <= xs[0]:
687	            return float(ys[0])
688	        if x >= xs[-1]:
689	            return float(ys[-1])
690	        if PchipInterpolator is not None:
691	            return float(PchipInterpolator(xs, ys, extrapolate=False)(x))
692	        return float(np.interp(x, xs, ys))
693	
694	    def draw_panel(ax, theory, panel_title, panel_letter, show_violation_fill=True):
695	        xs_t = theory["diag_thresh"]
696	        vr_t = theory["violation_rate"]
697	        sf_t = theory["sign_flip_rate"]
698	
699	        xx, vr_curve = smooth_curve(xs_t, vr_t)
700	        _, sf_curve = smooth_curve(xs_t, sf_t)
701	
702	        # Shading zones
703	        ax.axvspan(0.0, 0.5, color="#FDAE61", alpha=0.12, zorder=0,
704	                   label="_nolegend_")  # danger
705	        ax.axvspan(0.5, 0.7, color="#FEE08B", alpha=0.10, zorder=0,
706	                   label="_nolegend_")  # caution
707	        ax.axvspan(0.9, 1.0, color="#A6D96A", alpha=0.12, zorder=0,
708	                   label="_nolegend_")  # safe
709	
710	        # Theory curves
711	        if show_violation_fill:
712	            ax.fill_between(xx, 0, vr_curve,
713	                            color="#888888", alpha=0.15, zorder=1,
714	                            label="Violation rate (theory)")
715	            ax.plot(xx, vr_curve, color="#555555", linewidth=1.2, zorder=2)
716	        else:
717	            ax.axhline(1.0, color="#888888", linewidth=1.0, alpha=0.5,
718	                       linestyle=":", zorder=1,
719	                       label="Violation rate (theory) $=1$")
720	
721	        ax.plot(xx, sf_curve, color="#B22222", linewidth=1.4,
722	                linestyle="--", zorder=3,
723	                label="Sign-flip rate (theory)")
724	
725	        # Theory anchor points
726	        ax.scatter(xs_t, vr_t, s=15, color="#555555",
727	                   marker="x", linewidth=0.8, zorder=4, label="_nolegend_")
728	        ax.scatter(xs_t, sf_t, s=15, color="#B22222",
729	                   marker="x", linewidth=0.8, zorder=4, label="_nolegend_")
730	
731	        # Empirical points
732	        handled = set()
733	        for cfg in configs:
734	            x = cfg["min_diag"]
735	            y = interp_at(x, xs_t, vr_t)
736	            ds = cfg["dataset"]
737	            style = DATASET_MARKERS[ds]
738	            color = MODEL_COLORS.get(cfg["model"], "#999999")
739	
740	            legend_key = (ds, cfg["model"])
741	            if legend_key not in handled:
742	                handled.add(legend_key)
743	                ds_short = {"humaid": "HumAID", "vast": "VAST",
744	                            "civil_comments": "CC"}[ds]
745	                lbl = f"{ds_short}/{cfg['model']} ($K$={cfg['K']})"
746	            else:
747	                lbl = None
748	
749	            ax.scatter(x, y, marker=style["marker"], s=style["size"],
750	                       facecolor=color, edgecolor="white", linewidth=0.6,
751	                       zorder=6, label=lbl)
752	
753	        # Zone labels
754	        for txt_str, pos, col in [
755	            ("sign-flip\nzone", (0.08, 0.55), "#A53A0C"),
756	            ("safe", (0.95, 0.06), "#2B7A3B"),
757	        ]:
758	            t = ax.text(pos[0], pos[1], txt_str, ha="center", va="center",
759	                        fontsize=7, color=col, fontstyle="italic",
760	                        transform=ax.transAxes)
761	            t.set_path_effects([pe.withStroke(linewidth=2.0, foreground="white")])
762	
763	        ax.set_xlim(0.0, 1.0)
764	        ax.set_ylim(-0.03, 1.15)
765	        ax.set_xlabel(r"Min.\ diagonal dominance $\min_k C_{kk}$")
766	        if panel_letter == "a":
767	            ax.set_ylabel("Violation / sign-flip rate")
768	        ax.set_title(f"({panel_letter}) {panel_title}", loc="left", pad=4,
769	                     fontweight="bold")
770	        ax.grid(True, axis="y", alpha=0.2, linewidth=0.4, zorder=0)
771	
772	    # Build figure (single-column width ~ 3.5 inches, but we use 7.0 for two panels)
773	    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2), sharey=True)
774	
775	    draw_panel(axes[0], EXPOSURE_THEORY, "Exposure", "a",
776	               show_violation_fill=True)
777	    draw_panel(axes[1], IV_THEORY, "IV", "b",
778	               show_violation_fill=False)
779	
780	    # Unified legend
781	    handles, labels = [], []
782	    for ax in axes:
783	        h, l = ax.get_legend_handles_labels()
784	        for hh, ll in zip(h, l):
785	            if ll and ll not in labels:
786	                handles.append(hh)
787	                labels.append(ll)
788	    fig.legend(handles, labels,
789	               loc="lower center", bbox_to_anchor=(0.5, -0.08),
790	               ncol=4, frameon=False, columnspacing=1.0,
791	               handletextpad=0.4, fontsize=7)
792	
793	    plt.tight_layout(rect=(0, 0.04, 1, 1.0))
794	
795	    out_pdf = PROJ / "figures/paper/fig7_dirichlet_overlay.pdf"
796	    out_png = PROJ / "figures/paper/fig7_dirichlet_overlay.png"
797	    out_pdf.parent.mkdir(parents=True, exist_ok=True)
798	    plt.savefig(out_pdf)
799	    plt.savefig(out_png)
800	    plt.close()
801	
802	    print(f"Saved: {out_pdf}")
803	    print(f"Saved: {out_png}")
804	
805	    # Print empirical positions for reference
806	    print(f"\n{'config':<52} {'K':>3} {'min_diag':>9}")
807	    print("-" * 70)
808	    for cfg in sorted(configs, key=lambda c: c["min_diag"]):
809	        key = f"{cfg['dataset']}_{cfg['model']}_{cfg['prompt']}"
810	        print(f"{key:<52} {cfg['K']:>3} {cfg['min_diag']:>9.4f}")
811	
812	    return {"n_configs": len(configs), "output_files": [str(out_pdf), str(out_png)]}
813	
814	
815	# ============================================================================
816	# Main
817	# ============================================================================
818	
819	def main():
820	    t_start = time.time()
821	    print("Loading all data...")
822	    all_cms, config_meta, bias_lookup, filter_data = load_all_data()
823	    print(f"Loaded {len(all_cms)} confusion matrices")
824	    for k, m in sorted(config_meta.items()):
825	        print(f"  {k:<52} K={m['K']:>2}  min_diag={m['min_diag']:.4f}  "
826	              f"trace={m['trace']:.4f}")
827	
828	    # Task 1
829	    mape_result = task1_mape(all_cms, config_meta, bias_lookup)
830	
831	    # Task 2
832	    ppi_result = task2_ppi(all_cms, config_meta)
833	
834	    # Task 3
835	    fig_result = task3_dirichlet_overlay(all_cms, config_meta)
836	
837	    print(f"\n{'='*80}")
838	    print(f"ALL TASKS COMPLETE in {time.time()-t_start:.1f}s")
839	    print(f"{'='*80}")
840	    print(f"\nTask 1: Grand MAPE = {mape_result['grand_mape']:.4%}")
841	    print(f"Task 2: Grand PPI++ reduction = {ppi_result['grand_mean_bias_reduction_pct']:.1f}%")
842	    if fig_result:
843	        print(f"Task 3: Figure saved with {fig_result['n_configs']} configs")
844	    else:
845	        print("Task 3: SKIPPED (matplotlib not available)")
846	
847	
848	if __name__ == "__main__":
849	    main()
850	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e2fd649-d176-485f-9c24-46d860612b41",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "6cd444f2-f417-4fe2-abaf-d69e0ce334ae",
  "sourceToolAssistantUUID": "4e2fd649-d176-485f-9c24-46d860612b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-22T11:30:23.174Z_

Now let me examine the plan_006_asv_empirical.py file to find where these functions are defined:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cd444f2-f417-4fe2-abaf-d69e0ce334ae",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkdmpinj6mGcUuPcZM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e3cd2027-fd14-4922-940d-32449714d588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0128mhtUVAJEYWuns9bCgT2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 19701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12953,
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

_source line 9 · 2026-05-22T11:30:23.746Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015HfRxAeP8EqE4CioFqjHPd`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3cd2027-fd14-4922-940d-32449714d588",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXkdmpinj6mGcUuPcZM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e44f6a9b-6904-4684-958f-04f47e70aedd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0128mhtUVAJEYWuns9bCgT2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 19701,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 121,
          "cache_read_input_tokens": 19701,
          "cache_creation_input_tokens": 12953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12953,
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

_source line 10 · 2026-05-22T11:30:23.814Z_

<details><summary>↩ Tool result · `toolu_015HfRxAeP8EqE4CioFqjHPd`</summary>

```text
1091 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e44f6a9b-6904-4684-958f-04f47e70aedd",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "84375791-8072-4c11-a01c-fd4894483bf6",
  "sourceToolAssistantUUID": "e44f6a9b-6904-4684-958f-04f47e70aedd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T11:30:26.455Z_

Let me search for the three functions in this file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84375791-8072-4c11-a01c-fd4894483bf6",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXknukS9pTSUdMxzMjV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea68abe3-26aa-4abd-b408-ed0ad07fb553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cSyXjcqQd5mTWSzt7h3Zt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 32654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 176,
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

_source line 12 · 2026-05-22T11:30:27.278Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YLj7DTYAaWxjN3Ug8P85Cv`</summary>

```json
{
  "pattern": "^def (compute_plim|precompute_suff_stats|extract_tau)",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea68abe3-26aa-4abd-b408-ed0ad07fb553",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXknukS9pTSUdMxzMjV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6cbd884-92dd-4563-98d0-2cef616c9b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011cSyXjcqQd5mTWSzt7h3Zt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 32654,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 158,
          "cache_read_input_tokens": 32654,
          "cache_creation_input_tokens": 176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 176,
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

_source line 13 · 2026-05-22T11:30:27.358Z_

<details><summary>↩ Tool result · `toolu_01YLj7DTYAaWxjN3Ug8P85Cv`</summary>

```text
342:def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
369:def compute_plim(C, st, K):
415:def extract_tau(plim_result, topology):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6cbd884-92dd-4563-98d0-2cef616c9b5a",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "ecab9106-8cee-460c-b96b-1f672881c0b0",
  "sourceToolAssistantUUID": "f6cbd884-92dd-4563-98d0-2cef616c9b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-22T11:30:28.532Z_

Perfect! Now let me read these function definitions to provide you with their details:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecab9106-8cee-460c-b96b-1f672881c0b0",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXm47oA35cuML8VsW2c",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "26b0f33c-a2a0-45a6-983e-4d987aa9744b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtY9M8hpuAqb1h4sEkEZNr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 32830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 231,
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

_source line 15 · 2026-05-22T11:30:28.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_019PEhJZBWqBFsSC3LMFFnvp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 342,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b0f33c-a2a0-45a6-983e-4d987aa9744b",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXm47oA35cuML8VsW2c",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "270ad87f-6c50-4f6e-bfcb-3d5f7238287b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtY9M8hpuAqb1h4sEkEZNr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 32830,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 231
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 143,
          "cache_read_input_tokens": 32830,
          "cache_creation_input_tokens": 231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 231,
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

_source line 16 · 2026-05-22T11:30:28.916Z_

<details><summary>↩ Tool result · `toolu_019PEhJZBWqBFsSC3LMFFnvp`</summary>

```text
342	def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
343	    rng = np.random.default_rng(seed)
344	    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
345	    DA = np.zeros((N, K))
346	    for k in range(K):
347	        DA[:, k] = (A == k).astype(float)
348	
349	    if topology == 'iv':
350	        Z = first_var
351	        z1 = Z == 1; z0 = Z == 0
352	        RF = Y[z1].mean() - Y[z0].mean()
353	        FS = np.zeros(K)
354	        for k in range(K):
355	            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
356	        return dict(RF=RF, FS=FS, topology='iv')
357	    elif topology == 'exposure':
358	        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
359	                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
360	    else:
361	        T = first_var
362	        return dict(
363	            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
364	            E_Y=Y.mean(), E_TY=(T * Y).mean(),
365	            E_TD=(DA * T[:, None]).mean(0),
366	            E_YD=(DA * Y[:, None]).mean(0), topology=topology)
367	
368	
369	def compute_plim(C, st, K):
370	    if st['topology'] == 'iv':
371	        FS_star = C @ st['FS']
372	        if abs(FS_star[1]) < 1e-8:
373	            return np.nan
374	        return st['RF'] / FS_star[1]
375	    elif st['topology'] == 'exposure':
376	        q = C @ st['p_A']
377	        cy = C @ st['E_YD']
378	        EZZ = np.zeros((K, K))
379	        EZZ[0, 0] = 1.0
380	        for j in range(1, K):
381	            EZZ[0, j] = EZZ[j, 0] = q[j]
382	            EZZ[j, j] = q[j]
383	        EZY = np.zeros(K)
384	        EZY[0] = st['E_Y']
385	        for j in range(1, K):
386	            EZY[j] = cy[j]
387	        try:
388	            return np.linalg.solve(EZZ, EZY)
389	        except np.linalg.LinAlgError:
390	            return np.full(K, np.nan)
391	    else:
392	        q = C @ st['p_A']
393	        ct = C @ st['E_TD']
394	        cy = C @ st['E_YD']
395	        dim = K + 1
396	        EZZ = np.zeros((dim, dim))
397	        EZZ[0, 0] = 1.0
398	        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
399	        EZZ[1, 1] = st['E_T2']
400	        for j in range(1, K):
401	            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
402	            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
403	            EZZ[j + 1, j + 1] = q[j]
404	        EZY = np.zeros(dim)
405	        EZY[0] = st['E_Y']
406	        EZY[1] = st['E_TY']
407	        for j in range(1, K):
408	            EZY[j + 1] = cy[j]
409	        try:
410	            return np.linalg.solve(EZZ, EZY)
411	        except np.linalg.LinAlgError:
412	            return np.full(dim, np.nan)
413	
414	
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
429	    d = np.load(path, allow_pickle=True)
430	    C = d['C']
431	    assert C.shape == (K, K), f"Expected ({K},{K}), got {C.shape}"
432	    return C
433	
434	
435	def load_annotations(data_dir, dataset, model, prompt):
436	    for suffix in ['_annotations.jsonl', '.jsonl']:
437	        path = os.path.join(data_dir, dataset, f"{model}_{prompt}{suffix}")
438	        if os.path.exists(path):
439	            break
440	    else:
441	        raise FileNotFoundError(f"No annotation file for {dataset}/{model}_{prompt}")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "270ad87f-6c50-4f6e-bfcb-3d5f7238287b",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "7de6a44e-3350-43ea-8253-e6a0649ef288",
  "sourceToolAssistantUUID": "270ad87f-6c50-4f6e-bfcb-3d5f7238287b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T11:30:30.171Z_

Perfect! I found all three functions. Let me also check if there are any other references to these functions or related utilities:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7de6a44e-3350-43ea-8253-e6a0649ef288",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmAq7osr9ZK9UVpfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24d2b2dc-fdb1-4564-b11d-0077f56a1603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YUnJiAmWq8c4tuR66WXgoe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 33061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1830,
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

_source line 18 · 2026-05-22T11:30:31.262Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KdhZUSVyy3fK7LtKAkLLEu`</summary>

```json
{
  "command": "grep -n \"N_PRECOMP\\|GEN_FNS\" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d2b2dc-fdb1-4564-b11d-0077f56a1603",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmAq7osr9ZK9UVpfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01f3dadb-9e8d-4213-a3ff-2835902ca507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YUnJiAmWq8c4tuR66WXgoe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1830,
      "cache_read_input_tokens": 33061,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 140,
          "cache_read_input_tokens": 33061,
          "cache_creation_input_tokens": 1830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1830,
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

_source line 19 · 2026-05-22T11:30:31.428Z_

<details><summary>↩ Tool result · `toolu_01KdhZUSVyy3fK7LtKAkLLEu`</summary>

```text
52:N_PRECOMP = 2_000_000
331:GEN_FNS = {
342:def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
344:    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
591:    gen_fn = GEN_FNS[topology]
679:    gen_fn = GEN_FNS[topology]
903:    n_precomp = 500_000 if args.mock else N_PRECOMP
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01f3dadb-9e8d-4213-a3ff-2835902ca507",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "5535411c-5039-452c-9fc8-43f7f7bba337",
  "sourceToolAssistantUUID": "01f3dadb-9e8d-4213-a3ff-2835902ca507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T11:30:33.400Z_

Let me get more context on the file structure and where these functions are used:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5535411c-5039-452c-9fc8-43f7f7bba337",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmMV4wGnKCBcsvxdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38312459-2335-4b93-bca9-d0b34d8f6444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TursWiFtJkjhPc6dN4zhMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 34891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 300,
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

_source line 21 · 2026-05-22T11:30:33.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A872g92brdg1EMxkGDehyH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38312459-2335-4b93-bca9-d0b34d8f6444",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmMV4wGnKCBcsvxdFT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a9c31bf-b624-461a-8b99-4ccf289eb96b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TursWiFtJkjhPc6dN4zhMq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 34891,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 143,
          "cache_read_input_tokens": 34891,
          "cache_creation_input_tokens": 300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 300,
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

_source line 22 · 2026-05-22T11:30:33.815Z_

<details><summary>↩ Tool result · `toolu_01A872g92brdg1EMxkGDehyH`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
60	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a9c31bf-b624-461a-8b99-4ccf289eb96b",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "4a6a74e9-3eb8-4689-8e54-aaded6cdd199",
  "sourceToolAssistantUUID": "5a9c31bf-b624-461a-8b99-4ccf289eb96b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T11:30:35.071Z_

Now let me check the functions one more time to get the complete definitions with better context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a6a74e9-3eb8-4689-8e54-aaded6cdd199",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmXx7X2KLv6wPKBkXE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fea6a69e-75dc-41be-bf16-543dcf9d94dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KfUKUvJtAMaz1t7fhpTws6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 35191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1100,
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

_source line 24 · 2026-05-22T11:30:35.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_0175qWMt861VHbCiWnSnmLui`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "offset": 330,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea6a69e-75dc-41be-bf16-543dcf9d94dc",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmXx7X2KLv6wPKBkXE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93321dc2-25c6-4e7f-9ae3-4e5eed218ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KfUKUvJtAMaz1t7fhpTws6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 35191,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1100
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 145,
          "cache_read_input_tokens": 35191,
          "cache_creation_input_tokens": 1100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1100,
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

_source line 25 · 2026-05-22T11:30:35.876Z_

<details><summary>↩ Tool result · `toolu_0175qWMt861VHbCiWnSnmLui`</summary>

```text
330	
331	GEN_FNS = {
332	    'confounding': gen_confounding, 'mediation': gen_mediation,
333	    'collider': gen_collider, 'exposure': gen_exposure,
334	    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
335	}
336	
337	
338	# ============================================================================
339	# Sufficient Statistics & Plim (general K)
340	# ============================================================================
341	
342	def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
343	    rng = np.random.default_rng(seed)
344	    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
345	    DA = np.zeros((N, K))
346	    for k in range(K):
347	        DA[:, k] = (A == k).astype(float)
348	
349	    if topology == 'iv':
350	        Z = first_var
351	        z1 = Z == 1; z0 = Z == 0
352	        RF = Y[z1].mean() - Y[z0].mean()
353	        FS = np.zeros(K)
354	        for k in range(K):
355	            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
356	        return dict(RF=RF, FS=FS, topology='iv')
357	    elif topology == 'exposure':
358	        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
359	                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
360	    else:
361	        T = first_var
362	        return dict(
363	            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
364	            E_Y=Y.mean(), E_TY=(T * Y).mean(),
365	            E_TD=(DA * T[:, None]).mean(0),
366	            E_YD=(DA * Y[:, None]).mean(0), topology=topology)
367	
368	
369	def compute_plim(C, st, K):
370	    if st['topology'] == 'iv':
371	        FS_star = C @ st['FS']
372	        if abs(FS_star[1]) < 1e-8:
373	            return np.nan
374	        return st['RF'] / FS_star[1]
375	    elif st['topology'] == 'exposure':
376	        q = C @ st['p_A']
377	        cy = C @ st['E_YD']
378	        EZZ = np.zeros((K, K))
379	        EZZ[0, 0] = 1.0
380	        for j in range(1, K):
381	            EZZ[0, j] = EZZ[j, 0] = q[j]
382	            EZZ[j, j] = q[j]
383	        EZY = np.zeros(K)
384	        EZY[0] = st['E_Y']
385	        for j in range(1, K):
386	            EZY[j] = cy[j]
387	        try:
388	            return np.linalg.solve(EZZ, EZY)
389	        except np.linalg.LinAlgError:
390	            return np.full(K, np.nan)
391	    else:
392	        q = C @ st['p_A']
393	        ct = C @ st['E_TD']
394	        cy = C @ st['E_YD']
395	        dim = K + 1
396	        EZZ = np.zeros((dim, dim))
397	        EZZ[0, 0] = 1.0
398	        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
399	        EZZ[1, 1] = st['E_T2']
400	        for j in range(1, K):
401	            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
402	            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
403	            EZZ[j + 1, j + 1] = q[j]
404	        EZY = np.zeros(dim)
405	        EZY[0] = st['E_Y']
406	        EZY[1] = st['E_TY']
407	        for j in range(1, K):
408	            EZY[j + 1] = cy[j]
409	        try:
410	            return np.linalg.solve(EZZ, EZY)
411	        except np.linalg.LinAlgError:
412	            return np.full(dim, np.nan)
413	
414	
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
429	    d = np.load(path, allow_pickle=True)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93321dc2-25c6-4e7f-9ae3-4e5eed218ba0",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "9be927ac-977d-4f6b-8697-00c068aac66c",
  "sourceToolAssistantUUID": "93321dc2-25c6-4e7f-9ae3-4e5eed218ba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-22T11:30:37.189Z_

Perfect! Now let me verify the file path and document structure one more time:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9be927ac-977d-4f6b-8697-00c068aac66c",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmgcWDbCGeQygizQyD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e780779-4cd5-408c-8a04-bc7642dcc175",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H1yhXcn4T5p4Sp5KuyVfpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 36291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1699,
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

_source line 27 · 2026-05-22T11:30:38.003Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JWagjGUMtmatW6uHU6TrMb`</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e780779-4cd5-408c-8a04-bc7642dcc175",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmgcWDbCGeQygizQyD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e4958a2-89da-486a-8212-ec4bec402737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H1yhXcn4T5p4Sp5KuyVfpN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 36291,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 36291,
          "cache_creation_input_tokens": 1699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1699,
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

_source line 28 · 2026-05-22T11:30:38.203Z_

<details><summary>↩ Tool result · `toolu_01JWagjGUMtmatW6uHU6TrMb`</summary>

```text
#!/usr/bin/env python3
"""
plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices

Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e4958a2-89da-486a-8212-ec4bec402737",
  "isSidechain": true,
  "promptId": "920e9e80-4df5-4966-ac7b-f70832625e1c",
  "agentId": "a6dcd171d346aa1b5",
  "type": "user",
  "uuid": "bfdc3b56-d506-4903-a894-87b5003b9158",
  "sourceToolAssistantUUID": "7e4958a2-89da-486a-8212-ec4bec402737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T11:30:45.949Z_

Excellent! Now I have all the information. Let me create a summary of my findings.

## Summary

I've successfully located all three functions referenced in `compute_all_tasks.py` as `plan_006.compute_plim`, `plan_006.precompute_suff_stats`, and `plan_006.extract_tau`. They are all defined in the same file that's imported:

### Functions Location
**File:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py`

### Function Definitions

**1. `precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42)`** (line 342)
- Precomputes sufficient statistics for a given topology and number of classes K
- Generates data using `GEN_FNS[topology]` generator function
- Returns different statistics based on topology:
  - **IV topology**: returns `dict(RF=..., FS=..., topology='iv')`
  - **Exposure topology**: returns `dict(p_A=..., E_Y=..., E_YD=..., topology='exposure')`
  - **Other topologies**: returns comprehensive statistics including `p_A`, `E_T`, `E_T2`, `E_Y`, `E_TY`, `E_TD`, `E_YD`

**2. `compute_plim(C, st, K)`** (line 369)
- Computes the probability limit (plim) of the estimator given confusion matrix C and sufficient statistics st
- Handles three cases based on topology:
  - **IV**: returns scalar value `st['RF'] / FS_star[1]`
  - **Exposure**: solves linear system `EZZ @ beta = EZY` and returns coefficient vector
  - **Other topologies**: solves expanded linear system with treatment term
- Returns `np.nan` on singular matrices or numerical issues

**3. `extract_tau(plim_result, topology)`** (line 415)
- Extracts the causal effect estimate (tau) from plim_result
- For IV topology: returns the scalar result as float
- For other topologies: returns element at index [1] from the coefficient vector (the treatment effect)
- Returns `np.nan` if result is not finite

### Context
These functions are core to the causal analysis pipeline for the paper on "Causal Annotation Error Attribution." They work together to:
1. Precompute sufficient statistics from data generated under a specific DAG topology
2. Compute the probability limit of causal effect estimates biased by confusion matrices
3. Extract the treatment effect coefficient from the full set of estimates

The `plan_006_asv_empirical.py` file is imported dynamically in `compute_all_tasks.py` (lines 24-29) to support three computational tasks: theory-empirical MAPE validation, PPI++ empirical validation, and Dirichlet subspace overlay visualization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfdc3b56-d506-4903-a894-87b5003b9158",
  "isSidechain": true,
  "agentId": "a6dcd171d346aa1b5",
  "requestId": "req_011CbHXmrmSmJCTawbkqoKQT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6a25015-ca94-4ec8-bb64-99ad8c1be799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a41664f4-9250-4c0c-9c38-9466fdeddc4e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fvoag992afBtGywfzu7Eap",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 185,
      "cache_read_input_tokens": 37990,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 185
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 37990,
          "cache_creation_input_tokens": 185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 185,
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
