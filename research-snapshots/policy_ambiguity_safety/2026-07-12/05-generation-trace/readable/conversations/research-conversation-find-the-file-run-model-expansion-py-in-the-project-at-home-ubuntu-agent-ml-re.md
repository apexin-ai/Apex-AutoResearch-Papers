# Research conversation: Find the file run_model_expansion.py in the project at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/polic

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7e21360add66fe7c.jsonl`
- **Structured JSON:** [`bb0765e4065e58cbcbfd.json`](../../sessions/bb/bb0765e4065e58cbcbfd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-21T08:40:56.310Z_

Find the file run_model_expansion.py in the project at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/. Search recursively. Report the full path and its contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b916ac82-3ef3-4f79-b8c5-a9085c242254",
  "agentId": "a7e21360add66fe7c",
  "type": "user",
  "uuid": "6124d5ec-feaa-440f-a370-7c0fba8348ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T08:40:58.320Z_

I'll search recursively for the `run_model_expansion.py` file in the project directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6124d5ec-feaa-440f-a370-7c0fba8348ee",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2PN2XXuPe9rfgNcF3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37f2d337-ad18-4840-be52-ba5eed761da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S8UxJCyxwWMTxqKx8WFgWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 53498,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 53498,
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

_source line 3 · 2026-05-21T08:40:58.549Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SUojWkuHbLpNEr5VGTpZNu`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety -name \"run_model_expansion.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f2d337-ad18-4840-be52-ba5eed761da8",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2PN2XXuPe9rfgNcF3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0d0b230-30d5-4f37-a2b0-77bfd6152054",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S8UxJCyxwWMTxqKx8WFgWV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 53498,
      "cache_read_input_tokens": 0,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 53498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 53498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 53498,
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

_source line 4 · 2026-05-21T08:40:58.771Z_

<details><summary>↩ Tool result · `toolu_01SUojWkuHbLpNEr5VGTpZNu`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/_project/intermediate/run_model_expansion.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_model_expansion.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0d0b230-30d5-4f37-a2b0-77bfd6152054",
  "isSidechain": true,
  "promptId": "b916ac82-3ef3-4f79-b8c5-a9085c242254",
  "agentId": "a7e21360add66fe7c",
  "type": "user",
  "uuid": "2ce9c488-426b-4811-8607-684234b7f5ff",
  "sourceToolAssistantUUID": "e0d0b230-30d5-4f37-a2b0-77bfd6152054",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T08:41:00.077Z_

Found two instances. Let me read both files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce9c488-426b-4811-8607-684234b7f5ff",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2ZroLVcUWpFCn5PFf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8608ce0e-c40a-430f-90c9-890d8cc14513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L3LgYgpEi1ewm6aDaEj7fR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 53498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1053,
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

_source line 6 · 2026-05-21T08:41:00.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NEgd2Eb1VzawN26F6KtQdr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_model_expansion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8608ce0e-c40a-430f-90c9-890d8cc14513",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2ZroLVcUWpFCn5PFf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c59d3b09-fd67-4870-9bfa-76fdb48511e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L3LgYgpEi1ewm6aDaEj7fR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 53498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1053,
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

_source line 7 · 2026-05-21T08:41:00.326Z_

<details><summary>↩ Tool result · `toolu_01NEgd2Eb1VzawN26F6KtQdr`</summary>

```text
1	#!/usr/bin/env python3
2	"""Model expansion experiment: replicate matched-pair study on new model families.
3	
4	Selected models (probed 2026-05-21):
5	  - google/gemini-2.5-flash  (Google family, tool calling confirmed)
6	  - meta-llama/llama-4-scout (Meta family, tool calling confirmed)
7	
8	Pipeline mirrors run_full_study.py: Phase 1 (episodes) → Phase 2 (judge) → analysis.
9	Judge: gpt-5.4 (consistent with Claude/Qwen3 experiments).
10	"""
11	
12	import argparse
13	import asyncio
14	import json
15	import os
16	import sys
17	import time
18	from pathlib import Path
19	
20	import numpy as np
21	import pandas as pd
22	from scipy import stats
23	
24	# -- Bootstrap API key before importing config --
25	sys.path.insert(0, "/home/ubuntu/agent-ml-research")
26	from core.crypto import load_secret
27	
28	key = load_secret(Path(
29	    "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
30	    "/config/secrets/policy_ambiguity_safety/openrouter_api_key.enc"
31	))
32	os.environ["OPENROUTER_API_KEY"] = key
33	
34	import config
35	import harness
36	import judge
37	import analyze
38	
39	# ---------------------------------------------------------------------------
40	# Register new models
41	# ---------------------------------------------------------------------------
42	
43	EXPANSION_MODELS = {
44	    "gemini-2.5-flash": {
45	        "model_id": "google/gemini-2.5-flash",
46	        "max_tokens": 4096,
47	        "api_key_env": config.API_KEY_ENV,
48	        "base_url": config.OPENROUTER_BASE_URL,
49	    },
50	    "llama-4-scout": {
51	        "model_id": "meta-llama/llama-4-scout",
52	        "max_tokens": 4096,
53	        "api_key_env": config.API_KEY_ENV,
54	        "base_url": config.OPENROUTER_BASE_URL,
55	    },
56	}
57	
58	JUDGE_MODEL = "gpt-5.4"
59	
60	for name, cfg in EXPANSION_MODELS.items():
61	    config.MODELS[name] = cfg
62	    config.CROSS_JUDGE_MAP[name] = JUDGE_MODEL
63	
64	# ---------------------------------------------------------------------------
65	# Paths
66	# ---------------------------------------------------------------------------
67	
68	BASE_DIR = config.ARTIFACTS_DIR / "model_expansion"
69	CLAUSES_PATH = config.ARTIFACTS_DIR / "_project" / "data" / "clause_templates_full.json"
70	ERRORS_FILE = BASE_DIR / "errors.jsonl"
71	
72	CONCURRENCY = 5
73	JUDGE_CONCURRENCY = 5
74	
75	# ---------------------------------------------------------------------------
76	# Phase 1: Episode Generation
77	# ---------------------------------------------------------------------------
78	
79	def _load_completed_episodes(episodes_file: Path) -> set[str]:
80	    completed = set()
81	    if episodes_file.exists():
82	        with open(episodes_file) as f:
83	            for line in f:
84	                if line.strip():
85	                    rec = json.loads(line)
86	                    completed.add(f"{rec['clause_id']}|{rec['condition']}")
87	    return completed
88	
89	
90	async def run_phase1(clauses: list[dict], model_name: str, resume: bool):
91	    model_dir = BASE_DIR / model_name
92	    model_dir.mkdir(parents=True, exist_ok=True)
93	    episodes_file = model_dir / "episodes.jsonl"
94	
95	    completed = _load_completed_episodes(episodes_file) if resume else set()
96	    tasks = []
97	    for clause in clauses:
98	        for condition in ("ambiguous", "unambiguous"):
99	            key = f"{clause['clause_id']}|{condition}"
100	            if key in completed:
101	                continue
102	            tasks.append((clause, condition))
103	
104	    if not tasks:
105	        print(f"[{model_name}] All {len(completed)} episodes complete — skipping Phase 1.")
106	        return
107	
108	    print(f"[{model_name}] Phase 1: {len(tasks)} episodes to run "
109	          f"(skipping {len(completed)}, concurrency={CONCURRENCY})")
110	
111	    semaphore = asyncio.Semaphore(CONCURRENCY)
112	    lock = asyncio.Lock()
113	    done = 0
114	    errors = 0
115	    t0 = time.time()
116	
117	    async def _run_one(clause, condition):
118	        nonlocal done, errors
119	        for attempt in range(3):
120	            async with semaphore:
121	                try:
122	                    result = await harness.run_episode(clause, condition, model_name)
123	                    async with lock:
124	                        with open(episodes_file, "a") as f:
125	                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
126	                        done += 1
127	                        if done % 100 == 0 or done == len(tasks):
128	                            elapsed = time.time() - t0
129	                            rate = done / elapsed * 60
130	                            print(f"  [{model_name}] {done}/{len(tasks)} "
131	                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
132	                    return
133	                except Exception as e:
134	                    if attempt < 2:
135	                        await asyncio.sleep(2 ** attempt)
136	                        continue
137	                    async with lock:
138	                        errors += 1
139	                        with open(ERRORS_FILE, "a") as f:
140	                            f.write(json.dumps({
141	                                "phase": 1, "model": model_name,
142	                                "clause_id": clause["clause_id"],
143	                                "condition": condition,
144	                                "error": str(e),
145	                                "timestamp": time.time(),
146	                            }, ensure_ascii=False) + "\n")
147	
148	    await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])
149	    elapsed = time.time() - t0
150	    print(f"  [{model_name}] Phase 1 done: {done} ok, {errors} errors ({elapsed:.0f}s)")
151	
152	
153	# ---------------------------------------------------------------------------
154	# Integrity check between phases
155	# ---------------------------------------------------------------------------
156	
157	def check_integrity(model_name: str, n_clauses: int) -> tuple[int, int, int]:
158	    episodes_file = BASE_DIR / model_name / "episodes.jsonl"
159	    if not episodes_file.exists():
160	        return 0, 0, 0
161	    total = 0
162	    ok = 0
163	    error_count = 0
164	    with open(episodes_file) as f:
165	        for line in f:
166	            if not line.strip():
167	                continue
168	            total += 1
169	            rec = json.loads(line)
170	            status = harness.validate_episode(rec)
171	            if status == "ok":
172	                ok += 1
173	            else:
174	                error_count += 1
175	    expected = n_clauses * 2
176	    print(f"  [{model_name}] Integrity: {total}/{expected} episodes "
177	          f"({ok} ok, {error_count} errors)")
178	    return total, ok, error_count
179	
180	
181	# ---------------------------------------------------------------------------
182	# Phase 2: Judge Evaluation
183	# ---------------------------------------------------------------------------
184	
185	def _load_judged_ids(judgments_file: Path) -> set[str]:
186	    judged = set()
187	    if judgments_file.exists():
188	        with open(judgments_file) as f:
189	            for line in f:
190	                if line.strip():
191	                    judged.add(json.loads(line)["episode_id"])
192	    return judged
193	
194	
195	async def run_phase2(clauses: list[dict], model_name: str, resume: bool):
196	    model_dir = BASE_DIR / model_name
197	    episodes_file = model_dir / "episodes.jsonl"
198	    if not episodes_file.exists():
199	        print(f"[{model_name}] No episodes — run Phase 1 first.")
200	        return
201	
202	    episodes = []
203	    with open(episodes_file) as f:
204	        for line in f:
205	            if line.strip():
206	                episodes.append(json.loads(line))
207	    if not episodes:
208	        print(f"[{model_name}] No episodes found.")
209	        return
210	
211	    clause_index = judge.build_clause_index(clauses)
212	    judgments_file = model_dir / "judgments.jsonl"
213	    judged_ids = _load_judged_ids(judgments_file) if resume else set()
214	    pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]
215	
216	    if not pending:
217	        print(f"[{model_name}] All {len(episodes)} episodes already judged — skipping Phase 2.")
218	        return
219	
220	    actual_judge = config.CROSS_JUDGE_MAP[model_name]
221	    print(f"[{model_name}] Phase 2: judging {len(pending)} episodes "
222	          f"(judge={actual_judge}, concurrency={JUDGE_CONCURRENCY})")
223	
224	    semaphore = asyncio.Semaphore(JUDGE_CONCURRENCY)
225	    lock = asyncio.Lock()
226	    done = 0
227	    errors = 0
228	    t0 = time.time()
229	
230	    async def _judge_one(episode):
231	        nonlocal done, errors
232	        for attempt in range(3):
233	            async with semaphore:
234	                try:
235	                    result = await judge.judge_episode(episode, clause_index)
236	                    async with lock:
237	                        with open(judgments_file, "a") as f:
238	                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
239	                        done += 1
240	                        if done % 100 == 0 or done == len(pending):
241	                            elapsed = time.time() - t0
242	                            rate = done / elapsed * 60
243	                            print(f"  [{model_name}] {done}/{len(pending)} judged "
244	                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
245	                    return
246	                except Exception as e:
247	                    if attempt < 2:
248	                        await asyncio.sleep(2 ** attempt)
249	                        continue
250	                    async with lock:
251	                        errors += 1
252	                        with open(ERRORS_FILE, "a") as f:
253	                            f.write(json.dumps({
254	                                "phase": 2, "model": model_name,
255	                                "episode_id": episode.get("episode_id", "?"),
256	                                "error": str(e),
257	                                "timestamp": time.time(),
258	                            }, ensure_ascii=False) + "\n")
259	
260	    await asyncio.gather(*[_judge_one(ep) for ep in pending])
261	    elapsed = time.time() - t0
262	    print(f"  [{model_name}] Phase 2 done: {done} judged, {errors} errors ({elapsed:.0f}s)")
263	
264	
265	# ---------------------------------------------------------------------------
266	# Phase 3: Analysis
267	# ---------------------------------------------------------------------------
268	
269	def run_analysis(model_name: str) -> dict | None:
270	    model_dir = BASE_DIR / model_name
271	    judgments_file = model_dir / "judgments.jsonl"
272	    if not judgments_file.exists():
273	        print(f"[{model_name}] No judgments — run Phase 2 first.")
274	        return None
275	
276	    records = []
277	    with open(judgments_file) as f:
278	        for line in f:
279	            if not line.strip():
280	                continue
281	            rec = json.loads(line)
282	            records.append({
283	                "episode_id": rec["episode_id"],
284	                "clause_id": rec["clause_id"],
285	                "ambiguity_type": rec["ambiguity_type"],
286	                "condition": rec["condition"],
287	                "model": rec["model"],
288	                "violation_level": rec["judgment"]["violation_level"],
289	                "confidence": rec["judgment"]["confidence"],
290	                "judge_model": rec["judge_model"],
291	            })
292	
293	    df = pd.DataFrame(records)
294	    if df.empty:
295	        print(f"[{model_name}] Empty judgments.")
296	        return None
297	
298	    level_order = pd.CategoricalDtype(categories=config.VIOLATION_LEVELS, ordered=True)
299	    df["violation_level"] = df["violation_level"].astype(level_order)
300	    df["violated"] = analyze.binarize_violations(df)
301	
302	    # Overall rates
303	    amb = df[df["condition"] == "ambiguous"]
304	    unamb = df[df["condition"] == "unambiguous"]
305	    amb_rate = float(amb["violated"].mean()) if len(amb) > 0 else None
306	    unamb_rate = float(unamb["violated"].mean()) if len(unamb) > 0 else None
307	
308	    # Fisher exact for overall
309	    ct = pd.crosstab(df["condition"], df["violated"])
310	    if ct.shape == (2, 2):
311	        odds_ratio_result = stats.fisher_exact(ct.values)
312	        or_val = float(odds_ratio_result[0])
313	        p_val = float(odds_ratio_result[1])
314	    else:
315	        or_val = None
316	        p_val = None
317	
318	    delta_pp = (amb_rate - unamb_rate) if (amb_rate is not None and unamb_rate is not None) else None
319	
320	    # Per-type rates
321	    per_type = {}
322	    type_amb_rates = {}
323	    for atype in config.AMBIGUITY_TYPES:
324	        tdf = df[df["ambiguity_type"] == atype]
325	        if tdf.empty:
326	            continue
327	        t_amb = tdf[tdf["condition"] == "ambiguous"]
328	        t_unamb = tdf[tdf["condition"] == "unambiguous"]
329	        a_r = float(t_amb["violated"].mean()) if len(t_amb) > 0 else None
330	        u_r = float(t_unamb["violated"].mean()) if len(t_unamb) > 0 else None
331	        d = (a_r - u_r) if (a_r is not None and u_r is not None) else None
332	        per_type[atype] = {
333	            "ambiguous_rate": a_r,
334	            "unambiguous_rate": u_r,
335	            "delta_pp": d,
336	        }
337	        if a_r is not None:
338	            type_amb_rates[atype] = a_r
339	
340	    # C1: does binary ambiguity effect replicate?
341	    c1_replicates = (p_val is not None and p_val < 0.05 and
342	                     delta_pp is not None and delta_pp > 0)
343	
344	    # C2: rank correlation with reference ordering
345	    reference_rank = ["scopal", "lexical", "coreferential",
346	                      "incompleteness", "conditional_precedence", "authorization_scope"]
347	    if len(type_amb_rates) >= 4:
348	        ref_ranks = []
349	        new_ranks = []
350	        sorted_new = sorted(type_amb_rates.items(), key=lambda x: -x[1])
351	        new_rank_map = {t: i for i, (t, _) in enumerate(sorted_new)}
352	        for i, t in enumerate(reference_rank):
353	            if t in new_rank_map:
354	                ref_ranks.append(i)
355	                new_ranks.append(new_rank_map[t])
356	        if len(ref_ranks) >= 4:
357	            rho, rho_p = stats.spearmanr(ref_ranks, new_ranks)
358	            c2_rank_corr = float(rho)
359	        else:
360	            c2_rank_corr = None
361	    else:
362	        c2_rank_corr = None
363	
364	    model_cfg = config.MODELS[model_name]
365	    result = {
366	        "model": model_name,
367	        "model_id": model_cfg["model_id"],
368	        "n_episodes": len(df),
369	        "n_ambiguous": len(amb),
370	        "n_unambiguous": len(unamb),
371	        "judge_model": JUDGE_MODEL,
372	        "overall": {
373	            "ambiguous_rate": amb_rate,
374	            "unambiguous_rate": unamb_rate,
375	            "delta_pp": delta_pp,
376	            "or": or_val,
377	            "p_value": p_val,
378	        },
379	        "per_type": per_type,
380	        "c1_replicates": c1_replicates,
381	        "c2_rank_correlation": c2_rank_corr,
382	        "type_ranking": sorted(type_amb_rates.keys(), key=lambda t: -type_amb_rates[t]),
383	    }
384	
385	    analysis_file = model_dir / "analysis.json"
386	    with open(analysis_file, "w") as f:
387	        json.dump(result, f, indent=2, default=str)
388	
389	    _print_analysis(result)
390	    return result
391	
392	
393	def _print_analysis(r: dict):
394	    print(f"\n{'=' * 60}")
395	    print(f"  Model: {r['model']} ({r['model_id']})")
396	    print(f"  Episodes: {r['n_episodes']} ({r['n_ambiguous']} amb + {r['n_unambiguous']} unamb)")
397	    print(f"  Judge: {r['judge_model']}")
398	    print(f"{'=' * 60}")
399	
400	    o = r["overall"]
401	    print(f"\n  Overall: amb={o['ambiguous_rate']:.1%}  unamb={o['unambiguous_rate']:.1%}"
402	          f"  delta={o['delta_pp']:+.1%}  OR={o['or']:.2f}  p={o['p_value']:.4f}")
403	
404	    print(f"\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'Delta':>7}")
405	    print(f"  {'-'*25} {'-'*7} {'-'*7} {'-'*7}")
406	    for atype in config.AMBIGUITY_TYPES:
407	        if atype in r["per_type"]:
408	            t = r["per_type"][atype]
409	            a = f"{t['ambiguous_rate']:.1%}" if t['ambiguous_rate'] is not None else "N/A"
410	            u = f"{t['unambiguous_rate']:.1%}" if t['unambiguous_rate'] is not None else "N/A"
411	            d = f"{t['delta_pp']:+.1%}" if t['delta_pp'] is not None else "N/A"
412	            print(f"  {atype:<25} {a:>7} {u:>7} {d:>7}")
413	
414	    c1 = "YES" if r["c1_replicates"] else "NO"
415	    c2 = f"{r['c2_rank_correlation']:.3f}" if r['c2_rank_correlation'] is not None else "N/A"
416	    print(f"\n  C1 (binary effect replicates): {c1}")
417	    print(f"  C2 (type rank correlation):    {c2}")
418	    print(f"  Type ranking: {' > '.join(r['type_ranking'])}")
419	    print()
420	
421	
422	# ---------------------------------------------------------------------------
423	# CLI
424	# ---------------------------------------------------------------------------
425	
426	def main():
427	    parser = argparse.ArgumentParser(description="Model expansion experiment.")
428	    parser.add_argument("--phase", type=int, choices=[1, 2, 3],
429	                        help="Run a specific phase.")
430	    parser.add_argument("--all", action="store_true",
431	                        help="Run all phases sequentially.")
432	    parser.add_argument("--models", default=",".join(EXPANSION_MODELS.keys()),
433	                        help="Comma-separated model names.")
434	    parser.add_argument("--resume", action="store_true", default=True)
435	    parser.add_argument("--no-resume", action="store_false", dest="resume")
436	    args = parser.parse_args()
437	
438	    if not args.phase and not args.all:
439	        args.all = True
440	
441	    models = [m.strip() for m in args.models.split(",")]
442	    clauses = harness.load_clauses(str(CLAUSES_PATH))
443	    print(f"Loaded {len(clauses)} clauses from {CLAUSES_PATH.name}")
444	
445	    phases = [1, 2, 3] if args.all else [args.phase]
446	
447	    for model_name in models:
448	        if model_name not in config.MODELS:
449	            print(f"Error: unknown model '{model_name}'")
450	            sys.exit(1)
451	
452	    for phase in phases:
453	        print(f"\n{'=' * 40} Phase {phase} {'=' * 40}")
454	        for model_name in models:
455	            if phase == 1:
456	                asyncio.run(run_phase1(clauses, model_name, args.resume))
457	            elif phase == 2:
458	                total, ok, errs = check_integrity(model_name, len(clauses))
459	                if ok < len(clauses):
460	                    print(f"  [{model_name}] WARNING: only {ok}/{len(clauses)*2} "
461	                          f"valid episodes. Proceeding with available data.")
462	                asyncio.run(run_phase2(clauses, model_name, args.resume))
463	            elif phase == 3:
464	                run_analysis(model_name)
465	
466	
467	if __name__ == "__main__":
468	    main()
469	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c59d3b09-fd67-4870-9bfa-76fdb48511e0",
  "isSidechain": true,
  "promptId": "b916ac82-3ef3-4f79-b8c5-a9085c242254",
  "agentId": "a7e21360add66fe7c",
  "type": "user",
  "uuid": "29201a01-4566-47b0-a57b-f3021ac36ef0",
  "sourceToolAssistantUUID": "c59d3b09-fd67-4870-9bfa-76fdb48511e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T08:41:00.476Z_

<details open><summary>🔧 Tool call — Read · `toolu_01315KK4YYMxSwpi8VGd86tr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/_project/intermediate/run_model_expansion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29201a01-4566-47b0-a57b-f3021ac36ef0",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2ZroLVcUWpFCn5PFf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac88e13c-4302-448c-a3d2-960d211c545e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L3LgYgpEi1ewm6aDaEj7fR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 53498,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 184,
          "cache_read_input_tokens": 53498,
          "cache_creation_input_tokens": 1053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1053,
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

_source line 9 · 2026-05-21T08:41:00.483Z_

<details><summary>↩ Tool result · `toolu_01315KK4YYMxSwpi8VGd86tr`</summary>

```text
1	#!/usr/bin/env python3
2	"""Model expansion experiment: replicate matched-pair study on new model families.
3	
4	Selected models (probed 2026-05-21):
5	  - google/gemini-2.5-flash  (Google family, tool calling confirmed)
6	  - meta-llama/llama-4-scout (Meta family, tool calling confirmed)
7	
8	Pipeline mirrors run_full_study.py: Phase 1 (episodes) → Phase 2 (judge) → analysis.
9	Judge: gpt-5.4 (consistent with Claude/Qwen3 experiments).
10	"""
11	
12	import argparse
13	import asyncio
14	import json
15	import os
16	import sys
17	import time
18	from pathlib import Path
19	
20	import numpy as np
21	import pandas as pd
22	from scipy import stats
23	
24	# -- Bootstrap API key before importing config --
25	sys.path.insert(0, "/home/ubuntu/agent-ml-research")
26	from core.crypto import load_secret
27	
28	key = load_secret(Path(
29	    "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
30	    "/config/secrets/policy_ambiguity_safety/openrouter_api_key.enc"
31	))
32	os.environ["OPENROUTER_API_KEY"] = key
33	
34	import config
35	import harness
36	import judge
37	import analyze
38	
39	# ---------------------------------------------------------------------------
40	# Register new models
41	# ---------------------------------------------------------------------------
42	
43	EXPANSION_MODELS = {
44	    "gemini-2.5-flash": {
45	        "model_id": "google/gemini-2.5-flash",
46	        "max_tokens": 4096,
47	        "api_key_env": config.API_KEY_ENV,
48	        "base_url": config.OPENROUTER_BASE_URL,
49	    },
50	    "llama-4-scout": {
51	        "model_id": "meta-llama/llama-4-scout",
52	        "max_tokens": 4096,
53	        "api_key_env": config.API_KEY_ENV,
54	        "base_url": config.OPENROUTER_BASE_URL,
55	    },
56	}
57	
58	JUDGE_MODEL = "gpt-5.4"
59	
60	for name, cfg in EXPANSION_MODELS.items():
61	    config.MODELS[name] = cfg
62	    config.CROSS_JUDGE_MAP[name] = JUDGE_MODEL
63	
64	# ---------------------------------------------------------------------------
65	# Paths
66	# ---------------------------------------------------------------------------
67	
68	BASE_DIR = config.ARTIFACTS_DIR / "model_expansion"
69	CLAUSES_PATH = config.ARTIFACTS_DIR / "_project" / "data" / "clause_templates_full.json"
70	ERRORS_FILE = BASE_DIR / "errors.jsonl"
71	
72	CONCURRENCY = 5
73	JUDGE_CONCURRENCY = 5
74	
75	# ---------------------------------------------------------------------------
76	# Phase 1: Episode Generation
77	# ---------------------------------------------------------------------------
78	
79	def _load_completed_episodes(episodes_file: Path) -> set[str]:
80	    completed = set()
81	    if episodes_file.exists():
82	        with open(episodes_file) as f:
83	            for line in f:
84	                if line.strip():
85	                    rec = json.loads(line)
86	                    completed.add(f"{rec['clause_id']}|{rec['condition']}")
87	    return completed
88	
89	
90	async def run_phase1(clauses: list[dict], model_name: str, resume: bool):
91	    model_dir = BASE_DIR / model_name
92	    model_dir.mkdir(parents=True, exist_ok=True)
93	    episodes_file = model_dir / "episodes.jsonl"
94	
95	    completed = _load_completed_episodes(episodes_file) if resume else set()
96	    tasks = []
97	    for clause in clauses:
98	        for condition in ("ambiguous", "unambiguous"):
99	            key = f"{clause['clause_id']}|{condition}"
100	            if key in completed:
101	                continue
102	            tasks.append((clause, condition))
103	
104	    if not tasks:
105	        print(f"[{model_name}] All {len(completed)} episodes complete — skipping Phase 1.")
106	        return
107	
108	    print(f"[{model_name}] Phase 1: {len(tasks)} episodes to run "
109	          f"(skipping {len(completed)}, concurrency={CONCURRENCY})")
110	
111	    semaphore = asyncio.Semaphore(CONCURRENCY)
112	    lock = asyncio.Lock()
113	    done = 0
114	    errors = 0
115	    t0 = time.time()
116	
117	    async def _run_one(clause, condition):
118	        nonlocal done, errors
119	        for attempt in range(3):
120	            async with semaphore:
121	                try:
122	                    result = await harness.run_episode(clause, condition, model_name)
123	                    async with lock:
124	                        with open(episodes_file, "a") as f:
125	                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
126	                        done += 1
127	                        if done % 100 == 0 or done == len(tasks):
128	                            elapsed = time.time() - t0
129	                            rate = done / elapsed * 60
130	                            print(f"  [{model_name}] {done}/{len(tasks)} "
131	                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
132	                    return
133	                except Exception as e:
134	                    if attempt < 2:
135	                        await asyncio.sleep(2 ** attempt)
136	                        continue
137	                    async with lock:
138	                        errors += 1
139	                        with open(ERRORS_FILE, "a") as f:
140	                            f.write(json.dumps({
141	                                "phase": 1, "model": model_name,
142	                                "clause_id": clause["clause_id"],
143	                                "condition": condition,
144	                                "error": str(e),
145	                                "timestamp": time.time(),
146	                            }, ensure_ascii=False) + "\n")
147	
148	    await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])
149	    elapsed = time.time() - t0
150	    print(f"  [{model_name}] Phase 1 done: {done} ok, {errors} errors ({elapsed:.0f}s)")
151	
152	
153	# ---------------------------------------------------------------------------
154	# Integrity check between phases
155	# ---------------------------------------------------------------------------
156	
157	def check_integrity(model_name: str, n_clauses: int) -> tuple[int, int, int]:
158	    episodes_file = BASE_DIR / model_name / "episodes.jsonl"
159	    if not episodes_file.exists():
160	        return 0, 0, 0
161	    total = 0
162	    ok = 0
163	    error_count = 0
164	    with open(episodes_file) as f:
165	        for line in f:
166	            if not line.strip():
167	                continue
168	            total += 1
169	            rec = json.loads(line)
170	            status = harness.validate_episode(rec)
171	            if status == "ok":
172	                ok += 1
173	            else:
174	                error_count += 1
175	    expected = n_clauses * 2
176	    print(f"  [{model_name}] Integrity: {total}/{expected} episodes "
177	          f"({ok} ok, {error_count} errors)")
178	    return total, ok, error_count
179	
180	
181	# ---------------------------------------------------------------------------
182	# Phase 2: Judge Evaluation
183	# ---------------------------------------------------------------------------
184	
185	def _load_judged_ids(judgments_file: Path) -> set[str]:
186	    judged = set()
187	    if judgments_file.exists():
188	        with open(judgments_file) as f:
189	            for line in f:
190	                if line.strip():
191	                    judged.add(json.loads(line)["episode_id"])
192	    return judged
193	
194	
195	async def run_phase2(clauses: list[dict], model_name: str, resume: bool):
196	    model_dir = BASE_DIR / model_name
197	    episodes_file = model_dir / "episodes.jsonl"
198	    if not episodes_file.exists():
199	        print(f"[{model_name}] No episodes — run Phase 1 first.")
200	        return
201	
202	    episodes = []
203	    with open(episodes_file) as f:
204	        for line in f:
205	            if line.strip():
206	                episodes.append(json.loads(line))
207	    if not episodes:
208	        print(f"[{model_name}] No episodes found.")
209	        return
210	
211	    clause_index = judge.build_clause_index(clauses)
212	    judgments_file = model_dir / "judgments.jsonl"
213	    judged_ids = _load_judged_ids(judgments_file) if resume else set()
214	    pending = [ep for ep in episodes if ep["episode_id"] not in judged_ids]
215	
216	    if not pending:
217	        print(f"[{model_name}] All {len(episodes)} episodes already judged — skipping Phase 2.")
218	        return
219	
220	    actual_judge = config.CROSS_JUDGE_MAP[model_name]
221	    print(f"[{model_name}] Phase 2: judging {len(pending)} episodes "
222	          f"(judge={actual_judge}, concurrency={JUDGE_CONCURRENCY})")
223	
224	    semaphore = asyncio.Semaphore(JUDGE_CONCURRENCY)
225	    lock = asyncio.Lock()
226	    done = 0
227	    errors = 0
228	    t0 = time.time()
229	
230	    async def _judge_one(episode):
231	        nonlocal done, errors
232	        for attempt in range(3):
233	            async with semaphore:
234	                try:
235	                    result = await judge.judge_episode(episode, clause_index)
236	                    async with lock:
237	                        with open(judgments_file, "a") as f:
238	                            f.write(json.dumps(result, ensure_ascii=False) + "\n")
239	                        done += 1
240	                        if done % 100 == 0 or done == len(pending):
241	                            elapsed = time.time() - t0
242	                            rate = done / elapsed * 60
243	                            print(f"  [{model_name}] {done}/{len(pending)} judged "
244	                                  f"({elapsed:.0f}s, {rate:.1f}/min)")
245	                    return
246	                except Exception as e:
247	                    if attempt < 2:
248	                        await asyncio.sleep(2 ** attempt)
249	                        continue
250	                    async with lock:
251	                        errors += 1
252	                        with open(ERRORS_FILE, "a") as f:
253	                            f.write(json.dumps({
254	                                "phase": 2, "model": model_name,
255	                                "episode_id": episode.get("episode_id", "?"),
256	                                "error": str(e),
257	                                "timestamp": time.time(),
258	                            }, ensure_ascii=False) + "\n")
259	
260	    await asyncio.gather(*[_judge_one(ep) for ep in pending])
261	    elapsed = time.time() - t0
262	    print(f"  [{model_name}] Phase 2 done: {done} judged, {errors} errors ({elapsed:.0f}s)")
263	
264	
265	# ---------------------------------------------------------------------------
266	# Phase 3: Analysis
267	# ---------------------------------------------------------------------------
268	
269	def run_analysis(model_name: str) -> dict | None:
270	    model_dir = BASE_DIR / model_name
271	    judgments_file = model_dir / "judgments.jsonl"
272	    if not judgments_file.exists():
273	        print(f"[{model_name}] No judgments — run Phase 2 first.")
274	        return None
275	
276	    records = []
277	    with open(judgments_file) as f:
278	        for line in f:
279	            if not line.strip():
280	                continue
281	            rec = json.loads(line)
282	            records.append({
283	                "episode_id": rec["episode_id"],
284	                "clause_id": rec["clause_id"],
285	                "ambiguity_type": rec["ambiguity_type"],
286	                "condition": rec["condition"],
287	                "model": rec["model"],
288	                "violation_level": rec["judgment"]["violation_level"],
289	                "confidence": rec["judgment"]["confidence"],
290	                "judge_model": rec["judge_model"],
291	            })
292	
293	    df = pd.DataFrame(records)
294	    if df.empty:
295	        print(f"[{model_name}] Empty judgments.")
296	        return None
297	
298	    level_order = pd.CategoricalDtype(categories=config.VIOLATION_LEVELS, ordered=True)
299	    df["violation_level"] = df["violation_level"].astype(level_order)
300	    df["violated"] = analyze.binarize_violations(df)
301	
302	    # Overall rates
303	    amb = df[df["condition"] == "ambiguous"]
304	    unamb = df[df["condition"] == "unambiguous"]
305	    amb_rate = float(amb["violated"].mean()) if len(amb) > 0 else None
306	    unamb_rate = float(unamb["violated"].mean()) if len(unamb) > 0 else None
307	
308	    # Fisher exact for overall
309	    ct = pd.crosstab(df["condition"], df["violated"])
310	    if ct.shape == (2, 2):
311	        odds_ratio_result = stats.fisher_exact(ct.values)
312	        or_val = float(odds_ratio_result[0])
313	        p_val = float(odds_ratio_result[1])
314	    else:
315	        or_val = None
316	        p_val = None
317	
318	    delta_pp = (amb_rate - unamb_rate) if (amb_rate is not None and unamb_rate is not None) else None
319	
320	    # Per-type rates
321	    per_type = {}
322	    type_amb_rates = {}
323	    for atype in config.AMBIGUITY_TYPES:
324	        tdf = df[df["ambiguity_type"] == atype]
325	        if tdf.empty:
326	            continue
327	        t_amb = tdf[tdf["condition"] == "ambiguous"]
328	        t_unamb = tdf[tdf["condition"] == "unambiguous"]
329	        a_r = float(t_amb["violated"].mean()) if len(t_amb) > 0 else None
330	        u_r = float(t_unamb["violated"].mean()) if len(t_unamb) > 0 else None
331	        d = (a_r - u_r) if (a_r is not None and u_r is not None) else None
332	        per_type[atype] = {
333	            "ambiguous_rate": a_r,
334	            "unambiguous_rate": u_r,
335	            "delta_pp": d,
336	        }
337	        if a_r is not None:
338	            type_amb_rates[atype] = a_r
339	
340	    # C1: does binary ambiguity effect replicate?
341	    c1_replicates = (p_val is not None and p_val < 0.05 and
342	                     delta_pp is not None and delta_pp > 0)
343	
344	    # C2: rank correlation with reference ordering
345	    reference_rank = ["scopal", "lexical", "coreferential",
346	                      "incompleteness", "conditional_precedence", "authorization_scope"]
347	    if len(type_amb_rates) >= 4:
348	        ref_ranks = []
349	        new_ranks = []
350	        sorted_new = sorted(type_amb_rates.items(), key=lambda x: -x[1])
351	        new_rank_map = {t: i for i, (t, _) in enumerate(sorted_new)}
352	        for i, t in enumerate(reference_rank):
353	            if t in new_rank_map:
354	                ref_ranks.append(i)
355	                new_ranks.append(new_rank_map[t])
356	        if len(ref_ranks) >= 4:
357	            rho, rho_p = stats.spearmanr(ref_ranks, new_ranks)
358	            c2_rank_corr = float(rho)
359	        else:
360	            c2_rank_corr = None
361	    else:
362	        c2_rank_corr = None
363	
364	    model_cfg = config.MODELS[model_name]
365	    result = {
366	        "model": model_name,
367	        "model_id": model_cfg["model_id"],
368	        "n_episodes": len(df),
369	        "n_ambiguous": len(amb),
370	        "n_unambiguous": len(unamb),
371	        "judge_model": JUDGE_MODEL,
372	        "overall": {
373	            "ambiguous_rate": amb_rate,
374	            "unambiguous_rate": unamb_rate,
375	            "delta_pp": delta_pp,
376	            "or": or_val,
377	            "p_value": p_val,
378	        },
379	        "per_type": per_type,
380	        "c1_replicates": c1_replicates,
381	        "c2_rank_correlation": c2_rank_corr,
382	        "type_ranking": sorted(type_amb_rates.keys(), key=lambda t: -type_amb_rates[t]),
383	    }
384	
385	    analysis_file = model_dir / "analysis.json"
386	    with open(analysis_file, "w") as f:
387	        json.dump(result, f, indent=2, default=str)
388	
389	    _print_analysis(result)
390	    return result
391	
392	
393	def _print_analysis(r: dict):
394	    print(f"\n{'=' * 60}")
395	    print(f"  Model: {r['model']} ({r['model_id']})")
396	    print(f"  Episodes: {r['n_episodes']} ({r['n_ambiguous']} amb + {r['n_unambiguous']} unamb)")
397	    print(f"  Judge: {r['judge_model']}")
398	    print(f"{'=' * 60}")
399	
400	    o = r["overall"]
401	    print(f"\n  Overall: amb={o['ambiguous_rate']:.1%}  unamb={o['unambiguous_rate']:.1%}"
402	          f"  delta={o['delta_pp']:+.1%}  OR={o['or']:.2f}  p={o['p_value']:.4f}")
403	
404	    print(f"\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'Delta':>7}")
405	    print(f"  {'-'*25} {'-'*7} {'-'*7} {'-'*7}")
406	    for atype in config.AMBIGUITY_TYPES:
407	        if atype in r["per_type"]:
408	            t = r["per_type"][atype]
409	            a = f"{t['ambiguous_rate']:.1%}" if t['ambiguous_rate'] is not None else "N/A"
410	            u = f"{t['unambiguous_rate']:.1%}" if t['unambiguous_rate'] is not None else "N/A"
411	            d = f"{t['delta_pp']:+.1%}" if t['delta_pp'] is not None else "N/A"
412	            print(f"  {atype:<25} {a:>7} {u:>7} {d:>7}")
413	
414	    c1 = "YES" if r["c1_replicates"] else "NO"
415	    c2 = f"{r['c2_rank_correlation']:.3f}" if r['c2_rank_correlation'] is not None else "N/A"
416	    print(f"\n  C1 (binary effect replicates): {c1}")
417	    print(f"  C2 (type rank correlation):    {c2}")
418	    print(f"  Type ranking: {' > '.join(r['type_ranking'])}")
419	    print()
420	
421	
422	# ---------------------------------------------------------------------------
423	# CLI
424	# ---------------------------------------------------------------------------
425	
426	def main():
427	    parser = argparse.ArgumentParser(description="Model expansion experiment.")
428	    parser.add_argument("--phase", type=int, choices=[1, 2, 3],
429	                        help="Run a specific phase.")
430	    parser.add_argument("--all", action="store_true",
431	                        help="Run all phases sequentially.")
432	    parser.add_argument("--models", default=",".join(EXPANSION_MODELS.keys()),
433	                        help="Comma-separated model names.")
434	    parser.add_argument("--resume", action="store_true", default=True)
435	    parser.add_argument("--no-resume", action="store_false", dest="resume")
436	    args = parser.parse_args()
437	
438	    if not args.phase and not args.all:
439	        args.all = True
440	
441	    models = [m.strip() for m in args.models.split(",")]
442	    clauses = harness.load_clauses(str(CLAUSES_PATH))
443	    print(f"Loaded {len(clauses)} clauses from {CLAUSES_PATH.name}")
444	
445	    phases = [1, 2, 3] if args.all else [args.phase]
446	
447	    for model_name in models:
448	        if model_name not in config.MODELS:
449	            print(f"Error: unknown model '{model_name}'")
450	            sys.exit(1)
451	
452	    for phase in phases:
453	        print(f"\n{'=' * 40} Phase {phase} {'=' * 40}")
454	        for model_name in models:
455	            if phase == 1:
456	                asyncio.run(run_phase1(clauses, model_name, args.resume))
457	            elif phase == 2:
458	                total, ok, errs = check_integrity(model_name, len(clauses))
459	                if ok < len(clauses):
460	                    print(f"  [{model_name}] WARNING: only {ok}/{len(clauses)*2} "
461	                          f"valid episodes. Proceeding with available data.")
462	                asyncio.run(run_phase2(clauses, model_name, args.resume))
463	            elif phase == 3:
464	                run_analysis(model_name)
465	
466	
467	if __name__ == "__main__":
468	    main()
469	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac88e13c-4302-448c-a3d2-960d211c545e",
  "isSidechain": true,
  "promptId": "b916ac82-3ef3-4f79-b8c5-a9085c242254",
  "agentId": "a7e21360add66fe7c",
  "type": "user",
  "uuid": "a73d3aa0-723e-4d40-a183-6d5790e8c960",
  "sourceToolAssistantUUID": "ac88e13c-4302-448c-a3d2-960d211c545e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T08:41:06.652Z_

The file appears in two locations (likely one is a copy or symlink). Both versions are identical. Here are the details:

**Full paths:**
1. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_model_expansion.py`
2. `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/_project/intermediate/run_model_expansion.py`

**File contents (469 lines):**

The script implements a model expansion experiment that replicates a matched-pair study on new model families (Gemini-2.5-flash and Llama-4-scout). It follows a three-phase pipeline:

1. **Phase 1 (Episode Generation)**: Runs simulated episodes for test clauses under ambiguous/unambiguous conditions using the specified models via OpenRouter API.

2. **Phase 2 (Judge Evaluation)**: Evaluates generated episodes using GPT-5.4 as judge, computing violation levels and confidence scores.

3. **Phase 3 (Analysis)**: Computes violation rates, Fisher exact test for binary effect, Spearman rank correlation for ambiguity types, and two core claims (C1: binary effect replicates, C2: type ranking correlation).

Key components:
- Loads clauses from `clause_templates_full.json`
- Manages concurrency (5 concurrent tasks per phase)
- Supports resumable runs with progress tracking
- Handles errors with exponential backoff (3 attempts max)
- Outputs JSONL files for episodes, judgments, and consolidated analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a73d3aa0-723e-4d40-a183-6d5790e8c960",
  "isSidechain": true,
  "agentId": "a7e21360add66fe7c",
  "requestId": "req_011CbFR2hJ2ZoSTMR8xPXaYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da49ff14-33f7-4945-a043-1dcb3e14f606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/agent_241139a3",
  "sessionId": "0516152c-93ba-4bea-8801-2ab4b7412013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "tender-gathering-crown",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Pc1TN2ZkGxHBpk7BXrkRSq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12822,
      "cache_read_input_tokens": 54551,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 399,
          "cache_read_input_tokens": 54551,
          "cache_creation_input_tokens": 12822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12822,
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
