# research re repair code audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_research_re-repair-code-audit_20260517T040024.log`
- **Structured JSON:** [`a6d67460b869a8c83a34.json`](../../sessions/a6/a6d67460b869a8c83a34.json)

## Before a recorded user message

10 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
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
  "uuid": "ef343e44-c899-448a-8d2f-1825ca5b6456",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779006600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d7a3d092-fdf8-4251-9fd9-a661e083cc8a",
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the two files the user wants me to analyze.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "6b81567c-8a99-4c47-b96b-4450dcd49fc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJ7mtmWUN2DQ7ShKp715h6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13799
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — Read · `toolu_01N94fSYZjQkwX5KZnwNe69i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/re_repair_phase0.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "61ddadfc-b2d2-474e-9780-d9d89a3499c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJ7mtmWUN2DQ7ShKp715h6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13799
      },
      "output_tokens": 37,
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

_source line 6 · 2026-05-17T04:00:36.914Z_

<details><summary>↩ Tool result · `toolu_01N94fSYZjQkwX5KZnwNe69i`</summary>

````text
1	#!/usr/bin/env python3
2	"""
3	Re-Repair Phase 0: Quick feasibility test with oracle labels.
4	No Docker verification — evaluates via diff similarity to gold patch.
5	
6	Runs 10 instances × 1 mutation patch × 4 conditions × K=5 samples.
7	"""
8	
9	import argparse
10	import difflib
11	import json
12	import logging
13	import os
14	import re
15	from collections import defaultdict
16	from pathlib import Path
17	
18	import numpy as np
19	
20	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
21	log = logging.getLogger(__name__)
22	
23	CONDITIONS = ["control", "cls-diag", "oracle-diag", "random-diag"]
24	
25	SYSTEM_PROMPT = (
26	    "You are a software engineer. You are given a code patch that was intended "
27	    "to fix an issue but does not fully work. Your task is to produce a corrected "
28	    "patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
29	)
30	
31	DIAGNOSTIC_TEMPLATE = (
32	    "## Test Diagnostic\n"
33	    "The current patch **fails** the following tests:\n{fail_list}\n\n"
34	    "The current patch **passes** the following tests:\n{pass_list}"
35	)
36	
37	
38	def load_jsonl(path):
39	    with open(path) as f:
40	        return [json.loads(line) for line in f]
41	
42	
43	def save_jsonl(data, path):
44	    os.makedirs(os.path.dirname(path), exist_ok=True)
45	    with open(path, "w") as f:
46	        for item in data:
47	            f.write(json.dumps(item, ensure_ascii=False) + "\n")
48	    log.info(f"Saved {len(data)} records to {path}")
49	
50	
51	def extract_diff(text):
52	    """Extract unified diff from LLM response."""
53	    if "&lt;/think>" in text:
54	        text = text.split("&lt;/think>", 1)[-1]
55	    m = re.search(r"```diff\s*\n(.*?)```", text, re.DOTALL)
56	    if m:
57	        return m.group(1).strip()
58	    m = re.search(r"```\s*\n(diff.*?)```", text, re.DOTALL)
59	    if m:
60	        return m.group(1).strip()
61	    m = re.search(r"(diff --git.*)", text, re.DOTALL)
62	    if m:
63	        return m.group(1).strip()
64	    return text.strip()
65	
66	
67	def diff_similarity(generated, gold):
68	    """Compute normalized sequence similarity between two diffs."""
69	    if not generated or not gold:
70	        return 0.0
71	    return difflib.SequenceMatcher(None, generated, gold).ratio()
72	
73	
74	def format_diagnostic(per_test):
75	    """Format per-test results into diagnostic prompt section."""
76	    if not per_test:
77	        return ""
78	    fails = [t for t, passed in per_test.items() if not passed]
79	    passes = [t for t, passed in per_test.items() if passed]
80	    if not fails:
81	        return ""
82	    fail_list = "\n".join(f"- `{t}`" for t in fails)
83	    pass_list = "\n".join(f"- `{t}`" for t in passes) if passes else "*(none)*"
84	    return DIAGNOSTIC_TEMPLATE.format(fail_list=fail_list, pass_list=pass_list)
85	
86	
87	def build_prompt(item, condition, rng):
88	    """Build repair prompt messages for a given condition."""
89	    base = (
90	        f"## Issue Description\n{item['problem_statement']}\n\n"
91	        f"## Current (Incorrect) Patch\n```diff\n{item['mutation_patch']}\n```\n"
92	    )
93	
94	    if condition == "control":
95	        diag = ""
96	    elif condition == "oracle-diag":
97	        diag = format_diagnostic(item["oracle_per_test"])
98	    elif condition == "cls-diag":
99	        # Phase 0: simulate CLS at ~84% accuracy by flipping 16% of oracle labels
100	        oracle = item["oracle_per_test"]
101	        simulated = {}
102	        for t, v in oracle.items():
103	            if rng.random() < 0.16:
104	                simulated[t] = not v
105	            else:
106	                simulated[t] = v
107	        diag = format_diagnostic(simulated)
108	    elif condition == "random-diag":
109	        all_tests = list(item["oracle_per_test"].keys())
110	        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
111	        diag = format_diagnostic(per_test)
112	    else:
113	        raise ValueError(f"Unknown condition: {condition}")
114	
115	    user_content = base
116	    if diag:
117	        user_content += f"\n{diag}\n"
118	    user_content += (
119	        "\nPlease produce a corrected patch in unified diff format."
120	        "\nOutput ONLY the diff, enclosed in ```diff ... ``` tags."
121	    )
122	
123	    return [
124	        {"role": "system", "content": SYSTEM_PROMPT},
125	        {"role": "user", "content": user_content},
126	    ]
127	
128	
129	def prepare_phase0_data(data_dir, n_instances=10, seed=42):
130	    """Prepare Phase 0 dataset from local data files + HF dataset."""
131	    from datasets import load_dataset
132	
133	    log.info("Loading SWE-bench Verified from HuggingFace...")
134	    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
135	    instance_info = {}
136	    for row in ds:
137	        f2p = json.loads(row["FAIL_TO_PASS"])
138	        if len(f2p) >= 2:
139	            instance_info[row["instance_id"]] = {
140	                "problem_statement": row.get("problem_statement", ""),
141	                "fail_to_pass": f2p,
142	                "pass_to_pass": json.loads(row["PASS_TO_PASS"]),
143	                "gold_patch": row["patch"],
144	            }
145	    log.info(f"T>=2 instances from HF: {len(instance_info)}")
146	
147	    # Load mutation patches
148	    mutation_files = list(Path(data_dir).glob("predictions_mutation_*.jsonl"))
149	    mutations_by_instance = defaultdict(list)
150	    for mf in mutation_files:
151	        mutation_type = mf.stem.replace("predictions_mutation_", "")
152	        for line in mf.open():
153	            rec = json.loads(line)
154	            iid = rec["instance_id"]
155	            if iid in instance_info:
156	                mutations_by_instance[iid].append({
157	                    "patch": rec["model_patch"],
158	                    "type": mutation_type,
159	                })
160	
161	    # Load per-test oracle labels from swebench_test.jsonl
162	    test_data = load_jsonl(os.path.join(data_dir, "swebench_test.jsonl"))
163	    # Group by (problem_id, mutation_type, patch) -> {test_name: label}
164	    oracle_labels = defaultdict(dict)
165	    for row in test_data:
166	        if row.get("mutation_type", "gold") != "gold":
167	            key = (row["metadata"]["instance_id"], row.get("mutation_type", ""))
168	            test_name = row["test"] if isinstance(row["test"], str) else row["metadata"].get("test_name", "")
169	            oracle_labels[key][test_name] = bool(row["label"])
170	
171	    # Select instances that have both: mutation patches AND oracle labels for them
172	    rng = np.random.default_rng(seed)
173	    candidates = []
174	    for iid, info in instance_info.items():
175	        muts = mutations_by_instance.get(iid, [])
176	        if not muts:
177	            continue
178	        # Check if we have oracle labels for any mutation
179	        for mut in muts:
180	            key = (iid, mut["type"])
181	            if key in oracle_labels and len(oracle_labels[key]) >= 2:
182	                candidates.append({
183	                    "instance_id": iid,
184	                    "problem_statement": info["problem_statement"],
185	                    "gold_patch": info["gold_patch"],
186	                    "fail_to_pass": info["fail_to_pass"],
187	                    "mutation_patch": mut["patch"],
188	                    "mutation_type": mut["type"],
189	                    "oracle_per_test": oracle_labels[key],
190	                })
191	                break  # one mutation per instance for Phase 0
192	
193	    log.info(f"Candidates with mutation + oracle labels: {len(candidates)}")
194	
195	    if len(candidates) < n_instances:
196	        log.warning(f"Only {len(candidates)} candidates available, using all")
197	        selected = candidates
198	    else:
199	        indices = rng.choice(len(candidates), size=n_instances, replace=False)
200	        selected = [candidates[i] for i in sorted(indices)]
201	
202	    log.info(f"Selected {len(selected)} instances for Phase 0")
203	    for i, s in enumerate(selected):
204	        n_fail = sum(1 for v in s["oracle_per_test"].values() if not v)
205	        n_pass = sum(1 for v in s["oracle_per_test"].values() if v)
206	        log.info(f"  [{i}] {s['instance_id']} ({s['mutation_type']}) "
207	                 f"oracle: {n_fail} fail, {n_pass} pass")
208	
209	    return selected
210	
211	
212	def generate_repairs(dataset, model_path, conditions, n_samples=5, output_dir="."):
213	    """Generate repairs using vLLM."""
214	    from vllm import LLM, SamplingParams
215	
216	    log.info(f"Loading model: {model_path}")
217	    llm = LLM(
218	        model=model_path,
219	        tensor_parallel_size=1,
220	        max_model_len=8192,
221	        trust_remote_code=True,
222	        dtype="bfloat16",
223	        gpu_memory_utilization=0.85,
224	    )
225	    tokenizer = llm.get_tokenizer()
226	
227	    sampling_params = SamplingParams(
228	        temperature=0.6,
229	        top_p=0.95,
230	        max_tokens=2048,
231	        n=n_samples,
232	    )
233	
234	    rng = np.random.default_rng(42)
235	    all_results = []
236	
237	    for cond in conditions:
238	        log.info(f"=== Condition: {cond} ===")
239	        prompts = []
240	        meta = []
241	
242	        for item in dataset:
243	            messages = build_prompt(item, cond, rng)
244	            prompt_text = tokenizer.apply_chat_template(
245	                messages, tokenize=False, add_generation_prompt=True
246	            )
247	            prompts.append(prompt_text)
248	            meta.append({
249	                "instance_id": item["instance_id"],
250	                "condition": cond,
251	                "mutation_type": item["mutation_type"],
252	                "gold_patch": item["gold_patch"],
253	            })
254	
255	        log.info(f"Generating {len(prompts)} prompts × {n_samples} samples...")
256	        outputs = llm.generate(prompts, sampling_params)
257	
258	        for output, m in zip(outputs, meta):
259	            for k, completion in enumerate(output.outputs):
260	                diff = extract_diff(completion.text)
261	                sim = diff_similarity(diff, m["gold_patch"])
262	                all_results.append({
263	                    "instance_id": m["instance_id"],
264	                    "condition": m["condition"],
265	                    "mutation_type": m["mutation_type"],
266	                    "sample_k": k,
267	                    "extracted_diff": diff,
268	                    "gold_similarity": sim,
269	                    "diff_nonempty": len(diff) > 20,
270	                    "has_diff_header": diff.startswith("diff ") or diff.startswith("---"),
271	                })
272	
273	        cond_sims = [r["gold_similarity"] for r in all_results if r["condition"] == cond]
274	        log.info(f"  Mean gold similarity: {np.mean(cond_sims):.3f} "
275	                 f"(max={np.max(cond_sims):.3f}, nonempty={sum(1 for r in all_results if r['condition']==cond and r['diff_nonempty'])}/{len(cond_sims)})")
276	
277	    out_path = os.path.join(output_dir, "phase0_repairs.jsonl")
278	    save_jsonl(all_results, out_path)
279	    return all_results
280	
281	
282	def analyze_results(results, output_dir="."):
283	    """Analyze Phase 0 results."""
284	    log.info("=== Phase 0 Analysis ===")
285	
286	    by_cond = defaultdict(list)
287	    for r in results:
288	        by_cond[r["condition"]].append(r)
289	
290	    summary = {}
291	    for cond in CONDITIONS:
292	        if cond not in by_cond:
293	            continue
294	        entries = by_cond[cond]
295	        sims = [e["gold_similarity"] for e in entries]
296	        nonempty = sum(1 for e in entries if e["diff_nonempty"])
297	        has_header = sum(1 for e in entries if e["has_diff_header"])
298	
299	        # Best-of-K similarity per instance
300	        by_inst = defaultdict(list)
301	        for e in entries:
302	            by_inst[e["instance_id"]].append(e["gold_similarity"])
303	        best_per_inst = [max(sims_list) for sims_list in by_inst.values()]
304	
305	        summary[cond] = {
306	            "n_samples": len(entries),
307	            "mean_similarity": float(np.mean(sims)),
308	            "max_similarity": float(np.max(sims)),
309	            "best_of_k_mean": float(np.mean(best_per_inst)),
310	            "best_of_k_max": float(np.max(best_per_inst)),
311	            "pct_nonempty": nonempty / len(entries) * 100,
312	            "pct_valid_diff": has_header / len(entries) * 100,
313	        }
314	
315	        log.info(f"\n  {cond}:")
316	        log.info(f"    Mean sim: {summary[cond]['mean_similarity']:.3f}")
317	        log.info(f"    Best-of-K mean: {summary[cond]['best_of_k_mean']:.3f}")
318	        log.info(f"    Best-of-K max: {summary[cond]['best_of_k_max']:.3f}")
319	        log.info(f"    Valid diff: {summary[cond]['pct_valid_diff']:.0f}%")
320	
321	    # Deltas
322	    if "control" in summary and "oracle-diag" in summary:
323	        delta_oracle = summary["oracle-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
324	        log.info(f"\n  Δ(oracle-diag - control) best-of-K: {delta_oracle:+.3f}")
325	    if "control" in summary and "cls-diag" in summary:
326	        delta_cls = summary["cls-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
327	        log.info(f"  Δ(cls-diag - control) best-of-K: {delta_cls:+.3f}")
328	    if "control" in summary and "random-diag" in summary:
329	        delta_rand = summary["random-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
330	        log.info(f"  Δ(random-diag - control) best-of-K: {delta_rand:+.3f}")
331	
332	    out_path = os.path.join(output_dir, "phase0_summary.json")
333	    os.makedirs(output_dir, exist_ok=True)
334	    with open(out_path, "w") as f:
335	        json.dump(summary, f, indent=2)
336	    log.info(f"\nSaved summary to {out_path}")
337	
338	    return summary
339	
340	
341	def main():
342	    parser = argparse.ArgumentParser(description="Re-Repair Phase 0")
343	    parser.add_argument("--data-dir", required=True,
344	                        help="Path to data/swebench_full/")
345	    parser.add_argument("--model", default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B",
346	                        help="Model path")
347	    parser.add_argument("--n-instances", type=int, default=10)
348	    parser.add_argument("--n-samples", type=int, default=5,
349	                        help="Completions per (instance, condition)")
350	    parser.add_argument("--conditions", nargs="+", default=CONDITIONS)
351	    parser.add_argument("--output-dir", default="/root/autodl-tmp/eval_results/re_repair_phase0")
352	    parser.add_argument("--seed", type=int, default=42)
353	    parser.add_argument("--analyze-only", type=str, default=None,
354	                        help="Path to existing phase0_repairs.jsonl to analyze")
355	    args = parser.parse_args()
356	
357	    if args.analyze_only:
358	        results = load_jsonl(args.analyze_only)
359	        analyze_results(results, args.output_dir)
360	        return
361	
362	    # Step 1: Prepare data
363	    dataset = prepare_phase0_data(args.data_dir, args.n_instances, args.seed)
364	
365	    # Save prepared dataset
366	    prep_path = os.path.join(args.output_dir, "phase0_dataset.jsonl")
367	    save_jsonl(dataset, prep_path)
368	
369	    # Step 2: Generate repairs
370	    results = generate_repairs(
371	        dataset, args.model, args.conditions, args.n_samples, args.output_dir
372	    )
373	
374	    # Step 3: Analyze
375	    analyze_results(results, args.output_dir)
376	
377	
378	if __name__ == "__main__":
379	    main()
380	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "86ace247-0709-4962-99ce-1cf5241bdb19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/re_repair_phase0.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nRe-Repair Phase 0: Quick feasibility test with oracle labels.\nNo Docker verification — evaluates via diff similarity to gold patch.\n\nRuns 10 instances × 1 mutation patch × 4 conditions × K=5 samples.\n\"\"\"\n\nimport argparse\nimport difflib\nimport json\nimport logging\nimport os\nimport re\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\nCONDITIONS = [\"control\", \"cls-diag\", \"oracle-diag\", \"random-diag\"]\n\nSYSTEM_PROMPT = (\n    \"You are a software engineer. You are given a code patch that was intended \"\n    \"to fix an issue but does not fully work. Your task is to produce a corrected \"\n    \"patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags.\"\n)\n\nDIAGNOSTIC_TEMPLATE = (\n    \"## Test Diagnostic\\n\"\n    \"The current patch **fails** the following tests:\\n{fail_list}\\n\\n\"\n    \"The current patch **passes** the following tests:\\n{pass_list}\"\n)\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef save_jsonl(data, path):\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    with open(path, \"w\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n    log.info(f\"Saved {len(data)} records to {path}\")\n\n\ndef extract_diff(text):\n    \"\"\"Extract unified diff from LLM response.\"\"\"\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\", 1)[-1]\n    m = re.search(r\"```diff\\s*\\n(.*?)```\", text, re.DOTALL)\n    if m:\n        return m.group(1).strip()\n    m = re.search(r\"```\\s*\\n(diff.*?)```\", text, re.DOTALL)\n    if m:\n        return m.group(1).strip()\n    m = re.search(r\"(diff --git.*)\", text, re.DOTALL)\n    if m:\n        return m.group(1).strip()\n    return text.strip()\n\n\ndef diff_similarity(generated, gold):\n    \"\"\"Compute normalized sequence similarity between two diffs.\"\"\"\n    if not generated or not gold:\n        return 0.0\n    return difflib.SequenceMatcher(None, generated, gold).ratio()\n\n\ndef format_diagnostic(per_test):\n    \"\"\"Format per-test results into diagnostic prompt section.\"\"\"\n    if not per_test:\n        return \"\"\n    fails = [t for t, passed in per_test.items() if not passed]\n    passes = [t for t, passed in per_test.items() if passed]\n    if not fails:\n        return \"\"\n    fail_list = \"\\n\".join(f\"- `{t}`\" for t in fails)\n    pass_list = \"\\n\".join(f\"- `{t}`\" for t in passes) if passes else \"*(none)*\"\n    return DIAGNOSTIC_TEMPLATE.format(fail_list=fail_list, pass_list=pass_list)\n\n\ndef build_prompt(item, condition, rng):\n    \"\"\"Build repair prompt messages for a given condition.\"\"\"\n    base = (\n        f\"## Issue Description\\n{item['problem_statement']}\\n\\n\"\n        f\"## Current (Incorrect) Patch\\n```diff\\n{item['mutation_patch']}\\n```\\n\"\n    )\n\n    if condition == \"control\":\n        diag = \"\"\n    elif condition == \"oracle-diag\":\n        diag = format_diagnostic(item[\"oracle_per_test\"])\n    elif condition == \"cls-diag\":\n        # Phase 0: simulate CLS at ~84% accuracy by flipping 16% of oracle labels\n        oracle = item[\"oracle_per_test\"]\n        simulated = {}\n        for t, v in oracle.items():\n            if rng.random() < 0.16:\n                simulated[t] = not v\n            else:\n                simulated[t] = v\n        diag = format_diagnostic(simulated)\n    elif condition == \"random-diag\":\n        all_tests = list(item[\"oracle_per_test\"].keys())\n        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}\n        diag = format_diagnostic(per_test)\n    else:\n        raise ValueError(f\"Unknown condition: {condition}\")\n\n    user_content = base\n    if diag:\n        user_content += f\"\\n{diag}\\n\"\n    user_content += (\n        \"\\nPlease produce a corrected patch in unified diff format.\"\n        \"\\nOutput ONLY the diff, enclosed in ```diff ... ``` tags.\"\n    )\n\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_content},\n    ]\n\n\ndef prepare_phase0_data(data_dir, n_instances=10, seed=42):\n    \"\"\"Prepare Phase 0 dataset from local data files + HF dataset.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading SWE-bench Verified from HuggingFace...\")\n    ds = load_dataset(\"princeton-nlp/SWE-bench_Verified\", split=\"test\")\n    instance_info = {}\n    for row in ds:\n        f2p = json.loads(row[\"FAIL_TO_PASS\"])\n        if len(f2p) >= 2:\n            instance_info[row[\"instance_id\"]] = {\n                \"problem_statement\": row.get(\"problem_statement\", \"\"),\n                \"fail_to_pass\": f2p,\n                \"pass_to_pass\": json.loads(row[\"PASS_TO_PASS\"]),\n                \"gold_patch\": row[\"patch\"],\n            }\n    log.info(f\"T>=2 instances from HF: {len(instance_info)}\")\n\n    # Load mutation patches\n    mutation_files = list(Path(data_dir).glob(\"predictions_mutation_*.jsonl\"))\n    mutations_by_instance = defaultdict(list)\n    for mf in mutation_files:\n        mutation_type = mf.stem.replace(\"predictions_mutation_\", \"\")\n        for line in mf.open():\n            rec = json.loads(line)\n            iid = rec[\"instance_id\"]\n            if iid in instance_info:\n                mutations_by_instance[iid].append({\n                    \"patch\": rec[\"model_patch\"],\n                    \"type\": mutation_type,\n                })\n\n    # Load per-test oracle labels from swebench_test.jsonl\n    test_data = load_jsonl(os.path.join(data_dir, \"swebench_test.jsonl\"))\n    # Group by (problem_id, mutation_type, patch) -> {test_name: label}\n    oracle_labels = defaultdict(dict)\n    for row in test_data:\n        if row.get(\"mutation_type\", \"gold\") != \"gold\":\n            key = (row[\"metadata\"][\"instance_id\"], row.get(\"mutation_type\", \"\"))\n            test_name = row[\"test\"] if isinstance(row[\"test\"], str) else row[\"metadata\"].get(\"test_name\", \"\")\n            oracle_labels[key][test_name] = bool(row[\"label\"])\n\n    # Select instances that have both: mutation patches AND oracle labels for them\n    rng = np.random.default_rng(seed)\n    candidates = []\n    for iid, info in instance_info.items():\n        muts = mutations_by_instance.get(iid, [])\n        if not muts:\n            continue\n        # Check if we have oracle labels for any mutation\n        for mut in muts:\n            key = (iid, mut[\"type\"])\n            if key in oracle_labels and len(oracle_labels[key]) >= 2:\n                candidates.append({\n                    \"instance_id\": iid,\n                    \"problem_statement\": info[\"problem_statement\"],\n                    \"gold_patch\": info[\"gold_patch\"],\n                    \"fail_to_pass\": info[\"fail_to_pass\"],\n                    \"mutation_patch\": mut[\"patch\"],\n                    \"mutation_type\": mut[\"type\"],\n                    \"oracle_per_test\": oracle_labels[key],\n                })\n                break  # one mutation per instance for Phase 0\n\n    log.info(f\"Candidates with mutation + oracle labels: {len(candidates)}\")\n\n    if len(candidates) < n_instances:\n        log.warning(f\"Only {len(candidates)} candidates available, using all\")\n        selected = candidates\n    else:\n        indices = rng.choice(len(candidates), size=n_instances, replace=False)\n        selected = [candidates[i] for i in sorted(indices)]\n\n    log.info(f\"Selected {len(selected)} instances for Phase 0\")\n    for i, s in enumerate(selected):\n        n_fail = sum(1 for v in s[\"oracle_per_test\"].values() if not v)\n        n_pass = sum(1 for v in s[\"oracle_per_test\"].values() if v)\n        log.info(f\"  [{i}] {s['instance_id']} ({s['mutation_type']}) \"\n                 f\"oracle: {n_fail} fail, {n_pass} pass\")\n\n    return selected\n\n\ndef generate_repairs(dataset, model_path, conditions, n_samples=5, output_dir=\".\"):\n    \"\"\"Generate repairs using vLLM.\"\"\"\n    from vllm import LLM, SamplingParams\n\n    log.info(f\"Loading model: {model_path}\")\n    llm = LLM(\n        model=model_path,\n        tensor_parallel_size=1,\n        max_model_len=8192,\n        trust_remote_code=True,\n        dtype=\"bfloat16\",\n        gpu_memory_utilization=0.85,\n    )\n    tokenizer = llm.get_tokenizer()\n\n    sampling_params = SamplingParams(\n        temperature=0.6,\n        top_p=0.95,\n        max_tokens=2048,\n        n=n_samples,\n    )\n\n    rng = np.random.default_rng(42)\n    all_results = []\n\n    for cond in conditions:\n        log.info(f\"=== Condition: {cond} ===\")\n        prompts = []\n        meta = []\n\n        for item in dataset:\n            messages = build_prompt(item, cond, rng)\n            prompt_text = tokenizer.apply_chat_template(\n                messages, tokenize=False, add_generation_prompt=True\n            )\n            prompts.append(prompt_text)\n            meta.append({\n                \"instance_id\": item[\"instance_id\"],\n                \"condition\": cond,\n                \"mutation_type\": item[\"mutation_type\"],\n                \"gold_patch\": item[\"gold_patch\"],\n            })\n\n        log.info(f\"Generating {len(prompts)} prompts × {n_samples} samples...\")\n        outputs = llm.generate(prompts, sampling_params)\n\n        for output, m in zip(outputs, meta):\n            for k, completion in enumerate(output.outputs):\n                diff = extract_diff(completion.text)\n                sim = diff_similarity(diff, m[\"gold_patch\"])\n                all_results.append({\n                    \"instance_id\": m[\"instance_id\"],\n                    \"condition\": m[\"condition\"],\n                    \"mutation_type\": m[\"mutation_type\"],\n                    \"sample_k\": k,\n                    \"extracted_diff\": diff,\n                    \"gold_similarity\": sim,\n                    \"diff_nonempty\": len(diff) > 20,\n                    \"has_diff_header\": diff.startswith(\"diff \") or diff.startswith(\"---\"),\n                })\n\n        cond_sims = [r[\"gold_similarity\"] for r in all_results if r[\"condition\"] == cond]\n        log.info(f\"  Mean gold similarity: {np.mean(cond_sims):.3f} \"\n                 f\"(max={np.max(cond_sims):.3f}, nonempty={sum(1 for r in all_results if r['condition']==cond and r['diff_nonempty'])}/{len(cond_sims)})\")\n\n    out_path = os.path.join(output_dir, \"phase0_repairs.jsonl\")\n    save_jsonl(all_results, out_path)\n    return all_results\n\n\ndef analyze_results(results, output_dir=\".\"):\n    \"\"\"Analyze Phase 0 results.\"\"\"\n    log.info(\"=== Phase 0 Analysis ===\")\n\n    by_cond = defaultdict(list)\n    for r in results:\n        by_cond[r[\"condition\"]].append(r)\n\n    summary = {}\n    for cond in CONDITIONS:\n        if cond not in by_cond:\n            continue\n        entries = by_cond[cond]\n        sims = [e[\"gold_similarity\"] for e in entries]\n        nonempty = sum(1 for e in entries if e[\"diff_nonempty\"])\n        has_header = sum(1 for e in entries if e[\"has_diff_header\"])\n\n        # Best-of-K similarity per instance\n        by_inst = defaultdict(list)\n        for e in entries:\n            by_inst[e[\"instance_id\"]].append(e[\"gold_similarity\"])\n        best_per_inst = [max(sims_list) for sims_list in by_inst.values()]\n\n        summary[cond] = {\n            \"n_samples\": len(entries),\n            \"mean_similarity\": float(np.mean(sims)),\n            \"max_similarity\": float(np.max(sims)),\n            \"best_of_k_mean\": float(np.mean(best_per_inst)),\n            \"best_of_k_max\": float(np.max(best_per_inst)),\n            \"pct_nonempty\": nonempty / len(entries) * 100,\n            \"pct_valid_diff\": has_header / len(entries) * 100,\n        }\n\n        log.info(f\"\\n  {cond}:\")\n        log.info(f\"    Mean sim: {summary[cond]['mean_similarity']:.3f}\")\n        log.info(f\"    Best-of-K mean: {summary[cond]['best_of_k_mean']:.3f}\")\n        log.info(f\"    Best-of-K max: {summary[cond]['best_of_k_max']:.3f}\")\n        log.info(f\"    Valid diff: {summary[cond]['pct_valid_diff']:.0f}%\")\n\n    # Deltas\n    if \"control\" in summary and \"oracle-diag\" in summary:\n        delta_oracle = summary[\"oracle-diag\"][\"best_of_k_mean\"] - summary[\"control\"][\"best_of_k_mean\"]\n        log.info(f\"\\n  Δ(oracle-diag - control) best-of-K: {delta_oracle:+.3f}\")\n    if \"control\" in summary and \"cls-diag\" in summary:\n        delta_cls = summary[\"cls-diag\"][\"best_of_k_mean\"] - summary[\"control\"][\"best_of_k_mean\"]\n        log.info(f\"  Δ(cls-diag - control) best-of-K: {delta_cls:+.3f}\")\n    if \"control\" in summary and \"random-diag\" in summary:\n        delta_rand = summary[\"random-diag\"][\"best_of_k_mean\"] - summary[\"control\"][\"best_of_k_mean\"]\n        log.info(f\"  Δ(random-diag - control) best-of-K: {delta_rand:+.3f}\")\n\n    out_path = os.path.join(output_dir, \"phase0_summary.json\")\n    os.makedirs(output_dir, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(f\"\\nSaved summary to {out_path}\")\n\n    return summary\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Re-Repair Phase 0\")\n    parser.add_argument(\"--data-dir\", required=True,\n                        help=\"Path to data/swebench_full/\")\n    parser.add_argument(\"--model\", default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\",\n                        help=\"Model path\")\n    parser.add_argument(\"--n-instances\", type=int, default=10)\n    parser.add_argument(\"--n-samples\", type=int, default=5,\n                        help=\"Completions per (instance, condition)\")\n    parser.add_argument(\"--conditions\", nargs=\"+\", default=CONDITIONS)\n    parser.add_argument(\"--output-dir\", default=\"/root/autodl-tmp/eval_results/re_repair_phase0\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--analyze-only\", type=str, default=None,\n                        help=\"Path to existing phase0_repairs.jsonl to analyze\")\n    args = parser.parse_args()\n\n    if args.analyze_only:\n        results = load_jsonl(args.analyze_only)\n        analyze_results(results, args.output_dir)\n        return\n\n    # Step 1: Prepare data\n    dataset = prepare_phase0_data(args.data_dir, args.n_instances, args.seed)\n\n    # Save prepared dataset\n    prep_path = os.path.join(args.output_dir, \"phase0_dataset.jsonl\")\n    save_jsonl(dataset, prep_path)\n\n    # Step 2: Generate repairs\n    results = generate_repairs(\n        dataset, args.model, args.conditions, args.n_samples, args.output_dir\n    )\n\n    # Step 3: Analyze\n    analyze_results(results, args.output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 380,
      "startLine": 1,
      "totalLines": 380
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01RFGpRJU8cbv8iHrENBEWvN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/re_repair_eval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "86ee7506-3b19-41fb-a1c3-6a0605938285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJ7mtmWUN2DQ7ShKp715h6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13799,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13799
      },
      "output_tokens": 37,
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

_source line 8 · 2026-05-17T04:00:37.514Z_

<details><summary>↩ Tool result · `toolu_01RFGpRJU8cbv8iHrENBEWvN`</summary>

````text
1	#!/usr/bin/env python3
2	"""
3	Re-Repair Downstream Experiment: evaluate whether CLS per-test diagnostic
4	information improves LLM patch repair success rate.
5	
6	Conditions:
7	  control     — "patch is incorrect, please fix" (no per-test info)
8	  cls-diag    — control + CLS-predicted per-test pass/fail
9	  oracle-diag — control + ground-truth per-test pass/fail
10	  random-diag — control + randomly assigned per-test pass/fail
11	
12	Usage:
13	  # Phase 1: prepare data (collect incorrect patches + CLS predictions)
14	  python re_repair_eval.py prepare \
15	      --swebench-predictions predictions_dir/ \
16	      --cls-checkpoint checkpoints/cls8b-s42-ckpt3600 \
17	      --output-dir artifacts/re_repair
18	
19	  # Phase 2: generate repairs
20	  python re_repair_eval.py generate \
21	      --data artifacts/re_repair/repair_dataset.jsonl \
22	      --model Qwen/Qwen3-8B-Instruct \
23	      --conditions control cls-diag oracle-diag random-diag \
24	      --output-dir artifacts/re_repair
25	
26	  # Phase 3: verify repairs via Docker execution
27	  python re_repair_eval.py verify \
28	      --repairs artifacts/re_repair/generated_repairs.jsonl \
29	      --output-dir artifacts/re_repair
30	
31	  # Phase 4: analyze results
32	  python re_repair_eval.py analyze \
33	      --results artifacts/re_repair/verification_results.jsonl \
34	      --output-dir artifacts/re_repair
35	"""
36	
37	import argparse
38	import json
39	import logging
40	import os
41	import re
42	from collections import defaultdict
43	from pathlib import Path
44	
45	import numpy as np
46	
47	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
48	log = logging.getLogger(__name__)
49	
50	# ---------------------------------------------------------------------------
51	# Constants
52	# ---------------------------------------------------------------------------
53	
54	MIN_F2P_TESTS = 2
55	
56	CONDITIONS = ["control", "cls-diag", "oracle-diag", "random-diag"]
57	
58	SYSTEM_PROMPT_REPAIR = (
59	    "You are a software engineer. You are given a code patch that was intended "
60	    "to fix an issue but does not fully work. Your task is to produce a corrected "
61	    "patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
62	)
63	
64	DIAGNOSTIC_TEMPLATE = (
65	    "## Test Diagnostic\n"
66	    "The current patch **fails** the following tests:\n{fail_list}\n\n"
67	    "The current patch **passes** the following tests:\n{pass_list}"
68	)
69	
70	# ---------------------------------------------------------------------------
71	# Data loading utilities
72	# ---------------------------------------------------------------------------
73	
74	
75	def load_jsonl(path):
76	    with open(path) as f:
77	        return [json.loads(line) for line in f]
78	
79	
80	def save_jsonl(data, path):
81	    os.makedirs(os.path.dirname(path), exist_ok=True)
82	    with open(path, "w") as f:
83	        for item in data:
84	            f.write(json.dumps(item, ensure_ascii=False) + "\n")
85	    log.info(f"Saved {len(data)} records to {path}")
86	
87	
88	def load_swebench_verified():
89	    """Load SWE-bench Verified and filter to T_f2p >= MIN_F2P_TESTS."""
90	    from datasets import load_dataset
91	
92	    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
93	    filtered = []
94	    for row in ds:
95	        f2p = json.loads(row["FAIL_TO_PASS"])
96	        if len(f2p) >= MIN_F2P_TESTS:
97	            filtered.append({
98	                "instance_id": row["instance_id"],
99	                "repo": row["repo"],
100	                "base_commit": row["base_commit"],
101	                "gold_patch": row["patch"],
102	                "test_patch": row["test_patch"],
103	                "fail_to_pass": f2p,
104	                "pass_to_pass": json.loads(row["PASS_TO_PASS"]),
105	                "problem_statement": row.get("problem_statement", row.get("hints_text", "")),
106	                "version": row["version"],
107	            })
108	    log.info(f"SWE-bench Verified: {len(ds)} total, {len(filtered)} with T_f2p >= {MIN_F2P_TESTS}")
109	    return filtered
110	
111	
112	# ---------------------------------------------------------------------------
113	# Phase 1: Prepare — collect incorrect patches + run CLS predictions
114	# ---------------------------------------------------------------------------
115	
116	
117	def collect_incorrect_patches(instances, predictions_dir):
118	    """Collect incorrect patches from public SWE-bench agent predictions.
119	
120	    Reads prediction JSONL files from predictions_dir/, matches to T>=2
121	    instances, and filters to patches that are incorrect (not all F2P pass).
122	
123	    Returns list of {instance_id, patch, source, ...}.
124	    """
125	    instance_ids = {inst["instance_id"] for inst in instances}
126	    patches = []
127	
128	    pred_dir = Path(predictions_dir)
129	    for pred_file in pred_dir.glob("*.jsonl"):
130	        source_name = pred_file.stem
131	        for line in pred_file.open():
132	            rec = json.loads(line)
133	            iid = rec.get("instance_id")
134	            if iid not in instance_ids:
135	                continue
136	            model_patch = rec.get("model_patch", rec.get("patch", ""))
137	            if not model_patch or not model_patch.strip():
138	                continue
139	            patches.append({
140	                "instance_id": iid,
141	                "patch": model_patch,
142	                "source": source_name,
143	            })
144	
145	    log.info(f"Collected {len(patches)} candidate incorrect patches from {predictions_dir}")
146	    return patches
147	
148	
149	def run_cls_predictions(patches_with_tests, cls_checkpoint, model_name="Qwen/Qwen3-8B"):
150	    """Run CLS model to predict per-test pass/fail for each (patch, test).
151	
152	    Args:
153	        patches_with_tests: list of {instance_id, patch, test_name, test_code, ...}
154	        cls_checkpoint: path to LoRA checkpoint
155	        model_name: base model name
156	
157	    Returns:
158	        list of {instance_id, patch_id, test_name, cls_pred (0/1), cls_prob}
159	    """
160	    import torch
161	    from peft import PeftModel
162	    from transformers import AutoModelForCausalLM, AutoTokenizer
163	
164	    log.info(f"Loading CLS model: {model_name} + {cls_checkpoint}")
165	    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
166	    base_model = AutoModelForCausalLM.from_pretrained(
167	        model_name, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True,
168	    )
169	    model = PeftModel.from_pretrained(base_model, cls_checkpoint)
170	    model.eval()
171	
172	    results = []
173	    for i, item in enumerate(patches_with_tests):
174	        messages = [
175	            {"role": "system", "content": "You are a code verifier. Given a code patch and a test case, predict whether the test will pass or fail."},
176	            {"role": "user", "content": f"## Code\n{item['patch']}\n\n## Test\n{item['test_code']}\n\nWill this test pass or fail?"},
177	        ]
178	        input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
179	        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
180	
181	        with torch.no_grad():
182	            outputs = model.generate(**inputs, max_new_tokens=8, do_sample=False)
183	
184	        generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
185	        pred = parse_cls_output(generated)
186	
187	        results.append({
188	            "instance_id": item["instance_id"],
189	            "patch_id": item.get("patch_id", i),
190	            "test_name": item["test_name"],
191	            "cls_pred": pred,
192	            "cls_raw": generated.strip(),
193	        })
194	
195	        if (i + 1) % 100 == 0:
196	            log.info(f"CLS inference: {i+1}/{len(patches_with_tests)}")
197	
198	    return results
199	
200	
201	def parse_cls_output(text):
202	    """Parse CLS model output to binary 0 (fail) / 1 (pass)."""
203	    if "&lt;/think>" in text:
204	        text = text.split("&lt;/think>")[-1]
205	    text = text.strip().lower()
206	    if "pass" in text and "fail" not in text:
207	        return 1
208	    if "fail" in text:
209	        return 0
210	    return -1  # unparseable
211	
212	
213	def run_ground_truth_verification(instance, patch):
214	    """Run Docker execution to get ground-truth per-test results.
215	
216	    Uses SWE-bench harness. Returns dict {test_name: bool(passed)}.
217	    """
218	    # TODO: implement using swebench.harness
219	    # from swebench.harness.run_evaluation import run_instances
220	    # from swebench.harness.test_spec import make_test_spec
221	    raise NotImplementedError("Requires SWE-bench Docker harness setup")
222	
223	
224	def cmd_prepare(args):
225	    log.info("=== Phase 1: Prepare repair dataset ===")
226	
227	    instances = load_swebench_verified()
228	    patches = collect_incorrect_patches(instances, args.swebench_predictions)
229	
230	    # TODO: for each (instance, patch), run ground-truth Docker verification
231	    # to confirm patch is actually incorrect and get per-test results.
232	    # Then run CLS model for per-test predictions.
233	    # Finally, assemble repair_dataset.jsonl.
234	
235	    instance_map = {inst["instance_id"]: inst for inst in instances}
236	
237	    dataset = []
238	    for p in patches:
239	        inst = instance_map.get(p["instance_id"])
240	        if inst is None:
241	            continue
242	        dataset.append({
243	            "instance_id": p["instance_id"],
244	            "repo": inst["repo"],
245	            "patch": p["patch"],
246	            "patch_source": p["source"],
247	            "gold_patch": inst["gold_patch"],
248	            "problem_statement": inst["problem_statement"],
249	            "fail_to_pass": inst["fail_to_pass"],
250	            "pass_to_pass": inst["pass_to_pass"],
251	            "gt_per_test": {},      # placeholder: ground-truth per-test results
252	            "cls_per_test": {},     # placeholder: CLS predictions
253	        })
254	
255	    out_path = os.path.join(args.output_dir, "repair_dataset.jsonl")
256	    save_jsonl(dataset, out_path)
257	    log.info(f"Prepared {len(dataset)} repair instances")
258	
259	
260	# ---------------------------------------------------------------------------
261	# Phase 2: Generate — produce repair patches under each condition
262	# ---------------------------------------------------------------------------
263	
264	
265	def build_repair_prompt(item, condition, rng=None):
266	    """Build the repair prompt for a given condition.
267	
268	    Returns list of chat messages [{role, content}].
269	    """
270	    base_content = (
271	        f"## Issue Description\n{item['problem_statement']}\n\n"
272	        f"## Current (Incorrect) Patch\n```diff\n{item['patch']}\n```\n"
273	    )
274	
275	    if condition == "control":
276	        diagnostic = ""
277	    elif condition == "cls-diag":
278	        per_test = item.get("cls_per_test", {})
279	        diagnostic = _format_diagnostic(per_test)
280	    elif condition == "oracle-diag":
281	        per_test = item.get("gt_per_test", {})
282	        diagnostic = _format_diagnostic(per_test)
283	    elif condition == "random-diag":
284	        all_tests = item.get("fail_to_pass", []) + item.get("pass_to_pass", [])
285	        if rng is None:
286	            rng = np.random.default_rng(42)
287	        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
288	        diagnostic = _format_diagnostic(per_test)
289	    else:
290	        raise ValueError(f"Unknown condition: {condition}")
291	
292	    user_content = base_content
293	    if diagnostic:
294	        user_content += f"\n{diagnostic}\n"
295	    user_content += (
296	        "\nPlease produce a corrected patch in unified diff format that "
297	        "resolves the issue.\nOutput ONLY the diff, enclosed in ```diff ... ``` tags."
298	    )
299	
300	    return [
301	        {"role": "system", "content": SYSTEM_PROMPT_REPAIR},
302	        {"role": "user", "content": user_content},
303	    ]
304	
305	
306	def _format_diagnostic(per_test):
307	    """Format per-test results into diagnostic prompt section."""
308	    if not per_test:
309	        return ""
310	    fails = [t for t, passed in per_test.items() if not passed]
311	    passes = [t for t, passed in per_test.items() if passed]
312	    if not fails:
313	        return ""
314	    fail_list = "\n".join(f"- `{t}`" for t in fails)
315	    pass_list = "\n".join(f"- `{t}`" for t in passes) if passes else "*(none)*"
316	    return DIAGNOSTIC_TEMPLATE.format(fail_list=fail_list, pass_list=pass_list)
317	
318	
319	def extract_diff_from_response(text):
320	    """Extract unified diff from LLM response."""
321	    pattern = r"```diff\s*\n(.*?)```"
322	    match = re.search(pattern, text, re.DOTALL)
323	    if match:
324	        return match.group(1).strip()
325	    pattern_generic = r"```\s*\n(diff.*?)```"
326	    match = re.search(pattern_generic, text, re.DOTALL)
327	    if match:
328	        return match.group(1).strip()
329	    return text.strip()
330	
331	
332	def generate_repairs_vllm(dataset, conditions, model_name, n_samples, output_dir):
333	    """Generate repair patches using vLLM for all conditions.
334	
335	    Args:
336	        dataset: list of repair instances from Phase 1
337	        conditions: list of condition names
338	        model_name: HF model name for repair LLM
339	        n_samples: number of completions per (instance, condition)
340	        output_dir: where to save results
341	    """
342	    from vllm import LLM, SamplingParams
343	
344	    log.info(f"Loading repair LLM: {model_name}")
345	    llm = LLM(
346	        model=model_name,
347	        tensor_parallel_size=1,  # adjust based on GPU count
348	        max_model_len=8192,
349	        trust_remote_code=True,
350	        dtype="bfloat16",
351	    )
352	    sampling_params = SamplingParams(
353	        temperature=0.6, top_p=0.95, max_tokens=2048, n=n_samples,
354	    )
355	
356	    all_repairs = []
357	    rng = np.random.default_rng(42)
358	
359	    for cond in conditions:
360	        log.info(f"Generating repairs for condition: {cond}")
361	        prompts = []
362	        meta = []
363	
364	        for item in dataset:
365	            messages = build_repair_prompt(item, cond, rng=rng)
366	            # vLLM chat: convert messages to single string
367	            # TODO: use tokenizer.apply_chat_template if needed
368	            prompt_text = "\n".join(
369	                f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>" for m in messages
370	            ) + "\n<|im_start|>assistant\n"
371	            prompts.append(prompt_text)
372	            meta.append({
373	                "instance_id": item["instance_id"],
374	                "condition": cond,
375	                "patch_source": item.get("patch_source", "unknown"),
376	            })
377	
378	        outputs = llm.generate(prompts, sampling_params)
379	
380	        for output, m in zip(outputs, meta):
381	            for k, completion in enumerate(output.outputs):
382	                diff = extract_diff_from_response(completion.text)
383	                all_repairs.append({
384	                    **m,
385	                    "sample_k": k,
386	                    "raw_response": completion.text,
387	                    "extracted_diff": diff,
388	                    "diff_valid": diff.startswith("diff ") or diff.startswith("---"),
389	                })
390	
391	    out_path = os.path.join(output_dir, "generated_repairs.jsonl")
392	    save_jsonl(all_repairs, out_path)
393	    log.info(f"Generated {len(all_repairs)} total repairs")
394	    return all_repairs
395	
396	
397	def cmd_generate(args):
398	    log.info("=== Phase 2: Generate repairs ===")
399	    dataset = load_jsonl(args.data)
400	    conditions = args.conditions or CONDITIONS
401	    generate_repairs_vllm(
402	        dataset, conditions, args.model, args.n_samples, args.output_dir,
403	    )
404	
405	
406	# ---------------------------------------------------------------------------
407	# Phase 3: Verify — Docker execution of generated repair patches
408	# ---------------------------------------------------------------------------
409	
410	
411	def cmd_verify(args):
412	    log.info("=== Phase 3: Verify repairs via Docker ===")
413	    repairs = load_jsonl(args.repairs)
414	
415	    # Dedup: many samples produce identical diffs
416	    seen = set()
417	    unique_repairs = []
418	    for r in repairs:
419	        key = (r["instance_id"], r["extracted_diff"])
420	        if key in seen:
421	            r["dedup_ref"] = True
422	            continue
423	        seen.add(key)
424	        unique_repairs.append(r)
425	
426	    log.info(f"Total repairs: {len(repairs)}, unique: {len(unique_repairs)}")
427	
428	    # TODO: run SWE-bench Docker harness on each unique repair
429	    # For each repair:
430	    #   1. Apply extracted_diff to repo at base_commit
431	    #   2. Run test suite
432	    #   3. Record per-test pass/fail
433	    #   4. Mark resolved = all F2P pass & no P2P regressions
434	
435	    results = []
436	    for r in unique_repairs:
437	        results.append({
438	            **r,
439	            "resolved": None,       # placeholder
440	            "f2p_passed": None,      # placeholder: list of passed F2P tests
441	            "f2p_failed": None,      # placeholder: list of failed F2P tests
442	            "p2p_regressed": None,   # placeholder: list of regressed P2P tests
443	            "error": None,
444	        })
445	
446	    out_path = os.path.join(args.output_dir, "verification_results.jsonl")
447	    save_jsonl(results, out_path)
448	
449	
450	# ---------------------------------------------------------------------------
451	# Phase 4: Analyze — compute metrics and statistical tests
452	# ---------------------------------------------------------------------------
453	
454	
455	def compute_resolve_rates(results):
456	    """Compute resolve rate per condition.
457	
458	    Returns dict {condition: {pass_at_1, pass_at_5, n_instances, n_patches}}.
459	    """
460	    by_condition = defaultdict(lambda: defaultdict(list))
461	
462	    for r in results:
463	        cond = r["condition"]
464	        iid = r["instance_id"]
465	        resolved = r.get("resolved", False)
466	        by_condition[cond][iid].append(resolved)
467	
468	    metrics = {}
469	    for cond, instances in by_condition.items():
470	        n_inst = len(instances)
471	        pass_at_1_sum = 0
472	        pass_at_5_sum = 0
473	
474	        for iid, resolutions in instances.items():
475	            k = len(resolutions)
476	            n_pass = sum(resolutions)
477	            # pass@1: unbiased estimator
478	            pass_at_1_sum += 1 - (comb_ratio(k - n_pass, 1, k, 1) if k >= 1 else 1.0)
479	            # pass@5
480	            pass_at_5_sum += 1 - (comb_ratio(k - n_pass, 5, k, 5) if k >= 5 else (0.0 if n_pass > 0 else 1.0))
481	
482	        metrics[cond] = {
483	            "pass_at_1": pass_at_1_sum / n_inst if n_inst else 0,
484	            "pass_at_5": pass_at_5_sum / n_inst if n_inst else 0,
485	            "n_instances": n_inst,
486	            "n_total_repairs": sum(len(v) for v in instances.values()),
487	        }
488	
489	    return metrics
490	
491	
492	def comb_ratio(a, b, c, d):
493	    """Compute C(a,b) / C(c,d) safely."""
494	    from math import comb
495	    denom = comb(c, d)
496	    if denom == 0:
497	        return 0.0
498	    return comb(a, b) / denom
499	
500	
501	def mcnemar_test(results, cond_a="control", cond_b="cls-diag"):
502	    """McNemar's test comparing two conditions on paired instances.
503	
504	    Returns (chi2, p_value, contingency_table).
505	    """
506	    from scipy.stats import chi2 as chi2_dist
507	
508	    paired = defaultdict(lambda: {})
509	    for r in results:
510	        cond = r["condition"]
511	        iid = r["instance_id"]
512	        if cond in (cond_a, cond_b):
513	            # Use best-of-K (any resolved)
514	            if iid not in paired or cond not in paired[iid]:
515	                paired[iid][cond] = False
516	            if r.get("resolved", False):
517	                paired[iid][cond] = True
518	
519	    a_only = 0  # cond_a resolves, cond_b doesn't
520	    b_only = 0  # cond_b resolves, cond_a doesn't
521	    both = 0
522	    neither = 0
523	
524	    for iid, conds in paired.items():
525	        ra = conds.get(cond_a, False)
526	        rb = conds.get(cond_b, False)
527	        if ra and rb:
528	            both += 1
529	        elif ra and not rb:
530	            a_only += 1
531	        elif not ra and rb:
532	            b_only += 1
533	        else:
534	            neither += 1
535	
536	    n_discord = a_only + b_only
537	    if n_discord == 0:
538	        return 0.0, 1.0, {"both": both, "neither": neither, "a_only": a_only, "b_only": b_only}
539	
540	    chi2 = (abs(a_only - b_only) - 1) ** 2 / n_discord
541	    p_value = 1 - chi2_dist.cdf(chi2, df=1)
542	
543	    return chi2, p_value, {"both": both, "neither": neither, "a_only": a_only, "b_only": b_only}
544	
545	
546	def clustered_bootstrap_ci(results, cond_a, cond_b, n_resamples=10000, seed=42):
547	    """Clustered bootstrap CI for Δ resolve rate (cond_b - cond_a).
548	
549	    Clusters by instance_id. Returns (mean_delta, ci_lower, ci_upper).
550	    """
551	    rng = np.random.default_rng(seed)
552	
553	    instance_resolve = defaultdict(lambda: defaultdict(bool))
554	    for r in results:
555	        if r.get("resolved", False):
556	            instance_resolve[r["instance_id"]][r["condition"]] = True
557	
558	    instance_ids = list(instance_resolve.keys())
559	    n = len(instance_ids)
560	    if n == 0:
561	        return 0.0, 0.0, 0.0
562	
563	    deltas = np.zeros(n_resamples)
564	    for b in range(n_resamples):
565	        idx = rng.choice(n, size=n, replace=True)
566	        ra = np.mean([instance_resolve[instance_ids[i]].get(cond_a, False) for i in idx])
567	        rb = np.mean([instance_resolve[instance_ids[i]].get(cond_b, False) for i in idx])
568	        deltas[b] = rb - ra
569	
570	    return float(np.mean(deltas)), float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))
571	
572	
573	def stratify_by_cls_accuracy(results, cls_predictions):
574	    """Split results by CLS accuracy per instance.
575	
576	    Returns {accuracy_bin: [results]}.
577	    """
578	    instance_cls_acc = defaultdict(list)
579	    for p in cls_predictions:
580	        correct = (p["cls_pred"] == p.get("gt_label"))
581	        instance_cls_acc[p["instance_id"]].append(correct)
582	
583	    instance_acc = {
584	        iid: np.mean(corrects) for iid, corrects in instance_cls_acc.items()
585	    }
586	
587	    bins = {"high_acc_ge90": [], "low_acc_lt90": []}
588	    for r in results:
589	        acc = instance_acc.get(r["instance_id"], 0.5)
590	        if acc >= 0.9:
591	            bins["high_acc_ge90"].append(r)
592	        else:
593	            bins["low_acc_lt90"].append(r)
594	
595	    return bins
596	
597	
598	def cmd_analyze(args):
599	    log.info("=== Phase 4: Analyze results ===")
600	    results = load_jsonl(args.results)
601	
602	    # Resolve rates
603	    rates = compute_resolve_rates(results)
604	    log.info("Resolve rates by condition:")
605	    for cond, m in rates.items():
606	        log.info(f"  {cond}: pass@1={m['pass_at_1']:.3f}, pass@5={m['pass_at_5']:.3f} (n={m['n_instances']})")
607	
608	    # McNemar: control vs cls-diag
609	    chi2, p, table = mcnemar_test(results, "control", "cls-diag")
610	    log.info(f"McNemar control vs cls-diag: chi2={chi2:.3f}, p={p:.4f}, table={table}")
611	
612	    # McNemar: control vs oracle-diag
613	    chi2_o, p_o, table_o = mcnemar_test(results, "control", "oracle-diag")
614	    log.info(f"McNemar control vs oracle-diag: chi2={chi2_o:.3f}, p={p_o:.4f}, table={table_o}")
615	
616	    # Bootstrap CI
617	    delta_mean, ci_lo, ci_hi = clustered_bootstrap_ci(results, "control", "cls-diag")
618	    log.info(f"Bootstrap Δ(cls-diag − control): {delta_mean:.3f} [{ci_lo:.3f}, {ci_hi:.3f}]")
619	
620	    delta_o_mean, ci_o_lo, ci_o_hi = clustered_bootstrap_ci(results, "control", "oracle-diag")
621	    log.info(f"Bootstrap Δ(oracle − control): {delta_o_mean:.3f} [{ci_o_lo:.3f}, {ci_o_hi:.3f}]")
622	
623	    # Summary
624	    summary = {
625	        "resolve_rates": rates,
626	        "mcnemar_control_vs_cls": {"chi2": chi2, "p_value": p, "table": table},
627	        "mcnemar_control_vs_oracle": {"chi2": chi2_o, "p_value": p_o, "table": table_o},
628	        "bootstrap_cls_minus_control": {"mean": delta_mean, "ci_95": [ci_lo, ci_hi]},
629	        "bootstrap_oracle_minus_control": {"mean": delta_o_mean, "ci_95": [ci_o_lo, ci_o_hi]},
630	    }
631	
632	    out_path = os.path.join(args.output_dir, "metrics_summary.json")
633	    os.makedirs(args.output_dir, exist_ok=True)
634	    with open(out_path, "w") as f:
635	        json.dump(summary, f, indent=2)
636	    log.info(f"Saved metrics summary to {out_path}")
637	
638	    # Generate figure
639	    generate_resolve_rate_figure(rates, args.output_dir)
640	
641	
642	def generate_resolve_rate_figure(rates, output_dir):
643	    """Bar chart: resolve rate by condition."""
644	    try:
645	        import matplotlib
646	        matplotlib.use("Agg")
647	        import matplotlib.pyplot as plt
648	    except ImportError:
649	        log.warning("matplotlib not available, skipping figure generation")
650	        return
651	
652	    conds = ["control", "cls-diag", "oracle-diag", "random-diag"]
653	    conds = [c for c in conds if c in rates]
654	    pass1 = [rates[c]["pass_at_1"] * 100 for c in conds]
655	    pass5 = [rates[c]["pass_at_5"] * 100 for c in conds]
656	
657	    x = np.arange(len(conds))
658	    width = 0.35
659	
660	    fig, ax = plt.subplots(figsize=(8, 5))
661	    bars1 = ax.bar(x - width / 2, pass1, width, label="pass@1", color="#4C72B0")
662	    bars2 = ax.bar(x + width / 2, pass5, width, label="pass@5", color="#55A868")
663	
664	    ax.set_ylabel("Resolve Rate (%)")
665	    ax.set_xlabel("Condition")
666	    ax.set_title("Re-Repair Resolve Rate by Diagnostic Condition")
667	    ax.set_xticks(x)
668	    ax.set_xticklabels(conds, rotation=15)
669	    ax.legend()
670	    ax.set_ylim(0, max(pass5 + pass1 + [10]) * 1.2)
671	
672	    for bars in [bars1, bars2]:
673	        for bar in bars:
674	            h = bar.get_height()
675	            ax.annotate(f"{h:.1f}", xy=(bar.get_x() + bar.get_width() / 2, h),
676	                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
677	
678	    fig.tight_layout()
679	    out_path = os.path.join(output_dir, "fig_resolve_rate.pdf")
680	    fig.savefig(out_path, dpi=150, bbox_inches="tight")
681	    plt.close(fig)
682	    log.info(f"Saved figure to {out_path}")
683	
684	
685	# ---------------------------------------------------------------------------
686	# CLI
687	# ---------------------------------------------------------------------------
688	
689	
690	def main():
691	    parser = argparse.ArgumentParser(description="Re-Repair Downstream Experiment")
692	    sub = parser.add_subparsers(dest="command", required=True)
693	
694	    # prepare
695	    p_prep = sub.add_parser("prepare", help="Phase 1: prepare repair dataset")
696	    p_prep.add_argument("--swebench-predictions", required=True, help="Dir with agent prediction .jsonl files")
697	    p_prep.add_argument("--cls-checkpoint", required=True, help="Path to CLS LoRA checkpoint")
698	    p_prep.add_argument("--cls-base-model", default="Qwen/Qwen3-8B", help="CLS base model name")
699	    p_prep.add_argument("--output-dir", default="artifacts/re_repair")
700	
701	    # generate
702	    p_gen = sub.add_parser("generate", help="Phase 2: generate repair patches")
703	    p_gen.add_argument("--data", required=True, help="repair_dataset.jsonl from Phase 1")
704	    p_gen.add_argument("--model", default="Qwen/Qwen3-8B-Instruct", help="Repair LLM")
705	    p_gen.add_argument("--conditions", nargs="+", default=CONDITIONS)
706	    p_gen.add_argument("--n-samples", type=int, default=10, help="Completions per (instance, condition)")
707	    p_gen.add_argument("--output-dir", default="artifacts/re_repair")
708	
709	    # verify
710	    p_ver = sub.add_parser("verify", help="Phase 3: verify repairs via Docker")
711	    p_ver.add_argument("--repairs", required=True, help="generated_repairs.jsonl from Phase 2")
712	    p_ver.add_argument("--max-workers", type=int, default=4, help="Parallel Docker containers")
713	    p_ver.add_argument("--timeout", type=int, default=300, help="Per-instance timeout (seconds)")
714	    p_ver.add_argument("--output-dir", default="artifacts/re_repair")
715	
716	    # analyze
717	    p_ana = sub.add_parser("analyze", help="Phase 4: analyze results")
718	    p_ana.add_argument("--results", required=True, help="verification_results.jsonl from Phase 3")
719	    p_ana.add_argument("--cls-predictions", default=None, help="CLS predictions for stratification")
720	    p_ana.add_argument("--output-dir", default="artifacts/re_repair")
721	
722	    args = parser.parse_args()
723	
724	    if args.command == "prepare":
725	        cmd_prepare(args)
726	    elif args.command == "generate":
727	        cmd_generate(args)
728	    elif args.command == "verify":
729	        cmd_verify(args)
730	    elif args.command == "analyze":
731	        cmd_analyze(args)
732	
733	
734	if __name__ == "__main__":
735	    main()
736	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "e1f3ed3e-d787-4927-a061-2332c5653648",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/re_repair_eval.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nRe-Repair Downstream Experiment: evaluate whether CLS per-test diagnostic\ninformation improves LLM patch repair success rate.\n\nConditions:\n  control     — \"patch is incorrect, please fix\" (no per-test info)\n  cls-diag    — control + CLS-predicted per-test pass/fail\n  oracle-diag — control + ground-truth per-test pass/fail\n  random-diag — control + randomly assigned per-test pass/fail\n\nUsage:\n  # Phase 1: prepare data (collect incorrect patches + CLS predictions)\n  python re_repair_eval.py prepare \\\n      --swebench-predictions predictions_dir/ \\\n      --cls-checkpoint checkpoints/cls8b-s42-ckpt3600 \\\n      --output-dir artifacts/re_repair\n\n  # Phase 2: generate repairs\n  python re_repair_eval.py generate \\\n      --data artifacts/re_repair/repair_dataset.jsonl \\\n      --model Qwen/Qwen3-8B-Instruct \\\n      --conditions control cls-diag oracle-diag random-diag \\\n      --output-dir artifacts/re_repair\n\n  # Phase 3: verify repairs via Docker execution\n  python re_repair_eval.py verify \\\n      --repairs artifacts/re_repair/generated_repairs.jsonl \\\n      --output-dir artifacts/re_repair\n\n  # Phase 4: analyze results\n  python re_repair_eval.py analyze \\\n      --results artifacts/re_repair/verification_results.jsonl \\\n      --output-dir artifacts/re_repair\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\n\nMIN_F2P_TESTS = 2\n\nCONDITIONS = [\"control\", \"cls-diag\", \"oracle-diag\", \"random-diag\"]\n\nSYSTEM_PROMPT_REPAIR = (\n    \"You are a software engineer. You are given a code patch that was intended \"\n    \"to fix an issue but does not fully work. Your task is to produce a corrected \"\n    \"patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags.\"\n)\n\nDIAGNOSTIC_TEMPLATE = (\n    \"## Test Diagnostic\\n\"\n    \"The current patch **fails** the following tests:\\n{fail_list}\\n\\n\"\n    \"The current patch **passes** the following tests:\\n{pass_list}\"\n)\n\n# ---------------------------------------------------------------------------\n# Data loading utilities\n# ---------------------------------------------------------------------------\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef save_jsonl(data, path):\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    with open(path, \"w\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n    log.info(f\"Saved {len(data)} records to {path}\")\n\n\ndef load_swebench_verified():\n    \"\"\"Load SWE-bench Verified and filter to T_f2p >= MIN_F2P_TESTS.\"\"\"\n    from datasets import load_dataset\n\n    ds = load_dataset(\"princeton-nlp/SWE-bench_Verified\", split=\"test\")\n    filtered = []\n    for row in ds:\n        f2p = json.loads(row[\"FAIL_TO_PASS\"])\n        if len(f2p) >= MIN_F2P_TESTS:\n            filtered.append({\n                \"instance_id\": row[\"instance_id\"],\n                \"repo\": row[\"repo\"],\n                \"base_commit\": row[\"base_commit\"],\n                \"gold_patch\": row[\"patch\"],\n                \"test_patch\": row[\"test_patch\"],\n                \"fail_to_pass\": f2p,\n                \"pass_to_pass\": json.loads(row[\"PASS_TO_PASS\"]),\n                \"problem_statement\": row.get(\"problem_statement\", row.get(\"hints_text\", \"\")),\n                \"version\": row[\"version\"],\n            })\n    log.info(f\"SWE-bench Verified: {len(ds)} total, {len(filtered)} with T_f2p >= {MIN_F2P_TESTS}\")\n    return filtered\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Prepare — collect incorrect patches + run CLS predictions\n# ---------------------------------------------------------------------------\n\n\ndef collect_incorrect_patches(instances, predictions_dir):\n    \"\"\"Collect incorrect patches from public SWE-bench agent predictions.\n\n    Reads prediction JSONL files from predictions_dir/, matches to T>=2\n    instances, and filters to patches that are incorrect (not all F2P pass).\n\n    Returns list of {instance_id, patch, source, ...}.\n    \"\"\"\n    instance_ids = {inst[\"instance_id\"] for inst in instances}\n    patches = []\n\n    pred_dir = Path(predictions_dir)\n    for pred_file in pred_dir.glob(\"*.jsonl\"):\n        source_name = pred_file.stem\n        for line in pred_file.open():\n            rec = json.loads(line)\n            iid = rec.get(\"instance_id\")\n            if iid not in instance_ids:\n                continue\n            model_patch = rec.get(\"model_patch\", rec.get(\"patch\", \"\"))\n            if not model_patch or not model_patch.strip():\n                continue\n            patches.append({\n                \"instance_id\": iid,\n                \"patch\": model_patch,\n                \"source\": source_name,\n            })\n\n    log.info(f\"Collected {len(patches)} candidate incorrect patches from {predictions_dir}\")\n    return patches\n\n\ndef run_cls_predictions(patches_with_tests, cls_checkpoint, model_name=\"Qwen/Qwen3-8B\"):\n    \"\"\"Run CLS model to predict per-test pass/fail for each (patch, test).\n\n    Args:\n        patches_with_tests: list of {instance_id, patch, test_name, test_code, ...}\n        cls_checkpoint: path to LoRA checkpoint\n        model_name: base model name\n\n    Returns:\n        list of {instance_id, patch_id, test_name, cls_pred (0/1), cls_prob}\n    \"\"\"\n    import torch\n    from peft import PeftModel\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading CLS model: {model_name} + {cls_checkpoint}\")\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    base_model = AutoModelForCausalLM.from_pretrained(\n        model_name, torch_dtype=torch.bfloat16, device_map=\"auto\", trust_remote_code=True,\n    )\n    model = PeftModel.from_pretrained(base_model, cls_checkpoint)\n    model.eval()\n\n    results = []\n    for i, item in enumerate(patches_with_tests):\n        messages = [\n            {\"role\": \"system\", \"content\": \"You are a code verifier. Given a code patch and a test case, predict whether the test will pass or fail.\"},\n            {\"role\": \"user\", \"content\": f\"## Code\\n{item['patch']}\\n\\n## Test\\n{item['test_code']}\\n\\nWill this test pass or fail?\"},\n        ]\n        input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\n        inputs = tokenizer(input_text, return_tensors=\"pt\").to(model.device)\n\n        with torch.no_grad():\n            outputs = model.generate(**inputs, max_new_tokens=8, do_sample=False)\n\n        generated = tokenizer.decode(outputs[0][inputs[\"input_ids\"].shape[1]:], skip_special_tokens=True)\n        pred = parse_cls_output(generated)\n\n        results.append({\n            \"instance_id\": item[\"instance_id\"],\n            \"patch_id\": item.get(\"patch_id\", i),\n            \"test_name\": item[\"test_name\"],\n            \"cls_pred\": pred,\n            \"cls_raw\": generated.strip(),\n        })\n\n        if (i + 1) % 100 == 0:\n            log.info(f\"CLS inference: {i+1}/{len(patches_with_tests)}\")\n\n    return results\n\n\ndef parse_cls_output(text):\n    \"\"\"Parse CLS model output to binary 0 (fail) / 1 (pass).\"\"\"\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\")[-1]\n    text = text.strip().lower()\n    if \"pass\" in text and \"fail\" not in text:\n        return 1\n    if \"fail\" in text:\n        return 0\n    return -1  # unparseable\n\n\ndef run_ground_truth_verification(instance, patch):\n    \"\"\"Run Docker execution to get ground-truth per-test results.\n\n    Uses SWE-bench harness. Returns dict {test_name: bool(passed)}.\n    \"\"\"\n    # TODO: implement using swebench.harness\n    # from swebench.harness.run_evaluation import run_instances\n    # from swebench.harness.test_spec import make_test_spec\n    raise NotImplementedError(\"Requires SWE-bench Docker harness setup\")\n\n\ndef cmd_prepare(args):\n    log.info(\"=== Phase 1: Prepare repair dataset ===\")\n\n    instances = load_swebench_verified()\n    patches = collect_incorrect_patches(instances, args.swebench_predictions)\n\n    # TODO: for each (instance, patch), run ground-truth Docker verification\n    # to confirm patch is actually incorrect and get per-test results.\n    # Then run CLS model for per-test predictions.\n    # Finally, assemble repair_dataset.jsonl.\n\n    instance_map = {inst[\"instance_id\"]: inst for inst in instances}\n\n    dataset = []\n    for p in patches:\n        inst = instance_map.get(p[\"instance_id\"])\n        if inst is None:\n            continue\n        dataset.append({\n            \"instance_id\": p[\"instance_id\"],\n            \"repo\": inst[\"repo\"],\n            \"patch\": p[\"patch\"],\n            \"patch_source\": p[\"source\"],\n            \"gold_patch\": inst[\"gold_patch\"],\n            \"problem_statement\": inst[\"problem_statement\"],\n            \"fail_to_pass\": inst[\"fail_to_pass\"],\n            \"pass_to_pass\": inst[\"pass_to_pass\"],\n            \"gt_per_test\": {},      # placeholder: ground-truth per-test results\n            \"cls_per_test\": {},     # placeholder: CLS predictions\n        })\n\n    out_path = os.path.join(args.output_dir, \"repair_dataset.jsonl\")\n    save_jsonl(dataset, out_path)\n    log.info(f\"Prepared {len(dataset)} repair instances\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Generate — produce repair patches under each condition\n# ---------------------------------------------------------------------------\n\n\ndef build_repair_prompt(item, condition, rng=None):\n    \"\"\"Build the repair prompt for a given condition.\n\n    Returns list of chat messages [{role, content}].\n    \"\"\"\n    base_content = (\n        f\"## Issue Description\\n{item['problem_statement']}\\n\\n\"\n        f\"## Current (Incorrect) Patch\\n```diff\\n{item['patch']}\\n```\\n\"\n    )\n\n    if condition == \"control\":\n        diagnostic = \"\"\n    elif condition == \"cls-diag\":\n        per_test = item.get(\"cls_per_test\", {})\n        diagnostic = _format_diagnostic(per_test)\n    elif condition == \"oracle-diag\":\n        per_test = item.get(\"gt_per_test\", {})\n        diagnostic = _format_diagnostic(per_test)\n    elif condition == \"random-diag\":\n        all_tests = item.get(\"fail_to_pass\", []) + item.get(\"pass_to_pass\", [])\n        if rng is None:\n            rng = np.random.default_rng(42)\n        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}\n        diagnostic = _format_diagnostic(per_test)\n    else:\n        raise ValueError(f\"Unknown condition: {condition}\")\n\n    user_content = base_content\n    if diagnostic:\n        user_content += f\"\\n{diagnostic}\\n\"\n    user_content += (\n        \"\\nPlease produce a corrected patch in unified diff format that \"\n        \"resolves the issue.\\nOutput ONLY the diff, enclosed in ```diff ... ``` tags.\"\n    )\n\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT_REPAIR},\n        {\"role\": \"user\", \"content\": user_content},\n    ]\n\n\ndef _format_diagnostic(per_test):\n    \"\"\"Format per-test results into diagnostic prompt section.\"\"\"\n    if not per_test:\n        return \"\"\n    fails = [t for t, passed in per_test.items() if not passed]\n    passes = [t for t, passed in per_test.items() if passed]\n    if not fails:\n        return \"\"\n    fail_list = \"\\n\".join(f\"- `{t}`\" for t in fails)\n    pass_list = \"\\n\".join(f\"- `{t}`\" for t in passes) if passes else \"*(none)*\"\n    return DIAGNOSTIC_TEMPLATE.format(fail_list=fail_list, pass_list=pass_list)\n\n\ndef extract_diff_from_response(text):\n    \"\"\"Extract unified diff from LLM response.\"\"\"\n    pattern = r\"```diff\\s*\\n(.*?)```\"\n    match = re.search(pattern, text, re.DOTALL)\n    if match:\n        return match.group(1).strip()\n    pattern_generic = r\"```\\s*\\n(diff.*?)```\"\n    match = re.search(pattern_generic, text, re.DOTALL)\n    if match:\n        return match.group(1).strip()\n    return text.strip()\n\n\ndef generate_repairs_vllm(dataset, conditions, model_name, n_samples, output_dir):\n    \"\"\"Generate repair patches using vLLM for all conditions.\n\n    Args:\n        dataset: list of repair instances from Phase 1\n        conditions: list of condition names\n        model_name: HF model name for repair LLM\n        n_samples: number of completions per (instance, condition)\n        output_dir: where to save results\n    \"\"\"\n    from vllm import LLM, SamplingParams\n\n    log.info(f\"Loading repair LLM: {model_name}\")\n    llm = LLM(\n        model=model_name,\n        tensor_parallel_size=1,  # adjust based on GPU count\n        max_model_len=8192,\n        trust_remote_code=True,\n        dtype=\"bfloat16\",\n    )\n    sampling_params = SamplingParams(\n        temperature=0.6, top_p=0.95, max_tokens=2048, n=n_samples,\n    )\n\n    all_repairs = []\n    rng = np.random.default_rng(42)\n\n    for cond in conditions:\n        log.info(f\"Generating repairs for condition: {cond}\")\n        prompts = []\n        meta = []\n\n        for item in dataset:\n            messages = build_repair_prompt(item, cond, rng=rng)\n            # vLLM chat: convert messages to single string\n            # TODO: use tokenizer.apply_chat_template if needed\n            prompt_text = \"\\n\".join(\n                f\"<|im_start|>{m['role']}\\n{m['content']}<|im_end|>\" for m in messages\n            ) + \"\\n<|im_start|>assistant\\n\"\n            prompts.append(prompt_text)\n            meta.append({\n                \"instance_id\": item[\"instance_id\"],\n                \"condition\": cond,\n                \"patch_source\": item.get(\"patch_source\", \"unknown\"),\n            })\n\n        outputs = llm.generate(prompts, sampling_params)\n\n        for output, m in zip(outputs, meta):\n            for k, completion in enumerate(output.outputs):\n                diff = extract_diff_from_response(completion.text)\n                all_repairs.append({\n                    **m,\n                    \"sample_k\": k,\n                    \"raw_response\": completion.text,\n                    \"extracted_diff\": diff,\n                    \"diff_valid\": diff.startswith(\"diff \") or diff.startswith(\"---\"),\n                })\n\n    out_path = os.path.join(output_dir, \"generated_repairs.jsonl\")\n    save_jsonl(all_repairs, out_path)\n    log.info(f\"Generated {len(all_repairs)} total repairs\")\n    return all_repairs\n\n\ndef cmd_generate(args):\n    log.info(\"=== Phase 2: Generate repairs ===\")\n    dataset = load_jsonl(args.data)\n    conditions = args.conditions or CONDITIONS\n    generate_repairs_vllm(\n        dataset, conditions, args.model, args.n_samples, args.output_dir,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Verify — Docker execution of generated repair patches\n# ---------------------------------------------------------------------------\n\n\ndef cmd_verify(args):\n    log.info(\"=== Phase 3: Verify repairs via Docker ===\")\n    repairs = load_jsonl(args.repairs)\n\n    # Dedup: many samples produce identical diffs\n    seen = set()\n    unique_repairs = []\n    for r in repairs:\n        key = (r[\"instance_id\"], r[\"extracted_diff\"])\n        if key in seen:\n            r[\"dedup_ref\"] = True\n            continue\n        seen.add(key)\n        unique_repairs.append(r)\n\n    log.info(f\"Total repairs: {len(repairs)}, unique: {len(unique_repairs)}\")\n\n    # TODO: run SWE-bench Docker harness on each unique repair\n    # For each repair:\n    #   1. Apply extracted_diff to repo at base_commit\n    #   2. Run test suite\n    #   3. Record per-test pass/fail\n    #   4. Mark resolved = all F2P pass & no P2P regressions\n\n    results = []\n    for r in unique_repairs:\n        results.append({\n            **r,\n            \"resolved\": None,       # placeholder\n            \"f2p_passed\": None,      # placeholder: list of passed F2P tests\n            \"f2p_failed\": None,      # placeholder: list of failed F2P tests\n            \"p2p_regressed\": None,   # placeholder: list of regressed P2P tests\n            \"error\": None,\n        })\n\n    out_path = os.path.join(args.output_dir, \"verification_results.jsonl\")\n    save_jsonl(results, out_path)\n\n\n# ---------------------------------------------------------------------------\n# Phase 4: Analyze — compute metrics and statistical tests\n# ---------------------------------------------------------------------------\n\n\ndef compute_resolve_rates(results):\n    \"\"\"Compute resolve rate per condition.\n\n    Returns dict {condition: {pass_at_1, pass_at_5, n_instances, n_patches}}.\n    \"\"\"\n    by_condition = defaultdict(lambda: defaultdict(list))\n\n    for r in results:\n        cond = r[\"condition\"]\n        iid = r[\"instance_id\"]\n        resolved = r.get(\"resolved\", False)\n        by_condition[cond][iid].append(resolved)\n\n    metrics = {}\n    for cond, instances in by_condition.items():\n        n_inst = len(instances)\n        pass_at_1_sum = 0\n        pass_at_5_sum = 0\n\n        for iid, resolutions in instances.items():\n            k = len(resolutions)\n            n_pass = sum(resolutions)\n            # pass@1: unbiased estimator\n            pass_at_1_sum += 1 - (comb_ratio(k - n_pass, 1, k, 1) if k >= 1 else 1.0)\n            # pass@5\n            pass_at_5_sum += 1 - (comb_ratio(k - n_pass, 5, k, 5) if k >= 5 else (0.0 if n_pass > 0 else 1.0))\n\n        metrics[cond] = {\n            \"pass_at_1\": pass_at_1_sum / n_inst if n_inst else 0,\n            \"pass_at_5\": pass_at_5_sum / n_inst if n_inst else 0,\n            \"n_instances\": n_inst,\n            \"n_total_repairs\": sum(len(v) for v in instances.values()),\n        }\n\n    return metrics\n\n\ndef comb_ratio(a, b, c, d):\n    \"\"\"Compute C(a,b) / C(c,d) safely.\"\"\"\n    from math import comb\n    denom = comb(c, d)\n    if denom == 0:\n        return 0.0\n    return comb(a, b) / denom\n\n\ndef mcnemar_test(results, cond_a=\"control\", cond_b=\"cls-diag\"):\n    \"\"\"McNemar's test comparing two conditions on paired instances.\n\n    Returns (chi2, p_value, contingency_table).\n    \"\"\"\n    from scipy.stats import chi2 as chi2_dist\n\n    paired = defaultdict(lambda: {})\n    for r in results:\n        cond = r[\"condition\"]\n        iid = r[\"instance_id\"]\n        if cond in (cond_a, cond_b):\n            # Use best-of-K (any resolved)\n            if iid not in paired or cond not in paired[iid]:\n                paired[iid][cond] = False\n            if r.get(\"resolved\", False):\n                paired[iid][cond] = True\n\n    a_only = 0  # cond_a resolves, cond_b doesn't\n    b_only = 0  # cond_b resolves, cond_a doesn't\n    both = 0\n    neither = 0\n\n    for iid, conds in paired.items():\n        ra = conds.get(cond_a, False)\n        rb = conds.get(cond_b, False)\n        if ra and rb:\n            both += 1\n        elif ra and not rb:\n            a_only += 1\n        elif not ra and rb:\n            b_only += 1\n        else:\n            neither += 1\n\n    n_discord = a_only + b_only\n    if n_discord == 0:\n        return 0.0, 1.0, {\"both\": both, \"neither\": neither, \"a_only\": a_only, \"b_only\": b_only}\n\n    chi2 = (abs(a_only - b_only) - 1) ** 2 / n_discord\n    p_value = 1 - chi2_dist.cdf(chi2, df=1)\n\n    return chi2, p_value, {\"both\": both, \"neither\": neither, \"a_only\": a_only, \"b_only\": b_only}\n\n\ndef clustered_bootstrap_ci(results, cond_a, cond_b, n_resamples=10000, seed=42):\n    \"\"\"Clustered bootstrap CI for Δ resolve rate (cond_b - cond_a).\n\n    Clusters by instance_id. Returns (mean_delta, ci_lower, ci_upper).\n    \"\"\"\n    rng = np.random.default_rng(seed)\n\n    instance_resolve = defaultdict(lambda: defaultdict(bool))\n    for r in results:\n        if r.get(\"resolved\", False):\n            instance_resolve[r[\"instance_id\"]][r[\"condition\"]] = True\n\n    instance_ids = list(instance_resolve.keys())\n    n = len(instance_ids)\n    if n == 0:\n        return 0.0, 0.0, 0.0\n\n    deltas = np.zeros(n_resamples)\n    for b in range(n_resamples):\n        idx = rng.choice(n, size=n, replace=True)\n        ra = np.mean([instance_resolve[instance_ids[i]].get(cond_a, False) for i in idx])\n        rb = np.mean([instance_resolve[instance_ids[i]].get(cond_b, False) for i in idx])\n        deltas[b] = rb - ra\n\n    return float(np.mean(deltas)), float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))\n\n\ndef stratify_by_cls_accuracy(results, cls_predictions):\n    \"\"\"Split results by CLS accuracy per instance.\n\n    Returns {accuracy_bin: [results]}.\n    \"\"\"\n    instance_cls_acc = defaultdict(list)\n    for p in cls_predictions:\n        correct = (p[\"cls_pred\"] == p.get(\"gt_label\"))\n        instance_cls_acc[p[\"instance_id\"]].append(correct)\n\n    instance_acc = {\n        iid: np.mean(corrects) for iid, corrects in instance_cls_acc.items()\n    }\n\n    bins = {\"high_acc_ge90\": [], \"low_acc_lt90\": []}\n    for r in results:\n        acc = instance_acc.get(r[\"instance_id\"], 0.5)\n        if acc >= 0.9:\n            bins[\"high_acc_ge90\"].append(r)\n        else:\n            bins[\"low_acc_lt90\"].append(r)\n\n    return bins\n\n\ndef cmd_analyze(args):\n    log.info(\"=== Phase 4: Analyze results ===\")\n    results = load_jsonl(args.results)\n\n    # Resolve rates\n    rates = compute_resolve_rates(results)\n    log.info(\"Resolve rates by condition:\")\n    for cond, m in rates.items():\n        log.info(f\"  {cond}: pass@1={m['pass_at_1']:.3f}, pass@5={m['pass_at_5']:.3f} (n={m['n_instances']})\")\n\n    # McNemar: control vs cls-diag\n    chi2, p, table = mcnemar_test(results, \"control\", \"cls-diag\")\n    log.info(f\"McNemar control vs cls-diag: chi2={chi2:.3f}, p={p:.4f}, table={table}\")\n\n    # McNemar: control vs oracle-diag\n    chi2_o, p_o, table_o = mcnemar_test(results, \"control\", \"oracle-diag\")\n    log.info(f\"McNemar control vs oracle-diag: chi2={chi2_o:.3f}, p={p_o:.4f}, table={table_o}\")\n\n    # Bootstrap CI\n    delta_mean, ci_lo, ci_hi = clustered_bootstrap_ci(results, \"control\", \"cls-diag\")\n    log.info(f\"Bootstrap Δ(cls-diag − control): {delta_mean:.3f} [{ci_lo:.3f}, {ci_hi:.3f}]\")\n\n    delta_o_mean, ci_o_lo, ci_o_hi = clustered_bootstrap_ci(results, \"control\", \"oracle-diag\")\n    log.info(f\"Bootstrap Δ(oracle − control): {delta_o_mean:.3f} [{ci_o_lo:.3f}, {ci_o_hi:.3f}]\")\n\n    # Summary\n    summary = {\n        \"resolve_rates\": rates,\n        \"mcnemar_control_vs_cls\": {\"chi2\": chi2, \"p_value\": p, \"table\": table},\n        \"mcnemar_control_vs_oracle\": {\"chi2\": chi2_o, \"p_value\": p_o, \"table\": table_o},\n        \"bootstrap_cls_minus_control\": {\"mean\": delta_mean, \"ci_95\": [ci_lo, ci_hi]},\n        \"bootstrap_oracle_minus_control\": {\"mean\": delta_o_mean, \"ci_95\": [ci_o_lo, ci_o_hi]},\n    }\n\n    out_path = os.path.join(args.output_dir, \"metrics_summary.json\")\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(summary, f, indent=2)\n    log.info(f\"Saved metrics summary to {out_path}\")\n\n    # Generate figure\n    generate_resolve_rate_figure(rates, args.output_dir)\n\n\ndef generate_resolve_rate_figure(rates, output_dir):\n    \"\"\"Bar chart: resolve rate by condition.\"\"\"\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        log.warning(\"matplotlib not available, skipping figure generation\")\n        return\n\n    conds = [\"control\", \"cls-diag\", \"oracle-diag\", \"random-diag\"]\n    conds = [c for c in conds if c in rates]\n    pass1 = [rates[c][\"pass_at_1\"] * 100 for c in conds]\n    pass5 = [rates[c][\"pass_at_5\"] * 100 for c in conds]\n\n    x = np.arange(len(conds))\n    width = 0.35\n\n    fig, ax = plt.subplots(figsize=(8, 5))\n    bars1 = ax.bar(x - width / 2, pass1, width, label=\"pass@1\", color=\"#4C72B0\")\n    bars2 = ax.bar(x + width / 2, pass5, width, label=\"pass@5\", color=\"#55A868\")\n\n    ax.set_ylabel(\"Resolve Rate (%)\")\n    ax.set_xlabel(\"Condition\")\n    ax.set_title(\"Re-Repair Resolve Rate by Diagnostic Condition\")\n    ax.set_xticks(x)\n    ax.set_xticklabels(conds, rotation=15)\n    ax.legend()\n    ax.set_ylim(0, max(pass5 + pass1 + [10]) * 1.2)\n\n    for bars in [bars1, bars2]:\n        for bar in bars:\n            h = bar.get_height()\n            ax.annotate(f\"{h:.1f}\", xy=(bar.get_x() + bar.get_width() / 2, h),\n                        xytext=(0, 3), textcoords=\"offset points\", ha=\"center\", fontsize=9)\n\n    fig.tight_layout()\n    out_path = os.path.join(output_dir, \"fig_resolve_rate.pdf\")\n    fig.savefig(out_path, dpi=150, bbox_inches=\"tight\")\n    plt.close(fig)\n    log.info(f\"Saved figure to {out_path}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Re-Repair Downstream Experiment\")\n    sub = parser.add_subparsers(dest=\"command\", required=True)\n\n    # prepare\n    p_prep = sub.add_parser(\"prepare\", help=\"Phase 1: prepare repair dataset\")\n    p_prep.add_argument(\"--swebench-predictions\", required=True, help=\"Dir with agent prediction .jsonl files\")\n    p_prep.add_argument(\"--cls-checkpoint\", required=True, help=\"Path to CLS LoRA checkpoint\")\n    p_prep.add_argument(\"--cls-base-model\", default=\"Qwen/Qwen3-8B\", help=\"CLS base model name\")\n    p_prep.add_argument(\"--output-dir\", default=\"artifacts/re_repair\")\n\n    # generate\n    p_gen = sub.add_parser(\"generate\", help=\"Phase 2: generate repair patches\")\n    p_gen.add_argument(\"--data\", required=True, help=\"repair_dataset.jsonl from Phase 1\")\n    p_gen.add_argument(\"--model\", default=\"Qwen/Qwen3-8B-Instruct\", help=\"Repair LLM\")\n    p_gen.add_argument(\"--conditions\", nargs=\"+\", default=CONDITIONS)\n    p_gen.add_argument(\"--n-samples\", type=int, default=10, help=\"Completions per (instance, condition)\")\n    p_gen.add_argument(\"--output-dir\", default=\"artifacts/re_repair\")\n\n    # verify\n    p_ver = sub.add_parser(\"verify\", help=\"Phase 3: verify repairs via Docker\")\n    p_ver.add_argument(\"--repairs\", required=True, help=\"generated_repairs.jsonl from Phase 2\")\n    p_ver.add_argument(\"--max-workers\", type=int, default=4, help=\"Parallel Docker containers\")\n    p_ver.add_argument(\"--timeout\", type=int, default=300, help=\"Per-instance timeout (seconds)\")\n    p_ver.add_argument(\"--output-dir\", default=\"artifacts/re_repair\")\n\n    # analyze\n    p_ana = sub.add_parser(\"analyze\", help=\"Phase 4: analyze results\")\n    p_ana.add_argument(\"--results\", required=True, help=\"verification_results.jsonl from Phase 3\")\n    p_ana.add_argument(\"--cls-predictions\", default=None, help=\"CLS predictions for stratification\")\n    p_ana.add_argument(\"--output-dir\", default=\"artifacts/re_repair\")\n\n    args = parser.parse_args()\n\n    if args.command == \"prepare\":\n        cmd_prepare(args)\n    elif args.command == \"generate\":\n        cmd_generate(args)\n    elif args.command == \"verify\":\n        cmd_verify(args)\n    elif args.command == \"analyze\":\n        cmd_analyze(args)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 736,
      "startLine": 1,
      "totalLines": 736
    }
  }
}
````

</details>

---

### Assistant

_source line 9_

## Re-Repair Phase0 代码审计报告

---

### 文件 1: `re_repair_phase0.py` — 快速可行性测试

#### 1. Prompt Template 结构

**System Prompt（所有 condition 共用）：**
```python
"You are a software engineer. You are given a code patch that was intended "
"to fix an issue but does not fully work. Your task is to produce a corrected "
"patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
```

**Control condition（L94）：**
```
## Issue Description
{problem_statement}

## Current (Incorrect) Patch
```diff
{mutation_patch}
```

Please produce a corrected patch in unified diff format.
Output ONLY the diff, enclosed in ```diff ... ``` tags.
```

**Diagnostic conditions（L96-112）追加内容：**
```
## Test Diagnostic
The current patch **fails** the following tests:
- `test_foo`
- `test_bar`

The current patch **passes** the following tests:
- `test_baz`
```

**信息差异：**
| Condition | 诊断来源 |
|-----------|----------|
| `control` | 无诊断 |
| `oracle-diag` | `item["oracle_per_test"]` — 真实 per-test pass/fail |
| `cls-diag` | oracle labels + 16% 随机翻转（模拟 84% accuracy CLS）|
| `random-diag` | 完全随机 50/50 |

**诊断信息来源：** `swebench_test.jsonl` 中的 oracle labels（L161-169），按 `(instance_id, mutation_type)` 分组，`label` 字段表示测试通过/失败。这是预先跑过 Docker 得到的 ground-truth 测试结果，不是 CLS verifier predictions。

#### 2. 评估方法

**Metric：`difflib.SequenceMatcher.ratio()`（L67-71）**
- 比较 LLM 输出的 diff 文本与 gold patch 的字符级序列相似度
- 范围 [0, 1]
- 额外指标：`diff_nonempty`（长度>20），`has_diff_header`（以 `diff ` 或 `---` 开头）

**评估方式：** Proxy metric（纯文本比较），不跑测试。

**Baseline：** 4 个 condition 之间横向比较 `best_of_k_mean`（每个 instance 取 K=5 samples 中最高 similarity），然后计算 `Δ(oracle-diag - control)` 等。

#### 3. 实验设计

| 维度 | 值 |
|------|-----|
| LLM | `Qwen/Qwen3-8B`（L345，**base model，非 instruct**）|
| 数据源 | `princeton-nlp/SWE-bench_Verified`（HF），筛选 `FAIL_TO_PASS >= 2` |
| Bug 类型 | **Mutation patches**（来自 `predictions_mutation_*.jsonl`）|
| Sample size | 10 instances × 4 conditions × K=5 = 200 completions |
| vLLM 参数 | temp=0.6, top_p=0.95, max_tokens=2048 |

#### 4. 评估方法（`re_repair_eval.py` 补充）

**Metric：** End-to-end Docker 验证（Phase 3），计算 `pass@1` 和 `pass@5`（unbiased estimator, L476-480）

**统计检验：**
- McNemar's test（paired instances, L501-543）
- Clustered bootstrap CI（10000 resamples, L546-570）

**Repair LLM：** `Qwen/Qwen3-8B-Instruct`（L703，注意是 Instruct 版本）

**Sample size：** N=10 per (instance, condition)

---

### 文件 2: `re_repair_eval.py` — 完整 4-phase pipeline

与 phase0 核心差异：
- 使用**真实 incorrect patches**（公开 SWE-bench agent predictions），而非 mutation
- CLS predictions 来自**实际 CLS LoRA 模型推理**（L149-198），不是模拟
- 验证通过 **Docker 执行**（Phase 3），非 diff similarity
- prompt 中 `item['patch']` 是 agent 生成的 incorrect patch，不是 mutation patch

---

### 需要修改的地方（D116 Design Space Characterization）

#### A. Base model → Instruct model

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L345 `--model` default | `Qwen/Qwen3-8B` (base) | `Qwen/Qwen3-8B-Instruct` |
| `re_repair_phase0.py` | L244 `tokenizer.apply_chat_template` | 调用存在，但 base model 的 chat template 行为未定义 | 换 instruct model 后 template 自动正确 |
| `re_repair_eval.py` | L703 | 已经是 `Qwen/Qwen3-8B-Instruct` ✓ | 无需改 |

**结论：** phase0 用 base model 做 chat completion 是设计缺陷——base model 没有 instruction following 能力，生成的 diff 质量会很差，similarity 指标可能主要反映格式噪声而非修复质量。

#### B. Mutation → Real bugs

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L148 | 读 `predictions_mutation_*.jsonl` | 读公开 agent predictions（如 SWE-bench leaderboard submissions） |
| `re_repair_phase0.py` | L92 prompt | `item['mutation_patch']` | `item['patch']`（agent 生成的 incorrect patch）|
| `re_repair_phase0.py` | L161-169 | oracle labels from `swebench_test.jsonl` keyed by mutation_type | Docker ground-truth per-test results for real patches |
| `re_repair_eval.py` | L117-146 | `collect_incorrect_patches` 已设计为读 agent predictions ✓ | 实际需要配合 Docker 验证确认 patch 确实 incorrect |

**`re_repair_eval.py` 已经设计为 real bugs 流程**，但 Phase 3 verify 是 placeholder（`raise NotImplementedError`）。需要实现 SWE-bench Docker harness 集成。

#### C. Eval metric

| 问题 | 详情 |
|------|------|
| Phase0 的 `diff_similarity` | 字符级 SequenceMatcher 是非常弱的 proxy：相同语义修复可能有完全不同的 diff 文本（不同 hunk 边界、不同变量命名重构路径）。会严重低估非 gold-patch-identical 的正确修复。 |
| 建议 | 用 end-to-end test pass rate（`re_repair_eval.py` Phase 3 已设计但未实现）。如果 Docker infra 不可用，至少用 CodeBLEU 或 AST-level diff 替代字符 similarity。 |
| `re_repair_eval.py` 的 pass@k | 正确的 end-to-end metric ✓，但需要 Docker harness |

#### D. Control/diagnostic info 在 real bug 场景下的来源

| Condition | Mutation 场景来源 | Real bug 场景应改为 |
|-----------|------------------|---------------------|
| `oracle-diag` | `swebench_test.jsonl` 预计算 labels | Docker 执行 incorrect patch 后的真实 per-test 结果（`gt_per_test`）|
| `cls-diag` | oracle × 84% 随机翻转模拟 | **实际 CLS LoRA 模型推理**（`re_repair_eval.py` L149-198 已实现）|
| `random-diag` | 随机 50/50 | 不变 |
| `control` | 无诊断 | 不变 |

**关键依赖：** real bug 流程需要先对每个 (incorrect_patch, instance) pair 跑 Docker 获得 `gt_per_test`，这既是 oracle-diag 的来源，也是验证 CLS accuracy 的 ground truth。`re_repair_eval.py` 的 `run_ground_truth_verification`（L213-221）是 placeholder。

---

### 总结

Phase0（`re_repair_phase0.py`）是一个快速 feasibility check，关键设计选择：base model + mutation patches + text similarity proxy。这三个都需要改。

`re_repair_eval.py` 是完整设计，架构正确（instruct model + real patches + Docker verify + pass@k + McNemar），但 Phase 1 的 ground-truth 收集和 Phase 3 的 Docker verify 是 placeholder。核心 blocker 是 SWE-bench Docker harness 集成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "uuid": "57e294a6-f1ab-4ebc-b60f-03c4809ee5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEjDLqFKtG9pMqj3V8McyU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15639,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15639
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

_source line 10_

## Re-Repair Phase0 代码审计报告

---

### 文件 1: `re_repair_phase0.py` — 快速可行性测试

#### 1. Prompt Template 结构

**System Prompt（所有 condition 共用）：**
```python
"You are a software engineer. You are given a code patch that was intended "
"to fix an issue but does not fully work. Your task is to produce a corrected "
"patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
```

**Control condition（L94）：**
```
## Issue Description
{problem_statement}

## Current (Incorrect) Patch
```diff
{mutation_patch}
```

Please produce a corrected patch in unified diff format.
Output ONLY the diff, enclosed in ```diff ... ``` tags.
```

**Diagnostic conditions（L96-112）追加内容：**
```
## Test Diagnostic
The current patch **fails** the following tests:
- `test_foo`
- `test_bar`

The current patch **passes** the following tests:
- `test_baz`
```

**信息差异：**
| Condition | 诊断来源 |
|-----------|----------|
| `control` | 无诊断 |
| `oracle-diag` | `item["oracle_per_test"]` — 真实 per-test pass/fail |
| `cls-diag` | oracle labels + 16% 随机翻转（模拟 84% accuracy CLS）|
| `random-diag` | 完全随机 50/50 |

**诊断信息来源：** `swebench_test.jsonl` 中的 oracle labels（L161-169），按 `(instance_id, mutation_type)` 分组，`label` 字段表示测试通过/失败。这是预先跑过 Docker 得到的 ground-truth 测试结果，不是 CLS verifier predictions。

#### 2. 评估方法

**Metric：`difflib.SequenceMatcher.ratio()`（L67-71）**
- 比较 LLM 输出的 diff 文本与 gold patch 的字符级序列相似度
- 范围 [0, 1]
- 额外指标：`diff_nonempty`（长度>20），`has_diff_header`（以 `diff ` 或 `---` 开头）

**评估方式：** Proxy metric（纯文本比较），不跑测试。

**Baseline：** 4 个 condition 之间横向比较 `best_of_k_mean`（每个 instance 取 K=5 samples 中最高 similarity），然后计算 `Δ(oracle-diag - control)` 等。

#### 3. 实验设计

| 维度 | 值 |
|------|-----|
| LLM | `Qwen/Qwen3-8B`（L345，**base model，非 instruct**）|
| 数据源 | `princeton-nlp/SWE-bench_Verified`（HF），筛选 `FAIL_TO_PASS >= 2` |
| Bug 类型 | **Mutation patches**（来自 `predictions_mutation_*.jsonl`）|
| Sample size | 10 instances × 4 conditions × K=5 = 200 completions |
| vLLM 参数 | temp=0.6, top_p=0.95, max_tokens=2048 |

#### 4. 评估方法（`re_repair_eval.py` 补充）

**Metric：** End-to-end Docker 验证（Phase 3），计算 `pass@1` 和 `pass@5`（unbiased estimator, L476-480）

**统计检验：**
- McNemar's test（paired instances, L501-543）
- Clustered bootstrap CI（10000 resamples, L546-570）

**Repair LLM：** `Qwen/Qwen3-8B-Instruct`（L703，注意是 Instruct 版本）

**Sample size：** N=10 per (instance, condition)

---

### 文件 2: `re_repair_eval.py` — 完整 4-phase pipeline

与 phase0 核心差异：
- 使用**真实 incorrect patches**（公开 SWE-bench agent predictions），而非 mutation
- CLS predictions 来自**实际 CLS LoRA 模型推理**（L149-198），不是模拟
- 验证通过 **Docker 执行**（Phase 3），非 diff similarity
- prompt 中 `item['patch']` 是 agent 生成的 incorrect patch，不是 mutation patch

---

### 需要修改的地方（D116 Design Space Characterization）

#### A. Base model → Instruct model

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L345 `--model` default | `Qwen/Qwen3-8B` (base) | `Qwen/Qwen3-8B-Instruct` |
| `re_repair_phase0.py` | L244 `tokenizer.apply_chat_template` | 调用存在，但 base model 的 chat template 行为未定义 | 换 instruct model 后 template 自动正确 |
| `re_repair_eval.py` | L703 | 已经是 `Qwen/Qwen3-8B-Instruct` ✓ | 无需改 |

**结论：** phase0 用 base model 做 chat completion 是设计缺陷——base model 没有 instruction following 能力，生成的 diff 质量会很差，similarity 指标可能主要反映格式噪声而非修复质量。

#### B. Mutation → Real bugs

| 文件 | 位置 | 当前 | 应改为 |
|------|------|------|--------|
| `re_repair_phase0.py` | L148 | 读 `predictions_mutation_*.jsonl` | 读公开 agent predictions（如 SWE-bench leaderboard submissions） |
| `re_repair_phase0.py` | L92 prompt | `item['mutation_patch']` | `item['patch']`（agent 生成的 incorrect patch）|
| `re_repair_phase0.py` | L161-169 | oracle labels from `swebench_test.jsonl` keyed by mutation_type | Docker ground-truth per-test results for real patches |
| `re_repair_eval.py` | L117-146 | `collect_incorrect_patches` 已设计为读 agent predictions ✓ | 实际需要配合 Docker 验证确认 patch 确实 incorrect |

**`re_repair_eval.py` 已经设计为 real bugs 流程**，但 Phase 3 verify 是 placeholder（`raise NotImplementedError`）。需要实现 SWE-bench Docker harness 集成。

#### C. Eval metric

| 问题 | 详情 |
|------|------|
| Phase0 的 `diff_similarity` | 字符级 SequenceMatcher 是非常弱的 proxy：相同语义修复可能有完全不同的 diff 文本（不同 hunk 边界、不同变量命名重构路径）。会严重低估非 gold-patch-identical 的正确修复。 |
| 建议 | 用 end-to-end test pass rate（`re_repair_eval.py` Phase 3 已设计但未实现）。如果 Docker infra 不可用，至少用 CodeBLEU 或 AST-level diff 替代字符 similarity。 |
| `re_repair_eval.py` 的 pass@k | 正确的 end-to-end metric ✓，但需要 Docker harness |

#### D. Control/diagnostic info 在 real bug 场景下的来源

| Condition | Mutation 场景来源 | Real bug 场景应改为 |
|-----------|------------------|---------------------|
| `oracle-diag` | `swebench_test.jsonl` 预计算 labels | Docker 执行 incorrect patch 后的真实 per-test 结果（`gt_per_test`）|
| `cls-diag` | oracle × 84% 随机翻转模拟 | **实际 CLS LoRA 模型推理**（`re_repair_eval.py` L149-198 已实现）|
| `random-diag` | 随机 50/50 | 不变 |
| `control` | 无诊断 | 不变 |

**关键依赖：** real bug 流程需要先对每个 (incorrect_patch, instance) pair 跑 Docker 获得 `gt_per_test`，这既是 oracle-diag 的来源，也是验证 CLS accuracy 的 ground truth。`re_repair_eval.py` 的 `run_ground_truth_verification`（L213-221）是 placeholder。

---

### 总结

Phase0（`re_repair_phase0.py`）是一个快速 feasibility check，关键设计选择：base model + mutation patches + text similarity proxy。这三个都需要改。

`re_repair_eval.py` 是完整设计，架构正确（instruct model + real patches + Docker verify + pass@k + McNemar），但 Phase 1 的 ground-truth 收集和 Phase 3 的 Docker verify 是 placeholder。核心 blocker 是 SWE-bench Docker harness 集成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67648,
  "duration_api_ms": 68554,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "84990399-ad84-43dc-95f0-965a8193c76c",
  "total_cost_usd": 0.27258499999999997,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 29438,
    "cache_read_input_tokens": 36693,
    "output_tokens": 2755,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29438,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2562,
        "cache_read_input_tokens": 25246,
        "cache_creation_input_tokens": 15639,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 15639
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1266,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001356,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 2755,
      "cacheReadInputTokens": 36693,
      "cacheCreationInputTokens": 29438,
      "webSearchRequests": 0,
      "costUSD": 0.271229,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "87f4e0b2-d4c2-49dd-b5ec-f5b7020dbb82"
}
```

</details>

---
