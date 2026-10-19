# code analyze divergence

**error diag dpo recovery** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_code_analyze-divergence_20260513T063822.log`
- **Structured JSON:** [`a1a1c6140a223b8adc11.json`](../../sessions/a1/a1a1c6140a223b8adc11.json)

## Before a recorded user message

34 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
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
  "uuid": "bbbb4f9f-b771-4fce-a1a9-a3022b41ebdb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-rl-active-probe-fl/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1778821200,
    "rateLimitType": "seven_day",
    "utilization": 0.76,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "7e1f58eb-678d-4b0d-90dc-bd59f8b582db",
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the reference files to understand the data formats and logic, then write the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "25a4d5b1-7623-4766-8078-766706874683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN3zzDKZGEB6Wx51NrYwYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12190
      },
      "output_tokens": 28,
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

Reading the three reference files to understand data formats and divergence logic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "e347c878-6fb0-4a1a-abcb-2f5a9a624c79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN3zzDKZGEB6Wx51NrYwYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12190
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — Read · `toolu_0162kh6C1umX9v1pcCBJZLFL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "035fbef2-dc05-41f9-bfa3-cd3fc09beef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN3zzDKZGEB6Wx51NrYwYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12190
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-13T06:38:33.038Z_

<details><summary>↩ Tool result · `toolu_0162kh6C1umX9v1pcCBJZLFL`</summary>

```text
1	"""Build DPO preference pairs from classified failures and expert trajectories.
2	
3	Fix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.
4	Old logic used failure_step as split point, but expert and failure trajectories
5	may already differ before that step → prompt-chosen state inconsistency.
6	New logic compares action sequences step-by-step to find the real divergence.
7	
8	For each classified failure:
9	  1. Match expert trajectory by game_file
10	  2. Compare actions step-by-step to find divergence point
11	  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected
12	
13	Input:
14	  - classified_errors.jsonl (error_type, failure_step, conversations)
15	  - alfworld_sft.json (expert trajectories)
16	  - (optional) trajectory_dir with failure JSONL files
17	
18	Output per line:
19	  {prompt, chosen, rejected, error_type, gamma_e, correction_span,
20	   task_id, task_type, game_file, failure_step, divergence_step, metadata}
21	
22	Usage:
23	  python src/build_dpo_pairs.py \
24	    --classified outputs/classify_compare_with_hint_20.jsonl \
25	    --expert data/alfworld_sft.json \
26	    --output data/dpo_pairs_v2.jsonl \
27	    --gamma action=0.85,verification=0.92,planning=0.97
28	
29	Dependencies: (stdlib only)
30	"""
31	
32	import argparse
33	import json
34	import logging
35	from collections import Counter, defaultdict
36	from pathlib import Path
37	
38	logger = logging.getLogger("build_dpo")
39	
40	DEFAULT_GAMMA_MAP = {
41	    "action": 0.85,
42	    "verification": 0.92,
43	    "planning": 0.97,
44	}
45	
46	
47	def parse_gamma_arg(s: str) -> dict[str, float]:
48	    """Parse 'action=0.85,verification=0.92,planning=0.97' → dict."""
49	    gamma_map = dict(DEFAULT_GAMMA_MAP)
50	    for item in s.split(","):
51	        k, v = item.strip().split("=")
52	        gamma_map[k.strip()] = float(v.strip())
53	    return gamma_map
54	
55	
56	# ---------------------------------------------------------------------------
57	# Game file normalization
58	# ---------------------------------------------------------------------------
59	
60	def normalize_game_file(game_file: str) -> str:
61	    """Extract &lt;task_dir>/&lt;trial_dir> as matching key.
62	
63	    Expert:     data/json_2.1.1/train/&lt;task>/&lt;trial>
64	    Trajectory: /root/.../json_2.1.1/train/&lt;task>/&lt;trial>/game.tw-pddl
65	    """
66	    gf = game_file.rstrip("/")
67	    if gf.endswith("/game.tw-pddl"):
68	        gf = gf[: -len("/game.tw-pddl")]
69	    parts = gf.split("/")
70	    return "/".join(parts[-2:]) if len(parts) >= 2 else gf
71	
72	
73	# ---------------------------------------------------------------------------
74	# Message helpers
75	# ---------------------------------------------------------------------------
76	
77	def _role(msg: dict) -> str:
78	    """Get role from either format."""
79	    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")
80	
81	
82	def _content(msg: dict) -> str:
83	    """Get content from either format."""
84	    return msg.get("content") or msg.get("value", "")
85	
86	
87	def msg_to_standard(msg: dict) -> dict:
88	    return {"role": _role(msg), "content": _content(msg)}
89	
90	
91	# ---------------------------------------------------------------------------
92	# Step extraction
93	# ---------------------------------------------------------------------------
94	
95	def find_task_start(conversations: list) -> int:
96	    """Index of first action step after the actual task description.
97	
98	    Handles both expert (no ICL) and trajectory (with ICL prefix) formats by
99	    finding the LAST 'Your task is to:' user message, then the first action after it.
100	    """
101	    task_desc_idx = -1
102	    for i, msg in enumerate(conversations):
103	        if _role(msg) in ("user", "human") and "Your task is to:" in _content(msg):
104	            task_desc_idx = i
105	
106	    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0
107	    for i in range(search_from, len(conversations)):
108	        if _role(conversations[i]) in ("assistant", "gpt") and "Action:" in _content(conversations[i]):
109	            return i
110	
111	    return len(conversations)
112	
113	
114	def extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:
115	    """Extract (action_msg, obs_msg|None) pairs from start_idx onward."""
116	    steps = []
117	    i = start_idx
118	    while i < len(conversations):
119	        if _role(conversations[i]) in ("assistant", "gpt"):
120	            action = conversations[i]
121	            obs = None
122	            if i + 1 < len(conversations) and _role(conversations[i + 1]) in ("user", "human"):
123	                obs = conversations[i + 1]
124	                i += 2
125	            else:
126	                i += 1
127	            steps.append((action, obs))
128	        else:
129	            i += 1
130	    return steps
131	
132	
133	def count_expert_action_steps(expert: dict) -> int:
134	    return sum(
135	        1
136	        for m in expert["conversations"]
137	        if m["from"] == "gpt" and "Action:" in m.get("value", "")
138	    )
139	
140	
141	# ---------------------------------------------------------------------------
142	# Action comparison
143	# ---------------------------------------------------------------------------
144	
145	def extract_action_text(content: str) -> str:
146	    """Extract normalized 'Action: ...' line from a step message.
147	
148	    ALFWorld actions follow "Thought: ...\\nAction: &lt;action>". We extract
149	    the action part and normalize whitespace + case for robust comparison.
150	    """
151	    for line in content.split("\n"):
152	        stripped = line.strip()
153	        if stripped.lower().startswith("action:"):
154	            return " ".join(stripped[len("action:"):].split()).lower()
155	    return " ".join(content.split()).lower()
156	
157	
158	def find_divergence_point(
159	    expert_steps: list[tuple[dict, dict | None]],
160	    fail_steps: list[tuple[dict, dict | None]],
161	) -> int:
162	    """Find the first step where expert and failure trajectories take different actions.
163	
164	    Compares normalized action strings step-by-step. In ALFWorld, same game_file
165	    + same actions → same observations, so action match guarantees state match.
166	
167	    Args:
168	        expert_steps: List of (action_msg, obs_msg|None) from expert trajectory.
169	        fail_steps: List of (action_msg, obs_msg|None) from failure trajectory.
170	
171	    Returns:
172	        0-based index of the first differing step. If one is a prefix of the
173	        other, returns the shorter length (no shared step beyond that).
174	    """
175	    min_len = min(len(expert_steps), len(fail_steps))
176	    for i in range(min_len):
177	        expert_action = extract_action_text(_content(expert_steps[i][0]))
178	        fail_action = extract_action_text(_content(fail_steps[i][0]))
179	        if expert_action != fail_action:
180	            return i
181	    return min_len
182	
183	
184	# ---------------------------------------------------------------------------
185	# Pair construction
186	# ---------------------------------------------------------------------------
187	
188	def build_pair(
189	    rec: dict,
190	    expert: dict,
191	    gamma_map: dict[str, float] | None = None,
192	) -> dict | None:
193	    """Build one DPO pair using true divergence point between expert and failure."""
194	    if gamma_map is None:
195	        gamma_map = DEFAULT_GAMMA_MAP
196	
197	    fail_convs = rec["conversations"]
198	    expert_convs = expert["conversations"]
199	
200	    fail_start = find_task_start(fail_convs)
201	    expert_start = find_task_start(expert_convs)
202	
203	    fail_steps = extract_steps(fail_convs, fail_start)
204	    expert_steps = extract_steps(expert_convs, expert_start)
205	
206	    if not fail_steps or not expert_steps:
207	        return None
208	
209	    divergence = find_divergence_point(expert_steps, fail_steps)
210	
211	    if divergence >= len(expert_steps) or divergence >= len(fail_steps):
212	        logger.debug(
213	            "task_id=%s: no divergence found (expert=%d, fail=%d steps, div=%d)",
214	            rec.get("task_id"), len(expert_steps), len(fail_steps), divergence,
215	        )
216	        return None
217	
218	    correction_span = len(expert_steps) - divergence
219	    error_type = rec.get("error_type", "unknown")
220	
221	    # Prompt: ICL/header + shared prefix steps (identical actions + observations)
222	    prompt_msgs = [msg_to_standard(m) for m in fail_convs[:fail_start]]
223	    for i in range(divergence):
224	        action, obs = expert_steps[i]
225	        prompt_msgs.append(msg_to_standard(action))
226	        if obs is not None:
227	            prompt_msgs.append(msg_to_standard(obs))
228	
229	    # Chosen: expert continuation from divergence point
230	    chosen_msgs = []
231	    for i in range(divergence, len(expert_steps)):
232	        action, obs = expert_steps[i]
233	        chosen_msgs.append(msg_to_standard(action))
234	        if obs is not None:
235	            chosen_msgs.append(msg_to_standard(obs))
236	
237	    # Rejected: failure continuation from divergence point
238	    rejected_msgs = []
239	    for i in range(divergence, len(fail_steps)):
240	        action, obs = fail_steps[i]
241	        rejected_msgs.append(msg_to_standard(action))
242	        if obs is not None:
243	            rejected_msgs.append(msg_to_standard(obs))
244	
245	    if not chosen_msgs or not rejected_msgs:
246	        return None
247	
248	    # Infer task_type from expert game_file (format: &lt;task_type>/&lt;trial_id>)
249	    gf = expert.get("game_file", "")
250	    parts = gf.split("/")
251	    task_type = ""
252	    for p in parts:
253	        if p.startswith(("pick_", "clean_", "heat_", "cool_", "put_", "examine_", "look_")):
254	            task_type = p
255	            break
256	    if not task_type:
257	        task_type = rec.get("task_type", "")
258	
259	    return {
260	        "prompt": prompt_msgs,
261	        "chosen": chosen_msgs,
262	        "rejected": rejected_msgs,
263	        "error_type": error_type,
264	        "gamma_e": gamma_map.get(error_type, gamma_map.get("verification", 0.92)),
265	        "correction_span": correction_span,
266	        "task_id": rec.get("task_id"),
267	        "task_type": task_type,
268	        "game_file": rec.get("game_file", ""),
269	        "failure_step": rec.get("failure_step", -1),
270	        "divergence_step": divergence + 1,
271	        "metadata": {
272	            "expert_steps": len(expert_steps),
273	            "model_steps": len(fail_steps),
274	            "divergence_step": divergence,
275	            "classification_source": rec.get("llm_original_type_source", "unknown"),
276	        },
277	    }
278	
279	
280	# ---------------------------------------------------------------------------
281	# Data loading
282	# ---------------------------------------------------------------------------
283	
284	def load_expert_index(path: str) -> dict:
285	    with open(path) as f:
286	        experts = json.load(f)
287	    index = {}
288	    for ex in experts:
289	        index[normalize_game_file(ex["game_file"])] = ex
290	    logger.info("Loaded %d experts", len(experts))
291	    return index
292	
293	
294	def load_classified(path: str) -> list:
295	    records = []
296	    with open(path) as f:
297	        for line in f:
298	            if line.strip():
299	                records.append(json.loads(line))
300	    logger.info("Loaded %d classified records", len(records))
301	    return records
302	
303	
304	def load_trajectories_from_dir(traj_dir: str) -> dict:
305	    """Index trajectory files by normalized game_file (fallback for missing conversations)."""
306	    index = {}
307	    for p in sorted(Path(traj_dir).glob("*.jsonl")):
308	        with open(p) as f:
309	            for line in f:
310	                if line.strip():
311	                    traj = json.loads(line)
312	                    index[normalize_game_file(traj.get("game_file", ""))] = traj
313	    logger.info("Loaded %d trajectories from %s", len(index), traj_dir)
314	    return index
315	
316	
317	# ---------------------------------------------------------------------------
318	# Main
319	# ---------------------------------------------------------------------------
320	
321	def main():
322	    parser = argparse.ArgumentParser(
323	        description="Build DPO pairs from classified failures + expert trajectories"
324	    )
325	    parser.add_argument(
326	        "--classified",
327	        type=str,
328	        default="data/classified/classified_errors.jsonl",
329	        help="Classified errors JSONL",
330	    )
331	    parser.add_argument(
332	        "--expert",
333	        type=str,
334	        default="eto_repo/data/alfworld_sft.json",
335	        help="Expert trajectories JSON",
336	    )
337	    parser.add_argument(
338	        "--trajectory_dir",
339	        type=str,
340	        default=None,
341	        help="Failure trajectory JSONL dir (optional; uses classified conversations if omitted)",
342	    )
343	    parser.add_argument(
344	        "--output",
345	        type=str,
346	        default="data/dpo_pairs_v2.jsonl",
347	        help="Output JSONL path",
348	    )
349	    parser.add_argument(
350	        "--gamma",
351	        type=str,
352	        default="action=0.85,verification=0.92,planning=0.97",
353	        help="Per-error-type γ_e values: action=0.85,verification=0.92,planning=0.97",
354	    )
355	    args = parser.parse_args()
356	
357	    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")
358	
359	    gamma_map = parse_gamma_arg(args.gamma)
360	    logger.info("γ_e map: %s", gamma_map)
361	
362	    expert_index = load_expert_index(args.expert)
363	    classified = load_classified(args.classified)
364	
365	    traj_index = None
366	    if args.trajectory_dir:
367	        traj_index = load_trajectories_from_dir(args.trajectory_dir)
368	
369	    out = Path(args.output)
370	    out.parent.mkdir(parents=True, exist_ok=True)
371	
372	    pairs = []
373	    skipped: Counter = Counter()
374	
375	    for rec in classified:
376	        if rec.get("error_type") in ("unknown", None):
377	            skipped["unknown_error_type"] += 1
378	            continue
379	
380	        key = normalize_game_file(rec.get("game_file", ""))
381	        expert = expert_index.get(key)
382	        if expert is None:
383	            skipped["no_expert_match"] += 1
384	            continue
385	
386	        if not rec.get("conversations"):
387	            if traj_index:
388	                traj = traj_index.get(key)
389	                if traj and traj.get("conversations"):
390	                    rec["conversations"] = traj["conversations"]
391	                else:
392	                    skipped["no_conversations"] += 1
393	                    continue
394	            else:
395	                skipped["no_conversations"] += 1
396	                continue
397	
398	        pair = build_pair(rec, expert, gamma_map)
399	        if pair is None:
400	            skipped["build_failed"] += 1
401	            continue
402	        pairs.append(pair)
403	
404	    with open(out, "w") as f:
405	        for pair in pairs:
406	            f.write(json.dumps(pair, ensure_ascii=False) + "\n")
407	
408	    logger.info("Built %d DPO pairs -> %s", len(pairs), out)
409	    if skipped:
410	        logger.info("Skipped: %s", dict(skipped))
411	
412	    # --- summary ---
413	    by_type: dict[str, list[int]] = defaultdict(list)
414	    div_steps: list[int] = []
415	    for p in pairs:
416	        by_type[p["error_type"]].append(p["correction_span"])
417	        div_steps.append(p["divergence_step"])
418	
419	    print(f"\n{'=' * 50}")
420	    print("DPO PAIR CONSTRUCTION SUMMARY")
421	    print(f"{'=' * 50}")
422	    print(f"Total pairs: {len(pairs)}")
423	    print(f"\n{'Type':<15} {'Count':>6} {'Avg CSpan':>10} {'γ_e':>6}")
424	    print("-" * 42)
425	    for et in ("action", "verification", "planning"):
426	        spans = by_type.get(et, [])
427	        ge = gamma_map.get(et, "-")
428	        if spans:
429	            avg = sum(spans) / len(spans)
430	            print(f"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}")
431	        else:
432	            print(f"{et:<15}      0          - {ge:>6}")
433	    if div_steps:
434	        print(f"\nDivergence step distribution:")
435	        print(f"  min={min(div_steps)}, max={max(div_steps)}, "
436	              f"mean={sum(div_steps)/len(div_steps):.1f}, "
437	              f"step1={sum(1 for d in div_steps if d == 1)}")
438	    if skipped:
439	        print(f"\nSkipped: {dict(skipped)}")
440	    print(f"{'=' * 50}")
441	
442	
443	if __name__ == "__main__":
444	    main()
445	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "b1cf85c7-72e7-44d0-b122-3558e85ce133",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py",
      "content": "\"\"\"Build DPO preference pairs from classified failures and expert trajectories.\n\nFix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.\nOld logic used failure_step as split point, but expert and failure trajectories\nmay already differ before that step → prompt-chosen state inconsistency.\nNew logic compares action sequences step-by-step to find the real divergence.\n\nFor each classified failure:\n  1. Match expert trajectory by game_file\n  2. Compare actions step-by-step to find divergence point\n  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected\n\nInput:\n  - classified_errors.jsonl (error_type, failure_step, conversations)\n  - alfworld_sft.json (expert trajectories)\n  - (optional) trajectory_dir with failure JSONL files\n\nOutput per line:\n  {prompt, chosen, rejected, error_type, gamma_e, correction_span,\n   task_id, task_type, game_file, failure_step, divergence_step, metadata}\n\nUsage:\n  python src/build_dpo_pairs.py \\\n    --classified outputs/classify_compare_with_hint_20.jsonl \\\n    --expert data/alfworld_sft.json \\\n    --output data/dpo_pairs_v2.jsonl \\\n    --gamma action=0.85,verification=0.92,planning=0.97\n\nDependencies: (stdlib only)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\nlogger = logging.getLogger(\"build_dpo\")\n\nDEFAULT_GAMMA_MAP = {\n    \"action\": 0.85,\n    \"verification\": 0.92,\n    \"planning\": 0.97,\n}\n\n\ndef parse_gamma_arg(s: str) -> dict[str, float]:\n    \"\"\"Parse 'action=0.85,verification=0.92,planning=0.97' → dict.\"\"\"\n    gamma_map = dict(DEFAULT_GAMMA_MAP)\n    for item in s.split(\",\"):\n        k, v = item.strip().split(\"=\")\n        gamma_map[k.strip()] = float(v.strip())\n    return gamma_map\n\n\n# ---------------------------------------------------------------------------\n# Game file normalization\n# ---------------------------------------------------------------------------\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\n\n    Expert:     data/json_2.1.1/train/&lt;task>/&lt;trial>\n    Trajectory: /root/.../json_2.1.1/train/&lt;task>/&lt;trial>/game.tw-pddl\n    \"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    \"\"\"Get role from either format.\"\"\"\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    \"\"\"Get content from either format.\"\"\"\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef msg_to_standard(msg: dict) -> dict:\n    return {\"role\": _role(msg), \"content\": _content(msg)}\n\n\n# ---------------------------------------------------------------------------\n# Step extraction\n# ---------------------------------------------------------------------------\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the actual task description.\n\n    Handles both expert (no ICL) and trajectory (with ICL prefix) formats by\n    finding the LAST 'Your task is to:' user message, then the first action after it.\n    \"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef count_expert_action_steps(expert: dict) -> int:\n    return sum(\n        1\n        for m in expert[\"conversations\"]\n        if m[\"from\"] == \"gpt\" and \"Action:\" in m.get(\"value\", \"\")\n    )\n\n\n# ---------------------------------------------------------------------------\n# Action comparison\n# ---------------------------------------------------------------------------\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract normalized 'Action: ...' line from a step message.\n\n    ALFWorld actions follow \"Thought: ...\\\\nAction: &lt;action>\". We extract\n    the action part and normalize whitespace + case for robust comparison.\n    \"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\ndef find_divergence_point(\n    expert_steps: list[tuple[dict, dict | None]],\n    fail_steps: list[tuple[dict, dict | None]],\n) -> int:\n    \"\"\"Find the first step where expert and failure trajectories take different actions.\n\n    Compares normalized action strings step-by-step. In ALFWorld, same game_file\n    + same actions → same observations, so action match guarantees state match.\n\n    Args:\n        expert_steps: List of (action_msg, obs_msg|None) from expert trajectory.\n        fail_steps: List of (action_msg, obs_msg|None) from failure trajectory.\n\n    Returns:\n        0-based index of the first differing step. If one is a prefix of the\n        other, returns the shorter length (no shared step beyond that).\n    \"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        expert_action = extract_action_text(_content(expert_steps[i][0]))\n        fail_action = extract_action_text(_content(fail_steps[i][0]))\n        if expert_action != fail_action:\n            return i\n    return min_len\n\n\n# ---------------------------------------------------------------------------\n# Pair construction\n# ---------------------------------------------------------------------------\n\ndef build_pair(\n    rec: dict,\n    expert: dict,\n    gamma_map: dict[str, float] | None = None,\n) -> dict | None:\n    \"\"\"Build one DPO pair using true divergence point between expert and failure.\"\"\"\n    if gamma_map is None:\n        gamma_map = DEFAULT_GAMMA_MAP\n\n    fail_convs = rec[\"conversations\"]\n    expert_convs = expert[\"conversations\"]\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    divergence = find_divergence_point(expert_steps, fail_steps)\n\n    if divergence >= len(expert_steps) or divergence >= len(fail_steps):\n        logger.debug(\n            \"task_id=%s: no divergence found (expert=%d, fail=%d steps, div=%d)\",\n            rec.get(\"task_id\"), len(expert_steps), len(fail_steps), divergence,\n        )\n        return None\n\n    correction_span = len(expert_steps) - divergence\n    error_type = rec.get(\"error_type\", \"unknown\")\n\n    # Prompt: ICL/header + shared prefix steps (identical actions + observations)\n    prompt_msgs = [msg_to_standard(m) for m in fail_convs[:fail_start]]\n    for i in range(divergence):\n        action, obs = expert_steps[i]\n        prompt_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            prompt_msgs.append(msg_to_standard(obs))\n\n    # Chosen: expert continuation from divergence point\n    chosen_msgs = []\n    for i in range(divergence, len(expert_steps)):\n        action, obs = expert_steps[i]\n        chosen_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            chosen_msgs.append(msg_to_standard(obs))\n\n    # Rejected: failure continuation from divergence point\n    rejected_msgs = []\n    for i in range(divergence, len(fail_steps)):\n        action, obs = fail_steps[i]\n        rejected_msgs.append(msg_to_standard(action))\n        if obs is not None:\n            rejected_msgs.append(msg_to_standard(obs))\n\n    if not chosen_msgs or not rejected_msgs:\n        return None\n\n    # Infer task_type from expert game_file (format: &lt;task_type>/&lt;trial_id>)\n    gf = expert.get(\"game_file\", \"\")\n    parts = gf.split(\"/\")\n    task_type = \"\"\n    for p in parts:\n        if p.startswith((\"pick_\", \"clean_\", \"heat_\", \"cool_\", \"put_\", \"examine_\", \"look_\")):\n            task_type = p\n            break\n    if not task_type:\n        task_type = rec.get(\"task_type\", \"\")\n\n    return {\n        \"prompt\": prompt_msgs,\n        \"chosen\": chosen_msgs,\n        \"rejected\": rejected_msgs,\n        \"error_type\": error_type,\n        \"gamma_e\": gamma_map.get(error_type, gamma_map.get(\"verification\", 0.92)),\n        \"correction_span\": correction_span,\n        \"task_id\": rec.get(\"task_id\"),\n        \"task_type\": task_type,\n        \"game_file\": rec.get(\"game_file\", \"\"),\n        \"failure_step\": rec.get(\"failure_step\", -1),\n        \"divergence_step\": divergence + 1,\n        \"metadata\": {\n            \"expert_steps\": len(expert_steps),\n            \"model_steps\": len(fail_steps),\n            \"divergence_step\": divergence,\n            \"classification_source\": rec.get(\"llm_original_type_source\", \"unknown\"),\n        },\n    }\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_expert_index(path: str) -> dict:\n    with open(path) as f:\n        experts = json.load(f)\n    index = {}\n    for ex in experts:\n        index[normalize_game_file(ex[\"game_file\"])] = ex\n    logger.info(\"Loaded %d experts\", len(experts))\n    return index\n\n\ndef load_classified(path: str) -> list:\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    logger.info(\"Loaded %d classified records\", len(records))\n    return records\n\n\ndef load_trajectories_from_dir(traj_dir: str) -> dict:\n    \"\"\"Index trajectory files by normalized game_file (fallback for missing conversations).\"\"\"\n    index = {}\n    for p in sorted(Path(traj_dir).glob(\"*.jsonl\")):\n        with open(p) as f:\n            for line in f:\n                if line.strip():\n                    traj = json.loads(line)\n                    index[normalize_game_file(traj.get(\"game_file\", \"\"))] = traj\n    logger.info(\"Loaded %d trajectories from %s\", len(index), traj_dir)\n    return index\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Build DPO pairs from classified failures + expert trajectories\"\n    )\n    parser.add_argument(\n        \"--classified\",\n        type=str,\n        default=\"data/classified/classified_errors.jsonl\",\n        help=\"Classified errors JSONL\",\n    )\n    parser.add_argument(\n        \"--expert\",\n        type=str,\n        default=\"eto_repo/data/alfworld_sft.json\",\n        help=\"Expert trajectories JSON\",\n    )\n    parser.add_argument(\n        \"--trajectory_dir\",\n        type=str,\n        default=None,\n        help=\"Failure trajectory JSONL dir (optional; uses classified conversations if omitted)\",\n    )\n    parser.add_argument(\n        \"--output\",\n        type=str,\n        default=\"data/dpo_pairs_v2.jsonl\",\n        help=\"Output JSONL path\",\n    )\n    parser.add_argument(\n        \"--gamma\",\n        type=str,\n        default=\"action=0.85,verification=0.92,planning=0.97\",\n        help=\"Per-error-type γ_e values: action=0.85,verification=0.92,planning=0.97\",\n    )\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(name)s %(levelname)s %(message)s\")\n\n    gamma_map = parse_gamma_arg(args.gamma)\n    logger.info(\"γ_e map: %s\", gamma_map)\n\n    expert_index = load_expert_index(args.expert)\n    classified = load_classified(args.classified)\n\n    traj_index = None\n    if args.trajectory_dir:\n        traj_index = load_trajectories_from_dir(args.trajectory_dir)\n\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n\n    pairs = []\n    skipped: Counter = Counter()\n\n    for rec in classified:\n        if rec.get(\"error_type\") in (\"unknown\", None):\n            skipped[\"unknown_error_type\"] += 1\n            continue\n\n        key = normalize_game_file(rec.get(\"game_file\", \"\"))\n        expert = expert_index.get(key)\n        if expert is None:\n            skipped[\"no_expert_match\"] += 1\n            continue\n\n        if not rec.get(\"conversations\"):\n            if traj_index:\n                traj = traj_index.get(key)\n                if traj and traj.get(\"conversations\"):\n                    rec[\"conversations\"] = traj[\"conversations\"]\n                else:\n                    skipped[\"no_conversations\"] += 1\n                    continue\n            else:\n                skipped[\"no_conversations\"] += 1\n                continue\n\n        pair = build_pair(rec, expert, gamma_map)\n        if pair is None:\n            skipped[\"build_failed\"] += 1\n            continue\n        pairs.append(pair)\n\n    with open(out, \"w\") as f:\n        for pair in pairs:\n            f.write(json.dumps(pair, ensure_ascii=False) + \"\\n\")\n\n    logger.info(\"Built %d DPO pairs -> %s\", len(pairs), out)\n    if skipped:\n        logger.info(\"Skipped: %s\", dict(skipped))\n\n    # --- summary ---\n    by_type: dict[str, list[int]] = defaultdict(list)\n    div_steps: list[int] = []\n    for p in pairs:\n        by_type[p[\"error_type\"]].append(p[\"correction_span\"])\n        div_steps.append(p[\"divergence_step\"])\n\n    print(f\"\\n{'=' * 50}\")\n    print(\"DPO PAIR CONSTRUCTION SUMMARY\")\n    print(f\"{'=' * 50}\")\n    print(f\"Total pairs: {len(pairs)}\")\n    print(f\"\\n{'Type':<15} {'Count':>6} {'Avg CSpan':>10} {'γ_e':>6}\")\n    print(\"-\" * 42)\n    for et in (\"action\", \"verification\", \"planning\"):\n        spans = by_type.get(et, [])\n        ge = gamma_map.get(et, \"-\")\n        if spans:\n            avg = sum(spans) / len(spans)\n            print(f\"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}\")\n        else:\n            print(f\"{et:<15}      0          - {ge:>6}\")\n    if div_steps:\n        print(f\"\\nDivergence step distribution:\")\n        print(f\"  min={min(div_steps)}, max={max(div_steps)}, \"\n              f\"mean={sum(div_steps)/len(div_steps):.1f}, \"\n              f\"step1={sum(1 for d in div_steps if d == 1)}\")\n    if skipped:\n        print(f\"\\nSkipped: {dict(skipped)}\")\n    print(f\"{'=' * 50}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 445,
      "startLine": 1,
      "totalLines": 445
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01CrpdEEHwj3QcAvxFeA5ar6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "e8a69272-6f5f-4da3-ac52-b95c70e70c8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN3zzDKZGEB6Wx51NrYwYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12190
      },
      "output_tokens": 28,
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

_source line 9 · 2026-05-13T06:38:33.521Z_

<details><summary>↩ Tool result · `toolu_01CrpdEEHwj3QcAvxFeA5ar6`</summary>

```text
1	"""ALFWorld trajectory collection with ICL few-shot from expert data.
2	
3	Uses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from
4	expert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.
5	
6	Usage:
7	  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \
8	    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \
9	    --gpu 0 --num_tasks 300 --seed 42 \
10	    --part_num 2 --part_idx 0 \
11	    --output_dir data/trajectories_v7_icl_cuda0
12	"""
13	
14	import os
15	import re
16	import json
17	import time
18	import random
19	import logging
20	import argparse
21	from pathlib import Path
22	from collections import defaultdict
23	
24	import yaml
25	import torch
26	import alfworld
27	from alfworld.agents.environment import get_environment
28	from transformers import AutoModelForCausalLM, AutoTokenizer
29	
30	logger = logging.getLogger("collect_traj_icl")
31	
32	PREFIXES = {
33	    "pick_and_place": "put",
34	    "pick_clean_then_place": "clean",
35	    "pick_heat_then_place": "heat",
36	    "pick_cool_then_place": "cool",
37	    "look_at_obj": "examine",
38	    "pick_two_obj": "puttwo",
39	}
40	
41	ALFWORLD_INSTRUCTION = (
42	    "Interact with a household to solve a task. Imagine you are an intelligent "
43	    "agent in a household environment and your target is to perform actions to "
44	    "complete the task goal. At the beginning of your interactions, you will be "
45	    "given the detailed description of the current environment and your goal to "
46	    "accomplish. \nFor each of your turn, you will be given the observation of "
47	    'the last turn. You should first think about the current condition and plan '
48	    'for your future actions, and then output your action in this turn. Your '
49	    'output must strictly follow this format:"Thought: your thoughts.\n'
50	    'Action: your next action".\n\n'
51	    "The available actions are:\n"
52	    "1. go to {recep}\n"
53	    "2. take {obj} from {recep}\n"
54	    "3. put {obj} in/on {recep}\n"
55	    "4. open {recep}\n"
56	    "5. close {recep}\n"
57	    "6. toggle {obj} {recep}\n"
58	    "7. clean {obj} with {recep}\n"
59	    "8. heat {obj} with {recep}\n"
60	    "9. cool {obj} with {recep}\n"
61	    "where {obj} and {recep} correspond to objects and receptacles.\n"
62	    "After your each turn, the environment will give you immediate feedback "
63	    'based on which you plan your next few steps. if the envrionment output '
64	    '"Nothing happened", that means the previous action is invalid and you '
65	    "should try more options.\n\n"
66	    "Your response should use the following format:\n\n"
67	    "Thought: &lt;your thoughts>\nAction: &lt;your next action>"
68	)
69	
70	
71	def get_task_type(game_file: str) -> str:
72	    for k in PREFIXES:
73	        if f"/{k}" in game_file:
74	            return k
75	    return "unknown"
76	
77	
78	def normalize_game_file(game_file: str) -> str:
79	    gf = game_file.rstrip("/")
80	    if gf.endswith("/game.tw-pddl"):
81	        gf = gf[: -len("/game.tw-pddl")]
82	    parts = gf.split("/")
83	    return "/".join(parts[-2:]) if len(parts) >= 2 else gf
84	
85	
86	def process_ob(ob: str) -> str:
87	    if ob.startswith("You arrive at loc "):
88	        ob = ob[ob.find(". ") + 2 :]
89	    return ob
90	
91	
92	def load_expert_data(expert_file: str, max_turns: int = 30) -> dict[str, list]:
93	    with open(expert_file) as f:
94	        sft_data = json.load(f)
95	
96	    by_type = defaultdict(list)
97	    for item in sft_data:
98	        tt = get_task_type(item["game_file"])
99	        convs = item["conversations"]
100	        if len(convs) > 2:
101	            interaction = convs[2:]
102	        else:
103	            continue
104	        n_turns = len(interaction)
105	        if n_turns <= max_turns:
106	            by_type[tt].append({
107	                "game_file": item["game_file"],
108	                "normalized_gf": normalize_game_file(item["game_file"]),
109	                "task_type": tt,
110	                "n_turns": n_turns,
111	                "interaction": interaction,
112	            })
113	
114	    for tt in by_type:
115	        by_type[tt].sort(key=lambda x: x["n_turns"])
116	
117	    total = sum(len(v) for v in by_type.values())
118	    logger.info("Loaded %d expert examples across %d task types", total, len(by_type))
119	    for tt, examples in sorted(by_type.items()):
120	        logger.info("  %s: %d examples", tt, len(examples))
121	
122	    return dict(by_type)
123	
124	
125	def sample_icl_examples(
126	    expert_by_type: dict[str, list],
127	    task_type: str,
128	    exclude_game_file: str,
129	    num_examples: int = 2,
130	    rng: random.Random = None,
131	) -> list[list[dict]]:
132	    if rng is None:
133	        rng = random.Random(42)
134	
135	    exclude_key = normalize_game_file(exclude_game_file)
136	
137	    same_type = [
138	        ex for ex in expert_by_type.get(task_type, [])
139	        if ex["normalized_gf"] != exclude_key
140	    ]
141	
142	    other_type = []
143	    for tt, examples in expert_by_type.items():
144	        if tt == task_type:
145	            continue
146	        for ex in examples:
147	            if ex["normalized_gf"] != exclude_key:
148	                other_type.append(ex)
149	    other_type.sort(key=lambda x: x["n_turns"])
150	
151	    selected = []
152	    if len(same_type) >= num_examples:
153	        selected = rng.sample(same_type, num_examples)
154	    else:
155	        selected = list(same_type)
156	        remaining = num_examples - len(selected)
157	        if remaining > 0 and other_type:
158	            supplement = other_type[:remaining]
159	            selected.extend(supplement)
160	
161	    icl_messages = []
162	    for ex in selected:
163	        msgs = []
164	        for turn in ex["interaction"]:
165	            role = "user" if turn["from"] == "human" else "assistant"
166	            msgs.append({"role": role, "content": turn["value"]})
167	        icl_messages.append(msgs)
168	
169	    return icl_messages
170	
171	
172	def load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):
173	    alfworld_data = "/root/autodl-tmp/alfworld_data"
174	    os.environ["ALFWORLD_DATA"] = alfworld_data
175	
176	    with open(os.path.join(alfworld_data, "base_config.yaml")) as f:
177	        config = yaml.safe_load(f)
178	
179	    split_map = {
180	        "train": ("train", 3321),
181	        "dev": ("eval_in_distribution", 140),
182	        "test": ("eval_out_of_distribution", 134),
183	    }
184	    env_split, n_tasks = split_map[split]
185	
186	    EnvClass = get_environment(config["env"]["type"])
187	    env = EnvClass(config, train_eval=env_split)
188	    env = env.init_env(batch_size=1)
189	
190	    if part_num > 1:
191	        assert part_idx >= 0
192	        part_sizes = [n_tasks // part_num] * part_num
193	        part_sizes[-1] += n_tasks % part_num
194	        env.skip(sum(part_sizes[:part_idx]))
195	        n_tasks = part_sizes[part_idx]
196	
197	    def generator():
198	        for idx in range(n_tasks):
199	            obs, info = env.reset()
200	            obs_text = "\n".join(obs[0].split("\n\n")[1:])
201	            game_file = info["extra.gamefile"][0]
202	            yield {
203	                "task_id": idx,
204	                "game_file": game_file,
205	                "obs": obs_text,
206	                "env": env,
207	            }
208	
209	    return generator(), n_tasks
210	
211	
212	def load_model(model_name: str, gpu: int = 0):
213	    model = AutoModelForCausalLM.from_pretrained(
214	        model_name,
215	        device_map=f"cuda:{gpu}",
216	        trust_remote_code=True,
217	        torch_dtype=torch.float16,
218	    )
219	    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
220	    model.eval()
221	    return model, tokenizer
222	
223	
224	def build_icl_messages(
225	    instruction: str, icl_examples: list[list[dict]], task_obs: str,
226	) -> list:
227	    messages = [
228	        {"role": "user", "content": instruction},
229	        {"role": "assistant", "content": "OK"},
230	    ]
231	    for example in icl_examples:
232	        for turn in example:
233	            messages.append({"role": turn["role"], "content": turn["content"]})
234	    messages.append({"role": "user", "content": task_obs})
235	    return messages
236	
237	
238	def generate_response(
239	    model, tokenizer, messages: list,
240	    temperature: float = 0.7, max_new_tokens: int = 256,
241	) -> str:
242	    try:
243	        text = tokenizer.apply_chat_template(
244	            messages, tokenize=False, add_generation_prompt=True,
245	            enable_thinking=False,
246	        )
247	    except TypeError:
248	        text = tokenizer.apply_chat_template(
249	            messages, tokenize=False, add_generation_prompt=True,
250	        )
251	
252	    inputs = tokenizer(text, return_tensors="pt").to(model.device)
253	
254	    with torch.no_grad():
255	        outputs = model.generate(
256	            **inputs,
257	            max_new_tokens=max_new_tokens,
258	            do_sample=temperature > 0,
259	            temperature=temperature if temperature > 0 else None,
260	            top_p=0.9 if temperature > 0 else None,
261	            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
262	        )
263	
264	    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
265	    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
266	    response = re.sub(r"&lt;think>.*?&lt;/think>", "", response, flags=re.DOTALL).strip()
267	    return response
268	
269	
270	def parse_action(response: str) -> str:
271	    match = re.search(r"Action:\s*(.*)", response, re.DOTALL)
272	    if match:
273	        action = match.group(1).strip().split("\n")[0].strip()
274	        if action:
275	            return action
276	    return "look"
277	
278	
279	def collect_single_trajectory(
280	    task_info: dict,
281	    model, tokenizer,
282	    expert_by_type: dict,
283	    num_icl_examples: int = 2,
284	    temperature: float = 0.7,
285	    max_steps: int = 40,
286	    max_new_tokens: int = 256,
287	    rng: random.Random = None,
288	) -> dict:
289	    env = task_info["env"]
290	    task_obs = task_info["obs"]
291	    game_file = task_info["game_file"]
292	    task_id = task_info["task_id"]
293	    task_type = get_task_type(game_file)
294	
295	    icl_examples = sample_icl_examples(
296	        expert_by_type, task_type, game_file,
297	        num_examples=num_icl_examples, rng=rng,
298	    )
299	
300	    messages = build_icl_messages(ALFWORLD_INSTRUCTION, icl_examples, task_obs)
301	
302	    reward = False
303	    steps = 0
304	
305	    for _ in range(max_steps):
306	        response = generate_response(
307	            model, tokenizer, messages, temperature, max_new_tokens,
308	        )
309	        action = parse_action(response)
310	        messages.append({"role": "assistant", "content": response})
311	
312	        try:
313	            observation, env_reward, env_done, info = env.step([action])
314	            observation = process_ob(observation[0])
315	            reward = info["won"][0]
316	            done = env_done[0]
317	        except Exception as e:
318	            logger.warning("Task %d env.step error: %s", task_id, e)
319	            observation = "Invalid action."
320	            reward = False
321	            done = False
322	
323	        steps += 1
324	        messages.append({"role": "user", "content": f"Observation: {observation}"})
325	
326	        if done or reward:
327	            break
328	
329	    return {
330	        "task_id": task_id,
331	        "task_type": task_type,
332	        "game_file": game_file,
333	        "reward": bool(reward),
334	        "steps": steps,
335	        "conversations": messages,
336	    }
337	
338	
339	def main():
340	    parser = argparse.ArgumentParser("Collect ALFWorld trajectories with ICL few-shot")
341	    parser.add_argument("--model_name", type=str,
342	                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ")
343	    parser.add_argument("--expert_file", type=str,
344	                        default="data/alfworld_sft.json")
345	    parser.add_argument("--output_dir", type=str, default="data/trajectories")
346	    parser.add_argument("--split", type=str, default="train",
347	                        choices=["train", "dev", "test"])
348	    parser.add_argument("--temperature", type=float, default=0.7)
349	    parser.add_argument("--max_steps", type=int, default=40)
350	    parser.add_argument("--max_new_tokens", type=int, default=256)
351	    parser.add_argument("--gpu", type=int, default=0)
352	    parser.add_argument("--num_tasks", type=int, default=-1, help="-1 = all tasks")
353	    parser.add_argument("--num_icl_examples", type=int, default=2)
354	    parser.add_argument("--part_num", type=int, default=1)
355	    parser.add_argument("--part_idx", type=int, default=-1)
356	    parser.add_argument("--seed", type=int, default=42)
357	    parser.add_argument("--dry_run", action="store_true",
358	                        help="Validate pipeline with 2 tasks then exit")
359	    args = parser.parse_args()
360	
361	    logging.basicConfig(
362	        level=logging.INFO,
363	        format="%(asctime)s %(levelname)s %(message)s",
364	    )
365	
366	    rng = random.Random(args.seed)
367	    torch.manual_seed(args.seed)
368	
369	    logger.info("Loading expert data from %s...", args.expert_file)
370	    expert_by_type = load_expert_data(args.expert_file)
371	
372	    logger.info("Loading model: %s", args.model_name)
373	    model, tokenizer = load_model(args.model_name, args.gpu)
374	
375	    logger.info("Loading ALFWorld %s environment...", args.split)
376	    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)
377	
378	    if args.dry_run:
379	        n_tasks = min(2, n_tasks)
380	        logger.info("DRY RUN: collecting %d tasks only", n_tasks)
381	    elif args.num_tasks > 0:
382	        n_tasks = min(n_tasks, args.num_tasks)
383	
384	    output_dir = Path(args.output_dir)
385	    output_dir.mkdir(parents=True, exist_ok=True)
386	    suffix = f"_part{args.part_idx}" if args.part_num > 1 else ""
387	    output_file = output_dir / f"{args.split}{suffix}.jsonl"
388	
389	    logger.info("Collecting %d trajectories -> %s", n_tasks, output_file)
390	    logger.info("ICL examples per task: %d", args.num_icl_examples)
391	
392	    success_count = 0
393	    total_count = 0
394	
395	    with open(output_file, "w") as f:
396	        for i, task_info in enumerate(task_gen):
397	            if i >= n_tasks:
398	                break
399	
400	            t0 = time.time()
401	            traj = collect_single_trajectory(
402	                task_info, model, tokenizer,
403	                expert_by_type,
404	                num_icl_examples=args.num_icl_examples,
405	                temperature=args.temperature,
406	                max_steps=args.max_steps,
407	                max_new_tokens=args.max_new_tokens,
408	                rng=rng,
409	            )
410	            elapsed = time.time() - t0
411	
412	            total_count += 1
413	            if traj["reward"]:
414	                success_count += 1
415	
416	            f.write(json.dumps(traj, ensure_ascii=False) + "\n")
417	            f.flush()
418	
419	            logger.info(
420	                "[%d/%d] task=%d type=%s reward=%s steps=%d time=%.1fs sr=%d/%d",
421	                total_count, n_tasks, traj["task_id"],
422	                traj["task_type"], traj["reward"],
423	                traj["steps"], elapsed,
424	                success_count, total_count,
425	            )
426	
427	    logger.info(
428	        "Done. %d/%d succeeded (%.1f%%)",
429	        success_count, total_count,
430	        success_count / max(total_count, 1) * 100,
431	    )
432	
433	
434	if __name__ == "__main__":
435	    main()
436	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "26bdb9c2-5b55-447a-ba39-7ee8796a9ac8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py",
      "content": "\"\"\"ALFWorld trajectory collection with ICL few-shot from expert data.\n\nUses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from\nexpert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.\n\nUsage:\n  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \\\n    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \\\n    --gpu 0 --num_tasks 300 --seed 42 \\\n    --part_num 2 --part_idx 0 \\\n    --output_dir data/trajectories_v7_icl_cuda0\n\"\"\"\n\nimport os\nimport re\nimport json\nimport time\nimport random\nimport logging\nimport argparse\nfrom pathlib import Path\nfrom collections import defaultdict\n\nimport yaml\nimport torch\nimport alfworld\nfrom alfworld.agents.environment import get_environment\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogger = logging.getLogger(\"collect_traj_icl\")\n\nPREFIXES = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\nALFWORLD_INSTRUCTION = (\n    \"Interact with a household to solve a task. Imagine you are an intelligent \"\n    \"agent in a household environment and your target is to perform actions to \"\n    \"complete the task goal. At the beginning of your interactions, you will be \"\n    \"given the detailed description of the current environment and your goal to \"\n    \"accomplish. \\nFor each of your turn, you will be given the observation of \"\n    'the last turn. You should first think about the current condition and plan '\n    'for your future actions, and then output your action in this turn. Your '\n    'output must strictly follow this format:\"Thought: your thoughts.\\n'\n    'Action: your next action\".\\n\\n'\n    \"The available actions are:\\n\"\n    \"1. go to {recep}\\n\"\n    \"2. take {obj} from {recep}\\n\"\n    \"3. put {obj} in/on {recep}\\n\"\n    \"4. open {recep}\\n\"\n    \"5. close {recep}\\n\"\n    \"6. toggle {obj} {recep}\\n\"\n    \"7. clean {obj} with {recep}\\n\"\n    \"8. heat {obj} with {recep}\\n\"\n    \"9. cool {obj} with {recep}\\n\"\n    \"where {obj} and {recep} correspond to objects and receptacles.\\n\"\n    \"After your each turn, the environment will give you immediate feedback \"\n    'based on which you plan your next few steps. if the envrionment output '\n    '\"Nothing happened\", that means the previous action is invalid and you '\n    \"should try more options.\\n\\n\"\n    \"Your response should use the following format:\\n\\n\"\n    \"Thought: &lt;your thoughts>\\nAction: &lt;your next action>\"\n)\n\n\ndef get_task_type(game_file: str) -> str:\n    for k in PREFIXES:\n        if f\"/{k}\" in game_file:\n            return k\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\ndef process_ob(ob: str) -> str:\n    if ob.startswith(\"You arrive at loc \"):\n        ob = ob[ob.find(\". \") + 2 :]\n    return ob\n\n\ndef load_expert_data(expert_file: str, max_turns: int = 30) -> dict[str, list]:\n    with open(expert_file) as f:\n        sft_data = json.load(f)\n\n    by_type = defaultdict(list)\n    for item in sft_data:\n        tt = get_task_type(item[\"game_file\"])\n        convs = item[\"conversations\"]\n        if len(convs) > 2:\n            interaction = convs[2:]\n        else:\n            continue\n        n_turns = len(interaction)\n        if n_turns <= max_turns:\n            by_type[tt].append({\n                \"game_file\": item[\"game_file\"],\n                \"normalized_gf\": normalize_game_file(item[\"game_file\"]),\n                \"task_type\": tt,\n                \"n_turns\": n_turns,\n                \"interaction\": interaction,\n            })\n\n    for tt in by_type:\n        by_type[tt].sort(key=lambda x: x[\"n_turns\"])\n\n    total = sum(len(v) for v in by_type.values())\n    logger.info(\"Loaded %d expert examples across %d task types\", total, len(by_type))\n    for tt, examples in sorted(by_type.items()):\n        logger.info(\"  %s: %d examples\", tt, len(examples))\n\n    return dict(by_type)\n\n\ndef sample_icl_examples(\n    expert_by_type: dict[str, list],\n    task_type: str,\n    exclude_game_file: str,\n    num_examples: int = 2,\n    rng: random.Random = None,\n) -> list[list[dict]]:\n    if rng is None:\n        rng = random.Random(42)\n\n    exclude_key = normalize_game_file(exclude_game_file)\n\n    same_type = [\n        ex for ex in expert_by_type.get(task_type, [])\n        if ex[\"normalized_gf\"] != exclude_key\n    ]\n\n    other_type = []\n    for tt, examples in expert_by_type.items():\n        if tt == task_type:\n            continue\n        for ex in examples:\n            if ex[\"normalized_gf\"] != exclude_key:\n                other_type.append(ex)\n    other_type.sort(key=lambda x: x[\"n_turns\"])\n\n    selected = []\n    if len(same_type) >= num_examples:\n        selected = rng.sample(same_type, num_examples)\n    else:\n        selected = list(same_type)\n        remaining = num_examples - len(selected)\n        if remaining > 0 and other_type:\n            supplement = other_type[:remaining]\n            selected.extend(supplement)\n\n    icl_messages = []\n    for ex in selected:\n        msgs = []\n        for turn in ex[\"interaction\"]:\n            role = \"user\" if turn[\"from\"] == \"human\" else \"assistant\"\n            msgs.append({\"role\": role, \"content\": turn[\"value\"]})\n        icl_messages.append(msgs)\n\n    return icl_messages\n\n\ndef load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\n    alfworld_data = \"/root/autodl-tmp/alfworld_data\"\n    os.environ[\"ALFWORLD_DATA\"] = alfworld_data\n\n    with open(os.path.join(alfworld_data, \"base_config.yaml\")) as f:\n        config = yaml.safe_load(f)\n\n    split_map = {\n        \"train\": (\"train\", 3321),\n        \"dev\": (\"eval_in_distribution\", 140),\n        \"test\": (\"eval_out_of_distribution\", 134),\n    }\n    env_split, n_tasks = split_map[split]\n\n    EnvClass = get_environment(config[\"env\"][\"type\"])\n    env = EnvClass(config, train_eval=env_split)\n    env = env.init_env(batch_size=1)\n\n    if part_num > 1:\n        assert part_idx >= 0\n        part_sizes = [n_tasks // part_num] * part_num\n        part_sizes[-1] += n_tasks % part_num\n        env.skip(sum(part_sizes[:part_idx]))\n        n_tasks = part_sizes[part_idx]\n\n    def generator():\n        for idx in range(n_tasks):\n            obs, info = env.reset()\n            obs_text = \"\\n\".join(obs[0].split(\"\\n\\n\")[1:])\n            game_file = info[\"extra.gamefile\"][0]\n            yield {\n                \"task_id\": idx,\n                \"game_file\": game_file,\n                \"obs\": obs_text,\n                \"env\": env,\n            }\n\n    return generator(), n_tasks\n\n\ndef load_model(model_name: str, gpu: int = 0):\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name,\n        device_map=f\"cuda:{gpu}\",\n        trust_remote_code=True,\n        torch_dtype=torch.float16,\n    )\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    model.eval()\n    return model, tokenizer\n\n\ndef build_icl_messages(\n    instruction: str, icl_examples: list[list[dict]], task_obs: str,\n) -> list:\n    messages = [\n        {\"role\": \"user\", \"content\": instruction},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n    ]\n    for example in icl_examples:\n        for turn in example:\n            messages.append({\"role\": turn[\"role\"], \"content\": turn[\"content\"]})\n    messages.append({\"role\": \"user\", \"content\": task_obs})\n    return messages\n\n\ndef generate_response(\n    model, tokenizer, messages: list,\n    temperature: float = 0.7, max_new_tokens: int = 256,\n) -> str:\n    try:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n            enable_thinking=False,\n        )\n    except TypeError:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n        )\n\n    inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=temperature > 0,\n            temperature=temperature if temperature > 0 else None,\n            top_p=0.9 if temperature > 0 else None,\n            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,\n        )\n\n    new_tokens = outputs[0][inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    response = re.sub(r\"&lt;think>.*?&lt;/think>\", \"\", response, flags=re.DOTALL).strip()\n    return response\n\n\ndef parse_action(response: str) -> str:\n    match = re.search(r\"Action:\\s*(.*)\", response, re.DOTALL)\n    if match:\n        action = match.group(1).strip().split(\"\\n\")[0].strip()\n        if action:\n            return action\n    return \"look\"\n\n\ndef collect_single_trajectory(\n    task_info: dict,\n    model, tokenizer,\n    expert_by_type: dict,\n    num_icl_examples: int = 2,\n    temperature: float = 0.7,\n    max_steps: int = 40,\n    max_new_tokens: int = 256,\n    rng: random.Random = None,\n) -> dict:\n    env = task_info[\"env\"]\n    task_obs = task_info[\"obs\"]\n    game_file = task_info[\"game_file\"]\n    task_id = task_info[\"task_id\"]\n    task_type = get_task_type(game_file)\n\n    icl_examples = sample_icl_examples(\n        expert_by_type, task_type, game_file,\n        num_examples=num_icl_examples, rng=rng,\n    )\n\n    messages = build_icl_messages(ALFWORLD_INSTRUCTION, icl_examples, task_obs)\n\n    reward = False\n    steps = 0\n\n    for _ in range(max_steps):\n        response = generate_response(\n            model, tokenizer, messages, temperature, max_new_tokens,\n        )\n        action = parse_action(response)\n        messages.append({\"role\": \"assistant\", \"content\": response})\n\n        try:\n            observation, env_reward, env_done, info = env.step([action])\n            observation = process_ob(observation[0])\n            reward = info[\"won\"][0]\n            done = env_done[0]\n        except Exception as e:\n            logger.warning(\"Task %d env.step error: %s\", task_id, e)\n            observation = \"Invalid action.\"\n            reward = False\n            done = False\n\n        steps += 1\n        messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n\n        if done or reward:\n            break\n\n    return {\n        \"task_id\": task_id,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": bool(reward),\n        \"steps\": steps,\n        \"conversations\": messages,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\"Collect ALFWorld trajectories with ICL few-shot\")\n    parser.add_argument(\"--model_name\", type=str,\n                        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ\")\n    parser.add_argument(\"--expert_file\", type=str,\n                        default=\"data/alfworld_sft.json\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"data/trajectories\")\n    parser.add_argument(\"--split\", type=str, default=\"train\",\n                        choices=[\"train\", \"dev\", \"test\"])\n    parser.add_argument(\"--temperature\", type=float, default=0.7)\n    parser.add_argument(\"--max_steps\", type=int, default=40)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=256)\n    parser.add_argument(\"--gpu\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=-1, help=\"-1 = all tasks\")\n    parser.add_argument(\"--num_icl_examples\", type=int, default=2)\n    parser.add_argument(\"--part_num\", type=int, default=1)\n    parser.add_argument(\"--part_idx\", type=int, default=-1)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Validate pipeline with 2 tasks then exit\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s %(levelname)s %(message)s\",\n    )\n\n    rng = random.Random(args.seed)\n    torch.manual_seed(args.seed)\n\n    logger.info(\"Loading expert data from %s...\", args.expert_file)\n    expert_by_type = load_expert_data(args.expert_file)\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model, tokenizer = load_model(args.model_name, args.gpu)\n\n    logger.info(\"Loading ALFWorld %s environment...\", args.split)\n    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)\n\n    if args.dry_run:\n        n_tasks = min(2, n_tasks)\n        logger.info(\"DRY RUN: collecting %d tasks only\", n_tasks)\n    elif args.num_tasks > 0:\n        n_tasks = min(n_tasks, args.num_tasks)\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    suffix = f\"_part{args.part_idx}\" if args.part_num > 1 else \"\"\n    output_file = output_dir / f\"{args.split}{suffix}.jsonl\"\n\n    logger.info(\"Collecting %d trajectories -> %s\", n_tasks, output_file)\n    logger.info(\"ICL examples per task: %d\", args.num_icl_examples)\n\n    success_count = 0\n    total_count = 0\n\n    with open(output_file, \"w\") as f:\n        for i, task_info in enumerate(task_gen):\n            if i >= n_tasks:\n                break\n\n            t0 = time.time()\n            traj = collect_single_trajectory(\n                task_info, model, tokenizer,\n                expert_by_type,\n                num_icl_examples=args.num_icl_examples,\n                temperature=args.temperature,\n                max_steps=args.max_steps,\n                max_new_tokens=args.max_new_tokens,\n                rng=rng,\n            )\n            elapsed = time.time() - t0\n\n            total_count += 1\n            if traj[\"reward\"]:\n                success_count += 1\n\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n            f.flush()\n\n            logger.info(\n                \"[%d/%d] task=%d type=%s reward=%s steps=%d time=%.1fs sr=%d/%d\",\n                total_count, n_tasks, traj[\"task_id\"],\n                traj[\"task_type\"], traj[\"reward\"],\n                traj[\"steps\"], elapsed,\n                success_count, total_count,\n            )\n\n    logger.info(\n        \"Done. %d/%d succeeded (%.1f%%)\",\n        success_count, total_count,\n        success_count / max(total_count, 1) * 100,\n    )\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 436,
      "startLine": 1,
      "totalLines": 436
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01FThqkWfeyJK8AqUCF6anfD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "7f0b7d81-3b44-431c-96d7-b5467af6d409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN3zzDKZGEB6Wx51NrYwYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12190,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12190
      },
      "output_tokens": 28,
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

_source line 11 · 2026-05-13T06:38:33.904Z_

<details><summary>↩ Tool result · `toolu_01FThqkWfeyJK8AqUCF6anfD`</summary>

```text
1	#!/usr/bin/env python3
2	"""ETADN error-type-aware temporal discount for DMPO.
3	
4	Core formula:
5	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
6	
7	Where:
8	    t = current timestep (0-indexed)
9	    T = total trajectory length
10	    γ = gamma_e (error-type-specific discount factor)
11	
12	γ_e mapping:
13	    action errors      → γ_a = 0.85 (short correction span, concentrated credit)
14	    verification errors → γ_v = 0.92 (medium span, moderate spread)
15	    planning errors     → γ_p = 0.97 (long span, near-uniform credit)
16	
17	Integration with DPO/DMPO:
18	    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))
19	    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum
20	    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair
21	
22	Dependencies: torch only
23	"""
24	import torch
25	import torch.nn.functional as F
26	from dataclasses import dataclass
27	
28	
29	@dataclass
30	class ETADNConfig:
31	    gamma_action: float = 0.85
32	    gamma_verification: float = 0.92
33	    gamma_planning: float = 0.97
34	    beta: float = 0.1
35	    label_smoothing: float = 0.0
36	
37	
38	def phi(t: int, T: int, gamma: float) -> float:
39	    """DMPO credit assignment weight for timestep t of T.
40	
41	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
42	
43	    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).
44	    """
45	    if T <= 0:
46	        return 0.0
47	    if abs(gamma - 1.0) < 1e-8:
48	        return 1.0 / T
49	    if abs(gamma) < 1e-12:
50	        return 1.0 if t == 0 else 0.0
51	    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))
52	    denominator = 1.0 - gamma ** T
53	    return numerator / denominator
54	
55	
56	def compute_discount_weights(T: int, gamma: float) -> torch.Tensor:
57	    """φ weight vector of length T. Returns shape (T,) float32 tensor."""
58	    if T <= 0:
59	        return torch.tensor([], dtype=torch.float32)
60	    if abs(gamma - 1.0) < 1e-8:
61	        return torch.full((T,), 1.0 / T, dtype=torch.float32)
62	    if abs(gamma) < 1e-12:
63	        w = torch.zeros(T, dtype=torch.float32)
64	        w[0] = 1.0
65	        return w
66	    t = torch.arange(T, dtype=torch.float64)
67	    g = torch.tensor(gamma, dtype=torch.float64)
68	    numerator = g.pow(t) * (1 - g.pow(T - t))
69	    denominator = 1 - g.pow(torch.tensor(T, dtype=torch.float64))
70	    return (numerator / denominator).float()
71	
72	
73	def get_gamma_for_error_type(error_type: str, config: ETADNConfig) -> float:
74	    """Look up γ_e by error type string."""
75	    mapping = {
76	        "action": config.gamma_action,
77	        "verification": config.gamma_verification,
78	        "planning": config.gamma_planning,
79	    }
80	    return mapping.get(error_type, config.gamma_verification)
81	
82	
83	# ---------------------------------------------------------------------------
84	# DPO loss variants
85	# ---------------------------------------------------------------------------
86	
87	def _dpo_loss_from_logratios(
88	    chosen_logratios: torch.Tensor,
89	    rejected_logratios: torch.Tensor,
90	    beta: float,
91	    label_smoothing: float = 0.0,
92	) -> torch.Tensor:
93	    """Standard DPO loss from per-sample log-ratio scalars.
94	
95	    L = -log σ(β · (chosen_logratio - rejected_logratio))
96	    """
97	    logits = beta * (chosen_logratios - rejected_logratios)
98	    if label_smoothing > 0:
99	        loss = (
100	            (1 - label_smoothing) * F.logsigmoid(logits)
101	            + label_smoothing * F.logsigmoid(-logits)
102	        )
103	    else:
104	        loss = F.logsigmoid(logits)
105	    return -loss.mean()
106	
107	
108	def uniform_dpo_loss(
109	    chosen_logps: torch.Tensor,
110	    rejected_logps: torch.Tensor,
111	    ref_chosen_logps: torch.Tensor,
112	    ref_rejected_logps: torch.Tensor,
113	    lengths: torch.Tensor,
114	    beta: float = 0.1,
115	    label_smoothing: float = 0.0,
116	) -> torch.Tensor:
117	    """Standard DPO with uniform per-token weighting (baseline).
118	
119	    Args:
120	        chosen_logps: (batch, max_len) per-token log probs for chosen
121	        rejected_logps: (batch, max_len) per-token log probs for rejected
122	        ref_chosen_logps: (batch, max_len) reference model per-token log probs
123	        ref_rejected_logps: (batch, max_len) reference model per-token log probs
124	        lengths: (batch,) valid token count per sample
125	        beta: DPO temperature
126	        label_smoothing: label smoothing factor
127	    """
128	    batch_size, max_len = chosen_logps.shape
129	    mask = torch.arange(max_len, device=chosen_logps.device).unsqueeze(0) < lengths.unsqueeze(1)
130	    mask = mask.float()
131	
132	    chosen_sums = (chosen_logps * mask).sum(dim=1)
133	    rejected_sums = (rejected_logps * mask).sum(dim=1)
134	    ref_chosen_sums = (ref_chosen_logps * mask).sum(dim=1)
135	    ref_rejected_sums = (ref_rejected_logps * mask).sum(dim=1)
136	
137	    chosen_logratios = chosen_sums - ref_chosen_sums
138	    rejected_logratios = rejected_sums - ref_rejected_sums
139	
140	    return _dpo_loss_from_logratios(
141	        chosen_logratios, rejected_logratios, beta, label_smoothing
142	    )
143	
144	
145	def single_gamma_dpo_loss(
146	    chosen_logps: torch.Tensor,
147	    rejected_logps: torch.Tensor,
148	    ref_chosen_logps: torch.Tensor,
149	    ref_rejected_logps: torch.Tensor,
150	    lengths: torch.Tensor,
151	    gamma: float = 0.92,
152	    beta: float = 0.1,
153	    label_smoothing: float = 0.0,
154	) -> torch.Tensor:
155	    """DMPO with a single shared γ for all samples (ablation baseline)."""
156	    batch_size, max_len = chosen_logps.shape
157	    device = chosen_logps.device
158	
159	    results_chosen = torch.zeros(batch_size, device=device)
160	    results_rejected = torch.zeros(batch_size, device=device)
161	    results_ref_chosen = torch.zeros(batch_size, device=device)
162	    results_ref_rejected = torch.zeros(batch_size, device=device)
163	
164	    for i in range(batch_size):
165	        T = int(lengths[i].item())
166	        if T <= 0:
167	            continue
168	        w = compute_discount_weights(T, gamma).to(device)
169	        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
170	        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
171	        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
172	        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()
173	
174	    chosen_logratios = results_chosen - results_ref_chosen
175	    rejected_logratios = results_rejected - results_ref_rejected
176	
177	    return _dpo_loss_from_logratios(
178	        chosen_logratios, rejected_logratios, beta, label_smoothing
179	    )
180	
181	
182	def etadn_dpo_loss(
183	    chosen_logps: torch.Tensor,
184	    rejected_logps: torch.Tensor,
185	    ref_chosen_logps: torch.Tensor,
186	    ref_rejected_logps: torch.Tensor,
187	    error_types: list[str],
188	    lengths: torch.Tensor,
189	    config: ETADNConfig,
190	) -> torch.Tensor:
191	    """ETADN-aware DPO loss with per-error-type temporal discount.
192	
193	    For each sample in the batch:
194	    1. Look up γ_e based on error_type
195	    2. Compute φ(t, T, γ_e) weights for sequence length T
196	    3. Compute weighted sum of per-token log prob differences
197	    4. Apply standard DPO loss with β
198	    """
199	    batch_size, max_len = chosen_logps.shape
200	    device = chosen_logps.device
201	
202	    results_chosen = torch.zeros(batch_size, device=device)
203	    results_rejected = torch.zeros(batch_size, device=device)
204	    results_ref_chosen = torch.zeros(batch_size, device=device)
205	    results_ref_rejected = torch.zeros(batch_size, device=device)
206	
207	    for i in range(batch_size):
208	        T = int(lengths[i].item())
209	        if T <= 0:
210	            continue
211	        gamma = get_gamma_for_error_type(error_types[i], config)
212	        w = compute_discount_weights(T, gamma).to(device)
213	        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
214	        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
215	        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
216	        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()
217	
218	    chosen_logratios = results_chosen - results_ref_chosen
219	    rejected_logratios = results_rejected - results_ref_rejected
220	
221	    return _dpo_loss_from_logratios(
222	        chosen_logratios, rejected_logratios, config.beta, config.label_smoothing
223	    )
224	
225	
226	# ---------------------------------------------------------------------------
227	# Self-tests
228	# ---------------------------------------------------------------------------
229	
230	def _test_phi_weights_properties():
231	    """φ weights: positive, monotonically decreasing for γ<1, γ=1 is uniform."""
232	    for gamma in [0.5, 0.85, 0.92, 0.97, 0.99]:
233	        for T in [1, 3, 5, 10, 20]:
234	            w = compute_discount_weights(T, gamma)
235	            assert len(w) == T
236	            assert (w > 0).all(), f"gamma={gamma}, T={T}: non-positive weights"
237	            for i in range(1, T):
238	                assert w[i] <= w[i - 1] + 1e-6, (
239	                    f"gamma={gamma}, T={T}: not monotonically decreasing at {i}"
240	                )
241	    # γ=1 → uniform
242	    w_uniform = compute_discount_weights(5, 1.0)
243	    assert abs(w_uniform.sum().item() - 1.0) < 1e-5
244	    assert abs(w_uniform[0].item() - 0.2) < 1e-5
245	    # scalar φ matches vectorized
246	    for gamma in [0.85, 0.97]:
247	        T = 8
248	        w = compute_discount_weights(T, gamma)
249	        for t in range(T):
250	            assert abs(w[t].item() - phi(t, T, gamma)) < 1e-5, (
251	                f"phi mismatch at t={t}, T={T}, gamma={gamma}"
252	            )
253	    print("  phi weights properties: PASS")
254	
255	
256	def _test_phi_shape_by_gamma():
257	    """Lower γ → steeper decay; higher γ → more uniform."""
258	    T = 10
259	    w_low = compute_discount_weights(T, 0.85)
260	    w_high = compute_discount_weights(T, 0.97)
261	
262	    # φ(0,T,γ) = 1 for all γ, so first weight is the same
263	    assert abs(w_low[0].item() - 1.0) < 1e-5
264	    assert abs(w_high[0].item() - 1.0) < 1e-5
265	    # Lower γ decays faster → last weight should be smaller
266	    assert w_low[-1] < w_high[-1], "Low gamma should decay faster at the tail"
267	    # γ=0.97 should be more uniform (smaller max-min spread)
268	    spread_low = (w_low.max() - w_low.min()).item()
269	    spread_high = (w_high.max() - w_high.min()).item()
270	    assert spread_low > spread_high, "High gamma should be more uniform"
271	    print("  phi shape by gamma: PASS")
272	
273	
274	def _test_dpo_loss_gradients():
275	    """All three loss variants should produce finite loss and valid gradients."""
276	    torch.manual_seed(42)
277	    batch_size, max_len = 4, 8
278	    config = ETADNConfig()
279	
280	    chosen = torch.randn(batch_size, max_len, requires_grad=True)
281	    rejected = torch.randn(batch_size, max_len, requires_grad=True)
282	    ref_chosen = torch.randn(batch_size, max_len)
283	    ref_rejected = torch.randn(batch_size, max_len)
284	    lengths = torch.tensor([6, 8, 5, 7])
285	    error_types = ["action", "verification", "planning", "action"]
286	
287	    # Uniform DPO
288	    loss_u = uniform_dpo_loss(chosen, rejected, ref_chosen, ref_rejected, lengths)
289	    loss_u.backward(retain_graph=True)
290	    assert torch.isfinite(loss_u), f"uniform loss not finite: {loss_u}"
291	    assert chosen.grad is not None
292	    chosen.grad.zero_()
293	
294	    # Single-gamma DMPO
295	    loss_s = single_gamma_dpo_loss(
296	        chosen, rejected, ref_chosen, ref_rejected, lengths, gamma=0.92
297	    )
298	    loss_s.backward(retain_graph=True)
299	    assert torch.isfinite(loss_s), f"single_gamma loss not finite: {loss_s}"
300	    chosen.grad.zero_()
301	
302	    # ETADN
303	    loss_e = etadn_dpo_loss(
304	        chosen, rejected, ref_chosen, ref_rejected, error_types, lengths, config
305	    )
306	    loss_e.backward()
307	    assert torch.isfinite(loss_e), f"etadn loss not finite: {loss_e}"
308	
309	    print(f"  uniform_dpo_loss:      {loss_u.item():.4f}")
310	    print(f"  single_gamma_dpo_loss: {loss_s.item():.4f}")
311	    print(f"  etadn_dpo_loss:        {loss_e.item():.4f}")
312	    print("  gradient check: PASS")
313	
314	
315	def _test_gamma_lookup():
316	    """get_gamma_for_error_type should return correct values."""
317	    config = ETADNConfig()
318	    assert get_gamma_for_error_type("action", config) == 0.85
319	    assert get_gamma_for_error_type("verification", config) == 0.92
320	    assert get_gamma_for_error_type("planning", config) == 0.97
321	    assert get_gamma_for_error_type("unknown", config) == 0.92  # fallback
322	    print("  gamma lookup: PASS")
323	
324	
325	if __name__ == "__main__":
326	    print("ETADN discount module self-tests")
327	    print("=" * 40)
328	    _test_phi_weights_properties()
329	    _test_phi_shape_by_gamma()
330	    _test_gamma_lookup()
331	    _test_dpo_loss_gradients()
332	    print("=" * 40)
333	    print("All tests passed.")
334	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "1f356d08-81a2-421d-9f1b-256f373d54b5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py",
      "content": "#!/usr/bin/env python3\n\"\"\"ETADN error-type-aware temporal discount for DMPO.\n\nCore formula:\n    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n\nWhere:\n    t = current timestep (0-indexed)\n    T = total trajectory length\n    γ = gamma_e (error-type-specific discount factor)\n\nγ_e mapping:\n    action errors      → γ_a = 0.85 (short correction span, concentrated credit)\n    verification errors → γ_v = 0.92 (medium span, moderate spread)\n    planning errors     → γ_p = 0.97 (long span, near-uniform credit)\n\nIntegration with DPO/DMPO:\n    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))\n    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum\n    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair\n\nDependencies: torch only\n\"\"\"\nimport torch\nimport torch.nn.functional as F\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass ETADNConfig:\n    gamma_action: float = 0.85\n    gamma_verification: float = 0.92\n    gamma_planning: float = 0.97\n    beta: float = 0.1\n    label_smoothing: float = 0.0\n\n\ndef phi(t: int, T: int, gamma: float) -> float:\n    \"\"\"DMPO credit assignment weight for timestep t of T.\n\n    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n\n    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).\n    \"\"\"\n    if T <= 0:\n        return 0.0\n    if abs(gamma - 1.0) < 1e-8:\n        return 1.0 / T\n    if abs(gamma) < 1e-12:\n        return 1.0 if t == 0 else 0.0\n    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))\n    denominator = 1.0 - gamma ** T\n    return numerator / denominator\n\n\ndef compute_discount_weights(T: int, gamma: float) -> torch.Tensor:\n    \"\"\"φ weight vector of length T. Returns shape (T,) float32 tensor.\"\"\"\n    if T <= 0:\n        return torch.tensor([], dtype=torch.float32)\n    if abs(gamma - 1.0) < 1e-8:\n        return torch.full((T,), 1.0 / T, dtype=torch.float32)\n    if abs(gamma) < 1e-12:\n        w = torch.zeros(T, dtype=torch.float32)\n        w[0] = 1.0\n        return w\n    t = torch.arange(T, dtype=torch.float64)\n    g = torch.tensor(gamma, dtype=torch.float64)\n    numerator = g.pow(t) * (1 - g.pow(T - t))\n    denominator = 1 - g.pow(torch.tensor(T, dtype=torch.float64))\n    return (numerator / denominator).float()\n\n\ndef get_gamma_for_error_type(error_type: str, config: ETADNConfig) -> float:\n    \"\"\"Look up γ_e by error type string.\"\"\"\n    mapping = {\n        \"action\": config.gamma_action,\n        \"verification\": config.gamma_verification,\n        \"planning\": config.gamma_planning,\n    }\n    return mapping.get(error_type, config.gamma_verification)\n\n\n# ---------------------------------------------------------------------------\n# DPO loss variants\n# ---------------------------------------------------------------------------\n\ndef _dpo_loss_from_logratios(\n    chosen_logratios: torch.Tensor,\n    rejected_logratios: torch.Tensor,\n    beta: float,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"Standard DPO loss from per-sample log-ratio scalars.\n\n    L = -log σ(β · (chosen_logratio - rejected_logratio))\n    \"\"\"\n    logits = beta * (chosen_logratios - rejected_logratios)\n    if label_smoothing > 0:\n        loss = (\n            (1 - label_smoothing) * F.logsigmoid(logits)\n            + label_smoothing * F.logsigmoid(-logits)\n        )\n    else:\n        loss = F.logsigmoid(logits)\n    return -loss.mean()\n\n\ndef uniform_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    lengths: torch.Tensor,\n    beta: float = 0.1,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"Standard DPO with uniform per-token weighting (baseline).\n\n    Args:\n        chosen_logps: (batch, max_len) per-token log probs for chosen\n        rejected_logps: (batch, max_len) per-token log probs for rejected\n        ref_chosen_logps: (batch, max_len) reference model per-token log probs\n        ref_rejected_logps: (batch, max_len) reference model per-token log probs\n        lengths: (batch,) valid token count per sample\n        beta: DPO temperature\n        label_smoothing: label smoothing factor\n    \"\"\"\n    batch_size, max_len = chosen_logps.shape\n    mask = torch.arange(max_len, device=chosen_logps.device).unsqueeze(0) < lengths.unsqueeze(1)\n    mask = mask.float()\n\n    chosen_sums = (chosen_logps * mask).sum(dim=1)\n    rejected_sums = (rejected_logps * mask).sum(dim=1)\n    ref_chosen_sums = (ref_chosen_logps * mask).sum(dim=1)\n    ref_rejected_sums = (ref_rejected_logps * mask).sum(dim=1)\n\n    chosen_logratios = chosen_sums - ref_chosen_sums\n    rejected_logratios = rejected_sums - ref_rejected_sums\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, beta, label_smoothing\n    )\n\n\ndef single_gamma_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    lengths: torch.Tensor,\n    gamma: float = 0.92,\n    beta: float = 0.1,\n    label_smoothing: float = 0.0,\n) -> torch.Tensor:\n    \"\"\"DMPO with a single shared γ for all samples (ablation baseline).\"\"\"\n    batch_size, max_len = chosen_logps.shape\n    device = chosen_logps.device\n\n    results_chosen = torch.zeros(batch_size, device=device)\n    results_rejected = torch.zeros(batch_size, device=device)\n    results_ref_chosen = torch.zeros(batch_size, device=device)\n    results_ref_rejected = torch.zeros(batch_size, device=device)\n\n    for i in range(batch_size):\n        T = int(lengths[i].item())\n        if T <= 0:\n            continue\n        w = compute_discount_weights(T, gamma).to(device)\n        results_chosen[i] = (chosen_logps[i, :T] * w).sum()\n        results_rejected[i] = (rejected_logps[i, :T] * w).sum()\n        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()\n        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()\n\n    chosen_logratios = results_chosen - results_ref_chosen\n    rejected_logratios = results_rejected - results_ref_rejected\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, beta, label_smoothing\n    )\n\n\ndef etadn_dpo_loss(\n    chosen_logps: torch.Tensor,\n    rejected_logps: torch.Tensor,\n    ref_chosen_logps: torch.Tensor,\n    ref_rejected_logps: torch.Tensor,\n    error_types: list[str],\n    lengths: torch.Tensor,\n    config: ETADNConfig,\n) -> torch.Tensor:\n    \"\"\"ETADN-aware DPO loss with per-error-type temporal discount.\n\n    For each sample in the batch:\n    1. Look up γ_e based on error_type\n    2. Compute φ(t, T, γ_e) weights for sequence length T\n    3. Compute weighted sum of per-token log prob differences\n    4. Apply standard DPO loss with β\n    \"\"\"\n    batch_size, max_len = chosen_logps.shape\n    device = chosen_logps.device\n\n    results_chosen = torch.zeros(batch_size, device=device)\n    results_rejected = torch.zeros(batch_size, device=device)\n    results_ref_chosen = torch.zeros(batch_size, device=device)\n    results_ref_rejected = torch.zeros(batch_size, device=device)\n\n    for i in range(batch_size):\n        T = int(lengths[i].item())\n        if T <= 0:\n            continue\n        gamma = get_gamma_for_error_type(error_types[i], config)\n        w = compute_discount_weights(T, gamma).to(device)\n        results_chosen[i] = (chosen_logps[i, :T] * w).sum()\n        results_rejected[i] = (rejected_logps[i, :T] * w).sum()\n        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()\n        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()\n\n    chosen_logratios = results_chosen - results_ref_chosen\n    rejected_logratios = results_rejected - results_ref_rejected\n\n    return _dpo_loss_from_logratios(\n        chosen_logratios, rejected_logratios, config.beta, config.label_smoothing\n    )\n\n\n# ---------------------------------------------------------------------------\n# Self-tests\n# ---------------------------------------------------------------------------\n\ndef _test_phi_weights_properties():\n    \"\"\"φ weights: positive, monotonically decreasing for γ<1, γ=1 is uniform.\"\"\"\n    for gamma in [0.5, 0.85, 0.92, 0.97, 0.99]:\n        for T in [1, 3, 5, 10, 20]:\n            w = compute_discount_weights(T, gamma)\n            assert len(w) == T\n            assert (w > 0).all(), f\"gamma={gamma}, T={T}: non-positive weights\"\n            for i in range(1, T):\n                assert w[i] <= w[i - 1] + 1e-6, (\n                    f\"gamma={gamma}, T={T}: not monotonically decreasing at {i}\"\n                )\n    # γ=1 → uniform\n    w_uniform = compute_discount_weights(5, 1.0)\n    assert abs(w_uniform.sum().item() - 1.0) < 1e-5\n    assert abs(w_uniform[0].item() - 0.2) < 1e-5\n    # scalar φ matches vectorized\n    for gamma in [0.85, 0.97]:\n        T = 8\n        w = compute_discount_weights(T, gamma)\n        for t in range(T):\n            assert abs(w[t].item() - phi(t, T, gamma)) < 1e-5, (\n                f\"phi mismatch at t={t}, T={T}, gamma={gamma}\"\n            )\n    print(\"  phi weights properties: PASS\")\n\n\ndef _test_phi_shape_by_gamma():\n    \"\"\"Lower γ → steeper decay; higher γ → more uniform.\"\"\"\n    T = 10\n    w_low = compute_discount_weights(T, 0.85)\n    w_high = compute_discount_weights(T, 0.97)\n\n    # φ(0,T,γ) = 1 for all γ, so first weight is the same\n    assert abs(w_low[0].item() - 1.0) < 1e-5\n    assert abs(w_high[0].item() - 1.0) < 1e-5\n    # Lower γ decays faster → last weight should be smaller\n    assert w_low[-1] < w_high[-1], \"Low gamma should decay faster at the tail\"\n    # γ=0.97 should be more uniform (smaller max-min spread)\n    spread_low = (w_low.max() - w_low.min()).item()\n    spread_high = (w_high.max() - w_high.min()).item()\n    assert spread_low > spread_high, \"High gamma should be more uniform\"\n    print(\"  phi shape by gamma: PASS\")\n\n\ndef _test_dpo_loss_gradients():\n    \"\"\"All three loss variants should produce finite loss and valid gradients.\"\"\"\n    torch.manual_seed(42)\n    batch_size, max_len = 4, 8\n    config = ETADNConfig()\n\n    chosen = torch.randn(batch_size, max_len, requires_grad=True)\n    rejected = torch.randn(batch_size, max_len, requires_grad=True)\n    ref_chosen = torch.randn(batch_size, max_len)\n    ref_rejected = torch.randn(batch_size, max_len)\n    lengths = torch.tensor([6, 8, 5, 7])\n    error_types = [\"action\", \"verification\", \"planning\", \"action\"]\n\n    # Uniform DPO\n    loss_u = uniform_dpo_loss(chosen, rejected, ref_chosen, ref_rejected, lengths)\n    loss_u.backward(retain_graph=True)\n    assert torch.isfinite(loss_u), f\"uniform loss not finite: {loss_u}\"\n    assert chosen.grad is not None\n    chosen.grad.zero_()\n\n    # Single-gamma DMPO\n    loss_s = single_gamma_dpo_loss(\n        chosen, rejected, ref_chosen, ref_rejected, lengths, gamma=0.92\n    )\n    loss_s.backward(retain_graph=True)\n    assert torch.isfinite(loss_s), f\"single_gamma loss not finite: {loss_s}\"\n    chosen.grad.zero_()\n\n    # ETADN\n    loss_e = etadn_dpo_loss(\n        chosen, rejected, ref_chosen, ref_rejected, error_types, lengths, config\n    )\n    loss_e.backward()\n    assert torch.isfinite(loss_e), f\"etadn loss not finite: {loss_e}\"\n\n    print(f\"  uniform_dpo_loss:      {loss_u.item():.4f}\")\n    print(f\"  single_gamma_dpo_loss: {loss_s.item():.4f}\")\n    print(f\"  etadn_dpo_loss:        {loss_e.item():.4f}\")\n    print(\"  gradient check: PASS\")\n\n\ndef _test_gamma_lookup():\n    \"\"\"get_gamma_for_error_type should return correct values.\"\"\"\n    config = ETADNConfig()\n    assert get_gamma_for_error_type(\"action\", config) == 0.85\n    assert get_gamma_for_error_type(\"verification\", config) == 0.92\n    assert get_gamma_for_error_type(\"planning\", config) == 0.97\n    assert get_gamma_for_error_type(\"unknown\", config) == 0.92  # fallback\n    print(\"  gamma lookup: PASS\")\n\n\nif __name__ == \"__main__\":\n    print(\"ETADN discount module self-tests\")\n    print(\"=\" * 40)\n    _test_phi_weights_properties()\n    _test_phi_shape_by_gamma()\n    _test_gamma_lookup()\n    _test_dpo_loss_gradients()\n    print(\"=\" * 40)\n    print(\"All tests passed.\")\n",
      "numLines": 334,
      "startLine": 1,
      "totalLines": 334
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of:

1. **Trajectory JSONL format** (from `collect_trajectories_icl.py` line 329-336):
   - `task_id`, `task_type`, `game_file`, `reward` (bool), `steps`, `conversations` (list of `{role, content}` messages)

2. **Expert data format** (from `collect_trajectories_icl.py` line 92-122):
   - JSON array, each item has `game_file`, `conversations` (with `from`/`value` format: `{from: "human"/"gpt", value: "..."}`)
   
3. **Building DPO pairs** involves normalizing game file paths, locating where the task actually starts, extracting action-observation sequences, comparing them to find where trajectories diverge, and normalizing the action text for comparison.

4. The γ(d) function applies a linear interpolation between minimum and maximum values based on the divergence point, which differs from the approach used in ETADN.

Now I need to verify the scripts directory exists and create the necessary script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "245cae8c-70b4-49c9-a9fc-7bfefec07cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UFjD29vEQrVbhRttTZTDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16193,
      "cache_read_input_tokens": 24031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16193
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

_source line 13_

Now I have the full picture. Let me check existing directory structure, then write the script and mock test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "470c455e-5403-49bb-90dc-5e69cfbca919",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UFjD29vEQrVbhRttTZTDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16193,
      "cache_read_input_tokens": 24031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16193
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01BJERRnZo7r3V8cdh71NNHY`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py 2>/dev/null",
  "description": "Check existing directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "574c98df-7e3a-466d-90dc-7dfb8a64b780",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UFjD29vEQrVbhRttTZTDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16193,
      "cache_read_input_tokens": 24031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16193
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

_source line 15 · 2026-05-13T06:38:48.381Z_

<details><summary>↩ Tool result · `toolu_01BJERRnZo7r3V8cdh71NNHY`</summary>

```text
run_training.sh
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "b261f931-7970-4b35-a8bc-34486284e8b3",
  "tool_use_result": {
    "stdout": "run_training.sh\n---\n/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py",
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

_source line 16_

Writing the analysis script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "4d0fa489-e143-4f6e-ba73-566d22618182",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhHoQKWzih3kDCyrrLF3nj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 40224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
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

_source line 17_

<details open><summary>🔧 Tool call — Write · `toolu_018oDs6h31A1Bz9qLmrdXHUk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/analyze_divergence.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Divergence point analysis for ALFWorld failure trajectories.\n\nComputes divergence statistics, early/mid/late grouping, and γ(d) distribution.\nOutputs structured JSON, LaTeX tables for paper, and human-readable summary.\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\ntry:\n    import numpy as np\nexcept ImportError:\n    np = None\n\n\n# ---------------------------------------------------------------------------\n# Game file normalization (same as build_dpo_pairs.py)\n# ---------------------------------------------------------------------------\n\ndef normalize_game_file(game_file: str) -> str:\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both {role,content} and {from,value} formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\n# ---------------------------------------------------------------------------\n# Task type detection\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_KEYS = [\n    \"pick_and_place\",\n    \"pick_clean_then_place\",\n    \"pick_heat_then_place\",\n    \"pick_cool_then_place\",\n    \"look_at_obj\",\n    \"pick_two_obj\",\n]\n\nTASK_TYPE_SHORT = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\n\ndef get_task_type(game_file: str) -> str:\n    for k in TASK_TYPE_KEYS:\n        if f\"/{k}\" in game_file or game_file.startswith(k):\n            return k\n    return \"unknown\"\n\n\n# ---------------------------------------------------------------------------\n# Step extraction & divergence (mirrors build_dpo_pairs.py logic)\n# ---------------------------------------------------------------------------\n\ndef find_task_start(conversations: list) -> int:\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_action_sequence(conversations: list, start_idx: int) -> list[str]:\n    actions = []\n    for i in range(start_idx, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            content = _content(conversations[i])\n            if \"Action:\" in content:\n                actions.append(_extract_action_text(content))\n    return actions\n\n\ndef _extract_action_text(content: str) -> str:\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\ndef find_divergence_point(expert_actions: list[str], fail_actions: list[str]) -> int:\n    min_len = min(len(expert_actions), len(fail_actions))\n    for i in range(min_len):\n        if expert_actions[i] != fail_actions[i]:\n            return i\n    return min_len\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(dirs: list[str]) -> list[dict]:\n    records = []\n    for d in dirs:\n        for p in sorted(Path(d).glob(\"*.jsonl\")):\n            with open(p) as f:\n                for line in f:\n                    if line.strip():\n                        records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(path: str) -> dict[str, dict]:\n    with open(path) as f:\n        experts = json.load(f)\n    index = {}\n    for ex in experts:\n        key = normalize_game_file(ex[\"game_file\"])\n        index[key] = ex\n    return index\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict, gamma_min: float, gamma_max: float) -> dict:\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n\n    # Per-task-type counts\n    type_total = defaultdict(int)\n    type_success = defaultdict(int)\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in sorted(set(list(type_total.keys()))):\n        n = type_total[tt]\n        s = type_success[tt]\n        per_type_sr[tt] = {\"total\": n, \"success\": s, \"rate\": s / n if n > 0 else 0.0}\n\n    # Divergence analysis on failures\n    d_values = []\n    correction_spans = []\n    unmatched = 0\n    matched = 0\n    per_type_d = defaultdict(list)\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n        if expert is None:\n            unmatched += 1\n            continue\n        matched += 1\n\n        fail_convs = t.get(\"conversations\", [])\n        expert_convs = expert.get(\"conversations\", [])\n\n        fail_start = find_task_start(fail_convs)\n        expert_start = find_task_start(expert_convs)\n\n        fail_actions = extract_action_sequence(fail_convs, fail_start)\n        expert_actions = extract_action_sequence(expert_convs, expert_start)\n\n        if not expert_actions:\n            continue\n\n        div_point = find_divergence_point(expert_actions, fail_actions)\n        d = div_point / len(expert_actions)\n        correction_span = len(expert_actions) - div_point\n\n        d_values.append(d)\n        correction_spans.append(correction_span)\n\n        tt = t.get(\"task_type\") or get_task_type(gf)\n        per_type_d[tt].append(d)\n\n    # d statistics\n    d_stats = _compute_stats(d_values)\n\n    # Histogram (10 bins)\n    histogram = [0] * 10\n    for d in d_values:\n        b = min(int(d * 10), 9)\n        histogram[b] += 1\n\n    # Per-type d mean\n    per_type_d_mean = {}\n    for tt in sorted(per_type_d.keys()):\n        vals = per_type_d[tt]\n        per_type_d_mean[tt] = {\"mean\": _mean(vals), \"count\": len(vals)}\n\n    # Early/Mid/Late grouping\n    early = [(d, cs) for d, cs in zip(d_values, correction_spans) if d < 0.33]\n    mid = [(d, cs) for d, cs in zip(d_values, correction_spans) if 0.33 <= d < 0.67]\n    late = [(d, cs) for d, cs in zip(d_values, correction_spans) if d >= 0.67]\n\n    n_div = len(d_values)\n    groups = {}\n    for name, subset in [(\"early\", early), (\"mid\", mid), (\"late\", late)]:\n        groups[name] = {\n            \"count\": len(subset),\n            \"proportion\": len(subset) / n_div if n_div > 0 else 0.0,\n            \"avg_correction_span\": _mean([cs for _, cs in subset]),\n            \"avg_d\": _mean([d for d, _ in subset]),\n        }\n\n    # γ(d) mapping\n    gamma_values = [gamma_min + (gamma_max - gamma_min) * d for d in d_values]\n    gamma_stats = _compute_stats(gamma_values)\n\n    return {\n        \"basic\": {\n            \"total_episodes\": total,\n            \"success\": len(successes),\n            \"failure\": len(failures),\n            \"success_rate\": len(successes) / total if total > 0 else 0.0,\n        },\n        \"per_task_type_sr\": per_type_sr,\n        \"divergence\": {\n            \"matched_failures\": matched,\n            \"unmatched_failures\": unmatched,\n            \"d_stats\": d_stats,\n            \"histogram_bins\": [\"[0.0,0.1)\", \"[0.1,0.2)\", \"[0.2,0.3)\", \"[0.3,0.4)\",\n                               \"[0.4,0.5)\", \"[0.5,0.6)\", \"[0.6,0.7)\", \"[0.7,0.8)\",\n                               \"[0.8,0.9)\", \"[0.9,1.0]\"],\n            \"histogram_counts\": histogram,\n            \"per_type_d_mean\": per_type_d_mean,\n        },\n        \"groups\": groups,\n        \"gamma\": {\n            \"gamma_min\": gamma_min,\n            \"gamma_max\": gamma_max,\n            \"stats\": gamma_stats,\n        },\n        \"expert_match\": {\n            \"exact_match\": matched,\n            \"unmatched\": unmatched,\n            \"match_rate\": matched / (matched + unmatched) if (matched + unmatched) > 0 else 0.0,\n        },\n    }\n\n\ndef _mean(vals):\n    return sum(vals) / len(vals) if vals else 0.0\n\n\ndef _std(vals):\n    if len(vals) < 2:\n        return 0.0\n    m = _mean(vals)\n    return math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))\n\n\ndef _percentile(vals, p):\n    if not vals:\n        return 0.0\n    s = sorted(vals)\n    k = (len(s) - 1) * p / 100.0\n    f = int(k)\n    c = min(f + 1, len(s) - 1)\n    d = k - f\n    return s[f] + d * (s[c] - s[f])\n\n\ndef _compute_stats(vals):\n    if not vals:\n        return {\"count\": 0, \"mean\": 0, \"median\": 0, \"std\": 0, \"min\": 0, \"max\": 0,\n                \"q25\": 0, \"q75\": 0}\n    return {\n        \"count\": len(vals),\n        \"mean\": _mean(vals),\n        \"median\": _percentile(vals, 50),\n        \"std\": _std(vals),\n        \"min\": min(vals),\n        \"max\": max(vals),\n        \"q25\": _percentile(vals, 25),\n        \"q75\": _percentile(vals, 75),\n    }\n\n\n# ---------------------------------------------------------------------------\n# LaTeX output\n# ---------------------------------------------------------------------------\n\ndef generate_latex(results: dict) -> str:\n    lines = []\n\n    # Table 1: Per-task-type success rate\n    lines.append(\"% Table 1: Per-task-type success rate\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Per-task-type success rate.}\")\n    lines.append(r\"\\label{tab:task_type_sr}\")\n    lines.append(r\"\\begin{tabular}{lrrr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Task Type & Total & Success & Rate (\\%) \\\\\")\n    lines.append(r\"\\midrule\")\n    sr = results[\"per_task_type_sr\"]\n    for tt in sorted(sr.keys()):\n        v = sr[tt]\n        short = TASK_TYPE_SHORT.get(tt, tt)\n        lines.append(f\"{short} & {v['total']} & {v['success']} & {v['rate']*100:.1f} \\\\\\\\\")\n    b = results[\"basic\"]\n    lines.append(r\"\\midrule\")\n    lines.append(f\"Overall & {b['total_episodes']} & {b['success']} & {b['success_rate']*100:.1f} \\\\\\\\\")\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n    lines.append(\"\")\n\n    # Table 2: Divergence point distribution (early/mid/late)\n    lines.append(\"% Table 2: Divergence point distribution\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Divergence point distribution by failure stage.}\")\n    lines.append(r\"\\label{tab:divergence_groups}\")\n    lines.append(r\"\\begin{tabular}{lcrrr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Stage & $d$ range & Count & Prop. (\\%) & Avg.\\ $C_{\\text{span}}$ \\\\\")\n    lines.append(r\"\\midrule\")\n    g = results[\"groups\"]\n    stage_labels = [\n        (\"Early\", \"$[0, 0.33)$\", \"early\"),\n        (\"Mid\", \"$[0.33, 0.67)$\", \"mid\"),\n        (\"Late\", \"$[0.67, 1.0]$\", \"late\"),\n    ]\n    for label, drange, key in stage_labels:\n        v = g[key]\n        lines.append(\n            f\"{label} & {drange} & {v['count']} & {v['proportion']*100:.1f} & {v['avg_correction_span']:.1f} \\\\\\\\\"\n        )\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n    lines.append(\"\")\n\n    # Table 3: γ(d) distribution statistics\n    lines.append(\"% Table 3: Gamma distribution statistics\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    gmin = results[\"gamma\"][\"gamma_min\"]\n    gmax = results[\"gamma\"][\"gamma_max\"]\n    lines.append(r\"\\caption{$\\gamma(d)$ distribution ($\\gamma_{\\min}=\" + f\"{gmin}\" + r\", \\gamma_{\\max}=\" + f\"{gmax}\" + r\"$).}\")\n    lines.append(r\"\\label{tab:gamma_dist}\")\n    lines.append(r\"\\begin{tabular}{lr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Statistic & Value \\\\\")\n    lines.append(r\"\\midrule\")\n    gs = results[\"gamma\"][\"stats\"]\n    for k, label in [(\"mean\", \"Mean\"), (\"median\", \"Median\"), (\"std\", \"Std\"),\n                     (\"min\", \"Min\"), (\"max\", \"Max\"), (\"q25\", \"Q25\"), (\"q75\", \"Q75\")]:\n        lines.append(f\"{label} & {gs[k]:.4f} \\\\\\\\\")\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n\n    return \"\\n\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Human-readable summary\n# ---------------------------------------------------------------------------\n\ndef print_summary(results: dict):\n    b = results[\"basic\"]\n    print(f\"\\n{'='*60}\")\n    print(\"DIVERGENCE ANALYSIS SUMMARY\")\n    print(f\"{'='*60}\")\n    print(f\"Episodes: {b['total_episodes']}  Success: {b['success']}  Failure: {b['failure']}  SR: {b['success_rate']*100:.1f}%\")\n\n    print(f\"\\n--- Per-task-type success rate ---\")\n    print(f\"{'Type':<25} {'Total':>6} {'Succ':>6} {'Rate':>8}\")\n    print(\"-\" * 50)\n    for tt in sorted(results[\"per_task_type_sr\"].keys()):\n        v = results[\"per_task_type_sr\"][tt]\n        print(f\"{tt:<25} {v['total']:>6} {v['success']:>6} {v['rate']*100:>7.1f}%\")\n\n    div = results[\"divergence\"]\n    ds = div[\"d_stats\"]\n    print(f\"\\n--- Divergence point (d = div_point / expert_len) ---\")\n    print(f\"Matched failures: {div['matched_failures']}  Unmatched: {div['unmatched_failures']}\")\n    if ds[\"count\"] > 0:\n        print(f\"Mean: {ds['mean']:.3f}  Median: {ds['median']:.3f}  Std: {ds['std']:.3f}\")\n        print(f\"Min: {ds['min']:.3f}  Max: {ds['max']:.3f}  Q25: {ds['q25']:.3f}  Q75: {ds['q75']:.3f}\")\n\n        print(f\"\\nHistogram:\")\n        for label, count in zip(div[\"histogram_bins\"], div[\"histogram_counts\"]):\n            bar = \"#\" * count\n            print(f\"  {label:>12}: {count:>4} {bar}\")\n\n    print(f\"\\n--- Early / Mid / Late ---\")\n    g = results[\"groups\"]\n    print(f\"{'Stage':<8} {'Count':>6} {'Prop':>8} {'Avg CSpan':>10} {'Avg d':>8}\")\n    print(\"-\" * 45)\n    for key in [\"early\", \"mid\", \"late\"]:\n        v = g[key]\n        print(f\"{key:<8} {v['count']:>6} {v['proportion']*100:>7.1f}% {v['avg_correction_span']:>10.1f} {v['avg_d']:>8.3f}\")\n\n    gs = results[\"gamma\"][\"stats\"]\n    print(f\"\\n--- γ(d) distribution (γ_min={results['gamma']['gamma_min']}, γ_max={results['gamma']['gamma_max']}) ---\")\n    if gs[\"count\"] > 0:\n        print(f\"Mean: {gs['mean']:.4f}  Median: {gs['median']:.4f}  Std: {gs['std']:.4f}\")\n        print(f\"Min: {gs['min']:.4f}  Max: {gs['max']:.4f}\")\n\n    em = results[\"expert_match\"]\n    print(f\"\\n--- Expert matching ---\")\n    print(f\"Matched: {em['exact_match']}  Unmatched: {em['unmatched']}  Match rate: {em['match_rate']*100:.1f}%\")\n    print(f\"{'='*60}\")\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Analyze divergence points in ALFWorld failure trajectories\")\n    parser.add_argument(\"--trajectory_dirs\", nargs=\"+\", required=True,\n                        help=\"One or more trajectory directories\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Path to alfworld_sft.json\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"outputs/divergence_analysis\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85)\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97)\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.trajectory_dirs)\n    if not trajectories:\n        print(\"ERROR: No trajectories loaded.\", file=sys.stderr)\n        sys.exit(1)\n\n    expert_index = load_expert_index(args.expert_file)\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    json_path = out_dir / \"divergence_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    tex_path = out_dir / \"divergence_tables.tex\"\n    with open(tex_path, \"w\") as f:\n        f.write(generate_latex(results))\n\n    print_summary(results)\n    print(f\"\\nJSON: {json_path}\")\n    print(f\"LaTeX: {tex_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "fb84429c-bd3f-4365-9c4e-770ce93a6fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhHoQKWzih3kDCyrrLF3nj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 40224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
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

_source line 18 · 2026-05-13T06:39:56.524Z_

<details><summary>↩ Tool result · `toolu_018oDs6h31A1Bz9qLmrdXHUk`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/analyze_divergence.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "78359f12-13f6-4883-a37e-b601fbe36f53",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/analyze_divergence.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Divergence point analysis for ALFWorld failure trajectories.\n\nComputes divergence statistics, early/mid/late grouping, and γ(d) distribution.\nOutputs structured JSON, LaTeX tables for paper, and human-readable summary.\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\ntry:\n    import numpy as np\nexcept ImportError:\n    np = None\n\n\n# ---------------------------------------------------------------------------\n# Game file normalization (same as build_dpo_pairs.py)\n# ---------------------------------------------------------------------------\n\ndef normalize_game_file(game_file: str) -> str:\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both {role,content} and {from,value} formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\n# ---------------------------------------------------------------------------\n# Task type detection\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_KEYS = [\n    \"pick_and_place\",\n    \"pick_clean_then_place\",\n    \"pick_heat_then_place\",\n    \"pick_cool_then_place\",\n    \"look_at_obj\",\n    \"pick_two_obj\",\n]\n\nTASK_TYPE_SHORT = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\n\ndef get_task_type(game_file: str) -> str:\n    for k in TASK_TYPE_KEYS:\n        if f\"/{k}\" in game_file or game_file.startswith(k):\n            return k\n    return \"unknown\"\n\n\n# ---------------------------------------------------------------------------\n# Step extraction & divergence (mirrors build_dpo_pairs.py logic)\n# ---------------------------------------------------------------------------\n\ndef find_task_start(conversations: list) -> int:\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_action_sequence(conversations: list, start_idx: int) -> list[str]:\n    actions = []\n    for i in range(start_idx, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            content = _content(conversations[i])\n            if \"Action:\" in content:\n                actions.append(_extract_action_text(content))\n    return actions\n\n\ndef _extract_action_text(content: str) -> str:\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\ndef find_divergence_point(expert_actions: list[str], fail_actions: list[str]) -> int:\n    min_len = min(len(expert_actions), len(fail_actions))\n    for i in range(min_len):\n        if expert_actions[i] != fail_actions[i]:\n            return i\n    return min_len\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(dirs: list[str]) -> list[dict]:\n    records = []\n    for d in dirs:\n        for p in sorted(Path(d).glob(\"*.jsonl\")):\n            with open(p) as f:\n                for line in f:\n                    if line.strip():\n                        records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(path: str) -> dict[str, dict]:\n    with open(path) as f:\n        experts = json.load(f)\n    index = {}\n    for ex in experts:\n        key = normalize_game_file(ex[\"game_file\"])\n        index[key] = ex\n    return index\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict, gamma_min: float, gamma_max: float) -> dict:\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n\n    # Per-task-type counts\n    type_total = defaultdict(int)\n    type_success = defaultdict(int)\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in sorted(set(list(type_total.keys()))):\n        n = type_total[tt]\n        s = type_success[tt]\n        per_type_sr[tt] = {\"total\": n, \"success\": s, \"rate\": s / n if n > 0 else 0.0}\n\n    # Divergence analysis on failures\n    d_values = []\n    correction_spans = []\n    unmatched = 0\n    matched = 0\n    per_type_d = defaultdict(list)\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n        if expert is None:\n            unmatched += 1\n            continue\n        matched += 1\n\n        fail_convs = t.get(\"conversations\", [])\n        expert_convs = expert.get(\"conversations\", [])\n\n        fail_start = find_task_start(fail_convs)\n        expert_start = find_task_start(expert_convs)\n\n        fail_actions = extract_action_sequence(fail_convs, fail_start)\n        expert_actions = extract_action_sequence(expert_convs, expert_start)\n\n        if not expert_actions:\n            continue\n\n        div_point = find_divergence_point(expert_actions, fail_actions)\n        d = div_point / len(expert_actions)\n        correction_span = len(expert_actions) - div_point\n\n        d_values.append(d)\n        correction_spans.append(correction_span)\n\n        tt = t.get(\"task_type\") or get_task_type(gf)\n        per_type_d[tt].append(d)\n\n    # d statistics\n    d_stats = _compute_stats(d_values)\n\n    # Histogram (10 bins)\n    histogram = [0] * 10\n    for d in d_values:\n        b = min(int(d * 10), 9)\n        histogram[b] += 1\n\n    # Per-type d mean\n    per_type_d_mean = {}\n    for tt in sorted(per_type_d.keys()):\n        vals = per_type_d[tt]\n        per_type_d_mean[tt] = {\"mean\": _mean(vals), \"count\": len(vals)}\n\n    # Early/Mid/Late grouping\n    early = [(d, cs) for d, cs in zip(d_values, correction_spans) if d < 0.33]\n    mid = [(d, cs) for d, cs in zip(d_values, correction_spans) if 0.33 <= d < 0.67]\n    late = [(d, cs) for d, cs in zip(d_values, correction_spans) if d >= 0.67]\n\n    n_div = len(d_values)\n    groups = {}\n    for name, subset in [(\"early\", early), (\"mid\", mid), (\"late\", late)]:\n        groups[name] = {\n            \"count\": len(subset),\n            \"proportion\": len(subset) / n_div if n_div > 0 else 0.0,\n            \"avg_correction_span\": _mean([cs for _, cs in subset]),\n            \"avg_d\": _mean([d for d, _ in subset]),\n        }\n\n    # γ(d) mapping\n    gamma_values = [gamma_min + (gamma_max - gamma_min) * d for d in d_values]\n    gamma_stats = _compute_stats(gamma_values)\n\n    return {\n        \"basic\": {\n            \"total_episodes\": total,\n            \"success\": len(successes),\n            \"failure\": len(failures),\n            \"success_rate\": len(successes) / total if total > 0 else 0.0,\n        },\n        \"per_task_type_sr\": per_type_sr,\n        \"divergence\": {\n            \"matched_failures\": matched,\n            \"unmatched_failures\": unmatched,\n            \"d_stats\": d_stats,\n            \"histogram_bins\": [\"[0.0,0.1)\", \"[0.1,0.2)\", \"[0.2,0.3)\", \"[0.3,0.4)\",\n                               \"[0.4,0.5)\", \"[0.5,0.6)\", \"[0.6,0.7)\", \"[0.7,0.8)\",\n                               \"[0.8,0.9)\", \"[0.9,1.0]\"],\n            \"histogram_counts\": histogram,\n            \"per_type_d_mean\": per_type_d_mean,\n        },\n        \"groups\": groups,\n        \"gamma\": {\n            \"gamma_min\": gamma_min,\n            \"gamma_max\": gamma_max,\n            \"stats\": gamma_stats,\n        },\n        \"expert_match\": {\n            \"exact_match\": matched,\n            \"unmatched\": unmatched,\n            \"match_rate\": matched / (matched + unmatched) if (matched + unmatched) > 0 else 0.0,\n        },\n    }\n\n\ndef _mean(vals):\n    return sum(vals) / len(vals) if vals else 0.0\n\n\ndef _std(vals):\n    if len(vals) < 2:\n        return 0.0\n    m = _mean(vals)\n    return math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))\n\n\ndef _percentile(vals, p):\n    if not vals:\n        return 0.0\n    s = sorted(vals)\n    k = (len(s) - 1) * p / 100.0\n    f = int(k)\n    c = min(f + 1, len(s) - 1)\n    d = k - f\n    return s[f] + d * (s[c] - s[f])\n\n\ndef _compute_stats(vals):\n    if not vals:\n        return {\"count\": 0, \"mean\": 0, \"median\": 0, \"std\": 0, \"min\": 0, \"max\": 0,\n                \"q25\": 0, \"q75\": 0}\n    return {\n        \"count\": len(vals),\n        \"mean\": _mean(vals),\n        \"median\": _percentile(vals, 50),\n        \"std\": _std(vals),\n        \"min\": min(vals),\n        \"max\": max(vals),\n        \"q25\": _percentile(vals, 25),\n        \"q75\": _percentile(vals, 75),\n    }\n\n\n# ---------------------------------------------------------------------------\n# LaTeX output\n# ---------------------------------------------------------------------------\n\ndef generate_latex(results: dict) -> str:\n    lines = []\n\n    # Table 1: Per-task-type success rate\n    lines.append(\"% Table 1: Per-task-type success rate\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Per-task-type success rate.}\")\n    lines.append(r\"\\label{tab:task_type_sr}\")\n    lines.append(r\"\\begin{tabular}{lrrr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Task Type & Total & Success & Rate (\\%) \\\\\")\n    lines.append(r\"\\midrule\")\n    sr = results[\"per_task_type_sr\"]\n    for tt in sorted(sr.keys()):\n        v = sr[tt]\n        short = TASK_TYPE_SHORT.get(tt, tt)\n        lines.append(f\"{short} & {v['total']} & {v['success']} & {v['rate']*100:.1f} \\\\\\\\\")\n    b = results[\"basic\"]\n    lines.append(r\"\\midrule\")\n    lines.append(f\"Overall & {b['total_episodes']} & {b['success']} & {b['success_rate']*100:.1f} \\\\\\\\\")\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n    lines.append(\"\")\n\n    # Table 2: Divergence point distribution (early/mid/late)\n    lines.append(\"% Table 2: Divergence point distribution\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Divergence point distribution by failure stage.}\")\n    lines.append(r\"\\label{tab:divergence_groups}\")\n    lines.append(r\"\\begin{tabular}{lcrrr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Stage & $d$ range & Count & Prop. (\\%) & Avg.\\ $C_{\\text{span}}$ \\\\\")\n    lines.append(r\"\\midrule\")\n    g = results[\"groups\"]\n    stage_labels = [\n        (\"Early\", \"$[0, 0.33)$\", \"early\"),\n        (\"Mid\", \"$[0.33, 0.67)$\", \"mid\"),\n        (\"Late\", \"$[0.67, 1.0]$\", \"late\"),\n    ]\n    for label, drange, key in stage_labels:\n        v = g[key]\n        lines.append(\n            f\"{label} & {drange} & {v['count']} & {v['proportion']*100:.1f} & {v['avg_correction_span']:.1f} \\\\\\\\\"\n        )\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n    lines.append(\"\")\n\n    # Table 3: γ(d) distribution statistics\n    lines.append(\"% Table 3: Gamma distribution statistics\")\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    gmin = results[\"gamma\"][\"gamma_min\"]\n    gmax = results[\"gamma\"][\"gamma_max\"]\n    lines.append(r\"\\caption{$\\gamma(d)$ distribution ($\\gamma_{\\min}=\" + f\"{gmin}\" + r\", \\gamma_{\\max}=\" + f\"{gmax}\" + r\"$).}\")\n    lines.append(r\"\\label{tab:gamma_dist}\")\n    lines.append(r\"\\begin{tabular}{lr}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Statistic & Value \\\\\")\n    lines.append(r\"\\midrule\")\n    gs = results[\"gamma\"][\"stats\"]\n    for k, label in [(\"mean\", \"Mean\"), (\"median\", \"Median\"), (\"std\", \"Std\"),\n                     (\"min\", \"Min\"), (\"max\", \"Max\"), (\"q25\", \"Q25\"), (\"q75\", \"Q75\")]:\n        lines.append(f\"{label} & {gs[k]:.4f} \\\\\\\\\")\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n    lines.append(r\"\\end{table}\")\n\n    return \"\\n\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Human-readable summary\n# ---------------------------------------------------------------------------\n\ndef print_summary(results: dict):\n    b = results[\"basic\"]\n    print(f\"\\n{'='*60}\")\n    print(\"DIVERGENCE ANALYSIS SUMMARY\")\n    print(f\"{'='*60}\")\n    print(f\"Episodes: {b['total_episodes']}  Success: {b['success']}  Failure: {b['failure']}  SR: {b['success_rate']*100:.1f}%\")\n\n    print(f\"\\n--- Per-task-type success rate ---\")\n    print(f\"{'Type':<25} {'Total':>6} {'Succ':>6} {'Rate':>8}\")\n    print(\"-\" * 50)\n    for tt in sorted(results[\"per_task_type_sr\"].keys()):\n        v = results[\"per_task_type_sr\"][tt]\n        print(f\"{tt:<25} {v['total']:>6} {v['success']:>6} {v['rate']*100:>7.1f}%\")\n\n    div = results[\"divergence\"]\n    ds = div[\"d_stats\"]\n    print(f\"\\n--- Divergence point (d = div_point / expert_len) ---\")\n    print(f\"Matched failures: {div['matched_failures']}  Unmatched: {div['unmatched_failures']}\")\n    if ds[\"count\"] > 0:\n        print(f\"Mean: {ds['mean']:.3f}  Median: {ds['median']:.3f}  Std: {ds['std']:.3f}\")\n        print(f\"Min: {ds['min']:.3f}  Max: {ds['max']:.3f}  Q25: {ds['q25']:.3f}  Q75: {ds['q75']:.3f}\")\n\n        print(f\"\\nHistogram:\")\n        for label, count in zip(div[\"histogram_bins\"], div[\"histogram_counts\"]):\n            bar = \"#\" * count\n            print(f\"  {label:>12}: {count:>4} {bar}\")\n\n    print(f\"\\n--- Early / Mid / Late ---\")\n    g = results[\"groups\"]\n    print(f\"{'Stage':<8} {'Count':>6} {'Prop':>8} {'Avg CSpan':>10} {'Avg d':>8}\")\n    print(\"-\" * 45)\n    for key in [\"early\", \"mid\", \"late\"]:\n        v = g[key]\n        print(f\"{key:<8} {v['count']:>6} {v['proportion']*100:>7.1f}% {v['avg_correction_span']:>10.1f} {v['avg_d']:>8.3f}\")\n\n    gs = results[\"gamma\"][\"stats\"]\n    print(f\"\\n--- γ(d) distribution (γ_min={results['gamma']['gamma_min']}, γ_max={results['gamma']['gamma_max']}) ---\")\n    if gs[\"count\"] > 0:\n        print(f\"Mean: {gs['mean']:.4f}  Median: {gs['median']:.4f}  Std: {gs['std']:.4f}\")\n        print(f\"Min: {gs['min']:.4f}  Max: {gs['max']:.4f}\")\n\n    em = results[\"expert_match\"]\n    print(f\"\\n--- Expert matching ---\")\n    print(f\"Matched: {em['exact_match']}  Unmatched: {em['unmatched']}  Match rate: {em['match_rate']*100:.1f}%\")\n    print(f\"{'='*60}\")\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Analyze divergence points in ALFWorld failure trajectories\")\n    parser.add_argument(\"--trajectory_dirs\", nargs=\"+\", required=True,\n                        help=\"One or more trajectory directories\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Path to alfworld_sft.json\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"outputs/divergence_analysis\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85)\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97)\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.trajectory_dirs)\n    if not trajectories:\n        print(\"ERROR: No trajectories loaded.\", file=sys.stderr)\n        sys.exit(1)\n\n    expert_index = load_expert_index(args.expert_file)\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    json_path = out_dir / \"divergence_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    tex_path = out_dir / \"divergence_tables.tex\"\n    with open(tex_path, \"w\") as f:\n        f.write(generate_latex(results))\n\n    print_summary(results)\n    print(f\"\\nJSON: {json_path}\")\n    print(f\"LaTeX: {tex_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Now writing the mock test script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "d705b170-31d7-4480-8fb1-7e60d64b879c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QLyWUiTncah4jwBw4rG4f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5661,
      "cache_read_input_tokens": 40857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5661
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

<details open><summary>🔧 Tool call — Bash · `toolu_01FKAidmhVXykyioC1495Qr1`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test",
  "description": "Create mock test directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "7927995f-b389-4453-8cd5-0c2d3f32ee87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QLyWUiTncah4jwBw4rG4f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5661,
      "cache_read_input_tokens": 40857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5661
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

_source line 21 · 2026-05-13T06:40:00.370Z_

<details><summary>↩ Tool result · `toolu_01FKAidmhVXykyioC1495Qr1`</summary>

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
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "5cf89d85-1f53-4753-8464-3122a2853acc",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Write · `toolu_011Q6TXH44xGeH7mgBDcTrJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/generate_mock_data.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Generate mock trajectory and expert data, then run analyze_divergence.py to validate output.\"\"\"\n\nimport json\nimport os\nimport subprocess\nimport sys\nfrom pathlib import Path\n\nSCRIPT_DIR = Path(__file__).parent\nPROJECT_ROOT = SCRIPT_DIR.parent.parent\nMOCK_TRAJ_DIR = SCRIPT_DIR / \"mock_trajectories\"\nMOCK_EXPERT_FILE = SCRIPT_DIR / \"mock_expert.json\"\nMOCK_OUTPUT_DIR = SCRIPT_DIR / \"mock_output\"\n\nTASK_TYPES = [\n    \"pick_and_place\",\n    \"pick_clean_then_place\",\n    \"pick_heat_then_place\",\n    \"pick_cool_then_place\",\n    \"look_at_obj\",\n    \"pick_two_obj\",\n]\n\n\ndef make_expert_actions(n_steps: int, task_idx: int) -> list[dict]:\n    \"\"\"Generate a synthetic expert conversation with n_steps actions.\"\"\"\n    msgs = [\n        {\"from\": \"human\", \"value\": f\"Your task is to: do task {task_idx}\"},\n        {\"from\": \"gpt\", \"value\": \"OK, I will help.\"},\n    ]\n    for i in range(n_steps):\n        msgs.append({\"from\": \"gpt\", \"value\": f\"Thought: step {i}\\nAction: go to shelf {i}\"})\n        msgs.append({\"from\": \"human\", \"value\": f\"Observation: You see shelf {i}.\"})\n    return msgs\n\n\ndef make_trajectory(task_idx: int, task_type: str, reward: bool,\n                    expert_actions: list[str], diverge_at: int | None) -> dict:\n    \"\"\"Generate a synthetic trajectory.\n\n    If reward=True, actions match expert exactly.\n    If reward=False, diverge at diverge_at step.\n    \"\"\"\n    game_file = f\"data/json_2.1.1/train/{task_type}/trial_{task_idx:03d}/game.tw-pddl\"\n\n    msgs = [\n        {\"role\": \"user\", \"content\": \"System instruction...\"},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n        {\"role\": \"user\", \"content\": f\"Your task is to: do task {task_idx}\"},\n    ]\n\n    n_steps = len(expert_actions)\n    for i in range(n_steps):\n        if not reward and diverge_at is not None and i >= diverge_at:\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: wrong step {i}\\nAction: take apple {i} from counter {i}\"})\n        else:\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: step {i}\\nAction: {expert_actions[i]}\"})\n        msgs.append({\"role\": \"user\", \"content\": f\"Observation: You see something at step {i}.\"})\n\n    if not reward:\n        for extra in range(2):\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: floundering {extra}\\nAction: look\"})\n            msgs.append({\"role\": \"user\", \"content\": \"Observation: Nothing happened.\"})\n\n    return {\n        \"task_id\": task_idx,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": reward,\n        \"steps\": n_steps + (0 if reward else 2),\n        \"conversations\": msgs,\n    }\n\n\ndef generate():\n    MOCK_TRAJ_DIR.mkdir(parents=True, exist_ok=True)\n    MOCK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    experts = []\n    trajectories = []\n\n    for idx in range(20):\n        task_type = TASK_TYPES[idx % len(TASK_TYPES)]\n        n_steps = 5 + (idx % 8)\n        expert_actions = [f\"go to shelf {i}\" for i in range(n_steps)]\n\n        game_file = f\"data/json_2.1.1/train/{task_type}/trial_{idx:03d}\"\n        experts.append({\n            \"game_file\": game_file,\n            \"conversations\": make_expert_actions(n_steps, idx),\n        })\n\n        if idx % 3 == 0:\n            # success\n            traj = make_trajectory(idx, task_type, True, expert_actions, None)\n        elif idx == 19:\n            # unmatched failure: use a game_file that won't match any expert\n            traj = make_trajectory(idx, task_type, False, expert_actions, 2)\n            traj[\"game_file\"] = \"data/json_2.1.1/train/unknown_type/trial_999/game.tw-pddl\"\n        else:\n            # failure with divergence\n            diverge_at = max(0, min(idx % n_steps, n_steps - 1))\n            traj = make_trajectory(idx, task_type, False, expert_actions, diverge_at)\n\n        trajectories.append(traj)\n\n    with open(MOCK_EXPERT_FILE, \"w\") as f:\n        json.dump(experts, f, indent=2)\n\n    traj_file = MOCK_TRAJ_DIR / \"train.jsonl\"\n    with open(traj_file, \"w\") as f:\n        for t in trajectories:\n            f.write(json.dumps(t) + \"\\n\")\n\n    print(f\"Generated {len(experts)} experts -> {MOCK_EXPERT_FILE}\")\n    print(f\"Generated {len(trajectories)} trajectories -> {traj_file}\")\n    return MOCK_TRAJ_DIR, MOCK_EXPERT_FILE, MOCK_OUTPUT_DIR\n\n\ndef validate(output_dir: Path) -> bool:\n    ok = True\n\n    # Check JSON\n    json_path = output_dir / \"divergence_summary.json\"\n    if not json_path.exists():\n        print(f\"FAIL: {json_path} not found\")\n        return False\n\n    with open(json_path) as f:\n        data = json.load(f)\n\n    required_keys = [\"basic\", \"per_task_type_sr\", \"divergence\", \"groups\", \"gamma\", \"expert_match\"]\n    for k in required_keys:\n        if k not in data:\n            print(f\"FAIL: missing top-level key '{k}' in JSON\")\n            ok = False\n\n    if ok:\n        assert data[\"basic\"][\"total_episodes\"] == 20, f\"Expected 20 episodes, got {data['basic']['total_episodes']}\"\n        assert data[\"basic\"][\"success\"] == 7, f\"Expected 7 successes, got {data['basic']['success']}\"\n        assert data[\"divergence\"][\"d_stats\"][\"count\"] > 0, \"No divergence samples\"\n        assert data[\"divergence\"][\"unmatched_failures\"] >= 1, \"Expected at least 1 unmatched\"\n        for g in [\"early\", \"mid\", \"late\"]:\n            assert g in data[\"groups\"], f\"Missing group '{g}'\"\n        print(f\"JSON structure: OK ({len(required_keys)} top-level keys present)\")\n        print(f\"  Episodes: {data['basic']['total_episodes']}, Success: {data['basic']['success']}\")\n        print(f\"  Divergence samples: {data['divergence']['d_stats']['count']}\")\n        print(f\"  Unmatched: {data['divergence']['unmatched_failures']}\")\n        print(f\"  Groups: early={data['groups']['early']['count']}, \"\n              f\"mid={data['groups']['mid']['count']}, late={data['groups']['late']['count']}\")\n\n    # Check LaTeX\n    tex_path = output_dir / \"divergence_tables.tex\"\n    if not tex_path.exists():\n        print(f\"FAIL: {tex_path} not found\")\n        return False\n\n    with open(tex_path) as f:\n        tex = f.read()\n\n    for marker in [r\"\\begin{table}\", r\"\\end{table}\", r\"\\toprule\", r\"\\bottomrule\",\n                   r\"\\midrule\", r\"\\begin{tabular}\", \"tab:task_type_sr\",\n                   \"tab:divergence_groups\", \"tab:gamma_dist\"]:\n        if marker not in tex:\n            print(f\"FAIL: LaTeX missing '{marker}'\")\n            ok = False\n\n    if ok:\n        table_count = tex.count(r\"\\begin{table}\")\n        print(f\"LaTeX structure: OK ({table_count} tables)\")\n\n    return ok\n\n\ndef main():\n    print(\"=\" * 60)\n    print(\"MOCK DIVERGENCE TEST\")\n    print(\"=\" * 60)\n\n    traj_dir, expert_file, output_dir = generate()\n\n    script = PROJECT_ROOT / \"scripts\" / \"analyze_divergence.py\"\n    cmd = [\n        sys.executable, str(script),\n        \"--trajectory_dirs\", str(traj_dir),\n        \"--expert_file\", str(expert_file),\n        \"--output_dir\", str(output_dir),\n        \"--gamma_min\", \"0.85\",\n        \"--gamma_max\", \"0.97\",\n    ]\n\n    print(f\"\\nRunning: {' '.join(cmd)}\")\n    print(\"-\" * 60)\n    result = subprocess.run(cmd, capture_output=False)\n    print(\"-\" * 60)\n\n    if result.returncode != 0:\n        print(f\"\\nFAIL: script exited with code {result.returncode}\")\n        sys.exit(1)\n\n    print(\"\\n--- Validation ---\")\n    if validate(output_dir):\n        print(\"\\nALL CHECKS PASSED\")\n    else:\n        print(\"\\nSOME CHECKS FAILED\")\n        sys.exit(1)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "c4e7ea2e-9d5f-4d48-a628-b2144f920d1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQgzAbXgdA3pK3A8Qdm4J6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 46518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
      },
      "output_tokens": 71,
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

_source line 23 · 2026-05-13T06:40:36.045Z_

<details><summary>↩ Tool result · `toolu_011Q6TXH44xGeH7mgBDcTrJ5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/generate_mock_data.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "52061d78-4045-4f46-a0f1-9e602b81ad18",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/generate_mock_data.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Generate mock trajectory and expert data, then run analyze_divergence.py to validate output.\"\"\"\n\nimport json\nimport os\nimport subprocess\nimport sys\nfrom pathlib import Path\n\nSCRIPT_DIR = Path(__file__).parent\nPROJECT_ROOT = SCRIPT_DIR.parent.parent\nMOCK_TRAJ_DIR = SCRIPT_DIR / \"mock_trajectories\"\nMOCK_EXPERT_FILE = SCRIPT_DIR / \"mock_expert.json\"\nMOCK_OUTPUT_DIR = SCRIPT_DIR / \"mock_output\"\n\nTASK_TYPES = [\n    \"pick_and_place\",\n    \"pick_clean_then_place\",\n    \"pick_heat_then_place\",\n    \"pick_cool_then_place\",\n    \"look_at_obj\",\n    \"pick_two_obj\",\n]\n\n\ndef make_expert_actions(n_steps: int, task_idx: int) -> list[dict]:\n    \"\"\"Generate a synthetic expert conversation with n_steps actions.\"\"\"\n    msgs = [\n        {\"from\": \"human\", \"value\": f\"Your task is to: do task {task_idx}\"},\n        {\"from\": \"gpt\", \"value\": \"OK, I will help.\"},\n    ]\n    for i in range(n_steps):\n        msgs.append({\"from\": \"gpt\", \"value\": f\"Thought: step {i}\\nAction: go to shelf {i}\"})\n        msgs.append({\"from\": \"human\", \"value\": f\"Observation: You see shelf {i}.\"})\n    return msgs\n\n\ndef make_trajectory(task_idx: int, task_type: str, reward: bool,\n                    expert_actions: list[str], diverge_at: int | None) -> dict:\n    \"\"\"Generate a synthetic trajectory.\n\n    If reward=True, actions match expert exactly.\n    If reward=False, diverge at diverge_at step.\n    \"\"\"\n    game_file = f\"data/json_2.1.1/train/{task_type}/trial_{task_idx:03d}/game.tw-pddl\"\n\n    msgs = [\n        {\"role\": \"user\", \"content\": \"System instruction...\"},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n        {\"role\": \"user\", \"content\": f\"Your task is to: do task {task_idx}\"},\n    ]\n\n    n_steps = len(expert_actions)\n    for i in range(n_steps):\n        if not reward and diverge_at is not None and i >= diverge_at:\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: wrong step {i}\\nAction: take apple {i} from counter {i}\"})\n        else:\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: step {i}\\nAction: {expert_actions[i]}\"})\n        msgs.append({\"role\": \"user\", \"content\": f\"Observation: You see something at step {i}.\"})\n\n    if not reward:\n        for extra in range(2):\n            msgs.append({\"role\": \"assistant\", \"content\": f\"Thought: floundering {extra}\\nAction: look\"})\n            msgs.append({\"role\": \"user\", \"content\": \"Observation: Nothing happened.\"})\n\n    return {\n        \"task_id\": task_idx,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": reward,\n        \"steps\": n_steps + (0 if reward else 2),\n        \"conversations\": msgs,\n    }\n\n\ndef generate():\n    MOCK_TRAJ_DIR.mkdir(parents=True, exist_ok=True)\n    MOCK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    experts = []\n    trajectories = []\n\n    for idx in range(20):\n        task_type = TASK_TYPES[idx % len(TASK_TYPES)]\n        n_steps = 5 + (idx % 8)\n        expert_actions = [f\"go to shelf {i}\" for i in range(n_steps)]\n\n        game_file = f\"data/json_2.1.1/train/{task_type}/trial_{idx:03d}\"\n        experts.append({\n            \"game_file\": game_file,\n            \"conversations\": make_expert_actions(n_steps, idx),\n        })\n\n        if idx % 3 == 0:\n            # success\n            traj = make_trajectory(idx, task_type, True, expert_actions, None)\n        elif idx == 19:\n            # unmatched failure: use a game_file that won't match any expert\n            traj = make_trajectory(idx, task_type, False, expert_actions, 2)\n            traj[\"game_file\"] = \"data/json_2.1.1/train/unknown_type/trial_999/game.tw-pddl\"\n        else:\n            # failure with divergence\n            diverge_at = max(0, min(idx % n_steps, n_steps - 1))\n            traj = make_trajectory(idx, task_type, False, expert_actions, diverge_at)\n\n        trajectories.append(traj)\n\n    with open(MOCK_EXPERT_FILE, \"w\") as f:\n        json.dump(experts, f, indent=2)\n\n    traj_file = MOCK_TRAJ_DIR / \"train.jsonl\"\n    with open(traj_file, \"w\") as f:\n        for t in trajectories:\n            f.write(json.dumps(t) + \"\\n\")\n\n    print(f\"Generated {len(experts)} experts -> {MOCK_EXPERT_FILE}\")\n    print(f\"Generated {len(trajectories)} trajectories -> {traj_file}\")\n    return MOCK_TRAJ_DIR, MOCK_EXPERT_FILE, MOCK_OUTPUT_DIR\n\n\ndef validate(output_dir: Path) -> bool:\n    ok = True\n\n    # Check JSON\n    json_path = output_dir / \"divergence_summary.json\"\n    if not json_path.exists():\n        print(f\"FAIL: {json_path} not found\")\n        return False\n\n    with open(json_path) as f:\n        data = json.load(f)\n\n    required_keys = [\"basic\", \"per_task_type_sr\", \"divergence\", \"groups\", \"gamma\", \"expert_match\"]\n    for k in required_keys:\n        if k not in data:\n            print(f\"FAIL: missing top-level key '{k}' in JSON\")\n            ok = False\n\n    if ok:\n        assert data[\"basic\"][\"total_episodes\"] == 20, f\"Expected 20 episodes, got {data['basic']['total_episodes']}\"\n        assert data[\"basic\"][\"success\"] == 7, f\"Expected 7 successes, got {data['basic']['success']}\"\n        assert data[\"divergence\"][\"d_stats\"][\"count\"] > 0, \"No divergence samples\"\n        assert data[\"divergence\"][\"unmatched_failures\"] >= 1, \"Expected at least 1 unmatched\"\n        for g in [\"early\", \"mid\", \"late\"]:\n            assert g in data[\"groups\"], f\"Missing group '{g}'\"\n        print(f\"JSON structure: OK ({len(required_keys)} top-level keys present)\")\n        print(f\"  Episodes: {data['basic']['total_episodes']}, Success: {data['basic']['success']}\")\n        print(f\"  Divergence samples: {data['divergence']['d_stats']['count']}\")\n        print(f\"  Unmatched: {data['divergence']['unmatched_failures']}\")\n        print(f\"  Groups: early={data['groups']['early']['count']}, \"\n              f\"mid={data['groups']['mid']['count']}, late={data['groups']['late']['count']}\")\n\n    # Check LaTeX\n    tex_path = output_dir / \"divergence_tables.tex\"\n    if not tex_path.exists():\n        print(f\"FAIL: {tex_path} not found\")\n        return False\n\n    with open(tex_path) as f:\n        tex = f.read()\n\n    for marker in [r\"\\begin{table}\", r\"\\end{table}\", r\"\\toprule\", r\"\\bottomrule\",\n                   r\"\\midrule\", r\"\\begin{tabular}\", \"tab:task_type_sr\",\n                   \"tab:divergence_groups\", \"tab:gamma_dist\"]:\n        if marker not in tex:\n            print(f\"FAIL: LaTeX missing '{marker}'\")\n            ok = False\n\n    if ok:\n        table_count = tex.count(r\"\\begin{table}\")\n        print(f\"LaTeX structure: OK ({table_count} tables)\")\n\n    return ok\n\n\ndef main():\n    print(\"=\" * 60)\n    print(\"MOCK DIVERGENCE TEST\")\n    print(\"=\" * 60)\n\n    traj_dir, expert_file, output_dir = generate()\n\n    script = PROJECT_ROOT / \"scripts\" / \"analyze_divergence.py\"\n    cmd = [\n        sys.executable, str(script),\n        \"--trajectory_dirs\", str(traj_dir),\n        \"--expert_file\", str(expert_file),\n        \"--output_dir\", str(output_dir),\n        \"--gamma_min\", \"0.85\",\n        \"--gamma_max\", \"0.97\",\n    ]\n\n    print(f\"\\nRunning: {' '.join(cmd)}\")\n    print(\"-\" * 60)\n    result = subprocess.run(cmd, capture_output=False)\n    print(\"-\" * 60)\n\n    if result.returncode != 0:\n        print(f\"\\nFAIL: script exited with code {result.returncode}\")\n        sys.exit(1)\n\n    print(\"\\n--- Validation ---\")\n    if validate(output_dir):\n        print(\"\\nALL CHECKS PASSED\")\n    else:\n        print(\"\\nSOME CHECKS FAILED\")\n        sys.exit(1)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 24_

Running the mock test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "6fa67cf9-cb34-4f89-899e-056da6a853df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFhXgGNs9VLRh6rnoUVaHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2614,
      "cache_read_input_tokens": 46761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2614
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01FVAf7pKHrYRjjxq7Awzfea`</summary>

```json
{
  "command": "python tests/mock_divergence_test/generate_mock_data.py",
  "description": "Run mock divergence test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "f4136898-6cb9-45a4-b7a4-00618383c2c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFhXgGNs9VLRh6rnoUVaHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2614,
      "cache_read_input_tokens": 46761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2614
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

### Runtime record

_source line 26_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778821200,
    "rateLimitType": "seven_day",
    "utilization": 0.77,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "94150cd7-e440-49dd-9002-d7a8ffd4014a",
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea"
}
```

---

### Tool result

_source line 27 · 2026-05-13T06:40:39.092Z_

<details><summary>↩ Tool result · reported error · `toolu_01FVAf7pKHrYRjjxq7Awzfea`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "2c793c13-986c-4ab1-85e5-17afb4468bc6",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y9AcVaeEJfAuc18qZZPd5n`</summary>

```json
{
  "command": "python3 tests/mock_divergence_test/generate_mock_data.py",
  "description": "Run mock divergence test with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "5eea6f88-2020-4a36-b3f9-7ba8947b1a3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TZF8N1iDnG2JoZBeVT3tQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 49375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
      },
      "output_tokens": 71,
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

_source line 29 · 2026-05-13T06:40:42.386Z_

<details><summary>↩ Tool result · `toolu_01Y9AcVaeEJfAuc18qZZPd5n`</summary>

```text
============================================================
DIVERGENCE ANALYSIS SUMMARY
============================================================
Episodes: 20  Success: 7  Failure: 13  SR: 35.0%

--- Per-task-type success rate ---
Type                       Total   Succ     Rate
--------------------------------------------------
look_at_obj                    3      0     0.0%
pick_and_place                 4      4   100.0%
pick_clean_then_place          4      0     0.0%
pick_cool_then_place           3      3   100.0%
pick_heat_then_place           3      0     0.0%
pick_two_obj                   3      0     0.0%

--- Divergence point (d = div_point / expert_len) ---
Matched failures: 12  Unmatched: 1
Mean: 0.416  Median: 0.402  Std: 0.192
Min: 0.167  Max: 0.833  Q25: 0.282  Q75: 0.521

Histogram:
     [0.0,0.1):    0 
     [0.1,0.2):    1 #
     [0.2,0.3):    3 ###
     [0.3,0.4):    2 ##
     [0.4,0.5):    2 ##
     [0.5,0.6):    2 ##
     [0.6,0.7):    1 #
     [0.7,0.8):    0 
     [0.8,0.9):    1 #
     [0.9,1.0]:    0 

--- Early / Mid / Late ---
Stage     Count     Prop  Avg CSpan    Avg d
---------------------------------------------
early         5    41.7%        5.8    0.245
mid           6    50.0%        4.3    0.489
late          1     8.3%        1.0    0.833

--- γ(d) distribution (γ_min=0.85, γ_max=0.97) ---
Mean: 0.8999  Median: 0.8982  Std: 0.0230
Min: 0.8700  Max: 0.9500

--- Expert matching ---
Matched: 12  Unmatched: 1  Match rate: 92.3%
============================================================

JSON: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_summary.json
LaTeX: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_tables.tex
============================================================
MOCK DIVERGENCE TEST
============================================================
Generated 20 experts -> /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_expert.json
Generated 20 trajectories -> /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_trajectories/train.jsonl

Running: /usr/bin/python3 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/analyze_divergence.py --trajectory_dirs /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_trajectories --expert_file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_expert.json --output_dir /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output --gamma_min 0.85 --gamma_max 0.97
------------------------------------------------------------
------------------------------------------------------------

--- Validation ---
JSON structure: OK (6 top-level keys present)
  Episodes: 20, Success: 7
  Divergence samples: 12
  Unmatched: 1
  Groups: early=5, mid=6, late=1
LaTeX structure: OK (3 tables)

ALL CHECKS PASSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "9a4aa08f-9952-4513-b4c0-acb29905eb70",
  "tool_use_result": {
    "stdout": "============================================================\nDIVERGENCE ANALYSIS SUMMARY\n============================================================\nEpisodes: 20  Success: 7  Failure: 13  SR: 35.0%\n\n--- Per-task-type success rate ---\nType                       Total   Succ     Rate\n--------------------------------------------------\nlook_at_obj                    3      0     0.0%\npick_and_place                 4      4   100.0%\npick_clean_then_place          4      0     0.0%\npick_cool_then_place           3      3   100.0%\npick_heat_then_place           3      0     0.0%\npick_two_obj                   3      0     0.0%\n\n--- Divergence point (d = div_point / expert_len) ---\nMatched failures: 12  Unmatched: 1\nMean: 0.416  Median: 0.402  Std: 0.192\nMin: 0.167  Max: 0.833  Q25: 0.282  Q75: 0.521\n\nHistogram:\n     [0.0,0.1):    0 \n     [0.1,0.2):    1 #\n     [0.2,0.3):    3 ###\n     [0.3,0.4):    2 ##\n     [0.4,0.5):    2 ##\n     [0.5,0.6):    2 ##\n     [0.6,0.7):    1 #\n     [0.7,0.8):    0 \n     [0.8,0.9):    1 #\n     [0.9,1.0]:    0 \n\n--- Early / Mid / Late ---\nStage     Count     Prop  Avg CSpan    Avg d\n---------------------------------------------\nearly         5    41.7%        5.8    0.245\nmid           6    50.0%        4.3    0.489\nlate          1     8.3%        1.0    0.833\n\n--- γ(d) distribution (γ_min=0.85, γ_max=0.97) ---\nMean: 0.8999  Median: 0.8982  Std: 0.0230\nMin: 0.8700  Max: 0.9500\n\n--- Expert matching ---\nMatched: 12  Unmatched: 1  Match rate: 92.3%\n============================================================\n\nJSON: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_summary.json\nLaTeX: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_tables.tex\n============================================================\nMOCK DIVERGENCE TEST\n============================================================\nGenerated 20 experts -> /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_expert.json\nGenerated 20 trajectories -> /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_trajectories/train.jsonl\n\nRunning: /usr/bin/python3 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/scripts/analyze_divergence.py --trajectory_dirs /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_trajectories --expert_file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_expert.json --output_dir /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output --gamma_min 0.85 --gamma_max 0.97\n------------------------------------------------------------\n------------------------------------------------------------\n\n--- Validation ---\nJSON structure: OK (6 top-level keys present)\n  Episodes: 20, Success: 7\n  Divergence samples: 12\n  Unmatched: 1\n  Groups: early=5, mid=6, late=1\nLaTeX structure: OK (3 tables)\n\nALL CHECKS PASSED",
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

_source line 30_

全部通过。验证一下生成的 LaTeX 格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "936d9e37-8203-4a77-b7a0-d096ec1f44b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SD4fNB4U5cPwteHipp6BR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 49509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1209
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_018dXNmtY6krVUdWHFUDpHu6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_tables.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "78e38977-a4ee-408f-b002-de4db3a26b9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SD4fNB4U5cPwteHipp6BR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 49509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1209
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

_source line 32 · 2026-05-13T06:40:46.014Z_

<details><summary>↩ Tool result · `toolu_018dXNmtY6krVUdWHFUDpHu6`</summary>

```text
1	% Table 1: Per-task-type success rate
2	\begin{table}[t]
3	\centering
4	\caption{Per-task-type success rate.}
5	\label{tab:task_type_sr}
6	\begin{tabular}{lrrr}
7	\toprule
8	Task Type & Total & Success & Rate (\%) \\
9	\midrule
10	examine & 3 & 0 & 0.0 \\
11	put & 4 & 4 & 100.0 \\
12	clean & 4 & 0 & 0.0 \\
13	cool & 3 & 3 & 100.0 \\
14	heat & 3 & 0 & 0.0 \\
15	puttwo & 3 & 0 & 0.0 \\
16	\midrule
17	Overall & 20 & 7 & 35.0 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
22	% Table 2: Divergence point distribution
23	\begin{table}[t]
24	\centering
25	\caption{Divergence point distribution by failure stage.}
26	\label{tab:divergence_groups}
27	\begin{tabular}{lcrrr}
28	\toprule
29	Stage & $d$ range & Count & Prop. (\%) & Avg.\ $C_{\text{span}}$ \\
30	\midrule
31	Early & $[0, 0.33)$ & 5 & 41.7 & 5.8 \\
32	Mid & $[0.33, 0.67)$ & 6 & 50.0 & 4.3 \\
33	Late & $[0.67, 1.0]$ & 1 & 8.3 & 1.0 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	% Table 3: Gamma distribution statistics
39	\begin{table}[t]
40	\centering
41	\caption{$\gamma(d)$ distribution ($\gamma_{\min}=0.85, \gamma_{\max}=0.97$).}
42	\label{tab:gamma_dist}
43	\begin{tabular}{lr}
44	\toprule
45	Statistic & Value \\
46	\midrule
47	Mean & 0.8999 \\
48	Median & 0.8982 \\
49	Std & 0.0230 \\
50	Min & 0.8700 \\
51	Max & 0.9500 \\
52	Q25 & 0.8839 \\
53	Q75 & 0.9125 \\
54	\bottomrule
55	\end{tabular}
56	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "6f4e14c2-f31f-4a7f-9e34-b0cb2cdde366",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/tests/mock_divergence_test/mock_output/divergence_tables.tex",
      "content": "% Table 1: Per-task-type success rate\n\\begin{table}[t]\n\\centering\n\\caption{Per-task-type success rate.}\n\\label{tab:task_type_sr}\n\\begin{tabular}{lrrr}\n\\toprule\nTask Type & Total & Success & Rate (\\%) \\\\\n\\midrule\nexamine & 3 & 0 & 0.0 \\\\\nput & 4 & 4 & 100.0 \\\\\nclean & 4 & 0 & 0.0 \\\\\ncool & 3 & 3 & 100.0 \\\\\nheat & 3 & 0 & 0.0 \\\\\nputtwo & 3 & 0 & 0.0 \\\\\n\\midrule\nOverall & 20 & 7 & 35.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Table 2: Divergence point distribution\n\\begin{table}[t]\n\\centering\n\\caption{Divergence point distribution by failure stage.}\n\\label{tab:divergence_groups}\n\\begin{tabular}{lcrrr}\n\\toprule\nStage & $d$ range & Count & Prop. (\\%) & Avg.\\ $C_{\\text{span}}$ \\\\\n\\midrule\nEarly & $[0, 0.33)$ & 5 & 41.7 & 5.8 \\\\\nMid & $[0.33, 0.67)$ & 6 & 50.0 & 4.3 \\\\\nLate & $[0.67, 1.0]$ & 1 & 8.3 & 1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Table 3: Gamma distribution statistics\n\\begin{table}[t]\n\\centering\n\\caption{$\\gamma(d)$ distribution ($\\gamma_{\\min}=0.85, \\gamma_{\\max}=0.97$).}\n\\label{tab:gamma_dist}\n\\begin{tabular}{lr}\n\\toprule\nStatistic & Value \\\\\n\\midrule\nMean & 0.8999 \\\\\nMedian & 0.8982 \\\\\nStd & 0.0230 \\\\\nMin & 0.8700 \\\\\nMax & 0.9500 \\\\\nQ25 & 0.8839 \\\\\nQ75 & 0.9125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

完成。产出：

1. **`scripts/analyze_divergence.py`** — 完整 CLI，支持多目录输入、expert 匹配、divergence 分布分析、early/mid/late 分组、γ(d) 映射。输出 JSON + LaTeX 表格 + stdout summary。
2. **`tests/mock_divergence_test/`** — mock 数据生成 + 自动验证脚本，20 条 trajectory（7 success, 12 matched failures, 1 unmatched），所有检查通过。
3. LaTeX 3 张表格格式正确（booktabs），可直接 `\input` 到论文。

v7 数据到后直接跑：
```bash
python3 scripts/analyze_divergence.py \
  --trajectory_dirs data/trajectories_v7_icl_cuda0 data/trajectories_v7_icl_cuda1 \
  --expert_file data/alfworld_sft.json \
  --output_dir outputs/divergence_analysis
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "uuid": "75c117e5-149c-4d18-b033-6bf648dcb96e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSoVWPhBPQjQdUuf4K8ZVf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 50718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 898
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

_source line 34_

完成。产出：

1. **`scripts/analyze_divergence.py`** — 完整 CLI，支持多目录输入、expert 匹配、divergence 分布分析、early/mid/late 分组、γ(d) 映射。输出 JSON + LaTeX 表格 + stdout summary。
2. **`tests/mock_divergence_test/`** — mock 数据生成 + 自动验证脚本，20 条 trajectory（7 success, 12 matched failures, 1 unmatched），所有检查通过。
3. LaTeX 3 张表格格式正确（booktabs），可直接 `\input` 到论文。

v7 数据到后直接跑：
```bash
python3 scripts/analyze_divergence.py \
  --trajectory_dirs data/trajectories_v7_icl_cuda0 data/trajectories_v7_icl_cuda1 \
  --expert_file data/alfworld_sft.json \
  --output_dir outputs/divergence_analysis
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 145679,
  "duration_api_ms": 145912,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "bf7a0433-08a1-4d4e-bfac-2b25fb4621ea",
  "total_cost_usd": 0.6756657500000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 39775,
    "cache_read_input_tokens": 359834,
    "output_tokens": 9799,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39775,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 277,
        "cache_read_input_tokens": 50718,
        "cache_creation_input_tokens": 898,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 898
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2040,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002125,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 9799,
      "cacheReadInputTokens": 359834,
      "cacheCreationInputTokens": 39775,
      "webSearchRequests": 0,
      "costUSD": 0.67354075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0497a756-ca36-4fa6-bbca-d4fa80f8015f"
}
```

</details>

---
