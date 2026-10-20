# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml, find ALL exp

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae0545680b43593da.jsonl`
- **Structured JSON:** [`b0b17006b724915aca1c.json`](../../sessions/b0/b0b17006b724915aca1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-16T06:11:27.377Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml, find ALL experiments with synthetic_ratio 0.50 or "a050" in the exp_id. For each, report the exp_id, status, conclusion, and seed. I need to know how many valid (status=DONE, conclusion=success) seeds exist at α=0.50.

Also check: are there any experiments with alpha/synthetic_ratio 0.0 besides seed=42? Search for "a000" or synthetic_ratio 0.0 in the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bfd10638-11d5-4fd5-a51c-fdbcd38a9e94",
  "agentId": "ae0545680b43593da",
  "type": "user",
  "uuid": "f97c2b81-da99-4c1e-be15-799f8898f0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-16T06:11:28.629Z_

I'll help you find these experiments in the registry file. Let me start by reading the registry and searching for the specific conditions you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f97c2b81-da99-4c1e-be15-799f8898f0dc",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kafs2YXq9Zzm9jeLx6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8502f1c4-183f-49c9-89be-5f730337a637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Df1G5foiGekeVVk76GsXBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20747,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20747,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 3 · 2026-05-16T06:11:28.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MvUpMiHhfU6QFBC31bVSiF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8502f1c4-183f-49c9-89be-5f730337a637",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kafs2YXq9Zzm9jeLx6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a5a540b8-44e8-4698-b7d9-d147e4670bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Df1G5foiGekeVVk76GsXBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20747,
      "cache_read_input_tokens": 0,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20747
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20747,
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

_source line 4 · 2026-05-16T06:11:29.096Z_

<details><summary>↩ Tool result · `toolu_01MvUpMiHhfU6QFBC31bVSiF`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_rep42:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T05:12:13.930Z'
7	    updated_at: '2026-05-14T05:37:17.438Z'
8	    spec:
9	      command: python iterative_train.py --seed 42 --output_dir results/mvp/rep_42
10	        --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen
11	        10000
12	      server: autodl-rtx6000
13	      gpu: cuda:0
14	      pid: '3878'
15	      log_path: ~/runs/distrib_canary_collapse/mvp_rep42.log
16	      submitted_at: '2026-05-14T05:34:46.013Z'
17	      submitted_via: submit_training_job
18	      backend: tmux
19	      account: root
20	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103
21	      data_count: 716506
22	      model_name: EleutherAI/pythia-410m
23	      seed: 42
24	      gpu_model: RTX PRO 6000 Blackwell 96GB
25	      tmux_session: mvp_rep42
26	      checkpoint_path: N/A
27	      kill_reason: '参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000'
28	      wall_clock_seconds: 151.4
29	      gpu_hours: 0.04
30	    conclusion: killed
31	    completed_at: '2026-05-14T05:37:17.438Z'
32	  mvp_rep43:
33	    status: DONE
34	    retry_count: 0
35	    created_at: '2026-05-14T05:12:14.237Z'
36	    updated_at: '2026-05-14T05:37:18.575Z'
37	    spec:
38	      command: python iterative_train.py --seed 43 --output_dir results/mvp/rep_43
39	        --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen
40	        10000
41	      server: autodl-rtx6000
42	      gpu: cuda:1
43	      pid: '3956'
44	      log_path: ~/runs/distrib_canary_collapse/mvp_rep43.log
45	      submitted_at: '2026-05-14T05:34:47.702Z'
46	      submitted_via: submit_training_job
47	      backend: tmux
48	      account: root
49	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103
50	      data_count: 716506
51	      model_name: EleutherAI/pythia-410m
52	      seed: 43
53	      gpu_model: RTX PRO 6000 Blackwell 96GB
54	      tmux_session: mvp_rep43
55	      checkpoint_path: N/A
56	      kill_reason: '参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000'
57	      wall_clock_seconds: 150.9
58	      gpu_hours: 0.04
59	    conclusion: killed
60	    completed_at: '2026-05-14T05:37:18.575Z'
61	  mvp_rep44:
62	    status: DONE
63	    retry_count: 0
64	    created_at: '2026-05-14T05:12:15.033Z'
65	    updated_at: '2026-05-16T00:10:25.605Z'
66	    spec:
67	      hypothesis: 至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性
68	      model_name: EleutherAI/pythia-410m
69	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103
70	      seed: 44
71	      server: autodl-rtx6000
72	      gpu: pending
73	      synthetic_ratio: 1
74	      num_generations: 10
75	      steps_per_gen: 10000
76	    metrics:
77	      gen10_token_entropy: 1.2205
78	      gen10_ece: 0.4237
79	      gen10_perplexity: 1033.16
80	      gen10_distinct_1: 0.0731
81	      gen10_distinct_2: 0.3637
82	      gen10_distinct_3: 0.6075
83	    conclusion: killed
84	    completed_at: '2026-05-16T00:10:25.605Z'
85	  mvp_v2_rep42:
86	    status: DONE
87	    retry_count: 0
88	    created_at: '2026-05-14T05:38:05.054Z'
89	    updated_at: '2026-05-14T06:25:27.286Z'
90	    spec:
91	      command: python iterative_train.py --seed 42 --output_dir results/mvp/rep_42
92	        --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10
93	        --steps_per_gen 5000
94	      server: autodl-rtx6000
95	      gpu: cuda:0
96	      pid: '5286'
97	      log_path: ~/runs/distrib_canary_collapse/mvp_v2_rep42.log
98	      submitted_at: '2026-05-14T05:42:37.404Z'
99	      submitted_via: submit_training_job
100	      backend: tmux
101	      account: root
102	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
103	      data_count: 5000
104	      model_name: EleutherAI/pythia-410m
105	      seed: 42
106	      gpu_model: RTX PRO 6000 Blackwell 96GB
107	      tmux_session: mvp_v2_rep42
108	      checkpoint_path: N/A
109	      kill_reason: v1旧进程未死导致输出目录冲突，v2死锁
110	      wall_clock_seconds: 2569.9
111	      gpu_hours: 0.71
112	    conclusion: killed
113	    completed_at: '2026-05-14T06:25:27.286Z'
114	  mvp_v2_rep43:
115	    status: DONE
116	    retry_count: 0
117	    created_at: '2026-05-14T05:38:10.434Z'
118	    updated_at: '2026-05-14T06:25:28.345Z'
119	    spec:
120	      command: python iterative_train.py --seed 43 --output_dir results/mvp/rep_43
121	        --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10
122	        --steps_per_gen 5000
123	      server: autodl-rtx6000
124	      gpu: cuda:1
125	      pid: '5364'
126	      log_path: ~/runs/distrib_canary_collapse/mvp_v2_rep43.log
127	      submitted_at: '2026-05-14T05:42:39.039Z'
128	      submitted_via: submit_training_job
129	      backend: tmux
130	      account: root
131	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
132	      data_count: 5000
133	      model_name: EleutherAI/pythia-410m
134	      seed: 43
135	      gpu_model: RTX PRO 6000 Blackwell 96GB
136	      tmux_session: mvp_v2_rep43
137	      checkpoint_path: N/A
138	      kill_reason: v1旧进程未死导致输出目录冲突，v2死锁
139	      wall_clock_seconds: 2569.3
140	      gpu_hours: 0.71
141	    conclusion: killed
142	    completed_at: '2026-05-14T06:25:28.345Z'
143	  mvp_v2_rep44:
144	    status: DONE
145	    retry_count: 0
146	    created_at: '2026-05-14T05:38:10.762Z'
147	    updated_at: '2026-05-16T00:10:26.251Z'
148	    spec:
149	      hypothesis: 至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性
150	      model_name: EleutherAI/pythia-410m
151	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103
152	      data_count: 5000
153	      seed: 44
154	      server: autodl-rtx6000
155	      gpu: pending
156	      synthetic_ratio: 1
157	      num_generations: 10
158	      steps_per_gen: 5000
159	      n_prompts: 5000
160	      fix_note: n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合
161	    conclusion: killed
162	    completed_at: '2026-05-16T00:10:26.251Z'
163	  mvp_v3_rep42:
164	    status: DONE
165	    retry_count: 0
166	    created_at: '2026-05-14T06:25:39.728Z'
167	    updated_at: '2026-05-14T06:47:59.908Z'
168	    spec:
169	      command: python iterative_train.py --seed 42 --output_dir results/mvp/rep_42
170	        --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10
171	        --steps_per_gen 5000
172	      server: autodl-rtx6000
173	      gpu: cuda:0
174	      pid: '7909'
175	      log_path: ~/runs/distrib_canary_collapse/mvp_v3_rep42.log
176	      submitted_at: '2026-05-14T06:26:16.939Z'
177	      submitted_via: submit_training_job
178	      backend: tmux
179	      account: root
180	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
181	      data_count: 5000
182	      model_name: EleutherAI/pythia-410m
183	      seed: 42
184	      gpu_model: RTX PRO 6000 Blackwell 96GB
185	      tmux_session: mvp_v3_rep42
186	      checkpoint_path: N/A
187	      failure_reason: 'MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required;
188	        无 PYTHONUNBUFFERED 导致日志丢失'
189	      wall_clock_seconds: 1303.0
190	      gpu_hours: 0.36
191	    conclusion: failed
192	    completed_at: '2026-05-14T06:47:59.908Z'
193	  mvp_v3_rep43:
194	    status: DONE
195	    retry_count: 0
196	    created_at: '2026-05-14T06:25:42.195Z'
197	    updated_at: '2026-05-14T06:48:01.316Z'
198	    spec:
199	      command: python iterative_train.py --seed 43 --output_dir results/mvp/rep_43
200	        --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10
201	        --steps_per_gen 5000
202	      server: autodl-rtx6000
203	      gpu: cuda:1
204	      pid: '7987'
205	      log_path: ~/runs/distrib_canary_collapse/mvp_v3_rep43.log
206	      submitted_at: '2026-05-14T06:26:18.477Z'
207	      submitted_via: submit_training_job
208	      backend: tmux
209	      account: root
210	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
211	      data_count: 5000
212	      model_name: EleutherAI/pythia-410m
213	      seed: 43
214	      gpu_model: RTX PRO 6000 Blackwell 96GB
215	      tmux_session: mvp_v3_rep43
216	      checkpoint_path: N/A
217	      failure_reason: 'MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required;
218	        无 PYTHONUNBUFFERED 导致日志丢失'
219	      wall_clock_seconds: 1302.8
220	      gpu_hours: 0.36
221	    conclusion: failed
222	    completed_at: '2026-05-14T06:48:01.316Z'
223	  mvp_v4_rep42:
224	    status: DONE
225	    retry_count: 0
226	    created_at: '2026-05-14T07:29:48.857Z'
227	    updated_at: '2026-05-15T21:29:47.171Z'
228	    spec:
229	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
230	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
231	        && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export
232	        SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh
233	        && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py
234	        --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
235	        10 --output_dir results/mvp/rep_42"
236	      server: westd-19828
237	      gpu:
238	      - cuda:0
239	      pid: '13678'
240	      log_path: ~/runs/distrib_canary_collapse/mvp_v4_rep42.log
241	      submitted_at: '2026-05-14T07:51:34.806Z'
242	      submitted_via: submit_training_job
243	      backend: tmux
244	      account: root
245	      checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_10/checkpoint
246	      metrics_summary:
247	        gen0_ppl: 26.9
248	        gen10_ppl: 1003.7
249	        gen0_entropy: 3.234
250	        gen10_entropy: 1.276
251	        gen0_ece: 0.011
252	        gen10_ece: 0.417
253	      wall_clock_seconds: 20898.3
254	      gpu_hours: 5.81
255	    conclusion: success
256	    completed_at: '2026-05-14T13:39:53.073Z'
257	    metrics:
258	      gen0_token_entropy: 3.234195
259	      gen0_ece: 0.010805
260	      gen0_perplexity: 26.948959
261	      gen0_distinct_1: 0.098216
262	      gen0_distinct_2: 0.517803
263	      gen0_distinct_3: 0.812728
264	      gen10_token_entropy: 1.27592
265	      gen10_ece: 0.41734
266	      gen10_perplexity: 1003.73
267	      gen10_distinct_1: 0.070383
268	      gen10_distinct_2: 0.335471
269	      gen10_distinct_3: 0.555579
270	      token_entropy_drift_pct: -60.5491
271	      ece_drift_pct: 3762.4711
272	      perplexity_drift_pct: 3624.5595
273	      distinct_1_drift_pct: -28.3386
274	      distinct_2_drift_pct: -35.2126
275	      distinct_3_drift_pct: -31.6402
276	  mvp_v4_rep43:
277	    status: DONE
278	    retry_count: 0
279	    created_at: '2026-05-14T07:48:50.161Z'
280	    updated_at: '2026-05-15T21:29:49.565Z'
281	    spec:
282	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
283	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
284	        && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export
285	        SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh
286	        && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py
287	        --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
288	        10 --output_dir results/mvp/rep_43"
289	      server: westd-19828
290	      gpu:
291	      - cuda:1
292	      pid: '13758'
293	      log_path: ~/runs/distrib_canary_collapse/mvp_v4_rep43.log
294	      submitted_at: '2026-05-14T07:51:36.759Z'
295	      submitted_via: submit_training_job
296	      backend: tmux
297	      account: root
298	      checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/gen_10/checkpoint
299	      metrics_summary:
300	        gen0_ppl: 26.9
301	        gen10_ppl: 1014.7
302	        gen0_entropy: 3.234
303	        gen10_entropy: 1.26
304	        gen0_ece: 0.011
305	        gen10_ece: 0.42
306	      wall_clock_seconds: 20897.7
307	      gpu_hours: 5.8
308	    conclusion: success
309	    completed_at: '2026-05-14T13:39:54.495Z'
310	    metrics:
311	      gen0_token_entropy: 3.234195
312	      gen0_ece: 0.010805
313	      gen0_perplexity: 26.948959
314	      gen0_distinct_1: 0.098334
315	      gen0_distinct_2: 0.513178
316	      gen0_distinct_3: 0.805669
317	      gen10_token_entropy: 1.25961
318	      gen10_ece: 0.41951
319	      gen10_perplexity: 1014.66
320	      gen10_distinct_1: 0.070383
321	      gen10_distinct_2: 0.329651
322	      gen10_distinct_3: 0.539571
323	      token_entropy_drift_pct: -61.0534
324	      ece_drift_pct: 3782.5544
325	      perplexity_drift_pct: 3665.1176
326	      distinct_1_drift_pct: -28.4246
327	      distinct_2_drift_pct: -35.7628
328	      distinct_3_drift_pct: -33.0282
329	  mvp_v4_rep44:
330	    status: DONE
331	    retry_count: 0
332	    created_at: '2026-05-14T07:48:52.613Z'
333	    updated_at: '2026-05-15T21:29:52.398Z'
334	    spec:
335	      hypothesis: 至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性
336	      model_name: EleutherAI/pythia-410m
337	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
338	      data_count: 5000
339	      seed: 44
340	      server: westd-19828
341	      gpu: cuda:0
342	      synthetic_ratio: 1
343	      num_generations: 10
344	      steps_per_gen: 5000
345	      n_prompts: 5000
346	      command: PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py
347	        --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
348	        10 --output_dir results/mvp/rep_44
349	      pid: '30672'
350	      log_path: ~/runs/distrib_canary_collapse/mvp_v4_rep44.log
351	    reproduce:
352	      finished_at: '2026-05-14T17:56:00.578Z'
353	    failure_reason: ''
354	    conclusion: success
355	    completed_at: '2026-05-14T17:56:00.717Z'
356	    extra:
357	      hook_events:
358	      - event: on_failed
359	        action: agent
360	        ts: '2026-05-14T17:56:03.546926+00:00'
361	    metrics_summary:
362	      gen0_ppl: 26.9
363	      gen10_ppl: 1033.16
364	      gen0_entropy: 3.234
365	      gen10_entropy: 1.2205
366	      gen0_ece: 0.011
367	      gen10_ece: 0.424
368	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/gen_10/checkpoint
369	    wall_clock_seconds: 15134
370	    gpu_hours: 4.2
371	    metrics:
372	      gen0_token_entropy: 3.234195
373	      gen0_ece: 0.010805
374	      gen0_perplexity: 26.948959
375	      gen0_distinct_1: 0.098088
376	      gen0_distinct_2: 0.513235
377	      gen0_distinct_3: 0.805767
378	      gen10_token_entropy: 1.22049
379	      gen10_ece: 0.42369
380	      gen10_perplexity: 1033.16
381	      gen10_distinct_1: 0.073102
382	      gen10_distinct_2: 0.363737
383	      gen10_distinct_3: 0.607502
384	      token_entropy_drift_pct: -62.2629
385	      ece_drift_pct: 3821.2402
386	      perplexity_drift_pct: 3733.7659
387	      distinct_1_drift_pct: -25.473
388	      distinct_2_drift_pct: -29.1286
389	      distinct_3_drift_pct: -24.6057
390	  mvp_v4_rep45:
391	    status: DONE
392	    retry_count: 0
393	    created_at: '2026-05-14T13:41:26.286Z'
394	    updated_at: '2026-05-15T21:29:54.928Z'
395	    spec:
396	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
397	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
398	        && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export
399	        SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh
400	        && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py
401	        --seed 45 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
402	        10 --output_dir results/mvp/rep_45"
403	      server: westd-19828
404	      gpu:
405	      - cuda:1
406	      pid: '31425'
407	      log_path: ~/runs/distrib_canary_collapse/mvp_v4_rep45.log
408	      submitted_at: '2026-05-14T13:42:10.455Z'
409	      submitted_via: submit_training_job
410	      backend: tmux
411	      account: root
412	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
413	      data_count: 5000
414	      model_name: EleutherAI/pythia-410m
415	      seed: 45
416	      wall_clock_seconds: 15350.2
417	      gpu_hours: 4.26
418	    reproduce:
419	      finished_at: '2026-05-14T17:55:42.230Z'
420	    extra:
421	      hook_events:
422	      - event: on_complete
423	        action: agent
424	        ts: '2026-05-14T17:55:42.934182+00:00'
425	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/gen_10/checkpoint
426	    metrics_summary:
427	      gen0_ppl: 26.9
428	      gen10_ppl: 1016.2
429	      gen0_entropy: 3.234
430	      gen10_entropy: 1.315
431	      gen0_ece: 0.011
432	      gen10_ece: 0.417
433	    wall_clock_seconds: 15212
434	    gpu_hours: 4.23
435	    conclusion: success
436	    metrics:
437	      gen0_token_entropy: 3.234195
438	      gen0_ece: 0.010805
439	      gen0_perplexity: 26.948959
440	      gen0_distinct_1: 0.098574
441	      gen0_distinct_2: 0.51463
442	      gen0_distinct_3: 0.808362
443	      gen10_token_entropy: 1.31536
444	      gen10_ece: 0.41654
445	      gen10_perplexity: 1016.22
446	      gen10_distinct_1: 0.069859
447	      gen10_distinct_2: 0.329549
448	      gen10_distinct_3: 0.543743
449	      token_entropy_drift_pct: -59.3296
450	      ece_drift_pct: 3755.0671
451	      perplexity_drift_pct: 3670.9063
452	      distinct_1_drift_pct: -29.1304
453	      distinct_2_drift_pct: -35.9639
454	      distinct_3_drift_pct: -32.7352
455	    completed_at: '2026-05-14T17:58:00.661Z'
456	  alpha_sweep_a000_s42:
457	    status: DONE
458	    retry_count: 0
459	    created_at: '2026-05-14T19:01:37.470Z'
460	    updated_at: '2026-05-14T23:42:18.748Z'
461	    spec:
462	      hypothesis: 'α=0.0 null control: 纯 real data 再训练无 canary signal，确认 signal 源于合成污染'
463	      model_name: EleutherAI/pythia-410m
464	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
465	      data_count: 5000
466	      seed: 42
467	      synthetic_ratio: 0
468	      num_generations: 10
469	      steps_per_gen: 5000
470	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
471	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
472	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
473	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
474	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir
475	        results/alpha_sweep/a000_s42"
476	      server: westd-19828
477	      gpu:
478	      - cuda:0
479	      pid: '46716'
480	      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log
481	    reproduce:
482	      finished_at: '2026-05-14T23:36:35.414Z'
483	    extra:
484	      hook_events:
485	      - event: on_complete
486	        action: agent
487	        ts: '2026-05-14T23:36:36.221435+00:00'
488	    conclusion: success
489	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint
490	    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log
491	    metrics:
492	      gen0_token_entropy: 3.2342
493	      gen10_token_entropy: 3.0693
494	      gen0_ece: 0.0108
495	      gen10_ece: 0.0164
496	      gen0_perplexity: 26.95
497	      gen10_perplexity: 21.11
498	      gen0_distinct_1: 0.0982
499	      gen10_distinct_1: 0.0847
500	      token_entropy_drift_pct: -5.1
501	      ece_drift_pct: 51.7
502	      perplexity_drift_pct: -21.7
503	      distinct_1_drift_pct: -13.8
504	      distinct_2_drift_pct: -9.8
505	      distinct_3_drift_pct: -4.5
506	      gen1_10_perplexity_drift_pct: 9.4
507	      gen1_10_distinct_1_drift_pct: -13.1
508	      gen1_10_entropy_drift_pct: 2.6
509	    completed_at: '2026-05-14T23:39:04.310Z'
510	  alpha_sweep_a025_s42:
511	    status: DONE
512	    retry_count: 0
513	    created_at: '2026-05-14T19:01:39.527Z'
514	    updated_at: '2026-05-16T00:10:24.973Z'
515	    spec:
516	      hypothesis: 'α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity
517	        lead 是否出现'
518	      model_name: EleutherAI/pythia-410m
519	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
520	      data_count: 5000
521	      seed: 42
522	      synthetic_ratio: 0.25
523	      num_generations: 10
524	      steps_per_gen: 5000
525	    conclusion: killed
526	    completed_at: '2026-05-16T00:10:24.973Z'
527	  alpha_sweep_a025_s42_v2:
528	    status: DONE
529	    retry_count: 0
530	    created_at: '2026-05-14T19:25:52.094Z'
531	    updated_at: '2026-05-16T00:10:24.568Z'
532	    spec:
533	      hypothesis: 'α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity
534	        lead 是否出现'
535	      model_name: EleutherAI/pythia-410m
536	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
537	      data_count: 5000
538	      seed: 42
539	      synthetic_ratio: 0.25
540	      num_generations: 10
541	      steps_per_gen: 5000
542	      parent: alpha_sweep_a025_s42 (killed, subsample bias fix)
543	    conclusion: killed
544	    failure_reason: 'data corruption: unkilled old process PID 46802 wrote concurrently
545	      with new PID 48454'
546	    completed_at: '2026-05-16T00:10:24.568Z'
547	  alpha_sweep_a025_s42_v3:
548	    status: DONE
549	    retry_count: 0
550	    created_at: '2026-05-14T21:04:05.726Z'
551	    updated_at: '2026-05-15T05:13:22.207Z'
552	    spec:
553	      hypothesis: 'α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持'
554	      model_name: EleutherAI/pythia-410m
555	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
556	      data_count: 5000
557	      seed: 42
558	      synthetic_ratio: 0.25
559	      num_generations: 10
560	      steps_per_gen: 5000
561	      parent: alpha_sweep_a025_s42_v2 (failed, data corruption)
562	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
563	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
564	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
565	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
566	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir
567	        results/alpha_sweep/a025_s42"
568	      server: westd-19828
569	      gpu:
570	      - cuda:1
571	      pid: '53069'
572	      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log
573	    reproduce:
574	      finished_at: '2026-05-15T01:18:42.377Z'
575	    extra:
576	      hook_events:
577	      - event: on_complete
578	        action: agent
579	        ts: '2026-05-15T01:18:43.329069+00:00'
580	    conclusion: success
581	    metrics:
582	      gen0_token_entropy: 3.2342
583	      gen10_token_entropy: 3.1017
584	      gen0_ece: 0.0108
585	      gen10_ece: 0.01942
586	      gen0_perplexity: 26.95
587	      gen10_perplexity: 22.32
588	      gen0_distinct_1: 0.0982
589	      gen10_distinct_1: 0.0586
590	      gen0_distinct_2: 0.5178
591	      gen10_distinct_2: 0.2219
592	      gen0_distinct_3: 0.8127
593	      gen10_distinct_3: 0.3263
594	      token_entropy_drift_pct: -4.1
595	      ece_drift_pct: 79.7
596	      perplexity_drift_pct: -17.2
597	      distinct_1_drift_pct: -40.3
598	      distinct_2_drift_pct: -57.1
599	      distinct_3_drift_pct: -59.9
600	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint
601	    completed_at: '2026-05-15T01:26:19.292Z'
602	    notes: 实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。
603	  plan_009_bootstrap_ty:
604	    status: DONE
605	    retry_count: 0
606	    created_at: '2026-05-14T21:33:04.665Z'
607	    updated_at: '2026-05-14T21:33:27.106Z'
608	    spec:
609	      hypothesis: Monte Carlo 验证 TY Granger 在短时间序列 (T=10,15,20,30) 下的 Type I error
610	        和 statistical power
611	      command: python bootstrap_ty_validation.py (N_sim=1000)
612	      server: westd-19828
613	      data_path: synthetic DGP (AR(1) for H0, VAR(2) for H1)
614	      data_count: 1000
615	      model_name: N/A (statistical simulation)
616	      seed: multiple
617	      log_path: results/bootstrap_ty_results.json
618	      checkpoint_path: N/A
619	    conclusion: success
620	    completed_at: '2026-05-14T21:33:24.769Z'
621	    metrics:
622	      T10_d0_type1: 0.081
623	      T10_d0_power: 0.205
624	      T10_d1_type1: 0.047
625	      T10_d1_power: 0.09
626	      T10_dadapt_type1: 0.052
627	      T10_dadapt_power: 0.05
628	      T20_d0_power: 0.409
629	      T20_d1_power: 0.172
630	      T30_d0_power: 0.606
631	      T30_d1_power: 0.283
632	  alpha_sweep_a050_s42:
633	    status: DONE
634	    retry_count: 0
635	    created_at: '2026-05-14T21:52:15.427Z'
636	    updated_at: '2026-05-15T13:17:48.134Z'
637	    spec:
638	      hypothesis: 'α=0.50 moderate contamination: test canary→diversity lead at mid-range
639	        synthetic ratio, key data point for non-monotonic dose-response'
640	      seed: 42
641	      model_name: EleutherAI/pythia-410m
642	      data_path: data/wikitext103_5k
643	      data_count: 5000
644	      synthetic_ratio: 0.5
645	      num_generations: 10
646	      steps_per_gen: 5000
647	    server: westd-19828
648	    gpu: cuda:1
649	    account: root
650	    reproduce:
651	      server: westd-19828
652	      gpu: cuda:1
653	      started_at: '2026-05-15T01:15:14.747Z'
654	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
655	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
656	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
657	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
658	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
659	        results/alpha_sweep/a050_s42"
660	      finished_at: '2026-05-15T05:42:25.788Z'
661	      training_hours: 4.45
662	    pid: '73737'
663	    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log
664	    metrics:
665	      progress: 11/11 gen (complete)
666	      gen0_token_entropy: 3.234
667	      gen10_token_entropy: 2.632
668	      gen0_ece: 0.011
669	      gen10_ece: 0.102
670	      gen0_perplexity: 26.95
671	      gen10_perplexity: 32.64
672	      gen0_distinct_1: 0.098
673	      gen10_distinct_1: 0.062
674	      gen0_distinct_2: 0.518
675	      gen10_distinct_2: 0.251
676	      gen0_distinct_3: 0.813
677	      gen10_distinct_3: 0.387
678	      token_entropy_drift_pct: -18.6
679	      ece_drift_pct: 842.8
680	      perplexity_drift_pct: 21.1
681	      distinct_1_drift_pct: -37.3
682	      distinct_2_drift_pct: -51.5
683	      distinct_3_drift_pct: -52.4
684	      granger_entropy_to_d1_p_raw: 0.095
685	      granger_entropy_to_d2_p_raw: 0.097
686	      granger_ece_to_d1_p_raw: 0.019
687	      granger_ece_to_d2_p_raw: 0.039
688	      granger_fdr_note: 4 tests within alpha=0.50; BH FDR threshold rank1=0.0125,
689	        rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative
690	        signal only.
691	      d024_non_monotonic: true
692	      d024_ece_vs_entropy_note: ECE raw p < entropy raw p at α=0.50 (0.019 vs 0.095
693	        at 5000 perms), 0/4 FDR-sig; regime switch hypothesis pending α=0.75 confirmation
694	    extra:
695	      hook_events:
696	      - event: on_complete
697	        action: agent
698	        ts: '2026-05-15T05:42:26.715028+00:00'
699	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint
700	    conclusion: success
701	    completed_at: '2026-05-15T05:46:48.692Z'
702	  alpha_sweep_a075_s42:
703	    status: DONE
704	    retry_count: 0
705	    created_at: '2026-05-14T21:52:17.315Z'
706	    updated_at: '2026-05-15T13:29:46.421Z'
707	    spec:
708	      hypothesis: 'α=0.75 high contamination: critical boundary point for Granger-causal
709	        detectability — determines Claim 1 scope (α≥0.75 vs α=1.0 only)'
710	      seed: 42
711	      model_name: EleutherAI/pythia-410m
712	      data_path: data/wikitext103_5k
713	      data_count: 5000
714	      synthetic_ratio: 0.75
715	      num_generations: 10
716	      steps_per_gen: 5000
717	    server: westd-19828
718	    gpu: cuda:1
719	    account: root
720	    reproduce:
721	      server: westd-19828
722	      gpu: cuda:1
723	      started_at: '2026-05-15T05:44:46.271Z'
724	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
725	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
726	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
727	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
728	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir
729	        results/alpha_sweep/a075_s42"
730	      finished_at: '2026-05-15T13:13:06.477Z'
731	      training_hours: 7.47
732	    pid: '89753'
733	    log_path: results/analysis/cross_alpha_v6_report.md
734	    metrics:
735	      progress: 11/11 gen (complete)
736	      gen0_token_entropy: 3.234
737	      gen10_token_entropy: 2.337
738	      gen0_ece: 0.0108
739	      gen10_ece: 0.2063
740	      gen0_perplexity: 26.95
741	      gen10_perplexity: 76.03
742	      gen0_distinct_1: 0.0982
743	      gen10_distinct_1: 0.0661
744	      gen0_distinct_2: 0.5178
745	      gen10_distinct_2: 0.3037
746	      gen0_distinct_3: 0.8127
747	      gen10_distinct_3: 0.5011
748	      token_entropy_drift_pct: -27.7
749	      ece_drift_pct: 1809.5
750	      perplexity_drift_pct: 182.1
751	      distinct_1_drift_pct: -32.7
752	      distinct_2_drift_pct: -41.3
753	      distinct_3_drift_pct: -38.4
754	      granger_ece_to_d1_p_fdr: 0.046
755	      granger_ece_to_d2_p_fdr: 0.046
756	      granger_entropy_to_d2_p_fdr: 0.048
757	      granger_entropy_to_d1_p_fdr: 0.054
758	      granger_fdr_sig_count: 3/8
759	      consensus_robust_pairs: 11/16
760	      xcorr_entropy_d1_lag: 2
761	      xcorr_entropy_d1_r: 0.973
762	    extra:
763	      hook_events:
764	      - event: on_complete
765	        action: agent
766	        ts: '2026-05-15T13:13:07.582542+00:00'
767	    conclusion: success
768	    checkpoint_path: results/alpha_sweep/a075_s42/
769	    completed_at: '2026-05-15T13:29:46.421Z'
770	  alpha_sweep_a010_s42:
771	    status: DONE
772	    retry_count: 0
773	    created_at: '2026-05-14T21:52:19.712Z'
774	    updated_at: '2026-05-16T00:03:53.018Z'
775	    spec:
776	      hypothesis: 'α=0.10 极低污染: phase boundary 精确化, canary signal 是否仍可检测'
777	      model_name: EleutherAI/pythia-410m
778	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
779	      data_count: 5000
780	      seed: 42
781	      synthetic_ratio: 0.1
782	      num_generations: 10
783	      steps_per_gen: 5000
784	    conclusion: killed
785	    completed_at: '2026-05-16T00:03:53.018Z'
786	  alpha_sweep_a060_s42:
787	    status: DONE
788	    retry_count: 0
789	    created_at: '2026-05-14T21:52:22.516Z'
790	    updated_at: '2026-05-16T00:04:01.429Z'
791	    spec:
792	      hypothesis: 'α=0.60 中高污染: phase boundary 精确化, 与 α=0.50/0.75 对比 lead time 变化'
793	      model_name: EleutherAI/pythia-410m
794	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
795	      data_count: 5000
796	      seed: 42
797	      synthetic_ratio: 0.6
798	      num_generations: 10
799	      steps_per_gen: 5000
800	    conclusion: killed
801	    completed_at: '2026-05-16T00:04:01.429Z'
802	  plan_006_s42:
803	    status: DONE
804	    retry_count: 0
805	    created_at: '2026-05-14T23:31:35.454Z'
806	    updated_at: '2026-05-15T12:17:14.093Z'
807	    spec:
808	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh
809	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
810	        HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1
811	        python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42
812	        --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000"
813	      server: westd-19828
814	      gpu:
815	      - cuda:0
816	      pid: '68368'
817	      log_path: ~/runs/distrib_canary_collapse/plan_006_s42.log
818	      submitted_at: '2026-05-14T23:41:30.666Z'
819	      submitted_via: submit_training_job
820	      backend: tmux
821	      account: root
822	      wall_clock_seconds: 43212.6
823	      gpu_hours: 12.0
824	    server: westd-19828
825	    gpu: cuda:0
826	    account: root
827	    reproduce:
828	      server: westd-19828
829	      gpu: cuda:0
830	      started_at: '2026-05-14T23:41:29.125Z'
831	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh
832	        && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export
833	        HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1
834	        python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42
835	        --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000"
836	      finished_at: '2026-05-15T11:41:42.336Z'
837	      training_hours: 12.0
838	    pid: '68368'
839	    log_path: ~/runs/distrib_canary_collapse/plan_006_s42.log
840	    metrics:
841	      progress: 18/20 gen (gen_0-17 complete, gen_18-20 timeout)
842	      gen0_token_entropy: 3.2342
843	      gen17_token_entropy: 1.1819
844	      gen0_ece: 0.0108
845	      gen17_ece: 0.4454
846	      gen0_perplexity: 26.95
847	      gen17_perplexity: 3367.66
848	      gen0_distinct_1: 0.0982
849	      gen17_distinct_1: 0.0756
850	      gen0_distinct_2: 0.5178
851	      gen17_distinct_2: 0.3617
852	      gen0_distinct_3: 0.8127
853	      gen17_distinct_3: 0.5865
854	      token_entropy_drift_pct_gen0_17: -63.4
855	      distinct_1_drift_pct_gen0_17: -23
856	      distinct_2_drift_pct_gen0_17: -30.1
857	      distinct_3_drift_pct_gen0_17: -27.8
858	      ece_drift_pct_gen0_17: 4024
859	      ppl_drift_pct_gen0_17: 12395
860	      phase1_rapid_collapse: gen0-5
861	      phase2_apparent_plateau: gen5-12
862	      phase3_secondary_decline: gen13-17
863	      phase3_d2_decline_pct: -5.8
864	      phase3_d3_decline_pct: -6.9
865	      diversity_saturated_at_gen: 5
866	      diversity_secondary_decline_at_gen: 13
867	      perplexity_saturated: false
868	    failure_reason: EXIT_CODE=124 (timeout — exceeded timeout_hours)
869	    conclusion: failed
870	    completed_at: '2026-05-15T11:41:43.235Z'
871	    extra:
872	      hook_events:
873	      - event: on_failed
874	        action: agent
875	        ts: '2026-05-15T11:41:44.300301+00:00'
876	    notes: 'gen_0-17 complete (T=18). 三相 collapse: Phase1 急速崩塌 gen0-5 (d1 -20.6%,
877	      entropy -63.8%), Phase2 表观稳态 gen5-12 (diversity <0.3% 变化, perplexity 仍+167%),
878	      Phase3 二次衰退 gen13-17 (d2 -5.8%, d3 -6.9%). Perplexity 未饱和 (26.95→3367.66, +12395%).
879	      T=18 vs T=10: 新增 diversity 二次衰退在 T=10 window 不可见. TY power 预估 ~0.28-0.41 (vs
880	      T=10 的 0.05-0.21).'
881	  plan_006_s43:
882	    status: DONE
883	    retry_count: 0
884	    created_at: '2026-05-14T23:31:37.257Z'
885	    updated_at: '2026-05-16T00:03:51.617Z'
886	    spec:
887	      plan_id: plan_006
888	      hypothesis: 'Multi-seed replication of three-phase collapse dynamics: verify
889	        Phase 3 secondary decline (gen 13+) reproduces with seed=43, confirming it
890	        is not a single-seed artifact'
891	      model_name: EleutherAI/pythia-410m
892	      seed: 43
893	      data_path: data/wikitext103_5k
894	      num_generations: 18
895	      synthetic_ratio: 1
896	      max_lag: 10
897	      data_count: 5000
898	      steps_per_gen: 5000
899	      parent: plan_006_s42
900	      claim: 1
901	      priority: P0
902	    conclusion: killed
903	    completed_at: '2026-05-16T00:03:51.617Z'
904	  method_ablation_phase1:
905	    status: DONE
906	    retry_count: 0
907	    created_at: '2026-05-14T23:49:16.519Z'
908	    updated_at: '2026-05-14T23:49:40.162Z'
909	    spec:
910	      plan_id: plan_002
911	      hypothesis: lead-lag 结论对分析方法高度敏感——naive Pearson 100% SIG vs TY 25% SIG，方法选择改变
912	        75% 的结论
913	      command: python method_ablation.py + python permutation_granger.py (差分版)
914	      server: westd-19828
915	      data_path: results/mvp/rep_{42,43,44,45}/all_metrics.json
916	      data_count: 4
917	      model_name: N/A (analysis on MVP data)
918	      seed: 42,43,44,45
919	      checkpoint_path: N/A
920	      log_path: results/mvp/analysis/method_ablation.json
921	    conclusion: success
922	    completed_at: '2026-05-14T23:49:37.295Z'
923	    metrics:
924	      spurious_rate_5method: 0.75
925	      spurious_rate_4method: 0.625
926	      naive_sig: 16/16
927	      differenced_sig: 14/16
928	      threshold_sig: 9/16
929	      permutation_granger_sig: 6/16
930	      ty_sig: 4/16
931	      ty_power_T10: 0.05-0.20
932	      bh_fdr_flips: 0
933	  alpha_sweep_a025_s43:
934	    status: DONE
935	    retry_count: 0
936	    created_at: '2026-05-15T06:58:43.090Z'
937	    updated_at: '2026-05-15T17:39:43.623Z'
938	    spec:
939	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
940	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
941	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
942	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
943	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir
944	        results/alpha_sweep/a025_s43"
945	      server: westd-19828
946	      gpu:
947	      - cuda:1
948	      pid: '121635'
949	      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log
950	      submitted_at: '2026-05-15T13:16:31.189Z'
951	      submitted_via: submit_training_job
952	      backend: tmux
953	      account: root
954	      wall_clock_seconds: 15792.4
955	      gpu_hours: 4.39
956	    server: westd-19828
957	    gpu: cuda:1
958	    pid: '121635'
959	    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log
960	    reproduce:
961	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
962	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
963	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
964	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
965	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir
966	        results/alpha_sweep/a025_s43"
967	      finished_at: '2026-05-15T17:36:20.945Z'
968	    metrics:
969	      gen0:
970	        token_entropy: 3.2342
971	        ece: 0.0108
972	        perplexity: 26.949
973	        distinct_1: 0.09833
974	        distinct_2: 0.5132
975	        distinct_3: 0.8057
976	        effective_rank: 46.61
977	        mauve: 0.03351
978	      gen10:
979	        token_entropy: 3.0723
980	        ece: 0.02146
981	        perplexity: 21.899
982	        distinct_1: 0.05849
983	        distinct_2: 0.2236
984	        distinct_3: 0.333
985	        effective_rank: 45.37
986	        mauve: 0.01871
987	      drift_pct:
988	        token_entropy: -5
989	        ece: 98.6
990	        perplexity: -18.7
991	        distinct_1: -40.5
992	        distinct_2: -56.4
993	        distinct_3: -58.7
994	        effective_rank: -2.7
995	        mauve: -44.2
996	    extra:
997	      hook_events:
998	      - event: on_complete
999	        action: agent
1000	        ts: '2026-05-15T17:36:22.072334+00:00'
1001	    conclusion: success
1002	    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint
1003	    completed_at: '2026-05-15T17:39:43.624Z'
1004	  alpha_sweep_a050_s43:
1005	    status: DONE
1006	    retry_count: 0
1007	    created_at: '2026-05-15T06:58:45.880Z'
1008	    updated_at: '2026-05-15T22:15:50.290Z'
1009	    spec:
1010	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
1011	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1012	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
1013	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
1014	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
1015	        results/alpha_sweep/a050_s43"
1016	      server: westd-19828
1017	      gpu:
1018	      - cuda:1
1019	      pid: '134860'
1020	      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log
1021	      submitted_at: '2026-05-15T17:40:27.060Z'
1022	      submitted_via: submit_training_job
1023	      backend: tmux
1024	      account: root
1025	      wall_clock_seconds: 16523.2
1026	      gpu_hours: 4.59
1027	    server: westd-19828
1028	    gpu: cuda:1
1029	    pid: '134860'
1030	    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log
1031	    reproduce:
1032	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
1033	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1034	        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
1035	        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
1036	        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
1037	        results/alpha_sweep/a050_s43"
1038	      finished_at: '2026-05-15T22:00:14.725Z'
1039	    extra:
1040	      hook_events:
1041	      - event: on_complete
1042	        action: agent
1043	        ts: '2026-05-15T22:00:15.908424+00:00'
1044	    conclusion: success
1045	    checkpoint_path: results/alpha_sweep/a050_s43/gen_10/checkpoint/
1046	    metrics:
1047	      gen0_token_entropy: 3.234195
1048	      gen0_ece: 0.010805
1049	      gen0_perplexity: 26.948959
1050	      gen10_token_entropy: 2.672
1051	      gen10_ece: 0.097
1052	      gen10_perplexity: 32.633
1053	      gen0_distinct_1: 0.09833
1054	      gen0_distinct_2: 0.5132
1055	      gen0_distinct_3: 0.8057
1056	      gen10_distinct_1: 0.0624
1057	      gen10_distinct_2: 0.2617
1058	      gen10_distinct_3: 0.4126
1059	      token_entropy_drift_pct: -17.4
1060	      ece_drift_pct: 799
1061	      perplexity_drift_pct: 21.1
1062	      distinct_1_drift_pct: -36.5
1063	      distinct_2_drift_pct: -49
1064	      distinct_3_drift_pct: -48.8
1065	      cross_seed_note: 'vs s42: drift direction identical, magnitude <7% deviation,
1066	        ppl near-identical (32.633 vs 32.64)'
1067	    completed_at: '2026-05-15T22:00:14Z'
1068	  alpha_sweep_a025_s44:
1069	    status: DONE
1070	    retry_count: 0
1071	    created_at: '2026-05-15T06:58:48.224Z'
1072	    updated_at: '2026-05-16T02:49:46.894Z'
1073	    spec:
1074	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
1075	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1076	        && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export
1077	        SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh
1078	        && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py
1079	        --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
1080	        10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44"
1081	      server: westd-19828
1082	      gpu:
1083	      - cuda:1
1084	      pid: '147811'
1085	      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log
1086	      submitted_at: '2026-05-15T22:04:28.318Z'
1087	      submitted_via: submit_training_job
1088	      backend: tmux
1089	      account: root
1090	      wall_clock_seconds: 17118.6
1091	      gpu_hours: 4.76
1092	    server: westd-19828
1093	    gpu: cuda:1
1094	    account: root
1095	    reproduce:
1096	      server: westd-19828
1097	      gpu: cuda:1
1098	      started_at: '2026-05-15T22:04:26.677Z'
1099	      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
1100	        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1101	        && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export
1102	        SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh
1103	        && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py
1104	        --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations
1105	        10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44"
1106	      finished_at: '2026-05-16T02:24:25.056Z'
1107	      training_hours: 4.33
1108	    pid: '147811'
1109	    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log
1110	    extra:
1111	      hook_events:
1112	      - event: on_complete
1113	        action: agent
1114	        ts: '2026-05-16T02:24:26.614491+00:00'
1115	    metrics: "{\n  \"gen0\": {\n    \"token_entropy\": 3.2342, \"ece\": 0.01080, \"\
1116	      perplexity\": 26.949,\n    \"distinct_1\": 0.09809, \"distinct_2\": 0.51324,\
1117	      \ \"distinct_3\": 0.80577,\n    \"effective_rank\": 46.613, \"mauve\": 0.02954\n\
1118	      \  },\n  \"gen10\": {\n    \"token_entropy\": 3.0721, \"ece\": 0.01804, \"perplexity\"\
1119	      : 21.984,\n    \"distinct_1\": 0.05884, \"distinct_2\": 0.22703, \"distinct_3\"\
1120	      : 0.33644,\n    \"effective_rank\": 44.354, \"mauve\": 0.01753\n  },\n  \"drift_pct\"\
1121	      : {\n    \"token_entropy\": -5.01, \"ece\": +67.0, \"perplexity\": -18.42,\n\
1122	      \    \"distinct_1\": -40.01, \"distinct_2\": -55.77, \"distinct_3\": -58.24,\n\
1123	      \    \"effective_rank\": -4.85, \"mauve\": -40.65\n  }\n}"
1124	    conclusion: success
1125	    checkpoint_path: results/alpha_sweep/a025_s44/gen_10/checkpoint
1126	    completed_at: '2026-05-16T02:49:46.894Z'
1127	  alpha_sweep_a050_s44:
1128	    status: DONE
1129	    retry_count: 0
1130	    created_at: '2026-05-15T06:58:50.550Z'
1131	    updated_at: '2026-05-16T00:03:52.118Z'
1132	    spec:
1133	      hypothesis: 'α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力'
1134	      model_name: EleutherAI/pythia-410m
1135	      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
1136	      data_count: 5000
1137	      seed: 44
1138	      synthetic_ratio: 0.5
1139	      num_generations: 10
1140	      steps_per_gen: 5000
1141	      parent: alpha_sweep_a050_s42
1142	      priority: D026-4
1143	    conclusion: killed
1144	    completed_at: '2026-05-16T00:03:52.118Z'
1145	  method_ablation_phase2:
1146	    status: DONE
1147	    retry_count: 0
1148	    created_at: '2026-05-15T08:58:35.270Z'
1149	    updated_at: '2026-05-15T11:07:42.688Z'
1150	    spec:
1151	      hypothesis: Method sensitivity is compounded by regime dependence — method x
1152	        alpha interaction is the headline Claim 3 evidence
1153	      command: python method_ablation_phase2.py
1154	      server: westd-19828
1155	      data_path: results/alpha_sweep + results/mvp
1156	      data_count: 56
1157	      model_name: N/A (analysis)
1158	      seed: 42,43,44,45
1159	      checkpoint_path: N/A
1160	      log_path: results/method_ablation_phase2_panel.json
1161	    conclusion: success
1162	    metrics:
1163	      n_panel_rows: 56
1164	      n_alphas: 4
1165	      alphas:
1166	      - 0
1167	      - 0.25
1168	      - 0.5
1169	      - 1
1170	      naive_sig_rate_overall: 1
1171	      perm_granger_sig_rate_a000_raw: 0
1172	      perm_granger_sig_rate_a000_fdr: 0
1173	      perm_granger_sig_rate_a025_raw: 0.25
1174	      perm_granger_sig_rate_a025_fdr: 0
1175	      perm_granger_sig_rate_a050_raw: 0.25
1176	      perm_granger_sig_rate_a050_fdr: 0
1177	      perm_granger_sig_rate_a100_raw: 0.75
1178	      perm_granger_sig_rate_a100_fdr: 0.75
1179	      TY_sig_rate_a000_raw: 0
1180	      TY_sig_rate_a000_fdr: 0
1181	      TY_sig_rate_a025_raw: 0.625
1182	      TY_sig_rate_a025_fdr: 0.375
1183	      TY_sig_rate_a050_raw: 0
1184	      TY_sig_rate_a050_fdr: 0
1185	      TY_sig_rate_a100_raw: 0.5938
1186	      TY_sig_rate_a100_fdr: 0.5938
1187	      diff_sig_rate_a000_raw: 0.5
1188	      diff_sig_rate_a000_fdr: 0.375
1189	      mean_inter_method_kappa: 0.185
1190	      naive_vs_perm_granger_flip_rate: 0.5
1191	      naive_vs_TY_flip_rate: 0.57
1192	      fdr_flips_perm_granger: 4
1193	      pair_verdict_a100_perm_granger: 6/8
1194	      pair_verdict_a100_TY: 6/8
1195	      entropy_to_diversity_a100_all_5methods_sig: true
1196	      fdr_correction: BH q=0.05
1197	    completed_at: '2026-05-15T08:58:54.741Z'
1198	  gen_wiki_gpt2m_a025_s42:
1199	    status: RUNNING
1200	    retry_count: 0
1201	    created_at: '2026-05-15T10:35:16.032Z'
1202	    updated_at: '2026-05-15T22:22:52.921Z'
1203	    spec:
1204	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1205	        base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1206	        TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py
1207	        --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio
1208	        0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir
1209	        results/gen_wiki_gpt2m_a025_s42"
1210	      server: westd-19828
1211	      gpu:
1212	      - cuda:0
1213	      pid: '149202'
1214	      log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log
1215	      submitted_at: '2026-05-15T22:22:52.615Z'
1216	      submitted_via: submit_training_job
1217	      backend: tmux
1218	      account: root
1219	    server: westd-19828
1220	    gpu: cuda:0
1221	    account: root
1222	    reproduce:
1223	      server: westd-19828
1224	      gpu: cuda:0
1225	      started_at: '2026-05-15T22:22:51.021Z'
1226	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1227	        base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1228	        TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py
1229	        --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio
1230	        0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir
1231	        results/gen_wiki_gpt2m_a025_s42"
1232	    pid: '149202'
1233	    log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log
1234	  gen_wiki_gpt2m_a100_s42:
1235	    status: DONE
1236	    retry_count: 0
1237	    created_at: '2026-05-15T10:35:18.700Z'
1238	    updated_at: '2026-05-15T12:01:58.523Z'
1239	    spec:
1240	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1241	        base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1242	        HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name
1243	        gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations
1244	        10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42"
1245	      server: westd-19828
1246	      gpu:
1247	      - cuda:0
1248	      pid: '115532'
1249	      log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log
1250	      submitted_at: '2026-05-15T11:57:48.767Z'
1251	      submitted_via: submit_training_job
1252	      backend: tmux
1253	      account: root
1254	      wall_clock_seconds: 249.8
1255	      gpu_hours: 0.07
1256	    server: westd-19828
1257	    gpu: cuda:0
1258	    account: root
1259	    reproduce:
1260	      server: westd-19828
1261	      gpu: cuda:0
1262	      started_at: '2026-05-15T11:57:47.340Z'
1263	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1264	        base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1265	        HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name
1266	        gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations
1267	        10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42"
1268	    pid: '115532'
1269	    log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log
1270	    conclusion: killed
1271	    completed_at: '2026-05-15T12:01:58.523Z'
1272	  plan_006_s42_resume:
1273	    status: DONE
1274	    retry_count: 0
1275	    created_at: '2026-05-15T11:55:26.236Z'
1276	    updated_at: '2026-05-15T12:10:54.859Z'
1277	    spec:
1278	      command: python -u resume_plan006_s42.py
1279	      server: westd-19828
1280	      gpu:
1281	      - cuda:0
1282	      pid: '114844'
1283	      log_path: ~/runs/distrib_canary_collapse/plan_006_s42_resume.log
1284	      submitted_at: '2026-05-15T11:55:31.984Z'
1285	      submitted_via: submit_training_job
1286	      backend: tmux
1287	      account: root
1288	      hypothesis: 恢复 plan_006_s42 从 gen_17，完成 gen_18-20 + all_metrics（α=1.0, 20gen,
1289	        s42）
1290	      seed: 42
1291	      model_name: EleutherAI/pythia-410m
1292	      data_path: data/wikitext103
1293	      data_count: 0
1294	      checkpoint_path: N/A
1295	      notes: D034 决定不恢复，T=18 数据已足够（超出 T=15 目标）。plan_006_s42 gen_0-17 数据可用。
1296	      wall_clock_seconds: 921.5
1297	      gpu_hours: 0.26
1298	    conclusion: killed
1299	    completed_at: '2026-05-15T12:10:53.514Z'
1300	    notes: D034 决定不恢复。T=18 数据已足够（超出 T=15 目标）。原 plan_006_s42 gen_0-17 数据可用于 power analysis
1301	      + supplementary。
1302	  gen_wiki_gpt2m_a100_s42_v2:
1303	    status: DONE
1304	    retry_count: 0
1305	    created_at: '2026-05-15T12:02:06.478Z'
1306	    updated_at: '2026-05-15T12:04:50.741Z'
1307	    spec:
1308	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1309	        base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1310	        TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py
1311	        --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k
1312	        --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size
1313	        32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42"
1314	      server: westd-19828
1315	      gpu:
1316	      - cuda:0
1317	      pid: '116204'
1318	      log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log
1319	      submitted_at: '2026-05-15T12:02:14.440Z'
1320	      submitted_via: submit_training_job
1321	      backend: tmux
1322	      account: root
1323	      wall_clock_seconds: 18.0
1324	      gpu_hours: 0.01
1325	    server: westd-19828
1326	    gpu: cuda:0
1327	    account: root
1328	    reproduce:
1329	      server: westd-19828
1330	      gpu: cuda:0
1331	      started_at: '2026-05-15T12:02:13.557Z'
1332	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1333	        base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1334	        TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py
1335	        --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k
1336	        --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size
1337	        32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42"
1338	      finished_at: '2026-05-15T12:02:31.643Z'
1339	      training_hours: 0.01
1340	    pid: '116204'
1341	    log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log
1342	    failure_reason: EXIT_CODE=1 (generic error — check log tail)
1343	    conclusion: killed
1344	    completed_at: '2026-05-15T12:02:32.472Z'
1345	    extra:
1346	      hook_events:
1347	      - event: on_failed
1348	        action: agent
1349	        ts: '2026-05-15T12:02:33.931882+00:00'
1350	  gen_wiki_gpt2m_a100_s42_v3:
1351	    status: DONE
1352	    retry_count: 0
1353	    created_at: '2026-05-15T12:07:20.050Z'
1354	    updated_at: '2026-05-15T22:30:21.573Z'
1355	    spec:
1356	      hypothesis: Method sensitivity patterns (Granger FDR collapse, cross-correlation
1357	        dominance) generalize from GPT-2-small to GPT-2-medium, validating cross-architecture
1358	        universality of methodological pitfalls
1359	      seed: 42
1360	      model_name: gpt2-medium
1361	      data_path: data/wikitext103_5k
1362	      data_count: 5000
1363	    server: westd-19828
1364	    gpu: cuda:0
1365	    account: root
1366	    reproduce:
1367	      server: westd-19828
1368	      gpu: cuda:0
1369	      started_at: '2026-05-15T12:07:30.366Z'
1370	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1371	        base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache
1372	        TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py
1373	        --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio
1374	        1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir
1375	        results/gen_wiki_gpt2m_a100_s42"
1376	      finished_at: '2026-05-15T22:14:43.852Z'
1377	      training_hours: 10.12
1378	    pid: '117632'
1379	    log_path: ~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v3.log
1380	    metrics:
1381	      token_entropy_drift_pct: -86.5
1382	      ece_drift_pct: 4543
1383	      perplexity_drift_pct: 44703
1384	      distinct_1_drift_pct: -12.4
1385	      distinct_2_drift_pct: -14.7
1386	      distinct_3_drift_pct: -12.7
1387	      five_method_forward_consensus: 6/6 pairs at 4/5 methods (Tier 3)
1388	      five_method_reverse_consensus: 0/6 pairs
1389	      naive_xcorr_forward: '|r|>0.98, all sig'
1390	      diff_xcorr_forward: all p_fdr<0.001
1391	      diff_xcorr_reverse: all p>0.18 (clean directional separation)
1392	      threshold_onset_entropy: gen 1 (earliest canary)
1393	      threshold_onset_ece: gen 1-2
1394	      threshold_onset_diversity: gen 3
1395	      perm_granger_forward: p_fdr=0.003, BH corrected
1396	      ty_granger_forward: 0/6 sig (df_resid=1-4, underpowered, consistent with Pythia
1397	        C001)
1398	      entropy_leads_diversity_lag: 1-2 gen
1399	      ece_leads_diversity_lag: 1 gen
1400	      diversity_plateau_from: gen5
1401	      cross_arch_note: Replicates Pythia entropy-leads-diversity pattern at Tier 3
1402	        consensus. TY underpowered as expected.
1403	    extra:
1404	      hook_events:
1405	      - event: on_complete
1406	        action: agent
1407	        ts: '2026-05-15T22:14:45.029003+00:00'
1408	    conclusion: success
1409	    checkpoint_path: results/gen_wiki_gpt2m_a100_s42/
1410	    completed_at: '2026-05-15T22:18:22.762Z'
1411	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5a540b8-44e8-4698-b7d9-d147e4670bd4",
  "isSidechain": true,
  "promptId": "bfd10638-11d5-4fd5-a51c-fdbcd38a9e94",
  "agentId": "ae0545680b43593da",
  "type": "user",
  "uuid": "5d12181a-b7e6-4b30-98ec-f046a0e8e481",
  "sourceToolAssistantUUID": "a5a540b8-44e8-4698-b7d9-d147e4670bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T06:11:31.408Z_

Now let me search for all experiments with synthetic_ratio 0.50 or "a050" in the exp_id:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d12181a-b7e6-4b30-98ec-f046a0e8e481",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kao5bvP16GzVUQMwYi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "30f187a1-c8d1-404b-a73a-a17af96be10f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019f7igZsUK1wToQLr3nsZWh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 26597,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26597,
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

_source line 6 · 2026-05-16T06:11:32.462Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QEN1xVSUBkSJc4B2BQuN5H`</summary>

```json
{
  "pattern": "a050|synthetic_ratio.*0\\.5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30f187a1-c8d1-404b-a73a-a17af96be10f",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kao5bvP16GzVUQMwYi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67824fcf-7798-4d9b-a211-a7e0d1be7671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019f7igZsUK1wToQLr3nsZWh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 26597,
      "cache_read_input_tokens": 20747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26597,
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

_source line 7 · 2026-05-16T06:11:32.480Z_

<details><summary>↩ Tool result · `toolu_01QEN1xVSUBkSJc4B2BQuN5H`</summary>

```text
629-      T20_d1_power: 0.172
630-      T30_d0_power: 0.606
631-      T30_d1_power: 0.283
632:  alpha_sweep_a050_s42:
633-    status: DONE
634-    retry_count: 0
635-    created_at: '2026-05-14T21:52:15.427Z'
--
641-      model_name: EleutherAI/pythia-410m
642-      data_path: data/wikitext103_5k
643-      data_count: 5000
644:      synthetic_ratio: 0.5
645-      num_generations: 10
646-      steps_per_gen: 5000
647-    server: westd-19828
--
655-        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
656-        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
657-        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
658:        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
659:        results/alpha_sweep/a050_s42"
660-      finished_at: '2026-05-15T05:42:25.788Z'
661-      training_hours: 4.45
662-    pid: '73737'
663:    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log
664-    metrics:
665-      progress: 11/11 gen (complete)
666-      gen0_token_entropy: 3.234
--
696-      - event: on_complete
697-        action: agent
698-        ts: '2026-05-15T05:42:26.715028+00:00'
699:    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint
700-    conclusion: success
701-    completed_at: '2026-05-15T05:46:48.692Z'
702-  alpha_sweep_a075_s42:
--
1001-    conclusion: success
1002-    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint
1003-    completed_at: '2026-05-15T17:39:43.624Z'
1004:  alpha_sweep_a050_s43:
1005-    status: DONE
1006-    retry_count: 0
1007-    created_at: '2026-05-15T06:58:45.880Z'
--
1011-        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1012-        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
1013-        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
1014:        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
1015:        results/alpha_sweep/a050_s43"
1016-      server: westd-19828
1017-      gpu:
1018-      - cuda:1
1019-      pid: '134860'
1020:      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log
1021-      submitted_at: '2026-05-15T17:40:27.060Z'
1022-      submitted_via: submit_training_job
1023-      backend: tmux
--
1027-    server: westd-19828
1028-    gpu: cuda:1
1029-    pid: '134860'
1030:    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log
1031-    reproduce:
1032-      command: bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache
1033-        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
1034-        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
1035-        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k
1036:        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir
1037:        results/alpha_sweep/a050_s43"
1038-      finished_at: '2026-05-15T22:00:14.725Z'
1039-    extra:
1040-      hook_events:
--
1042-        action: agent
1043-        ts: '2026-05-15T22:00:15.908424+00:00'
1044-    conclusion: success
1045:    checkpoint_path: results/alpha_sweep/a050_s43/gen_10/checkpoint/
1046-    metrics:
1047-      gen0_token_entropy: 3.234195
1048-      gen0_ece: 0.010805
--
1124-    conclusion: success
1125-    checkpoint_path: results/alpha_sweep/a025_s44/gen_10/checkpoint
1126-    completed_at: '2026-05-16T02:49:46.894Z'
1127:  alpha_sweep_a050_s44:
1128-    status: DONE
1129-    retry_count: 0
1130-    created_at: '2026-05-15T06:58:50.550Z'
--
1135-      data_path: /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
1136-      data_count: 5000
1137-      seed: 44
1138:      synthetic_ratio: 0.5
1139-      num_generations: 10
1140-      steps_per_gen: 5000
1141:      parent: alpha_sweep_a050_s42
1142-      priority: D026-4
1143-    conclusion: killed
1144-    completed_at: '2026-05-16T00:03:52.118Z'
--
1172-      perm_granger_sig_rate_a000_fdr: 0
1173-      perm_granger_sig_rate_a025_raw: 0.25
1174-      perm_granger_sig_rate_a025_fdr: 0
1175:      perm_granger_sig_rate_a050_raw: 0.25
1176:      perm_granger_sig_rate_a050_fdr: 0
1177-      perm_granger_sig_rate_a100_raw: 0.75
1178-      perm_granger_sig_rate_a100_fdr: 0.75
1179-      TY_sig_rate_a000_raw: 0
1180-      TY_sig_rate_a000_fdr: 0
1181-      TY_sig_rate_a025_raw: 0.625
1182-      TY_sig_rate_a025_fdr: 0.375
1183:      TY_sig_rate_a050_raw: 0
1184:      TY_sig_rate_a050_fdr: 0
1185-      TY_sig_rate_a100_raw: 0.5938
1186-      TY_sig_rate_a100_fdr: 0.5938
1187-      diff_sig_rate_a000_raw: 0.5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67824fcf-7798-4d9b-a211-a7e0d1be7671",
  "isSidechain": true,
  "promptId": "bfd10638-11d5-4fd5-a51c-fdbcd38a9e94",
  "agentId": "ae0545680b43593da",
  "type": "user",
  "uuid": "cb3b7c66-3522-4a4a-bbef-2c8669713e97",
  "sourceToolAssistantUUID": "67824fcf-7798-4d9b-a211-a7e0d1be7671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T06:11:32.866Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JV4H5jC913XqAZQ6NbQwe7`</summary>

```json
{
  "pattern": "a000|synthetic_ratio.*0\\.0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3b7c66-3522-4a4a-bbef-2c8669713e97",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kao5bvP16GzVUQMwYi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2b8d996-8dc3-4f63-8fc3-3992c50216ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019f7igZsUK1wToQLr3nsZWh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 26597,
      "cache_read_input_tokens": 20747,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 303,
          "cache_read_input_tokens": 20747,
          "cache_creation_input_tokens": 26597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26597,
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

_source line 9 · 2026-05-16T06:11:32.884Z_

<details><summary>↩ Tool result · `toolu_01JV4H5jC913XqAZQ6NbQwe7`</summary>

```text
453-      distinct_2_drift_pct: -35.9639
454-      distinct_3_drift_pct: -32.7352
455-    completed_at: '2026-05-14T17:58:00.661Z'
456:  alpha_sweep_a000_s42:
457-    status: DONE
458-    retry_count: 0
459-    created_at: '2026-05-14T19:01:37.470Z'
--
471-        && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com
472-        && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&
473-        PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k
474:        --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir
475:        results/alpha_sweep/a000_s42"
476-      server: westd-19828
477-      gpu:
478-      - cuda:0
479-      pid: '46716'
480:      log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log
481-    reproduce:
482-      finished_at: '2026-05-14T23:36:35.414Z'
483-    extra:
--
486-        action: agent
487-        ts: '2026-05-14T23:36:36.221435+00:00'
488-    conclusion: success
489:    checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint
490:    log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log
491-    metrics:
492-      gen0_token_entropy: 3.2342
493-      gen10_token_entropy: 3.0693
--
1168-      - 0.5
1169-      - 1
1170-      naive_sig_rate_overall: 1
1171:      perm_granger_sig_rate_a000_raw: 0
1172:      perm_granger_sig_rate_a000_fdr: 0
1173-      perm_granger_sig_rate_a025_raw: 0.25
1174-      perm_granger_sig_rate_a025_fdr: 0
1175-      perm_granger_sig_rate_a050_raw: 0.25
1176-      perm_granger_sig_rate_a050_fdr: 0
1177-      perm_granger_sig_rate_a100_raw: 0.75
1178-      perm_granger_sig_rate_a100_fdr: 0.75
1179:      TY_sig_rate_a000_raw: 0
1180:      TY_sig_rate_a000_fdr: 0
1181-      TY_sig_rate_a025_raw: 0.625
1182-      TY_sig_rate_a025_fdr: 0.375
1183-      TY_sig_rate_a050_raw: 0
1184-      TY_sig_rate_a050_fdr: 0
1185-      TY_sig_rate_a100_raw: 0.5938
1186-      TY_sig_rate_a100_fdr: 0.5938
1187:      diff_sig_rate_a000_raw: 0.5
1188:      diff_sig_rate_a000_fdr: 0.375
1189-      mean_inter_method_kappa: 0.185
1190-      naive_vs_perm_granger_flip_rate: 0.5
1191-      naive_vs_TY_flip_rate: 0.57
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b8d996-8dc3-4f63-8fc3-3992c50216ea",
  "isSidechain": true,
  "promptId": "bfd10638-11d5-4fd5-a51c-fdbcd38a9e94",
  "agentId": "ae0545680b43593da",
  "type": "user",
  "uuid": "afb6e5be-a888-4925-8b82-17bc1c571298",
  "sourceToolAssistantUUID": "a2b8d996-8dc3-4f63-8fc3-3992c50216ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-16T06:11:38.474Z_

Perfect! I found the experiments. Let me now extract the complete details for all α=0.50 experiments and verify the α=0.0 experiments:

## Summary of Findings

### Experiments with synthetic_ratio 0.50 (α=0.50):

**1. alpha_sweep_a050_s42**
- exp_id: alpha_sweep_a050_s42
- seed: 42
- status: DONE
- conclusion: success
- synthetic_ratio: 0.5

**2. alpha_sweep_a050_s43**
- exp_id: alpha_sweep_a050_s43
- seed: 43
- status: DONE
- conclusion: success
- synthetic_ratio: 0.5

**3. alpha_sweep_a050_s44**
- exp_id: alpha_sweep_a050_s44
- seed: 44
- status: DONE
- conclusion: killed
- synthetic_ratio: 0.5

**Valid experiments at α=0.50 (status=DONE, conclusion=success): 2 seeds**
- Seed 42: VALID
- Seed 43: VALID
- Seed 44: KILLED (not valid)

### Experiments with synthetic_ratio 0.0 (α=0.0):

**1. alpha_sweep_a000_s42**
- exp_id: alpha_sweep_a000_s42
- seed: 42
- status: DONE
- conclusion: success
- synthetic_ratio: 0.0

**Finding: There is only ONE experiment at α=0.0 in the registry: seed=42**

No other α=0.0 experiments exist besides seed=42.

### Summary Table:

| Alpha | Seed | Exp_ID | Status | Conclusion | Valid? |
|-------|------|--------|--------|-----------|--------|
| 0.50 | 42 | alpha_sweep_a050_s42 | DONE | success | YES |
| 0.50 | 43 | alpha_sweep_a050_s43 | DONE | success | YES |
| 0.50 | 44 | alpha_sweep_a050_s44 | DONE | killed | NO |
| 0.0 | 42 | alpha_sweep_a000_s42 | DONE | success | YES |

**Key finding: You have 2 valid seeds at α=0.50 (seeds 42 and 43 with successful completions). Seed 44 was killed, so it doesn't count as valid.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afb6e5be-a888-4925-8b82-17bc1c571298",
  "isSidechain": true,
  "agentId": "ae0545680b43593da",
  "requestId": "req_011Cb5kb5NeBnJssEAabWTe6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eec2ca13-e7f7-408c-bab0-161299b85ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/reviewer_32964115",
  "sessionId": "2c3e5d83-b422-4bac-ad82-a671bb5f4094",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "graceful-baking-micali",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ULgWKL5Wz8oasaHGoDTYy9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 47344,
      "output_tokens": 612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 612,
          "cache_read_input_tokens": 47344,
          "cache_creation_input_tokens": 3474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3474,
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
