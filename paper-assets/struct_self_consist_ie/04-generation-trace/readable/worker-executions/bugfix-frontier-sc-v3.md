# bugfix frontier sc v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_bugfix_frontier_sc_v3_20260520T220547.log`
- **Structured JSON:** [`a6b1674ff9a8332e05c6.json`](../../sessions/a6/a6b1674ff9a8332e05c6.json)

## Before a recorded user message

51 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "b10d73b3-b854-4da4-a079-fa87ec7583b3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779328200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6a8e0b9f-5459-4d5b-bfbb-3fd8672a9774",
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Fix 3 bugs in `run_frontier_sc.py`
2. Kill old process if alive
3. Run smoke test
4. Run full experiment
5. Register experiment

Let me start by reading the code and checking the process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "bdc9aed6-4b93-4b3c-9866-ff3f1e831d73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

先读代码并检查旧进程状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "d4934ccf-1364-4202-8a3f-c8815779e02c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — Read · `toolu_01JdpGjR929mF65HXb1wmNmd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "4a73c293-890f-406d-b9be-f6fe672b2808",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

_source line 7 · 2026-05-20T22:06:01.599Z_

<details><summary>↩ Tool result · `toolu_01JdpGjR929mF65HXb1wmNmd`</summary>

```text
1	#!/usr/bin/env python3
2	"""Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).
3	
4	Tests whether the correlation-selection gap in structured self-consistency
5	persists with frontier models (GPT-5.5, Claude Opus 4.6), validating it
6	as a fundamental limitation rather than a capability issue.
7	
8	CPU-only — all computation is via API calls through OpenRouter.
9	
10	Usage:
11	    export OPENROUTER_API_KEY="[REDACTED]"
12	    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl
13	    python run_frontier_sc.py --from-hf  # load from HuggingFace
14	"""
15	
16	from __future__ import annotations
17	
18	import argparse
19	import json
20	import logging
21	import os
22	import random
23	import sys
24	import time
25	from collections import defaultdict
26	from pathlib import Path
27	
28	import numpy as np
29	from scipy.stats import spearmanr
30	
31	# ---------------------------------------------------------------------------
32	# Configuration
33	# ---------------------------------------------------------------------------
34	
35	MODELS = {
36	    "gpt-5.5": "openai/gpt-5.5",
37	    "claude-opus-4.6": "anthropic/claude-opus-4.6",
38	}
39	
40	API_BASE_URL = "http://47.94.22.126/v1"
41	
42	ENTITY_TYPES = {
43	    "person": "Person names",
44	    "organization": "Organizations, companies, teams",
45	    "location": "Geographic locations, countries, cities",
46	    "building": "Buildings, facilities, landmarks",
47	    "art": "Artworks, songs, films, books",
48	    "product": "Commercial products, software, vehicles",
49	    "event": "Events, competitions, wars, festivals",
50	    "other": "Other named entities not fitting the above categories",
51	}
52	
53	VALID_TYPES = set(ENTITY_TYPES.keys())
54	
55	MV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
56	
57	logging.basicConfig(
58	    level=logging.INFO,
59	    format="%(asctime)s [%(levelname)s] %(message)s",
60	    datefmt="%Y-%m-%d %H:%M:%S",
61	)
62	log = logging.getLogger(__name__)
63	
64	
65	# ---------------------------------------------------------------------------
66	# Data Loading
67	# ---------------------------------------------------------------------------
68	
69	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
70	    offsets = []
71	    pos = 0
72	    for tok in tokens:
73	        offsets.append((pos, pos + len(tok)))
74	        pos += len(tok) + 1
75	    return offsets
76	
77	
78	def _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:
79	    """Convert tagged tokens to entity spans with char offsets.
80	
81	    Supports both BIO format (B-type/I-type) and flat format (type name only,
82	    as in DFKI-SLT/few-nerd coarse ner_tags).
83	    """
84	    offsets = _token_offsets(tokens)
85	    entities = []
86	    current = None
87	
88	    has_bio = any(t.startswith("B-") or t.startswith("I-") for t in tag_names if t != "O")
89	
90	    for i, tag_id in enumerate(tag_ids):
91	        tag = tag_names[tag_id]
92	
93	        if has_bio:
94	            if tag.startswith("B-"):
95	                if current is not None:
96	                    entities.append(current)
97	                fine_type = tag[2:]
98	                coarse = fine_type.split("-")[0].lower()
99	                current = {
100	                    "text": tokens[i],
101	                    "type": coarse,
102	                    "start": offsets[i][0],
103	                    "end": offsets[i][1],
104	                }
105	            elif tag.startswith("I-") and current is not None:
106	                fine_type = tag[2:]
107	                coarse = fine_type.split("-")[0].lower()
108	                if coarse == current["type"]:
109	                    current["text"] = current["text"] + " " + tokens[i]
110	                    current["end"] = offsets[i][1]
111	                else:
112	                    entities.append(current)
113	                    current = None
114	            else:
115	                if current is not None:
116	                    entities.append(current)
117	                    current = None
118	        else:
119	            # Flat tags: consecutive same-type tokens form one entity
120	            if tag == "O":
121	                if current is not None:
122	                    entities.append(current)
123	                    current = None
124	            else:
125	                etype = tag.lower()
126	                if current is not None and current["type"] == etype:
127	                    current["text"] = current["text"] + " " + tokens[i]
128	                    current["end"] = offsets[i][1]
129	                else:
130	                    if current is not None:
131	                        entities.append(current)
132	                    current = {
133	                        "text": tokens[i],
134	                        "type": etype,
135	                        "start": offsets[i][0],
136	                        "end": offsets[i][1],
137	                    }
138	
139	    if current is not None:
140	        entities.append(current)
141	
142	    return entities
143	
144	
145	def load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:
146	    """Load FewNERD test set from HuggingFace, convert to UIE format."""
147	    from datasets import load_dataset
148	
149	    log.info("Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...")
150	    ds = load_dataset("DFKI-SLT/few-nerd", "supervised", split="test")
151	    tag_names = ds.features["ner_tags"].feature.names
152	
153	    instances = []
154	    for idx, example in enumerate(ds):
155	        tokens = example["tokens"]
156	        tag_ids = example["ner_tags"]
157	        text = " ".join(tokens)
158	        entities = _bio_to_entities(tokens, tag_names, tag_ids)
159	
160	        instances.append({
161	            "id": f"fewnerd_test_{idx:05d}",
162	            "text": text,
163	            "entities": entities,
164	            "relations": [],
165	            "events": [],
166	        })
167	
168	    instances_with_ents = [inst for inst in instances if inst["entities"]]
169	    log.info("  Total test: %d, with entities: %d", len(instances), len(instances_with_ents))
170	
171	    rng = random.Random(seed)
172	    if len(instances_with_ents) > n_instances:
173	        instances_with_ents = rng.sample(instances_with_ents, n_instances)
174	
175	    log.info("  Sampled %d instances (seed=%d)", len(instances_with_ents), seed)
176	    return instances_with_ents
177	
178	
179	def load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:
180	    """Load FewNERD from local UIE-format JSONL file."""
181	    instances = []
182	    with open(path, encoding="utf-8") as f:
183	        for line in f:
184	            line = line.strip()
185	            if not line:
186	                continue
187	            obj = json.loads(line)
188	            if isinstance(obj, dict) and obj.get("entities"):
189	                instances.append(obj)
190	
191	    log.info("Loaded %d instances with entities from %s", len(instances), path)
192	
193	    rng = random.Random(seed)
194	    if len(instances) > n_instances:
195	        instances = rng.sample(instances, n_instances)
196	
197	    log.info("Sampled %d instances (seed=%d)", len(instances), seed)
198	    return instances
199	
200	
201	# ---------------------------------------------------------------------------
202	# Prompt Construction (matches project template in zeroshot_prompts.py)
203	# ---------------------------------------------------------------------------
204	
205	SYSTEM_PROMPT = (
206	    "You are a precise named entity recognition (NER) system. "
207	    "Extract all named entities from the given text and output them in the specified JSON format. "
208	    "Be exhaustive: identify every entity that matches the given types. "
209	    "Be precise: the 'start' and 'end' values must be character offsets in the original text, "
210	    "where 'start' is the index of the first character and 'end' is the index after the last character, "
211	    "such that text[start:end] == entity text."
212	)
213	
214	
215	def build_ner_prompt(text: str) -> list[dict]:
216	    type_desc_lines = "\n".join(f"  - {t}: {d}" for t, d in ENTITY_TYPES.items())
217	    user_prompt = (
218	        "Extract all named entities from the following text.\n\n"
219	        f"Entity types and their definitions:\n{type_desc_lines}\n\n"
220	        f"Text: {text}\n\n"
221	        "Output a JSON object in exactly this format:\n"
222	        '{"entities": [{"text": "exact span", "type": "TYPE", "start": 0, "end": 5}], '
223	        '"relations": [], "events": []}\n\n'
224	        "Rules:\n"
225	        "- Extract ALL entities matching the given types\n"
226	        "- 'start' is the character offset of the first character of the entity in the text\n"
227	        "- 'end' is the character offset after the last character (Python slice convention)\n"
228	        "- 'text' must be the exact substring from the input text\n"
229	        '- If no entities are found, return: {"entities": [], "relations": [], "events": []}\n'
230	        "- Output ONLY the JSON object, no explanation"
231	    )
232	    return [
233	        {"role": "system", "content": SYSTEM_PROMPT},
234	        {"role": "user", "content": user_prompt},
235	    ]
236	
237	
238	# ---------------------------------------------------------------------------
239	# API Sampling
240	# ---------------------------------------------------------------------------
241	
242	def create_client(api_base: str):
243	    from openai import OpenAI
244	
245	    api_key = [REDACTED]"OPENROUTER_API_KEY", "")
246	    if not api_key:
[REDACTED]	        log.error("OPENROUTER_API_KEY not set")
248	        sys.exit(1)
249	    return OpenAI(base_url=api_base, api_key=[REDACTED]
250	
251	
252	def _api_call(client, model_id: str, messages: list[dict],
253	              temperature: float, max_retries: int = 5) -> str:
254	    for attempt in range(max_retries):
255	        try:
256	            kwargs = dict(
257	                model=model_id,
258	                messages=messages,
259	                temperature=temperature,
260	                max_tokens=1024,
261	                response_format={"type": "json_object"},
262	            )
263	            resp = client.chat.completions.create(**kwargs)
264	            return resp.choices[0].message.content or "{}"
265	        except Exception as e:
266	            err_msg = str(e)
267	            # Some models (e.g. GPT-5.5) only support temperature=1
268	            if "temperature" in err_msg and "unsupported" in err_msg.lower():
269	                log.warning("  Model %s does not support temperature=%.1f, retrying with temperature=1",
270	                            model_id, temperature)
271	                try:
272	                    kwargs["temperature"] = 1.0
273	                    resp = client.chat.completions.create(**kwargs)
274	                    return resp.choices[0].message.content or "{}"
275	                except Exception as e2:
276	                    log.warning("  Retry also failed: %s", e2)
277	            wait = min(2 ** attempt * 1.0, 60)
278	            log.warning("  API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
279	            if attempt < max_retries - 1:
280	                time.sleep(wait)
281	            else:
282	                log.error("  FAILED after %d attempts, returning empty", max_retries)
283	                return "{}"
284	
285	
286	def sample_instance(client, model_id: str, messages: list[dict],
287	                    n_samples: int, temperature: float) -> tuple[str, list[str]]:
288	    """Return (greedy_response, [n_samples stochastic responses])."""
289	    greedy = _api_call(client, model_id, messages, temperature=0.0)
290	    stochastic = []
291	    for _ in range(n_samples):
292	        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))
293	    return greedy, stochastic
294	
295	
296	# ---------------------------------------------------------------------------
297	# Response Parsing
298	# ---------------------------------------------------------------------------
299	
300	def parse_response(raw: str) -> dict:
301	    raw = raw.strip()
302	    try:
303	        data = json.loads(raw)
304	    except json.JSONDecodeError:
305	        start = raw.find("{")
306	        end = raw.rfind("}")
307	        if start != -1 and end != -1 and end > start:
308	            try:
309	                data = json.loads(raw[start : end + 1])
310	            except json.JSONDecodeError:
311	                return {"entities": [], "relations": [], "events": []}
312	        else:
313	            return {"entities": [], "relations": [], "events": []}
314	
315	    if not isinstance(data, dict):
316	        return {"entities": [], "relations": [], "events": []}
317	
318	    entities = []
319	    for e in data.get("entities", []):
320	        if not isinstance(e, dict):
321	            continue
322	        try:
323	            etype = str(e["type"]).lower()
324	            if etype not in VALID_TYPES:
325	                continue
326	            entities.append({
327	                "text": str(e["text"]),
328	                "type": etype,
329	                "start": int(e["start"]),
330	                "end": int(e["end"]),
331	            })
332	        except (KeyError, ValueError, TypeError):
333	            continue
334	
335	    return {"entities": entities, "relations": [], "events": []}
336	
337	
338	# ---------------------------------------------------------------------------
339	# Evaluation Primitives
340	# ---------------------------------------------------------------------------
341	
342	def entity_set(entities: list[dict]) -> set[tuple]:
343	    return {(e["start"], e["end"], e["type"]) for e in entities}
344	
345	
346	def compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:
347	    if not gold_set and not pred_set:
348	        return 1.0, 1.0, 1.0
349	    if not pred_set:
350	        return 0.0, 0.0, 0.0
351	    if not gold_set:
352	        return 0.0, 0.0, 0.0
353	    tp = len(pred_set & gold_set)
354	    if tp == 0:
355	        return 0.0, 0.0, 0.0
356	    p = tp / len(pred_set)
357	    r = tp / len(gold_set)
358	    f = 2 * p * r / (p + r)
359	    return p, r, f
360	
361	
362	def entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:
363	    counts: dict[tuple, int] = defaultdict(int)
364	    N = len(samples)
365	    for sample in samples:
366	        for e in sample.get("entities", []):
367	            counts[(e["start"], e["end"], e["type"])] += 1
368	    return {k for k, c in counts.items() if c / N >= threshold}
369	
370	
371	# ---------------------------------------------------------------------------
372	# Instance-level Metrics
373	# ---------------------------------------------------------------------------
374	
375	def _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:
376	    tp = len(pred_set & gold_set)
377	    fp = len(pred_set - gold_set)
378	    fn = len(gold_set - pred_set)
379	    return tp, fp, fn
380	
381	
382	def compute_instance_metrics(
383	    greedy_parsed: dict,
384	    sc_parsed: list[dict],
385	    gold_entities: list[dict],
386	) -> dict:
387	    gold = entity_set(gold_entities)
388	
389	    # Greedy
390	    greedy_ents = entity_set(greedy_parsed)
391	    g_p, g_r, g_f = compute_prf(greedy_ents, gold)
392	    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)
393	
394	    # Per-sample F1
395	    sample_f1s = []
396	    for s in sc_parsed:
397	        _, _, f = compute_prf(entity_set(s), gold)
398	        sample_f1s.append(f)
399	
400	    # MV at multiple thresholds
401	    mv_results = {}
402	    for t in MV_THRESHOLDS:
403	        mv_ents = entity_majority_vote(sc_parsed, threshold=t)
404	        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)
405	        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)
406	        mv_results[f"t{t:.1f}"] = {
407	            "p": mv_p, "r": mv_r, "f1": mv_f,
408	            "tp": mv_tp, "fp": mv_fp, "fn": mv_fn,
409	        }
410	
411	    # Entity-level agreement: frequency of each entity across N samples
412	    N = len(sc_parsed)
413	    ent_counts: dict[tuple, int] = defaultdict(int)
414	    for s in sc_parsed:
415	        for e in s.get("entities", []):
416	            ent_counts[(e["start"], e["end"], e["type"])] += 1
417	
418	    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}
419	    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0
420	
421	    # Degeneracy: all sample entity sets identical
422	    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]
423	    is_degenerate = len(set(sample_sets)) == 1
424	
425	    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)
426	    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0
427	
428	    return {
429	        "greedy_p": g_p,
430	        "greedy_r": g_r,
431	        "greedy_f1": g_f,
432	        "greedy_tp": g_tp,
433	        "greedy_fp": g_fp,
434	        "greedy_fn": g_fn,
435	        "sample_f1s": sample_f1s,
436	        "mean_sample_f1": float(np.mean(sample_f1s)) if sample_f1s else 0.0,
437	        "oracle_f1": oracle_f1,
438	        "mv": mv_results,
439	        "mean_agreement": mean_agreement,
440	        "n_unique_entities": len(ent_counts),
441	        "n_gold_entities": len(gold),
442	        "is_degenerate": is_degenerate,
443	    }
444	
445	
446	# ---------------------------------------------------------------------------
447	# Aggregate Analysis
448	# ---------------------------------------------------------------------------
449	
450	def _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:
451	    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
452	    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
453	    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
454	    return p, r, f
455	
456	
457	def aggregate_model_results(results: list[dict]) -> dict:
458	    n = len(results)
459	
460	    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---
461	    greedy_tp = sum(r["metrics"]["greedy_tp"] for r in results)
462	    greedy_fp = sum(r["metrics"]["greedy_fp"] for r in results)
463	    greedy_fn = sum(r["metrics"]["greedy_fn"] for r in results)
464	    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)
465	
466	    # MV micro-F1 per threshold
467	    mv_by_threshold = {}
468	    for t in MV_THRESHOLDS:
469	        tk = f"t{t:.1f}"
470	        t_tp = sum(r["metrics"]["mv"][tk]["tp"] for r in results)
471	        t_fp = sum(r["metrics"]["mv"][tk]["fp"] for r in results)
472	        t_fn = sum(r["metrics"]["mv"][tk]["fn"] for r in results)
473	        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)
474	        # Also keep macro for reference
475	        macro_f1s = [r["metrics"]["mv"][tk]["f1"] for r in results]
476	        mv_by_threshold[tk] = {
477	            "micro_p": mp, "micro_r": mr, "micro_f1": mf,
478	            "macro_f1": float(np.mean(macro_f1s)),
479	            "std_f1": float(np.std(macro_f1s)),
480	        }
481	
482	    # Best threshold by micro-F1
483	    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k]["micro_f1"])
484	    best_mv_micro_f1 = mv_by_threshold[best_t]["micro_f1"]
485	
486	    selection_gap = best_mv_micro_f1 - greedy_micro_f1
487	
488	    # --- Macro-F1 (secondary): per-instance F1 averaged ---
489	    greedy_f1s = [r["metrics"]["greedy_f1"] for r in results]
490	    oracle_f1s = [r["metrics"]["oracle_f1"] for r in results]
491	    mean_sample_f1s = [r["metrics"]["mean_sample_f1"] for r in results]
492	    agreements = [r["metrics"]["mean_agreement"] for r in results]
493	    degeneracy_flags = [r["metrics"]["is_degenerate"] for r in results]
494	
495	    # Correlation: mean_agreement vs greedy_f1 (Spearman)
496	    if n >= 3:
497	        rho, pval = spearmanr(agreements, greedy_f1s)
498	        corr_agreement_f1 = {"rho": float(rho), "p": float(pval)}
499	    else:
500	        corr_agreement_f1 = {"rho": 0.0, "p": 1.0}
501	
502	    # Correlation: mean_agreement vs MV F1 at best threshold
503	    best_mv_f1s = [r["metrics"]["mv"][best_t]["f1"] for r in results]
504	    if n >= 3:
505	        rho2, pval2 = spearmanr(agreements, best_mv_f1s)
506	        corr_agreement_mv = {"rho": float(rho2), "p": float(pval2)}
507	    else:
508	        corr_agreement_mv = {"rho": 0.0, "p": 1.0}
509	
510	    return {
511	        "n_instances": n,
512	        # Primary: micro-F1
513	        "greedy_micro": {"p": greedy_micro_p, "r": greedy_micro_r, "f1": greedy_micro_f1},
514	        "best_mv_micro_f1": best_mv_micro_f1,
515	        "selection_gap": selection_gap,
516	        # Secondary: macro-F1
517	        "greedy_f1": {"mean": float(np.mean(greedy_f1s)), "std": float(np.std(greedy_f1s))},
518	        "oracle_f1": {"mean": float(np.mean(oracle_f1s)), "std": float(np.std(oracle_f1s))},
519	        "mean_sample_f1": {"mean": float(np.mean(mean_sample_f1s)), "std": float(np.std(mean_sample_f1s))},
520	        "mv_f1_by_threshold": mv_by_threshold,
521	        "best_threshold": best_t,
522	        "degeneracy_rate": sum(degeneracy_flags) / n,
523	        "mean_agreement": {"mean": float(np.mean(agreements)), "std": float(np.std(agreements))},
524	        "correlation_agreement_greedy_f1": corr_agreement_f1,
525	        "correlation_agreement_mv_f1": corr_agreement_mv,
526	    }
527	
528	
529	def diagnose_failure_modes(results: list[dict]) -> dict:
530	    """Categorize failure modes across instances."""
531	    n = len(results)
532	    degenerate = [r for r in results if r["metrics"]["is_degenerate"]]
533	    best_t_key = f"t0.5"
534	
535	    mv_better = []
536	    mv_worse = []
537	    mv_same = []
538	
539	    for r in results:
540	        g = r["metrics"]["greedy_f1"]
541	        m = r["metrics"]["mv"][best_t_key]["f1"]
542	        diff = m - g
543	        if diff > 0.01:
544	            mv_better.append(r)
545	        elif diff < -0.01:
546	            mv_worse.append(r)
547	        else:
548	            mv_same.append(r)
549	
550	    # High agreement but wrong
551	    high_agree_wrong = [
552	        r for r in results
553	        if r["metrics"]["mean_agreement"] > 0.8 and r["metrics"]["greedy_f1"] < 0.5
554	    ]
555	
556	    # Low agreement but correct
557	    low_agree_correct = [
558	        r for r in results
559	        if r["metrics"]["mean_agreement"] < 0.3 and r["metrics"]["greedy_f1"] > 0.8
560	    ]
561	
562	    return {
563	        "degeneracy_count": len(degenerate),
564	        "degeneracy_rate": len(degenerate) / n,
565	        "mv_better_count": len(mv_better),
566	        "mv_worse_count": len(mv_worse),
567	        "mv_same_count": len(mv_same),
568	        "high_agreement_wrong_count": len(high_agree_wrong),
569	        "low_agreement_correct_count": len(low_agree_correct),
570	    }
571	
572	
573	# ---------------------------------------------------------------------------
574	# Checkpointing
575	# ---------------------------------------------------------------------------
576	
577	def save_checkpoint(data: list[dict], path: str):
578	    with open(path, "w", encoding="utf-8") as f:
579	        for item in data:
580	            f.write(json.dumps(item, ensure_ascii=False) + "\n")
581	
582	
583	def load_checkpoint(path: str) -> list[dict]:
584	    if not os.path.exists(path):
585	        return []
586	    data = []
587	    with open(path, encoding="utf-8") as f:
588	        for line in f:
589	            line = line.strip()
590	            if line:
591	                data.append(json.loads(line))
592	    return data
593	
594	
595	# ---------------------------------------------------------------------------
596	# Main Experiment Loop
597	# ---------------------------------------------------------------------------
598	
599	def run_model(
600	    client,
601	    model_name: str,
602	    model_id: str,
603	    instances: list[dict],
604	    n_samples: int,
605	    temperature: float,
606	    output_dir: Path,
607	    resume: bool = True,
608	) -> list[dict]:
609	    ckpt_path = output_dir / f"checkpoint_{model_name}.jsonl"
610	    results = load_checkpoint(str(ckpt_path)) if resume else []
611	    done_ids = {r["id"] for r in results}
612	
613	    remaining = [inst for inst in instances if inst["id"] not in done_ids]
614	    log.info("Model %s: %d done, %d remaining", model_name, len(done_ids), len(remaining))
615	
616	    for i, inst in enumerate(remaining):
617	        log.info(
618	            "  [%d/%d] id=%s len=%d entities=%d",
619	            len(done_ids) + i + 1,
620	            len(instances),
621	            inst["id"],
622	            len(inst["text"]),
623	            len(inst["entities"]),
624	        )
625	
626	        messages = build_ner_prompt(inst["text"])
627	        greedy_raw, sc_raws = sample_instance(
628	            client, model_id, messages, n_samples, temperature
629	        )
630	
631	        greedy_parsed = parse_response(greedy_raw)
632	        sc_parsed = [parse_response(r) for r in sc_raws]
633	
634	        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst["entities"])
635	
636	        result = {
637	            "id": inst["id"],
638	            "text": inst["text"],
639	            "gold_entities": inst["entities"],
640	            "greedy_raw": greedy_raw,
641	            "greedy_parsed": greedy_parsed,
642	            "sc_raws": sc_raws,
643	            "sc_parsed": sc_parsed,
644	            "metrics": metrics,
645	        }
646	        results.append(result)
647	
648	        # Checkpoint every 10 instances
649	        if (len(done_ids) + i + 1) % 10 == 0:
650	            save_checkpoint(results, str(ckpt_path))
651	            running = aggregate_model_results(results)
652	            log.info(
653	                "    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%",
654	                running["greedy_micro"]["f1"],
655	                running["mv_f1_by_threshold"]["t0.5"]["micro_f1"],
656	                running["selection_gap"],
657	                running["degeneracy_rate"] * 100,
658	            )
659	
660	    save_checkpoint(results, str(ckpt_path))
661	    return results
662	
663	
664	def main():
665	    parser = argparse.ArgumentParser(description="Frontier SC on FewNERD")
666	    parser.add_argument("--data-path", type=str, default=None,
667	                        help="Path to local FewNERD UIE JSONL file")
668	    parser.add_argument("--from-hf", action="store_true",
669	                        help="Load FewNERD from HuggingFace")
670	    parser.add_argument("--n-instances", type=int, default=200)
671	    parser.add_argument("--n-samples", type=int, default=8)
672	    parser.add_argument("--temperature", type=float, default=1.0)
673	    parser.add_argument("--seed", type=int, default=42)
674	    parser.add_argument("--api-base", type=str, default=API_BASE_URL)
675	    parser.add_argument("--models", type=str, nargs="+", default=list(MODELS.keys()),
676	                        choices=list(MODELS.keys()),
677	                        help="Which models to run")
678	    parser.add_argument("--output-dir", type=str,
679	                        default=str(Path(__file__).parent / "output"))
680	    parser.add_argument("--no-resume", action="store_true",
681	                        help="Start fresh, ignore checkpoints")
682	    args = parser.parse_args()
683	
684	    output_dir = Path(args.output_dir)
685	    output_dir.mkdir(parents=True, exist_ok=True)
686	
687	    # Load data
688	    if args.data_path and os.path.exists(args.data_path):
689	        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)
690	    elif args.from_hf:
691	        instances = load_fewnerd_hf(args.n_instances, args.seed)
692	    else:
693	        parser.error("Specify --data-path or --from-hf")
694	
695	    # Save selected instance IDs for reproducibility
696	    id_list = [inst["id"] for inst in instances]
697	    with open(output_dir / "instance_ids.json", "w") as f:
698	        json.dump({"seed": args.seed, "n": len(id_list), "ids": id_list}, f, indent=2)
699	
700	    client = create_client(args.api_base)
701	
702	    all_summaries = {}
703	
704	    for model_name in args.models:
705	        model_id = MODELS[model_name]
706	        log.info("=" * 60)
707	        log.info("Running model: %s (%s)", model_name, model_id)
708	        log.info("=" * 60)
709	
710	        results = run_model(
711	            client, model_name, model_id, instances,
712	            args.n_samples, args.temperature, output_dir,
713	            resume=not args.no_resume,
714	        )
715	
716	        # Aggregate
717	        summary = aggregate_model_results(results)
718	        diagnosis = diagnose_failure_modes(results)
719	        summary["diagnosis"] = diagnosis
720	        all_summaries[model_name] = summary
721	
722	        # Print summary
723	        log.info("\n--- %s Summary ---", model_name)
724	        log.info("  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)",
725	                 summary["greedy_micro"]["f1"], summary["greedy_micro"]["p"], summary["greedy_micro"]["r"])
726	        log.info("  [micro] Best MV F1: %.4f (threshold=%s)", summary["best_mv_micro_f1"], summary["best_threshold"])
727	        log.info("  [micro] Selection gap: %+.4f", summary["selection_gap"])
728	        log.info("  [macro] Greedy F1: %.4f (±%.4f)", summary["greedy_f1"]["mean"], summary["greedy_f1"]["std"])
729	        log.info("  [macro] Oracle F1: %.4f", summary["oracle_f1"]["mean"])
730	        log.info("  Degeneracy rate: %.1f%%", summary["degeneracy_rate"] * 100)
731	        log.info("  Corr(agree,F1):  rho=%.4f (p=%.4f)",
732	                 summary["correlation_agreement_greedy_f1"]["rho"],
733	                 summary["correlation_agreement_greedy_f1"]["p"])
734	        log.info("  MV threshold sweep (micro-F1):")
735	        for t in MV_THRESHOLDS:
736	            tk = f"t{t:.1f}"
737	            mv = summary["mv_f1_by_threshold"][tk]
738	            delta = mv["micro_f1"] - summary["greedy_micro"]["f1"]
739	            marker = " <-- BEST" if tk == summary["best_threshold"] else ""
740	            log.info("    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s",
741	                     t, mv["micro_f1"], mv["macro_f1"], delta, marker)
742	
743	    # Cross-model comparison
744	    if len(all_summaries) > 1:
745	        log.info("\n" + "=" * 60)
746	        log.info("CROSS-MODEL COMPARISON")
747	        log.info("=" * 60)
748	        log.info("%-20s %10s %10s %10s %10s %8s",
749	                 "Model", "Greedy(μ)", "MV@best(μ)", "Oracle(M)", "Gap(μ)", "Degen%")
750	        for name, s in all_summaries.items():
751	            log.info(
752	                "%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%",
753	                name,
754	                s["greedy_micro"]["f1"],
755	                s["best_mv_micro_f1"],
756	                s["oracle_f1"]["mean"],
757	                s["selection_gap"],
758	                s["degeneracy_rate"] * 100,
759	            )
760	
761	    # Save final results
762	    final_output = {
763	        "config": {
764	            "n_instances": args.n_instances,
765	            "n_samples": args.n_samples,
766	            "temperature": args.temperature,
767	            "seed": args.seed,
768	            "api_base": args.api_base,
769	            "models": {m: MODELS[m] for m in args.models},
770	        },
771	        "summaries": all_summaries,
772	    }
773	
774	    with open(output_dir / "results_summary.json", "w") as f:
775	        json.dump(final_output, f, indent=2, default=str)
776	
777	    log.info("\nResults saved to %s", output_dir)
778	
779	
780	if __name__ == "__main__":
781	    main()
782	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "4416d31e-a8ed-4ce3-9e66-c2d69270af5b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 782,
      "startLine": 1,
      "totalLines": 782
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cf5NLq9t7zcBxJSmnmTDdS`</summary>

```json
{
  "command": "ps -p 1509955 -o pid= 2>/dev/null && echo \"ALIVE\" || echo \"DEAD\"",
  "description": "Check if old process is alive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "a4d47cc5-0e5e-45a8-b856-883f41272e39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

_source line 9 · 2026-05-20T22:06:01.964Z_

<details><summary>↩ Tool result · `toolu_01Cf5NLq9t7zcBxJSmnmTDdS`</summary>

```text
DEAD
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "1b008dac-3347-40e9-a88c-62491b2c73cd",
  "tool_use_result": {
    "stdout": "DEAD",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_015raZ79kfZqQV52mx8o4yqu`</summary>

```json
{
  "command": "echo $OPENROUTER_API_KEY | head -c 10",
  "description": "Check OpenRouter API key"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "17983f01-6f5f-43a6-b25a-0380cea73055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

_source line 11 · 2026-05-20T22:06:02.931Z_

<details><summary>↩ Tool result · `toolu_015raZ79kfZqQV52mx8o4yqu`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "887a36f2-6891-4252-a053-57289a52aa26",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_0153QJfSkxT3tb1ehoBUZmjm`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/output/ 2>/dev/null || echo \"NO_OUTPUT_DIR\"",
  "description": "Check existing checkpoints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "548be12d-9a81-4ae0-9eb5-b4eebe243e97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDPW8Efy22HxXmM55ECW5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12745,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12745
      },
      "output_tokens": 33,
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

_source line 13 · 2026-05-20T22:06:03.475Z_

<details><summary>↩ Tool result · `toolu_0153QJfSkxT3tb1ehoBUZmjm`</summary>

```text
total 16
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 19:26 .
drwxr-xr-x 4 ubuntu ubuntu 4096 May 20 21:02 ..
-rw-r--r-- 1 ubuntu ubuntu 5243 May 20 21:02 instance_ids.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "4276b863-d950-4fce-8572-3c1f0c408514",
  "tool_use_result": {
    "stdout": "total 16\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 20 19:26 .\ndrwxr-xr-x 4 ubuntu ubuntu 4096 May 20 21:02 ..\n-rw-r--r-- 1 ubuntu ubuntu 5243 May 20 21:02 instance_ids.json",
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

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Issues found:
1. Old process is DEAD - no need to kill
2. OPENROUTER_API_KEY is empty - need to check .env or memory
3. Output dir exists but only has instance_ids.json (no checkpoints)

Let me check for the API key before proceeding with fixes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "03c94c7e-759a-494b-8fbe-3253c3fbd687",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dntr3ZDJsfuVgM25WX6yZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11459,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11459
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

OPENROUTER_API_KEY 为空。检查 .env 和 memory 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "49f3a521-a9a3-400a-9438-3cb70f2c6a2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dntr3ZDJsfuVgM25WX6yZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11459,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11459
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

<details open><summary>🔧 Tool call — Bash · `toolu_013zDW5ZWoUcbqtRLDec9D6H`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \".env\" -o -name \"*.env\" 2>/dev/null | head -5",
  "description": "Find .env files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "ad10200b-9db3-4672-9962-4a8944d4d0df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dntr3ZDJsfuVgM25WX6yZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11459,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11459
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

_source line 17 · 2026-05-20T22:06:10.957Z_

<details><summary>↩ Tool result · `toolu_013zDW5ZWoUcbqtRLDec9D6H`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "816e5e3a-e660-45fa-a422-aa43ae3e8aac",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01JT9jy11dozYRfJcY8qXNov`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md 2>/dev/null | grep -i -A2 \"openrouter\\|api.key\\|API_KEY\" || echo \"NOT_FOUND\"",
  "description": "Check memory.md for API key references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "11205511-70ad-41c0-984a-12748de3bc07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dntr3ZDJsfuVgM25WX6yZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11459,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11459
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

_source line 19 · 2026-05-20T22:06:12.602Z_

<details><summary>↩ Tool result · `toolu_01JT9jy11dozYRfJcY8qXNov`</summary>

```text
## OpenRouter API 限制（2026-05-20）

- Base URL: `http://47.94.22.126/v1`（TUM 代理）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "fc5be314-db1e-4484-9faf-397dcd27f44a",
  "tool_use_result": {
    "stdout": "## OpenRouter API 限制（2026-05-20）\n\n- Base URL: `http://47.94.22.126/v1`（TUM 代理）",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01XDkzmnU5ZRBw34wyMJicj2`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea_gen_0514_1-projects-struct_self_consist_ie/memory/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "849a9356-7423-43c4-bcb2-85ff1330f54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dntr3ZDJsfuVgM25WX6yZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11459,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11459
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

_source line 21 · 2026-05-20T22:06:13.539Z_

<details><summary>↩ Tool result · reported error · `toolu_01XDkzmnU5ZRBw34wyMJicj2`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "ab8596ce-6446-4ab7-9826-aeefd93697d3",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie."
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01LjQv58uxFh7hZLZzbt61TB`</summary>

```json
{
  "command": "grep -r \"OPENROUTER_API_KEY\\|openrouter\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md 2>/dev/null | head -10",
  "description": "Check memory.md for full API key references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "dcc0ee55-f822-4051-9576-82bd421ddc40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StjwsLax5apvV5k9Dwb8Sw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 36045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
      },
      "output_tokens": 63,
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

_source line 23 · 2026-05-20T22:06:16.884Z_

<details><summary>↩ Tool result · `toolu_01LjQv58uxFh7hZLZzbt61TB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "b6a7dc7e-9f94-420a-bb65-8fae17b42bd4",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01GRiy6f16qJErdGLy8T6rby`</summary>

```json
{
  "command": "grep -r \"OPENROUTER_API_KEY\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/ --include=\"*.md\" --include=\"*.env\" --include=\"*.sh\" --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -10",
  "description": "Search all config files for OPENROUTER_API_KEY"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "f6d11cb0-f0b7-43fb-80d9-36060a0da039",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StjwsLax5apvV5k9Dwb8Sw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 36045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
      },
      "output_tokens": 63,
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

_source line 25 · 2026-05-20T22:06:18.466Z_

<details><summary>↩ Tool result · `toolu_01GRiy6f16qJErdGLy8T6rby`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_b_frontier_sc_20260520T181716_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "d69a61c6-e3a2-45d3-ad20-ebca677efc66",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/workers/registry.json\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_b_frontier_sc_20260520T181716_result.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_012c9gDSTrgr8HsTA5byuReM`</summary>

```json
{
  "command": "grep \"OPENROUTER_API_KEY\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_b_frontier_sc_20260520T181716_result.json 2>/dev/null | head -5",
  "description": "Check worker result for API key info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "0c1264b3-a706-405a-9223-36f31a78b556",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMiPuiWw85Qv8gJeLmrqoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 36663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 536
      },
      "output_tokens": 63,
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

_source line 27 · 2026-05-20T22:06:22.035Z_

<details><summary>↩ Tool result · `toolu_012c9gDSTrgr8HsTA5byuReM`</summary>

````text
  "raw": "代码和 registry 已就绪。产出报告：\n\n---\n\n## 产出报告：exp_b_frontier_sc_fewnerd\n\n### 代码路径\n`artifacts/experiments/frontier_sc/run_frontier_sc.py`\n\n### OpenRouter Model IDs\n| Model | OpenRouter ID |\n|---|---|\n| GPT-5.5 | `openai/gpt-5.5` |\n| Claude Opus 4.6 | `anthropic/claude-opus-4.6` |\n\n### Cost 估算\n\n| 项目 | 数值 |\n|---|---|\n| API calls | 200 inst × (1 greedy + 8 SC) × 2 models = **3,600 calls** |\n| 每 call tokens | ~800 input + ~300 output |\n| 总 input | ~2.88M tokens |\n| 总 output | ~1.08M tokens |\n| **GPT-5.5** | 1.44M × $5/M + 0.54M × $30/M = **$23.4** |\n| **Claude Opus 4.6** | 1.44M × $5/M + 0.54M × $25/M = **$20.7** |\n| **总计** | **~$44** |\n\n### 依赖\n```\nopenai          # OpenAI SDK (兼容 OpenRouter)\nnumpy\nscipy\ndatasets        # 仅 --from-hf 模式需要\n```\n\n### 运行方式\n```bash\nexport OPENROUTER_API_KEY=[REDACTED]"sk-...\"\n\n# 从 HuggingFace 加载数据\npython run_frontier_sc.py --from-hf\n\n# 或从本地 UIE JSONL 加载（可从服务器 scp）\npython run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n\n# 只跑单个模型\npython run_frontier_sc.py --from-hf --models gpt-5.5\n```\n\n### 关键设计\n- **Greedy 独立调用**（T=0）与 **8 个 SC 样本**（T=1.0）分开\n- **9 阈值 MV 扫描**（0.1-0.9），自动找最优阈值\n- **每 10 个 instance checkpoint**，支持断点续跑（`--no-resume` 强制重新开始）\n- **Failure mode 诊断**：degeneracy rate、high-agreement-wrong、low-agreement-correct\n- **Spearman correlation**：agreement ↔ greedy F1、agreement ↔ MV F1\n- Prompt 模板与项目 `zeroshot_prompts.py` 完全一致（带 type descriptions）"
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "5bbf7385-7233-4e7a-a728-0190b7daa664",
  "tool_use_result": {
    "stdout": "  \"raw\": \"代码和 registry 已就绪。产出报告：\\n\\n---\\n\\n## 产出报告：exp_b_frontier_sc_fewnerd\\n\\n### 代码路径\\n`artifacts/experiments/frontier_sc/run_frontier_sc.py`\\n\\n### OpenRouter Model IDs\\n| Model | OpenRouter ID |\\n|---|---|\\n| GPT-5.5 | `openai/gpt-5.5` |\\n| Claude Opus 4.6 | `anthropic/claude-opus-4.6` |\\n\\n### Cost 估算\\n\\n| 项目 | 数值 |\\n|---|---|\\n| API calls | 200 inst × (1 greedy + 8 SC) × 2 models = **3,600 calls** |\\n| 每 call tokens | ~800 input + ~300 output |\\n| 总 input | ~2.88M tokens |\\n| 总 output | ~1.08M tokens |\\n| **GPT-5.5** | 1.44M × $5/M + 0.54M × $30/M = **$23.4** |\\n| **Claude Opus 4.6** | 1.44M × $5/M + 0.54M × $25/M = **$20.7** |\\n| **总计** | **~$44** |\\n\\n### 依赖\\n```\\nopenai          # OpenAI SDK (兼容 OpenRouter)\\nnumpy\\nscipy\\ndatasets        # 仅 --from-hf 模式需要\\n```\\n\\n### 运行方式\\n```bash\\nexport OPENROUTER_API_KEY=[REDACTED]\"sk-...\\\"\\n\\n# 从 HuggingFace 加载数据\\npython run_frontier_sc.py --from-hf\\n\\n# 或从本地 UIE JSONL 加载（可从服务器 scp）\\npython run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\\n\\n# 只跑单个模型\\npython run_frontier_sc.py --from-hf --models gpt-5.5\\n```\\n\\n### 关键设计\\n- **Greedy 独立调用**（T=0）与 **8 个 SC 样本**（T=1.0）分开\\n- **9 阈值 MV 扫描**（0.1-0.9），自动找最优阈值\\n- **每 10 个 instance checkpoint**，支持断点续跑（`--no-resume` 强制重新开始）\\n- **Failure mode 诊断**：degeneracy rate、high-agreement-wrong、low-agreement-correct\\n- **Spearman correlation**：agreement ↔ greedy F1、agreement ↔ MV F1\\n- Prompt 模板与项目 `zeroshot_prompts.py` 完全一致（带 type descriptions）\"",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
````

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_011MJKb1xS4DLmso6jgUTvp9`</summary>

```json
{
  "command": "grep \"OPENROUTER_API_KEY\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/workers/registry.json 2>/dev/null | head -5",
  "description": "Check global registry for API key info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "a9967c16-b15a-48c3-a082-7d5b7b175863",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMiPuiWw85Qv8gJeLmrqoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 36663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 536
      },
      "output_tokens": 63,
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

_source line 29 · 2026-05-20T22:06:22.496Z_

<details><summary>↩ Tool result · `toolu_011MJKb1xS4DLmso6jgUTvp9`</summary>

````text
      "task_prompt": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：编写 HumanEval SC pilot 实验代码\n\n### 背景\nCross-task universality 扩展：验证 SC failure modes 在 code generation 上的表现。Code 有确定性验证（unit tests），与 NER 不同。\n\n### 实验设计\n\n- **模型**: GPT-5.5 via OpenRouter API\n- **API**: base_url=http://47.94.22.126/v1, model name 需要确认（可能是 \"openai/gpt-5.5\" 或类似格式）\n- **数据**: HumanEval 164 problems\n- **采样**: N=8, T=1.0\n- **评估**: 生成 8 个 code solutions → 执行 unit test → pass@1\n- **对比**: greedy vs MV（多数 test-passing solutions 投票）vs random selection\n- **诊断**: degeneracy rate、agreement patterns\n- **CPU-only**（API 调用 + local test execution）\n\n### 你要做的\n\n1. **编写脚本 `run_humaneval_sc.py`**（写到本地 `artifacts/experiments/humaneval_sc/run_humaneval_sc.py`）:\n\n   核心流程:\n   ```\n   a) load_humaneval(): 从 HuggingFace 加载 HumanEval dataset\n      from datasets import load_dataset\n      ds = load_dataset(\"openai/openai_humaneval\", split=\"test\")\n   \n   b) build_prompts(): 构建 code completion prompt\n      使用 HumanEval 标准 prompt format\n   \n   c) api_sample(): 调 OpenRouter API, N=8, T=1.0\n      - 使用 openai SDK: \n        from openai import OpenAI\n        client = OpenAI(base_url=\"http://47.94.22.126/v1\", api_key=[REDACTED]"OPENROUTER_API_KEY\"])\n        response = client.chat.completions.create(model=\"openai/gpt-5.5\", messages=[...], n=8, temperature=1.0)\n      - 注意 rate limiting, 加 retry + backoff\n      - 先用 1 个 problem 测试 API 连通性\n   \n   d) execute_tests(): 对每个 solution 执行 HumanEval unit tests\n      - 使用 subprocess with timeout (30s per test)\n      - 记录 pass/fail\n      - ⚠️ 安全: 在 sandbox 中执行（限制 imports, timeout）\n   \n   e) evaluate():\n      - greedy: 第一个 sample 的 pass rate\n      - MV: 多数 test-passing solutions 中选一个\n      - pass@k: 标准 pass@1, pass@8 计算\n      - random: 随机选一个 sample 的 pass rate\n   \n   f) diagnose():\n      - degeneracy: 8 个 solutions 完全相同的比例\n      - agreement: 多数一致 solutions 是否 test-passing\n      - execution agreement: 相同 output 的 solutions 分组\n   \n   g) save_results()\n   ```\n\n2. **API key 处理**:\n   - 脚本从环境变量 `OPENROUTER_API_KEY` 读取\n   - API key 正在审批中，先写代码，key 到了再运行\n   - 先用 WebSearch 确认 OpenRouter 上 GPT-5.5 的 model ID 格式\n\n3. **HumanEval test execution**:\n   - 使用标准 HumanEval evaluation harness\n   - 或自己实现 safe execution（exec() with restricted globals + timeout）\n   - 参考 human-eval package: `pip install human-eval`\n\n4. **更新 registry spec**:\n   - exp_id: exp_a2_humaneval_sc\n   - command, data_count=164, model_name=\"GPT-5.5 (OpenRouter)\", seed=42\n\n5. **产出报告**: 代码路径、依赖列表、API cost 估算、预计时长。\n\n### 注意\n- CPU-only 实验，不需要 GPU\n- API key 待审批，先写代码\n- HumanEval test execution 需要安全 sandbox\n- 不要等结果，代码就绪即完成\n- 先用 WebSearch 确认 OpenRouter GPT-5.5 model ID\n",
      "task_prompt": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：编写 Frontier Model SC on FewNERD 实验代码\n\n### 背景\n验证 correlation-selection gap 在 frontier 模型上是否依然存在。如果 frontier 模型也有同样的 gap，说明这是 LLM SC 的 fundamental limit 而非 capability limitation。\n\n### 实验设计\n\n- **模型**: GPT-5.5 + Claude Opus 4.6（通过 OpenRouter API）\n- **API**: base_url=http://47.94.22.126/v1\n- **数据**: FewNERD test set 随机 200 instances（seed=42）\n- **采样**: N=8, T=1.0\n- **不需要 logprob**——只统计 frequency-based agreement（每个 entity 在 8 个 sample 中出现几次）\n- **对比**: greedy vs MV，记录 correlation-selection gap\n- **输出**: per-model F1 表 + failure mode 分布\n- **CPU-only**（API 调用）\n- **预估 cost**: ~$50-100，~4-6h\n\n### 你要做的\n\n1. **编写脚本 `run_frontier_sc.py`**（写到本地 `artifacts/experiments/frontier_sc/run_frontier_sc.py`）:\n\n   核心流程:\n   ```\n   a) load_fewnerd_subset(): 从项目数据加载 FewNERD test, random sample 200 instances\n      - FewNERD data 在服务器上: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\n      - 但这个脚本要在本地/CPU 跑，所以需要能本地读取数据\n      - 或者从 HuggingFace 加载 FewNERD\n   \n   b) build_ner_prompt(): 构建 NER prompt（与项目标准 template 一致）\n      - 参考项目的 UIE JSON schema\n      - Entity types: person, organization, location, building, art, product, event, other\n   \n   c) api_sample(): 调 OpenRouter API\n      - 使用 openai SDK:\n        client = OpenAI(base_url=\"http://47.94.22.126/v1\", api_key=[REDACTED]"OPENROUTER_API_KEY\"])\n      - GPT-5.5: model=\"openai/gpt-5.5\"（需确认 OpenRouter model ID）\n      - Claude Opus 4.6: model=\"anthropic/claude-opus-4-6\"（需确认）\n      - N=8, T=1.0\n      - JSON mode / structured output（如支持的话）\n      - Rate limiting: retry + exponential backoff\n      - 每个 model × 200 instances × 8 samples = 1600 API calls per model\n   \n   d) parse_responses(): 解析 JSON 输出，提取 entities\n      - 容错处理: 部分 response 可能不是 valid JSON\n      - Normalize entity format: (text, type, start, end)\n   \n   e) evaluate():\n      - greedy F1: 第一个 sample vs gold\n      - MV F1: majority vote construction vs gold\n      - entity-level agreement: 每个 entity 在 8 samples 中出现的次数\n      - correlation: agreement score vs instance F1 的 Spearman correlation\n      - selection gap: MV F1 - greedy F1\n   \n   f) diagnose():\n      - degeneracy rate: 8 个 entity sets 完全相同的比例\n      - agreement-correctness correlation\n      - per-model comparison\n   \n   g) save_results(): JSON output + summary\n   ```\n\n2. **API key 处理**:\n   - 从环境变量 `OPENROUTER_API_KEY` 读取\n   - API key 正在审批中，先写代码\n   - 先用 WebSearch 确认 OpenRouter 上 GPT-5.5 和 Claude Opus 4.6 的 model ID\n\n3. **FewNERD 数据**:\n   - 需要在本地或 CPU 服务器上可用\n   - 检查本地项目目录是否有 FewNERD data\n   - 如果没有，从 HuggingFace 下载或从服务器 scp\n\n4. **Cost estimation**:\n   - 200 instances × 8 samples × 2 models = 3200 API calls\n   - 估算每个 call 的 token 数（prompt ~500 tokens + response ~200 tokens）\n   - 计算总 cost\n\n5. **更新 registry spec**:\n   - exp_id: exp_b_frontier_sc_fewnerd\n   - command, data_count=200, model_name=\"GPT-5.5 + Claude Opus 4.6\", seed=42\n\n6. **产出报告**: 代码路径、API model IDs、cost 估算、依赖列表。\n\n### 注意\n- CPU-only 实验\n- API key 待审批\n- 不需要 logprob\n- 不要等结果，代码就绪即完成\n- 先用 WebSearch 确认 OpenRouter model IDs\n",
      "task_prompt": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：修复 MV metric bug 并运行 HumanEval SC 实验\n\n**目标**：修复 run_humaneval_sc.py 的 MV 投票 bug，然后运行实验。\n\n**exp_id**: `exp_a2_humaneval_sc`\n**类型**: CPU + OpenRouter API\n**API Key**: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`\n**API Base**: `http://47.94.22.126/v1`\n**Model**: `openai/gpt-5.5`\n\n### Bug 描述（必须先修再跑）\n\n文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`\n\n`evaluate()` 函数 (约 L233-246) 的 MV 实现有 bug：\n\n```python\npassing_codes = [s[\"code\"] for s in r[\"sample_results\"] if s[\"passed\"]]\nif not passing_codes:\n    continue\nmv_applicable += 1\ncode_counts = Counter(passing_codes)\nmajority_code = code_counts.most_common(1)[0][0]\nmv_correct += 1  # BUG: 从 passing codes 里投票，结果 trivially 全对\n```\n\n**问题**：MV 只在 passing solutions 中投票，所以 majority-voted code 必然 pass（by construction）。这使得 `mv_pass_rate == oracle_pass_rate`，指标无意义。\n\n**修复方案**：MV 应该在 **所有 N 个 solution** 中按文本投票，选出 majority code，然后检查这个 code 是否 pass tests：\n\n```python\n# 正确的 MV: 在所有 solutions 中投票\nall_codes = [s[\"code\"] for s in r[\"sample_results\"]]\ncode_counts = Counter(all_codes)\nmajority_code = code_counts.most_common(1)[0][0]\n# 检查 majority code 是否通过测试\nmajority_passed = any(\n    s[\"passed\"] for s in r[\"sample_results\"] if s[\"code\"] == majority_code\n)\nif majority_passed:\n    mv_correct += 1\n```\n\n### 运行步骤\n\n1. **先修 bug**：编辑本地文件 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`，修复 `evaluate()` 中的 MV 逻辑。\n\n2. **测试 API 连通性**：\n   ```bash\n   export OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\"\n   cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc\n   python run_humaneval_sc.py --test_api --n_samples 1 --output_dir ./test_output\n   ```\n   验证 API 可达。如果失败，检查网络/key。\n\n3. **正式运行**：\n   ```bash\n   export OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\"\n   python run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 \\\n       --output_dir ./results --test_api\n   ```\n   预计 30-60 min，有 checkpoint 支持断点续跑。\n\n4. **收集结果**：\n   - greedy pass rate, pass@1, pass@8\n   - MV pass rate (修复后的)\n   - random pass rate, oracle pass rate\n   - degeneracy rate, majority agreement rate\n   - MV vs greedy 的 gap\n\n5. **更新 registry**：\n   - status → DONE\n   - conclusion: 基于 correlation-selection gap 是否存在\n   - metrics: 所有指标\n   - checkpoint_path, log_path\n\n**环境**：本地运行即可（CPU + API），不需要 SSH 到服务器。需要 `pip install openai datasets numpy`。\n",
      "task_prompt": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：修复 micro-F1 并运行 Frontier SC 实验\n\n**目标**：修复 run_frontier_sc.py 的评估指标（macro-F1 → micro-F1），然后运行实验。\n\n**exp_id**: `exp_b_frontier_sc_fewnerd`\n**类型**: CPU + OpenRouter API\n**API Key**: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`\n**API Base**: `http://47.94.22.126/v1`\n**Models**: GPT-5.5 (`openai/gpt-5.5`) + Claude Opus 4.6 (`anthropic/claude-opus-4.6`)\n\n### Bug 描述（必须先修再跑）\n\n文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py`\n\n`aggregate_model_results()` 函数 (约 L396-451) 使用 **macro-F1**（per-instance F1 平均），但 NER 标准是 **micro-F1**（全局 TP/FP/FN 汇总后算 P/R/F1）。\n\n**修复方案**：\n\n1. 在 `compute_instance_metrics()` 中，除了返回 per-instance F1，还要返回 raw TP/FP/FN counts：\n   ```python\n   # 在 compute_prf 之外加一个函数或修改返回值\n   greedy_ents = entity_set(greedy_parsed)\n   tp = len(greedy_ents & gold)\n   fp = len(greedy_ents - gold)\n   fn = len(gold - greedy_ents)\n   ```\n   对 greedy 和每个 MV threshold 都返回 tp/fp/fn。\n\n2. 在 `aggregate_model_results()` 中，汇总所有 instance 的 TP/FP/FN，计算 micro-F1：\n   ```python\n   total_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n   total_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n   total_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n   micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0\n   micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0\n   micro_f1 = 2*micro_p*micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0\n   ```\n\n3. **同时保留 macro-F1 和 micro-F1**（方便分析），但主要报告 micro-F1。对 greedy、每个 MV threshold、oracle 都要计算 micro 版本。\n\n4. `selection_gap` 应基于 micro-F1 计算（best_mv_micro_f1 - greedy_micro_f1）。\n\n### 运行步骤\n\n1. **先修 bug**：编辑本地文件修复 micro-F1。\n\n2. **测试 API 连通性**：\n   ```bash\n   export OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\"\n   cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc\n   python -c \"\n   from openai import OpenAI\n   c = OpenAI(base_url='http://47.94.22.126/v1', api_key='[REDACTED]')\n   r = c.chat.completions.create(model='openai/gpt-5.5', messages=[{'role':'user','content':'Hi'}], max_tokens=5)\n   print(r.choices[0].message.content)\n   \"\n   ```\n\n3. **正式运行**（使用 --from-hf 加载数据）：\n   ```bash\n   export OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\"\n   python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 \\\n       --temperature 1.0 --seed 42 --output-dir ./output\n   ```\n   预计 ~1-2h（3600 API calls，两个模型串行）。有 checkpoint 支持断点续跑。\n\n4. **收集结果**：\n   - 每个模型的 greedy micro-F1, best MV micro-F1, oracle micro-F1\n   - Selection gap (micro-F1)\n   - Degeneracy rate\n   - Correlation (agreement ↔ F1)\n   - Cross-model comparison table\n   - Failure mode diagnosis\n\n5. **更新 registry**：\n   - status → DONE\n   - conclusion: 基于 correlation-selection gap 是否在 frontier models 上持续存在\n   - metrics: 包含 micro-F1 和 macro-F1 两套指标\n   - checkpoint_path, log_path\n\n**环境**：本地运行（CPU + API）。需要 `pip install openai datasets numpy scipy`。\n",
      "task_prompt": "&lt;project_context>\n# 项目: struct_self_consist_ie\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：修复 HumanEval SC 代码 bug 并在本地 nohup 运行\n\n### 背景\nexp_a2_humaneval_sc 之前 Worker 因 5 分钟超时失败（实验需要 30-60 min API 调用）。Director 要求修复两个 bug 后重跑。\n\n### Bug 1: api_sample_greedy() temperature\n文件：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`\n\n在 `api_sample_greedy()` 函数中，temperature 设为 1.0。greedy 解码应该用 temperature=0.0（或非常小的值）。\n找到 `temperature=1.0` 在 greedy 函数中的位置，改为 `temperature=0.0`。\n\n### Bug 2: MV metric（验证是否存在）\n检查 `evaluate()` 函数中的 majority voting 计算。正确行为：\n- 在所有 N 个 samples 中投票（不限于 passing samples）\n- 选出最高票的代码\n- 检查该代码是否 pass tests\n- MV pass rate = 通过的 problems / 总 problems\n\n如果代码已经是这个逻辑（投票在 all_codes 上而非 passing_codes），则不需要修复。\n如果代码只在 passing solutions 中投票，需要修复。\n\n### 运行\n修复后，在本地用 nohup 运行（这是 CPU+API 实验，不需要 GPU）：\n\n```bash\ncd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/\n\n# 设置 API key\nexport OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\"\n\n# 先 dry-run 测试 API 连通性\npython run_humaneval_sc.py --test_api --n_samples 1 --output_dir ./results_test 2>&1 | head -20\n\n# 如果 API 连通，正式运行（nohup 后台）\nnohup python run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results --test_api > humaneval_sc.log 2>&1 &\necho \"PID: $!\"\n```\n\n注意：\n- 有 checkpoint 机制，之前跑了 1/164 problems，会自动恢复\n- 但如果之前的 results/checkpoint.jsonl 是 bug 版本的输出，需要清除后重跑：`rm -f ./results/checkpoint.jsonl`\n- API base URL: http://47.94.22.126/v1, model: openai/gpt-5.5\n- 预计运行 30-60 分钟\n\n### 产出\n1. 修复的代码文件\n2. nohup PID\n3. 确认 API 连通性\n4. 用 update_registry 更新 exp_a2_humaneval_sc status 和 spec（command, server=local, pid）",
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "902b8974-168f-4902-a0bb-83ed2eed9db8",
  "tool_use_result": {
    "stdout": "      \"task_prompt\": \"&lt;project_context>\\n# 项目: struct_self_consist_ie\\n\\n## 运行环境\\n- 服务器名: autodl-5090\\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\\\"root\\\"）\\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\\n\\n## ⚠️ 活跃约束（必须遵守）\\n\\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\\n\\n\\n## 环境搭建\\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\\n\\n## 输出风格\\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\\n&lt;/project_context>\\n## 任务：编写 HumanEval SC pilot 实验代码\\n\\n### 背景\\nCross-task universality 扩展：验证 SC failure modes 在 code generation 上的表现。Code 有确定性验证（unit tests），与 NER 不同。\\n\\n### 实验设计\\n\\n- **模型**: GPT-5.5 via OpenRouter API\\n- **API**: base_url=http://47.94.22.126/v1, model name 需要确认（可能是 \\\"openai/gpt-5.5\\\" 或类似格式）\\n- **数据**: HumanEval 164 problems\\n- **采样**: N=8, T=1.0\\n- **评估**: 生成 8 个 code solutions → 执行 unit test → pass@1\\n- **对比**: greedy vs MV（多数 test-passing solutions 投票）vs random selection\\n- **诊断**: degeneracy rate、agreement patterns\\n- **CPU-only**（API 调用 + local test execution）\\n\\n### 你要做的\\n\\n1. **编写脚本 `run_humaneval_sc.py`**（写到本地 `artifacts/experiments/humaneval_sc/run_humaneval_sc.py`）:\\n\\n   核心流程:\\n   ```\\n   a) load_humaneval(): 从 HuggingFace 加载 HumanEval dataset\\n      from datasets import load_dataset\\n      ds = load_dataset(\\\"openai/openai_humaneval\\\", split=\\\"test\\\")\\n   \\n   b) build_prompts(): 构建 code completion prompt\\n      使用 HumanEval 标准 prompt format\\n   \\n   c) api_sample(): 调 OpenRouter API, N=8, T=1.0\\n      - 使用 openai SDK: \\n        from openai import OpenAI\\n        client = OpenAI(base_url=\\\"http://47.94.22.126/v1\\\", api_key=[REDACTED]\"OPENROUTER_API_KEY\\\"])\\n        response = client.chat.completions.create(model=\\\"openai/gpt-5.5\\\", messages=[...], n=8, temperature=1.0)\\n      - 注意 rate limiting, 加 retry + backoff\\n      - 先用 1 个 problem 测试 API 连通性\\n   \\n   d) execute_tests(): 对每个 solution 执行 HumanEval unit tests\\n      - 使用 subprocess with timeout (30s per test)\\n      - 记录 pass/fail\\n      - ⚠️ 安全: 在 sandbox 中执行（限制 imports, timeout）\\n   \\n   e) evaluate():\\n      - greedy: 第一个 sample 的 pass rate\\n      - MV: 多数 test-passing solutions 中选一个\\n      - pass@k: 标准 pass@1, pass@8 计算\\n      - random: 随机选一个 sample 的 pass rate\\n   \\n   f) diagnose():\\n      - degeneracy: 8 个 solutions 完全相同的比例\\n      - agreement: 多数一致 solutions 是否 test-passing\\n      - execution agreement: 相同 output 的 solutions 分组\\n   \\n   g) save_results()\\n   ```\\n\\n2. **API key 处理**:\\n   - 脚本从环境变量 `OPENROUTER_API_KEY` 读取\\n   - API key 正在审批中，先写代码，key 到了再运行\\n   - 先用 WebSearch 确认 OpenRouter 上 GPT-5.5 的 model ID 格式\\n\\n3. **HumanEval test execution**:\\n   - 使用标准 HumanEval evaluation harness\\n   - 或自己实现 safe execution（exec() with restricted globals + timeout）\\n   - 参考 human-eval package: `pip install human-eval`\\n\\n4. **更新 registry spec**:\\n   - exp_id: exp_a2_humaneval_sc\\n   - command, data_count=164, model_name=\\\"GPT-5.5 (OpenRouter)\\\", seed=42\\n\\n5. **产出报告**: 代码路径、依赖列表、API cost 估算、预计时长。\\n\\n### 注意\\n- CPU-only 实验，不需要 GPU\\n- API key 待审批，先写代码\\n- HumanEval test execution 需要安全 sandbox\\n- 不要等结果，代码就绪即完成\\n- 先用 WebSearch 确认 OpenRouter GPT-5.5 model ID\\n\",\n      \"task_prompt\": \"&lt;project_context>\\n# 项目: struct_self_consist_ie\\n\\n## 运行环境\\n- 服务器名: autodl-5090\\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\\\"root\\\"）\\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\\n\\n## ⚠️ 活跃约束（必须遵守）\\n\\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\\n\\n\\n## 环境搭建\\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\\n\\n## 输出风格\\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\\n&lt;/project_context>\\n## 任务：编写 Frontier Model SC on FewNERD 实验代码\\n\\n### 背景\\n验证 correlation-selection gap 在 frontier 模型上是否依然存在。如果 frontier 模型也有同样的 gap，说明这是 LLM SC 的 fundamental limit 而非 capability limitation。\\n\\n### 实验设计\\n\\n- **模型**: GPT-5.5 + Claude Opus 4.6（通过 OpenRouter API）\\n- **API**: base_url=http://47.94.22.126/v1\\n- **数据**: FewNERD test set 随机 200 instances（seed=42）\\n- **采样**: N=8, T=1.0\\n- **不需要 logprob**——只统计 frequency-based agreement（每个 entity 在 8 个 sample 中出现几次）\\n- **对比**: greedy vs MV，记录 correlation-selection gap\\n- **输出**: per-model F1 表 + failure mode 分布\\n- **CPU-only**（API 调用）\\n- **预估 cost**: ~$50-100，~4-6h\\n\\n### 你要做的\\n\\n1. **编写脚本 `run_frontier_sc.py`**（写到本地 `artifacts/experiments/frontier_sc/run_frontier_sc.py`）:\\n\\n   核心流程:\\n   ```\\n   a) load_fewnerd_subset(): 从项目数据加载 FewNERD test, random sample 200 instances\\n      - FewNERD data 在服务器上: /root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\\n      - 但这个脚本要在本地/CPU 跑，所以需要能本地读取数据\\n      - 或者从 HuggingFace 加载 FewNERD\\n   \\n   b) build_ner_prompt(): 构建 NER prompt（与项目标准 template 一致）\\n      - 参考项目的 UIE JSON schema\\n      - Entity types: person, organization, location, building, art, product, event, other\\n   \\n   c) api_sample(): 调 OpenRouter API\\n      - 使用 openai SDK:\\n        client = OpenAI(base_url=\\\"http://47.94.22.126/v1\\\", api_key=[REDACTED]\"OPENROUTER_API_KEY\\\"])\\n      - GPT-5.5: model=\\\"openai/gpt-5.5\\\"（需确认 OpenRouter model ID）\\n      - Claude Opus 4.6: model=\\\"anthropic/claude-opus-4-6\\\"（需确认）\\n      - N=8, T=1.0\\n      - JSON mode / structured output（如支持的话）\\n      - Rate limiting: retry + exponential backoff\\n      - 每个 model × 200 instances × 8 samples = 1600 API calls per model\\n   \\n   d) parse_responses(): 解析 JSON 输出，提取 entities\\n      - 容错处理: 部分 response 可能不是 valid JSON\\n      - Normalize entity format: (text, type, start, end)\\n   \\n   e) evaluate():\\n      - greedy F1: 第一个 sample vs gold\\n      - MV F1: majority vote construction vs gold\\n      - entity-level agreement: 每个 entity 在 8 samples 中出现的次数\\n      - correlation: agreement score vs instance F1 的 Spearman correlation\\n      - selection gap: MV F1 - greedy F1\\n   \\n   f) diagnose():\\n      - degeneracy rate: 8 个 entity sets 完全相同的比例\\n      - agreement-correctness correlation\\n      - per-model comparison\\n   \\n   g) save_results(): JSON output + summary\\n   ```\\n\\n2. **API key 处理**:\\n   - 从环境变量 `OPENROUTER_API_KEY` 读取\\n   - API key 正在审批中，先写代码\\n   - 先用 WebSearch 确认 OpenRouter 上 GPT-5.5 和 Claude Opus 4.6 的 model ID\\n\\n3. **FewNERD 数据**:\\n   - 需要在本地或 CPU 服务器上可用\\n   - 检查本地项目目录是否有 FewNERD data\\n   - 如果没有，从 HuggingFace 下载或从服务器 scp\\n\\n4. **Cost estimation**:\\n   - 200 instances × 8 samples × 2 models = 3200 API calls\\n   - 估算每个 call 的 token 数（prompt ~500 tokens + response ~200 tokens）\\n   - 计算总 cost\\n\\n5. **更新 registry spec**:\\n   - exp_id: exp_b_frontier_sc_fewnerd\\n   - command, data_count=200, model_name=\\\"GPT-5.5 + Claude Opus 4.6\\\", seed=42\\n\\n6. **产出报告**: 代码路径、API model IDs、cost 估算、依赖列表。\\n\\n### 注意\\n- CPU-only 实验\\n- API key 待审批\\n- 不需要 logprob\\n- 不要等结果，代码就绪即完成\\n- 先用 WebSearch 确认 OpenRouter model IDs\\n\",\n      \"task_prompt\": \"&lt;project_context>\\n# 项目: struct_self_consist_ie\\n\\n## 运行环境\\n- 服务器名: autodl-5090\\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\\\"root\\\"）\\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\\n\\n## ⚠️ 活跃约束（必须遵守）\\n\\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\\n\\n\\n## 环境搭建\\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\\n\\n## 输出风格\\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\\n&lt;/project_context>\\n## 任务：修复 MV metric bug 并运行 HumanEval SC 实验\\n\\n**目标**：修复 run_humaneval_sc.py 的 MV 投票 bug，然后运行实验。\\n\\n**exp_id**: `exp_a2_humaneval_sc`\\n**类型**: CPU + OpenRouter API\\n**API Key**: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`\\n**API Base**: `http://47.94.22.126/v1`\\n**Model**: `openai/gpt-5.5`\\n\\n### Bug 描述（必须先修再跑）\\n\\n文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`\\n\\n`evaluate()` 函数 (约 L233-246) 的 MV 实现有 bug：\\n\\n```python\\npassing_codes = [s[\\\"code\\\"] for s in r[\\\"sample_results\\\"] if s[\\\"passed\\\"]]\\nif not passing_codes:\\n    continue\\nmv_applicable += 1\\ncode_counts = Counter(passing_codes)\\nmajority_code = code_counts.most_common(1)[0][0]\\nmv_correct += 1  # BUG: 从 passing codes 里投票，结果 trivially 全对\\n```\\n\\n**问题**：MV 只在 passing solutions 中投票，所以 majority-voted code 必然 pass（by construction）。这使得 `mv_pass_rate == oracle_pass_rate`，指标无意义。\\n\\n**修复方案**：MV 应该在 **所有 N 个 solution** 中按文本投票，选出 majority code，然后检查这个 code 是否 pass tests：\\n\\n```python\\n# 正确的 MV: 在所有 solutions 中投票\\nall_codes = [s[\\\"code\\\"] for s in r[\\\"sample_results\\\"]]\\ncode_counts = Counter(all_codes)\\nmajority_code = code_counts.most_common(1)[0][0]\\n# 检查 majority code 是否通过测试\\nmajority_passed = any(\\n    s[\\\"passed\\\"] for s in r[\\\"sample_results\\\"] if s[\\\"code\\\"] == majority_code\\n)\\nif majority_passed:\\n    mv_correct += 1\\n```\\n\\n### 运行步骤\\n\\n1. **先修 bug**：编辑本地文件 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`，修复 `evaluate()` 中的 MV 逻辑。\\n\\n2. **测试 API 连通性**：\\n   ```bash\\n   export OPENROUTER_API_KEY=[REDACTED]\"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\\\"\\n   cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc\\n   python run_humaneval_sc.py --test_api --n_samples 1 --output_dir ./test_output\\n   ```\\n   验证 API 可达。如果失败，检查网络/key。\\n\\n3. **正式运行**：\\n   ```bash\\n   export OPENROUTER_API_KEY=[REDACTED]\"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\\\"\\n   python run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 \\\\\\n       --output_dir ./results --test_api\\n   ```\\n   预计 30-60 min，有 checkpoint 支持断点续跑。\\n\\n4. **收集结果**：\\n   - greedy pass rate, pass@1, pass@8\\n   - MV pass rate (修复后的)\\n   - random pass rate, oracle pass rate\\n   - degeneracy rate, majority agreement rate\\n   - MV vs greedy 的 gap\\n\\n5. **更新 registry**：\\n   - status → DONE\\n   - conclusion: 基于 correlation-selection gap 是否存在\\n   - metrics: 所有指标\\n   - checkpoint_path, log_path\\n\\n**环境**：本地运行即可（CPU + API），不需要 SSH 到服务器。需要 `pip install openai datasets numpy`。\\n\",\n      \"task_prompt\": \"&lt;project_context>\\n# 项目: struct_self_consist_ie\\n\\n## 运行环境\\n- 服务器名: autodl-5090\\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\\\"root\\\"）\\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\\n\\n## ⚠️ 活跃约束（必须遵守）\\n\\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\\n\\n\\n## 环境搭建\\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\\n\\n## 输出风格\\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\\n&lt;/project_context>\\n## 任务：修复 micro-F1 并运行 Frontier SC 实验\\n\\n**目标**：修复 run_frontier_sc.py 的评估指标（macro-F1 → micro-F1），然后运行实验。\\n\\n**exp_id**: `exp_b_frontier_sc_fewnerd`\\n**类型**: CPU + OpenRouter API\\n**API Key**: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`\\n**API Base**: `http://47.94.22.126/v1`\\n**Models**: GPT-5.5 (`openai/gpt-5.5`) + Claude Opus 4.6 (`anthropic/claude-opus-4.6`)\\n\\n### Bug 描述（必须先修再跑）\\n\\n文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py`\\n\\n`aggregate_model_results()` 函数 (约 L396-451) 使用 **macro-F1**（per-instance F1 平均），但 NER 标准是 **micro-F1**（全局 TP/FP/FN 汇总后算 P/R/F1）。\\n\\n**修复方案**：\\n\\n1. 在 `compute_instance_metrics()` 中，除了返回 per-instance F1，还要返回 raw TP/FP/FN counts：\\n   ```python\\n   # 在 compute_prf 之外加一个函数或修改返回值\\n   greedy_ents = entity_set(greedy_parsed)\\n   tp = len(greedy_ents & gold)\\n   fp = len(greedy_ents - gold)\\n   fn = len(gold - greedy_ents)\\n   ```\\n   对 greedy 和每个 MV threshold 都返回 tp/fp/fn。\\n\\n2. 在 `aggregate_model_results()` 中，汇总所有 instance 的 TP/FP/FN，计算 micro-F1：\\n   ```python\\n   total_tp = sum(r[\\\"metrics\\\"][\\\"greedy_tp\\\"] for r in results)\\n   total_fp = sum(r[\\\"metrics\\\"][\\\"greedy_fp\\\"] for r in results)\\n   total_fn = sum(r[\\\"metrics\\\"][\\\"greedy_fn\\\"] for r in results)\\n   micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0\\n   micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0\\n   micro_f1 = 2*micro_p*micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0\\n   ```\\n\\n3. **同时保留 macro-F1 和 micro-F1**（方便分析），但主要报告 micro-F1。对 greedy、每个 MV threshold、oracle 都要计算 micro 版本。\\n\\n4. `selection_gap` 应基于 micro-F1 计算（best_mv_micro_f1 - greedy_micro_f1）。\\n\\n### 运行步骤\\n\\n1. **先修 bug**：编辑本地文件修复 micro-F1。\\n\\n2. **测试 API 连通性**：\\n   ```bash\\n   export OPENROUTER_API_KEY=[REDACTED]\"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\\\"\\n   cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc\\n   python -c \\\"\\n   from openai import OpenAI\\n   c = OpenAI(base_url='http://47.94.22.126/v1', api_key='[REDACTED]')\\n   r = c.chat.completions.create(model='openai/gpt-5.5', messages=[{'role':'user','content':'Hi'}], max_tokens=5)\\n   print(r.choices[0].message.content)\\n   \\\"\\n   ```\\n\\n3. **正式运行**（使用 --from-hf 加载数据）：\\n   ```bash\\n   export OPENROUTER_API_KEY=[REDACTED]\"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\\\"\\n   python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 \\\\\\n       --temperature 1.0 --seed 42 --output-dir ./output\\n   ```\\n   预计 ~1-2h（3600 API calls，两个模型串行）。有 checkpoint 支持断点续跑。\\n\\n4. **收集结果**：\\n   - 每个模型的 greedy micro-F1, best MV micro-F1, oracle micro-F1\\n   - Selection gap (micro-F1)\\n   - Degeneracy rate\\n   - Correlation (agreement ↔ F1)\\n   - Cross-model comparison table\\n   - Failure mode diagnosis\\n\\n5. **更新 registry**：\\n   - status → DONE\\n   - conclusion: 基于 correlation-selection gap 是否在 frontier models 上持续存在\\n   - metrics: 包含 micro-F1 和 macro-F1 两套指标\\n   - checkpoint_path, log_path\\n\\n**环境**：本地运行（CPU + API）。需要 `pip install openai datasets numpy scipy`。\\n\",\n      \"task_prompt\": \"&lt;project_context>\\n# 项目: struct_self_consist_ie\\n\\n## 运行环境\\n- 服务器名: autodl-5090\\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\\\"root\\\"）\\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\\n- 项目代码根目录: /root/autodl-tmp/struct_self_consist_ie\\n\\n## ⚠️ 活跃约束（必须遵守）\\n\\n- **C001**: 论文 tex 文件只能修改 docs/paper/sections/ 下的编译版本，禁止直接修改 artifacts/_project/paper/ 下的 tex 文件（原因：两次出现 Worker 修改 artifacts/ 旧版本而非 docs/ 编译版本的系统性错误（patch-narrative worker + patch-experiments worker）。artifacts/_project/paper/ 是旧版残留，不参与编译。）\\n\\n\\n## 环境搭建\\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\\n\\n## 输出风格\\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\\n&lt;/project_context>\\n## 任务：修复 HumanEval SC 代码 bug 并在本地 nohup 运行\\n\\n### 背景\\nexp_a2_humaneval_sc 之前 Worker 因 5 分钟超时失败（实验需要 30-60 min API 调用）。Director 要求修复两个 bug 后重跑。\\n\\n### Bug 1: api_sample_greedy() temperature\\n文件：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py`\\n\\n在 `api_sample_greedy()` 函数中，temperature 设为 1.0。greedy 解码应该用 temperature=0.0（或非常小的值）。\\n找到 `temperature=1.0` 在 greedy 函数中的位置，改为 `temperature=0.0`。\\n\\n### Bug 2: MV metric（验证是否存在）\\n检查 `evaluate()` 函数中的 majority voting 计算。正确行为：\\n- 在所有 N 个 samples 中投票（不限于 passing samples）\\n- 选出最高票的代码\\n- 检查该代码是否 pass tests\\n- MV pass rate = 通过的 problems / 总 problems\\n\\n如果代码已经是这个逻辑（投票在 all_codes 上而非 passing_codes），则不需要修复。\\n如果代码只在 passing solutions 中投票，需要修复。\\n\\n### 运行\\n修复后，在本地用 nohup 运行（这是 CPU+API 实验，不需要 GPU）：\\n\\n```bash\\ncd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/\\n\\n# 设置 API key\\nexport OPENROUTER_API_KEY=[REDACTED]\"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\\\"\\n\\n# 先 dry-run 测试 API 连通性\\npython run_humaneval_sc.py --test_api --n_samples 1 --output_dir ./results_test 2>&1 | head -20\\n\\n# 如果 API 连通，正式运行（nohup 后台）\\nnohup python run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results --test_api > humaneval_sc.log 2>&1 &\\necho \\\"PID: $!\\\"\\n```\\n\\n注意：\\n- 有 checkpoint 机制，之前跑了 1/164 problems，会自动恢复\\n- 但如果之前的 results/checkpoint.jsonl 是 bug 版本的输出，需要清除后重跑：`rm -f ./results/checkpoint.jsonl`\\n- API base URL: http://47.94.22.126/v1, model: openai/gpt-5.5\\n- 预计运行 30-60 分钟\\n\\n### 产出\\n1. 修复的代码文件\\n2. nohup PID\\n3. 确认 API 连通性\\n4. 用 update_registry 更新 exp_a2_humaneval_sc status 和 spec（command, server=local, pid）\",",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
````

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
I found the API key in the worker logs: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`. But the task says this API key has exhausted its balance ("已耗尽余额的 API"). Let me also check if there is a different OPENROUTER_API_KEY set somewhere.

Wait, re-reading the task: "代码中 `API_BASE_URL = "http://47.94.22.126/v1"` 是已耗尽余额的 API" - this is about the base URL, not necessarily about the API key itself. 

The task wants me to switch to OpenRouter at `https://openrouter.ai/api/v1` and use the OPENROUTER_API_KEY environment variable. Let me check if that's actually set in the environment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "005e7d9e-c86d-4789-9050-0502939f6dce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sip6PR2y7FRawu5atrQyyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9980,
      "cache_read_input_tokens": 37199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9980
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

_source line 31_

找到了之前使用的 API key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，但任务说这个 API base (`47.94.22.126`) 已耗尽余额。需要确认是否有 OpenRouter 原生的 API key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "dcbc43ab-de69-4d20-b6cb-30ef0524de8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sip6PR2y7FRawu5atrQyyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9980,
      "cache_read_input_tokens": 37199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9980
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

<details open><summary>🔧 Tool call — Bash · `toolu_01XQ1rN1VnsWdXfBRoczs6Lk`</summary>

```json
{
  "command": "grep -rn \"OPENROUTER_API_KEY\\|sk-or-\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ --include=\"*.env\" --include=\"*.md\" --include=\"*.sh\" 2>/dev/null | grep -v \".log\" | head -10",
  "description": "Search for OpenRouter API key"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "939f47e7-22e1-410d-9bb8-cd77f24c06af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sip6PR2y7FRawu5atrQyyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9980,
      "cache_read_input_tokens": 37199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9980
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

_source line 33 · 2026-05-20T22:06:36.066Z_

<details><summary>↩ Tool result · `toolu_01XQ1rN1VnsWdXfBRoczs6Lk`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "77127f98-9132-4307-b3d8-bd2cab859ffb",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01KicZmoX5GV5EahnqVKrAWL`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md 2>/dev/null | grep -B2 -A5 -i \"openrouter\\|api.*key\\|余额\"",
  "description": "Check memory.md for API info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "6b1b21af-32cb-4f10-8b35-e34fe40dd959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sip6PR2y7FRawu5atrQyyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9980,
      "cache_read_input_tokens": 37199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9980
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

_source line 35 · 2026-05-20T22:06:37.438Z_

<details><summary>↩ Tool result · `toolu_01KicZmoX5GV5EahnqVKrAWL`</summary>

```text
根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel。**教训：LLaMA-Factory 训练配置中加 `report_to: wandb`。** 遇到 "process dead + no W&B" 失败时，优先检查日志尾部是否有正常完成的 train/eval metrics。

## OpenRouter API 限制（2026-05-20）

- Base URL: `http://47.94.22.126/v1`（TUM 代理）
- GPT-5.5 只支持 temperature=1.0，设 0.0 返回 HTTP 400
- HumanEval greedy baseline 只能用 single-sample T=1.0，非真正 T=0 greedy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "ee0f8ce9-77d5-46b6-ad9b-7176c26fb986",
  "tool_use_result": {
    "stdout": "根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel。**教训：LLaMA-Factory 训练配置中加 `report_to: wandb`。** 遇到 \"process dead + no W&B\" 失败时，优先检查日志尾部是否有正常完成的 train/eval metrics。\n\n## OpenRouter API 限制（2026-05-20）\n\n- Base URL: `http://47.94.22.126/v1`（TUM 代理）\n- GPT-5.5 只支持 temperature=1.0，设 0.0 返回 HTTP 400\n- HumanEval greedy baseline 只能用 single-sample T=1.0，非真正 T=0 greedy",
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

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
The task says to use `--api-base https://openrouter.ai/api/v1` but I need an OPENROUTER_API_KEY. The old key was `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8` but that was for the TUM proxy. For OpenRouter directly, we'd need a different key format (usually `sk-or-...`).

Wait, let me re-read the task instructions more carefully:

"3. 

I need to check if the OPENROUTER_API_KEY environment variable is set, and if not, look through the .env file or memory.md for any stored keys. The old TUM proxy key won't work with the OpenRouter API directly, so if there's no valid key available, I should stop and report that rather than continuing. The TUM proxy key with the `tum_` prefix won't work with OpenRouter directly since they're separate systems—OpenRouter uses `sk-or-` prefixed keys. Since I don't have a valid OpenRouter API key in the environment and the task explicitly says to stop and report if no key exists, I should report this issue rather than attempt to use an incompatible key. I need to work through the steps in order: fix the bugs first, then check for the API key and report if it's missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "3ccddf52-e2b4-45a9-bb0f-70b80275900d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP5sThL63YSUecWSTZJGFL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 47179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

_source line 37_

旧进程已死，无 checkpoint。现在修复 3 个 bug。

**Bug 1**: `entity_set()` 传参错误 — 传了完整 parsed dict 而非 `entities` 列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "c2a0866c-9c4d-406f-b3bf-2dd6e71fdd69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP5sThL63YSUecWSTZJGFL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 47179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01DFBKL3AJ8QV8Cin9RAShaR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "old_string": "    # Greedy\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)",
  "new_string": "    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "edc4b797-1795-4521-a32d-716284a4e4c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP5sThL63YSUecWSTZJGFL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 47179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 935
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

_source line 39 · 2026-05-20T22:07:06.667Z_

<details><summary>↩ Tool result · `toolu_01DFBKL3AJ8QV8Cin9RAShaR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "2cdc6dd4-7c91-49b7-8cd3-44928b1f8999",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "oldString": "    # Greedy\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)",
    "newString": "    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 387,
        "oldLines": 7,
        "newStart": 387,
        "newLines": 7,
        "lines": [
          "     gold = entity_set(gold_entities)",
          " ",
          "     # Greedy",
          "-    greedy_ents = entity_set(greedy_parsed)",
          "+    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))",
          "     g_p, g_r, g_f = compute_prf(greedy_ents, gold)",
          "     g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)",
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_013qthXwgNb3ASaS5Ehdk2BT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "old_string": "        _, _, f = compute_prf(entity_set(s), gold)",
  "new_string": "        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "5dc1e4fe-3bf0-4d93-98fc-d312bc94821a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vAiqqvg5aAUfvmLWsnxZj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1387,
      "cache_read_input_tokens": 48114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1387
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

_source line 41 · 2026-05-20T22:07:10.258Z_

<details><summary>↩ Tool result · `toolu_013qthXwgNb3ASaS5Ehdk2BT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "2cd72058-89a5-4ec7-bc84-09c78c817c60",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "oldString": "        _, _, f = compute_prf(entity_set(s), gold)",
    "newString": "        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 394,
        "oldLines": 7,
        "newStart": 394,
        "newLines": 7,
        "lines": [
          "     # Per-sample F1",
          "     sample_f1s = []",
          "     for s in sc_parsed:",
          "-        _, _, f = compute_prf(entity_set(s), gold)",
          "+        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)",
          "         sample_f1s.append(f)",
          " ",
          "     # MV at multiple thresholds"
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01NZLvJmX37KrPkjWmtSWk6e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "old_string": "    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]",
  "new_string": "    sample_sets = [frozenset(entity_set(s.get(\"entities\", []))) for s in sc_parsed]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "8f880b06-8f96-433b-a747-17370dde0848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLzSc2HgBauk1cg4DKqYG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 49501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
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

_source line 43 · 2026-05-20T22:07:14.745Z_

<details><summary>↩ Tool result · `toolu_01NZLvJmX37KrPkjWmtSWk6e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "2e636c83-e14f-4d08-a95a-1b42ab8eebbb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "oldString": "    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]",
    "newString": "    sample_sets = [frozenset(entity_set(s.get(\"entities\", []))) for s in sc_parsed]",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 419,
        "oldLines": 7,
        "newStart": 419,
        "newLines": 7,
        "lines": [
          "     mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0",
          " ",
          "     # Degeneracy: all sample entity sets identical",
          "-    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]",
          "+    sample_sets = [frozenset(entity_set(s.get(\"entities\", []))) for s in sc_parsed]",
          "     is_degenerate = len(set(sample_sets)) == 1",
          " ",
          "     # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)"
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

_source line 44_

**Bug 2**: JSON 嵌套字符串容错。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "1cda9cf6-0bbd-464c-a511-cabde10e50a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaXmSCtCWKzmtrDttYfJPf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 49756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 267
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_019ny9gk8y1XpWzFFaYSpe45`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "old_string": "    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):",
  "new_string": "    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if isinstance(data, str):\n        try:\n            data = json.loads(data)\n        except (json.JSONDecodeError, TypeError):\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    ent_field = data.get(\"entities\", [])\n    if isinstance(ent_field, str):\n        try:\n            ent_field = json.loads(ent_field)\n        except (json.JSONDecodeError, TypeError):\n            ent_field = []\n\n    entities = []\n    for e in ent_field:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "56d358d6-fdaf-44ba-990c-749944357c42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaXmSCtCWKzmtrDttYfJPf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 49756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 267
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

_source line 46 · 2026-05-20T22:07:23.255Z_

<details><summary>↩ Tool result · `toolu_019ny9gk8y1XpWzFFaYSpe45`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "5a5e8d8c-4f75-49d2-b280-142dc02d5c3a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "oldString": "    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):",
    "newString": "    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if isinstance(data, str):\n        try:\n            data = json.loads(data)\n        except (json.JSONDecodeError, TypeError):\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    ent_field = data.get(\"entities\", [])\n    if isinstance(ent_field, str):\n        try:\n            ent_field = json.loads(ent_field)\n        except (json.JSONDecodeError, TypeError):\n            ent_field = []\n\n    entities = []\n    for e in ent_field:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s.get(\"entities\", []))) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 312,
        "oldLines": 11,
        "newStart": 312,
        "newLines": 24,
        "lines": [
          "         else:",
          "             return {\"entities\": [], \"relations\": [], \"events\": []}",
          " ",
          "+    if isinstance(data, str):",
          "+        try:",
          "+            data = json.loads(data)",
          "+        except (json.JSONDecodeError, TypeError):",
          "+            return {\"entities\": [], \"relations\": [], \"events\": []}",
          "+",
          "     if not isinstance(data, dict):",
          "         return {\"entities\": [], \"relations\": [], \"events\": []}",
          " ",
          "+    ent_field = data.get(\"entities\", [])",
          "+    if isinstance(ent_field, str):",
          "+        try:",
          "+            ent_field = json.loads(ent_field)",
          "+        except (json.JSONDecodeError, TypeError):",
          "+            ent_field = []",
          "+",
          "     entities = []",
          "-    for e in data.get(\"entities\", []):",
          "+    for e in ent_field:",
          "         if not isinstance(e, dict):",
          "             continue",
          "         try:"
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

_source line 47_

**Bug 3**: API Base URL 默认值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "8b065ee2-d1a3-421d-8d4e-acdf259f4b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZws38Vz2mBvUoxKsTWcwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 50023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 813
      },
      "output_tokens": 6,
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01FXUVZLUkGceVnfXDvzxkZA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "old_string": "API_BASE_URL = \"http://47.94.22.126/v1\"",
  "new_string": "API_BASE_URL = \"https://openrouter.ai/api/v1\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "f9e05d9c-76df-4bfb-83d6-900bd1714cfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZws38Vz2mBvUoxKsTWcwV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 50023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 813
      },
      "output_tokens": 6,
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

_source line 49 · 2026-05-20T22:07:33.886Z_

<details><summary>↩ Tool result · `toolu_01FXUVZLUkGceVnfXDvzxkZA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "312799ec-f2d0-49ad-8db5-00a00e7db08a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "oldString": "API_BASE_URL = \"http://47.94.22.126/v1\"",
    "newString": "API_BASE_URL = \"https://openrouter.ai/api/v1\"",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert tagged tokens to entity spans with char offsets.\n\n    Supports both BIO format (B-type/I-type) and flat format (type name only,\n    as in DFKI-SLT/few-nerd coarse ner_tags).\n    \"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    has_bio = any(t.startswith(\"B-\") or t.startswith(\"I-\") for t in tag_names if t != \"O\")\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if has_bio:\n            if tag.startswith(\"B-\"):\n                if current is not None:\n                    entities.append(current)\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                current = {\n                    \"text\": tokens[i],\n                    \"type\": coarse,\n                    \"start\": offsets[i][0],\n                    \"end\": offsets[i][1],\n                }\n            elif tag.startswith(\"I-\") and current is not None:\n                fine_type = tag[2:]\n                coarse = fine_type.split(\"-\")[0].lower()\n                if coarse == current[\"type\"]:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    entities.append(current)\n                    current = None\n            else:\n                if current is not None:\n                    entities.append(current)\n                    current = None\n        else:\n            # Flat tags: consecutive same-type tokens form one entity\n            if tag == \"O\":\n                if current is not None:\n                    entities.append(current)\n                    current = None\n            else:\n                etype = tag.lower()\n                if current is not None and current[\"type\"] == etype:\n                    current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                    current[\"end\"] = offsets[i][1]\n                else:\n                    if current is not None:\n                        entities.append(current)\n                    current = {\n                        \"text\": tokens[i],\n                        \"type\": etype,\n                        \"start\": offsets[i][0],\n                        \"end\": offsets[i][1],\n                    }\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            kwargs = dict(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            resp = client.chat.completions.create(**kwargs)\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            err_msg = str(e)\n            # Some models (e.g. GPT-5.5) only support temperature=1\n            if \"temperature\" in err_msg and \"unsupported\" in err_msg.lower():\n                log.warning(\"  Model %s does not support temperature=%.1f, retrying with temperature=1\",\n                            model_id, temperature)\n                try:\n                    kwargs[\"temperature\"] = 1.0\n                    resp = client.chat.completions.create(**kwargs)\n                    return resp.choices[0].message.content or \"{}\"\n                except Exception as e2:\n                    log.warning(\"  Retry also failed: %s\", e2)\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if isinstance(data, str):\n        try:\n            data = json.loads(data)\n        except (json.JSONDecodeError, TypeError):\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    ent_field = data.get(\"entities\", [])\n    if isinstance(ent_field, str):\n        try:\n            ent_field = json.loads(ent_field)\n        except (json.JSONDecodeError, TypeError):\n            ent_field = []\n\n    entities = []\n    for e in ent_field:\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef _count_tp_fp_fn(pred_set: set, gold_set: set) -> tuple[int, int, int]:\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    return tp, fp, fn\n\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy\n    greedy_ents = entity_set(greedy_parsed.get(\"entities\", []))\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n    g_tp, g_fp, g_fn = _count_tp_fp_fn(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s.get(\"entities\", [])), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_tp, mv_fp, mv_fn = _count_tp_fp_fn(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\n            \"p\": mv_p, \"r\": mv_r, \"f1\": mv_f,\n            \"tp\": mv_tp, \"fp\": mv_fp, \"fn\": mv_fn,\n        }\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s.get(\"entities\", []))) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N (per-instance, keep macro only — micro oracle is less meaningful)\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"greedy_tp\": g_tp,\n        \"greedy_fp\": g_fp,\n        \"greedy_fn\": g_fn,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef _micro_prf(total_tp: int, total_fp: int, total_fn: int) -> tuple[float, float, float]:\n    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0\n    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0\n    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0\n    return p, r, f\n\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # --- Micro-F1 (primary): aggregate TP/FP/FN across all instances ---\n    greedy_tp = sum(r[\"metrics\"][\"greedy_tp\"] for r in results)\n    greedy_fp = sum(r[\"metrics\"][\"greedy_fp\"] for r in results)\n    greedy_fn = sum(r[\"metrics\"][\"greedy_fn\"] for r in results)\n    greedy_micro_p, greedy_micro_r, greedy_micro_f1 = _micro_prf(greedy_tp, greedy_fp, greedy_fn)\n\n    # MV micro-F1 per threshold\n    mv_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        t_tp = sum(r[\"metrics\"][\"mv\"][tk][\"tp\"] for r in results)\n        t_fp = sum(r[\"metrics\"][\"mv\"][tk][\"fp\"] for r in results)\n        t_fn = sum(r[\"metrics\"][\"mv\"][tk][\"fn\"] for r in results)\n        mp, mr, mf = _micro_prf(t_tp, t_fp, t_fn)\n        # Also keep macro for reference\n        macro_f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_by_threshold[tk] = {\n            \"micro_p\": mp, \"micro_r\": mr, \"micro_f1\": mf,\n            \"macro_f1\": float(np.mean(macro_f1s)),\n            \"std_f1\": float(np.std(macro_f1s)),\n        }\n\n    # Best threshold by micro-F1\n    best_t = max(mv_by_threshold, key=lambda k: mv_by_threshold[k][\"micro_f1\"])\n    best_mv_micro_f1 = mv_by_threshold[best_t][\"micro_f1\"]\n\n    selection_gap = best_mv_micro_f1 - greedy_micro_f1\n\n    # --- Macro-F1 (secondary): per-instance F1 averaged ---\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        # Primary: micro-F1\n        \"greedy_micro\": {\"p\": greedy_micro_p, \"r\": greedy_micro_r, \"f1\": greedy_micro_f1},\n        \"best_mv_micro_f1\": best_mv_micro_f1,\n        \"selection_gap\": selection_gap,\n        # Secondary: macro-F1\n        \"greedy_f1\": {\"mean\": float(np.mean(greedy_f1s)), \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_by_threshold,\n        \"best_threshold\": best_t,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy_micro=%.4f, MV@0.5_micro=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_micro\"][\"f1\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"micro_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  [micro] Greedy F1: %.4f (P=%.4f R=%.4f)\",\n                 summary[\"greedy_micro\"][\"f1\"], summary[\"greedy_micro\"][\"p\"], summary[\"greedy_micro\"][\"r\"])\n        log.info(\"  [micro] Best MV F1: %.4f (threshold=%s)\", summary[\"best_mv_micro_f1\"], summary[\"best_threshold\"])\n        log.info(\"  [micro] Selection gap: %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  [macro] Greedy F1: %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  [macro] Oracle F1: %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep (micro-F1):\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"micro_f1\"] - summary[\"greedy_micro\"][\"f1\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  micro=%.4f  macro=%.4f  Δ=%+.4f%s\",\n                     t, mv[\"micro_f1\"], mv[\"macro_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %10s %10s %10s %10s %8s\",\n                 \"Model\", \"Greedy(μ)\", \"MV@best(μ)\", \"Oracle(M)\", \"Gap(μ)\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %10.4f %10.4f %10.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_micro\"][\"f1\"],\n                s[\"best_mv_micro_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 37,
        "oldLines": 7,
        "newStart": 37,
        "newLines": 7,
        "lines": [
          "     \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",",
          " }",
          " ",
          "-API_BASE_URL = \"http://47.94.22.126/v1\"",
          "+API_BASE_URL = \"https://openrouter.ai/api/v1\"",
          " ",
          " ENTITY_TYPES = {",
          "     \"person\": \"Person names\","
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

_source line 50_

3 个 bug 已修复。现在检查 OPENROUTER_API_KEY。

环境变量 `OPENROUTER_API_KEY` 为空。在 worker 日志中找到旧 key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，但这是 TUM 代理的 key（`http://47.94.22.126/v1`），任务说该代理已耗尽余额。OpenRouter 原生 key 通常以 `sk-or-` 开头。

**停止并报告**：没有可用的 OpenRouter API key。需要你提供一个有效的 `OPENROUTER_API_KEY`（格式 `sk-or-...`），或者确认旧的 TUM key 是否可以直接用于 `https://openrouter.ai/api/v1`。

### 已完成
- Bug 1 修复：`entity_set()` 传参改为 `.get("entities", [])`（3 处）
- Bug 2 修复：`parse_response()` 增加嵌套 JSON string 容错（data 和 entities 字段）
- Bug 3 修复：`API_BASE_URL` 默认值改为 `https://openrouter.ai/api/v1`
- 旧进程 PID 1509955 已死，无需 kill
- output 目录无 checkpoint（只有 instance_ids.json）

### 待提供
- 有效的 `OPENROUTER_API_KEY`，提供后可继续 smoke test 和全量实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "uuid": "c2f42e8c-704b-49ae-9e99-90183c255aa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Stz98em6vyiN7nLAouEVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 50836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 51_

3 个 bug 已修复。现在检查 OPENROUTER_API_KEY。

环境变量 `OPENROUTER_API_KEY` 为空。在 worker 日志中找到旧 key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，但这是 TUM 代理的 key（`http://47.94.22.126/v1`），任务说该代理已耗尽余额。OpenRouter 原生 key 通常以 `sk-or-` 开头。

**停止并报告**：没有可用的 OpenRouter API key。需要你提供一个有效的 `OPENROUTER_API_KEY`（格式 `sk-or-...`），或者确认旧的 TUM key 是否可以直接用于 `https://openrouter.ai/api/v1`。

### 已完成
- Bug 1 修复：`entity_set()` 传参改为 `.get("entities", [])`（3 处）
- Bug 2 修复：`parse_response()` 增加嵌套 JSON string 容错（data 和 entities 字段）
- Bug 3 修复：`API_BASE_URL` 默认值改为 `https://openrouter.ai/api/v1`
- 旧进程 PID 1509955 已死，无需 kill
- output 目录无 checkpoint（只有 instance_ids.json）

### 待提供
- 有效的 `OPENROUTER_API_KEY`，提供后可继续 smoke test 和全量实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 113488,
  "duration_api_ms": 114302,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "f60ead3f-170c-4318-bfc7-2604e39cdec8",
  "total_cost_usd": 0.5961275,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 39264,
    "cache_read_input_tokens": 441743,
    "output_tokens": 5102,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39264,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 449,
        "cache_read_input_tokens": 50836,
        "cache_creation_input_tokens": 269,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 269
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2146,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002241,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 5102,
      "cacheReadInputTokens": 441743,
      "cacheCreationInputTokens": 39264,
      "webSearchRequests": 0,
      "costUSD": 0.5938865,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "75da40e3-376f-4c9a-9960-5f3e6391df53"
}
```

</details>

---
