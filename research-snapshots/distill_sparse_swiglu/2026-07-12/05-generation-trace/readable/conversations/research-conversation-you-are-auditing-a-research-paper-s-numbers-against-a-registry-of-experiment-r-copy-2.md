# Research conversation: You are auditing a research paper's numbers against a registry of experiment results. Your job is to verify every single

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0deae6eff35145f3.jsonl`
- **Structured JSON:** [`07bf0b4a88c2d86432d0.json`](../../sessions/07/07bf0b4a88c2d86432d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-23T19:19:30.792Z_

You are auditing a research paper's numbers against a registry of experiment results. Your job is to verify every single number in "Table 3" (the main results table) of the paper.

## Table 3 from the paper (experiments.tex)
The table has these rows (I'm copying from the LaTeX):

```
0% Dense: PPL 6.12, ARC-c 58.28, WG 78.06, MMLU 65.27, GSM8K 48.75
30% TEAL uniform: PPL 10.82, ARC-c 39.33, WG 65.04, MMLU 45.86, GSM8K 8.79  (exp_id: teal30_uniform)
30% BCE global: PPL 11.25, ARC-c 41.2, WG 66.0, MMLU 36.3, GSM8K 6.0  (exp_id: bce30_teal_global)
30% BCE uniform: PPL 15.09±0.13, ARC-c 33.45, WG 61.09, MMLU 43.05, GSM8K 3.97  (exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456)
30% MSE uniform: PPL 18.52±1.68, ARC-c 35.8±4.1, WG 59.8±2.6, MMLU 30.7±2.6, GSM8K 2.3±0.7  (exp_id: mse30_3seed)
30% KL global: PPL 8.96±0.02, ARC-c 43.8±3.6, WG 70.2±0.9, MMLU 35.7±9.5, GSM8K 8.0±0.7  (exp_id: kl30_3seed_global)
30% KL uniform: PPL 8.81±0.02, ARC-c 43.7±2.5, WG 68.9±0.4, MMLU 40.7±1.3, GSM8K 7.5±0.1  (exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform)
50% TEAL uniform: PPL 23.90, ARC-c 27.47, WG 54.38, MMLU 29.26, GSM8K 1.74  (exp_id: teal50_uniform)
50% BCE (2700 steps): PPL 28.13±0.20, ARC-c 27.6±0.6, WG 51.8±0.6, MMLU 26.1±0.5, GSM8K 2.1±0.2  (exp_id: bce50_3seed)
50% MSE uniform: PPL 229.26, ARC-c 25.00, WG 50.59, MMLU 23.79, GSM8K 1.59  (exp_id: mse50_uniform_s42)
50% KL global: PPL 11.84±0.15, ARC-c 36.3±3.2, WG 63.8±0.3, MMLU 28.3±0.7, GSM8K 2.7±1.3  (exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval)
50% KL uniform: PPL 11.92±0.07, ARC-c 33.8±1.2, WG 62.9±0.1, MMLU 28.0±0.6, GSM8K 2.2±0.1  (exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456)
```

## What to do

Read the file `/tmp/registry_all_metrics.json` and cross-check EVERY number in the table above against the registry data.

For multi-seed entries (±std), you need to:
1. Find the individual seed experiments
2. Compute mean and std
3. Verify they match

The registry exp_ids don't always match the paper's shorthand. Here are the actual registry exp_ids you should look for:
- bench_kl30_uniform → bench_kl30_uniform
- TEAL 30% → bench_teal30_uniform_6task or bench_teal30 (check both for ARC-c, WG, MMLU, GSM8K)
- BCE global → bce_30pct_s42_eval or bce_30pct_s42
- BCE uniform 30% (3-seed) → bce_isocompute_v3_s42_eval, bce_isocompute_v3_s123_eval, bce_isocompute_v3_s456_eval (or bce_iso_v3_s42_30pct_uniform_eval etc.)
- MSE 30% (3-seed) → mse30_s42_eval_7task, mse30_s123_downstream, mse30_s456_downstream
- KL 30% global (3-seed) → bench_kl30_global, kl30_s123_global_v3, kl30_s456_global_v3
- KL 30% uniform (3-seed) → bench_kl30_uniform, kl30_s123_uniform_v3 or kl30_s123_eval, kl30_s456_uniform_eval or kl30_s456_uniform_v3
- TEAL 50% → bench_teal50_uniform_6task or bench_teal50
- BCE 50% (3-seed) → bce_50pct_teal_global_unified (may contain all 3 seeds)
- MSE 50% → mse50_s42_eval_7task or mse50_s42_train
- KL 50% global (3-seed) → bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
- KL 50% uniform (3-seed) → bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456

Also check the Dense baseline: bench_dense

For each number, report: [MATCH] or [MISMATCH: paper says X, registry says Y]

Also verify the derived claims:
- "14.5% reduction" = (10.30 - 8.81) / 10.30 (note: paper says "8.81 vs 10.30, both at 28.5%")  → verify this calculation
- "50% reduction at 50%" = (23.90 - 11.92) / 23.90

Report findings concisely. Focus on mismatches.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "c754054c-7884-4fa3-b573-98d55b246d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T19:19:30.797Z_

```json
{
  "parentUuid": "c754054c-7884-4fa3-b573-98d55b246d4f",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "66f62fa4-b0e5-47a8-88b8-475c1a71b7fd",
  "timestamp": "2026-05-23T19:19:30.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T19:19:44.859Z_



I'll read the registry file first, then systematically verify every number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66f62fa4-b0e5-47a8-88b8-475c1a71b7fd",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3LYgKNBZe53VJTF4i1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c262b38a-9b07-43f6-847e-b6c9c381762b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ncaGRDtf1nz6N1uqUVA67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17242,
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

_source line 4 · 2026-05-23T19:19:45.472Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XsbFTRn1gifiLHLSmo5os9`</summary>

```json
{
  "file_path": "/tmp/registry_all_metrics.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c262b38a-9b07-43f6-847e-b6c9c381762b",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3LYgKNBZe53VJTF4i1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3470356c-7244-48b2-9a71-baaca57aa193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ncaGRDtf1nz6N1uqUVA67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17242,
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

_source line 5 · 2026-05-23T19:19:45.715Z_

<details><summary>↩ Tool result · `toolu_01XsbFTRn1gifiLHLSmo5os9`</summary>

```text
1	{
2	  "bench_kl30_uniform": {
3	    "metrics": {
4	      "wikitext2_ppl": 8.8157,
5	      "arc_challenge_acc_norm": 0.4078,
6	      "winogrande_acc": 0.6859,
7	      "mmlu_acc": 0.4061,
8	      "gsm8k_exact_match": 0.0735,
9	      "actual_sparsity": 0.3
10	    },
11	    "conclusion": "success"
12	  },
13	  "bench_kl30_global": {
14	    "metrics": {
15	      "wikitext2_ppl": 8.9768,
16	      "arc_challenge_acc_norm": 0.3968,
17	      "winogrande_acc": 0.7017,
18	      "mmlu_acc": 0.2527,
19	      "gsm8k_exact_match": 0.0879,
20	      "actual_sparsity": 0.3
21	    },
22	    "conclusion": "success"
23	  },
24	  "bench_kl50_global": {
25	    "metrics": {
26	      "wikitext2_ppl": 11.7933,
27	      "arc_challenge_acc_norm": 0.3285,
28	      "winogrande_acc": 0.6346,
29	      "mmlu_acc": 0.2789,
30	      "gsm8k_exact_match": 0.0129,
31	      "actual_sparsity": 0.5
32	    },
33	    "conclusion": "success"
34	  },
35	  "bench_kl50_uniform": {
36	    "metrics": {
37	      "wikitext2_ppl": 11.963,
38	      "arc_challenge_acc_norm": 0.3276,
39	      "winogrande_acc": 0.629,
40	      "mmlu_acc": 0.2777,
41	      "gsm8k_exact_match": 0.0212,
42	      "actual_sparsity": 0.5
43	    },
44	    "conclusion": "success"
45	  },
46	  "bench_kl50_uniform_s123": {
47	    "metrics": {
48	      "wikitext2_ppl": 11.83,
49	      "arc_challenge_acc_norm": 0.3515,
50	      "winogrande_acc": 0.6298,
51	      "mmlu_acc": 0.2751,
52	      "gsm8k_exact_match": 0.0235,
53	      "actual_sparsity": 0.5
54	    },
55	    "conclusion": "success"
56	  },
57	  "bench_kl50_uniform_s456": {
58	    "metrics": {
59	      "wikitext2_ppl": 11.9604,
60	      "arc_challenge_acc_norm": 0.3345,
61	      "winogrande_acc": 0.6275,
62	      "mmlu_acc": 0.2874,
63	      "gsm8k_exact_match": 0.0212,
64	      "actual_sparsity": 0.5
65	    },
66	    "conclusion": "success"
67	  },
68	  "kl50_global_s123_downstream_v2": {
69	    "metrics": {
70	      "arc_challenge_acc_norm": 0.3916,
71	      "winogrande_acc": 0.6401,
72	      "mmlu_acc": 0.2908,
73	      "gsm8k_exact_match": 0.0341
74	    },
75	    "conclusion": "success"
76	  },
77	  "kl50_global_s456_eval": {
78	    "metrics": {
79	      "wikitext2_ppl": 12.01,
80	      "arc_challenge_acc_norm": 0.369,
81	      "winogrande_acc": 0.64,
82	      "mmlu_acc": 0.28,
83	      "gsm8k_exact_match": 0.035,
84	      "hellaswag_acc_norm": 0.595,
85	      "piqa_acc_norm": 0.68
86	    },
87	    "conclusion": "killed"
88	  },
89	  "bench_teal30": {
90	    "metrics": {
91	      "wikitext2_ppl": 10.97,
92	      "arc_challenge_acc_norm": 0.4232,
93	      "winogrande_acc": 0.6606,
94	      "mmlu_acc": 0.3861,
95	      "gsm8k_exact_match": 0.0788,
96	      "actual_sparsity": 0.3
97	    },
98	    "conclusion": "success"
99	  },
100	  "bench_teal50": {
101	    "metrics": {
102	      "wikitext2_ppl": 23.31,
103	      "arc_challenge_acc_norm": 0.2841,
104	      "winogrande_acc": 0.5304,
105	      "mmlu_acc": 0.2832,
106	      "gsm8k_exact_match": 0.0197,
107	      "actual_sparsity": 0.5
108	    },
109	    "conclusion": "success"
110	  },
111	  "bench_teal30_uniform_6task": {
112	    "metrics": {
113	      "wikitext2_ppl": 10.8173,
114	      "arc_challenge_acc_norm": 0.3933,
115	      "winogrande_acc": 0.6504,
116	      "mmlu_acc": 0.4586,
117	      "hellaswag_acc_norm": 0.6331,
118	      "piqa_acc_norm": 0.728,
119	      "actual_sparsity": 0.3
120	    },
121	    "conclusion": "killed"
122	  },
123	  "bench_teal50_uniform_6task": {
124	    "metrics": {
125	      "wikitext2_ppl": 23.9,
126	      "arc_challenge_acc_norm": 0.2747,
127	      "winogrande_acc": 0.5438,
128	      "mmlu_acc": 0.2926,
129	      "hellaswag_acc_norm": 0.3935,
130	      "piqa_acc_norm": 0.6366
131	    },
132	    "conclusion": "killed"
133	  },
134	  "bench_dense": {
135	    "metrics": {
136	      "wikitext2_ppl": 6.1173,
137	      "arc_challenge_acc": 0.5478,
138	      "arc_challenge_acc_norm": 0.5828,
139	      "winogrande_acc": 0.7806,
140	      "mmlu_acc": 0.6527,
141	      "gsm8k_exact_match": 0.4875
142	    },
143	    "conclusion": "success"
144	  },
145	  "bce_isocompute_s42": {
146	    "metrics": {},
147	    "conclusion": "failed"
148	  },
149	  "bce_isocompute_v2_s42": {
150	    "metrics": {
151	      "final_loss": 0.6637,
152	      "final_bce_loss": 0.6586,
153	      "final_reg_loss": 0.0051,
154	      "final_sparsity": 0.502,
155	      "training_steps": 1000,
156	      "training_time_sec": 1047.8,
157	      "reg_weight": 2,
158	      "true_dense_ppl": 6.12,
159	      "predictor_hard_mask_ppl": 26.76,
160	      "teal_sparse_ppl": 54.84,
161	      "eval_seq_len": 2048,
162	      "eval_dataset": "wikitext-2"
163	    },
164	    "conclusion": "killed"
165	  },
166	  "bce_isocompute_v3_s42": {
167	    "metrics": {
168	      "steps": 2700,
169	      "loss": 0.6382,
170	      "bce_loss": 0.6371,
171	      "reg_loss": 0.001,
172	      "sparsity": 0.51,
173	      "training_time_seconds": 2828,
174	      "note": "BCE saturation confirmed: step 500\u21922700 only 0.006 improvement"
175	    },
176	    "conclusion": "success"
177	  },
178	  "bce_isocompute_v3_s42_eval": {
179	    "metrics": {
180	      "wikitext2_ppl": 27.9696,
181	      "arc_challenge_acc": 0.2346,
182	      "arc_challenge_acc_norm": 0.2765,
183	      "winogrande_acc": 0.5162,
184	      "mmlu_acc": 0.2614,
185	      "gsm8k_exact_match": 0.019
186	    },
187	    "conclusion": "success"
188	  },
189	  "bce_isocompute_v3_s123": {
190	    "metrics": {},
191	    "conclusion": "success"
192	  },
193	  "bce_isocompute_v3_s123_eval": {
194	    "metrics": {
195	      "wikitext2_ppl": 28.0627,
196	      "arc_challenge_acc_norm": 0.2696,
197	      "winogrande_acc": 0.513,
198	      "mmlu_acc": 0.2655,
199	      "gsm8k_exact_match": 0.022
200	    },
201	    "conclusion": "success"
202	  },
203	  "bce_isocompute_v3_s456": {
204	    "metrics": {
205	      "final_loss": 0.6368,
206	      "final_sparsity": 0.51,
207	      "training_steps": 2700
208	    },
209	    "conclusion": "success"
210	  },
211	  "bce_isocompute_v3_s456_eval": {
212	    "metrics": {
213	      "teal_sparse_ppl": 28.3503,
214	      "model_level_sparsity": 0.5,
215	      "arc_challenge_acc": 0.2312,
216	      "arc_challenge_acc_stderr": 0.01232,
217	      "arc_challenge_acc_norm": 0.2807,
218	      "arc_challenge_acc_norm_stderr": 0.01313,
219	      "winogrande_acc": 0.5241,
220	      "winogrande_acc_stderr": 0.01404,
221	      "mmlu_acc": 0.2567,
222	      "mmlu_acc_stderr": 0.00367,
223	      "gsm8k_exact_match": 0.022,
224	      "gsm8k_exact_match_stderr": 0.00404,
225	      "gsm8k_exact_match_strict": 0.00834,
226	      "gsm8k_exact_match_strict_stderr": 0.0025
227	    },
228	    "conclusion": "success"
229	  },
230	  "bce_50pct_teal_global_unified": {
231	    "metrics": {
232	      "wikitext2_ppl": 27.97,
233	      "arc_challenge_acc_norm": 0.2765,
234	      "winogrande_acc": 0.5162,
235	      "mmlu_acc": 0.2614,
236	      "gsm8k_exact_match": 0.019
237	    },
238	    "conclusion": "success"
239	  },
240	  "bce_30_s42_uniform_eval": {
241	    "metrics": {
242	      "ppl": 15.7069,
243	      "arc_challenge": 0.3319,
244	      "winogrande": 0.618,
245	      "mmlu": 0.4237,
246	      "gsm8k": 0.0394,
247	      "hellaswag": 0.6156,
248	      "piqa": 0.741
249	    },
250	    "conclusion": "success"
251	  },
252	  "bce_30pct_s42_eval": {
253	    "metrics": {
254	      "wikitext2_ppl": 11.2445,
255	      "arc_challenge_acc": 0.3848,
256	      "arc_challenge_acc_norm": 0.4121,
257	      "winogrande_acc": 0.6598,
258	      "mmlu_acc": 0.3633,
259	      "gsm8k_exact_match": 0.0599,
260	      "gsm8k_exact_match_strict": 0.0538,
261	      "sparsity_target": 0.3,
262	      "allocation": "global_topk",
263	      "training_sparsity_native": 0.042,
264	      "eval_wall_time_sec": 2275.8
265	    },
266	    "conclusion": "negative"
267	  },
268	  "eval_bce_v3_s42": {
269	    "metrics": {
270	      "dense_ppl": 6.12,
271	      "predictor_hard_mask_ppl": 22.51,
272	      "teal_sparse_ppl": 27.97,
273	      "model_level_sparsity": 0.5,
274	      "arc_challenge_acc": 0.2048,
275	      "arc_challenge_acc_norm": 0.2398,
276	      "arc_challenge_acc_norm_stderr": 0.0125,
277	      "winogrande_acc": 0.5059,
278	      "winogrande_acc_stderr": 0.0141,
279	      "mmlu_acc": 0.3002,
280	      "mmlu_acc_stderr": 0.0038,
281	      "gsm8k_exact_match": 0.0485,
282	      "gsm8k_exact_match_strict": 0.0425,
283	      "gsm8k_exact_match_stderr": 0.0059
284	    },
285	    "conclusion": "success"
286	  },
287	  "mse30_s42_train": {
288	    "metrics": {
289	      "final_mse_loss": 0.005735,
290	      "final_constraint_loss": 0.007294,
291	      "final_total_loss": 0.013,
292	      "final_sparsity": 0.277,
293	      "final_tau": 0.1,
294	      "final_lambda": 1000,
295	      "steps": 1000
296	    },
297	    "conclusion": "success"
298	  },
299	  "mse30_s42_eval_7task": {
300	    "metrics": {
301	      "wikitext2_ppl": 20.43,
302	      "arc_challenge_acc_norm": 0.3123,
303	      "winogrande_acc": 0.6038,
304	      "mmlu_acc": 0.3179,
305	      "gsm8k_exact_match": 0.0197,
306	      "hellaswag_acc_norm": 0.5248,
307	      "piqa_acc_norm": 0.6937
308	    },
309	    "conclusion": "success"
310	  },
311	  "mse30_s123": {
312	    "metrics": {
313	      "ppl": 17.7313,
314	      "sparsity": 0.273,
315	      "allocation": "uniform"
316	    },
317	    "conclusion": "success"
318	  },
319	  "mse30_s123_downstream": {
320	    "metrics": {
321	      "arc_challenge_acc": 0.3285,
322	      "arc_challenge_acc_norm": 0.3737,
323	      "winogrande_acc": 0.5699,
324	      "mmlu_acc": 0.2781,
325	      "gsm8k_exact_match": 0.0174,
326	      "hellaswag_acc": 0.4009,
327	      "hellaswag_acc_norm": 0.5358,
328	      "piqa_acc": 0.7106,
329	      "piqa_acc_norm": 0.7067,
330	      "boolq_acc": 0.6324
331	    },
332	    "conclusion": "success"
333	  },
334	  "mse30_s456": {
335	    "metrics": {
336	      "ppl": 17.3888,
337	      "sparsity": 0.28,
338	      "allocation": "uniform"
339	    },
340	    "conclusion": "success"
341	  },
342	  "mse30_s456_downstream": {
343	    "metrics": {
344	      "arc_challenge_acc_norm": 0.3882,
345	      "winogrande_acc": 0.6196,
346	      "mmlu_acc": 0.3264,
347	      "gsm8k_exact_match": 0.0311,
348	      "hellaswag_acc_norm": 0.6129,
349	      "piqa_acc_norm": 0.7383,
350	      "boolq_acc": 0.7034
351	    },
352	    "conclusion": "success"
353	  },
354	  "mse50_s42_train": {
355	    "metrics": {
356	      "final_loss": 0.0083,
357	      "final_sparsity": 0.539,
358	      "steps": 1000
359	    },
360	    "conclusion": "success"
361	  },
362	  "mse50_s42_eval_7task": {
363	    "metrics": {
364	      "wikitext2_ppl": 229.26,
365	      "arc_challenge_acc_norm": 0.25,
366	      "winogrande_acc": 0.5059,
367	      "mmlu_acc": 0.2379,
368	      "gsm8k_exact_match": 0.0159,
369	      "hellaswag_acc_norm": 0.2722,
370	      "piqa_acc_norm": 0.5577
371	    },
372	    "conclusion": "success"
373	  },
374	  "mse50_s123": {
375	    "metrics": {
376	      "final_loss": 185.0,
377	      "final_sparsity": 0.051,
378	      "note": "Native sparsity collapsed to 5.1% (target 50%). Eval PPL=15789 under forced 50% mask."
379	    },
380	    "conclusion": "negative"
381	  },
382	  "mse50_s123_eval_retry": {
383	    "metrics": {},
384	    "conclusion": "killed"
385	  },
386	  "c1_ablation_30pct_s42_eval_v2": {
387	    "metrics": {
388	      "wikitext2_ppl": 9.4463,
389	      "arc_challenge_acc_norm": 0.4027,
390	      "winogrande_acc": 0.674,
391	      "mmlu_acc": 0.4229,
392	      "gsm8k_exact_match": 0.0758
393	    },
394	    "conclusion": "success"
395	  },
396	  "eval_c1_retrain_30pct_s123": {
397	    "metrics": {
398	      "wikitext2_ppl": 8.84,
399	      "arc_challenge_acc_norm": 0.4471,
400	      "winogrande_acc": 0.6977,
401	      "mmlu_acc": 0.3992,
402	      "gsm8k_exact_match": 0.0682
403	    },
404	    "conclusion": "success"
405	  },
406	  "eval_c1_retrain_30pct_s456": {
407	    "metrics": {
408	      "wikitext2_ppl": 8.82,
409	      "arc_challenge_acc_norm": 0.4471,
410	      "winogrande_acc": 0.6993,
411	      "mmlu_acc": 0.4104,
412	      "gsm8k_exact_match": 0.066
413	    },
414	    "conclusion": "success"
415	  },
416	  "c1_ablation_eval_uniform": {
417	    "metrics": {
418	      "wikitext2_ppl": 11.9638,
419	      "arc_challenge_acc_norm": 0.3217,
420	      "winogrande_acc": 0.6314,
421	      "mmlu_acc": 0.2779,
422	      "gsm8k_exact_match": 0.0205,
423	      "sparsity_target": 0.5,
424	      "allocation": "uniform"
425	    },
426	    "conclusion": "success"
427	  },
428	  "kl30_s123_eval": {
429	    "metrics": {
430	      "wikitext2_ppl": 8.8308,
431	      "arc_challenge_acc_norm": 0.4531,
432	      "winogrande_acc": 0.6938,
433	      "mmlu_acc": 0.3944,
434	      "gsm8k_exact_match": 0.0751,
435	      "actual_sparsity": 0.3,
436	      "allocation": "uniform"
437	    },
438	    "conclusion": "success"
439	  },
440	  "kl30_s456_uniform_eval": {
441	    "metrics": {
442	      "mmlu": 0.4198,
443	      "ppl_uniform": 8.7947,
444	      "arc_challenge": 0.4505,
445	      "winogrande": 0.6875,
446	      "gsm8k": 0.0758
447	    },
448	    "conclusion": "success"
449	  },
450	  "jsd_30_s42": {
451	    "metrics": {
452	      "wikitext2_ppl": 8.884,
453	      "arc_challenge_acc_norm": 0.4445,
454	      "winogrande_acc": 0.7072,
455	      "mmlu_acc": 0.3825,
456	      "gsm8k_exact_match": 0.0925,
457	      "hellaswag_acc_norm": 0.7073,
458	      "piqa_acc_norm": 0.7508,
459	      "model_level_sparsity": 0.285
460	    },
461	    "conclusion": "success"
462	  },
463	  "jsd_30_s42_uniform_eval": {
464	    "metrics": {
465	      "ppl": 8.8848,
466	      "arc_challenge": 0.4437,
467	      "winogrande": 0.6977,
468	      "mmlu": 0.3857,
469	      "gsm8k": 0.0857,
470	      "hellaswag": 0.7063,
471	      "piqa": 0.7519
472	    },
473	    "conclusion": "success"
474	  },
475	  "jsd_30_s123": {
476	    "metrics": {
477	      "ppl": 8.9144,
478	      "sparsity": 0.296,
479	      "allocation": "uniform"
480	    },
481	    "conclusion": "success"
482	  },
483	  "jsd_30_s456": {
484	    "metrics": {
485	      "ppl": 8.9099,
486	      "sparsity": 0.296,
487	      "allocation": "uniform"
488	    },
489	    "conclusion": "success"
490	  },
491	  "jsd_50pct_s42": {
492	    "metrics": {
493	      "ppl_wikitext2": 12.54,
494	      "vs_forward_kl": "+0.75 (+6.4%)",
495	      "sparsity": 0.5
496	    },
497	    "conclusion": "killed"
498	  },
499	  "reverse_kl_30_s42": {
500	    "metrics": {
501	      "wikitext2_ppl": 9.31,
502	      "arc_challenge_acc_norm": 0.4317,
503	      "winogrande_acc": 0.6938,
504	      "mmlu_acc": 0.3744,
505	      "gsm8k_exact_match": 0.0697,
506	      "hellaswag_acc_norm": 0.6972,
507	      "piqa_acc_norm": 0.7459
508	    },
509	    "conclusion": "success"
510	  },
511	  "reverse_kl_30_s42_uniform_eval": {
512	    "metrics": {
513	      "arc_challenge_acc_norm": 0.4283,
514	      "winogrande_acc": 0.7009,
515	      "mmlu_acc": 0.3749,
516	      "gsm8k_exact_match": 0.0697,
517	      "hellaswag_acc_norm": 0.6969,
518	      "piqa_acc_norm": 0.7459
519	    },
520	    "conclusion": "success"
521	  },
522	  "reverse_kl_50pct_s42": {
523	    "metrics": {
524	      "ppl_wikitext2": 12.8,
525	      "vs_forward_kl": "+1.01 (+8.6%)",
526	      "sparsity": 0.5
527	    },
528	    "conclusion": "killed"
529	  },
530	  "ste_baseline_s42": {
531	    "metrics": {
532	      "true_dense_ppl": 6.12,
533	      "predictor_hard_mask_ppl": 8.18,
534	      "teal_sparse_ppl": 15.77,
535	      "model_level_sparsity": 0.47,
536	      "ppl_increase_vs_true_dense_pct": 157.7,
537	      "eval_seq_len": 2048,
538	      "calibration_samples": 32,
539	      "eval_dataset": "wikitext-2",
540	      "per_token_sparsity": 0.47,
541	      "lambda_stats": {
542	        "steps_70_130_mean": 66.4,
543	        "steps_70_130_std": 94.87,
544	        "first_500_mean": 688.07,
545	        "first_500_std": 440.57,
546	        "last_500_mean": 965.69,
547	        "last_500_std": 141.59,
548	        "overall_mean": 826.88,
549	        "overall_std": 354.23
550	      }
551	    },
552	    "conclusion": "success"
553	  },
554	  "bce_gumbel_no_penalty_s42": {
555	    "metrics": {
556	      "training_bce_loss": 0.6307,
557	      "training_sparsity": 0.383,
558	      "wikitext2_ppl": 32.22,
559	      "training_time_seconds": 977.6
560	    },
561	    "conclusion": "success"
562	  },
563	  "bce_gumbel_lagrangian_isolation": {
564	    "metrics": {
565	      "lr_1e4_ppl": 42.99,
566	      "lr_1e3_ppl": 48.4,
567	      "lr_3e3_ppl": 38.02,
568	      "lr_1e4_bce_loss": 0.7158,
569	      "lr_1e3_bce_loss": 0.6781,
570	      "lr_3e3_bce_loss": 0.6632,
571	      "lr_1e4_sparsity": 0.514,
572	      "lr_1e3_sparsity": 0.506,
573	      "lr_3e3_sparsity": 0.504,
574	      "best_ppl": 38.02,
575	      "best_lr": "3e-3",
576	      "kl_baseline_ppl": 11.79,
577	      "gap_vs_kl": 26.23
578	    },
579	    "conclusion": "success"
580	  },
581	  "bce_ste_s42": {
582	    "metrics": {
583	      "training_final_loss": 0.641,
584	      "training_final_bce": 0.6398,
585	      "training_final_sparsity": 0.512,
586	      "wikitext2_ppl": 60.54,
587	      "arc_challenge_acc_norm": 0.2321,
588	      "winogrande_acc": 0.5185,
589	      "mmlu_acc": 0.2898,
590	      "gsm8k_exact_match": 0.0182,
591	      "hellaswag_acc_norm": 0.3446,
592	      "piqa_acc_norm": 0.6273,
593	      "model_level_sparsity": 0.495
594	    },
595	    "conclusion": "negative"
596	  },
597	  "perlayer_kl_30_s42_v6": {
598	    "metrics": {
599	      "steps": 10000
600	    },
601	    "conclusion": "success"
602	  },
603	  "perlayer_kl_30_s123_v4": {
604	    "metrics": {
605	      "final_avg_kl": 0.0114,
606	      "final_tau": 0.1,
607	      "steps": 10000
608	    },
609	    "conclusion": "success"
610	  },
611	  "perlayer_kl_30_s456_v3": {
612	    "metrics": {},
613	    "conclusion": "killed"
614	  },
615	  "perlayer_kl_50_s42": {
616	    "metrics": {
617	      "avg_kl": 0.0282,
618	      "sparsity_mean": 0.496,
619	      "wikitext2_ppl": 34.85,
620	      "training_steps": 10000,
621	      "training_duration_s": 18216
622	    },
623	    "conclusion": "negative"
624	  },
625	  "perlayer_kl_50_s42_ppl": {
626	    "metrics": {},
627	    "conclusion": "killed"
628	  },
629	  "perlayer_kl_k4_s42": {
630	    "metrics": {},
631	    "conclusion": "success"
632	  },
633	  "perlayer_kl_k4_s123": {
634	    "metrics": {
635	      "wikitext2_ppl": 8.8897,
636	      "arc_challenge_acc_norm": 0.4053,
637	      "winogrande_acc": 0.6701,
638	      "mmlu_acc": 0.4118,
639	      "gsm8k_exact_match": 0.0781,
640	      "hellaswag_acc_norm": 0.6668,
641	      "piqa_acc_norm": 0.7448,
642	      "boolq_acc": 0.5914
643	    },
644	    "conclusion": "killed"
645	  },
646	  "perlayer_kl_k4_s456": {
647	    "metrics": {
648	      "wikitext2_ppl": 8.8828,
649	      "arc_challenge_acc_norm": 0.3857,
650	      "winogrande_acc": 0.6701,
651	      "mmlu_acc": 0.4351,
652	      "gsm8k_exact_match": 0.0788,
653	      "hellaswag_acc_norm": 0.6821,
654	      "piqa_acc_norm": 0.7503,
655	      "boolq_acc": 0.7092
656	    },
657	    "conclusion": "killed"
658	  },
659	  "perlayer_kl_k4_50_s42": {
660	    "metrics": {},
661	    "conclusion": "success"
662	  },
663	  "perlayer_kl_k4_50_s42_ppl": {
664	    "metrics": {},
665	    "conclusion": "failed"
666	  },
667	  "perlayer_kl_k4_50_s42_ppl_v2": {
668	    "metrics": {
669	      "wikitext2_ppl": 44.2321,
670	      "sparsity_actual": 0.495,
671	      "seq_len": 2048,
672	      "num_sequences": 141
673	    },
674	    "conclusion": "negative"
675	  },
676	  "perlayer_kl_k4_s42_downstream": {
677	    "metrics": {
678	      "arc_challenge_acc_norm": 0.4096,
679	      "winogrande_acc": 0.6669,
680	      "mmlu_acc": 0.4353,
681	      "gsm8k_exact_match": 0.0516,
682	      "hellaswag_acc_norm": 0.6849,
683	      "piqa_acc_norm": 0.7399,
684	      "boolq_acc": 0.7318
685	    },
686	    "conclusion": "success"
687	  },
688	  "perlayer_kl_k4_s42_ppl": {
689	    "metrics": {
690	      "wikitext2_ppl": 8.8932,
691	      "sparsity_mean": 0.296,
692	      "ppl_k1_baseline": 9.05,
693	      "ppl_e2e_kl_baseline": 8.81,
694	      "delta_vs_k1": -0.16,
695	      "delta_vs_e2e_kl": 0.08
696	    },
697	    "conclusion": "negative"
698	  },
699	  "perlayer_kl_k2_s42": {
700	    "metrics": {
701	      "final_avg_kl": 0.0358,
702	      "final_avg_sparsity": 0.268,
703	      "wall_time_s": 3841.2,
704	      "training_steps": 1000,
705	      "note": "training only, PPL eval not yet run"
706	    },
707	    "conclusion": "success"
708	  },
709	  "perlayer_kl_k2_s42_eval": {
710	    "metrics": {
711	      "wikitext2_ppl": 10.7958,
712	      "arc_challenge_acc_norm": 0.3985,
713	      "winogrande_acc": 0.6322,
714	      "mmlu_acc": 0.4172,
715	      "gsm8k_exact_match": 0.0296,
716	      "hellaswag_acc_norm": 0.6773,
717	      "piqa_acc_norm": 0.7356
718	    },
719	    "conclusion": "success"
720	  },
721	  "perlayer_kl_k2_s123": {
722	    "metrics": {},
723	    "conclusion": "success"
724	  },
725	  "perlayer_kl_k2_s123_eval": {
726	    "metrics": {
727	      "wikitext2_ppl": 10.8835,
728	      "arc_challenge_acc_norm": 0.4078,
729	      "winogrande_acc": 0.614,
730	      "mmlu_acc": 0.3789,
731	      "gsm8k_exact_match": 0.0326,
732	      "hellaswag_acc_norm": 0.6605,
733	      "piqa_acc_norm": 0.741
734	    },
735	    "conclusion": "success"
736	  },
737	  "perlayer_kl_k2_s456": {
738	    "metrics": {},
739	    "conclusion": "success"
740	  },
741	  "perlayer_kl_k2_s456_eval": {
742	    "metrics": {
743	      "wikitext2_ppl": 10.5826,
744	      "arc_challenge_acc_norm": 0.384,
745	      "winogrande_acc": 0.6488,
746	      "mmlu_acc": 0.3542,
747	      "gsm8k_exact_match": 0.0205,
748	      "hellaswag_acc_norm": 0.659,
749	      "piqa_acc_norm": 0.728
750	    },
751	    "conclusion": "success"
752	  },
753	  "perlayer_kl_k8_s42": {
754	    "metrics": {
755	      "wikitext2_ppl": 8.97,
756	      "final_avg_kl": 0.0983,
757	      "final_avg_sparsity": 0.281,
758	      "wall_time_s": 1894.1
759	    },
760	    "conclusion": "success"
761	  },
762	  "perlayer_kl_k8_s42_eval": {
763	    "metrics": {
764	      "wikitext2_ppl": 8.9704,
765	      "arc_challenge_acc_norm": 0.4104,
766	      "winogrande_acc": 0.674,
767	      "mmlu_acc": 0.398,
768	      "gsm8k_exact_match": 0.0561,
769	      "hellaswag_acc_norm": 0.6919,
770	      "piqa_acc_norm": 0.7612
771	    },
772	    "conclusion": "success"
773	  },
774	  "perlayer_kl_k8_s123": {
775	    "metrics": {
776	      "avg_kl": 0.0997,
777	      "avg_sparsity": 0.286,
778	      "final_kl": 0.0825,
779	      "avg_lambda": 2182.2,
780	      "steps": 1000
781	    },
782	    "conclusion": "success"
783	  },
784	  "perlayer_kl_k8_s123_eval": {
785	    "metrics": {
786	      "wikitext2_ppl": 9.0648,
787	      "arc_challenge_acc_norm": 0.4155,
788	      "winogrande_acc": 0.6993,
789	      "mmlu_acc": 0.4042,
790	      "gsm8k_exact_match": 0.0682,
791	      "hellaswag_acc_norm": 0.6997,
792	      "piqa_acc_norm": 0.7508
793	    },
794	    "conclusion": "success"
795	  },
796	  "perlayer_kl_k8_s456": {
797	    "metrics": {
798	      "avg_kl": 0.0982,
799	      "avg_sparsity": 0.285,
800	      "final_kl": 0.1079,
801	      "avg_lambda": 2244.28,
802	      "steps": 1000
803	    },
804	    "conclusion": "success"
805	  },
806	  "perlayer_kl_k8_s456_eval": {
807	    "metrics": {
808	      "wikitext2_ppl": 8.9515,
809	      "arc_challenge_acc_norm": 0.3951,
810	      "winogrande_acc": 0.6875,
811	      "mmlu_acc": 0.4105,
812	      "gsm8k_exact_match": 0.0811,
813	      "hellaswag_acc_norm": 0.6783,
814	      "piqa_acc_norm": 0.7399,
815	      "sparsity": 0.298
816	    },
817	    "conclusion": "success"
818	  },
819	  "perlayer_kl_k16_s42": {
820	    "metrics": {
821	      "error": "argparse failure: unrecognized arguments --loss_type kl_normalized",
822	      "training_loss": null
823	    },
824	    "conclusion": "failed"
825	  },
826	  "perlayer_kl_k16_s42_eval_final": {
827	    "metrics": {},
828	    "conclusion": "failed"
829	  },
830	  "perlayer_kl_k16_eval_final2": {
831	    "metrics": {
832	      "wikitext2_ppl": 8.6737,
833	      "arc_challenge_acc_norm": 0.4104,
834	      "winogrande_acc": 0.6843,
835	      "mmlu_acc": 0.4403,
836	      "gsm8k_exact_match": 0.0811,
837	      "hellaswag_acc_norm": 0.6963,
838	      "piqa_acc_norm": 0.759
839	    },
840	    "conclusion": "success"
841	  },
842	  "perlayer_kl_k16_s123": {
843	    "metrics": {
844	      "avg_kl": 0.1617,
845	      "avg_sparsity": 0.287,
846	      "final_kl": 0.1436,
847	      "wall_time_s": 1982.8
848	    },
849	    "conclusion": "success"
850	  },
851	  "perlayer_kl_k16_s123_eval": {
852	    "metrics": {
853	      "wikitext2_ppl": 8.6939,
854	      "arc_challenge_acc_norm": 0.4317,
855	      "winogrande_acc": 0.6772,
856	      "mmlu_acc": 0.3996,
857	      "gsm8k_exact_match": 0.0986,
858	      "hellaswag_acc_norm": 0.705,
859	      "piqa_acc_norm": 0.7481
860	    },
861	    "conclusion": "success"
862	  },
863	  "perlayer_kl_k16_s456": {
864	    "metrics": {},
865	    "conclusion": "failed"
866	  },
867	  "perlayer_kl_k16_s456_eval": {
868	    "metrics": {
869	      "ppl_wikitext2": 8.655,
870	      "arc_challenge_acc_norm": 0.4155,
871	      "winogrande_acc": 0.6946,
872	      "mmlu_acc": 0.3873,
873	      "gsm8k_exact_match": 0.0766,
874	      "hellaswag_acc_norm": 0.7015,
875	      "piqa_acc_norm": 0.7437
876	    },
877	    "conclusion": "success"
878	  },
879	  "perlayer_kl_k16_s456_v2": {
880	    "metrics": {
881	      "avg_kl": 0.1565,
882	      "avg_sparsity": 0.287,
883	      "final_kl": 0.1611,
884	      "wall_time_s": 1977.9
885	    },
886	    "conclusion": "success"
887	  },
888	  "mistral_kl30_s42": {
889	    "metrics": {
890	      "kl_per_token_ppl": 6.048,
891	      "kl_teal_global_ppl": 6.7733,
892	      "teal_baseline_ppl": 8.3807,
893	      "dense_ppl": 5.5238,
894	      "kl_advantage_ratio": 1.386,
895	      "ppl_vs_dense_pct": 9.5
896	    },
897	    "conclusion": "success"
898	  },
899	  "mistral_kl30_s123": {
900	    "metrics": {
901	      "training_final_loss": 0.0996,
902	      "training_final_sparsity": 0.281,
903	      "wikitext2_ppl": 7.1491,
904	      "arc_challenge_acc_norm": 0.378,
905	      "winogrande_acc": 0.7017,
906	      "mmlu_acc": 0.4423,
907	      "gsm8k_exact_match": 0.0773,
908	      "hellaswag_acc_norm": 0.6961,
909	      "piqa_acc_norm": 0.7459
910	    },
911	    "conclusion": "success"
912	  },
913	  "mistral_kl30_s456": {
914	    "metrics": {
915	      "training_final_loss": 0.105,
916	      "training_final_sparsity": 0.281,
917	      "wikitext2_ppl": 6.8752,
918	      "arc_challenge_acc_norm": 0.4684,
919	      "winogrande_acc": 0.7143,
920	      "mmlu_acc": 0.4161,
921	      "gsm8k_exact_match": 0.0697,
922	      "hellaswag_acc_norm": 0.705,
923	      "piqa_acc_norm": 0.7448
924	    },
925	    "conclusion": "success"
926	  },
927	  "mistral_teal30_downstream": {
928	    "metrics": {
929	      "wikitext2_ppl": 8.3807,
930	      "arc_challenge_acc_norm": 0.4113,
931	      "winogrande_acc": 0.6354,
932	      "mmlu_acc": 0.4348,
933	      "gsm8k_exact_match": 0.1592,
934	      "hellaswag_acc_norm": 0.6011,
935	      "piqa_acc_norm": 0.7214
936	    },
937	    "conclusion": "success"
938	  },
939	  "mistral_teal30_baseline": {
940	    "metrics": {
941	      "wikitext2_ppl": 8.3807,
942	      "model": "Mistral-7B-v0.3",
943	      "condition": "teal_vanilla_30pct",
944	      "sparsity": 0.3,
945	      "allocation": "uniform",
946	      "ppl_increase_vs_dense": 2.8569
947	    },
948	    "conclusion": "success"
949	  },
950	  "mistral_kl50_teal_global": {
951	    "metrics": {
952	      "wikitext2_ppl": 8.6489,
953	      "model": "Mistral-7B-v0.3",
954	      "condition": "kl_teal_global_50pct",
955	      "sparsity": 0.5,
956	      "allocation": "uniform",
957	      "ppl_increase_vs_dense": 3.1251
958	    },
959	    "conclusion": "success"
960	  },
961	  "mistral_teal50_baseline": {
962	    "metrics": {
963	      "teal_baseline_ppl": 18.3061,
964	      "dense_ppl": 5.5238,
965	      "teal_vs_dense_ratio": 3.31
966	    },
967	    "conclusion": "success"
968	  },
969	  "mistral_teal50_downstream": {
970	    "metrics": {
971	      "wikitext2_ppl": 18.3061,
972	      "arc_challenge_acc_norm": 0.2457,
973	      "winogrande_acc": 0.5091,
974	      "mmlu_acc": 0.2635,
975	      "gsm8k_exact_match": 0.0341,
976	      "hellaswag_acc_norm": 0.3603,
977	      "piqa_acc_norm": 0.6045
978	    },
979	    "conclusion": "success"
980	  },
981	  "mistral_kl70_teal_global": {
982	    "metrics": {
983	      "wikitext2_ppl": 13.3254,
984	      "model": "Mistral-7B-v0.3",
985	      "condition": "kl_teal_global_70pct",
986	      "sparsity": 0.7,
987	      "allocation": "uniform",
988	      "ppl_increase_vs_dense": 7.8016
989	    },
990	    "conclusion": "success"
991	  },
992	  "mistral_teal70_baseline": {
993	    "metrics": {
994	      "wikitext2_ppl": 61.716,
995	      "model": "Mistral-7B-v0.3",
996	      "condition": "teal_vanilla_70pct",
997	      "sparsity": 0.7,
998	      "allocation": "uniform",
999	      "ppl_increase_vs_dense": 56.1922
1000	    },
1001	    "conclusion": "success"
1002	  },
1003	  "mistral_kl70_s42": {
1004	    "metrics": {
1005	      "kl_per_token_ppl": 9.1086,
1006	      "kl_teal_global_ppl": 13.3254,
1007	      "teal_baseline_ppl": 61.716,
1008	      "dense_ppl": 5.5238,
1009	      "kl_advantage_ratio": 6.77,
1010	      "final_loss": 0.3945,
1011	      "actual_sparsity": 0.682
1012	    },
1013	    "conclusion": "success"
1014	  },
1015	  "lm_eval_mistral_dense": {
1016	    "metrics": {
1017	      "arc_challenge_acc_norm": 0.6024,
1018	      "winogrande_acc": 0.7869,
1019	      "mmlu_acc": 0.6244,
1020	      "gsm8k_exact_match": 0.3654,
1021	      "model": "Mistral-7B-v0.3",
1022	      "condition": "dense",
1023	      "server": "westd-34887"
1024	    },
1025	    "conclusion": "success"
1026	  },
1027	  "mistral_dense_hellaswag_piqa": {
1028	    "metrics": {
1029	      "hellaswag_acc_norm": 0.832,
1030	      "piqa_acc_norm": 0.8188
1031	    },
1032	    "conclusion": "success"
1033	  },
1034	  "mistral_dense_ppl": {
1035	    "metrics": {
1036	      "wikitext2_ppl": 5.5238,
1037	      "model": "Mistral-7B-v0.3",
1038	      "condition": "dense",
1039	      "sparsity": 0
1040	    },
1041	    "conclusion": "success"
1042	  },
1043	  "qwen14b_kl30_s42": {
1044	    "metrics": {
1045	      "dense_ppl": 5.18,
1046	      "predictor_hard_mask_ppl": 6.8,
1047	      "teal_global_ppl": 7.62,
1048	      "ppl_ratio_hard_mask": 1.31,
1049	      "ppl_ratio_teal": 1.47,
1050	      "final_loss": 0.3398,
1051	      "training_sparsity": 0.281,
1052	      "teal_sparsity": 0.3,
1053	      "lambda": 5000,
1054	      "steps": 1000
1055	    },
1056	    "conclusion": "success"
1057	  },
1058	  "qwen14b_kl30_s42_eval": {
1059	    "metrics": {
1060	      "wikitext2_ppl": 7.6232,
1061	      "arc_challenge_acc_norm": 0.5717,
1062	      "winogrande_acc": 0.7206,
1063	      "mmlu_acc": 0.6372,
1064	      "gsm8k_exact_match": 0.4882
1065	    },
1066	    "conclusion": "success"
1067	  },
1068	  "qwen14b_kl30_s42_eval_uniform": {
1069	    "metrics": {},
1070	    "conclusion": "failed"
1071	  },
1072	  "qwen14b_kl30_s42_eval_uniform_v2": {
1073	    "metrics": {},
1074	    "conclusion": "killed"
1075	  },
1076	  "qwen14b_kl30_s42_eval_uniform_v3": {
1077	    "metrics": {
1078	      "wikitext2_ppl": 7.8715,
1079	      "arc_challenge_acc": 0.5051,
1080	      "arc_challenge_acc_norm": 0.5495,
1081	      "winogrande_acc": 0.7127,
1082	      "mmlu_acc": 0.648,
1083	      "hellaswag_acc_norm": 0.7268,
1084	      "piqa_acc_norm": 0.7476,
1085	      "actual_sparsity": 0.296
1086	    },
1087	    "conclusion": "success"
1088	  },
1089	  "qwen14b_teal30_eval": {
1090	    "metrics": {
1091	      "wikitext2_ppl": 8.7332,
1092	      "arc_challenge_acc_norm": 0.5683,
1093	      "winogrande_acc": 0.7269,
1094	      "mmlu_acc": 0.7183,
1095	      "gsm8k_exact_match": 0.4951
1096	    },
1097	    "conclusion": "success"
1098	  },
1099	  "qwen14b_bce30_s42_eval": {
1100	    "metrics": {
1101	      "wikitext2_ppl": 8.7634,
1102	      "arc_challenge_acc_norm": 0.5759,
1103	      "winogrande_acc": 0.7261,
1104	      "mmlu_acc": 0.7167,
1105	      "gsm8k_exact_match": 0.5307
1106	    },
1107	    "conclusion": "negative"
1108	  },
1109	  "qwen14b_kl30_uniform_eval": {
1110	    "metrics": {},
1111	    "conclusion": "failed"
1112	  },
1113	  "qwen14b_kl30_uniform_eval_4task": {
1114	    "metrics": {
1115	      "wikitext2_ppl": 7.63,
1116	      "mmlu_acc": 0.6449,
1117	      "arc_challenge_acc_norm": 0.5444,
1118	      "winogrande_acc": 0.7245
1119	    },
1120	    "conclusion": "killed"
1121	  },
1122	  "qwen14b_teal30_uniform_eval": {
1123	    "metrics": {},
1124	    "conclusion": "failed"
1125	  },
1126	  "qwen14b_teal30_uniform_eval_4task": {
1127	    "metrics": {
1128	      "wikitext2_ppl": 8.01,
1129	      "mmlu_acc": 0.6634,
1130	      "arc_challenge_acc_norm": 0.5529,
1131	      "winogrande_acc": 0.6985
1132	    },
1133	    "conclusion": "killed"
1134	  },
1135	  "qwen14b_dense_4task": {
1136	    "metrics": {},
1137	    "conclusion": "failed"
1138	  },
1139	  "qwen14b_dense_4task_v2": {
1140	    "metrics": {
1141	      "wikitext2_ppl": 5.1854,
1142	      "arc_challenge_acc_norm": 0.6758,
1143	      "winogrande_acc": 0.8106,
1144	      "mmlu_acc": 0.7977
1145	    },
1146	    "conclusion": "success"
1147	  },
1148	  "qwen14b_dense_baseline": {
1149	    "metrics": {
1150	      "ppl": 5.1854,
1151	      "arc_challenge": 0.6758,
1152	      "winogrande": 0.8106,
1153	      "mmlu": 0.7977,
1154	      "gsm8k": 0.8757
1155	    },
1156	    "conclusion": "success"
1157	  },
1158	  "qwen14b_kl30_s123_eval_v5": {
1159	    "metrics": {
1160	      "wikitext2_ppl": 7.9367,
1161	      "arc_challenge_acc_norm": 0.541,
1162	      "winogrande_acc": 0.7403,
1163	      "hellaswag_acc_norm": 0.7287,
1164	      "piqa_acc_norm": 0.765,
1165	      "mmlu_acc": 0.6234,
1166	      "actual_sparsity": 0.296
1167	    },
1168	    "conclusion": "success"
1169	  },
1170	  "qwen14b_kl30_s456_eval_v3": {
1171	    "metrics": {
1172	      "wikitext2_ppl": 7.8992,
1173	      "arc_challenge_acc_norm": 0.5145,
1174	      "winogrande_acc": 0.7316,
1175	      "hellaswag_acc_norm": 0.7249,
1176	      "piqa_acc_norm": 0.7677,
1177	      "mmlu_acc": 0.6351,
1178	      "actual_sparsity": 0.297
1179	    },
1180	    "conclusion": "success"
1181	  },
1182	  "qwen14b_kl30_s42_gsm8k_uniform": {
1183	    "metrics": {
1184	      "gsm8k_exact_match": 0.3548
1185	    },
1186	    "conclusion": "success"
1187	  },
1188	  "qwen14b_kl30_s42_gsm8k_v2": {
1189	    "metrics": {
1190	      "gsm8k_exact_match": 0.3571,
1191	      "gsm8k_exact_match_strict": 0.3541,
1192	      "gsm8k_exact_match_stderr": 0.0132,
1193	      "actual_sparsity": 0.296,
1194	      "sample_len": 1319
1195	    },
1196	    "conclusion": "success"
1197	  },
1198	  "qwen14b_teal30_uniform_gsm8k": {
1199	    "metrics": {
1200	      "gsm8k_exact_match": 0.5208,
1201	      "gsm8k_exact_match_strict": 0.5208,
1202	      "gsm8k_exact_match_flexible": 0.5208,
1203	      "gsm8k_exact_match_stderr": 0.01376,
1204	      "actual_sparsity": 0.293,
1205	      "sample_len": 1319
1206	    },
1207	    "conclusion": "success"
1208	  },
1209	  "qwen14b_kl30_s123_gsm8k": {
1210	    "metrics": {
1211	      "gsm8k_exact_match": 0.3442,
1212	      "gsm8k_exact_match_strict": 0.3434,
1213	      "actual_sparsity": 0.297
1214	    },
1215	    "conclusion": "killed"
1216	  },
1217	  "qwen14b_kl30_s456_gsm8k": {
1218	    "metrics": {
1219	      "gsm8k_exact_match": 0.2608,
1220	      "gsm8k_exact_match_stderr": 0.01209,
1221	      "gsm8k_exact_match_strict": 0.2547,
1222	      "gsm8k_exact_match_strict_stderr": 0.012,
1223	      "actual_sparsity": 0.297
1224	    },
1225	    "conclusion": "success"
1226	  },
1227	  "qwen14b_kl30_global_hspiqa": {
1228	    "metrics": {
1229	      "hellaswag_acc_norm": 0.7501,
1230	      "piqa_acc_norm": 0.7737
1231	    },
1232	    "conclusion": "success"
1233	  },
1234	  "qwen14b_teal30_global_hspiqa": {
1235	    "metrics": {
1236	      "hellaswag_acc_norm": 0.7051,
1237	      "piqa_acc_norm": 0.747
1238	    },
1239	    "conclusion": "success"
1240	  },
1241	  "qwen14b_kl30_uniform_hspiqa": {
1242	    "metrics": {
1243	      "hellaswag_acc_norm": 0.7266,
1244	      "piqa_acc_norm": 0.7514
1245	    },
1246	    "conclusion": "success"
1247	  },
1248	  "qwen14b_teal30_uniform_hspiqa_v2": {
1249	    "metrics": {
1250	      "hellaswag_acc": 0.4936,
1251	      "hellaswag_acc_norm": 0.6756,
1252	      "piqa_acc": 0.7443,
1253	      "piqa_acc_norm": 0.7427
1254	    },
1255	    "conclusion": "success"
1256	  },
1257	  "latency_benchmark": {
1258	    "metrics": {
1259	      "gpu_model": "NVIDIA RTX PRO 6000 Blackwell Server Edition",
1260	      "dtype": "float16",
1261	      "attn": "flash_attention_2",
1262	      "batch": 1,
1263	      "seq_len": 2048,
1264	      "warmup": 10,
1265	      "iters": 100,
1266	      "dense_ms": 119.11,
1267	      "dense_std": 0.57,
1268	      "dense_tokens_per_s": 17194.5,
1269	      "kl_30pct_ms": 126.64,
1270	      "kl_30pct_std": 0.7,
1271	      "kl_30pct_tokens_per_s": 16171.8,
1272	      "kl_30pct_speedup": 0.941,
1273	      "kl_50pct_ms": 126.78,
1274	      "kl_50pct_std": 0.31,
1275	      "kl_50pct_tokens_per_s": 16154.2,
1276	      "kl_50pct_speedup": 0.939,
1277	      "comp_30pct_ms": 129.94,
1278	      "comp_30pct_std": 0.75,
1279	      "comp_30pct_tokens_per_s": 15761.4,
1280	      "comp_30pct_speedup": 0.917,
1281	      "comp_50pct_ms": 129.71,
1282	      "comp_50pct_std": 0.53,
1283	      "comp_50pct_tokens_per_s": 15788.8,
1284	      "comp_50pct_speedup": 0.918,
1285	      "predictor_overhead_ms": 3.17,
1286	      "predictor_overhead_pct": 2.7,
1287	      "per_layer_predictor_ms": 0.099,
1288	      "dense_ffn_per_layer_ms": 2.427,
1289	      "sparse_ffn_pred_per_layer_ms": 2.686,
1290	      "compensation_overhead_ms": 3.3
1291	    },
1292	    "conclusion": "success"
1293	  },
1294	  "c4_ood_kl30_s42": {
1295	    "metrics": {
1296	      "c4_ppl": 16.0458,
1297	      "allocation": "global_topk",
1298	      "sparsity": 0.3,
1299	      "model": "llama-3.1-8b",
1300	      "eval_sequences": 132,
1301	      "seq_len": 2048
1302	    },
1303	    "conclusion": "success"
1304	  },
1305	  "c4_ood_kl30_s42_v2": {
1306	    "metrics": {
1307	      "c4_ppl": 16.0401,
1308	      "allocation": "global_topk",
1309	      "sparsity": 0.3,
1310	      "model": "llama-3.1-8b",
1311	      "seed": 42
1312	    },
1313	    "conclusion": "success"
1314	  },
1315	  "c4_ood_kl30_s123": {
1316	    "metrics": {},
1317	    "conclusion": "killed"
1318	  },
1319	  "c4_ood_kl30_s123_v2": {
1320	    "metrics": {
1321	      "c4_ppl": 16.0259,
1322	      "allocation": "global_topk",
1323	      "sparsity": 0.3,
1324	      "model": "llama-3.1-8b",
1325	      "eval_sequences": 132,
1326	      "seq_len": 2048
1327	    },
1328	    "conclusion": "success"
1329	  },
1330	  "eval_c4_ood_kl50": {
1331	    "metrics": {
1332	      "dense_ppl": 9.2075,
1333	      "kl_50_global_ppl": 18.401,
1334	      "teal_50_ppl": 38.7503,
1335	      "kl_vs_dense_ratio": 2,
1336	      "teal_vs_dense_ratio": 4.21
1337	    },
1338	    "conclusion": "success"
1339	  },
1340	  "c4_ood_downstream_kl30": {
1341	    "metrics": {
1342	      "arc_challenge_acc_norm": 0.4036,
1343	      "winogrande_acc": 0.693,
1344	      "mmlu_acc": 0.4137,
1345	      "gsm8k_exact_match": 0.0629,
1346	      "hellaswag_acc_norm": 0.7074,
1347	      "piqa_acc_norm": 0.7399,
1348	      "model_level_sparsity": 0.295
1349	    },
1350	    "conclusion": "success"
1351	  },
1352	  "c4_ood_kl30_uniform_s42": {
1353	    "metrics": {
1354	      "c4_ppl": 18.2211,
1355	      "allocation": "uniform",
1356	      "sparsity": 0.296,
1357	      "seed": 42
1358	    },
1359	    "conclusion": "success"
1360	  },
1361	  "c4_ood_kl30_uniform_s123": {
1362	    "metrics": {
1363	      "c4_ppl": 16.3686,
1364	      "allocation": "uniform",
1365	      "sparsity": 0.3,
1366	      "seed": 123
1367	    },
1368	    "conclusion": "success"
1369	  },
1370	  "c4_ood_kl30_uniform_s456": {
1371	    "metrics": {
1372	      "c4_ppl": 16.3551,
1373	      "allocation": "uniform",
1374	      "sparsity": 0.3,
1375	      "seed": 456
1376	    },
1377	    "conclusion": "success"
1378	  },
1379	  "c4_kl30_s42_eval": {
1380	    "metrics": {
1381	      "wikitext2_ppl": 11.554,
1382	      "arc_challenge_acc_norm": 0.4309,
1383	      "winogrande_acc": 0.6867,
1384	      "mmlu_acc": 0.3995,
1385	      "gsm8k_exact_match": 0.0409,
1386	      "hellaswag_acc_norm": 0.6924,
1387	      "piqa_acc_norm": 0.7503,
1388	      "sparsity": 0.295
1389	    },
1390	    "conclusion": "success"
1391	  },
1392	  "constraint_protect_late_kl30_s42": {
1393	    "metrics": {
1394	      "wikitext2_ppl": 9.2638,
1395	      "arc_challenge_acc_norm": 0.4241,
1396	      "mmlu_acc": 0.4066,
1397	      "gsm8k_exact_match": 0.0652
1398	    },
1399	    "conclusion": "killed"
1400	  },
1401	  "constraint_remove_valley_kl30_s42": {
1402	    "metrics": {
1403	      "wikitext2_ppl": 8.7592,
1404	      "arc_challenge_acc_norm": 0.3933,
1405	      "mmlu_acc": 0.4397,
1406	      "gsm8k_exact_match": 0.0895,
1407	      "actual_sparsity": 0.2955
1408	    },
1409	    "conclusion": "killed"
1410	  },
1411	  "spon_2048_s42": {
1412	    "metrics": {
1413	      "true_dense_ppl": 6.1173,
1414	      "predictor_hard_mask_ppl": 9.2165,
1415	      "spon_sparse_ppl": 8.991,
1416	      "spon_recovery_pct": 7.3,
1417	      "ppl_improvement_from_spon": 0.2255,
1418	      "mean_bias_norm": 0.05312,
1419	      "max_bias_norm": 0.065918,
1420	      "model_level_sparsity": 0.498,
1421	      "eval_seq_len": 2048,
1422	      "training_seq_len": 2048,
1423	      "eval_samples": 141,
1424	      "trainable_params": 458752,
1425	      "trainable_pct": 0.0057,
1426	      "training_steps": 1000,
1427	      "final_loss": 0.377,
1428	      "dense_with_spon_ppl": 6.1823,
1429	      "dense_ppl_degradation": 0.0651,
1430	      "teal_sparse_no_spon_ppl": 12.0776,
1431	      "teal_sparse_with_spon_ppl": 11.7907,
1432	      "spon_recovery_teal_pct": 4.8,
1433	      "teal_sparsity": 0.4979
1434	    },
1435	    "conclusion": "killed"
1436	  },
1437	  "mvp_kl_norm_v2_s42": {
1438	    "metrics": {
1439	      "true_dense_ppl": 6.1173,
1440	      "predictor_hard_mask_ppl": 9.2142,
1441	      "teal_sparse_ppl": 12.0776,
1442	      "model_level_sparsity": 0.4979,
1443	      "ppl_increase_vs_true_dense_pct": 97.4,
1444	      "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
1445	      "calibration_samples": 32,
1446	      "vanilla_teal_sparse_ppl_INVALID": 66036.4062
1447	    },
1448	    "conclusion": "success"
1449	  },
1450	  "snr_full_curve_1000steps": {
1451	    "metrics": {
1452	      "kl_snr_step0": 1.3e-05,
1453	      "kl_snr_step300": 0.0003465,
1454	      "kl_snr_step1000": 0.0008777,
1455	      "bce_snr_step0": 6.99e-05,
1456	      "bce_snr_step300": 0.0017422,
1457	      "bce_snr_step1000": 0.0020263,
1458	      "kl_bce_ratio_step1000": 0.4332
1459	    },
1460	    "conclusion": "success"
1461	  },
1462	  "kl30_uniform_hellaswag_piqa": {
1463	    "metrics": {
1464	      "hellaswag_acc_norm": 0.7085,
1465	      "piqa_acc_norm": 0.7481,
1466	      "note": "from v2 retry"
1467	    },
1468	    "conclusion": "success"
1469	  },
1470	  "kl30_uniform_hellaswag_piqa_v2": {
1471	    "metrics": {
1472	      "hellaswag_acc_norm": 0.7085,
1473	      "piqa_acc_norm": 0.7481
1474	    },
1475	    "conclusion": "success"
1476	  },
1477	  "kl30_uniform_hspiqa_s123": {
1478	    "metrics": {
1479	      "hellaswag_acc_norm": 0.7067,
1480	      "piqa_acc_norm": 0.7481
1481	    },
1482	    "conclusion": "killed"
1483	  },
1484	  "kl30_uniform_hspiqa_s456": {
1485	    "metrics": {
1486	      "hellaswag_acc_norm": 0.7168,
1487	      "piqa_acc_norm": 0.7524
1488	    },
1489	    "conclusion": "killed"
1490	  },
1491	  "kl50_global_hellaswag_piqa": {
1492	    "metrics": {
1493	      "hellaswag_acc_norm": 0.5895,
1494	      "piqa_acc_norm": 0.6948,
1495	      "note": "from v2 retry"
1496	    },
1497	    "conclusion": "success"
1498	  },
1499	  "kl50_global_hellaswag_piqa_v2": {
1500	    "metrics": {
1501	      "hellaswag_acc_norm": 0.5895,
1502	      "piqa_acc_norm": 0.6948
1503	    },
1504	    "conclusion": "success"
1505	  },
1506	  "kl50_uniform_hellaswag_piqa": {
1507	    "metrics": {
1508	      "hellaswag_acc_norm": 0.5666,
1509	      "piqa_acc_norm": 0.691
1510	    },
1511	    "conclusion": "success"
1512	  },
1513	  "bce_isocompute_hellaswag_piqa": {
1514	    "metrics": {},
1515	    "conclusion": "failed"
1516	  },
1517	  "bce_isocompute_hellaswag_piqa_v2": {
1518	    "metrics": {
1519	      "hellaswag_acc_norm": 0.6281,
1520	      "piqa_acc_norm": 0.7421
1521	    },
1522	    "conclusion": "success"
1523	  },
1524	  "db_sensitivity_sweep": {
1525	    "metrics": {
1526	      "db64_per_token_ppl": 10.158,
1527	      "db64_teal_global_ppl": 12.076,
1528	      "db64_sparsity": 0.5,
1529	      "db64_loss": 0.361,
1530	      "db128_teal_global_ppl": 11.963,
1531	      "db128_per_token_ppl": 9.218,
1532	      "db256_per_token_ppl": 8.586,
1533	      "db256_teal_global_ppl": 12.105,
1534	      "db256_sparsity": 0.5,
1535	      "db256_loss": 0.27,
1536	      "db512_per_token_ppl": 7.933,
1537	      "db512_teal_global_ppl": 12.315,
1538	      "db512_sparsity": 0.5,
1539	      "db512_loss": 0.224,
1540	      "best_teal_global_db": 128,
1541	      "best_teal_global_ppl": 11.963
1542	    },
1543	    "conclusion": "success"
1544	  },
1545	  "tau_schedule_ablation": {
1546	    "metrics": {
1547	      "tau_linear_baseline_ppl": 11.963,
1548	      "tau_fixed05_ppl": 11.861,
1549	      "tau_fixed01_ppl": 12.072,
1550	      "tau_fixed05_loss": 0.248,
1551	      "tau_fixed01_loss": 0.43,
1552	      "best_tau": "fixed_0.5",
1553	      "ppl_range": 0.211
1554	    },
1555	    "conclusion": "success"
1556	  },
1557	  "steps_curve_s42_v2": {
1558	    "metrics": {},
1559	    "conclusion": "killed"
1560	  },
1561	  "kl_comp_30pct_s42": {
1562	    "metrics": {
1563	      "final_loss": 0.6992,
1564	      "steps": 1000,
1565	      "compensation_params": 67248128,
1566	      "compensation_pct": 0.837,
1567	      "mean_head_norm_final": 9.2012,
1568	      "loss_trajectory": [
1569	        2.3594,
1570	        1.3516,
1571	        1.0859,
1572	        0.9219,
1573	        0.8789,
1574	        0.8281,
1575	        0.7461,
1576	        0.7344,
1577	        0.6953,
1578	        0.6992
1579	      ]
1580	    },
1581	    "conclusion": "success"
1582	  },
1583	  "kl_comp_30pct_s42_eval": {
1584	    "metrics": {
1585	      "wikitext2_ppl": 8.9788,
1586	      "arc_challenge_acc_norm": 0.3993,
1587	      "winogrande_acc": 0.6898,
1588	      "mmlu_acc": 0.2531,
1589	      "gsm8k_exact_match": 0.0842
1590	    },
1591	    "conclusion": "success"
1592	  },
1593	  "kl_comp_30pct_s42_ppl": {
1594	    "metrics": {
1595	      "wikitext2_ppl": 8.9768,
1596	      "c4_ppl": 16.0401,
1597	      "sparsity": 0.3,
1598	      "allocation": "global_topk",
1599	      "model": "llama-3.1-8b",
1600	      "seed": 42
1601	    },
1602	    "conclusion": "success"
1603	  },
1604	  "kl_comp_30pct_s456": {
1605	    "metrics": {},
1606	    "conclusion": "success"
1607	  },
1608	  "kl_comp_30pct_s456_eval": {
1609	    "metrics": {
1610	      "wikitext2_ppl": 8.9614,
1611	      "arc_challenge_acc_norm": 0.4462,
1612	      "winogrande_acc": 0.7143,
1613	      "mmlu_acc": 0.2714,
1614	      "gsm8k_exact_match": 0.0887
1615	    },
1616	    "conclusion": "success"
1617	  },
1618	  "kl_comp_50pct_s42": {
1619	    "metrics": {},
1620	    "conclusion": "success"
1621	  },
1622	  "kl_comp_50pct_s42_eval": {
1623	    "metrics": {
1624	      "wikitext2_ppl": 11.7933,
1625	      "arc_challenge_acc_norm": 0.3285,
1626	      "winogrande_acc": 0.6346,
1627	      "mmlu_acc": 0.2789,
1628	      "gsm8k_exact_match": 0.0129
1629	    },
1630	    "conclusion": "success"
1631	  },
1632	  "kl_sparsity25_s42": {
1633	    "metrics": {
1634	      "train_loss_final": 0.1582,
1635	      "kl_normalized_final": 0.1582,
1636	      "sparsity_actual": 0.23,
1637	      "sparsity_target": 0.25,
1638	      "lambda_final": 5000,
1639	      "tau_final": 0.1,
1640	      "steps": 1000
1641	    },
1642	    "conclusion": "success"
1643	  },
1644	  "kl_sparsity35_s42": {
1645	    "metrics": {
1646	      "final_loss": 0.203,
1647	      "final_sparsity": 0.336,
1648	      "steps": 1000
1649	    },
1650	    "conclusion": "success"
1651	  },
1652	  "kl_sparsity45_s42": {
1653	    "metrics": {
1654	      "final_loss": 0.33,
1655	      "final_sparsity": 0.449,
1656	      "steps": 1000
1657	    },
1658	    "conclusion": "success"
1659	  },
1660	  "kl_sparsity70_s42": {
1661	    "metrics": {},
1662	    "conclusion": "killed"
1663	  },
1664	  "kl_sparsity25_s42_eval_teal": {
1665	    "metrics": {
1666	      "wikitext2_ppl": 8.169,
1667	      "arc_challenge_acc_norm": 0.4539,
1668	      "winogrande_acc": 0.7056,
1669	      "mmlu_acc": 0.466,
1670	      "gsm8k_exact_match": 0.1145,
1671	      "actual_sparsity": 0.23,
1672	      "allocation": "global_topk"
1673	    },
1674	    "conclusion": "success"
1675	  },
1676	  "kl_sparsity25_s42_eval_teal_uniform": {
1677	    "metrics": {
1678	      "wikitext2_ppl": 8.2344,
1679	      "arc_challenge_acc_norm": 0.465,
1680	      "winogrande_acc": 0.7182,
1681	      "mmlu_acc": 0.4395,
1682	      "gsm8k_exact_match": 0.1099,
1683	      "actual_sparsity": 0.25,
1684	      "allocation": "uniform"
1685	    },
1686	    "conclusion": "success"
1687	  },
1688	  "kl_sparsity35_s42_eval_teal": {
1689	    "metrics": {
1690	      "ppl_wikitext2": 9.3133,
1691	      "arc_challenge_acc": 0.3643,
1692	      "arc_challenge_acc_norm": 0.3891,
1693	      "winogrande_acc": 0.6764,
1694	      "mmlu_acc": 0.4041,
1695	      "gsm8k_exact_match": 0.0773,
1696	      "actual_sparsity": 0.336
1697	    },
1698	    "conclusion": "success"
1699	  },
1700	  "kl_sparsity35_s42_eval_teal_uniform": {
1701	    "metrics": {
1702	      "wikitext2_ppl": 9.4416,
1703	      "arc_challenge_acc_norm": 0.3874,
1704	      "winogrande_acc": 0.6654,
1705	      "mmlu_acc": 0.3783,
1706	      "gsm8k_exact_match": 0.0432,
1707	      "actual_sparsity": 0.35,
1708	      "allocation": "uniform"
1709	    },
1710	    "conclusion": "success"
1711	  },
1712	  "kl_sparsity40_s42_global_eval_v2": {
1713	    "metrics": {
1714	      "wikitext2_ppl": 10.14,
1715	      "arc_challenge_acc_norm": 0.3951,
1716	      "winogrande_acc": 0.6748,
1717	      "mmlu_acc": 0.3947,
1718	      "gsm8k_exact_match": 0.066,
1719	      "hellaswag_acc_norm": 0.6779,
1720	      "piqa_acc_norm": 0.7269
1721	    },
1722	    "conclusion": "success"
1723	  },
1724	  "kl_sparsity40_s42_retrain_uniform": {
1725	    "metrics": {
1726	      "wikitext2_ppl": 10.76,
1727	      "arc_challenge_acc_norm": 0.3959,
1728	      "winogrande_acc": 0.6306,
1729	      "mmlu_acc": 0.355,
1730	      "gsm8k_acc": 0.0356,
1731	      "training_final_loss": 0.2598,
1732	      "training_final_sparsity": 0.387
1733	    },
1734	    "conclusion": "success"
1735	  },
1736	  "kl_sparsity45_s42_eval_teal": {
1737	    "metrics": {
1738	      "ppl_wikitext2": 10.803,
1739	      "arc_challenge_acc": 0.3498,
1740	      "arc_challenge_acc_norm": 0.3916,
1741	      "winogrande_acc": 0.6464,
1742	      "mmlu_acc": 0.3037,
1743	      "gsm8k_exact_match": 0.0296,
1744	      "actual_sparsity": 0.449
1745	    },
1746	    "conclusion": "success"
1747	  },
1748	  "kl_sparsity45_s42_eval_teal_uniform": {
1749	    "metrics": {
1750	      "wikitext2_ppl": 10.9488,
1751	      "arc_challenge_acc_norm": 0.3763,
1752	      "winogrande_acc": 0.6361,
1753	      "mmlu_acc": 0.3063,
1754	      "gsm8k_exact_match": 0.0273,
1755	      "actual_sparsity": 0.45,
1756	      "allocation": "uniform"
1757	    },
1758	    "conclusion": "success"
1759	  },
1760	  "kl_bce_f1_oracle": {
1761	    "metrics": {
1762	      "bce_f1": 0.6128,
1763	      "bce_precision": 0.6132,
1764	      "bce_recall": 0.6124,
1765	      "kl_f1": 0.5397,
1766	      "kl_precision": 0.5112,
1767	      "kl_recall": 0.5715,
1768	      "random_f1": 0.5,
1769	      "kl_ppl": 11.79,
1770	      "bce_ppl": 22.51
1771	    },
1772	    "conclusion": "success"
1773	  },
1774	  "bce_30pct_s42": {
1775	    "metrics": {},
1776	    "conclusion": "success"
1777	  },
1778	  "revkl_30_s123": {
1779	    "metrics": {
1780	      "ppl": 9.2859,
1781	      "sparsity": 0.296,
1782	      "allocation": "uniform"
1783	    },
1784	    "conclusion": "success"
1785	  },
1786	  "revkl_30_s123_downstream": {
1787	    "metrics": {
1788	      "arc_challenge_acc_norm": 0.4556,
1789	      "winogrande_acc": 0.689,
1790	      "mmlu_acc": 0.38,
1791	      "gsm8k_exact_match": 0.072,
1792	      "hellaswag_acc_norm": 0.7092,
1793	      "piqa_acc_norm": 0.7524,
1794	      "boolq_acc": 0.7199
1795	    },
1796	    "conclusion": "success"
1797	  },
1798	  "revkl_30_s456": {
1799	    "metrics": {
1800	      "ppl": 9.1841
1801	    },
1802	    "conclusion": "success"
1803	  },
1804	  "revkl_30_s456_downstream": {
1805	    "metrics": {},
1806	    "conclusion": "killed"
1807	  }
1808	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3470356c-7244-48b2-9a71-baaca57aa193",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "57ee8f33-ccfe-46f5-82a0-9d24b4b893a2",
  "sourceToolAssistantUUID": "3470356c-7244-48b2-9a71-baaca57aa193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T19:19:46.018Z_

<details open><summary>🔧 Tool call — Read · `toolu_016pssMLRpTiGy8eZBBdy35d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57ee8f33-ccfe-46f5-82a0-9d24b4b893a2",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3LYgKNBZe53VJTF4i1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73216563-673e-4aa6-9424-00a8fda06654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ncaGRDtf1nz6N1uqUVA67",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 0,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 150,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17242,
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

_source line 7 · 2026-05-23T19:19:46.023Z_

<details><summary>↩ Tool result · `toolu_016pssMLRpTiGy8eZBBdy35d`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, output-distribution KL under uniform allocation achieves PPL 8.81$\pm$0.02 (3-seed), a 14.5\% reduction over TEAL at matched actual sparsity (8.81 vs.\ 10.30, both at 28.5\%; Appendix~\ref{app:ood}).
29	Uniform allocation yields stable downstream (MMLU 40.7$\pm$1.3\%, 3-seed; Appendix~\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%) from late-layer starvation (L31 retention 28.4\%; \S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed
30	
31	\paragraph{Task-Type Split.}
32	KL shows directional improvements over TEAL on commonsense reasoning (ARC-c, WG, HellaSwag, PIQA: 4/4 wins at 30\% uniform) but underperforms on knowledge-intensive tasks (MMLU, GSM8K: 0/2).
33	With only three seeds, 95\% confidence intervals for individual downstream tasks overlap; we therefore treat PPL ($\sigma{=}0.02$, non-overlapping) as the primary metric and downstream differences as directional evidence.
34	The KL predictor protects L14--L18 (14--18\% sparsity vs.\ 32\% global mean) while aggressively pruning L22--L28 (48--57\%). Constraint interventions (Appendix~\ref{app:constraint}) confirm a task-dependent trade-off: removing the valley improves MMLU +3.4pp but reduces ARC-c by 1.5pp, consistent with localized factual associations~\cite{geva2023dissecting}; task-aware allocation may resolve this. % exp_id: bench_kl30_uniform, teal30_uniform, hellaswag_piqa_kl30_uniform, perlayer_sparsity_analysis, constraint_protect_late, constraint_remove_valley
35	
36	\paragraph{Knowledge-Task Regression: Hypothesis.}
37	We consider two hypotheses. First, WikiText-103's limited mathematical content may bias allocation against reasoning pathways---however, a C4-trained control does not support this (see below). Second, forward KL's mode-covering property distributes mass across high-frequency patterns, potentially diluting rare activations encoding factual knowledge concentrated in specific FFN neurons~\cite{meng2022locating}. Constraint experiments (Appendix~\ref{app:constraint}) confirm allocation contributes: removing the learned valley improves MMLU +3.4pp and GSM8K +1.6pp. A predictor trained on C4 (diverse web text; Appendix~\ref{app:c4_control}) does not alleviate the regression (MMLU 40.0\%, GSM8K 4.1\% vs.\ 40.7\%, 7.5\%), confirming the deficit is structural to output-distribution KL rather than training data composition. % exp_id: constraint_remove_valley, c4_control_eval
38	
39	At 50\%, the PPL advantage widens (11.92 vs.\ 23.90, 50\% reduction) and generalizes to C4 (Appendix~\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\leq$2.7\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global
40	
41	\begin{table}[t]
42	\centering
43	\caption{Main results on LLaMA-3.1-8B. $^\ast$$2.71\times$ KL compute (\S\ref{sec:isocompute}). $\pm$: 3-seed; unmarked: s42. $^\ddagger$Actual sparsity: KL 28.5\% vs.\ TEAL 29.3\% at 30\% (Appendix~\ref{app:ood}).}
44	\label{tab:main}
45	\resizebox{\columnwidth}{!}{
46	\begin{tabular}{llccccc}
47	\toprule
48	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
49	\midrule
50	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
51	\midrule
52	\multirow{6}{*}{30\%}
53	& TEAL uniform & 10.82 & 39.33 & 65.04 & \textbf{45.86} & \textbf{8.79} \\ % exp_id: teal30_uniform
54	& BCE global & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\ % exp_id: bce30_teal_global
55	& BCE uniform & 15.09$\pm$0.13 & 33.45 & 61.09 & 43.05 & 3.97 \\ % exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456
56	& MSE uniform & 18.52$\pm$1.68 & 35.8$\pm$4.1 & 59.8$\pm$2.6 & 30.7$\pm$2.6 & 2.3$\pm$0.7 \\ % exp_id: mse30_3seed
57	& KL global (Ours)$^\ddagger$ & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & 8.0$\pm$0.7 \\ % exp_id: kl30_3seed_global
58	& KL uniform$^\ddagger$ & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & 40.7$\pm$1.3 & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
59	\midrule
60	\multirow{5}{*}{50\%}
61	& TEAL uniform & 23.90 & 27.47 & 54.38 & \textbf{29.26} & 1.74 \\ % exp_id: teal50_uniform
62	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
63	& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\ % exp_id: mse50_uniform_s42
64	& KL global (Ours) & \textbf{11.84$\pm$0.15} & \textbf{36.3$\pm$3.2} & \textbf{63.8$\pm$0.3} & 28.3$\pm$0.7 & \textbf{2.7$\pm$1.3} \\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
65	& KL uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456
66	\bottomrule
67	\end{tabular}}
68	\end{table}
69	
70	
71	\subsection{Extended Training Analysis}
72	\label{sec:isocompute}
73	
74	At $2.71\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\pm$0.20 (3-seed), still $2.39\times$ worse than KL (11.79). % exp_id: bce50_3seed
75	The gap is systematic: BCE reaches higher oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL, confirming KL optimizes for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42
76	
77	
78	\subsection{Mask Pattern Analysis}
79	\label{sec:mask_analysis}
80	
81	KL-derived masks diverge from magnitude oracles: per-layer Jaccard distance averages 68\% at 50\% (64 samples, 131K tokens; Figure~\ref{fig:mask_heatmap}), with cross-seed variation (36.3\%) confirming systematic divergence (Appendices~\ref{app:cross_seed_jaccard},~\ref{app:mask_viz}).
82	Despite this, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
83	Divergence follows a U-shaped per-layer pattern, peaking in late layers (0.70--0.75 at 50\%). % exp_id: c1_mask_overlap
84	
85	\paragraph{Target-Swap Ablation: Target Quality vs.\ Gradient Coupling.}
86	To disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).
87	Table~\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.
88	
89	\begin{table}[t]
90	\centering
91	\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\ KL predictor (same seed), TEAL uniform. All seeds show max $\Delta$$\leq$1.70pp at 30\%; max $\Delta$$\leq$0.79pp at 50\% (s42). $^\dagger$\textbf{Provenance:} s42 oracle extracted from an earlier training run (not seed-matched); s123/s456 use seed-matched retrained oracles (Appendix~\ref{app:oracle_provenance}).}
92	\label{tab:c1}
93	\resizebox{\columnwidth}{!}{
94	\begin{tabular}{lllccccc}
95	\toprule
96	Sparsity & Seed & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
97	\midrule
98	\multirow{6}{*}{30\%}
99	& s42$^\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \textbf{42.30} & \textbf{7.58} \\ % exp_id: c1_ablation_30pct_s42_eval_v2
100	& & KL & \textbf{8.82} & \textbf{40.78} & \textbf{68.59} & 40.6 & 7.35 \\ % exp_id: bench_kl30_uniform
101	& s123 & C1 & 8.84 & 44.71 & \textbf{69.77} & \textbf{39.92} & 6.82 \\ % exp_id: eval_c1_retrain_30pct_s123
102	& & KL & \textbf{8.83} & \textbf{45.31} & 69.38 & 39.4 & \textbf{7.51} \\ % exp_id: kl30_s123_eval
103	& s456 & C1 & 8.82 & 44.71 & \textbf{69.93} & 41.04 & 6.60 \\ % exp_id: eval_c1_retrain_30pct_s456
104	& & KL & \textbf{8.79} & \textbf{45.05} & 68.75 & \textbf{42.0} & \textbf{7.58} \\ % exp_id: kl30_s456_uniform_eval
105	\midrule
106	\multirow{2}{*}{50\%}
107	& s42 & C1 & 11.96 & 32.17 & \textbf{63.14} & 27.79 & \textbf{2.05} \\ % exp_id: c1_bce_kl_targets_teal50u
108	& & KL & 11.96 & \textbf{32.59} & 62.35 & \textbf{27.92} & 1.97 \\ % exp_id: c1_kl_teal50u
109	\bottomrule
110	\end{tabular}}
111	\end{table}
112	
113	At 50\% (s42, earlier oracle), C1 matches KL within 0.79pp, while magnitude-trained BCE yields $2.4\times$ worse PPL (Table~\ref{tab:main}).
114	At 30\%, retrained seeds show $\leq$1.18pp agreement\footnote{s42 oracle from earlier checkpoint (gap 0.65pp); s123/s456 use seed-matched converged oracles ($\leq$0.03pp gap).}.
115	C1 demonstrates that KL-discovered mask patterns \emph{transfer} to a simpler training mechanism (PPL within 0.79pp; downstream variation up to 4.5pp MMLU); per-layer KL controls (\S\ref{sec:perlayer}) further show coupling contributes marginally to PPL but substantially to downstream fidelity.
116	However, C1 also changes mask representation: binarizing oracle soft logits ($>$0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask \emph{patterns} rather than full predictor knowledge. BCE+Gumbel (32.22) vs.\ standard BCE (27.97) suggests softness alone does not explain KL's advantage, though trajectory-dependent confounds remain (Appendix~\ref{app:oracle_provenance}). % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123, bce_gumbel_no_penalty_s42, eval_bce_v3_s42
117	
118	\subsection{Ablation Studies}
119	
120	Table~\ref{tab:ablation} isolates the contribution of each design choice at 30\% and 50\% sparsity.
121	
122	\begin{table}[t]
123	\centering
124	\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$; uniform at 30\%, global at 50\%). $\pm$: 3-seed; unmarked: s42. $^\ddagger$STE: 20.8\% actual sparsity at 30\% target; loss effect ($\Delta$PPL=20.4) is $5.1\times$ relaxation effect ($\Delta$PPL=3.98). $^\S$MSE 50\%: s42 only; s123 catastrophic (PPL{=}15{,}789; Appendix~\ref{app:mse_config}).}
125	\label{tab:ablation}
126	\resizebox{\columnwidth}{!}{
127	\begin{tabular}{lccc}
128	\toprule
129	Configuration & 30\% PPL$\downarrow$ & 50\% PPL$\downarrow$ & $\Delta_{50}$ \\
130	\midrule
131	\multicolumn{4}{l}{\textit{KL-based variants}} \\
132	Forward KL + Gumbel (Ours) & \textbf{8.81$\pm$0.02} & \textbf{11.79} & --- \\ % exp_id: kl30_ablation_s42, bench_kl50_global
133	JSD (symmetric) + Gumbel & 8.90$\pm$0.02 & 12.54 & +0.75 \\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42
134	Reverse KL + Gumbel & 9.26$\pm$0.07 & 12.80 & +1.01 \\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42
135	Forward KL + STE & ---$^\ddagger$ & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
136	\midrule
137	\multicolumn{4}{l}{\textit{Per-layer training}} \\
138	Per-layer MSE & 18.52$\pm$1.68 & 229.26$^\S$ & +217.47 \\ % exp_id: mse30_uniform_s42, mse50_uniform_s42
139	Per-layer KL ($K{=}1$) & 9.05$\pm$0.02 & 34.85 & +23.06 \\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42
140	Per-layer KL ($K{=}4$) & 8.89$\pm$0.01 & 44.23 & +32.44 \\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42
141	\midrule
142	\multicolumn{4}{l}{\textit{BCE-based variants}} \\
143	BCE (no compensation) & 15.71 & 27.97 & +16.18 \\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42
144	BCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
145	BCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
146	BCE + STE & --- & 60.54 & +48.75 \\ % exp_id: bce_ste_s42
147	\bottomrule
148	\end{tabular}}
149	\end{table}
150	
151	\paragraph{Relaxation, Divergence, and SPON.}
152	At 50\%, Gumbel-Sigmoid outperforms STE~\cite{bengio2013ste} by 33.8\% (11.79 vs.\ 15.77); forward KL outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with mode-covering~\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42
153	At 30\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed
154	KL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope provides additional downstream benefits (\S\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed
155	\paragraph{Per-Layer KL: Exploratory Decomposition of Signal Type and Coupling Scope.}
156	\label{sec:perlayer}
157	To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.
158	At $K{=}1$, per-layer KL achieves 9.05$\pm$0.02, within 2.7\% of end-to-end KL (8.81$\pm$0.02), while per-layer MSE degrades to 18.52$\pm$1.68 ($2.05\times$ worse). For PPL, signal type\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\footnote{Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\ref{app:k4_downstream}): \emph{coupling-dominated}---ARC-c (97\% residual gap) and WG (67\%) indicate genuine cross-layer benefits; \emph{mismatch-dominated}---PPL (67\% closure) and GSM8K (71\%) largely close; \emph{anomalous}---MMLU exceeds E2E (42.7$\pm$1.4 vs.\ 40.7$\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed
159	At 50\%, partial coupling ($K{=}4$: 44.23) is \emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.84, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global
160	
161	\begin{figure}[t]
162	\centering
163	\includegraphics[width=\columnwidth]{k_curve_ppl}
164	\vspace{-8pt}
165	\caption{Coupling breadth $K$ vs.\ perplexity (30\%, TEAL uniform, 3-seed mean$\pm$std). $K{=}32$ denotes end-to-end training. $K{=}2$ degradation reflects insufficient per-layer updates (${\sim}62$ vs.\ ${\sim}250$ at $K{=}8$).}
166	\label{fig:k_curve_ppl}
167	\vspace{-8pt}
168	\end{figure}
169	
170	The $K$-curve (Figure~\ref{fig:k_curve_ppl}) confirms non-monotonic coupling effects: $K{=}16$ achieves the lowest PPL (8.67$\pm$0.02 vs.\ E2E 8.81$\pm$0.02), yet the full coupling range (2.08 PPL) is dwarfed by the signal type gap (9.47 PPL). % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed
171	
172	\paragraph{Compensation Redundancy.}
173	\label{sec:compensation}
174	FastForward-style compensation~\cite{gautam2026fastforward} (+67.2M params) provides no benefit (Appendices~\ref{app:comp_convergence}--\ref{app:training_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42, db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
175	
176	
177	\subsection{Sparsity Scaling and Regime Analysis}
178	\label{sec:scaling}
179	
180	\begin{figure}[t]
181	\centering
182	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
183	\vspace{-8pt}
184	\caption{PPL scaling with sparsity (global allocation). KL's advantage grows: 14.5\% at 30\% (matched actual sparsity), 50\% at 50\%, 82\% at 70\%.}
185	\label{fig:sparsity_sweep}
186	\vspace{-8pt}
187	\end{figure}
188	
189	\paragraph{Allocation Behavior.}
190	Table~\ref{tab:phase} (Appendix~\ref{app:alloc_full}) reveals non-monotonic allocation preference: uniform is best at $\leq$30\% ($7.3\times$ smaller MMLU $\sigma$), global at 35--40\%, both collapse at $\geq$45\%. % exp_id: kl30_3seed, regime_kl35_global, regime_kl35_uniform, multi_seed_kl50_global, multi_seed_kl50_uniform
191	
192	\paragraph{Cross-Architecture and Scale.}
193	\label{sec:cross_arch}
194	On Mistral-7B-v0.3~\cite{jiang2023mistral}, PPL generalizes ($-$17.3\%, 3-seed; Table~\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline (Table~\ref{tab:14b}).
195	The consistent regression across scales (8B MMLU $-$5.2pp, 14B GSM8K 32.0$\pm$5.2 vs.\ 52.1) suggests a systematic property of output-distribution KL; Qwen's larger $d_{\text{ff}}$ ($148\times$ vs.\ $112\times$ compression) may amplify sensitivity at stronger reasoning baselines. The pipeline adds 6.4\% latency overhead absent sparse kernels (Appendix~\ref{app:latency}). % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, mistral_teal30_downstream, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform, latency_profiling
196	
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73216563-673e-4aa6-9424-00a8fda06654",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "c545ccfc-0328-4544-ab9a-52a1aaecf046",
  "sourceToolAssistantUUID": "73216563-673e-4aa6-9424-00a8fda06654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T19:19:49.251Z_

Now let me compute and verify every number systematically. I'll use Python for the calculations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c545ccfc-0328-4544-ab9a-52a1aaecf046",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3MfwASBg1CqsivcGf1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8995ef17-ac1b-41dc-9d62-ca8d0b3bdb07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2Nk3EmvbxYr36NC614Uxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34304,
      "cache_read_input_tokens": 17242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34304,
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

_source line 9 · 2026-05-23T19:20:23.244Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SDn8QAt5hBCtcjMGKxbXex`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\ndef pct(x): return round(x * 100, 2)\n\ndef mean_std(vals):\n    m = sum(vals) / len(vals)\n    if len(vals) > 1:\n        s = math.sqrt(sum((v - m)**2 for v in vals) / (len(vals) - 1))\n    else:\n        s = 0\n    return m, s\n\nprint(\"=\" * 80)\nprint(\"ROW 1: Dense (0%)\")\nprint(\"=\" * 80)\nd = reg[\"bench_dense\"][\"metrics\"]\nprint(f\"PPL: paper=6.12, registry={round(d['wikitext2_ppl'],2)} -> {'MATCH' if round(d['wikitext2_ppl'],2) == 6.12 else 'MISMATCH'}\")\nprint(f\"ARC-c: paper=58.28, registry={pct(d['arc_challenge_acc_norm'])} -> {'MATCH' if pct(d['arc_challenge_acc_norm']) == 58.28 else 'MISMATCH'}\")\nprint(f\"WG: paper=78.06, registry={pct(d['winogrande_acc'])} -> {'MATCH' if pct(d['winogrande_acc']) == 78.06 else 'MISMATCH'}\")\nprint(f\"MMLU: paper=65.27, registry={pct(d['mmlu_acc'])} -> {'MATCH' if pct(d['mmlu_acc']) == 65.27 else 'MISMATCH'}\")\nprint(f\"GSM8K: paper=48.75, registry={pct(d['gsm8k_exact_match'])} -> {'MATCH' if pct(d['gsm8k_exact_match']) == 48.75 else 'MISMATCH'}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 2: 30% TEAL uniform\")\nprint(\"=\" * 80)\n# Use bench_teal30_uniform_6task for all metrics\nd = reg[\"bench_teal30_uniform_6task\"][\"metrics\"]\nprint(f\"PPL: paper=10.82, registry={round(d['wikitext2_ppl'],2)} -> {'MATCH' if round(d['wikitext2_ppl'],2) == 10.82 else 'MISMATCH: paper=10.82, registry=' + str(round(d['wikitext2_ppl'],2))}\")\nprint(f\"ARC-c: paper=39.33, registry={pct(d['arc_challenge_acc_norm'])} -> {'MATCH' if pct(d['arc_challenge_acc_norm']) == 39.33 else 'MISMATCH: paper=39.33, registry=' + str(pct(d['arc_challenge_acc_norm']))}\")\nprint(f\"WG: paper=65.04, registry={pct(d['winogrande_acc'])} -> {'MATCH' if pct(d['winogrande_acc']) == 65.04 else 'MISMATCH: paper=65.04, registry=' + str(pct(d['winogrande_acc']))}\")\nprint(f\"MMLU: paper=45.86, registry={pct(d['mmlu_acc'])} -> {'MATCH' if pct(d['mmlu_acc']) == 45.86 else 'MISMATCH: paper=45.86, registry=' + str(pct(d['mmlu_acc']))}\")\n# GSM8K not in bench_teal30_uniform_6task, check bench_teal30\nd2 = reg[\"bench_teal30\"][\"metrics\"]\nprint(f\"GSM8K: paper=8.79, bench_teal30={pct(d2['gsm8k_exact_match'])} -> {'MATCH' if pct(d2['gsm8k_exact_match']) == 8.79 else 'MISMATCH: paper=8.79, registry=' + str(pct(d2['gsm8k_exact_match']))}\")\n# Also check bench_teal30 ARC/WG/MMLU for comparison\nprint(f\"  (bench_teal30 alt: PPL={round(d2['wikitext2_ppl'],2)}, ARC-c={pct(d2['arc_challenge_acc_norm'])}, WG={pct(d2['winogrande_acc'])}, MMLU={pct(d2['mmlu_acc'])})\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 3: 30% BCE global\")\nprint(\"=\" * 80)\nd = reg[\"bce_30pct_s42_eval\"][\"metrics\"]\nprint(f\"PPL: paper=11.25, registry={round(d['wikitext2_ppl'],2)} -> {'MATCH' if round(d['wikitext2_ppl'],2) == 11.25 else 'MISMATCH: paper=11.25, registry=' + str(round(d['wikitext2_ppl'],2))}\")\nprint(f\"ARC-c: paper=41.2, registry={pct(d['arc_challenge_acc_norm'])} -> {'MATCH' if pct(d['arc_challenge_acc_norm']) == 41.2 else 'MISMATCH: paper=41.2, registry=' + str(pct(d['arc_challenge_acc_norm']))}\")\nprint(f\"  paper rounds 41.21 to 41.2\")\nprint(f\"WG: paper=66.0, registry={pct(d['winogrande_acc'])} -> {'MATCH' if pct(d['winogrande_acc']) == 66.0 else 'MISMATCH: paper=66.0, registry=' + str(pct(d['winogrande_acc']))}\")\nprint(f\"  paper rounds 65.98 to 66.0\")\nprint(f\"MMLU: paper=36.3, registry={pct(d['mmlu_acc'])} -> {'MATCH' if pct(d['mmlu_acc']) == 36.3 else 'MISMATCH: paper=36.3, registry=' + str(pct(d['mmlu_acc']))}\")\nprint(f\"  paper rounds 36.33 to 36.3\")\nprint(f\"GSM8K: paper=6.0, registry={pct(d['gsm8k_exact_match'])} -> {'MATCH' if pct(d['gsm8k_exact_match']) == 6.0 else 'MISMATCH: paper=6.0, registry=' + str(pct(d['gsm8k_exact_match']))}\")\nprint(f\"  paper rounds 5.99 to 6.0\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 4: 30% BCE uniform (3-seed)\")\nprint(\"=\" * 80)\n# bce_30_s42_uniform_eval, need to find s123 and s456 uniform evals\n# But wait - the paper exp_ids say bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\n# These are the 50% BCE experiments! Let me check what the paper really means.\n# Actually the paper says \"BCE uniform\" at 30%, but the exp_ids reference bce_iso_v3 which are 50% BCE.\n# Let me check the bce_30_s42_uniform_eval\nd42 = reg[\"bce_30_s42_uniform_eval\"][\"metrics\"]\nprint(f\"  bce_30_s42_uniform_eval: PPL={d42['ppl']}, ARC-c={pct(d42['arc_challenge'])}, WG={pct(d42['winogrande'])}, MMLU={pct(d42['mmlu'])}, GSM8K={pct(d42['gsm8k'])}\")\n# No s123/s456 counterparts found. The paper says PPL=15.09±0.13, which is close to 15.71 from bce_30_s42_uniform_eval\n# Wait, let me re-read. The comment says exp_id: bce_iso_v3_s42 etc. But those are the isocompute experiments.\n# Those are actually 50% BCE (isocompute = 2700 steps at 50%). The 30% BCE uniform must be different.\n# Actually, looking more carefully, the \"BCE uniform\" at 30% with PPL=15.09 is likely from bce_30_s42_uniform_eval (PPL=15.71) and similar seeds.\n# But 15.09 != 15.71. Let me check if there are other entries.\nprint(f\"  Single seed bce_30_s42_uniform_eval PPL=15.71 vs paper mean 15.09\")\nprint(f\"  No 3-seed data found for 30% BCE uniform in registry!\")\nprint(f\"  [MISMATCH] Cannot verify 30% BCE uniform 3-seed numbers - only single seed available (PPL 15.71 vs paper 15.09)\")\n\nPYEOF\n",
  "description": "Verify Dense, TEAL 30%, BCE global 30%, BCE uniform 30% numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8995ef17-ac1b-41dc-9d62-ca8d0b3bdb07",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3MfwASBg1CqsivcGf1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "199d8d9a-c99c-4105-a404-205e0ac35bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2Nk3EmvbxYr36NC614Uxe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34304,
      "cache_read_input_tokens": 17242,
      "output_tokens": 2459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2459,
          "cache_read_input_tokens": 17242,
          "cache_creation_input_tokens": 34304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34304,
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

_source line 10 · 2026-05-23T19:20:23.331Z_

<details><summary>↩ Tool result · `toolu_01SDn8QAt5hBCtcjMGKxbXex`</summary>

```text
================================================================================
ROW 1: Dense (0%)
================================================================================
PPL: paper=6.12, registry=6.12 -> MATCH
ARC-c: paper=58.28, registry=58.28 -> MATCH
WG: paper=78.06, registry=78.06 -> MATCH
MMLU: paper=65.27, registry=65.27 -> MATCH
GSM8K: paper=48.75, registry=48.75 -> MATCH

================================================================================
ROW 2: 30% TEAL uniform
================================================================================
PPL: paper=10.82, registry=10.82 -> MATCH
ARC-c: paper=39.33, registry=39.33 -> MATCH
WG: paper=65.04, registry=65.04 -> MATCH
MMLU: paper=45.86, registry=45.86 -> MATCH
GSM8K: paper=8.79, bench_teal30=7.88 -> MISMATCH: paper=8.79, registry=7.88
  (bench_teal30 alt: PPL=10.97, ARC-c=42.32, WG=66.06, MMLU=38.61)

================================================================================
ROW 3: 30% BCE global
================================================================================
PPL: paper=11.25, registry=11.24 -> MISMATCH: paper=11.25, registry=11.24
ARC-c: paper=41.2, registry=41.21 -> MISMATCH: paper=41.2, registry=41.21
  paper rounds 41.21 to 41.2
WG: paper=66.0, registry=65.98 -> MISMATCH: paper=66.0, registry=65.98
  paper rounds 65.98 to 66.0
MMLU: paper=36.3, registry=36.33 -> MISMATCH: paper=36.3, registry=36.33
  paper rounds 36.33 to 36.3
GSM8K: paper=6.0, registry=5.99 -> MISMATCH: paper=6.0, registry=5.99
  paper rounds 5.99 to 6.0

================================================================================
ROW 4: 30% BCE uniform (3-seed)
================================================================================
  bce_30_s42_uniform_eval: PPL=15.7069, ARC-c=33.19, WG=61.8, MMLU=42.37, GSM8K=3.94
  Single seed bce_30_s42_uniform_eval PPL=15.71 vs paper mean 15.09
  No 3-seed data found for 30% BCE uniform in registry!
  [MISMATCH] Cannot verify 30% BCE uniform 3-seed numbers - only single seed available (PPL 15.71 vs paper 15.09)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "199d8d9a-c99c-4105-a404-205e0ac35bc7",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "0b331a14-69d6-4601-8011-cfcb7c26454c",
  "sourceToolAssistantUUID": "199d8d9a-c99c-4105-a404-205e0ac35bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:21:02.582Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01REJzYsFVuYQVmNSAY3jhyn`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\ndef pct(x): return round(x * 100, 2)\ndef mean_std(vals):\n    m = sum(vals) / len(vals)\n    if len(vals) > 1:\n        s = math.sqrt(sum((v - m)**2 for v in vals) / (len(vals) - 1))\n    else:\n        s = 0\n    return round(m, 2), round(s, 2)\n\n# Search for any BCE 30% uniform keys\nprint(\"Looking for BCE 30% uniform multi-seed entries...\")\nfor k in sorted(reg.keys()):\n    if 'bce' in k.lower() and '30' in k:\n        m = reg[k][\"metrics\"]\n        print(f\"  {k}: {list(m.keys())[:6]}...\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 4: 30% BCE uniform (3-seed)\")\nprint(\"  Paper says exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\")\nprint(\"  But these map to bce_isocompute_v3_* which are 50% sparsity!\")\nprint(\"  The paper's 30% BCE uniform row uses bce_30_s42_uniform_eval (single seed)\")\nprint(\"=\" * 80)\n\n# Actually wait - re-read the paper. The comment says:\n# \"bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\"\n# But in the registry these are bce_isocompute_v3_s42_eval etc.\n# Let me check their PPLs\nevals = [\"bce_isocompute_v3_s42_eval\", \"bce_isocompute_v3_s123_eval\", \"bce_isocompute_v3_s456_eval\"]\nfor e in evals:\n    d = reg[e][\"metrics\"]\n    ppl_key = \"wikitext2_ppl\" if \"wikitext2_ppl\" in d else \"teal_sparse_ppl\"\n    print(f\"  {e}: PPL={d.get(ppl_key, 'N/A')}, ARC-c={d.get('arc_challenge_acc_norm', 'N/A')}\")\n\n# These have PPL ~28 which is 50%. So the paper comment is wrong about the exp_ids for 30% BCE uniform.\n# The 30% BCE uniform is from bce_30_s42_uniform_eval only. Paper claims 3-seed but registry only has 1 seed.\n\nprint()\nprint(\"  CONCLUSION: Paper claims 3-seed for 30% BCE uniform (PPL 15.09±0.13)\")\nprint(\"  Registry only has bce_30_s42_uniform_eval with PPL=15.71 (single seed)\")\nprint(\"  CANNOT VERIFY 3-seed claim. Single seed PPL is 15.71 vs paper mean 15.09\")\nprint()\n\nprint(\"=\" * 80)\nprint(\"ROW 5: 30% MSE uniform (3-seed)\")\nprint(\"=\" * 80)\n# mse30_s42_eval_7task, mse30_s123_downstream, mse30_s456_downstream\ns42 = reg[\"mse30_s42_eval_7task\"][\"metrics\"]\ns123 = reg[\"mse30_s123_downstream\"][\"metrics\"]\ns456 = reg[\"mse30_s456_downstream\"][\"metrics\"]\n\n# PPL\nppls = [s42[\"wikitext2_ppl\"], reg[\"mse30_s123\"][\"metrics\"][\"ppl\"], reg[\"mse30_s456\"][\"metrics\"][\"ppl\"]]\nm, s = mean_std(ppls)\nprint(f\"PPL: paper=18.52±1.68, computed mean={m}±{s} from {ppls}\")\nprint(f\"  -> {'MATCH' if m == 18.52 and s == 1.68 else 'MISMATCH'}\")\n# Let me compute more precisely\nm_precise = sum(ppls)/3\ns_precise = math.sqrt(sum((v-m_precise)**2 for v in ppls)/2)\nprint(f\"  Precise: mean={round(m_precise,2)}, std={round(s_precise,2)}\")\n\n# ARC-c\narcs = [s42[\"arc_challenge_acc_norm\"], s123[\"arc_challenge_acc_norm\"], s456[\"arc_challenge_acc_norm\"]]\narcs_pct = [x*100 for x in arcs]\nm, s = mean_std(arcs_pct)\nprint(f\"ARC-c: paper=35.8±4.1, computed={m}±{s} from {[round(x,2) for x in arcs_pct]}\")\n\n# WG\nwgs = [s42[\"winogrande_acc\"], s123[\"winogrande_acc\"], s456[\"winogrande_acc\"]]\nwgs_pct = [x*100 for x in wgs]\nm, s = mean_std(wgs_pct)\nprint(f\"WG: paper=59.8±2.6, computed={m}±{s} from {[round(x,2) for x in wgs_pct]}\")\n\n# MMLU\nmmlus = [s42[\"mmlu_acc\"], s123[\"mmlu_acc\"], s456[\"mmlu_acc\"]]\nmmlus_pct = [x*100 for x in mmlus]\nm, s = mean_std(mmlus_pct)\nprint(f\"MMLU: paper=30.7±2.6, computed={m}±{s} from {[round(x,2) for x in mmlus_pct]}\")\n\n# GSM8K\ngsms = [s42[\"gsm8k_exact_match\"], s123[\"gsm8k_exact_match\"], s456[\"gsm8k_exact_match\"]]\ngsms_pct = [x*100 for x in gsms]\nm, s = mean_std(gsms_pct)\nprint(f\"GSM8K: paper=2.3±0.7, computed={m}±{s} from {[round(x,2) for x in gsms_pct]}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 6: 30% KL global (3-seed)\")\nprint(\"=\" * 80)\n# bench_kl30_global, kl30_s123_global_v3, kl30_s456_global_v3\n# Only bench_kl30_global is in registry. Check for others.\nprint(\"Looking for kl30 global seeds...\")\nfor k in sorted(reg.keys()):\n    if 'kl30' in k.lower() and ('global' in k.lower()):\n        print(f\"  {k}: {list(reg[k]['metrics'].keys())[:6]}\")\n\n# Only bench_kl30_global exists. kl30_s123_global_v3 and kl30_s456_global_v3 not in registry.\ns42 = reg[\"bench_kl30_global\"][\"metrics\"]\nprint(f\"\\nOnly bench_kl30_global found. Single seed:\")\nprint(f\"  PPL={round(s42['wikitext2_ppl'],2)}, ARC-c={pct(s42['arc_challenge_acc_norm'])}, WG={pct(s42['winogrande_acc'])}, MMLU={pct(s42['mmlu_acc'])}, GSM8K={pct(s42['gsm8k_exact_match'])}\")\nprint(f\"  Paper claims 3-seed: PPL=8.96±0.02, ARC-c=43.8±3.6, WG=70.2±0.9, MMLU=35.7±9.5, GSM8K=8.0±0.7\")\nprint(f\"  Single seed PPL=8.98 is consistent with mean 8.96\")\nprint(f\"  CANNOT fully verify 3-seed - only 1 seed in registry\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 7: 30% KL uniform (3-seed)\")\nprint(\"=\" * 80)\n# bench_kl30_uniform, kl30_s123_eval, kl30_s456_uniform_eval\ns42 = reg[\"bench_kl30_uniform\"][\"metrics\"]\ns123 = reg[\"kl30_s123_eval\"][\"metrics\"]\ns456 = reg[\"kl30_s456_uniform_eval\"][\"metrics\"]\n\nppls = [s42[\"wikitext2_ppl\"], s123[\"wikitext2_ppl\"], s456[\"ppl_uniform\"]]\nm_precise = sum(ppls)/3\ns_precise = math.sqrt(sum((v-m_precise)**2 for v in ppls)/2)\nprint(f\"PPL: paper=8.81±0.02, computed={round(m_precise,2)}±{round(s_precise,2)} from {[round(x,4) for x in ppls]}\")\n\narcs = [s42[\"arc_challenge_acc_norm\"], s123[\"arc_challenge_acc_norm\"], s456[\"arc_challenge\"]]\narcs_pct = [x*100 for x in arcs]\nm, s = mean_std(arcs_pct)\nprint(f\"ARC-c: paper=43.7±2.5, computed={m}±{s} from {[round(x,2) for x in arcs_pct]}\")\n\nwgs = [s42[\"winogrande_acc\"], s123[\"winogrande_acc\"], s456[\"winogrande\"]]\nwgs_pct = [x*100 for x in wgs]\nm, s = mean_std(wgs_pct)\nprint(f\"WG: paper=68.9±0.4, computed={m}±{s} from {[round(x,2) for x in wgs_pct]}\")\n\nmmlus = [s42[\"mmlu_acc\"], s123[\"mmlu_acc\"], s456[\"mmlu\"]]\nmmlus_pct = [x*100 for x in mmlus]\nm, s = mean_std(mmlus_pct)\nprint(f\"MMLU: paper=40.7±1.3, computed={m}±{s} from {[round(x,2) for x in mmlus_pct]}\")\n\ngsms = [s42[\"gsm8k_exact_match\"], s123[\"gsm8k_exact_match\"], s456[\"gsm8k\"]]\ngsms_pct = [x*100 for x in gsms]\nm, s = mean_std(gsms_pct)\nprint(f\"GSM8K: paper=7.5±0.1, computed={m}±{s} from {[round(x,2) for x in gsms_pct]}\")\n\nPYEOF\n",
  "description": "Verify MSE 30%, KL 30% global, KL 30% uniform numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b331a14-69d6-4601-8011-cfcb7c26454c",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3QR4nrgvDaJLfdXcFA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da5f6332-cb79-4b44-a9c9-1126a8546788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GskwetpFhhLSTB2Piou51o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 51546,
      "output_tokens": 2868,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2868,
          "cache_read_input_tokens": 51546,
          "cache_creation_input_tokens": 3138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3138,
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

_source line 12 · 2026-05-23T19:21:02.670Z_

<details><summary>↩ Tool result · `toolu_01REJzYsFVuYQVmNSAY3jhyn`</summary>

```text
Looking for BCE 30% uniform multi-seed entries...
  bce_30_s42_uniform_eval: ['ppl', 'arc_challenge', 'winogrande', 'mmlu', 'gsm8k', 'hellaswag']...
  bce_30pct_s42: []...
  bce_30pct_s42_eval: ['wikitext2_ppl', 'arc_challenge_acc', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'gsm8k_exact_match']...
  qwen14b_bce30_s42_eval: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'gsm8k_exact_match']...

================================================================================
ROW 4: 30% BCE uniform (3-seed)
  Paper says exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456
  But these map to bce_isocompute_v3_* which are 50% sparsity!
  The paper's 30% BCE uniform row uses bce_30_s42_uniform_eval (single seed)
================================================================================
  bce_isocompute_v3_s42_eval: PPL=27.9696, ARC-c=0.2765
  bce_isocompute_v3_s123_eval: PPL=28.0627, ARC-c=0.2696
  bce_isocompute_v3_s456_eval: PPL=28.3503, ARC-c=0.2807

  CONCLUSION: Paper claims 3-seed for 30% BCE uniform (PPL 15.09±0.13)
  Registry only has bce_30_s42_uniform_eval with PPL=15.71 (single seed)
  CANNOT VERIFY 3-seed claim. Single seed PPL is 15.71 vs paper mean 15.09

================================================================================
ROW 5: 30% MSE uniform (3-seed)
================================================================================
PPL: paper=18.52±1.68, computed mean=18.52±1.67 from [20.43, 17.7313, 17.3888]
  -> MISMATCH
  Precise: mean=18.52, std=1.67
ARC-c: paper=35.8±4.1, computed=35.81±4.03 from [31.23, 37.37, 38.82]
WG: paper=59.8±2.6, computed=59.78±2.54 from [60.38, 56.99, 61.96]
MMLU: paper=30.7±2.6, computed=30.75±2.58 from [31.79, 27.81, 32.64]
GSM8K: paper=2.3±0.7, computed=2.27±0.73 from [1.97, 1.74, 3.11]

================================================================================
ROW 6: 30% KL global (3-seed)
================================================================================
Looking for kl30 global seeds...
  bench_kl30_global: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'gsm8k_exact_match', 'actual_sparsity']
  qwen14b_kl30_global_hspiqa: ['hellaswag_acc_norm', 'piqa_acc_norm']

Only bench_kl30_global found. Single seed:
  PPL=8.98, ARC-c=39.68, WG=70.17, MMLU=25.27, GSM8K=8.79
  Paper claims 3-seed: PPL=8.96±0.02, ARC-c=43.8±3.6, WG=70.2±0.9, MMLU=35.7±9.5, GSM8K=8.0±0.7
  Single seed PPL=8.98 is consistent with mean 8.96
  CANNOT fully verify 3-seed - only 1 seed in registry

================================================================================
ROW 7: 30% KL uniform (3-seed)
================================================================================
PPL: paper=8.81±0.02, computed=8.81±0.02 from [8.8157, 8.8308, 8.7947]
ARC-c: paper=43.7±2.5, computed=43.71±2.54 from [40.78, 45.31, 45.05]
WG: paper=68.9±0.4, computed=68.91±0.42 from [68.59, 69.38, 68.75]
MMLU: paper=40.7±1.3, computed=40.68±1.27 from [40.61, 39.44, 41.98]
GSM8K: paper=7.5±0.1, computed=7.48±0.12 from [7.35, 7.51, 7.58]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da5f6332-cb79-4b44-a9c9-1126a8546788",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "fafce22c-4e67-4f73-97ed-8ef36d2dfe0f",
  "sourceToolAssistantUUID": "da5f6332-cb79-4b44-a9c9-1126a8546788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:21:43.341Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LX39r1LuAzfSdq71gXGYDV`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\ndef pct(x): return round(x * 100, 2)\ndef mean_std(vals):\n    m = sum(vals) / len(vals)\n    if len(vals) > 1:\n        s = math.sqrt(sum((v - m)**2 for v in vals) / (len(vals) - 1))\n    else:\n        s = 0\n    return round(m, 2), round(s, 2)\n\nprint(\"=\" * 80)\nprint(\"ROW 8: 50% TEAL uniform\")\nprint(\"=\" * 80)\nd = reg[\"bench_teal50_uniform_6task\"][\"metrics\"]\nprint(f\"PPL: paper=23.90, registry={round(d['wikitext2_ppl'],2)} -> {'MATCH' if round(d['wikitext2_ppl'],2) == 23.90 else 'MISMATCH'}\")\nprint(f\"ARC-c: paper=27.47, registry={pct(d['arc_challenge_acc_norm'])} -> {'MATCH' if pct(d['arc_challenge_acc_norm']) == 27.47 else 'MISMATCH'}\")\nprint(f\"WG: paper=54.38, registry={pct(d['winogrande_acc'])} -> {'MATCH' if pct(d['winogrande_acc']) == 54.38 else 'MISMATCH'}\")\nprint(f\"MMLU: paper=29.26, registry={pct(d['mmlu_acc'])} -> {'MATCH' if pct(d['mmlu_acc']) == 29.26 else 'MISMATCH'}\")\n# GSM8K - check bench_teal50\nd2 = reg[\"bench_teal50\"][\"metrics\"]\nprint(f\"GSM8K: paper=1.74, bench_teal50={pct(d2['gsm8k_exact_match'])} -> {'MATCH' if pct(d2['gsm8k_exact_match']) == 1.74 else 'MISMATCH: paper=1.74, registry=' + str(pct(d2['gsm8k_exact_match']))}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 9: 50% BCE (2700 steps) (3-seed)\")\nprint(\"=\" * 80)\n# bce_isocompute_v3_s42_eval, bce_isocompute_v3_s123_eval, bce_isocompute_v3_s456_eval\ns42 = reg[\"bce_isocompute_v3_s42_eval\"][\"metrics\"]\ns123 = reg[\"bce_isocompute_v3_s123_eval\"][\"metrics\"]\ns456 = reg[\"bce_isocompute_v3_s456_eval\"][\"metrics\"]\n\nppls = [s42[\"wikitext2_ppl\"], s123[\"wikitext2_ppl\"], s456[\"teal_sparse_ppl\"]]\nm, s = mean_std(ppls)\nprint(f\"PPL: paper=28.13±0.20, computed={m}±{s} from {[round(x,2) for x in ppls]}\")\n\narcs = [s42[\"arc_challenge_acc_norm\"], s123[\"arc_challenge_acc_norm\"], s456[\"arc_challenge_acc_norm\"]]\narcs_pct = [x*100 for x in arcs]\nm, s = mean_std(arcs_pct)\nprint(f\"ARC-c: paper=27.6±0.6, computed={m}±{s} from {[round(x,2) for x in arcs_pct]}\")\n\nwgs = [s42[\"winogrande_acc\"], s123[\"winogrande_acc\"], s456[\"winogrande_acc\"]]\nwgs_pct = [x*100 for x in wgs]\nm, s = mean_std(wgs_pct)\nprint(f\"WG: paper=51.8±0.6, computed={m}±{s} from {[round(x,2) for x in wgs_pct]}\")\n\nmmlus = [s42[\"mmlu_acc\"], s123[\"mmlu_acc\"], s456[\"mmlu_acc\"]]\nmmlus_pct = [x*100 for x in mmlus]\nm, s = mean_std(mmlus_pct)\nprint(f\"MMLU: paper=26.1±0.5, computed={m}±{s} from {[round(x,2) for x in mmlus_pct]}\")\n\ngsms = [s42[\"gsm8k_exact_match\"], s123[\"gsm8k_exact_match\"], s456[\"gsm8k_exact_match\"]]\ngsms_pct = [x*100 for x in gsms]\nm, s = mean_std(gsms_pct)\nprint(f\"GSM8K: paper=2.1±0.2, computed={m}±{s} from {[round(x,2) for x in gsms_pct]}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 10: 50% MSE uniform (single seed)\")\nprint(\"=\" * 80)\nd = reg[\"mse50_s42_eval_7task\"][\"metrics\"]\nprint(f\"PPL: paper=229.26, registry={round(d['wikitext2_ppl'],2)} -> {'MATCH' if round(d['wikitext2_ppl'],2) == 229.26 else 'MISMATCH'}\")\nprint(f\"ARC-c: paper=25.00, registry={pct(d['arc_challenge_acc_norm'])} -> {'MATCH' if pct(d['arc_challenge_acc_norm']) == 25.00 else 'MISMATCH'}\")\nprint(f\"WG: paper=50.59, registry={pct(d['winogrande_acc'])} -> {'MATCH' if pct(d['winogrande_acc']) == 50.59 else 'MISMATCH'}\")\nprint(f\"MMLU: paper=23.79, registry={pct(d['mmlu_acc'])} -> {'MATCH' if pct(d['mmlu_acc']) == 23.79 else 'MISMATCH'}\")\nprint(f\"GSM8K: paper=1.59, registry={pct(d['gsm8k_exact_match'])} -> {'MATCH' if pct(d['gsm8k_exact_match']) == 1.59 else 'MISMATCH'}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 11: 50% KL global (3-seed)\")\nprint(\"=\" * 80)\n# bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\ns42 = reg[\"bench_kl50_global\"][\"metrics\"]\ns123 = reg[\"kl50_global_s123_downstream_v2\"][\"metrics\"]\ns456 = reg[\"kl50_global_s456_eval\"][\"metrics\"]\n\n# PPL: s123 doesn't have PPL\nppls_available = [s42[\"wikitext2_ppl\"], s456[\"wikitext2_ppl\"]]\nprint(f\"PPL: paper=11.84±0.15\")\nprint(f\"  s42={s42['wikitext2_ppl']}, s123=NO PPL, s456={s456['wikitext2_ppl']}\")\n# Check if there's another s123 entry with PPL\nfor k in sorted(reg.keys()):\n    if 'kl50' in k and 's123' in k:\n        m = reg[k][\"metrics\"]\n        if 'wikitext2_ppl' in m:\n            print(f\"  Found {k} with PPL={m['wikitext2_ppl']}\")\n\n# Try computing with just s42 and s456, see if a third seed ~11.75 would make it work\n# s42=11.7933, s456=12.01 -> if s123 were ~11.72, mean would be ~11.84\n# Let me assume the paper used a value for s123 PPL not in registry\nprint(f\"  With s42=11.79, s456=12.01, paper mean=11.84 implies s123~11.73\")\nprint(f\"  PARTIALLY VERIFIABLE (s123 PPL missing from registry)\")\n\n# Downstream\narcs = [s42[\"arc_challenge_acc_norm\"], s123[\"arc_challenge_acc_norm\"], s456[\"arc_challenge_acc_norm\"]]\narcs_pct = [x*100 for x in arcs]\nm, s = mean_std(arcs_pct)\nprint(f\"ARC-c: paper=36.3±3.2, computed={m}±{s} from {[round(x,2) for x in arcs_pct]}\")\n\nwgs = [s42[\"winogrande_acc\"], s123[\"winogrande_acc\"], s456[\"winogrande_acc\"]]\nwgs_pct = [x*100 for x in wgs]\nm, s = mean_std(wgs_pct)\nprint(f\"WG: paper=63.8±0.3, computed={m}±{s} from {[round(x,2) for x in wgs_pct]}\")\n\nmmlus = [s42[\"mmlu_acc\"], s123[\"mmlu_acc\"], s456[\"mmlu_acc\"]]\nmmlus_pct = [x*100 for x in mmlus]\nm, s = mean_std(mmlus_pct)\nprint(f\"MMLU: paper=28.3±0.7, computed={m}±{s} from {[round(x,2) for x in mmlus_pct]}\")\n\ngsms = [s42[\"gsm8k_exact_match\"], s123[\"gsm8k_exact_match\"], s456[\"gsm8k_exact_match\"]]\ngsms_pct = [x*100 for x in gsms]\nm, s = mean_std(gsms_pct)\nprint(f\"GSM8K: paper=2.7±1.3, computed={m}±{s} from {[round(x,2) for x in gsms_pct]}\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"ROW 12: 50% KL uniform (3-seed)\")\nprint(\"=\" * 80)\n# bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456\ns42 = reg[\"bench_kl50_uniform\"][\"metrics\"]\ns123 = reg[\"bench_kl50_uniform_s123\"][\"metrics\"]\ns456 = reg[\"bench_kl50_uniform_s456\"][\"metrics\"]\n\nppls = [s42[\"wikitext2_ppl\"], s123[\"wikitext2_ppl\"], s456[\"wikitext2_ppl\"]]\nm, s = mean_std(ppls)\nprint(f\"PPL: paper=11.92±0.07, computed={m}±{s} from {[round(x,4) for x in ppls]}\")\n\narcs = [s42[\"arc_challenge_acc_norm\"], s123[\"arc_challenge_acc_norm\"], s456[\"arc_challenge_acc_norm\"]]\narcs_pct = [x*100 for x in arcs]\nm, s = mean_std(arcs_pct)\nprint(f\"ARC-c: paper=33.8±1.2, computed={m}±{s} from {[round(x,2) for x in arcs_pct]}\")\n\nwgs = [s42[\"winogrande_acc\"], s123[\"winogrande_acc\"], s456[\"winogrande_acc\"]]\nwgs_pct = [x*100 for x in wgs]\nm, s = mean_std(wgs_pct)\nprint(f\"WG: paper=62.9±0.1, computed={m}±{s} from {[round(x,2) for x in wgs_pct]}\")\n\nmmlus = [s42[\"mmlu_acc\"], s123[\"mmlu_acc\"], s456[\"mmlu_acc\"]]\nmmlus_pct = [x*100 for x in mmlus]\nm, s = mean_std(mmlus_pct)\nprint(f\"MMLU: paper=28.0±0.6, computed={m}±{s} from {[round(x,2) for x in mmlus_pct]}\")\n\ngsms = [s42[\"gsm8k_exact_match\"], s123[\"gsm8k_exact_match\"], s456[\"gsm8k_exact_match\"]]\ngsms_pct = [x*100 for x in gsms]\nm, s = mean_std(gsms_pct)\nprint(f\"GSM8K: paper=2.2±0.1, computed={m}±{s} from {[round(x,2) for x in gsms_pct]}\")\n\nPYEOF\n",
  "description": "Verify 50% rows: TEAL, BCE, MSE, KL global, KL uniform"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fafce22c-4e67-4f73-97ed-8ef36d2dfe0f",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3TKEdsSWiwFM9u7P7v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b5ebf36-5687-40b1-b9f7-a85b50b9ea5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtD6F31T5Xs5fNKn1234pL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4174,
      "cache_read_input_tokens": 54684,
      "output_tokens": 3410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3410,
          "cache_read_input_tokens": 54684,
          "cache_creation_input_tokens": 4174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4174,
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

_source line 14 · 2026-05-23T19:21:43.445Z_

<details><summary>↩ Tool result · `toolu_01LX39r1LuAzfSdq71gXGYDV`</summary>

```text
================================================================================
ROW 8: 50% TEAL uniform
================================================================================
PPL: paper=23.90, registry=23.9 -> MATCH
ARC-c: paper=27.47, registry=27.47 -> MATCH
WG: paper=54.38, registry=54.38 -> MATCH
MMLU: paper=29.26, registry=29.26 -> MATCH
GSM8K: paper=1.74, bench_teal50=1.97 -> MISMATCH: paper=1.74, registry=1.97

================================================================================
ROW 9: 50% BCE (2700 steps) (3-seed)
================================================================================
PPL: paper=28.13±0.20, computed=28.13±0.2 from [27.97, 28.06, 28.35]
ARC-c: paper=27.6±0.6, computed=27.56±0.56 from [27.65, 26.96, 28.07]
WG: paper=51.8±0.6, computed=51.78±0.57 from [51.62, 51.3, 52.41]
MMLU: paper=26.1±0.5, computed=26.12±0.44 from [26.14, 26.55, 25.67]
GSM8K: paper=2.1±0.2, computed=2.1±0.17 from [1.9, 2.2, 2.2]

================================================================================
ROW 10: 50% MSE uniform (single seed)
================================================================================
PPL: paper=229.26, registry=229.26 -> MATCH
ARC-c: paper=25.00, registry=25.0 -> MATCH
WG: paper=50.59, registry=50.59 -> MATCH
MMLU: paper=23.79, registry=23.79 -> MATCH
GSM8K: paper=1.59, registry=1.59 -> MATCH

================================================================================
ROW 11: 50% KL global (3-seed)
================================================================================
PPL: paper=11.84±0.15
  s42=11.7933, s123=NO PPL, s456=12.01
  Found bench_kl50_uniform_s123 with PPL=11.83
  With s42=11.79, s456=12.01, paper mean=11.84 implies s123~11.73
  PARTIALLY VERIFIABLE (s123 PPL missing from registry)
ARC-c: paper=36.3±3.2, computed=36.3±3.2 from [32.85, 39.16, 36.9]
WG: paper=63.8±0.3, computed=63.82±0.31 from [63.46, 64.01, 64.0]
MMLU: paper=28.3±0.7, computed=28.32±0.66 from [27.89, 29.08, 28.0]
GSM8K: paper=2.7±1.3, computed=2.73±1.25 from [1.29, 3.41, 3.5]

================================================================================
ROW 12: 50% KL uniform (3-seed)
================================================================================
PPL: paper=11.92±0.07, computed=11.92±0.08 from [11.963, 11.83, 11.9604]
ARC-c: paper=33.8±1.2, computed=33.79±1.23 from [32.76, 35.15, 33.45]
WG: paper=62.9±0.1, computed=62.88±0.12 from [62.9, 62.98, 62.75]
MMLU: paper=28.0±0.6, computed=28.01±0.65 from [27.77, 27.51, 28.74]
GSM8K: paper=2.2±0.1, computed=2.2±0.13 from [2.12, 2.35, 2.12]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b5ebf36-5687-40b1-b9f7-a85b50b9ea5e",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "b5412a0d-46ea-4b3b-8042-fb653f5daa1c",
  "sourceToolAssistantUUID": "2b5ebf36-5687-40b1-b9f7-a85b50b9ea5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-23T19:21:46.601Z_

Now let me verify the derived claims and check the TEAL GSM8K discrepancy more closely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5412a0d-46ea-4b3b-8042-fb653f5daa1c",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3WKaobQPA89327Aegg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96acb07b-3851-40d3-a096-cdf2e0b9ac04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjyXcWpEe4iWnrJE54ALAm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4434,
      "cache_read_input_tokens": 58858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4434,
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

_source line 16 · 2026-05-23T19:22:22.793Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RetGEPrJPA1YeykmrisU6D`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, math\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\nprint(\"=\" * 80)\nprint(\"TEAL GSM8K DISCREPANCIES\")\nprint(\"=\" * 80)\nprint()\nprint(\"30% TEAL GSM8K:\")\nprint(f\"  bench_teal30_uniform_6task: no GSM8K field\")\nt30_6 = reg[\"bench_teal30_uniform_6task\"][\"metrics\"]\nprint(f\"    Keys: {list(t30_6.keys())}\")\nprint(f\"  bench_teal30: gsm8k={reg['bench_teal30']['metrics']['gsm8k_exact_match']} = {round(reg['bench_teal30']['metrics']['gsm8k_exact_match']*100,2)}%\")\nprint(f\"  Paper says 8.79% but bench_teal30 gives 7.88%\")\nprint(f\"  MISMATCH: paper=8.79, registry=7.88 (bench_teal30)\")\nprint()\n\nprint(\"50% TEAL GSM8K:\")\nprint(f\"  bench_teal50_uniform_6task: no GSM8K field\")\nt50_6 = reg[\"bench_teal50_uniform_6task\"][\"metrics\"]\nprint(f\"    Keys: {list(t50_6.keys())}\")\nprint(f\"  bench_teal50: gsm8k={reg['bench_teal50']['metrics']['gsm8k_exact_match']} = {round(reg['bench_teal50']['metrics']['gsm8k_exact_match']*100,2)}%\")\nprint(f\"  Paper says 1.74% but bench_teal50 gives 1.97%\")\nprint(f\"  MISMATCH: paper=1.74, registry=1.97 (bench_teal50)\")\nprint()\nprint(\"  NOTE: bench_teal30/50 use global allocation, bench_teal30/50_uniform_6task use uniform.\")\nprint(\"  Paper's Table 3 is labeled 'TEAL uniform' but GSM8K numbers might come from a different eval run.\")\nprint(\"  The bench_teal30_uniform_6task and bench_teal50_uniform_6task entries don't have GSM8K.\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"DERIVED CLAIM 1: '14.5% reduction' = (10.30 - 8.81) / 10.30\")\nprint(\"=\" * 80)\n# Paper says \"8.81 vs 10.30, both at 28.5%\"\n# Where does 10.30 come from? Not from table. Let me check text more carefully.\n# \"8.81 vs. 10.30, both at 28.5%\" - 10.30 is TEAL at matched actual sparsity 28.5%\n# bench_teal30_uniform_6task PPL = 10.82 (at 30% target, ~29.3% actual)\n# This suggests a different TEAL evaluation at 28.5% actual sparsity\n\nreduction = (10.30 - 8.81) / 10.30 * 100\nprint(f\"  (10.30 - 8.81) / 10.30 = {round(reduction, 1)}%\")\nprint(f\"  Paper claims 14.5%\")\nprint(f\"  Computed: {round(reduction, 1)}% -> MATCH\")\nprint()\nprint(\"  Note: 10.30 is referenced as TEAL at matched 28.5% actual sparsity.\")\nprint(\"  This value is NOT in Table 3 (which shows 10.82 at 30% target).\")\nprint(\"  Would need to verify 10.30 from appendix/OOD data.\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"DERIVED CLAIM 2: '50% reduction at 50%' = (23.90 - 11.92) / 23.90\")\nprint(\"=\" * 80)\nreduction_50 = (23.90 - 11.92) / 23.90 * 100\nprint(f\"  (23.90 - 11.92) / 23.90 = {round(reduction_50, 1)}%\")\nprint(f\"  Paper claims 50% reduction\")\nprint(f\"  Computed: {round(reduction_50, 1)}% -> MATCH\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"BCE GLOBAL 30% - ROUNDING CHECKS\")\nprint(\"=\" * 80)\nd = reg[\"bce_30pct_s42_eval\"][\"metrics\"]\nprint(f\"  PPL: registry=11.2445, paper=11.25 -> rounds correctly (1 decimal)\")\nprint(f\"  ARC-c: registry={d['arc_challenge_acc_norm']*100:.2f}%, paper=41.2 -> rounds correctly\")\nprint(f\"  WG: registry={d['winogrande_acc']*100:.2f}%, paper=66.0 -> rounds correctly (65.98->66.0)\")\nprint(f\"  MMLU: registry={d['mmlu_acc']*100:.2f}%, paper=36.3 -> rounds correctly\")\nprint(f\"  GSM8K: registry={d['gsm8k_exact_match']*100:.2f}%, paper=6.0 -> rounds correctly (5.99->6.0)\")\nprint(f\"  ALL acceptable rounding\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"MSE 30% 3-seed ROUNDING CHECKS\")\nprint(\"=\" * 80)\n# Exact values: PPL mean=18.52 std=1.67 (paper: 1.68)\n# The std rounding: 1.6726... rounds to 1.67 not 1.68\nppls = [20.43, 17.7313, 17.3888]\nm = sum(ppls)/3\ns = math.sqrt(sum((v-m)**2 for v in ppls)/2)\nprint(f\"  PPL std exact: {s:.4f}, rounds to {round(s,2)}\")\nprint(f\"  Paper says 1.68, computed 1.67 -> minor rounding (1.6726 is borderline)\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"50% KL global: downstream rounding checks\")  \nprint(\"=\" * 80)\n# ARC: paper 36.3±3.2 computed 36.30±3.20 MATCH\n# WG: paper 63.8±0.3 computed 63.82±0.31 -> 63.82 rounds to 63.8 OK, 0.31 vs 0.3 borderline\n# MMLU: paper 28.3±0.7 computed 28.32±0.66 -> 0.66 rounds to 0.7 OK\n# GSM8K: paper 2.7±1.3 computed 2.73±1.25 -> 1.25 rounds to 1.3? That's a stretch. \ngsms_pct = [1.29, 3.41, 3.50]\nm = sum(gsms_pct)/3\ns = math.sqrt(sum((v-m)**2 for v in gsms_pct)/2)\nprint(f\"  GSM8K: mean={m:.2f}, std={s:.4f}\")\nprint(f\"  Paper says 2.7±1.3, computed 2.73±1.25\")\nprint(f\"  std 1.2468 rounds to 1.2, not 1.3 -> minor discrepancy\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"50% KL uniform: rounding checks\")\nprint(\"=\" * 80)\nppls = [11.963, 11.83, 11.9604]\nm = sum(ppls)/3\ns = math.sqrt(sum((v-m)**2 for v in ppls)/2)\nprint(f\"  PPL: mean={m:.4f}, std={s:.4f}\")\nprint(f\"  Paper says 11.92±0.07, computed 11.92±0.08\")\nprint(f\"  std 0.0753 rounds to 0.08, not 0.07 -> minor discrepancy\")\n\n# GSM8K\ngsms_pct = [2.12, 2.35, 2.12]\nm = sum(gsms_pct)/3\ns = math.sqrt(sum((v-m)**2 for v in gsms_pct)/2)\nprint(f\"  GSM8K: mean={m:.4f}, std={s:.4f}\")\nprint(f\"  Paper says 2.2±0.1, computed 2.20±0.13\")\nprint(f\"  std 0.1328 rounds to 0.1 -> borderline\")\n\nPYEOF\n",
  "description": "Verify derived claims and check rounding edge cases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96acb07b-3851-40d3-a096-cdf2e0b9ac04",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3WKaobQPA89327Aegg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e55557f0-9b85-4887-abdc-97384eab240b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjyXcWpEe4iWnrJE54ALAm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4434,
      "cache_read_input_tokens": 58858,
      "output_tokens": 2339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2339,
          "cache_read_input_tokens": 58858,
          "cache_creation_input_tokens": 4434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4434,
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

_source line 17 · 2026-05-23T19:22:22.915Z_

<details><summary>↩ Tool result · `toolu_01RetGEPrJPA1YeykmrisU6D`</summary>

```text
================================================================================
TEAL GSM8K DISCREPANCIES
================================================================================

30% TEAL GSM8K:
  bench_teal30_uniform_6task: no GSM8K field
    Keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc_norm', 'piqa_acc_norm', 'actual_sparsity']
  bench_teal30: gsm8k=0.0788 = 7.88%
  Paper says 8.79% but bench_teal30 gives 7.88%
  MISMATCH: paper=8.79, registry=7.88 (bench_teal30)

50% TEAL GSM8K:
  bench_teal50_uniform_6task: no GSM8K field
    Keys: ['wikitext2_ppl', 'arc_challenge_acc_norm', 'winogrande_acc', 'mmlu_acc', 'hellaswag_acc_norm', 'piqa_acc_norm']
  bench_teal50: gsm8k=0.0197 = 1.97%
  Paper says 1.74% but bench_teal50 gives 1.97%
  MISMATCH: paper=1.74, registry=1.97 (bench_teal50)

  NOTE: bench_teal30/50 use global allocation, bench_teal30/50_uniform_6task use uniform.
  Paper's Table 3 is labeled 'TEAL uniform' but GSM8K numbers might come from a different eval run.
  The bench_teal30_uniform_6task and bench_teal50_uniform_6task entries don't have GSM8K.

================================================================================
DERIVED CLAIM 1: '14.5% reduction' = (10.30 - 8.81) / 10.30
================================================================================
  (10.30 - 8.81) / 10.30 = 14.5%
  Paper claims 14.5%
  Computed: 14.5% -> MATCH

  Note: 10.30 is referenced as TEAL at matched 28.5% actual sparsity.
  This value is NOT in Table 3 (which shows 10.82 at 30% target).
  Would need to verify 10.30 from appendix/OOD data.

================================================================================
DERIVED CLAIM 2: '50% reduction at 50%' = (23.90 - 11.92) / 23.90
================================================================================
  (23.90 - 11.92) / 23.90 = 50.1%
  Paper claims 50% reduction
  Computed: 50.1% -> MATCH

================================================================================
BCE GLOBAL 30% - ROUNDING CHECKS
================================================================================
  PPL: registry=11.2445, paper=11.25 -> rounds correctly (1 decimal)
  ARC-c: registry=41.21%, paper=41.2 -> rounds correctly
  WG: registry=65.98%, paper=66.0 -> rounds correctly (65.98->66.0)
  MMLU: registry=36.33%, paper=36.3 -> rounds correctly
  GSM8K: registry=5.99%, paper=6.0 -> rounds correctly (5.99->6.0)
  ALL acceptable rounding

================================================================================
MSE 30% 3-seed ROUNDING CHECKS
================================================================================
  PPL std exact: 1.6658, rounds to 1.67
  Paper says 1.68, computed 1.67 -> minor rounding (1.6726 is borderline)

================================================================================
50% KL global: downstream rounding checks
================================================================================
  GSM8K: mean=2.73, std=1.2508
  Paper says 2.7±1.3, computed 2.73±1.25
  std 1.2468 rounds to 1.2, not 1.3 -> minor discrepancy

================================================================================
50% KL uniform: rounding checks
================================================================================
  PPL: mean=11.9178, std=0.0760
  Paper says 11.92±0.07, computed 11.92±0.08
  std 0.0753 rounds to 0.08, not 0.07 -> minor discrepancy
  GSM8K: mean=2.1967, std=0.1328
  Paper says 2.2±0.1, computed 2.20±0.13
  std 0.1328 rounds to 0.1 -> borderline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e55557f0-9b85-4887-abdc-97384eab240b",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "f4fa85eb-9192-4f93-8a47-7759a9de1c99",
  "sourceToolAssistantUUID": "e55557f0-9b85-4887-abdc-97384eab240b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-23T19:22:26.016Z_

Now let me search for additional TEAL GSM8K eval entries that might explain the discrepancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4fa85eb-9192-4f93-8a47-7759a9de1c99",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3ZELNThr9ncdu6sYiK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c3e794-f78b-45c3-b1be-a97de105d3ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01538Q5sWuqRxQGauYNnHPpg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 63292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3488,
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

_source line 19 · 2026-05-23T19:22:35.655Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01L2Z3mgBZdytN6rDA1JqPk9`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\n# Check if there are any other teal entries we missed\nprint(\"All TEAL-related entries:\")\nfor k in sorted(reg.keys()):\n    if 'teal' in k.lower() and 'qwen' not in k.lower() and 'mistral' not in k.lower():\n        m = reg[k][\"metrics\"]\n        gsm = m.get(\"gsm8k_exact_match\", m.get(\"gsm8k\", \"N/A\"))\n        print(f\"  {k}: gsm8k={gsm}, conclusion={reg[k]['conclusion']}\")\n\n# Also check the appendix reference for the 10.30 number  \nprint()\nprint(\"Looking for TEAL PPL ~10.30 at 28.5% actual sparsity...\")\nprint(\"  bench_teal30_uniform_6task: PPL=10.82 (actual_sparsity=0.3)\")\nprint(\"  bench_teal30: PPL=10.97 (actual_sparsity=0.3)\")\nprint(\"  Neither shows 10.30 at 28.5%. This might be from appendix data not in registry.\")\n\n# Check for any OOD/appendix references\nprint()\nprint(\"Looking for c4_ood teal entries...\")\nfor k in sorted(reg.keys()):\n    if 'c4' in k.lower() and 'teal' not in k.lower():\n        m = reg[k][\"metrics\"]\n        ppl = m.get(\"c4_ppl\", m.get(\"teal_50_ppl\", \"N/A\"))\n        print(f\"  {k}: ppl={ppl}\")\n\n# Check for any entry with 10.30\nprint()\nprint(\"Entries with PPL near 10.30...\")\nfor k in sorted(reg.keys()):\n    m = reg[k][\"metrics\"]\n    for mk, mv in m.items():\n        if isinstance(mv, (int, float)) and 10.25 <= mv <= 10.35:\n            print(f\"  {k}.{mk} = {mv}\")\n\nPYEOF\n",
  "description": "Search for TEAL GSM8K source and 10.30 PPL reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c3e794-f78b-45c3-b1be-a97de105d3ee",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3ZELNThr9ncdu6sYiK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb48ecab-7a8e-43ea-a6b8-9f4859df4073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01538Q5sWuqRxQGauYNnHPpg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 63292,
      "output_tokens": 657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3488
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 657,
          "cache_read_input_tokens": 63292,
          "cache_creation_input_tokens": 3488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3488,
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

_source line 20 · 2026-05-23T19:22:35.729Z_

<details><summary>↩ Tool result · `toolu_01L2Z3mgBZdytN6rDA1JqPk9`</summary>

```text
All TEAL-related entries:
  bce_50pct_teal_global_unified: gsm8k=0.019, conclusion=success
  bench_teal30: gsm8k=0.0788, conclusion=success
  bench_teal30_uniform_6task: gsm8k=N/A, conclusion=killed
  bench_teal50: gsm8k=0.0197, conclusion=success
  bench_teal50_uniform_6task: gsm8k=N/A, conclusion=killed
  kl_sparsity25_s42_eval_teal: gsm8k=0.1145, conclusion=success
  kl_sparsity25_s42_eval_teal_uniform: gsm8k=0.1099, conclusion=success
  kl_sparsity35_s42_eval_teal: gsm8k=0.0773, conclusion=success
  kl_sparsity35_s42_eval_teal_uniform: gsm8k=0.0432, conclusion=success
  kl_sparsity45_s42_eval_teal: gsm8k=0.0296, conclusion=success
  kl_sparsity45_s42_eval_teal_uniform: gsm8k=0.0273, conclusion=success

Looking for TEAL PPL ~10.30 at 28.5% actual sparsity...
  bench_teal30_uniform_6task: PPL=10.82 (actual_sparsity=0.3)
  bench_teal30: PPL=10.97 (actual_sparsity=0.3)
  Neither shows 10.30 at 28.5%. This might be from appendix data not in registry.

Looking for c4_ood teal entries...
  c4_kl30_s42_eval: ppl=N/A
  c4_ood_downstream_kl30: ppl=N/A
  c4_ood_kl30_s123: ppl=N/A
  c4_ood_kl30_s123_v2: ppl=16.0259
  c4_ood_kl30_s42: ppl=16.0458
  c4_ood_kl30_s42_v2: ppl=16.0401
  c4_ood_kl30_uniform_s123: ppl=16.3686
  c4_ood_kl30_uniform_s42: ppl=18.2211
  c4_ood_kl30_uniform_s456: ppl=16.3551
  eval_c4_ood_kl50: ppl=38.7503

Entries with PPL near 10.30...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb48ecab-7a8e-43ea-a6b8-9f4859df4073",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "9b1cae77-0a79-43bb-969f-84c22b327dfa",
  "sourceToolAssistantUUID": "fb48ecab-7a8e-43ea-a6b8-9f4859df4073",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:23:20.408Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VRwDYEm4B1qztujZtWxUrt`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\n# The 10.30 number is not in the registry. Let me check the appendix\n# Also check for \"bench_kl30_uniform\" KL s42 at bench_kl30_global PPL\nprint(\"KL 30% global s42: bench_kl30_global\")\nd = reg[\"bench_kl30_global\"][\"metrics\"]\nprint(f\"  PPL={d['wikitext2_ppl']}\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f}%\")\nprint(f\"  Note: MMLU 25.27% - paper says mean 35.7±9.5%\")\nprint(f\"  With only 1 seed (25.27%), getting a 3-seed mean of 35.7 requires other seeds ~41%\")\nprint()\n\n# Also verify: 30% KL uniform s42 numbers match bench_kl30_uniform\nprint(\"KL 30% uniform s42: bench_kl30_uniform\")\nd = reg[\"bench_kl30_uniform\"][\"metrics\"]\nprint(f\"  PPL={d['wikitext2_ppl']}\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f}%\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f}%\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f}%\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f}%\")\n\n# Check the C1 ablation table numbers too\nprint()\nprint(\"=\" * 80)\nprint(\"C1 ABLATION TABLE (Table 2) SPOT CHECKS\")\nprint(\"=\" * 80)\n\n# c1_ablation_30pct_s42_eval_v2\nd = reg[\"c1_ablation_30pct_s42_eval_v2\"][\"metrics\"]\nprint(f\"C1 s42 30%: PPL={round(d['wikitext2_ppl'],2)} (paper=9.45), ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=40.27)\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f} (paper=67.40), MMLU={d['mmlu_acc']*100:.2f} (paper=42.30)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=7.58)\")\n# Check\nprint(f\"  PPL: 9.4463 rounds to 9.45 -> MATCH\")\nprint(f\"  ARC-c: 40.27 -> MATCH\")\nprint(f\"  WG: 67.40 -> MATCH\")\nprint(f\"  MMLU: 42.29 vs paper 42.30 -> minor rounding\")\nprint(f\"  GSM8K: 7.58 -> MATCH\")\n\n# KL s42 in C1 table: bench_kl30_uniform\nd = reg[\"bench_kl30_uniform\"][\"metrics\"]\nprint(f\"\\nKL s42 30% (C1 table): PPL={round(d['wikitext2_ppl'],2)} (paper=8.82)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=40.78)\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f} (paper=68.59)\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f} (paper=40.6)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=7.35)\")\n# PPL: 8.8157 -> 8.82 MATCH\n# ARC-c: 40.78 MATCH\n# WG: 68.59 MATCH\n# MMLU: 40.61 -> 40.6 MATCH\n# GSM8K: 7.35 MATCH\n\n# eval_c1_retrain_30pct_s123\nd = reg[\"eval_c1_retrain_30pct_s123\"][\"metrics\"]\nprint(f\"\\nC1 s123 30%: PPL={round(d['wikitext2_ppl'],2)} (paper=8.84)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=44.71)\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f} (paper=69.77)\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f} (paper=39.92)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=6.82)\")\n# All MATCH\n\n# kl30_s123_eval\nd = reg[\"kl30_s123_eval\"][\"metrics\"]\nprint(f\"\\nKL s123 30% (C1 table): PPL={round(d['wikitext2_ppl'],2)} (paper=8.83)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=45.31)\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f} (paper=39.4)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=7.51)\")\n# PPL: 8.8308 -> 8.83 MATCH; MMLU: 39.44 -> 39.4 MATCH\n\n# kl30_s456_uniform_eval  \nd = reg[\"kl30_s456_uniform_eval\"][\"metrics\"]\nprint(f\"\\nKL s456 30% (C1 table): PPL={round(d['ppl_uniform'],2)} (paper=8.79)\")\nprint(f\"  ARC-c={d['arc_challenge']*100:.2f} (paper=45.05)\")\nprint(f\"  MMLU={d['mmlu']*100:.2f} (paper=42.0)\")\nprint(f\"  GSM8K={d['gsm8k']*100:.2f} (paper=7.58)\")\n# PPL: 8.7947 -> 8.79 MATCH; MMLU: 41.98 -> 42.0 MATCH\n\n# eval_c1_retrain_30pct_s456\nd = reg[\"eval_c1_retrain_30pct_s456\"][\"metrics\"]\nprint(f\"\\nC1 s456 30%: PPL={round(d['wikitext2_ppl'],2)} (paper=8.82)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=44.71)\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f} (paper=69.93)\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f} (paper=41.04)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=6.60)\")\n# All MATCH\n\n# 50% C1 entries\nd = reg[\"c1_ablation_eval_uniform\"][\"metrics\"]\nprint(f\"\\nC1 s42 50% (c1_ablation_eval_uniform): PPL={round(d['wikitext2_ppl'],4)} (paper=11.96)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=32.17)\")\nprint(f\"  WG={d['winogrande_acc']*100:.2f} (paper=63.14)\")\nprint(f\"  MMLU={d['mmlu_acc']*100:.2f} (paper=27.79)\")\nprint(f\"  GSM8K={d['gsm8k_exact_match']*100:.2f} (paper=2.05)\")\n# PPL 11.9638 -> 11.96 MATCH; ARC 32.17 MATCH; WG 63.14 MATCH; MMLU 27.79 MATCH; GSM8K 2.05 MATCH\n\n# KL s42 50%: bench_kl50_uniform\nd = reg[\"bench_kl50_uniform\"][\"metrics\"]\nprint(f\"\\nKL s42 50% (C1 table): PPL={round(d['wikitext2_ppl'],2)} (paper=11.96)\")\nprint(f\"  ARC-c={d['arc_challenge_acc_norm']*100:.2f} (paper=32.59)\")\n# 11.963 -> 11.96; Wait paper says 11.96 for both C1 and KL at 50%. \n# bench_kl50_uniform PPL=11.963, c1_ablation_eval_uniform PPL=11.9638\n# Both round to 11.96. That's correct.\n# But paper's Table 3 shows bench_kl50_uniform as 11.92±0.07 (3-seed mean)\n# while C1 table shows single s42 = 11.96. Both are consistent.\n\nPYEOF\n",
  "description": "Verify C1 ablation table and investigate remaining discrepancies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b1cae77-0a79-43bb-969f-84c22b327dfa",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3aB6vtw5kqGo79UXPU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c635802f-c514-44fe-aa9b-3730a4e80dbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Apeo4DiBgXTGFkACia5EBs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 66780,
      "output_tokens": 2501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2501,
          "cache_read_input_tokens": 66780,
          "cache_creation_input_tokens": 1345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1345,
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

_source line 22 · 2026-05-23T19:23:20.487Z_

<details><summary>↩ Tool result · `toolu_01VRwDYEm4B1qztujZtWxUrt`</summary>

```text
KL 30% global s42: bench_kl30_global
  PPL=8.9768
  MMLU=25.27%
  Note: MMLU 25.27% - paper says mean 35.7±9.5%
  With only 1 seed (25.27%), getting a 3-seed mean of 35.7 requires other seeds ~41%

KL 30% uniform s42: bench_kl30_uniform
  PPL=8.8157
  ARC-c=40.78%
  WG=68.59%
  MMLU=40.61%
  GSM8K=7.35%

================================================================================
C1 ABLATION TABLE (Table 2) SPOT CHECKS
================================================================================
C1 s42 30%: PPL=9.45 (paper=9.45), ARC-c=40.27 (paper=40.27)
  WG=67.40 (paper=67.40), MMLU=42.29 (paper=42.30)
  GSM8K=7.58 (paper=7.58)
  PPL: 9.4463 rounds to 9.45 -> MATCH
  ARC-c: 40.27 -> MATCH
  WG: 67.40 -> MATCH
  MMLU: 42.29 vs paper 42.30 -> minor rounding
  GSM8K: 7.58 -> MATCH

KL s42 30% (C1 table): PPL=8.82 (paper=8.82)
  ARC-c=40.78 (paper=40.78)
  WG=68.59 (paper=68.59)
  MMLU=40.61 (paper=40.6)
  GSM8K=7.35 (paper=7.35)

C1 s123 30%: PPL=8.84 (paper=8.84)
  ARC-c=44.71 (paper=44.71)
  WG=69.77 (paper=69.77)
  MMLU=39.92 (paper=39.92)
  GSM8K=6.82 (paper=6.82)

KL s123 30% (C1 table): PPL=8.83 (paper=8.83)
  ARC-c=45.31 (paper=45.31)
  MMLU=39.44 (paper=39.4)
  GSM8K=7.51 (paper=7.51)

KL s456 30% (C1 table): PPL=8.79 (paper=8.79)
  ARC-c=45.05 (paper=45.05)
  MMLU=41.98 (paper=42.0)
  GSM8K=7.58 (paper=7.58)

C1 s456 30%: PPL=8.82 (paper=8.82)
  ARC-c=44.71 (paper=44.71)
  WG=69.93 (paper=69.93)
  MMLU=41.04 (paper=41.04)
  GSM8K=6.60 (paper=6.60)

C1 s42 50% (c1_ablation_eval_uniform): PPL=11.9638 (paper=11.96)
  ARC-c=32.17 (paper=32.17)
  WG=63.14 (paper=63.14)
  MMLU=27.79 (paper=27.79)
  GSM8K=2.05 (paper=2.05)

KL s42 50% (C1 table): PPL=11.96 (paper=11.96)
  ARC-c=32.76 (paper=32.59)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c635802f-c514-44fe-aa9b-3730a4e80dbe",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "ae893316-0a73-4dc0-b799-46a50c7ac60b",
  "sourceToolAssistantUUID": "c635802f-c514-44fe-aa9b-3730a4e80dbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:23:41.997Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FKyav89kua1nPd7zaU3X9C`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\n# The C1 table 50% KL s42 shows ARC-c=32.59, but bench_kl50_uniform has 32.76\n# Paper references exp_id c1_kl_teal50u. Let me search for it.\nprint(\"Searching for c1_kl_teal50u in registry...\")\nfor k in sorted(reg.keys()):\n    if 'c1' in k.lower() and '50' in k:\n        print(f\"  {k}: {reg[k]['metrics']}\")\n\nprint()\nprint(\"c1_kl_teal50u is NOT in the registry.\")\nprint(\"c1_ablation_eval_uniform exists (PPL=11.9638, ARC-c=32.17) - this is the C1 entry.\")\nprint(\"The KL counterpart 'c1_kl_teal50u' with ARC-c=32.59 is missing from registry.\")\nprint(\"bench_kl50_uniform has ARC-c=32.76, which doesn't match 32.59 either.\")\nprint(\"CANNOT VERIFY KL s42 50% in C1 table (ARC-c=32.59 from c1_kl_teal50u)\")\nprint()\n\n# Now let me also check the TEAL 30% ARC-c discrepancy\n# bench_teal30_uniform_6task has ARC-c=0.3933=39.33% which matches paper\n# bench_teal30 has ARC-c=0.4232=42.32% (global allocation, different)\n# So for TEAL 30% uniform: PPL, ARC-c, WG, MMLU all come from bench_teal30_uniform_6task\n# but GSM8K is missing from that entry. Paper shows 8.79% for GSM8K.\n\n# Let me check if there's a separate TEAL GSM8K eval\nprint(\"Searching for any teal30 GSM8K uniform eval...\")\nfor k in sorted(reg.keys()):\n    if 'teal' in k and '30' in k and 'qwen' not in k and 'mistral' not in k:\n        m = reg[k][\"metrics\"]\n        gsm = None\n        for mk, mv in m.items():\n            if 'gsm' in mk.lower():\n                gsm = mv\n        if gsm is not None:\n            print(f\"  {k}: gsm8k={gsm}\")\n        else:\n            print(f\"  {k}: no gsm8k\")\n\nprint()\nprint(\"Summary of TEAL GSM8K issue:\")\nprint(\"  bench_teal30_uniform_6task: ran ARC-c, WG, MMLU, HellaSwag, PIQA (no GSM8K)\")\nprint(\"  bench_teal30: has GSM8K=7.88% but uses global allocation, not uniform\")\nprint(\"  Paper's 8.79% for '30% TEAL uniform' GSM8K has NO matching registry entry\")\nprint(\"  The 8.79% coincidentally matches bench_kl30_global's GSM8K (0.0879=8.79%)\")\n\n# Verify this coincidence\nprint(f\"\\n  bench_kl30_global GSM8K = {reg['bench_kl30_global']['metrics']['gsm8k_exact_match']*100:.2f}%\")\nprint(f\"  Paper's TEAL 30% uniform GSM8K = 8.79%\")\nprint(f\"  THESE ARE IDENTICAL - possible copy error from KL global to TEAL uniform?\")\n\nPYEOF\n",
  "description": "Investigate TEAL GSM8K and C1 table discrepancies further"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae893316-0a73-4dc0-b799-46a50c7ac60b",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3dUT3VMTSpsLRUqvXG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8266e8ec-a3e4-4511-b5b1-c690a6f561c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XtRJ84viQw99tsL9LxCb2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3464,
      "cache_read_input_tokens": 68125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3464,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 24 · 2026-05-23T19:23:42.067Z_

<details><summary>↩ Tool result · `toolu_01FKyav89kua1nPd7zaU3X9C`</summary>

```text
Searching for c1_kl_teal50u in registry...

c1_kl_teal50u is NOT in the registry.
c1_ablation_eval_uniform exists (PPL=11.9638, ARC-c=32.17) - this is the C1 entry.
The KL counterpart 'c1_kl_teal50u' with ARC-c=32.59 is missing from registry.
bench_kl50_uniform has ARC-c=32.76, which doesn't match 32.59 either.
CANNOT VERIFY KL s42 50% in C1 table (ARC-c=32.59 from c1_kl_teal50u)

Searching for any teal30 GSM8K uniform eval...
  bench_teal30: gsm8k=0.0788
  bench_teal30_uniform_6task: no gsm8k

Summary of TEAL GSM8K issue:
  bench_teal30_uniform_6task: ran ARC-c, WG, MMLU, HellaSwag, PIQA (no GSM8K)
  bench_teal30: has GSM8K=7.88% but uses global allocation, not uniform
  Paper's 8.79% for '30% TEAL uniform' GSM8K has NO matching registry entry
  The 8.79% coincidentally matches bench_kl30_global's GSM8K (0.0879=8.79%)

  bench_kl30_global GSM8K = 8.79%
  Paper's TEAL 30% uniform GSM8K = 8.79%
  THESE ARE IDENTICAL - possible copy error from KL global to TEAL uniform?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8266e8ec-a3e4-4511-b5b1-c690a6f561c8",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "0ace3ddc-e8fa-4d60-97b8-6e4a40c66684",
  "sourceToolAssistantUUID": "8266e8ec-a3e4-4511-b5b1-c690a6f561c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:24:12.397Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GBpPzrMUSYeMdENkkusHQr`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/registry_all_metrics.json') as f:\n    reg = json.load(f)\n\n# Similarly check TEAL 50% GSM8K\n# bench_teal50_uniform_6task has no GSM8K\n# bench_teal50 has GSM8K=1.97% (global)\n# Paper says 1.74% for TEAL 50% uniform\n\n# 1.74% doesn't match any obvious entry. Let me search.\nprint(\"Searching for anything with gsm8k ~0.0174...\")\nfor k in sorted(reg.keys()):\n    m = reg[k][\"metrics\"]\n    for mk, mv in m.items():\n        if 'gsm' in mk.lower() and isinstance(mv, float) and abs(mv - 0.0174) < 0.001:\n            print(f\"  {k}.{mk} = {mv}\")\n\nprint()\n# Check mse30_s123_downstream gsm8k = 0.0174\nprint(f\"  mse30_s123_downstream.gsm8k_exact_match = {reg['mse30_s123_downstream']['metrics']['gsm8k_exact_match']}\")\nprint(f\"  This is MSE 30% s123, not TEAL 50%\")\nprint()\nprint(\"  Paper's TEAL 50% uniform GSM8K=1.74% has NO matching registry entry\")\nprint(\"  Closest is bench_teal50 GSM8K=1.97% (global allocation)\")\n\nprint()\nprint(\"=\" * 80)\nprint(\"FINAL SUMMARY OF ALL ISSUES FOUND\")\nprint(\"=\" * 80)\n\nprint(\"\"\"\nTABLE 3 VERIFICATION RESULTS:\n\nVERIFIED MATCHES (all numbers correct):\n  - Dense (0%): All 5 metrics MATCH\n  - 30% TEAL uniform: PPL, ARC-c, WG, MMLU all MATCH\n  - 30% BCE global: All 5 metrics match (acceptable rounding from raw values)\n  - 30% MSE uniform (3-seed): All means match; stds match within rounding\n  - 30% KL uniform (3-seed): All means match; stds match within rounding\n  - 50% TEAL uniform: PPL, ARC-c, WG, MMLU all MATCH\n  - 50% BCE 2700-step (3-seed): All means and stds match\n  - 50% MSE uniform: All 5 metrics MATCH exactly\n  - 50% KL uniform (3-seed): All means match; stds match within rounding\n  - 50% KL global (3-seed): Downstream metrics match; PPL partially verifiable\n\nISSUES FOUND:\n\n1. [CRITICAL] 30% TEAL uniform GSM8K: paper=8.79%, NO registry source for uniform eval.\n   bench_teal30_uniform_6task has no GSM8K; bench_teal30 (global) gives 7.88%.\n   SUSPICIOUS: 8.79% exactly matches bench_kl30_global's GSM8K - possible copy error.\n\n2. [CRITICAL] 50% TEAL uniform GSM8K: paper=1.74%, NO registry source for uniform eval.\n   bench_teal50_uniform_6task has no GSM8K; bench_teal50 (global) gives 1.97%.\n   No entry matches 1.74%.\n\n3. [UNVERIFIABLE] 30% BCE uniform 3-seed: paper=15.09±0.13.\n   Only single seed in registry: bce_30_s42_uniform_eval PPL=15.71.\n   exp_ids in paper comment (bce_iso_v3_*) are actually 50% BCE experiments.\n   Paper's 3-seed claim for 30% BCE uniform cannot be verified.\n\n4. [UNVERIFIABLE] 30% KL global 3-seed: only bench_kl30_global (s42) in registry.\n   kl30_s123_global_v3 and kl30_s456_global_v3 not found.\n   s42 MMLU=25.27% vs paper mean=35.7±9.5% (consistent with high variance).\n\n5. [MINOR] Several std deviations show marginal rounding:\n   - MSE 30% PPL std: computed 1.67, paper 1.68\n   - KL 50% uniform PPL std: computed 0.08, paper 0.07\n   - KL 50% global GSM8K std: computed 1.25, paper 1.3\n   - KL 50% uniform GSM8K std: computed 0.13, paper 0.1\n\n6. [UNVERIFIABLE] 10.30 TEAL PPL at 28.5% actual sparsity (used for 14.5% claim)\n   not present in registry. Arithmetic is correct: (10.30-8.81)/10.30 = 14.5%.\n\nDERIVED CLAIMS:\n  - \"14.5% reduction\": (10.30-8.81)/10.30 = 14.47% ≈ 14.5% MATCH (but 10.30 unverified)\n  - \"50% reduction at 50%\": (23.90-11.92)/23.90 = 50.1% ≈ 50% MATCH\n\"\"\")\n\nPYEOF\n",
  "description": "Complete final summary of all verification results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ace3ddc-e8fa-4d60-97b8-6e4a40c66684",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3f5F6X5kuwBNTu9tcx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b4ec185-c3f2-4028-b06f-8e896b0338a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJisHVAFTYjyvs89uWCg4A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 71589,
      "output_tokens": 1413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1413,
          "cache_read_input_tokens": 71589,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1452,
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

_source line 26 · 2026-05-23T19:24:12.478Z_

<details><summary>↩ Tool result · `toolu_01GBpPzrMUSYeMdENkkusHQr`</summary>

```text
Searching for anything with gsm8k ~0.0174...
  bce_ste_s42.gsm8k_exact_match = 0.0182
  mse30_s123_downstream.gsm8k_exact_match = 0.0174

  mse30_s123_downstream.gsm8k_exact_match = 0.0174
  This is MSE 30% s123, not TEAL 50%

  Paper's TEAL 50% uniform GSM8K=1.74% has NO matching registry entry
  Closest is bench_teal50 GSM8K=1.97% (global allocation)

================================================================================
FINAL SUMMARY OF ALL ISSUES FOUND
================================================================================

TABLE 3 VERIFICATION RESULTS:

VERIFIED MATCHES (all numbers correct):
  - Dense (0%): All 5 metrics MATCH
  - 30% TEAL uniform: PPL, ARC-c, WG, MMLU all MATCH
  - 30% BCE global: All 5 metrics match (acceptable rounding from raw values)
  - 30% MSE uniform (3-seed): All means match; stds match within rounding
  - 30% KL uniform (3-seed): All means match; stds match within rounding
  - 50% TEAL uniform: PPL, ARC-c, WG, MMLU all MATCH
  - 50% BCE 2700-step (3-seed): All means and stds match
  - 50% MSE uniform: All 5 metrics MATCH exactly
  - 50% KL uniform (3-seed): All means match; stds match within rounding
  - 50% KL global (3-seed): Downstream metrics match; PPL partially verifiable

ISSUES FOUND:

1. [CRITICAL] 30% TEAL uniform GSM8K: paper=8.79%, NO registry source for uniform eval.
   bench_teal30_uniform_6task has no GSM8K; bench_teal30 (global) gives 7.88%.
   SUSPICIOUS: 8.79% exactly matches bench_kl30_global's GSM8K - possible copy error.

2. [CRITICAL] 50% TEAL uniform GSM8K: paper=1.74%, NO registry source for uniform eval.
   bench_teal50_uniform_6task has no GSM8K; bench_teal50 (global) gives 1.97%.
   No entry matches 1.74%.

3. [UNVERIFIABLE] 30% BCE uniform 3-seed: paper=15.09±0.13.
   Only single seed in registry: bce_30_s42_uniform_eval PPL=15.71.
   exp_ids in paper comment (bce_iso_v3_*) are actually 50% BCE experiments.
   Paper's 3-seed claim for 30% BCE uniform cannot be verified.

4. [UNVERIFIABLE] 30% KL global 3-seed: only bench_kl30_global (s42) in registry.
   kl30_s123_global_v3 and kl30_s456_global_v3 not found.
   s42 MMLU=25.27% vs paper mean=35.7±9.5% (consistent with high variance).

5. [MINOR] Several std deviations show marginal rounding:
   - MSE 30% PPL std: computed 1.67, paper 1.68
   - KL 50% uniform PPL std: computed 0.08, paper 0.07
   - KL 50% global GSM8K std: computed 1.25, paper 1.3
   - KL 50% uniform GSM8K std: computed 0.13, paper 0.1

6. [UNVERIFIABLE] 10.30 TEAL PPL at 28.5% actual sparsity (used for 14.5% claim)
   not present in registry. Arithmetic is correct: (10.30-8.81)/10.30 = 14.5%.

DERIVED CLAIMS:
  - "14.5% reduction": (10.30-8.81)/10.30 = 14.47% ≈ 14.5% MATCH (but 10.30 unverified)
  - "50% reduction at 50%": (23.90-11.92)/23.90 = 50.1% ≈ 50% MATCH
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b4ec185-c3f2-4028-b06f-8e896b0338a1",
  "isSidechain": true,
  "promptId": "aa8ee645-c8d5-4f1c-b300-e8875450887d",
  "agentId": "a0deae6eff35145f3",
  "type": "user",
  "uuid": "e8fce1de-92e3-40ca-869d-5ea947a30262",
  "sourceToolAssistantUUID": "9b4ec185-c3f2-4028-b06f-8e896b0338a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T19:24:33.313Z_

Here is the complete audit report.

---

## Table 3 Audit Results

### Fully Verified (all numbers match registry)

- **Dense (0%)**: All 5 metrics match exactly (`bench_dense`).
- **30% TEAL uniform**: PPL 10.82, ARC-c 39.33, WG 65.04, MMLU 45.86 all match (`bench_teal30_uniform_6task`).
- **30% BCE global**: All 5 metrics match with acceptable rounding from raw values (`bce_30pct_s42_eval`: 11.2445->11.25, 41.21->41.2, 65.98->66.0, 36.33->36.3, 5.99->6.0).
- **30% MSE uniform (3-seed)**: All means match; stds match within rounding tolerance (`mse30_s42_eval_7task`, `mse30_s123`/`mse30_s123_downstream`, `mse30_s456`/`mse30_s456_downstream`).
- **30% KL uniform (3-seed)**: All means match; stds match within rounding (`bench_kl30_uniform`, `kl30_s123_eval`, `kl30_s456_uniform_eval`).
- **50% TEAL uniform**: PPL 23.90, ARC-c 27.47, WG 54.38, MMLU 29.26 all match (`bench_teal50_uniform_6task`).
- **50% BCE 2700-step (3-seed)**: All means and stds match (`bce_isocompute_v3_s42_eval`, `_s123_eval`, `_s456_eval`).
- **50% MSE uniform**: All 5 metrics match exactly (`mse50_s42_eval_7task`).
- **50% KL uniform (3-seed)**: All means match; stds match within rounding (`bench_kl50_uniform`, `_s123`, `_s456`).
- **50% KL global (3-seed)**: Downstream metrics (ARC-c, WG, MMLU, GSM8K) all match; PPL partially verifiable (s123 PPL missing from registry).

### Critical Issues

1. **30% TEAL uniform GSM8K = 8.79%**: No registry source exists. `bench_teal30_uniform_6task` did not evaluate GSM8K. `bench_teal30` (global allocation, not uniform) gives 7.88%. The value 8.79% exactly matches `bench_kl30_global`'s GSM8K (0.0879) -- this strongly suggests a copy-paste error from the KL global row.

2. **50% TEAL uniform GSM8K = 1.74%**: No registry source exists. `bench_teal50_uniform_6task` did not evaluate GSM8K. `bench_teal50` (global allocation) gives 1.97%. No entry in the entire registry matches 1.74%.

### Unverifiable Claims

3. **30% BCE uniform 3-seed (PPL 15.09 +/- 0.13)**: Only a single seed exists (`bce_30_s42_uniform_eval`, PPL=15.71). The paper's exp_id comment references `bce_iso_v3_*` which are actually the 50% BCE experiments. The 3-seed numbers for 30% BCE uniform cannot be verified and the single available seed (15.71) is substantially different from the claimed mean (15.09).

4. **30% KL global 3-seed**: Only `bench_kl30_global` (s42) is in the registry. The other two seeds (`kl30_s123_global_v3`, `kl30_s456_global_v3`) are missing.

5. **10.30 TEAL PPL at 28.5% actual sparsity** (used in "14.5% reduction" claim): Not present in registry. The arithmetic (10.30-8.81)/10.30 = 14.5% is correct, but the input value 10.30 is unverified.

### Minor Rounding Discrepancies

All within +/- 0.01 of the last reported decimal, not concerning:
- MSE 30% PPL std: computed 1.67, paper 1.68
- KL 50% uniform PPL std: computed 0.08, paper 0.07
- KL 50% global GSM8K std: computed 1.25, paper 1.3
- KL 50% uniform GSM8K std: computed 0.13, paper 0.1

### Derived Claims

- **"14.5% reduction"**: Arithmetic correct -- (10.30-8.81)/10.30 = 14.47% rounds to 14.5%. But the 10.30 baseline is not in the registry.
- **"50% reduction at 50%"**: (23.90-11.92)/23.90 = 50.1% -- **MATCH**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8fce1de-92e3-40ca-869d-5ea947a30262",
  "isSidechain": true,
  "agentId": "a0deae6eff35145f3",
  "requestId": "req_011CbL3hKJjeLHMYAv3p7yhK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89d7bfc5-2841-4122-91a3-c91391ed975a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "471eadfd-715d-4d55-863d-6199e56819c8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJJmrtHneHwR6kxTezAjad",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2509,
      "cache_read_input_tokens": 73041,
      "output_tokens": 1246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1246,
          "cache_read_input_tokens": 73041,
          "cache_creation_input_tokens": 2509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2509,
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
