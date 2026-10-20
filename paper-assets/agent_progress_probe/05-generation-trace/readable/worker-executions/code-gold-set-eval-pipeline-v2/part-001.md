# code gold set eval pipeline v2 — Part 1 of 2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

[Transcript overview](../code-gold-set-eval-pipeline-v2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/dd/dd2b123464c2882036ff.json)

## Before a recorded user message

## Before a recorded user message

103 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
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
  "uuid": "b67d8022-cb4b-41b8-a8a7-ff3c736dd9ae",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778814000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ad081507-c844-4a77-a54b-10714800fc83",
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b"
}
```

---


### Assistant

_source line 4_

I'll start by reading the target file and finding the reference file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "61fee99a-bb3c-4760-af08-206ce7696806",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQvdV855NRYdyrU2aqMKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11778
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_01TTfo7ErJmCTXxnjjUp1ooJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "6f0d7403-93f1-4a96-9f4e-702010d5b31d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQvdV855NRYdyrU2aqMKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11778
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-14T22:49:28.554Z_

<details><summary>↩ Tool result · `toolu_01TTfo7ErJmCTXxnjjUp1ooJ`</summary>

````text
1	#!/usr/bin/env python3
2	"""Gold-set evaluation pipeline for agent_progress_probe.
3	
4	Evaluates multiple stagnation detectors against human-annotated gold labels:
5	  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features
6	  - GRU probe (ProgressProbe) on pre-computed embeddings
7	  - LLM-as-judge (from cached prediction JSONL)
8	  - Silver labels (majority-vote from labeling functions)
9	
10	Inputs:
11	  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),
12	                    optional annotator_id, confidence
13	  --predictions-dir Directory with model artifacts (checkpoints, embeddings,
14	                    windows_labeled.jsonl, trajectories, cached LLM predictions)
15	  --output-dir      Where to write results JSON and reliability diagram PDF
16	
17	Outputs:
18	  {output-dir}/gold_set_results.json   — full metrics for every model
19	  {output-dir}/gold_set_reliability.pdf — calibration curves
20	
21	Dependencies: torch, scikit-learn, numpy, matplotlib
22	"""
23	
24	import argparse
25	import csv
26	import json
27	import re
28	import sys
29	import time
30	import warnings
31	from collections import Counter
32	from difflib import SequenceMatcher
33	from pathlib import Path
34	
35	import numpy as np
36	from sklearn.calibration import calibration_curve
37	from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
38	from sklearn.linear_model import LogisticRegression
39	from sklearn.metrics import (
40	    accuracy_score,
41	    cohen_kappa_score,
42	    f1_score,
43	    precision_score,
44	    recall_score,
45	)
46	from sklearn.preprocessing import StandardScaler
47	
48	warnings.filterwarnings("ignore", category=UserWarning)
49	
50	# ---------------------------------------------------------------------------
51	# Optional: torch (only needed for GRU probe)
52	# ---------------------------------------------------------------------------
53	try:
54	    import torch
55	    import torch.nn as nn
56	    from torch.utils.data import DataLoader
57	
58	    HAS_TORCH = True
59	except ImportError:
60	    HAS_TORCH = False
61	
62	# ---------------------------------------------------------------------------
63	# Try importing probe model from project artifacts
64	# ---------------------------------------------------------------------------
65	_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / "artifacts"
66	if _ARTIFACTS_DIR.exists():
67	    sys.path.insert(0, str(_ARTIFACTS_DIR))
68	try:
69	    from probe_model import ProgressProbe, WindowDataset, collate_fn
70	    HAS_PROBE = True
71	except ImportError:
72	    HAS_PROBE = False
73	
74	
75	# ===========================================================================
76	# Metrics
77	# ===========================================================================
78	
79	def compute_metrics(y_true, y_pred):
80	    """Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa."""
81	    return {
82	        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
83	        "accuracy": accuracy_score(y_true, y_pred),
84	        "precision_stag": precision_score(y_true, y_pred, pos_label=0, zero_division=0),
85	        "recall_stag": recall_score(y_true, y_pred, pos_label=0, zero_division=0),
86	        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
87	        "precision_prog": precision_score(y_true, y_pred, pos_label=1, zero_division=0),
88	        "recall_prog": recall_score(y_true, y_pred, pos_label=1, zero_division=0),
89	        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
90	        "cohens_kappa": cohen_kappa_score(y_true, y_pred),
91	    }
92	
93	
94	# ===========================================================================
95	# Structural feature extraction (mirrors non_nlp_baseline.py)
96	# ===========================================================================
97	
98	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
99	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
100	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
101	
102	
103	def _extract_command(text):
104	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
105	    return match.group(1).strip() if match else None
106	
107	
108	def _cmd_similarity(a, b):
109	    if a == b:
110	        return 1.0
111	    if not a or not b:
112	        return 0.0
113	    return SequenceMatcher(None, a, b).ratio()
114	
115	
116	def extract_structural_features(steps, is_short):
117	    """Extract 30-dim structural feature vector from a list of step dicts."""
118	    n = len(steps)
119	    if n == 0:
120	        return np.zeros(30, dtype=np.float32)
121	
122	    texts = [s["text"] for s in steps]
123	    text_lens = [len(t) for t in texts]
124	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
125	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
126	    n_actions = len(actions)
127	    n_obs = len(observations)
128	
129	    mean_tlen = np.mean(text_lens)
130	    std_tlen = np.std(text_lens) if n > 1 else 0.0
131	    max_tlen = max(text_lens)
132	    min_tlen = min(text_lens)
133	    action_lens = [len(t) for _, t in actions] if actions else [0]
134	    obs_lens = [len(t) for _, t in observations] if observations else [0]
135	    mean_action_len = np.mean(action_lens)
136	    mean_obs_len = np.mean(obs_lens)
137	
138	    if n > 1:
139	        x = np.arange(n, dtype=float)
140	        y = np.array(text_lens, dtype=float)
141	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (
142	            n * np.dot(x, x) - x.sum() ** 2 + 1e-9
143	        )
144	    else:
145	        slope = 0.0
146	
147	    commands = []
148	    for _, t in actions:
149	        cmd = _extract_command(t)
150	        if cmd:
151	            commands.append(cmd)
152	    n_cmds = len(commands)
153	    cmd_lens = [len(c) for c in commands] if commands else [0]
154	    mean_cmd_len = np.mean(cmd_lens)
155	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
156	
157	    if n_cmds > 0:
158	        unique_cmds = len(set(commands))
159	        unique_cmd_ratio = unique_cmds / n_cmds
160	        cmd_counter = Counter(commands)
161	        max_repeat = cmd_counter.most_common(1)[0][1]
162	        repeat_ratio = max_repeat / n_cmds
163	    else:
164	        unique_cmd_ratio = 1.0
165	        repeat_ratio = 0.0
166	
167	    n_edit = n_search = n_nav = n_submit = 0
168	    for cmd in commands:
169	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
170	        if first_word in EDIT_CMDS:
171	            n_edit += 1
172	        elif first_word in SEARCH_CMDS:
173	            n_search += 1
174	        elif first_word in NAV_CMDS:
175	            n_nav += 1
176	        elif first_word == "submit":
177	            n_submit += 1
178	    edit_ratio = n_edit / max(n_cmds, 1)
179	    search_ratio = n_search / max(n_cmds, 1)
180	
181	    if n_cmds >= 2:
182	        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]
183	        avg_adj_sim = np.mean(sims)
184	        max_adj_sim = max(sims)
185	        max_run, cur_run = 1, 1
186	        for s in sims:
187	            if s >= 0.9:
188	                cur_run += 1
189	                max_run = max(max_run, cur_run)
190	            else:
191	                cur_run = 1
192	    else:
193	        avg_adj_sim = max_adj_sim = 0.0
194	        max_run = 0
195	
196	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
197	    n_test_output = sum(
198	        1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower()
199	    )
200	    n_file_display = sum(1 for t in texts if "[File:" in t)
201	    n_nonzero_exit = sum(
202	        1
203	        for _, t in observations
204	        if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
205	    )
206	
207	    return np.array(
208	        [
209	            n, n_actions, n_obs, n_actions / max(n, 1),
210	            mean_tlen, std_tlen, max_tlen, min_tlen,
211	            mean_action_len, mean_obs_len, slope,
212	            n_cmds, mean_cmd_len, max_cmd_len,
213	            unique_cmd_ratio, repeat_ratio,
214	            n_edit, n_search, n_nav, n_submit,
215	            edit_ratio, search_ratio,
216	            avg_adj_sim, max_adj_sim, max_run,
217	            n_errors, n_test_output, n_file_display, n_nonzero_exit,
218	            float(is_short),
219	        ],
220	        dtype=np.float32,
221	    )
222	
223	
224	# ===========================================================================
225	# Data loading helpers
226	# ===========================================================================
227	
228	def load_gold_labels(path):
229	    """Load gold labels from CSV or JSONL.
230	
231	    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]
232	    """
233	    path = Path(path)
234	    records = []
235	    if path.suffix == ".csv":
236	        with open(path) as f:
237	            reader = csv.DictReader(f)
238	            for row in reader:
239	                rec = {
240	                    "window_id": row["window_id"],
241	                    "gold_label": int(row["gold_label"]),
242	                }
243	                if "annotator_id" in row:
244	                    rec["annotator_id"] = row["annotator_id"]
245	                if "confidence" in row:
246	                    rec["confidence"] = int(row["confidence"]) if row["confidence"] else None
247	                records.append(rec)
248	    else:
249	        with open(path) as f:
250	            for line in f:
251	                line = line.strip()
252	                if not line:
253	                    continue
254	                obj = json.loads(line)
255	                rec = {
256	                    "window_id": obj["window_id"],
257	                    "gold_label": int(obj["gold_label"]),
258	                }
259	                if "annotator_id" in obj:
260	                    rec["annotator_id"] = obj["annotator_id"]
261	                if "confidence" in obj:
262	                    rec["confidence"] = obj.get("confidence")
263	                records.append(rec)
264	    return records
265	
266	
267	def load_windows_jsonl(path):
268	    windows = []
269	    with open(path) as f:
270	        for line in f:
271	            line = line.strip()
272	            if line:
273	                windows.append(json.loads(line))
274	    return windows
275	
276	
277	def build_trajectory_index(traj_path):
278	    index = {}
279	    with open(traj_path) as f:
280	        for row_idx, line in enumerate(f):
281	            line = line.strip()
282	            if not line:
283	                continue
284	            raw = json.loads(line)
285	            steps = []
286	            for s in raw.get("trajectory") or []:
287	                steps.append(
288	                    {
289	                        "role": s.get("role", "unknown"),
290	                        "text": s.get("text") or s.get("system_prompt") or "",
291	                    }
292	                )
293	            index[row_idx] = steps
294	    return index
295	
296	
297	def window_id_from_window(w):
298	    return f"{w['trajectory_id']}__w{w['window_idx']}"
299	
300	
301	def parse_row_index(trajectory_id):
302	    return int(trajectory_id.rsplit("__r", 1)[1])
303	
304	
305	# ===========================================================================
306	# Model evaluators
307	# ===========================================================================
308	
309	def _align(gold_wids, gold_labels, prediction_map):
310	    """Align gold labels with predictions by window_id.
311	
312	    Returns (aligned_gold, aligned_preds, n_missing).
313	    """
314	    aligned_gold, aligned_preds = [], []
315	    n_missing = 0
316	    for wid, gl in zip(gold_wids, gold_labels):
317	        pred = prediction_map.get(wid)
318	        if pred is None:
319	            n_missing += 1
320	            continue
321	        aligned_gold.append(gl)
322	        aligned_preds.append(pred)
323	    return aligned_gold, aligned_preds, n_missing
324	
325	
326	def evaluate_silver(gold_wids, gold_labels, wid_to_window):
327	    """Silver majority-vote labels vs gold."""
328	    pred_map = {}
329	    prob_map = {}
330	    conf_map = {}
331	    for wid in gold_wids:
332	        w = wid_to_window.get(wid)
333	        if w is None:
334	            continue
335	        pred_map[wid] = w["majority_label"]
336	        prob_map[wid] = float(w["majority_label"])
337	        conf_map[wid] = w.get("confidence", 0)
338	    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
339	    if not gold_al:
340	        return None, 0, {}, {}, {}
341	    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map
342	
343	
344	def evaluate_structural_clf(
345	    gold_wids,
346	    gold_labels,
347	    wid_to_noabs_idx,
348	    all_features,
349	    all_mv_labels,
350	    split_info,
351	    model_cls,
352	    model_kwargs,
353	    use_scaler=False,
354	):
355	    """Train structural classifier on silver train split, predict on gold windows."""
356	    keep_indices = split_info.get("keep_indices")
357	    if keep_indices is not None:
358	        feat_subset = all_features[keep_indices]
359	        label_subset = np.array(all_mv_labels)[keep_indices]
360	    else:
361	        feat_subset = all_features
362	        label_subset = np.array(all_mv_labels)
363	
364	    train_idx = split_info["train_indices"]
365	    X_train = feat_subset[train_idx]
366	    y_train = label_subset[train_idx]
367	
368	    scaler = None
369	    if use_scaler:
370	        scaler = StandardScaler()
371	        X_train = scaler.fit_transform(X_train)
372	
373	    clf = model_cls(**model_kwargs)
374	    clf.fit(X_train, y_train)
375	
376	    pred_map = {}
377	    prob_map = {}
378	    for wid in gold_wids:
379	        idx = wid_to_noabs_idx.get(wid)
380	        if idx is None:
381	            continue
382	        feat = all_features[idx].reshape(1, -1)
383	        if scaler is not None:
384	            feat = scaler.transform(feat)
385	        pred_map[wid] = int(clf.predict(feat)[0])
386	        if hasattr(clf, "predict_proba"):
387	            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])
388	
389	    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
390	    if not gold_al:
391	        return None, 0, n_miss, prob_map
392	    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map
393	
394	
395	def evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):
396	    """GRU probe evaluation on gold windows."""
397	    if not HAS_TORCH or not HAS_PROBE:
398	        return None, 0, len(gold_wids), {}
399	
400	    ckpt_path = Path(ckpt_path)
401	    if not ckpt_path.exists():
402	        return None, 0, len(gold_wids), {}
403	
404	    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
405	    model = ProgressProbe(
406	        embed_dim=ckpt["embed_dim"],
407	        hidden_size=ckpt["hidden_size"],
408	        num_layers=ckpt["num_layers"],
409	    ).to(device)
410	    model.load_state_dict(ckpt["model_state_dict"])
411	    model.eval()
412	
413	    ordered_wids = []
414	    gold_embs = []
415	    valid_gold = []
416	    n_miss = 0
417	    for wid, gl in zip(gold_wids, gold_labels):
418	        idx = wid_to_emb_idx.get(wid)
419	        if idx is None:
420	            n_miss += 1
421	            continue
422	        ordered_wids.append(wid)
423	        gold_embs.append(embeddings[idx])
424	        valid_gold.append(gl)
425	
426	    if not gold_embs:
427	        return None, 0, n_miss, {}
428	
429	    ds = WindowDataset(gold_embs, valid_gold)
430	    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)
431	
432	    all_preds = []
433	    all_probs = []
434	    all_labels = []
435	    with torch.no_grad():
436	        for padded, labels, lengths in loader:
437	            logits = model(padded.to(device), lengths)
438	            probs = torch.sigmoid(logits).cpu()
439	            preds = (probs >= 0.5).long()
440	            all_preds.extend(preds.tolist())
441	            all_probs.extend(probs.tolist())
442	            all_labels.extend(labels.long().tolist())
443	
444	    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}
445	    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map
446	
447	
448	def evaluate_llm_judge(gold_wids, gold_labels, predictions_path):
449	    """LLM-as-judge from cached predictions JSONL/JSON."""
450	    predictions_path = Path(predictions_path)
451	    if not predictions_path.exists():
452	        return None, 0, len(gold_wids), {}
453	
454	    pred_index = {}
455	    if predictions_path.suffix == ".jsonl":
456	        with open(predictions_path) as f:
457	            for line in f:
458	                line = line.strip()
459	                if not line:
460	                    continue
461	                obj = json.loads(line)
462	                wid = f"{obj['trajectory_id']}__w{obj['window_idx']}"
463	                if obj.get("predicted_label", -1) != -1:
464	                    pred_index[wid] = obj
465	    else:
466	        with open(predictions_path) as f:
467	            data = json.load(f)
468	        for obj in data.get("results", []):
469	            wid = f"{obj['trajectory_id']}__w{obj['window_idx']}"
470	            if obj.get("predicted_label", -1) != -1:
471	                pred_index[wid] = obj
472	
473	    pred_map = {wid: obj["predicted_label"] for wid, obj in pred_index.items()}
474	    prob_map = {}
475	    for wid, obj in pred_index.items():
476	        conf = obj.get("llm_confidence", 3)
477	        label = obj["predicted_label"]
478	        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)
479	
480	    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
481	    if not gold_al:
482	        return None, 0, n_miss, prob_map
483	    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map
484	
485	
486	# ===========================================================================
487	# Confidence stratification (silver label confidence vs gold agreement)
488	# ===========================================================================
489	
490	def confidence_stratification(gold_wids, gold_labels, wid_to_window):
491	    """Agreement between silver and gold stratified by silver confidence (1/2/3)."""
492	    strata = {1: {"agree": 0, "total": 0}, 2: {"agree": 0, "total": 0}, 3: {"agree": 0, "total": 0}}
493	    for wid, gl in zip(gold_wids, gold_labels):
494	        w = wid_to_window.get(wid)
495	        if w is None:
496	            continue
497	        conf = w.get("confidence", 0)
498	        if conf not in strata:
499	            continue
500	        strata[conf]["total"] += 1
501	        if w["majority_label"] == gl:
502	            strata[conf]["agree"] += 1
503	
504	    result = {}
505	    for conf in [1, 2, 3]:
506	        total = strata[conf]["total"]
507	        agree = strata[conf]["agree"]
508	        result[f"conf_{conf}"] = {
509	            "total": total,
510	            "agree": agree,
511	            "agreement_rate": agree / total if total > 0 else None,
512	        }
513	    return result
514	
515	
516	# ===========================================================================
517	# Reliability diagram
518	# ===========================================================================
519	
520	def plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):
521	    """Plot calibration curves for all models with predicted probabilities."""
522	    import matplotlib
523	
524	    matplotlib.use("Agg")
525	    import matplotlib.pyplot as plt
526	
527	    plt.rcParams.update(
528	        {
529	            "font.family": "serif",
530	            "font.size": 10,
531	            "axes.labelsize": 11,
532	            "axes.titlesize": 12,
533	            "legend.fontsize": 9,
534	            "figure.dpi": 150,
535	        }
536	    )
537	
538	    gold_map = dict(zip(gold_wids, gold_labels))
539	
540	    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={"width_ratios": [2, 1]})
541	
542	    ax1.plot([0, 1], [0, 1], "k--", lw=1, label="Perfect calibration")
543	
544	    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
545	    for i, (model_name, prob_map) in enumerate(model_probs.items()):
546	        y_true, y_prob = [], []
547	        for wid, prob in prob_map.items():
548	            gl = gold_map.get(wid)
549	            if gl is not None:
550	                y_true.append(gl)
551	                y_prob.append(prob)
552	        if len(y_true) < 10:
553	            continue
554	
555	        y_true = np.array(y_true)
556	        y_prob = np.array(y_prob)
557	
558	        fraction_pos, mean_predicted = calibration_curve(
559	            y_true, y_prob, n_bins=n_bins, strategy="uniform"
560	        )
561	        ax1.plot(
562	            mean_predicted, fraction_pos,
563	            "o-", color=colors[i % len(colors)], label=model_name, markersize=4,
564	        )
565	
566	        ax2.hist(
567	            y_prob, bins=n_bins, range=(0, 1),
568	            alpha=0.5, color=colors[i % len(colors)], label=model_name,
569	        )
570	
571	    ax1.set_xlabel("Mean predicted probability")
572	    ax1.set_ylabel("Fraction of positives (progress)")
573	    ax1.set_title("Reliability Diagram")
574	    ax1.legend(loc="lower right")
575	    ax1.set_xlim(-0.02, 1.02)
576	    ax1.set_ylim(-0.02, 1.02)
577	    ax1.set_aspect("equal")
578	
579	    ax2.set_xlabel("Predicted probability")
580	    ax2.set_ylabel("Count")
581	    ax2.set_title("Prediction Distribution")
582	    ax2.legend(loc="upper right")
583	
584	    fig.tight_layout()
585	    fig.savefig(output_path, bbox_inches="tight")
586	    plt.close(fig)
587	
588	
589	# ===========================================================================
590	# Console summary
591	# ===========================================================================
592	
593	def print_summary_table(results):
594	    """Print markdown-formatted summary to console."""
595	    header = (
596	        "| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) "
597	        "| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |"
598	    )
599	    sep = "|" + "|".join(["---"] * 11) + "|"
600	    print(header)
601	    print(sep)
602	    for name, metrics, n, n_miss in results:
603	        if metrics is None:
604	            print(f"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}")
605	            continue
606	        print(
607	            f"| {name:19s} "
608	            f"| {n:5d} "
609	            f"| {metrics['macro_f1']:.4f}   "
610	            f"| {metrics['accuracy']:.4f}   "
611	            f"| {metrics['precision_stag']:.4f}  "
612	            f"| {metrics['recall_stag']:.4f}  "
613	            f"| {metrics['f1_stag']:.4f}   "
614	            f"| {metrics['precision_prog']:.4f}  "
615	            f"| {metrics['recall_prog']:.4f}  "
616	            f"| {metrics['f1_prog']:.4f}   "
617	            f"| {metrics['cohens_kappa']:.4f}  |"
618	        )
619	
620	
621	# ===========================================================================
622	# Main
623	# ===========================================================================
624	
625	ALL_MODELS = ["silver", "rf", "gb", "lr", "gru_probe", "llm_judge"]
626	
627	
628	def main():
629	    parser = argparse.ArgumentParser(
630	        description="Gold-set evaluation pipeline for agent_progress_probe",
631	        formatter_class=argparse.RawDescriptionHelpFormatter,
632	    )
633	    parser.add_argument(
634	        "--gold-file", required=True,
635	        help="Path to gold label file (CSV or JSONL). "
636	             "Required fields: window_id, gold_label (0=stagnation, 1=progress). "
637	             "Optional: annotator_id, confidence.",
638	    )
639	    parser.add_argument(
640	        "--predictions-dir", required=True,
641	        help="Directory containing model artifacts: "
642	             "data/windows_labeled.jsonl, data/embeddings.pt, "
643	             "checkpoints/best_model.pt, checkpoints/split_info.json, "
644	             "data/swe_agent_trajectories_5000.jsonl, "
645	             "results/llm_judge_results.json",
646	    )
647	    parser.add_argument(
648	        "--output-dir", default="artifacts",
649	        help="Output directory for results JSON and reliability PDF (default: artifacts)",
650	    )
651	    parser.add_argument(
652	        "--models", nargs="+", default=ALL_MODELS, choices=ALL_MODELS,
653	        help="Which models to evaluate (default: all). "
654	             "Choices: silver, rf, gb, lr, gru_probe, llm_judge",
655	    )
656	    parser.add_argument("--device", default=None, help="Torch device (default: auto)")
657	    parser.add_argument(
658	        "--llm-predictions", default=None,
659	        help="Override path to LLM-as-judge cached predictions (JSON or JSONL)",
660	    )
661	    parser.add_argument(
662	        "--checkpoint", default=None,
663	        help="Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)",
664	    )
665	    parser.add_argument(
666	        "--trajectories", default=None,
667	        help="Override path to raw trajectories JSONL",
668	    )
669	    parser.add_argument("--n-bins", type=int, default=10, help="Calibration curve bins")
670	    args = parser.parse_args()
671	
672	    t_start = time.time()
673	    pdir = Path(args.predictions_dir)
674	    output_dir = Path(args.output_dir)
675	    output_dir.mkdir(parents=True, exist_ok=True)
676	
677	    device = args.device
678	    if device is None and HAS_TORCH:
679	        device = "cuda" if torch.cuda.is_available() else "cpu"
680	    elif device is None:
681	        device = "cpu"
682	
683	    selected_models = set(args.models)
684	
685	    # ------------------------------------------------------------------
686	    # 1. Load gold labels
687	    # ------------------------------------------------------------------
688	    print(f"Loading gold labels: {args.gold_file}")
689	    gold_records = load_gold_labels(args.gold_file)
690	    gold_wids = [r["window_id"] for r in gold_records]
691	    gold_labels = [r["gold_label"] for r in gold_records]
692	    gold_dist = Counter(gold_labels)
693	    print(f"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}")
694	
695	    # ------------------------------------------------------------------
696	    # 2. Load windows_labeled.jsonl
697	    # ------------------------------------------------------------------
698	    windows_path = None
699	    for candidate in [
700	        pdir / "data" / "windows_labeled.jsonl",
701	        pdir / "windows_labeled.jsonl",
702	        pdir / "artifacts" / "data" / "windows_labeled.jsonl",
703	    ]:
704	        if candidate.exists():
705	            windows_path = candidate
706	            break
707	    if windows_path is None:
708	        print("ERROR: windows_labeled.jsonl not found under predictions-dir")
709	        sys.exit(1)
710	    print(f"Loading windows: {windows_path}")
711	    all_windows = load_windows_jsonl(str(windows_path))
712	    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
713	    print(f"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}")
714	
715	    wid_to_window = {window_id_from_window(w): w for w in non_abstain}
716	    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}
717	
718	    # ------------------------------------------------------------------
719	    # 3. Load split info
720	    # ------------------------------------------------------------------
721	    split_info_path = None
722	    for candidate in [
723	        pdir / "checkpoints" / "split_info.json",
724	        pdir / "split_info.json",
725	        pdir / "artifacts" / "split_info.json",
726	    ]:
727	        if candidate.exists():
728	            split_info_path = candidate
729	            break
730	    split_info = None
731	    if split_info_path is not None:
732	        print(f"Loading split info: {split_info_path}")
733	        with open(split_info_path) as f:
734	            split_info = json.load(f)
735	
736	    # ------------------------------------------------------------------
737	    # 4. Evaluate models
738	    # ------------------------------------------------------------------
739	    results = []
740	    model_probs = {}
741	
742	    # --- Silver labels ---
743	    if "silver" in selected_models:
744	        print("\nEvaluating: Silver (MV) Labels vs Gold ...")
745	        m, n, n_miss, prob_map, conf_map = evaluate_silver(
746	            gold_wids, gold_labels, wid_to_window
747	        )
748	        if m:
749	            print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
750	        results.append(("Silver (MV)", m, n, n_miss))
751	        if prob_map:
752	            model_probs["Silver (MV)"] = prob_map
753	
754	    # --- Structural classifiers (RF, GB, LR) ---
755	    need_structural = selected_models & {"rf", "gb", "lr"}
756	    if need_structural:
757	        traj_path = Path(args.trajectories) if args.trajectories else None
758	        if traj_path is None:
759	            for candidate in [
760	                pdir / "data" / "swe_agent_trajectories_5000.jsonl",
761	                pdir / "swe_agent_trajectories_5000.jsonl",
762	                pdir / "artifacts" / "data" / "swe_agent_trajectories_5000.jsonl",
763	                pdir / "data" / "swe_agent_trajectories_1000.jsonl",
764	                pdir / "artifacts" / "data" / "swe_agent_trajectories_1000.jsonl",
765	            ]:
766	                if candidate.exists():
767	                    traj_path = candidate
768	                    break
769	
770	        if traj_path is not None and traj_path.exists() and split_info is not None:
771	            print(f"\nBuilding structural features (trajectories: {traj_path}) ...")
772	            traj_index = build_trajectory_index(str(traj_path))
773	            print(f"  Indexed {len(traj_index)} trajectories")
774	
775	            all_features = []
776	            all_mv_labels = []
777	            for w in non_abstain:
778	                row_idx = w.get("row_index", 0)
779	                step_indices = w["step_indices"]
780	                traj_steps = traj_index.get(row_idx, [])
781	                window_steps = []
782	                for si in step_indices:
783	                    if si < len(traj_steps):
784	                        window_steps.append(traj_steps[si])
785	                    else:
786	                        window_steps.append({"role": "unknown", "text": ""})
787	                feat = extract_structural_features(window_steps, w.get("short_trajectory", False))
788	                all_features.append(feat)
789	                all_mv_labels.append(w["majority_label"])
790	
791	            all_features = np.stack(all_features)
792	            print(f"  Feature matrix: {all_features.shape}")
793	
794	            struct_configs = {
795	                "rf": (
796	                    "Structural RF",
797	                    RandomForestClassifier,
798	                    {"n_estimators": 200, "max_depth": 10, "random_state": 42, "n_jobs": -1},
799	                    False,
800	                ),
801	                "gb": (
802	                    "Structural GB",
803	                    GradientBoostingClassifier,
804	                    {"n_estimators": 200, "learning_rate": 0.1, "max_depth": 5, "random_state": 42},
805	                    False,
806	                ),
807	                "lr": (
808	                    "Structural LR",
809	                    LogisticRegression,
810	                    {"max_iter": 2000, "C": 1.0, "solver": "lbfgs"},
811	                    True,
812	                ),
813	            }
814	            for key in ["rf", "gb", "lr"]:
815	                if key not in selected_models:
816	                    continue
817	                name, cls, kwargs, scaler = struct_configs[key]
818	                print(f"  Evaluating {name} ...")
819	                m, n, n_miss, prob_map = evaluate_structural_clf(
820	                    gold_wids, gold_labels, wid_to_noabs_idx,
821	                    all_features, all_mv_labels, split_info,
822	                    cls, kwargs, use_scaler=scaler,
823	                )
824	                if m:
825	                    print(f"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
826	                results.append((name, m, n, n_miss))
827	                if prob_map:
828	                    model_probs[name] = prob_map
829	        else:
830	            reason = "trajectories not found" if traj_path is None else "split_info not found"
831	            print(f"\nSkipping structural classifiers: {reason}")
832	            for key in ["rf", "gb", "lr"]:
833	                if key in selected_models:
834	                    name = {"rf": "Structural RF", "gb": "Structural GB", "lr": "Structural LR"}[key]
835	                    results.append((name, None, 0, len(gold_wids)))
836	
837	    # --- GRU Probe ---
838	    if "gru_probe" in selected_models:
839	        ckpt_path = Path(args.checkpoint) if args.checkpoint else None
840	        if ckpt_path is None:
841	            for candidate in [
842	                pdir / "checkpoints" / "best_model.pt",
843	                pdir / "best_model.pt",
844	                pdir / "artifacts" / "best_model.pt",
845	            ]:
846	                if candidate.exists():
847	                    ckpt_path = candidate
848	                    break
849	
850	        emb_path = None
851	        for candidate in [
852	            pdir / "data" / "embeddings.pt",
853	            pdir / "embeddings.pt",
854	            pdir / "artifacts" / "data" / "embeddings.pt",
855	        ]:
856	            if candidate.exists():
857	                emb_path = candidate
858	                break
859	
860	        print(f"\nEvaluating: GRU Probe ...")
861	        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:
862	            emb_data = torch.load(emb_path, map_location="cpu", weights_only=False)
863	            embeddings = emb_data["embeddings"]
864	
865	            wid_to_emb_idx = {}
866	            if len(embeddings) == len(non_abstain):
867	                for i, w in enumerate(non_abstain):
868	                    wid_to_emb_idx[window_id_from_window(w)] = i
869	            else:
870	                for i in range(min(len(embeddings), len(non_abstain))):
871	                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i
872	
873	            m, n, n_miss, prob_map = evaluate_gru_probe(
874	                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device
875	            )
876	            if m:
877	                print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
878	            results.append(("GRU Probe", m, n, n_miss))
879	            if prob_map:
880	                model_probs["GRU Probe"] = prob_map
881	        else:
882	            missing = []
883	            if not HAS_TORCH:
884	                missing.append("torch")
885	            if not HAS_PROBE:
886	                missing.append("probe_model")
887	            if emb_path is None:
888	                missing.append("embeddings.pt")
889	            if ckpt_path is None:
890	                missing.append("checkpoint")
891	            print(f"  SKIPPED: {', '.join(missing)} not available")
892	            results.append(("GRU Probe", None, 0, len(gold_wids)))
893	
894	    # --- LLM-as-judge ---
895	    if "llm_judge" in selected_models:
896	        llm_path = Path(args.llm_predictions) if args.llm_predictions else None
897	        if llm_path is None:
898	            for candidate in [
899	                pdir / "results" / "llm_judge_results.json",
900	                pdir / "llm_judge_results.json",
901	                pdir / "artifacts" / "results" / "llm_judge_results.json",
902	                pdir / "results" / "llm_judge_results.jsonl",
903	            ]:
904	                if candidate.exists():
905	                    llm_path = candidate
906	                    break
907	
908	        print(f"\nEvaluating: LLM-as-Judge ...")
909	        if llm_path is not None and llm_path.exists():
910	            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)
911	            if m:
912	                print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
913	            results.append(("LLM-as-Judge", m, n, n_miss))
914	            if prob_map:
915	                model_probs["LLM-as-Judge"] = prob_map
916	        else:
917	            print(f"  SKIPPED: no cached predictions found")
918	            results.append(("LLM-as-Judge", None, 0, len(gold_wids)))
919	
920	    # ------------------------------------------------------------------
921	    # 5. Confidence stratification
922	    # ------------------------------------------------------------------
923	    print("\nConfidence stratification (silver conf vs gold agreement):")
924	    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)
925	    for conf_key in ["conf_1", "conf_2", "conf_3"]:
926	        s = conf_strat[conf_key]
927	        rate = f"{s['agreement_rate']:.4f}" if s["agreement_rate"] is not None else "N/A"
928	        print(f"  {conf_key}: {s['agree']}/{s['total']} = {rate}")
929	
930	    # ------------------------------------------------------------------
931	    # 6. Console summary
932	    # ------------------------------------------------------------------
933	    print("\n" + "=" * 120)
934	    print("GOLD SET EVALUATION RESULTS")
935	    print("=" * 120)
936	    print_summary_table(results)
937	
938	    # ------------------------------------------------------------------
939	    # 7. Reliability diagram
940	    # ------------------------------------------------------------------
941	    pdf_path = output_dir / "gold_set_reliability.pdf"
942	    if model_probs:
943	        try:
944	            plot_reliability_diagram(
945	                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins
946	            )
947	            print(f"\nReliability diagram: {pdf_path}")
948	        except Exception as e:
949	            print(f"\nFailed to generate reliability diagram: {e}")
950	    else:
951	        print("\nNo probability estimates available; skipping reliability diagram.")
952	
953	    # ------------------------------------------------------------------
954	    # 8. JSON output
955	    # ------------------------------------------------------------------
956	    elapsed = time.time() - t_start
957	    output = {
958	        "gold_file": str(args.gold_file),
959	        "gold_distribution": {"total": len(gold_labels), "stagnation": gold_dist.get(0, 0), "progress": gold_dist.get(1, 0)},
960	        "confidence_stratification": conf_strat,
961	        "models": {},
962	        "elapsed_seconds": round(elapsed, 2),
963	    }
964	    for name, metrics, n, n_miss in results:
965	        output["models"][name] = {
966	            "n_evaluated": n,
967	            "n_missing": n_miss,
968	            "metrics": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,
969	        }
970	
971	    json_path = output_dir / "gold_set_results.json"
972	    with open(json_path, "w") as f:
973	        json.dump(output, f, indent=2)
974	    print(f"Results JSON: {json_path}")
975	    print(f"Elapsed: {elapsed:.1f}s")
976	
977	
978	if __name__ == "__main__":
979	    main()
980	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "753a868c-04fe-4819-8c8d-1436356bb1ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 980,
      "startLine": 1,
      "totalLines": 980
    }
  }
}
````

</details>

---


### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01M44CcFNeZS4Yq878cGmjaR`</summary>

```json
{
  "pattern": "**/non_nlp_baseline.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "4328646d-b6af-43c0-b1f5-71386e9c3dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQvdV855NRYdyrU2aqMKg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11778
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-14T22:49:28.673Z_

<details><summary>↩ Tool result · `toolu_01M44CcFNeZS4Yq878cGmjaR`</summary>

```text
artifacts/non_nlp_baseline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "46c95ee1-49a0-48e3-9b6e-1a7ef266459b",
  "tool_use_result": {
    "filenames": [
      "artifacts/non_nlp_baseline.py"
    ],
    "durationMs": 85,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the non_nlp_baseline.py file to compare the structural feature extraction logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "d0dd2b52-fbe5-4a83-9342-d7cb70e2c716",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWtoGiwt3QS81ehjZYKUdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13456
      },
      "output_tokens": 10,
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

Now let me read the reference file to compare feature extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "9cd98e4d-2b39-47ff-a165-a86a519a55a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWtoGiwt3QS81ehjZYKUdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13456
      },
      "output_tokens": 10,
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01XaBE282qgCqEqcLia1Xjc6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "e767ee6f-f082-462b-a608-147e4775c613",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWtoGiwt3QS81ehjZYKUdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 23619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13456
      },
      "output_tokens": 10,
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

_source line 12 · 2026-05-14T22:49:33.453Z_

<details><summary>↩ Tool result · `toolu_01XaBE282qgCqEqcLia1Xjc6`</summary>

````text
1	#!/usr/bin/env python3
2	"""Non-NLP baseline: structural/numerical features only.
3	
4	Extracts hand-crafted features from raw trajectory steps (no embeddings),
5	trains LogisticRegression, RandomForest, GradientBoosting.
6	Uses the same train/val/test split as probe_001.
7	"""
8	
9	import json
10	import re
11	import sys
12	import argparse
13	from collections import Counter
14	from difflib import SequenceMatcher
15	from pathlib import Path
16	
17	import numpy as np
18	from sklearn.linear_model import LogisticRegression
19	from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
20	from sklearn.preprocessing import StandardScaler
21	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
22	
23	
24	def compute_metrics(labels, preds):
25	    return {
26	        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
27	        "accuracy": accuracy_score(labels, preds),
28	        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
29	        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
30	        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
31	        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
32	    }
33	
34	
35	def extract_command(text):
36	    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
37	    return match.group(1).strip() if match else None
38	
39	
40	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
41	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
42	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
43	
44	
45	def cmd_similarity(a, b):
46	    if a == b:
47	        return 1.0
48	    if not a or not b:
49	        return 0.0
50	    return SequenceMatcher(None, a, b).ratio()
51	
52	
53	def extract_features(steps, is_short):
54	    """Extract structural features from a list of step dicts.
55	
56	    Each step dict has: role, text
57	    """
58	    n = len(steps)
59	    if n == 0:
60	        return np.zeros(30)
61	
62	    roles = [s["role"] for s in steps]
63	    texts = [s["text"] for s in steps]
64	    text_lens = [len(t) for t in texts]
65	
66	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
67	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
68	
69	    n_actions = len(actions)
70	    n_obs = len(observations)
71	
72	    # --- text length features ---
73	    mean_tlen = np.mean(text_lens)
74	    std_tlen = np.std(text_lens) if n > 1 else 0.0
75	    max_tlen = max(text_lens)
76	    min_tlen = min(text_lens)
77	
78	    action_lens = [len(t) for _, t in actions] if actions else [0]
79	    obs_lens = [len(t) for _, t in observations] if observations else [0]
80	    mean_action_len = np.mean(action_lens)
81	    mean_obs_len = np.mean(obs_lens)
82	
83	    # text length trend (slope via simple linear regression)
84	    if n > 1:
85	        x = np.arange(n, dtype=float)
86	        y = np.array(text_lens, dtype=float)
87	        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
88	    else:
89	        slope = 0.0
90	
91	    # --- command features ---
92	    commands = []
93	    for s, t in actions:
94	        cmd = extract_command(t)
95	        if cmd:
96	            commands.append(cmd)
97	
98	    n_cmds = len(commands)
99	    cmd_lens = [len(c) for c in commands] if commands else [0]
100	    mean_cmd_len = np.mean(cmd_lens)
101	    max_cmd_len = max(cmd_lens) if cmd_lens else 0
102	
103	    if n_cmds > 0:
104	        unique_cmds = len(set(commands))
105	        unique_cmd_ratio = unique_cmds / n_cmds
106	        cmd_counter = Counter(commands)
107	        max_repeat = cmd_counter.most_common(1)[0][1]
108	        repeat_ratio = max_repeat / n_cmds
109	    else:
110	        unique_cmd_ratio = 1.0
111	        repeat_ratio = 0.0
112	
113	    # command type counts
114	    n_edit = 0
115	    n_search = 0
116	    n_nav = 0
117	    n_submit = 0
118	    for cmd in commands:
119	        first_word = cmd.strip().split()[0] if cmd.strip() else ""
120	        if first_word in EDIT_CMDS:
121	            n_edit += 1
122	        elif first_word in SEARCH_CMDS:
123	            n_search += 1
124	        elif first_word in NAV_CMDS:
125	            n_nav += 1
126	        elif first_word == "submit":
127	            n_submit += 1
128	
129	    edit_ratio = n_edit / max(n_cmds, 1)
130	    search_ratio = n_search / max(n_cmds, 1)
131	
132	    # adjacent command similarity
133	    if n_cmds >= 2:
134	        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
135	        avg_adj_sim = np.mean(sims)
136	        max_adj_sim = max(sims)
137	        # max consecutive run with sim >= 0.9
138	        max_run = 1
139	        cur_run = 1
140	        for s in sims:
141	            if s >= 0.9:
142	                cur_run += 1
143	                max_run = max(max_run, cur_run)
144	            else:
145	                cur_run = 1
146	    else:
147	        avg_adj_sim = 0.0
148	        max_adj_sim = 0.0
149	        max_run = 0
150	
151	    # --- content pattern features ---
152	    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
153	    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
154	    n_file_display = sum(1 for t in texts if "[File:" in t)
155	
156	    # exit code patterns in observations (look for "exit code" or "$?" patterns)
157	    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))
158	
159	    feature_vec = np.array([
160	        n,                    # 0: num_steps
161	        n_actions,            # 1: num_actions
162	        n_obs,                # 2: num_observations
163	        n_actions / max(n, 1),# 3: action_ratio
164	        mean_tlen,            # 4: mean_text_len
165	        std_tlen,             # 5: std_text_len
166	        max_tlen,             # 6: max_text_len
167	        min_tlen,             # 7: min_text_len
168	        mean_action_len,      # 8: mean_action_len
169	        mean_obs_len,         # 9: mean_obs_len
170	        slope,                # 10: text_len_trend
171	        n_cmds,               # 11: num_commands
172	        mean_cmd_len,         # 12: mean_cmd_len
173	        max_cmd_len,          # 13: max_cmd_len
174	        unique_cmd_ratio,     # 14: unique_cmd_ratio
175	        repeat_ratio,         # 15: max_repeat_ratio
176	        n_edit,               # 16: num_edit_cmds
177	        n_search,             # 17: num_search_cmds
178	        n_nav,                # 18: num_nav_cmds
179	        n_submit,             # 19: num_submit_cmds
180	        edit_ratio,           # 20: edit_ratio
181	        search_ratio,         # 21: search_ratio
182	        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity
183	        max_adj_sim,          # 23: max_adjacent_cmd_similarity
184	        max_run,              # 24: max_consecutive_similar_cmds
185	        n_errors,             # 25: num_errors
186	        n_test_output,        # 26: num_test_outputs
187	        n_file_display,       # 27: num_file_displays
188	        n_nonzero_exit,       # 28: num_nonzero_exits
189	        float(is_short),      # 29: is_short_trajectory
190	    ], dtype=np.float32)
191	
192	    return feature_vec
193	
194	
195	FEATURE_NAMES = [
196	    "num_steps", "num_actions", "num_observations", "action_ratio",
197	    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
198	    "mean_action_len", "mean_obs_len", "text_len_trend",
199	    "num_commands", "mean_cmd_len", "max_cmd_len",
200	    "unique_cmd_ratio", "max_repeat_ratio",
201	    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
202	    "edit_ratio", "search_ratio",
203	    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
204	    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
205	    "is_short_trajectory",
206	]
207	
208	
209	def build_trajectory_index(traj_path):
210	    """row_index -> list of step dicts [{role, text}, ...]"""
211	    index = {}
212	    with open(traj_path) as f:
213	        for row_idx, line in enumerate(f):
214	            line = line.strip()
215	            if not line:
216	                continue
217	            raw = json.loads(line)
218	            steps = []
219	            for s in raw.get("trajectory") or []:
220	                steps.append({
221	                    "role": s.get("role", "unknown"),
222	                    "text": s.get("text") or s.get("system_prompt") or "",
223	                })
224	            index[row_idx] = steps
225	    return index
226	
227	
228	def load_windows(path):
229	    windows = []
230	    with open(path) as f:
231	        for line in f:
232	            line = line.strip()
233	            if line:
234	                windows.append(json.loads(line))
235	    return windows
236	
237	
238	def print_table(results):
239	    header = "| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |"
240	    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 4) + "|"
241	    print(header)
242	    print(sep)
243	    for name, m in results:
244	        row = f"| {name:28s} |"
245	        for key in ["macro_f1", "accuracy", "f1_stagnation", "f1_progress"]:
246	            v = m.get(key)
247	            if v is None:
248	                row += "    —     |"
249	            else:
250	                row += f" {v:.4f}   |"
251	        print(row)
252	
253	
254	def main():
255	    parser = argparse.ArgumentParser(description="Non-NLP structural baseline")
256	    parser.add_argument("--data_dir", required=True)
257	    parser.add_argument("--split_info", required=True)
258	    parser.add_argument("--trajectories", required=True)
259	    args = parser.parse_args()
260	
261	    data_dir = Path(args.data_dir)
262	
263	    # Load split info
264	    with open(args.split_info) as f:
265	        split_info = json.load(f)
266	
267	    # Build trajectory index
268	    print("Building trajectory index ...")
269	    traj_index = build_trajectory_index(args.trajectories)
270	    print(f"Indexed {len(traj_index)} trajectories")
271	
272	    # Load windows
273	    print("Loading windows ...")
274	    all_windows = load_windows(data_dir / "windows_labeled.jsonl")
275	    print(f"Total windows: {len(all_windows)}")
276	
277	    # Step 1: filter out ABSTAIN (mirrors generate_embeddings.py)
278	    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
279	    print(f"Non-abstain: {len(non_abstain)}")
280	
281	    # Step 2: apply keep_indices (confidence filter, indexes into non_abstain array)
282	    keep_indices = split_info.get("keep_indices")
283	    if keep_indices is not None:
284	        min_conf = split_info.get("min_confidence", 0)
285	        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(non_abstain)}")
286	        windows = [non_abstain[i] for i in keep_indices]
287	    else:
288	        windows = non_abstain
289	
290	    print(f"Usable windows: {len(windows)}")
291	
292	    # Extract features for all usable windows
293	    print("Extracting features ...")
294	    features = []
295	    labels = []
296	    n_missing = 0
297	    for w in windows:
298	        row_idx = w.get("row_index", 0)
299	        step_indices = w["step_indices"]
300	        traj_steps = traj_index.get(row_idx, [])
301	
302	        window_steps = []
303	        for si in step_indices:
304	            if si < len(traj_steps):
305	                window_steps.append(traj_steps[si])
306	            else:
307	                window_steps.append({"role": "unknown", "text": ""})
308	                n_missing += 1
309	
310	        feat = extract_features(window_steps, w.get("short_trajectory", False))
311	        features.append(feat)
312	        labels.append(w["majority_label"])
313	
314	    X = np.stack(features)
315	    y = np.array(labels)
316	    print(f"Feature matrix: {X.shape}, missing steps: {n_missing}")
317	
318	    # Split
319	    train_idx = split_info["train_indices"]
320	    val_idx = split_info["val_indices"]
321	    test_idx = split_info["test_indices"]
322	    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")
323	
324	    X_train, y_train = X[train_idx], y[train_idx]
325	    X_val, y_val = X[val_idx], y[val_idx]
326	    X_test, y_test = X[test_idx], y[test_idx]
327	
328	    print(f"Train label dist: stag={sum(y_train==0)}, prog={sum(y_train==1)}")
329	    print(f"Test label dist:  stag={sum(y_test==0)}, prog={sum(y_test==1)}")
330	    print()
331	
332	    # Standardize
333	    scaler = StandardScaler()
334	    X_train_s = scaler.fit_transform(X_train)
335	    X_val_s = scaler.transform(X_val)
336	    X_test_s = scaler.transform(X_test)
337	
338	    results = []
339	    results.append(("GRU Probe (ref)", {"macro_f1": 0.9055}))
340	    results.append(("MeanPool+LR (ref)", {"macro_f1": 0.8435}))
341	
342	    # --- LogisticRegression ---
343	    print("=== Logistic Regression (C tuning) ===")
344	    best_c, best_val_f1 = None, -1
345	    for c in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]:
346	        lr = LogisticRegression(max_iter=2000, C=c, solver="lbfgs")
347	        lr.fit(X_train_s, y_train)
348	        val_preds = lr.predict(X_val_s)
349	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
350	        print(f"  C={c:7.3f} → val Macro-F1={m['macro_f1']:.4f}")
351	        if m["macro_f1"] > best_val_f1:
352	            best_val_f1 = m["macro_f1"]
353	            best_c = c
354	
355	    print(f"  Best C={best_c}")
356	    lr_final = LogisticRegression(max_iter=2000, C=best_c, solver="lbfgs")
357	    lr_final.fit(X_train_s, y_train)
358	    test_preds_lr = lr_final.predict(X_test_s)
359	    m_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())
360	    results.append(("Struct + LR", m_lr))
361	    print(f"  Test: {m_lr}")
362	
363	    # Feature importance (LR coefficients)
364	    print("\n  Top features (LR coef magnitude):")
365	    coefs = np.abs(lr_final.coef_[0])
366	    top_idx = np.argsort(coefs)[::-1][:10]
367	    for i in top_idx:
368	        print(f"    {FEATURE_NAMES[i]:30s} = {lr_final.coef_[0][i]:+.4f}")
369	    print()
370	
371	    # --- RandomForest ---
372	    print("=== Random Forest (n_estimators tuning) ===")
373	    best_n, best_val_f1_rf = None, -1
374	    for n in [50, 100, 200, 500]:
375	        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)
376	        rf.fit(X_train, y_train)
377	        val_preds = rf.predict(X_val)
378	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
379	        print(f"  n={n:4d} → val Macro-F1={m['macro_f1']:.4f}")
380	        if m["macro_f1"] > best_val_f1_rf:
381	            best_val_f1_rf = m["macro_f1"]
382	            best_n = n
383	
384	    print(f"  Best n_estimators={best_n}")
385	    rf_final = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)
386	    rf_final.fit(X_train, y_train)
387	    test_preds_rf = rf_final.predict(X_test)
388	    m_rf = compute_metrics(y_test.tolist(), test_preds_rf.tolist())
389	    results.append(("Struct + RF", m_rf))
390	    print(f"  Test: {m_rf}")
391	
392	    print("\n  Top features (RF importance):")
393	    imp = rf_final.feature_importances_
394	    top_idx = np.argsort(imp)[::-1][:10]
395	    for i in top_idx:
396	        print(f"    {FEATURE_NAMES[i]:30s} = {imp[i]:.4f}")
397	    print()
398	
399	    # --- GradientBoosting ---
400	    print("=== Gradient Boosting ===")
401	    best_lr_gb, best_val_f1_gb = None, -1
402	    for lr_val in [0.01, 0.05, 0.1, 0.2]:
403	        gb = GradientBoostingClassifier(
404	            n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42
405	        )
406	        gb.fit(X_train, y_train)
407	        val_preds = gb.predict(X_val)
408	        m = compute_metrics(y_val.tolist(), val_preds.tolist())
409	        print(f"  lr={lr_val:.2f} → val Macro-F1={m['macro_f1']:.4f}")
410	        if m["macro_f1"] > best_val_f1_gb:
411	            best_val_f1_gb = m["macro_f1"]
412	            best_lr_gb = lr_val
413	
414	    print(f"  Best lr={best_lr_gb}")
415	    gb_final = GradientBoostingClassifier(
416	        n_estimators=200, learning_rate=best_lr_gb, max_depth=5, random_state=42
417	    )
418	    gb_final.fit(X_train, y_train)
419	    test_preds_gb = gb_final.predict(X_test)
420	    m_gb = compute_metrics(y_test.tolist(), test_preds_gb.tolist())
421	    results.append(("Struct + GB", m_gb))
422	    print(f"  Test: {m_gb}")
423	    print()
424	
425	    # --- Summary ---
426	    print("=" * 80)
427	    print("RESULTS SUMMARY")
428	    print("=" * 80)
429	    print_table(results)
430	
431	    # Best non-NLP
432	    best_name = max(results[2:], key=lambda x: x[1].get("macro_f1", 0))
433	    print(f"\nBest structural baseline: {best_name[0]} (Macro-F1={best_name[1]['macro_f1']:.4f})")
434	    print(f"vs GRU Probe:      {0.9055 - best_name[1]['macro_f1']:+.4f}")
435	    print(f"vs MeanPool+LR:    {0.8435 - best_name[1]['macro_f1']:+.4f}")
436	
437	    # Save results
438	    output = {
439	        "Struct + LR": {f"test_{k}": round(v, 4) for k, v in m_lr.items()},
440	        "Struct + RF": {f"test_{k}": round(v, 4) for k, v in m_rf.items()},
441	        "Struct + GB": {f"test_{k}": round(v, 4) for k, v in m_gb.items()},
442	        "best_model": best_name[0],
443	        "best_macro_f1": round(best_name[1]["macro_f1"], 4),
444	        "probe_ref_macro_f1": 0.9055,
445	        "meanpool_lr_ref_macro_f1": 0.8435,
446	        "num_features": len(FEATURE_NAMES),
447	        "feature_names": FEATURE_NAMES,
448	        "hyperparams": {
449	            "LR_best_C": best_c,
450	            "RF_best_n_estimators": best_n,
451	            "GB_best_lr": best_lr_gb,
452	        },
453	    }
454	    out_path = data_dir / "non_nlp_baseline_results.json"
455	    with open(out_path, "w") as f:
456	        json.dump(output, f, indent=2)
457	    print(f"\nResults saved to {out_path}")
458	
459	
460	if __name__ == "__main__":
461	    main()
462	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "eba89302-cbaa-4c40-af52-0b7c2796363f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/non_nlp_baseline.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Non-NLP baseline: structural/numerical features only.\n\nExtracts hand-crafted features from raw trajectory steps (no embeddings),\ntrains LogisticRegression, RandomForest, GradientBoosting.\nUses the same train/val/test split as probe_001.\n\"\"\"\n\nimport json\nimport re\nimport sys\nimport argparse\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score\n\n\ndef compute_metrics(labels, preds):\n    return {\n        \"macro_f1\": f1_score(labels, preds, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(labels, preds),\n        \"precision_macro\": precision_score(labels, preds, average=\"macro\", zero_division=0),\n        \"recall_macro\": recall_score(labels, preds, average=\"macro\", zero_division=0),\n        \"f1_stagnation\": f1_score(labels, preds, pos_label=0, zero_division=0),\n        \"f1_progress\": f1_score(labels, preds, pos_label=1, zero_division=0),\n    }\n\n\ndef extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_features(steps, is_short):\n    \"\"\"Extract structural features from a list of step dicts.\n\n    Each step dict has: role, text\n    \"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30)\n\n    roles = [s[\"role\"] for s in steps]\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    # --- text length features ---\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    # text length trend (slope via simple linear regression)\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)\n    else:\n        slope = 0.0\n\n    # --- command features ---\n    commands = []\n    for s, t in actions:\n        cmd = extract_command(t)\n        if cmd:\n            commands.append(cmd)\n\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    # command type counts\n    n_edit = 0\n    n_search = 0\n    n_nav = 0\n    n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    # adjacent command similarity\n    if n_cmds >= 2:\n        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        # max consecutive run with sim >= 0.9\n        max_run = 1\n        cur_run = 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = 0.0\n        max_adj_sim = 0.0\n        max_run = 0\n\n    # --- content pattern features ---\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower())\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n\n    # exit code patterns in observations (look for \"exit code\" or \"$?\" patterns)\n    n_nonzero_exit = sum(1 for _, t in observations if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t))\n\n    feature_vec = np.array([\n        n,                    # 0: num_steps\n        n_actions,            # 1: num_actions\n        n_obs,                # 2: num_observations\n        n_actions / max(n, 1),# 3: action_ratio\n        mean_tlen,            # 4: mean_text_len\n        std_tlen,             # 5: std_text_len\n        max_tlen,             # 6: max_text_len\n        min_tlen,             # 7: min_text_len\n        mean_action_len,      # 8: mean_action_len\n        mean_obs_len,         # 9: mean_obs_len\n        slope,                # 10: text_len_trend\n        n_cmds,               # 11: num_commands\n        mean_cmd_len,         # 12: mean_cmd_len\n        max_cmd_len,          # 13: max_cmd_len\n        unique_cmd_ratio,     # 14: unique_cmd_ratio\n        repeat_ratio,         # 15: max_repeat_ratio\n        n_edit,               # 16: num_edit_cmds\n        n_search,             # 17: num_search_cmds\n        n_nav,                # 18: num_nav_cmds\n        n_submit,             # 19: num_submit_cmds\n        edit_ratio,           # 20: edit_ratio\n        search_ratio,         # 21: search_ratio\n        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity\n        max_adj_sim,          # 23: max_adjacent_cmd_similarity\n        max_run,              # 24: max_consecutive_similar_cmds\n        n_errors,             # 25: num_errors\n        n_test_output,        # 26: num_test_outputs\n        n_file_display,       # 27: num_file_displays\n        n_nonzero_exit,       # 28: num_nonzero_exits\n        float(is_short),      # 29: is_short_trajectory\n    ], dtype=np.float32)\n\n    return feature_vec\n\n\nFEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n\n\ndef build_trajectory_index(traj_path):\n    \"\"\"row_index -> list of step dicts [{role, text}, ...]\"\"\"\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append({\n                    \"role\": s.get(\"role\", \"unknown\"),\n                    \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                })\n            index[row_idx] = steps\n    return index\n\n\ndef load_windows(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef print_table(results):\n    header = \"| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |\"\n    sep = \"|\" + \"|\".join([\"-\" * 30] + [\"-\" * 10] * 4) + \"|\"\n    print(header)\n    print(sep)\n    for name, m in results:\n        row = f\"| {name:28s} |\"\n        for key in [\"macro_f1\", \"accuracy\", \"f1_stagnation\", \"f1_progress\"]:\n            v = m.get(key)\n            if v is None:\n                row += \"    —     |\"\n            else:\n                row += f\" {v:.4f}   |\"\n        print(row)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Non-NLP structural baseline\")\n    parser.add_argument(\"--data_dir\", required=True)\n    parser.add_argument(\"--split_info\", required=True)\n    parser.add_argument(\"--trajectories\", required=True)\n    args = parser.parse_args()\n\n    data_dir = Path(args.data_dir)\n\n    # Load split info\n    with open(args.split_info) as f:\n        split_info = json.load(f)\n\n    # Build trajectory index\n    print(\"Building trajectory index ...\")\n    traj_index = build_trajectory_index(args.trajectories)\n    print(f\"Indexed {len(traj_index)} trajectories\")\n\n    # Load windows\n    print(\"Loading windows ...\")\n    all_windows = load_windows(data_dir / \"windows_labeled.jsonl\")\n    print(f\"Total windows: {len(all_windows)}\")\n\n    # Step 1: filter out ABSTAIN (mirrors generate_embeddings.py)\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"Non-abstain: {len(non_abstain)}\")\n\n    # Step 2: apply keep_indices (confidence filter, indexes into non_abstain array)\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        min_conf = split_info.get(\"min_confidence\", 0)\n        print(f\"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(non_abstain)}\")\n        windows = [non_abstain[i] for i in keep_indices]\n    else:\n        windows = non_abstain\n\n    print(f\"Usable windows: {len(windows)}\")\n\n    # Extract features for all usable windows\n    print(\"Extracting features ...\")\n    features = []\n    labels = []\n    n_missing = 0\n    for w in windows:\n        row_idx = w.get(\"row_index\", 0)\n        step_indices = w[\"step_indices\"]\n        traj_steps = traj_index.get(row_idx, [])\n\n        window_steps = []\n        for si in step_indices:\n            if si < len(traj_steps):\n                window_steps.append(traj_steps[si])\n            else:\n                window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                n_missing += 1\n\n        feat = extract_features(window_steps, w.get(\"short_trajectory\", False))\n        features.append(feat)\n        labels.append(w[\"majority_label\"])\n\n    X = np.stack(features)\n    y = np.array(labels)\n    print(f\"Feature matrix: {X.shape}, missing steps: {n_missing}\")\n\n    # Split\n    train_idx = split_info[\"train_indices\"]\n    val_idx = split_info[\"val_indices\"]\n    test_idx = split_info[\"test_indices\"]\n    print(f\"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}\")\n\n    X_train, y_train = X[train_idx], y[train_idx]\n    X_val, y_val = X[val_idx], y[val_idx]\n    X_test, y_test = X[test_idx], y[test_idx]\n\n    print(f\"Train label dist: stag={sum(y_train==0)}, prog={sum(y_train==1)}\")\n    print(f\"Test label dist:  stag={sum(y_test==0)}, prog={sum(y_test==1)}\")\n    print()\n\n    # Standardize\n    scaler = StandardScaler()\n    X_train_s = scaler.fit_transform(X_train)\n    X_val_s = scaler.transform(X_val)\n    X_test_s = scaler.transform(X_test)\n\n    results = []\n    results.append((\"GRU Probe (ref)\", {\"macro_f1\": 0.9055}))\n    results.append((\"MeanPool+LR (ref)\", {\"macro_f1\": 0.8435}))\n\n    # --- LogisticRegression ---\n    print(\"=== Logistic Regression (C tuning) ===\")\n    best_c, best_val_f1 = None, -1\n    for c in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]:\n        lr = LogisticRegression(max_iter=2000, C=c, solver=\"lbfgs\")\n        lr.fit(X_train_s, y_train)\n        val_preds = lr.predict(X_val_s)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  C={c:7.3f} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1:\n            best_val_f1 = m[\"macro_f1\"]\n            best_c = c\n\n    print(f\"  Best C={best_c}\")\n    lr_final = LogisticRegression(max_iter=2000, C=best_c, solver=\"lbfgs\")\n    lr_final.fit(X_train_s, y_train)\n    test_preds_lr = lr_final.predict(X_test_s)\n    m_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())\n    results.append((\"Struct + LR\", m_lr))\n    print(f\"  Test: {m_lr}\")\n\n    # Feature importance (LR coefficients)\n    print(\"\\n  Top features (LR coef magnitude):\")\n    coefs = np.abs(lr_final.coef_[0])\n    top_idx = np.argsort(coefs)[::-1][:10]\n    for i in top_idx:\n        print(f\"    {FEATURE_NAMES[i]:30s} = {lr_final.coef_[0][i]:+.4f}\")\n    print()\n\n    # --- RandomForest ---\n    print(\"=== Random Forest (n_estimators tuning) ===\")\n    best_n, best_val_f1_rf = None, -1\n    for n in [50, 100, 200, 500]:\n        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)\n        rf.fit(X_train, y_train)\n        val_preds = rf.predict(X_val)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  n={n:4d} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1_rf:\n            best_val_f1_rf = m[\"macro_f1\"]\n            best_n = n\n\n    print(f\"  Best n_estimators={best_n}\")\n    rf_final = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)\n    rf_final.fit(X_train, y_train)\n    test_preds_rf = rf_final.predict(X_test)\n    m_rf = compute_metrics(y_test.tolist(), test_preds_rf.tolist())\n    results.append((\"Struct + RF\", m_rf))\n    print(f\"  Test: {m_rf}\")\n\n    print(\"\\n  Top features (RF importance):\")\n    imp = rf_final.feature_importances_\n    top_idx = np.argsort(imp)[::-1][:10]\n    for i in top_idx:\n        print(f\"    {FEATURE_NAMES[i]:30s} = {imp[i]:.4f}\")\n    print()\n\n    # --- GradientBoosting ---\n    print(\"=== Gradient Boosting ===\")\n    best_lr_gb, best_val_f1_gb = None, -1\n    for lr_val in [0.01, 0.05, 0.1, 0.2]:\n        gb = GradientBoostingClassifier(\n            n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42\n        )\n        gb.fit(X_train, y_train)\n        val_preds = gb.predict(X_val)\n        m = compute_metrics(y_val.tolist(), val_preds.tolist())\n        print(f\"  lr={lr_val:.2f} → val Macro-F1={m['macro_f1']:.4f}\")\n        if m[\"macro_f1\"] > best_val_f1_gb:\n            best_val_f1_gb = m[\"macro_f1\"]\n            best_lr_gb = lr_val\n\n    print(f\"  Best lr={best_lr_gb}\")\n    gb_final = GradientBoostingClassifier(\n        n_estimators=200, learning_rate=best_lr_gb, max_depth=5, random_state=42\n    )\n    gb_final.fit(X_train, y_train)\n    test_preds_gb = gb_final.predict(X_test)\n    m_gb = compute_metrics(y_test.tolist(), test_preds_gb.tolist())\n    results.append((\"Struct + GB\", m_gb))\n    print(f\"  Test: {m_gb}\")\n    print()\n\n    # --- Summary ---\n    print(\"=\" * 80)\n    print(\"RESULTS SUMMARY\")\n    print(\"=\" * 80)\n    print_table(results)\n\n    # Best non-NLP\n    best_name = max(results[2:], key=lambda x: x[1].get(\"macro_f1\", 0))\n    print(f\"\\nBest structural baseline: {best_name[0]} (Macro-F1={best_name[1]['macro_f1']:.4f})\")\n    print(f\"vs GRU Probe:      {0.9055 - best_name[1]['macro_f1']:+.4f}\")\n    print(f\"vs MeanPool+LR:    {0.8435 - best_name[1]['macro_f1']:+.4f}\")\n\n    # Save results\n    output = {\n        \"Struct + LR\": {f\"test_{k}\": round(v, 4) for k, v in m_lr.items()},\n        \"Struct + RF\": {f\"test_{k}\": round(v, 4) for k, v in m_rf.items()},\n        \"Struct + GB\": {f\"test_{k}\": round(v, 4) for k, v in m_gb.items()},\n        \"best_model\": best_name[0],\n        \"best_macro_f1\": round(best_name[1][\"macro_f1\"], 4),\n        \"probe_ref_macro_f1\": 0.9055,\n        \"meanpool_lr_ref_macro_f1\": 0.8435,\n        \"num_features\": len(FEATURE_NAMES),\n        \"feature_names\": FEATURE_NAMES,\n        \"hyperparams\": {\n            \"LR_best_C\": best_c,\n            \"RF_best_n_estimators\": best_n,\n            \"GB_best_lr\": best_lr_gb,\n        },\n    }\n    out_path = data_dir / \"non_nlp_baseline_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 462,
      "startLine": 1,
      "totalLines": 462
    }
  }
}
````

</details>

---


### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both files. Let me implement all the changes:

1. **P0-1: Inter-Annotator Agreement** - `compute_inter_annotator_agreement()` function
2. **P0-2: Bootstrap CIs + McNemar** - paired bootstrap + McNemar's test
3. **Minor fix 1**: LLM-as-judge label in reliability diagram gets "(pseudo-probability)" suffix
4. **Minor fix 2**: Structural feature assertion (dim=30, feature names match)

Let me compare the feature extraction between the two files:


- Both have the same EDIT_CMDS, SEARCH_CMDS, NAV_CMDS sets
- Both extract the same 30 features in the same order
- The FEATURE_NAMES list from non_nlp_baseline.py gives us the canonical names to assert against

Now I'm ready to write all the changes. For the inter-annotator agreement function, I need to handle three cases: skip with a warning if there's only one annotator, compute Cohen's κ for two annotators, and implement Fleiss' κ manually for three or more annotators.

For the bootstrap confidence intervals and McNemar test, I'll create functions to compute the macro-F1 difference CI across 1000 bootstrap samples and get the p-value from McNemar's test, then apply these to the model pairs I can extract from available predictions. I need to think through how each model's predictions are currently collected during evaluation so I can properly pair them for comparison. I'm seeing that each evaluate function returns different structures, and I need to decide whether to modify them all to return prediction maps or reconstruct predictions from probabilities. Since Silver has exact labels and structural classifiers have actual predictions rather than probabilities, reconstructing from thresholding won't work reliably. The cleanest solution is to modify each evaluate function to also return prediction maps, then use those for the pairwise comparisons at the end. Looking at what each evaluation function returns, I see they all give me probability maps but not the actual binary predictions. I could threshold the probabilities at 0.5, though that might not perfectly match how some models make their actual predictions—let me check what thresholds each one actually uses.

For the Silver model it's straightforward since the prediction is just the majority label. The structural classifier and GRU both use 0.5 thresholds, so those would align. The LLM judge might be trickier since its pseudo-probabilities may not correspond exactly to its decision boundary.

Rather than trying to reconstruct predictions from probabilities, I should modify each evaluate function to return the actual prediction maps as a fifth return value. This is cleaner than adding extra logic in main, though I need to be careful about how I handle the existing return signatures. I see that `pred_map` is already being created in most of these evaluate functions but just not returned. I'll add it to the return statements for each one—`evaluate_silver`, `evaluate_structural_clf`, `evaluate_gru_probe`, and `evaluate_llm_judge`—and then update the callers to handle the extra return value.

Now I'm writing out the complete updated file with all the modifications: updating the docstring, adding the structural feature names constant and assertion, implementing the inter-annotator agreement and statistical test functions, modifying each evaluate function to return `pred_map`, and updating the main function to compute inter-annotator agreement, collect the prediction maps, add the pseudo-probability label for the LLM judge, and run pairwise comparisons. I'm planning out the edits systematically—updating the docstring, adding necessary imports like `combinations` and scipy dependencies, then implementing the inter-annotator agreement calculation using Fleiss' kappa with the proper matrix organization and formula. I'm planning out the specific edits needed throughout the file: updating the docstring, adding imports for combinations and scipy, defining structural feature names, adding assertions and new functions for inter-annotator agreement and statistical tests, then modifying each evaluation function to return prediction maps alongside their existing outputs. I'm planning out the edits systematically, starting with simpler changes and building up to the main function modifications. For the return values, I need to check what `evaluate_silver` currently returns and add `pred_map` to it since that variable is already being constructed internally. I'm realizing the return statement needs to match what the caller expects—currently it unpacks 5 values, but I'm adding pred_map as a 6th return value, so I need to update both the function's return statement and the caller's unpacking to include it. Let me trace through the error case to make sure the tuple structure is consistent across both the success and failure paths. I need to add `pred_map` to the return statements across these evaluation functions. For `evaluate_structural_clf`, I'm including the existing `prob_map` and adding `pred_map` to the returns. In `evaluate_gru_probe`, I need to construct `pred_map` from the ordered word IDs and predictions before returning it alongside `prob_map`. For `evaluate_llm_judge`, `pred_map` is already being built from the prediction index, so I just need to make sure it's included in the final return.

Now I'm moving to the main orchestration logic where I'll collect all the `pred_map` dictionaries from each evaluation function, compute inter-annotator agreement after loading the gold labels, run pairwise comparisons between models, and write the results to JSON. I also need to handle the naming convention for the LLM-as-Judge model in the probability maps—adding the "(pseudo-probability)" suffix when it's used in the reliability diagram plotting.

For the pairwise comparisons, I'm thinking through which model pairs make sense: the best structural model paired against the probe, the probe against the LLM judge, the best structural model against the LLM judge, and then silver predictions compared against the other models if silver is included in the evaluation. I think the simplest approach is to just run all pairwise comparisons among whatever models are available—that naturally covers the requested pairs whether silver is present or not.

Now I'm going to implement this carefully. Rather than making a bunch of scattered edits, I should do a thorough rewrite of the whole file since I understand the full structure. Actually, targeted edits will be more reviewable, so let me organize the changes logically and count them out. I'm going back and forth on whether to do a full rewrite or targeted edits on this 980-line file. A complete rewrite risks introducing bugs, but the number of scattered changes throughout main() makes targeted edits tedious. Let me commit to the edit approach—I'll work through the changes systematically in groups to minimize risk while staying organized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "64134594-1b37-4fa7-9173-ef9ce29b61da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnUY2idv2aXdPSq6aRMLBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7116,
      "cache_read_input_tokens": 37075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7116
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

_source line 14_

I have both files. The feature extraction in `gold_set_eval.py` matches `non_nlp_baseline.py`. Now I'll implement all four changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "a4b25bd9-7c12-441f-89ae-12b03486a74b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnUY2idv2aXdPSq6aRMLBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7116,
      "cache_read_input_tokens": 37075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7116
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_012Sd19ManFvbMmqdrqj5VtU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"",
  "new_string": "\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "7de1cf82-ac4a-42f2-9ef0-bfce4770fdb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnUY2idv2aXdPSq6aRMLBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7116,
      "cache_read_input_tokens": 37075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7116
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

_source line 16 · 2026-05-14T22:51:45.319Z_

<details><summary>↩ Tool result · `toolu_012Sd19ManFvbMmqdrqj5VtU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "8f711b97-ac15-4bb9-b9a1-b9f862855317",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"",
    "newString": "\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 6,
        "newStart": 7,
        "newLines": 14,
        "lines": [
          "   - LLM-as-judge (from cached prediction JSONL)",
          "   - Silver labels (majority-vote from labeling functions)",
          " ",
          "+Pre-evaluation checks:",
          "+  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)",
          "+    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.",
          "+",
          "+Post-evaluation statistics:",
          "+  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)",
          "+  - McNemar's test for pairwise model comparisons",
          "+",
          " Inputs:",
          "   --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),",
          "                     optional annotator_id, confidence"
        ]
      },
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          "   {output-dir}/gold_set_results.json   — full metrics for every model",
          "   {output-dir}/gold_set_reliability.pdf — calibration curves",
          " ",
          "-Dependencies: torch, scikit-learn, numpy, matplotlib",
          "+Dependencies: torch, scikit-learn, numpy, matplotlib, scipy",
          " \"\"\"",
          " ",
          " import argparse"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01LvDTAHV1Xo3SM9vEvEdFqA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "import argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path",
  "new_string": "import argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "7bd759ea-404f-46f7-88f4-d11d2571eed2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168C4FDZNv4gW7LeXqwU3by",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 44191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6766
      },
      "output_tokens": 61,
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

_source line 18 · 2026-05-14T22:51:53.921Z_

<details><summary>↩ Tool result · `toolu_01LvDTAHV1Xo3SM9vEvEdFqA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "0ccae4c2-60e5-4a74-8d44-d1e9a2f3e07c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "import argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path",
    "newString": "import argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 36,
        "oldLines": 8,
        "newStart": 36,
        "newLines": 9,
        "lines": [
          " import sys",
          " import time",
          " import warnings",
          "-from collections import Counter",
          "+from collections import Counter, defaultdict",
          " from difflib import SequenceMatcher",
          "+from itertools import combinations",
          " from pathlib import Path",
          " ",
          " import numpy as np"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 19_

Now add STRUCTURAL_FEATURE_NAMES and the assertion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "f8b39789-91d0-4bb9-aea2-a81b82be253b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjjRtZiaUpeMTxkbewq1Nt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 50957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_012LtvjxjmSHDzGP2kCbdiCu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "EDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}",
  "new_string": "EDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "6dd71919-7087-4a2f-b998-3ef5438de398",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjjRtZiaUpeMTxkbewq1Nt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 50957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
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

_source line 21 · 2026-05-14T22:52:03.400Z_

<details><summary>↩ Tool result · `toolu_012LtvjxjmSHDzGP2kCbdiCu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "f8b13fb9-ce86-4f6a-ab98-8a9c3962abcd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "EDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}",
    "newString": "EDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 7,
        "newStart": 108,
        "newLines": 21,
        "lines": [
          " SEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}",
          " NAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}",
          " ",
          "+STRUCTURAL_FEATURE_NAMES = [",
          "+    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",",
          "+    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",",
          "+    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",",
          "+    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",",
          "+    \"unique_cmd_ratio\", \"max_repeat_ratio\",",
          "+    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",",
          "+    \"edit_ratio\", \"search_ratio\",",
          "+    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",",
          "+    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",",
          "+    \"is_short_trajectory\",",
          "+]",
          "+_EXPECTED_FEATURE_DIM = 30",
          " ",
          "+",
          " def _extract_command(text):",
          "     match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)",
          "     return match.group(1).strip() if match else None"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 22_

Add the assertion at the end of `extract_structural_features`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "3fb43b3a-048f-47a0-a274-0e2b5608daaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3QhUm9a6TavuFFy4nJ3jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 51249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 740
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01NLbFHj3qkY7hukgjf45EqW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )",
  "new_string": "    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "51b55a48-6c39-40a2-a5f0-1ec0314e0e9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3QhUm9a6TavuFFy4nJ3jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 51249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 740
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

_source line 24 · 2026-05-14T22:52:11.559Z_

<details><summary>↩ Tool result · `toolu_01NLbFHj3qkY7hukgjf45EqW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "0299d349-2d59-41cf-b3a2-9a4b2212fe00",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )",
    "newString": "    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 227,
        "oldLines": 7,
        "newStart": 227,
        "newLines": 7,
        "lines": [
          "         if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)",
          "     )",
          " ",
          "-    return np.array(",
          "+    vec = np.array(",
          "         [",
          "             n, n_actions, n_obs, n_actions / max(n, 1),",
          "             mean_tlen, std_tlen, max_tlen, min_tlen,"
        ]
      },
      {
        "oldStart": 242,
        "oldLines": 6,
        "newStart": 242,
        "newLines": 13,
        "lines": [
          "         ],",
          "         dtype=np.float32,",
          "     )",
          "+    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (",
          "+        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"",
          "+    )",
          "+    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (",
          "+        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"",
          "+    )",
          "+    return vec",
          " ",
          " ",
          " # ==========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 25_

Now add the IAA function. I'll insert it after `extract_structural_features` and before the data loading helpers section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "e9d7b635-9108-436c-b796-2d699ecd6cb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9VqztkQtsc8ZQjboxWHS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 51989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
      },
      "output_tokens": 2,
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_017tYUtN6yLqjrr15Vk2Tpcg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "# ===========================================================================\n# Data loading helpers\n# ===========================================================================",
  "new_string": "# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ==========================================================================="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "0c5fb726-46e6-4120-8f32-29a25fc5e445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9VqztkQtsc8ZQjboxWHS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 51989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
      },
      "output_tokens": 2,
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

_source line 27 · 2026-05-14T22:52:53.575Z_

<details><summary>↩ Tool result · `toolu_017tYUtN6yLqjrr15Vk2Tpcg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "a55985ba-23fc-4381-a1d4-98bfc8b549b0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "# ===========================================================================\n# Data loading helpers\n# ===========================================================================",
    "newString": "# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 252,
        "oldLines": 6,
        "newStart": 252,
        "newLines": 188,
        "lines": [
          " ",
          " ",
          " # ===========================================================================",
          "+# Inter-annotator agreement",
          "+# ===========================================================================",
          "+",
          "+def _fleiss_kappa(table):",
          "+    \"\"\"Fleiss' κ for multiple raters.",
          "+",
          "+    Args:",
          "+        table: (N, k) array where N = items, k = categories.",
          "+               table[i, j] = number of raters who assigned category j to item i.",
          "+",
          "+    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among",
          "+    many raters.\" Psychological Bulletin, 76(5), 378–382.",
          "+    \"\"\"",
          "+    N, k = table.shape",
          "+    n = table[0].sum()",
          "+    if n <= 1 or N == 0:",
          "+        return 0.0",
          "+",
          "+    p_j = table.sum(axis=0) / (N * n)",
          "+    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))",
          "+    P_bar = np.mean(P_i)",
          "+    P_e = np.sum(p_j ** 2)",
          "+",
          "+    if abs(1.0 - P_e) < 1e-9:",
          "+        return 1.0",
          "+    return (P_bar - P_e) / (1.0 - P_e)",
          "+",
          "+",
          "+def compute_inter_annotator_agreement(gold_records):",
          "+    \"\"\"Compute inter-annotator agreement on gold labels.",
          "+",
          "+    Args:",
          "+        gold_records: list of dicts with window_id, gold_label, optional annotator_id.",
          "+",
          "+    Returns:",
          "+        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),",
          "+        value (float | None), passed (bool).",
          "+    \"\"\"",
          "+    annotators = set()",
          "+    for r in gold_records:",
          "+        aid = r.get(\"annotator_id\")",
          "+        if aid is not None:",
          "+            annotators.add(aid)",
          "+",
          "+    if len(annotators) <= 1:",
          "+        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")",
          "+        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}",
          "+",
          "+    by_window = defaultdict(dict)",
          "+    for r in gold_records:",
          "+        aid = r.get(\"annotator_id\")",
          "+        if aid is not None:",
          "+            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]",
          "+",
          "+    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}",
          "+    if not multi_annotated:",
          "+        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")",
          "+        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}",
          "+",
          "+    n_annotators = len(annotators)",
          "+",
          "+    if n_annotators == 2:",
          "+        ann_list = sorted(annotators)",
          "+        y1, y2 = [], []",
          "+        for wid, labels in multi_annotated.items():",
          "+            if ann_list[0] in labels and ann_list[1] in labels:",
          "+                y1.append(labels[ann_list[0]])",
          "+                y2.append(labels[ann_list[1]])",
          "+        if not y1:",
          "+            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}",
          "+        kappa = cohen_kappa_score(y1, y2)",
          "+        metric_name = \"cohens_kappa\"",
          "+    else:",
          "+        categories = sorted({r[\"gold_label\"] for r in gold_records})",
          "+        cat_idx = {c: i for i, c in enumerate(categories)}",
          "+        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)",
          "+        for row_i, (wid, labels) in enumerate(multi_annotated.items()):",
          "+            for aid, lbl in labels.items():",
          "+                table[row_i, cat_idx[lbl]] += 1",
          "+        kappa = _fleiss_kappa(table)",
          "+        metric_name = \"fleiss_kappa\"",
          "+",
          "+    passed = kappa >= 0.8",
          "+    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"",
          "+    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")",
          "+    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")",
          "+    if not passed:",
          "+        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")",
          "+",
          "+    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}",
          "+",
          "+",
          "+# ===========================================================================",
          "+# Pairwise statistical tests",
          "+# ===========================================================================",
          "+",
          "+def _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):",
          "+    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.",
          "+",
          "+    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).",
          "+    \"\"\"",
          "+    rng = np.random.RandomState(seed)",
          "+    y_true = np.asarray(y_true)",
          "+    preds_a = np.asarray(preds_a)",
          "+    preds_b = np.asarray(preds_b)",
          "+    n = len(y_true)",
          "+    diffs = []",
          "+    for _ in range(n_bootstrap):",
          "+        idx = rng.randint(0, n, size=n)",
          "+        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)",
          "+        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)",
          "+        diffs.append(f1_a - f1_b)",
          "+    diffs = np.array(diffs)",
          "+    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))",
          "+",
          "+",
          "+def _mcnemar_test(y_true, preds_a, preds_b):",
          "+    \"\"\"McNemar's test (with continuity correction) comparing two models.",
          "+",
          "+    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.",
          "+    \"\"\"",
          "+    from scipy.stats import chi2",
          "+",
          "+    y_true = np.asarray(y_true)",
          "+    preds_a = np.asarray(preds_a)",
          "+    preds_b = np.asarray(preds_b)",
          "+",
          "+    correct_a = (preds_a == y_true)",
          "+    correct_b = (preds_b == y_true)",
          "+    # b: A correct, B wrong; c: A wrong, B correct",
          "+    b = int(np.sum(correct_a & ~correct_b))",
          "+    c = int(np.sum(~correct_a & correct_b))",
          "+",
          "+    if b + c == 0:",
          "+        return 1.0",
          "+    stat = (abs(b - c) - 1) ** 2 / (b + c)",
          "+    return float(chi2.sf(stat, df=1))",
          "+",
          "+",
          "+def compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):",
          "+    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.",
          "+",
          "+    Args:",
          "+        gold_wids: list of window IDs (gold order).",
          "+        gold_labels: list of gold labels.",
          "+        model_preds: dict {model_name: {wid: predicted_label}}.",
          "+",
          "+    Returns:",
          "+        dict of pairwise results keyed as \"model_a_vs_model_b\".",
          "+    \"\"\"",
          "+    gold_map = dict(zip(gold_wids, gold_labels))",
          "+    model_names = list(model_preds.keys())",
          "+    results = {}",
          "+",
          "+    for name_a, name_b in combinations(model_names, 2):",
          "+        preds_a_map = model_preds[name_a]",
          "+        preds_b_map = model_preds[name_b]",
          "+        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())",
          "+        if len(common_wids) < 10:",
          "+            continue",
          "+",
          "+        wids = sorted(common_wids)",
          "+        y_true = [gold_map[w] for w in wids]",
          "+        pa = [preds_a_map[w] for w in wids]",
          "+        pb = [preds_b_map[w] for w in wids]",
          "+",
          "+        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)",
          "+        p_val = _mcnemar_test(y_true, pa, pb)",
          "+",
          "+        key = f\"{name_a}_vs_{name_b}\"",
          "+        results[key] = {",
          "+            \"n_common\": len(wids),",
          "+            \"bootstrap_mean_diff\": round(mean_diff, 6),",
          "+            \"ci_95_lower\": round(ci_lo, 6),",
          "+            \"ci_95_upper\": round(ci_hi, 6),",
          "+            \"mcnemar_p\": round(p_val, 6),",
          "+        }",
          "+",
          "+    return results",
          "+",
          "+",
          "+# ===========================================================================",
          " # Data loading helpers",
          " # ===========================================================================",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 28_

Now modify the evaluate functions to also return pred_maps. Let me do all four:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "894a9e50-0123-4d23-9ec7-2991063c7b4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqnRoqWM9JFV8Dou9d7Yn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 52723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 2,
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01T3M7qFQck2qVdraTWiTQhJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "def evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map",
  "new_string": "def evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "264423d2-b2ec-474f-8be3-4aa1a9de68e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqnRoqWM9JFV8Dou9d7Yn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 52723,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 2,
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


### Runtime record

_source line 30_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778814000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a4af5f31-46ac-4b4f-907c-2d8c03241ad6",
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b"
}
```

---


### Tool result

_source line 31 · 2026-05-14T22:53:02.644Z_

<details><summary>↩ Tool result · `toolu_01T3M7qFQck2qVdraTWiTQhJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "5ae7aaa0-2df8-495c-93bd-7b9c0d607507",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "def evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map",
    "newString": "def evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 549,
        "oldLines": 8,
        "newStart": 549,
        "newLines": 8,
        "lines": [
          "         conf_map[wid] = w.get(\"confidence\", 0)",
          "     gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)",
          "     if not gold_al:",
          "-        return None, 0, {}, {}, {}",
          "-    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map",
          "+        return None, 0, {}, {}, {}, {}",
          "+    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map",
          " ",
          " ",
          " def evaluate_structural_clf("
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_014SXhJRdiMvSZdT51bTN275`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe",
  "new_string": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "adfe3e0e-e7d2-4668-a7f7-0fafb8f8cfb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHqEuAhAH8ohNy21zng67W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 55287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 33 · 2026-05-14T22:53:08.045Z_

<details><summary>↩ Tool result · `toolu_014SXhJRdiMvSZdT51bTN275`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "b01ee057-d3cb-47b6-8af5-52483b800eb2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe",
    "newString": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 600,
        "oldLines": 8,
        "newStart": 600,
        "newLines": 8,
        "lines": [
          " ",
          "     gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)",
          "     if not gold_al:",
          "-        return None, 0, n_miss, prob_map",
          "-    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map",
          "+        return None, 0, n_miss, prob_map, pred_map",
          "+    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map",
          " ",
          " ",
          " def evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01KrzG7j5JsPLWUiNNbsptm3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}",
  "new_string": "    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "fbf46e18-2567-4cd0-b503-275c48d03c36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPG6As2nBj8ppcEtS7X8ZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 55963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 35 · 2026-05-14T22:53:12.878Z_

<details><summary>↩ Tool result · `toolu_01KrzG7j5JsPLWUiNNbsptm3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "dbb1843c-9131-41e8-a1d1-12840b18332b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}",
    "newString": "    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 607,
        "oldLines": 7,
        "newStart": 607,
        "newLines": 7,
        "lines": [
          " def evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):",
          "     \"\"\"GRU probe evaluation on gold windows.\"\"\"",
          "     if not HAS_TORCH or not HAS_PROBE:",
          "-        return None, 0, len(gold_wids), {}",
          "+        return None, 0, len(gold_wids), {}, {}",
          " ",
          "     ckpt_path = Path(ckpt_path)",
          "     if not ckpt_path.exists():"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01XN7K39FrDfrGnXNwVEQRAA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}",
  "new_string": "    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "c6699ad3-3990-4069-ad20-b9ef752e4a42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147dBugwhCThEEY4Uy7cV6D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 56346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 37 · 2026-05-14T22:53:16.064Z_

<details><summary>↩ Tool result · `toolu_01XN7K39FrDfrGnXNwVEQRAA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "49726212-9da9-48fc-b254-e9d82be964d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}",
    "newString": "    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 611,
        "oldLines": 7,
        "newStart": 611,
        "newLines": 7,
        "lines": [
          " ",
          "     ckpt_path = Path(ckpt_path)",
          "     if not ckpt_path.exists():",
          "-        return None, 0, len(gold_wids), {}",
          "+        return None, 0, len(gold_wids), {}, {}",
          " ",
          "     ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)",
          "     model = ProgressProbe("
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_013ZHHok9te69fNmvMR21gGp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    if not gold_embs:\n        return None, 0, n_miss, {}",
  "new_string": "    if not gold_embs:\n        return None, 0, n_miss, {}, {}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "20483b68-385f-4f80-b3e2-36af5f906c7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfM5ktP9qwtowmnYDycKWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 56611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 39 · 2026-05-14T22:53:19.435Z_

<details><summary>↩ Tool result · `toolu_013ZHHok9te69fNmvMR21gGp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "bdf50a47-d0fa-45b4-83fd-f92744ca01d6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    if not gold_embs:\n        return None, 0, n_miss, {}",
    "newString": "    if not gold_embs:\n        return None, 0, n_miss, {}, {}",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 636,
        "oldLines": 7,
        "newStart": 636,
        "newLines": 7,
        "lines": [
          "         valid_gold.append(gl)",
          " ",
          "     if not gold_embs:",
          "-        return None, 0, n_miss, {}",
          "+        return None, 0, n_miss, {}, {}",
          " ",
          "     ds = WindowDataset(gold_embs, valid_gold)",
          "     loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 40_

Now update the GRU probe return to include pred_map:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "a09525ac-df69-428f-a2ea-25f87b69792f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ySrMgfgA9i5SgYhdvHjZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 56898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01LqhmYcWSRNHQ6Hya1qciNR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map",
  "new_string": "    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "46b5a7d2-6a38-4a71-afde-31744e564ab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ySrMgfgA9i5SgYhdvHjZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 56898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 42 · 2026-05-14T22:53:23.989Z_

<details><summary>↩ Tool result · `toolu_01LqhmYcWSRNHQ6Hya1qciNR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "d633afcc-3652-41e8-a8af-19739094f2d8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map",
    "newString": "    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 654,
        "oldLines": 7,
        "newStart": 654,
        "newLines": 8,
        "lines": [
          "             all_labels.extend(labels.long().tolist())",
          " ",
          "     prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}",
          "-    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map",
          "+    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}",
          "+    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out",
          " ",
          " ",
          " def evaluate_llm_judge(gold_wids, gold_labels, predictions_path):"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 43_

Now update `evaluate_llm_judge` returns:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "1311b20a-973c-44ea-b471-bbefb7277d1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WHMvbdS7DVPi4MNVUgrKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 57245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01UCXmuVroKVCho8heSoxA1Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}",
  "new_string": "    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}, {}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "4f62fec3-0942-4713-9a67-591324ad62d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WHMvbdS7DVPi4MNVUgrKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 57245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
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

_source line 45 · 2026-05-14T22:53:27.425Z_

<details><summary>↩ Tool result · `toolu_01UCXmuVroKVCho8heSoxA1Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "cc9c5805-2920-4e4d-8d2f-2b64710444ad",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}",
    "newString": "    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}, {}",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 662,
        "oldLines": 7,
        "newStart": 662,
        "newLines": 7,
        "lines": [
          "     \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"",
          "     predictions_path = Path(predictions_path)",
          "     if not predictions_path.exists():",
          "-        return None, 0, len(gold_wids), {}",
          "+        return None, 0, len(gold_wids), {}, {}",
          " ",
          "     pred_index = {}",
          "     if predictions_path.suffix == \".jsonl\":"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_011bpkPqysUKdTpuAJsVY6Vu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification",
  "new_string": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\n# ===========================================================================\n# Confidence stratification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "c4d41f8c-2fc7-442d-9d21-8a05a5909ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjWkDJqmHhaFgbGkv5pDpc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 57612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 264
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

_source line 47 · 2026-05-14T22:53:32.022Z_

<details><summary>↩ Tool result · `toolu_011bpkPqysUKdTpuAJsVY6Vu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "66f5a370-f8b3-426c-bf7c-e950cfd430d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification",
    "newString": "    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\n# ===========================================================================\n# Confidence stratification",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nPre-evaluation checks:\n  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)\n    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.\n\nPost-evaluation statistics:\n  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)\n  - McNemar's test for pairwise model comparisons\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib, scipy\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter, defaultdict\nfrom difflib import SequenceMatcher\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\nSTRUCTURAL_FEATURE_NAMES = [\n    \"num_steps\", \"num_actions\", \"num_observations\", \"action_ratio\",\n    \"mean_text_len\", \"std_text_len\", \"max_text_len\", \"min_text_len\",\n    \"mean_action_len\", \"mean_obs_len\", \"text_len_trend\",\n    \"num_commands\", \"mean_cmd_len\", \"max_cmd_len\",\n    \"unique_cmd_ratio\", \"max_repeat_ratio\",\n    \"num_edit_cmds\", \"num_search_cmds\", \"num_nav_cmds\", \"num_submit_cmds\",\n    \"edit_ratio\", \"search_ratio\",\n    \"avg_adjacent_cmd_sim\", \"max_adjacent_cmd_sim\", \"max_consecutive_similar\",\n    \"num_errors\", \"num_test_outputs\", \"num_file_displays\", \"num_nonzero_exits\",\n    \"is_short_trajectory\",\n]\n_EXPECTED_FEATURE_DIM = 30\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    vec = np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (\n        f\"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}\"\n    )\n    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (\n        f\"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}\"\n    )\n    return vec\n\n\n# ===========================================================================\n# Inter-annotator agreement\n# ===========================================================================\n\ndef _fleiss_kappa(table):\n    \"\"\"Fleiss' κ for multiple raters.\n\n    Args:\n        table: (N, k) array where N = items, k = categories.\n               table[i, j] = number of raters who assigned category j to item i.\n\n    Reference: Fleiss, J.L. (1971). \"Measuring nominal scale agreement among\n    many raters.\" Psychological Bulletin, 76(5), 378–382.\n    \"\"\"\n    N, k = table.shape\n    n = table[0].sum()\n    if n <= 1 or N == 0:\n        return 0.0\n\n    p_j = table.sum(axis=0) / (N * n)\n    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))\n    P_bar = np.mean(P_i)\n    P_e = np.sum(p_j ** 2)\n\n    if abs(1.0 - P_e) < 1e-9:\n        return 1.0\n    return (P_bar - P_e) / (1.0 - P_e)\n\n\ndef compute_inter_annotator_agreement(gold_records):\n    \"\"\"Compute inter-annotator agreement on gold labels.\n\n    Args:\n        gold_records: list of dicts with window_id, gold_label, optional annotator_id.\n\n    Returns:\n        dict with keys: n_annotators, metric (\"cohens_kappa\" | \"fleiss_kappa\" | None),\n        value (float | None), passed (bool).\n    \"\"\"\n    annotators = set()\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            annotators.add(aid)\n\n    if len(annotators) <= 1:\n        print(\"  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.\")\n        return {\"n_annotators\": max(len(annotators), 1), \"metric\": None, \"value\": None, \"passed\": True}\n\n    by_window = defaultdict(dict)\n    for r in gold_records:\n        aid = r.get(\"annotator_id\")\n        if aid is not None:\n            by_window[r[\"window_id\"]][aid] = r[\"gold_label\"]\n\n    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}\n    if not multi_annotated:\n        print(\"  WARNING: No windows with multiple annotations; skipping IAA check.\")\n        return {\"n_annotators\": len(annotators), \"metric\": None, \"value\": None, \"passed\": True}\n\n    n_annotators = len(annotators)\n\n    if n_annotators == 2:\n        ann_list = sorted(annotators)\n        y1, y2 = [], []\n        for wid, labels in multi_annotated.items():\n            if ann_list[0] in labels and ann_list[1] in labels:\n                y1.append(labels[ann_list[0]])\n                y2.append(labels[ann_list[1]])\n        if not y1:\n            return {\"n_annotators\": 2, \"metric\": None, \"value\": None, \"passed\": True}\n        kappa = cohen_kappa_score(y1, y2)\n        metric_name = \"cohens_kappa\"\n    else:\n        categories = sorted({r[\"gold_label\"] for r in gold_records})\n        cat_idx = {c: i for i, c in enumerate(categories)}\n        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)\n        for row_i, (wid, labels) in enumerate(multi_annotated.items()):\n            for aid, lbl in labels.items():\n                table[row_i, cat_idx[lbl]] += 1\n        kappa = _fleiss_kappa(table)\n        metric_name = \"fleiss_kappa\"\n\n    passed = kappa >= 0.8\n    status = \"PASS\" if passed else \"WARNING — below 0.8 threshold\"\n    print(f\"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]\")\n    print(f\"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}\")\n    if not passed:\n        print(\"  WARNING: Low agreement. Results may be unreliable. Continuing anyway.\")\n\n    return {\"n_annotators\": n_annotators, \"metric\": metric_name, \"value\": round(kappa, 6), \"passed\": passed}\n\n\n# ===========================================================================\n# Pairwise statistical tests\n# ===========================================================================\n\ndef _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for the difference in macro-F1 between two models.\n\n    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n    n = len(y_true)\n    diffs = []\n    for _ in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        f1_a = f1_score(y_true[idx], preds_a[idx], average=\"macro\", zero_division=0)\n        f1_b = f1_score(y_true[idx], preds_b[idx], average=\"macro\", zero_division=0)\n        diffs.append(f1_a - f1_b)\n    diffs = np.array(diffs)\n    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))\n\n\ndef _mcnemar_test(y_true, preds_a, preds_b):\n    \"\"\"McNemar's test (with continuity correction) comparing two models.\n\n    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.\n    \"\"\"\n    from scipy.stats import chi2\n\n    y_true = np.asarray(y_true)\n    preds_a = np.asarray(preds_a)\n    preds_b = np.asarray(preds_b)\n\n    correct_a = (preds_a == y_true)\n    correct_b = (preds_b == y_true)\n    # b: A correct, B wrong; c: A wrong, B correct\n    b = int(np.sum(correct_a & ~correct_b))\n    c = int(np.sum(~correct_a & correct_b))\n\n    if b + c == 0:\n        return 1.0\n    stat = (abs(b - c) - 1) ** 2 / (b + c)\n    return float(chi2.sf(stat, df=1))\n\n\ndef compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):\n    \"\"\"Compute bootstrap CIs and McNemar tests for all model pairs.\n\n    Args:\n        gold_wids: list of window IDs (gold order).\n        gold_labels: list of gold labels.\n        model_preds: dict {model_name: {wid: predicted_label}}.\n\n    Returns:\n        dict of pairwise results keyed as \"model_a_vs_model_b\".\n    \"\"\"\n    gold_map = dict(zip(gold_wids, gold_labels))\n    model_names = list(model_preds.keys())\n    results = {}\n\n    for name_a, name_b in combinations(model_names, 2):\n        preds_a_map = model_preds[name_a]\n        preds_b_map = model_preds[name_b]\n        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())\n        if len(common_wids) < 10:\n            continue\n\n        wids = sorted(common_wids)\n        y_true = [gold_map[w] for w in wids]\n        pa = [preds_a_map[w] for w in wids]\n        pb = [preds_b_map[w] for w in wids]\n\n        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)\n        p_val = _mcnemar_test(y_true, pa, pb)\n\n        key = f\"{name_a}_vs_{name_b}\"\n        results[key] = {\n            \"n_common\": len(wids),\n            \"bootstrap_mean_diff\": round(mean_diff, 6),\n            \"ci_95_lower\": round(ci_lo, 6),\n            \"ci_95_upper\": round(ci_hi, 6),\n            \"mcnemar_p\": round(p_val, 6),\n        }\n\n    return results\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map, pred_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}, {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}, {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 692,
        "oldLines": 8,
        "newStart": 692,
        "newLines": 8,
        "lines": [
          " ",
          "     gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)",
          "     if not gold_al:",
          "-        return None, 0, n_miss, prob_map",
          "-    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map",
          "+        return None, 0, n_miss, prob_map, pred_map",
          "+    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map",
          " ",
          " ",
          " # ==========================================================================="
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 48_

Now update the main function. Let me read the current state of main() to make precise edits:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "d656e899-0abb-4321-95c4-31bdd93d128a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6eGdhfB27VEUPHCqDykU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 57876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01VZsBWjzZwYS9fv1oBMmGDR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "offset": 750
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "13222614-c969-4796-8fbd-cc13c4d5d58b",
  "uuid": "2d431563-89d6-49fe-8524-aea092f2d52f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6eGdhfB27VEUPHCqDykU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 57876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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
