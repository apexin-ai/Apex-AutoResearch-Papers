# code asb write

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_code_asb_write_20260520T162800.log`
- **Structured JSON:** [`76f53e8174ef7fbc7fc2.json`](../../sessions/76/76f53e8174ef7fbc7fc2.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__distill_papers",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_distill_status",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_mistakes",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "ab99a9ba-9688-42f3-a2ab-cbbe701ba257",
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
    "resetsAt": 1779309600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ce121f87-efb3-4679-9d7d-d4212e4b1c9c",
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the reference files to understand the data format and existing utility functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "5326c927-f1f3-4ea6-9c86-cd1e0845de25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QehufsjwHyEtW5aSaJdkWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 24,
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

Reading reference files to understand data format and existing utilities.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "83f03b22-2444-4a43-bf5f-7368e3801b8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QehufsjwHyEtW5aSaJdkWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Read · `toolu_01J6FDVzDuyFZdVk6S9b2N4a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/esj/run_esj.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "0248b247-51ec-4312-bae2-ef9a693c082b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QehufsjwHyEtW5aSaJdkWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-20T16:28:14.525Z_

<details><summary>↩ Tool result · `toolu_01J6FDVzDuyFZdVk6S9b2N4a`</summary>

```text
1	#!/usr/bin/env python3
2	"""Entity-Level Self-Judgment (ESJ) for structured self-consistency IE.
3	
4	For each unique entity across N=8 samples, uses the FT model to do a
5	yes/no verification forward pass. P(yes) serves as entity-level confidence
6	for weighted construction.
7	"""
8	
9	import argparse
10	import json
11	import os
12	import sys
13	import time
14	from collections import defaultdict
15	
16	import numpy as np
17	import torch
18	from transformers import AutoTokenizer, AutoModelForCausalLM
19	from peft import PeftModel
20	from scipy.stats import spearmanr
21	from sklearn.metrics import roc_auc_score
22	
23	
24	# ---------------------------------------------------------------------------
25	# Data
26	# ---------------------------------------------------------------------------
27	
28	def load_samples(path, max_instances=0):
29	    data = []
30	    with open(path) as f:
31	        for line in f:
32	            if line.strip():
33	                data.append(json.loads(line))
34	                if 0 < max_instances <= len(data):
35	                    break
36	    return data
37	
38	
39	def extract_unique_entities(instance):
40	    """Return {(start, end, type, text): count_across_samples}."""
41	    emap = defaultdict(int)
42	    for sample in instance["samples"]:
43	        for e in sample.get("entities", []):
44	            emap[(e["start"], e["end"], e["type"], e["text"])] += 1
45	    return emap
46	
47	
48	# ---------------------------------------------------------------------------
49	# Prompt
50	# ---------------------------------------------------------------------------
51	
52	def build_verification_prompt(sentence, entity_text, entity_type):
53	    return (
54	        f'In the following sentence, is "{entity_text}" a {entity_type} entity? '
55	        f'Answer only yes or no.\n\n'
56	        f'Sentence: {sentence}\n'
57	        f'Answer:'
58	    )
59	
60	
61	# ---------------------------------------------------------------------------
62	# Model
63	# ---------------------------------------------------------------------------
64	
65	def load_model(base_path, adapter_path, device="cuda"):
66	    tok_path = adapter_path if adapter_path else base_path
67	    print(f"Loading tokenizer from {tok_path} ...")
68	    tokenizer = AutoTokenizer.from_pretrained(
69	        tok_path, trust_remote_code=True, padding_side="left",
70	    )
71	    if tokenizer.pad_token is None:
72	        tokenizer.pad_token = tokenizer.eos_token
73	
74	    print(f"Loading base model from {base_path} ...")
75	    model = AutoModelForCausalLM.from_pretrained(
76	        base_path,
77	        torch_dtype=torch.bfloat16,
78	        device_map=device,
79	        trust_remote_code=True,
80	    )
81	
82	    if adapter_path:
83	        print(f"Loading LoRA adapter from {adapter_path} ...")
84	        model = PeftModel.from_pretrained(model, adapter_path)
85	        model = model.merge_and_unload()
86	        print("LoRA merged.")
87	
88	    model.eval()
89	    return model, tokenizer
90	
91	
92	def get_yes_no_ids(tokenizer):
93	    yes_ids, no_ids = [], []
94	    for w in ["yes", "Yes", "YES"]:
95	        ids = tokenizer.encode(w, add_special_tokens=False)
96	        if len(ids) == 1:
97	            yes_ids.append(ids[0])
98	    for w in ["no", "No", "NO"]:
99	        ids = tokenizer.encode(w, add_special_tokens=False)
100	        if len(ids) == 1:
101	            no_ids.append(ids[0])
102	    yes_ids = list(set(yes_ids))
103	    no_ids = list(set(no_ids))
104	    print(f"yes token IDs: {yes_ids}  no token IDs: {no_ids}")
105	    assert yes_ids and no_ids, "Could not find yes/no token IDs"
106	    return yes_ids, no_ids
107	
108	
109	# ---------------------------------------------------------------------------
110	# Batch verification
111	# ---------------------------------------------------------------------------
112	
113	@torch.no_grad()
114	def batch_verify(model, tokenizer, prompts, yes_ids, no_ids,
115	                 batch_size=16, device="cuda"):
116	    yes_t = torch.tensor(yes_ids, device=device)
117	    no_t = torch.tensor(no_ids, device=device)
118	    all_p_yes = []
119	
120	    n_batches = (len(prompts) + batch_size - 1) // batch_size
121	    for bi in range(n_batches):
122	        start = bi * batch_size
123	        batch = prompts[start:start + batch_size]
124	
125	        formatted = []
126	        for p in batch:
127	            msgs = [{"role": "user", "content": p}]
128	            try:
129	                fp = tokenizer.apply_chat_template(
130	                    msgs, tokenize=False, add_generation_prompt=True,
131	                    enable_thinking=False,
132	                )
133	            except TypeError:
134	                fp = tokenizer.apply_chat_template(
135	                    msgs, tokenize=False, add_generation_prompt=True,
136	                )
137	            formatted.append(fp)
138	
139	        inputs = tokenizer(
140	            formatted, return_tensors="pt", padding=True,
141	            truncation=True, max_length=512,
142	        ).to(device)
143	
144	        logits = model(**inputs).logits  # (B, L, V)
145	
146	        for i in range(len(batch)):
147	            last_pos = inputs.attention_mask[i].sum() - 1
148	            next_logits = logits[i, last_pos]
149	            y_logits = next_logits[yes_t]
150	            n_logits = next_logits[no_t]
151	            combined = torch.cat([y_logits, n_logits])
152	            probs = torch.softmax(combined, dim=0)
153	            p_yes = probs[:len(yes_ids)].sum().item()
154	            all_p_yes.append(p_yes)
155	
156	        if bi % 100 == 0:
157	            print(f"  batch {bi}/{n_batches}  avg_p_yes={np.mean(all_p_yes[-len(batch):]):.3f}")
158	
159	    return all_p_yes
160	
161	
162	# ---------------------------------------------------------------------------
163	# Eval helpers
164	# ---------------------------------------------------------------------------
165	
166	def entity_set(entities):
167	    return {(e["start"], e["end"], e["type"]) for e in entities}
168	
169	
170	def compute_prf(pred, gold):
171	    if not gold and not pred:
172	        return 1.0, 1.0, 1.0
173	    if not pred or not gold:
174	        return 0.0, 0.0, 0.0
175	    tp = len(pred & gold)
176	    if tp == 0:
177	        return 0.0, 0.0, 0.0
178	    p = tp / len(pred)
179	    r = tp / len(gold)
180	    return p, r, 2 * p * r / (p + r)
181	
182	
183	def majority_vote(instance, threshold=0.5):
184	    counts = defaultdict(int)
185	    N = len(instance["samples"])
186	    for s in instance["samples"]:
187	        for e in s.get("entities", []):
188	            counts[(e["start"], e["end"], e["type"])] += 1
189	    return {k for k, c in counts.items() if c / N >= threshold}
190	
191	
192	def esj_construction(instance, esj_scores, threshold):
193	    counts = defaultdict(int)
194	    N = len(instance["samples"])
195	    for s in instance["samples"]:
196	        for e in s.get("entities", []):
197	            counts[(e["start"], e["end"], e["type"])] += 1
198	    out = set()
199	    for key, c in counts.items():
200	        p_yes = esj_scores.get(key, 0.0)
201	        if p_yes * (c / N) >= threshold:
202	            out.add(key)
203	    return out
204	
205	
206	def safe_spearman(a, b):
207	    mask = np.isfinite(a) & np.isfinite(b)
208	    if mask.sum() < 3:
209	        return float("nan"), float("nan")
210	    return spearmanr(a[mask], b[mask])
211	
212	
213	def safe_auroc(scores, labels):
214	    mask = np.isfinite(scores)
215	    s, l = scores[mask], labels[mask]
216	    if len(set(l)) < 2:
217	        return float("nan")
218	    try:
219	        return roc_auc_score(l, s)
220	    except Exception:
221	        return float("nan")
222	
223	
224	# ---------------------------------------------------------------------------
225	# Within-instance sample ranking (ESJ can rank samples, LP cannot for entity-level)
226	# ---------------------------------------------------------------------------
227	
228	def compute_sample_esj_scores(instance, esj_scores):
229	    """Mean P(yes) across entities in each sample."""
230	    per_sample = []
231	    for s in instance["samples"]:
232	        ents = s.get("entities", [])
233	        if not ents:
234	            per_sample.append(0.0)
235	            continue
236	        pyes_vals = []
237	        for e in ents:
238	            key = (e["start"], e["end"], e["type"])
239	            pyes_vals.append(esj_scores.get(key, 0.0))
240	        per_sample.append(float(np.mean(pyes_vals)))
241	    return per_sample
242	
243	
244	def compute_sample_lp_scores(instance):
245	    out = []
246	    for s in instance["samples"]:
247	        lp = s.get("mean_logprob")
248	        if lp is None:
249	            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
250	        out.append(lp)
251	    return out
252	
253	
254	# ---------------------------------------------------------------------------
255	# Main
256	# ---------------------------------------------------------------------------
257	
258	def main():
259	    ap = argparse.ArgumentParser()
260	    ap.add_argument("--base_model_path", type=str, required=True)
261	    ap.add_argument("--adapter_path", type=str, default=None)
262	    ap.add_argument("--data_path", type=str, required=True)
263	    ap.add_argument("--output_dir", type=str, required=True)
264	    ap.add_argument("--max_instances", type=int, default=0)
265	    ap.add_argument("--batch_size", type=int, default=16)
266	    args = ap.parse_args()
267	
268	    os.makedirs(args.output_dir, exist_ok=True)
269	    device = "cuda"
270	
271	    # ---- 1. Load data ----
272	    print(f"Loading data from {args.data_path} ...")
273	    data = load_samples(args.data_path, args.max_instances)
274	    print(f"  {len(data)} instances loaded")
275	
276	    # ---- 2. Collect unique entities ----
277	    print("Extracting unique entities ...")
278	    inst_emaps = []
279	    total_occ, total_uniq = 0, 0
280	    for inst in data:
281	        em = extract_unique_entities(inst)
282	        inst_emaps.append(em)
283	        total_occ += sum(em.values())
284	        total_uniq += len(em)
285	    print(f"  {total_uniq} unique entities to verify ({total_occ} total occurrences)")
286	    print(f"  avg {total_uniq/len(data):.1f} unique / {total_occ/len(data):.1f} total per instance")
287	
288	    # ---- 3. Build prompts ----
289	    all_prompts = []
290	    prompt_idx = []  # (instance_i, (start, end, type))
291	    for i, inst in enumerate(data):
292	        for (s, e, t, txt), _ in inst_emaps[i].items():
293	            all_prompts.append(build_verification_prompt(inst["text"], txt, t))
294	            prompt_idx.append((i, (s, e, t)))
295	    print(f"  {len(all_prompts)} verification prompts built")
296	
297	    # ---- 4. Load model ----
298	    model, tokenizer = load_model(args.base_model_path, args.adapter_path, device)
299	    yes_ids, no_ids = get_yes_no_ids(tokenizer)
300	
301	    # ---- 5. Run verification ----
302	    print(f"Running batch verification (batch_size={args.batch_size}) ...")
303	    t0 = time.time()
304	    p_yes_all = batch_verify(model, tokenizer, all_prompts, yes_ids, no_ids,
305	                             args.batch_size, device)
306	    elapsed = time.time() - t0
307	    print(f"  Done in {elapsed:.1f}s ({len(all_prompts)/elapsed:.0f} prompts/s)")
308	
309	    del model
310	    import gc; gc.collect(); torch.cuda.empty_cache()
311	
312	    # ---- 6. Map P(yes) back ----
313	    inst_esj = [dict() for _ in range(len(data))]
314	    for idx, (ii, key) in enumerate(prompt_idx):
315	        inst_esj[ii][key] = p_yes_all[idx]
316	
317	    # ---- 7. Baselines ----
318	    print("Computing baselines ...")
319	    greedy_f1s, oracle_f1s = [], []
320	    for inst in data:
321	        gold = entity_set(inst["gold"]["entities"])
322	        g = entity_set(inst.get("greedy", inst["samples"][0]).get("entities", []))
323	        greedy_f1s.append(compute_prf(g, gold)[2])
324	        oracle_f1s.append(max(
325	            compute_prf(entity_set(s.get("entities", [])), gold)[2]
326	            for s in inst["samples"]
327	        ))
328	    greedy_f1 = float(np.mean(greedy_f1s))
329	    oracle_f1 = float(np.mean(oracle_f1s))
330	
331	    mv_ths = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75]
332	    mv_res = {}
333	    for th in mv_ths:
334	        fs = []
335	        for i, inst in enumerate(data):
336	            gold = entity_set(inst["gold"]["entities"])
337	            fs.append(compute_prf(majority_vote(inst, th), gold)[2])
338	        mv_res[str(th)] = float(np.mean(fs))
339	    best_mv_th = max(mv_res, key=mv_res.get)
340	    best_mv_f1 = mv_res[best_mv_th]
341	
342	    # ---- 8. ESJ construction ----
343	    print("Evaluating ESJ construction ...")
344	    esj_ths = [0.02, 0.05, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
345	    esj_res = {}
346	    for th in esj_ths:
347	        fs = []
348	        for i, inst in enumerate(data):
349	            gold = entity_set(inst["gold"]["entities"])
350	            fs.append(compute_prf(esj_construction(inst, inst_esj[i], th), gold)[2])
351	        esj_res[str(th)] = float(np.mean(fs))
352	    best_esj_th = max(esj_res, key=esj_res.get)
353	    best_esj_f1 = esj_res[best_esj_th]
354	
355	    # ---- 9. Entity-level signal quality ----
356	    print("Entity-level analysis ...")
357	    ent_correct, ent_esj, ent_agree = [], [], []
358	    for i, inst in enumerate(data):
359	        gold = entity_set(inst["gold"]["entities"])
360	        N = len(inst["samples"])
361	        counts = defaultdict(int)
362	        for s in inst["samples"]:
363	            for e in s.get("entities", []):
364	                counts[(e["start"], e["end"], e["type"])] += 1
365	        for key, c in counts.items():
366	            ent_correct.append(1 if key in gold else 0)
367	            ent_esj.append(inst_esj[i].get(key, 0.0))
368	            ent_agree.append(c / N)
369	
370	    ent_correct = np.array(ent_correct)
371	    ent_esj_arr = np.array(ent_esj)
372	    ent_agree_arr = np.array(ent_agree)
373	    ent_combined = ent_esj_arr * ent_agree_arr
374	
375	    rho_esj, p_rho_esj = safe_spearman(ent_esj_arr, ent_correct.astype(float))
376	    rho_agree, _ = safe_spearman(ent_agree_arr, ent_correct.astype(float))
377	    rho_comb, _ = safe_spearman(ent_combined, ent_correct.astype(float))
378	    auroc_esj = safe_auroc(ent_esj_arr, ent_correct)
379	    auroc_agree = safe_auroc(ent_agree_arr, ent_correct)
380	    auroc_comb = safe_auroc(ent_combined, ent_correct)
381	
382	    # ---- 10. Breakdown by agreement ----
383	    disputed = ent_agree_arr < 0.5
384	    consensus = ent_agree_arr >= 0.75
385	    mid = (~disputed) & (~consensus)
386	
387	    def group_stats(mask, label):
388	        n = int(mask.sum())
389	        if n < 3:
390	            return {"n": n}
391	        return {
392	            "n": n,
393	            "correct_rate": round(float(ent_correct[mask].mean()), 4),
394	            "esj_mean": round(float(ent_esj_arr[mask].mean()), 4),
395	            "esj_std": round(float(ent_esj_arr[mask].std()), 4),
396	            "rho_esj_correct": round(float(safe_spearman(ent_esj_arr[mask], ent_correct[mask].astype(float))[0]), 4),
397	            "auroc_esj": round(safe_auroc(ent_esj_arr[mask], ent_correct[mask]), 4),
398	        }
399	
400	    # ---- 11. Within-instance sample ranking ----
401	    print("Within-instance sample ranking ...")
402	    esj_rank_corrs, lp_rank_corrs = [], []
403	    for i, inst in enumerate(data):
404	        gold = entity_set(inst["gold"]["entities"])
405	        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
406	                      for s in inst["samples"]]
407	        if len(set(sample_f1s)) < 2:
408	            continue
409	        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])
410	        lp_sample = compute_sample_lp_scores(inst)
411	        r_esj, _ = spearmanr(esj_sample, sample_f1s)
412	        r_lp, _ = spearmanr(lp_sample, sample_f1s)
413	        if np.isfinite(r_esj):
414	            esj_rank_corrs.append(r_esj)
415	        if np.isfinite(r_lp):
416	            lp_rank_corrs.append(r_lp)
417	
418	    # ESJ-based selection F1 (pick best sample by ESJ score)
419	    esj_sel_f1s, lp_sel_f1s = [], []
420	    for i, inst in enumerate(data):
421	        gold = entity_set(inst["gold"]["entities"])
422	        sample_f1s = [compute_prf(entity_set(s.get("entities", [])), gold)[2]
423	                      for s in inst["samples"]]
424	        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])
425	        lp_sample = compute_sample_lp_scores(inst)
426	        esj_sel_f1s.append(sample_f1s[int(np.argmax(esj_sample))])
427	        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_sample))])
428	
429	    # ---- 12. P(yes) distribution ----
430	    pya = np.array(p_yes_all)
431	    p_yes_dist = {
432	        "mean": round(float(pya.mean()), 4),
433	        "std": round(float(pya.std()), 4),
434	        "median": round(float(np.median(pya)), 4),
435	        "q25": round(float(np.percentile(pya, 25)), 4),
436	        "q75": round(float(np.percentile(pya, 75)), 4),
437	    }
438	
439	    # ---- Build result ----
440	    result = {
441	        "experiment": "ESJ_entity_self_judgment",
442	        "model_base": args.base_model_path,
443	        "adapter": args.adapter_path,
444	        "data": args.data_path,
445	        "n_instances": len(data),
446	        "n_unique_entities": total_uniq,
447	        "n_entity_occurrences": total_occ,
448	        "avg_unique_per_instance": round(total_uniq / len(data), 2),
449	        "verification_seconds": round(elapsed, 1),
450	        "prompts_per_second": round(len(all_prompts) / elapsed, 1),
451	        "p_yes_distribution": p_yes_dist,
452	        "construction_f1": {
453	            "greedy": round(greedy_f1, 4),
454	            "oracle": round(oracle_f1, 4),
455	            "majority_vote": {k: round(v, 4) for k, v in mv_res.items()},
456	            "best_mv": {"threshold": best_mv_th, "f1": round(best_mv_f1, 4)},
457	            "esj_weighted": {k: round(v, 4) for k, v in esj_res.items()},
458	            "best_esj": {"threshold": best_esj_th, "f1": round(best_esj_f1, 4)},
459	        },
460	        "deltas": {
461	            "esj_vs_greedy": round(best_esj_f1 - greedy_f1, 4),
462	            "esj_vs_mv": round(best_esj_f1 - best_mv_f1, 4),
463	            "mv_vs_greedy": round(best_mv_f1 - greedy_f1, 4),
464	        },
465	        "entity_signal_quality": {
466	            "n_entities": len(ent_correct),
467	            "overall_correct_rate": round(float(ent_correct.mean()), 4),
468	            "esj": {"rho": round(float(rho_esj), 4), "auroc": round(float(auroc_esj), 4)},
469	            "agreement": {"rho": round(float(rho_agree), 4), "auroc": round(float(auroc_agree), 4)},
470	            "esj_x_agreement": {"rho": round(float(rho_comb), 4), "auroc": round(float(auroc_comb), 4)},
471	        },
472	        "agreement_breakdown": {
473	            "disputed_lt0.5": group_stats(disputed, "disputed"),
474	            "mid_0.5_0.75": group_stats(mid, "mid"),
475	            "consensus_gte0.75": group_stats(consensus, "consensus"),
476	        },
477	        "within_instance_ranking": {
478	            "esj_mean_rho": round(float(np.mean(esj_rank_corrs)), 4) if esj_rank_corrs else None,
479	            "lp_mean_rho": round(float(np.mean(lp_rank_corrs)), 4) if lp_rank_corrs else None,
480	            "n_rankable_instances": len(esj_rank_corrs),
481	            "esj_selection_f1": round(float(np.mean(esj_sel_f1s)), 4),
482	            "lp_selection_f1": round(float(np.mean(lp_sel_f1s)), 4),
483	        },
484	    }
485	
486	    out_path = os.path.join(args.output_dir, "esj_results.json")
487	    with open(out_path, "w") as f:
488	        json.dump(result, f, indent=2)
489	    print(f"\nSaved: {out_path}")
490	
491	    # ---- Print summary ----
492	    print(f"\n{'='*60}")
493	    print("ESJ Entity-Level Self-Judgment Results")
494	    print(f"{'='*60}")
495	    print(f"Instances: {len(data)}  Unique entities verified: {total_uniq}")
496	    print(f"P(yes): mean={p_yes_dist['mean']}, std={p_yes_dist['std']}, median={p_yes_dist['median']}")
497	    print(f"\nConstruction F1 (macro):")
498	    print(f"  Greedy:              {greedy_f1:.4f}")
499	    print(f"  Best MV (θ={best_mv_th}):  {best_mv_f1:.4f}  (Δ={best_mv_f1-greedy_f1:+.4f})")
500	    print(f"  Best ESJ (θ={best_esj_th}): {best_esj_f1:.4f}  (Δ={best_esj_f1-greedy_f1:+.4f})")
501	    print(f"  Oracle:              {oracle_f1:.4f}")
502	    print(f"  ESJ vs MV: {best_esj_f1-best_mv_f1:+.4f}")
503	    print(f"\nEntity-level signal:")
504	    print(f"  ESJ         ρ={rho_esj:+.4f}  AUROC={auroc_esj:.4f}")
505	    print(f"  Agreement   ρ={rho_agree:+.4f}  AUROC={auroc_agree:.4f}")
506	    print(f"  ESJ×Agree   ρ={rho_comb:+.4f}  AUROC={auroc_comb:.4f}")
507	    print(f"\nWithin-instance ranking (rho with sample F1):")
508	    if esj_rank_corrs:
509	        print(f"  ESJ: {np.mean(esj_rank_corrs):+.4f} ({len(esj_rank_corrs)} instances)")
510	    if lp_rank_corrs:
511	        print(f"  LP:  {np.mean(lp_rank_corrs):+.4f} ({len(lp_rank_corrs)} instances)")
512	    print(f"\nSelection F1 (pick best sample):")
513	    print(f"  ESJ: {np.mean(esj_sel_f1s):.4f}  LP: {np.mean(lp_sel_f1s):.4f}  Greedy: {greedy_f1:.4f}")
514	    print(f"\nBreakdown by agreement:")
515	    for label, mask in [("Disputed (<0.5)", disputed), ("Mid [0.5,0.75)", mid), ("Consensus (≥0.75)", consensus)]:
516	        n = mask.sum()
517	        if n >= 3:
518	            print(f"  {label}: n={n}, correct={ent_correct[mask].mean():.3f}, "
519	                  f"ESJ_mean={ent_esj_arr[mask].mean():.3f}, "
520	                  f"AUROC={safe_auroc(ent_esj_arr[mask], ent_correct[mask]):.4f}")
521	
522	
523	if __name__ == "__main__":
524	    main()
525	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "9be8b456-721c-4137-97aa-e003e2eba1da",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/esj/run_esj.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Entity-Level Self-Judgment (ESJ) for structured self-consistency IE.\n\nFor each unique entity across N=8 samples, uses the FT model to do a\nyes/no verification forward pass. P(yes) serves as entity-level confidence\nfor weighted construction.\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nfrom collections import defaultdict\n\nimport numpy as np\nimport torch\nfrom transformers import AutoTokenizer, AutoModelForCausalLM\nfrom peft import PeftModel\nfrom scipy.stats import spearmanr\nfrom sklearn.metrics import roc_auc_score\n\n\n# ---------------------------------------------------------------------------\n# Data\n# ---------------------------------------------------------------------------\n\ndef load_samples(path, max_instances=0):\n    data = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                data.append(json.loads(line))\n                if 0 < max_instances <= len(data):\n                    break\n    return data\n\n\ndef extract_unique_entities(instance):\n    \"\"\"Return {(start, end, type, text): count_across_samples}.\"\"\"\n    emap = defaultdict(int)\n    for sample in instance[\"samples\"]:\n        for e in sample.get(\"entities\", []):\n            emap[(e[\"start\"], e[\"end\"], e[\"type\"], e[\"text\"])] += 1\n    return emap\n\n\n# ---------------------------------------------------------------------------\n# Prompt\n# ---------------------------------------------------------------------------\n\ndef build_verification_prompt(sentence, entity_text, entity_type):\n    return (\n        f'In the following sentence, is \"{entity_text}\" a {entity_type} entity? '\n        f'Answer only yes or no.\\n\\n'\n        f'Sentence: {sentence}\\n'\n        f'Answer:'\n    )\n\n\n# ---------------------------------------------------------------------------\n# Model\n# ---------------------------------------------------------------------------\n\ndef load_model(base_path, adapter_path, device=\"cuda\"):\n    tok_path = adapter_path if adapter_path else base_path\n    print(f\"Loading tokenizer from {tok_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(\n        tok_path, trust_remote_code=True, padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading base model from {base_path} ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        base_path,\n        torch_dtype=torch.bfloat16,\n        device_map=device,\n        trust_remote_code=True,\n    )\n\n    if adapter_path:\n        print(f\"Loading LoRA adapter from {adapter_path} ...\")\n        model = PeftModel.from_pretrained(model, adapter_path)\n        model = model.merge_and_unload()\n        print(\"LoRA merged.\")\n\n    model.eval()\n    return model, tokenizer\n\n\ndef get_yes_no_ids(tokenizer):\n    yes_ids, no_ids = [], []\n    for w in [\"yes\", \"Yes\", \"YES\"]:\n        ids = tokenizer.encode(w, add_special_tokens=False)\n        if len(ids) == 1:\n            yes_ids.append(ids[0])\n    for w in [\"no\", \"No\", \"NO\"]:\n        ids = tokenizer.encode(w, add_special_tokens=False)\n        if len(ids) == 1:\n            no_ids.append(ids[0])\n    yes_ids = list(set(yes_ids))\n    no_ids = list(set(no_ids))\n    print(f\"yes token IDs: {yes_ids}  no token IDs: {no_ids}\")\n    assert yes_ids and no_ids, \"Could not find yes/no token IDs\"\n    return yes_ids, no_ids\n\n\n# ---------------------------------------------------------------------------\n# Batch verification\n# ---------------------------------------------------------------------------\n\n@torch.no_grad()\ndef batch_verify(model, tokenizer, prompts, yes_ids, no_ids,\n                 batch_size=16, device=\"cuda\"):\n    yes_t = torch.tensor(yes_ids, device=device)\n    no_t = torch.tensor(no_ids, device=device)\n    all_p_yes = []\n\n    n_batches = (len(prompts) + batch_size - 1) // batch_size\n    for bi in range(n_batches):\n        start = bi * batch_size\n        batch = prompts[start:start + batch_size]\n\n        formatted = []\n        for p in batch:\n            msgs = [{\"role\": \"user\", \"content\": p}]\n            try:\n                fp = tokenizer.apply_chat_template(\n                    msgs, tokenize=False, add_generation_prompt=True,\n                    enable_thinking=False,\n                )\n            except TypeError:\n                fp = tokenizer.apply_chat_template(\n                    msgs, tokenize=False, add_generation_prompt=True,\n                )\n            formatted.append(fp)\n\n        inputs = tokenizer(\n            formatted, return_tensors=\"pt\", padding=True,\n            truncation=True, max_length=512,\n        ).to(device)\n\n        logits = model(**inputs).logits  # (B, L, V)\n\n        for i in range(len(batch)):\n            last_pos = inputs.attention_mask[i].sum() - 1\n            next_logits = logits[i, last_pos]\n            y_logits = next_logits[yes_t]\n            n_logits = next_logits[no_t]\n            combined = torch.cat([y_logits, n_logits])\n            probs = torch.softmax(combined, dim=0)\n            p_yes = probs[:len(yes_ids)].sum().item()\n            all_p_yes.append(p_yes)\n\n        if bi % 100 == 0:\n            print(f\"  batch {bi}/{n_batches}  avg_p_yes={np.mean(all_p_yes[-len(batch):]):.3f}\")\n\n    return all_p_yes\n\n\n# ---------------------------------------------------------------------------\n# Eval helpers\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities):\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred, gold):\n    if not gold and not pred:\n        return 1.0, 1.0, 1.0\n    if not pred or not gold:\n        return 0.0, 0.0, 0.0\n    tp = len(pred & gold)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred)\n    r = tp / len(gold)\n    return p, r, 2 * p * r / (p + r)\n\n\ndef majority_vote(instance, threshold=0.5):\n    counts = defaultdict(int)\n    N = len(instance[\"samples\"])\n    for s in instance[\"samples\"]:\n        for e in s.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\ndef esj_construction(instance, esj_scores, threshold):\n    counts = defaultdict(int)\n    N = len(instance[\"samples\"])\n    for s in instance[\"samples\"]:\n        for e in s.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    out = set()\n    for key, c in counts.items():\n        p_yes = esj_scores.get(key, 0.0)\n        if p_yes * (c / N) >= threshold:\n            out.add(key)\n    return out\n\n\ndef safe_spearman(a, b):\n    mask = np.isfinite(a) & np.isfinite(b)\n    if mask.sum() < 3:\n        return float(\"nan\"), float(\"nan\")\n    return spearmanr(a[mask], b[mask])\n\n\ndef safe_auroc(scores, labels):\n    mask = np.isfinite(scores)\n    s, l = scores[mask], labels[mask]\n    if len(set(l)) < 2:\n        return float(\"nan\")\n    try:\n        return roc_auc_score(l, s)\n    except Exception:\n        return float(\"nan\")\n\n\n# ---------------------------------------------------------------------------\n# Within-instance sample ranking (ESJ can rank samples, LP cannot for entity-level)\n# ---------------------------------------------------------------------------\n\ndef compute_sample_esj_scores(instance, esj_scores):\n    \"\"\"Mean P(yes) across entities in each sample.\"\"\"\n    per_sample = []\n    for s in instance[\"samples\"]:\n        ents = s.get(\"entities\", [])\n        if not ents:\n            per_sample.append(0.0)\n            continue\n        pyes_vals = []\n        for e in ents:\n            key = (e[\"start\"], e[\"end\"], e[\"type\"])\n            pyes_vals.append(esj_scores.get(key, 0.0))\n        per_sample.append(float(np.mean(pyes_vals)))\n    return per_sample\n\n\ndef compute_sample_lp_scores(instance):\n    out = []\n    for s in instance[\"samples\"]:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        out.append(lp)\n    return out\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    ap = argparse.ArgumentParser()\n    ap.add_argument(\"--base_model_path\", type=str, required=True)\n    ap.add_argument(\"--adapter_path\", type=str, default=None)\n    ap.add_argument(\"--data_path\", type=str, required=True)\n    ap.add_argument(\"--output_dir\", type=str, required=True)\n    ap.add_argument(\"--max_instances\", type=int, default=0)\n    ap.add_argument(\"--batch_size\", type=int, default=16)\n    args = ap.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    device = \"cuda\"\n\n    # ---- 1. Load data ----\n    print(f\"Loading data from {args.data_path} ...\")\n    data = load_samples(args.data_path, args.max_instances)\n    print(f\"  {len(data)} instances loaded\")\n\n    # ---- 2. Collect unique entities ----\n    print(\"Extracting unique entities ...\")\n    inst_emaps = []\n    total_occ, total_uniq = 0, 0\n    for inst in data:\n        em = extract_unique_entities(inst)\n        inst_emaps.append(em)\n        total_occ += sum(em.values())\n        total_uniq += len(em)\n    print(f\"  {total_uniq} unique entities to verify ({total_occ} total occurrences)\")\n    print(f\"  avg {total_uniq/len(data):.1f} unique / {total_occ/len(data):.1f} total per instance\")\n\n    # ---- 3. Build prompts ----\n    all_prompts = []\n    prompt_idx = []  # (instance_i, (start, end, type))\n    for i, inst in enumerate(data):\n        for (s, e, t, txt), _ in inst_emaps[i].items():\n            all_prompts.append(build_verification_prompt(inst[\"text\"], txt, t))\n            prompt_idx.append((i, (s, e, t)))\n    print(f\"  {len(all_prompts)} verification prompts built\")\n\n    # ---- 4. Load model ----\n    model, tokenizer = load_model(args.base_model_path, args.adapter_path, device)\n    yes_ids, no_ids = get_yes_no_ids(tokenizer)\n\n    # ---- 5. Run verification ----\n    print(f\"Running batch verification (batch_size={args.batch_size}) ...\")\n    t0 = time.time()\n    p_yes_all = batch_verify(model, tokenizer, all_prompts, yes_ids, no_ids,\n                             args.batch_size, device)\n    elapsed = time.time() - t0\n    print(f\"  Done in {elapsed:.1f}s ({len(all_prompts)/elapsed:.0f} prompts/s)\")\n\n    del model\n    import gc; gc.collect(); torch.cuda.empty_cache()\n\n    # ---- 6. Map P(yes) back ----\n    inst_esj = [dict() for _ in range(len(data))]\n    for idx, (ii, key) in enumerate(prompt_idx):\n        inst_esj[ii][key] = p_yes_all[idx]\n\n    # ---- 7. Baselines ----\n    print(\"Computing baselines ...\")\n    greedy_f1s, oracle_f1s = [], []\n    for inst in data:\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        g = entity_set(inst.get(\"greedy\", inst[\"samples\"][0]).get(\"entities\", []))\n        greedy_f1s.append(compute_prf(g, gold)[2])\n        oracle_f1s.append(max(\n            compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n            for s in inst[\"samples\"]\n        ))\n    greedy_f1 = float(np.mean(greedy_f1s))\n    oracle_f1 = float(np.mean(oracle_f1s))\n\n    mv_ths = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75]\n    mv_res = {}\n    for th in mv_ths:\n        fs = []\n        for i, inst in enumerate(data):\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            fs.append(compute_prf(majority_vote(inst, th), gold)[2])\n        mv_res[str(th)] = float(np.mean(fs))\n    best_mv_th = max(mv_res, key=mv_res.get)\n    best_mv_f1 = mv_res[best_mv_th]\n\n    # ---- 8. ESJ construction ----\n    print(\"Evaluating ESJ construction ...\")\n    esj_ths = [0.02, 0.05, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]\n    esj_res = {}\n    for th in esj_ths:\n        fs = []\n        for i, inst in enumerate(data):\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            fs.append(compute_prf(esj_construction(inst, inst_esj[i], th), gold)[2])\n        esj_res[str(th)] = float(np.mean(fs))\n    best_esj_th = max(esj_res, key=esj_res.get)\n    best_esj_f1 = esj_res[best_esj_th]\n\n    # ---- 9. Entity-level signal quality ----\n    print(\"Entity-level analysis ...\")\n    ent_correct, ent_esj, ent_agree = [], [], []\n    for i, inst in enumerate(data):\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        N = len(inst[\"samples\"])\n        counts = defaultdict(int)\n        for s in inst[\"samples\"]:\n            for e in s.get(\"entities\", []):\n                counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n        for key, c in counts.items():\n            ent_correct.append(1 if key in gold else 0)\n            ent_esj.append(inst_esj[i].get(key, 0.0))\n            ent_agree.append(c / N)\n\n    ent_correct = np.array(ent_correct)\n    ent_esj_arr = np.array(ent_esj)\n    ent_agree_arr = np.array(ent_agree)\n    ent_combined = ent_esj_arr * ent_agree_arr\n\n    rho_esj, p_rho_esj = safe_spearman(ent_esj_arr, ent_correct.astype(float))\n    rho_agree, _ = safe_spearman(ent_agree_arr, ent_correct.astype(float))\n    rho_comb, _ = safe_spearman(ent_combined, ent_correct.astype(float))\n    auroc_esj = safe_auroc(ent_esj_arr, ent_correct)\n    auroc_agree = safe_auroc(ent_agree_arr, ent_correct)\n    auroc_comb = safe_auroc(ent_combined, ent_correct)\n\n    # ---- 10. Breakdown by agreement ----\n    disputed = ent_agree_arr < 0.5\n    consensus = ent_agree_arr >= 0.75\n    mid = (~disputed) & (~consensus)\n\n    def group_stats(mask, label):\n        n = int(mask.sum())\n        if n < 3:\n            return {\"n\": n}\n        return {\n            \"n\": n,\n            \"correct_rate\": round(float(ent_correct[mask].mean()), 4),\n            \"esj_mean\": round(float(ent_esj_arr[mask].mean()), 4),\n            \"esj_std\": round(float(ent_esj_arr[mask].std()), 4),\n            \"rho_esj_correct\": round(float(safe_spearman(ent_esj_arr[mask], ent_correct[mask].astype(float))[0]), 4),\n            \"auroc_esj\": round(safe_auroc(ent_esj_arr[mask], ent_correct[mask]), 4),\n        }\n\n    # ---- 11. Within-instance sample ranking ----\n    print(\"Within-instance sample ranking ...\")\n    esj_rank_corrs, lp_rank_corrs = [], []\n    for i, inst in enumerate(data):\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        sample_f1s = [compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n                      for s in inst[\"samples\"]]\n        if len(set(sample_f1s)) < 2:\n            continue\n        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])\n        lp_sample = compute_sample_lp_scores(inst)\n        r_esj, _ = spearmanr(esj_sample, sample_f1s)\n        r_lp, _ = spearmanr(lp_sample, sample_f1s)\n        if np.isfinite(r_esj):\n            esj_rank_corrs.append(r_esj)\n        if np.isfinite(r_lp):\n            lp_rank_corrs.append(r_lp)\n\n    # ESJ-based selection F1 (pick best sample by ESJ score)\n    esj_sel_f1s, lp_sel_f1s = [], []\n    for i, inst in enumerate(data):\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        sample_f1s = [compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n                      for s in inst[\"samples\"]]\n        esj_sample = compute_sample_esj_scores(inst, inst_esj[i])\n        lp_sample = compute_sample_lp_scores(inst)\n        esj_sel_f1s.append(sample_f1s[int(np.argmax(esj_sample))])\n        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_sample))])\n\n    # ---- 12. P(yes) distribution ----\n    pya = np.array(p_yes_all)\n    p_yes_dist = {\n        \"mean\": round(float(pya.mean()), 4),\n        \"std\": round(float(pya.std()), 4),\n        \"median\": round(float(np.median(pya)), 4),\n        \"q25\": round(float(np.percentile(pya, 25)), 4),\n        \"q75\": round(float(np.percentile(pya, 75)), 4),\n    }\n\n    # ---- Build result ----\n    result = {\n        \"experiment\": \"ESJ_entity_self_judgment\",\n        \"model_base\": args.base_model_path,\n        \"adapter\": args.adapter_path,\n        \"data\": args.data_path,\n        \"n_instances\": len(data),\n        \"n_unique_entities\": total_uniq,\n        \"n_entity_occurrences\": total_occ,\n        \"avg_unique_per_instance\": round(total_uniq / len(data), 2),\n        \"verification_seconds\": round(elapsed, 1),\n        \"prompts_per_second\": round(len(all_prompts) / elapsed, 1),\n        \"p_yes_distribution\": p_yes_dist,\n        \"construction_f1\": {\n            \"greedy\": round(greedy_f1, 4),\n            \"oracle\": round(oracle_f1, 4),\n            \"majority_vote\": {k: round(v, 4) for k, v in mv_res.items()},\n            \"best_mv\": {\"threshold\": best_mv_th, \"f1\": round(best_mv_f1, 4)},\n            \"esj_weighted\": {k: round(v, 4) for k, v in esj_res.items()},\n            \"best_esj\": {\"threshold\": best_esj_th, \"f1\": round(best_esj_f1, 4)},\n        },\n        \"deltas\": {\n            \"esj_vs_greedy\": round(best_esj_f1 - greedy_f1, 4),\n            \"esj_vs_mv\": round(best_esj_f1 - best_mv_f1, 4),\n            \"mv_vs_greedy\": round(best_mv_f1 - greedy_f1, 4),\n        },\n        \"entity_signal_quality\": {\n            \"n_entities\": len(ent_correct),\n            \"overall_correct_rate\": round(float(ent_correct.mean()), 4),\n            \"esj\": {\"rho\": round(float(rho_esj), 4), \"auroc\": round(float(auroc_esj), 4)},\n            \"agreement\": {\"rho\": round(float(rho_agree), 4), \"auroc\": round(float(auroc_agree), 4)},\n            \"esj_x_agreement\": {\"rho\": round(float(rho_comb), 4), \"auroc\": round(float(auroc_comb), 4)},\n        },\n        \"agreement_breakdown\": {\n            \"disputed_lt0.5\": group_stats(disputed, \"disputed\"),\n            \"mid_0.5_0.75\": group_stats(mid, \"mid\"),\n            \"consensus_gte0.75\": group_stats(consensus, \"consensus\"),\n        },\n        \"within_instance_ranking\": {\n            \"esj_mean_rho\": round(float(np.mean(esj_rank_corrs)), 4) if esj_rank_corrs else None,\n            \"lp_mean_rho\": round(float(np.mean(lp_rank_corrs)), 4) if lp_rank_corrs else None,\n            \"n_rankable_instances\": len(esj_rank_corrs),\n            \"esj_selection_f1\": round(float(np.mean(esj_sel_f1s)), 4),\n            \"lp_selection_f1\": round(float(np.mean(lp_sel_f1s)), 4),\n        },\n    }\n\n    out_path = os.path.join(args.output_dir, \"esj_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    print(f\"\\nSaved: {out_path}\")\n\n    # ---- Print summary ----\n    print(f\"\\n{'='*60}\")\n    print(\"ESJ Entity-Level Self-Judgment Results\")\n    print(f\"{'='*60}\")\n    print(f\"Instances: {len(data)}  Unique entities verified: {total_uniq}\")\n    print(f\"P(yes): mean={p_yes_dist['mean']}, std={p_yes_dist['std']}, median={p_yes_dist['median']}\")\n    print(f\"\\nConstruction F1 (macro):\")\n    print(f\"  Greedy:              {greedy_f1:.4f}\")\n    print(f\"  Best MV (θ={best_mv_th}):  {best_mv_f1:.4f}  (Δ={best_mv_f1-greedy_f1:+.4f})\")\n    print(f\"  Best ESJ (θ={best_esj_th}): {best_esj_f1:.4f}  (Δ={best_esj_f1-greedy_f1:+.4f})\")\n    print(f\"  Oracle:              {oracle_f1:.4f}\")\n    print(f\"  ESJ vs MV: {best_esj_f1-best_mv_f1:+.4f}\")\n    print(f\"\\nEntity-level signal:\")\n    print(f\"  ESJ         ρ={rho_esj:+.4f}  AUROC={auroc_esj:.4f}\")\n    print(f\"  Agreement   ρ={rho_agree:+.4f}  AUROC={auroc_agree:.4f}\")\n    print(f\"  ESJ×Agree   ρ={rho_comb:+.4f}  AUROC={auroc_comb:.4f}\")\n    print(f\"\\nWithin-instance ranking (rho with sample F1):\")\n    if esj_rank_corrs:\n        print(f\"  ESJ: {np.mean(esj_rank_corrs):+.4f} ({len(esj_rank_corrs)} instances)\")\n    if lp_rank_corrs:\n        print(f\"  LP:  {np.mean(lp_rank_corrs):+.4f} ({len(lp_rank_corrs)} instances)\")\n    print(f\"\\nSelection F1 (pick best sample):\")\n    print(f\"  ESJ: {np.mean(esj_sel_f1s):.4f}  LP: {np.mean(lp_sel_f1s):.4f}  Greedy: {greedy_f1:.4f}\")\n    print(f\"\\nBreakdown by agreement:\")\n    for label, mask in [(\"Disputed (<0.5)\", disputed), (\"Mid [0.5,0.75)\", mid), (\"Consensus (≥0.75)\", consensus)]:\n        n = mask.sum()\n        if n >= 3:\n            print(f\"  {label}: n={n}, correct={ent_correct[mask].mean():.3f}, \"\n                  f\"ESJ_mean={ent_esj_arr[mask].mean():.3f}, \"\n                  f\"AUROC={safe_auroc(ent_esj_arr[mask], ent_correct[mask]):.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 525,
      "startLine": 1,
      "totalLines": 525
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01RrRtYsgnzARg8ckq2d6SYL`</summary>

```json
{
  "pattern": "artifacts/experiments/asb/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "b6717aed-54f1-4f3c-9d48-593e392837b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QehufsjwHyEtW5aSaJdkWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 24,
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

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_0155rJquFhWGEKNyJCkFNk16`</summary>

```json
{
  "pattern": "artifacts/n_inverse_scaling/run_analysis.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "3129c745-55cf-44a7-ba0f-a3fd0464879b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QehufsjwHyEtW5aSaJdkWT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13716,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13716
      },
      "output_tokens": 24,
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

_source line 10 · 2026-05-20T16:28:15.854Z_

<details><summary>↩ Tool result · `toolu_01RrRtYsgnzARg8ckq2d6SYL`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "f32794fa-d167-4d34-b3ae-f8def6b4af63",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 67,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T16:28:15.880Z_

<details><summary>↩ Tool result · `toolu_0155rJquFhWGEKNyJCkFNk16`</summary>

```text
artifacts/n_inverse_scaling/run_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "49be358a-ec58-4bc3-ac31-86c67c9d34d9",
  "tool_use_result": {
    "filenames": [
      "artifacts/n_inverse_scaling/run_analysis.py"
    ],
    "durationMs": 45,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01L6rnjKCgWp7mXVu462DWke`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "f553f0e4-12b5-4283-8534-1d3ae55bb2fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEyLV1tBzBhb7SjtmwpoR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8538,
      "cache_read_input_tokens": 25557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8538
      },
      "output_tokens": 35,
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

_source line 13 · 2026-05-20T16:28:19.847Z_

<details><summary>↩ Tool result · `toolu_01L6rnjKCgWp7mXVu462DWke`</summary>

```text
1	#!/usr/bin/env python3
2	"""Inverse scaling test: check if F1 decreases as N increases for construction methods.
3	
4	For each dataset×model×method, sub-sample N=16 (or N=8) samples to N=2,4,6,8,(16),
5	compute entity-level micro F1, detect inverse scaling (F1 drop > 0.1pp),
6	and run paired bootstrap significance tests.
7	"""
8	
9	import json
10	import math
11	import os
12	import sys
13	import time
14	import numpy as np
15	from collections import defaultdict, Counter
16	
17	BASE = "/root/autodl-tmp/struct_self_consist_ie"
18	OUTPUT_DIR = f"{BASE}/artifacts/n_inverse_scaling"
19	
20	CONFIGS = {
21	    "Qwen_SciERC": {
22	        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
23	        "model": "Qwen3-8B-FT", "dataset": "SciERC",
24	    },
25	    "Qwen_CoNLL": {
26	        "path": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
27	        "model": "Qwen3-8B-FT", "dataset": "CoNLL",
28	    },
29	    "Qwen_FewNERD": {
30	        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
31	        "model": "Qwen3-8B-FT", "dataset": "FewNERD",
32	    },
33	    "LLaMA_SciERC": {
34	        "path": f"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl",
35	        "model": "LLaMA-3.1-8B-FT", "dataset": "SciERC",
36	    },
37	    "LLaMA_CoNLL": {
38	        "path": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
39	        "model": "LLaMA-3.1-8B-FT", "dataset": "CoNLL",
40	    },
41	    "LLaMA_FewNERD": {
42	        "path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
43	        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD",
44	    },
45	}
46	
47	METHODS = ["majority_vote", "lp_weighted", "vc_weighted", "sj_weighted", "theta2n", "uniform"]
48	
49	# ---- helpers ----
50	
51	def entity_set(entities):
52	    return {(e["start"], e["end"], e["type"]) for e in entities}
53	
54	def load_data(path, gold_filter=True):
55	    instances = []
56	    with open(path) as f:
57	        for line in f:
58	            if not line.strip():
59	                continue
60	            obj = json.loads(line)
61	            if gold_filter and not obj["gold"].get("entities", []):
62	                continue
63	            instances.append(obj)
64	    return instances
65	
66	# ---- weight functions ----
67	
68	def get_lp_weights(samples, inst):
69	    logprobs_list = inst.get("logprobs", None)
70	    lps = []
71	    for i, s in enumerate(samples):
72	        lp = s.get("mean_logprob", None)
73	        if lp is None and logprobs_list is not None and i < len(logprobs_list):
74	            lp = logprobs_list[i]
75	        if lp is None or not math.isfinite(lp):
76	            lp = -100.0
77	        lps.append(lp)
78	    max_lp = max(lps)
79	    ws = [math.exp(lp - max_lp) for lp in lps]
80	    total = sum(ws)
81	    if total == 0:
82	        return [1.0 / len(samples)] * len(samples)
83	    return [w / total for w in ws]
84	
85	def get_vc_weights(samples):
86	    N = len(samples)
87	    entity_counts = Counter()
88	    for s in samples:
89	        seen = set()
90	        for e in s.get("entities", []):
91	            key = (e["start"], e["end"], e["type"])
92	            if key not in seen:
93	                entity_counts[key] += 1
94	                seen.add(key)
95	    weights = []
96	    for s in samples:
97	        ents = set()
98	        for e in s.get("entities", []):
99	            ents.add((e["start"], e["end"], e["type"]))
100	        if ents:
101	            w = sum(entity_counts[k] for k in ents) / (N * len(ents))
102	        else:
103	            w = 1.0 / N
104	        weights.append(w)
105	    total = sum(weights)
106	    if total == 0:
107	        return [1.0 / N] * N
108	    return [w / total for w in weights]
109	
110	def get_sj_weights(samples):
111	    N = len(samples)
112	    sets = []
113	    for s in samples:
114	        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
115	        sets.append(es)
116	    weights = []
117	    for i in range(N):
118	        if N == 1:
119	            weights.append(1.0)
120	            continue
121	        total_j = 0.0
122	        for j in range(N):
123	            if j == i:
124	                continue
125	            a, b = sets[i], sets[j]
126	            if not a and not b:
127	                total_j += 1.0
128	            elif not a or not b:
129	                pass
130	            else:
131	                total_j += len(a & b) / len(a | b)
132	        weights.append(total_j / (N - 1))
133	    total = sum(weights)
134	    if total == 0:
135	        return [1.0 / N] * N
136	    return [w / total for w in weights]
137	
138	# ---- construction ----
139	
140	def weighted_construction(samples, threshold, weights=None):
141	    entity_counts = defaultdict(float)
142	    N = len(samples)
143	    for i, sample in enumerate(samples):
144	        w = weights[i] if weights is not None else 1.0
145	        seen = set()
146	        for e in sample.get("entities", []):
147	            key = (e["start"], e["end"], e["type"])
148	            if key not in seen:
149	                entity_counts[key] += w
150	                seen.add(key)
151	    total_weight = sum(weights) if weights is not None else N
152	    constructed = set()
153	    for key, count in entity_counts.items():
154	        if count / total_weight >= threshold:
155	            constructed.add(key)
156	    return constructed
157	
158	# ---- evaluation ----
159	
160	def evaluate_instance(inst, n, method):
161	    """Return (tp, fp, fn) for one instance at sample size n."""
162	    samples = inst["samples"][:n]
163	    gold = entity_set(inst["gold"]["entities"])
164	
165	    if method == "majority_vote":
166	        pred = weighted_construction(samples, threshold=0.5)
167	    elif method == "lp_weighted":
168	        ws = get_lp_weights(samples, inst)
169	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
170	    elif method == "vc_weighted":
171	        ws = get_vc_weights(samples)
172	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
173	    elif method == "sj_weighted":
174	        ws = get_sj_weights(samples)
175	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
176	    elif method == "theta2n":
177	        pred = weighted_construction(samples, threshold=2.0/n)
178	    elif method == "uniform":
179	        pred = weighted_construction(samples, threshold=0.25)
180	    elif method == "greedy":
181	        pred = entity_set(inst["greedy"]["entities"])
182	    else:
183	        raise ValueError(f"Unknown: {method}")
184	
185	    tp = len(pred & gold)
186	    fp = len(pred - gold)
187	    fn = len(gold - pred)
188	    return tp, fp, fn
189	
190	def micro_f1_from_tuples(tuples):
191	    tp = sum(t[0] for t in tuples)
192	    fp = sum(t[1] for t in tuples)
193	    fn = sum(t[2] for t in tuples)
194	    if tp == 0:
195	        return 0.0
196	    p = tp / (tp + fp)
197	    r = tp / (tp + fn)
198	    return 2 * p * r / (p + r)
199	
200	def micro_prf_from_tuples(tuples):
201	    tp = sum(t[0] for t in tuples)
202	    fp = sum(t[1] for t in tuples)
203	    fn = sum(t[2] for t in tuples)
204	    if tp == 0:
205	        return 0.0, 0.0, 0.0
206	    p = tp / (tp + fp)
207	    r = tp / (tp + fn)
208	    f = 2 * p * r / (p + r)
209	    return p, r, f
210	
211	# ---- bootstrap ----
212	
213	def bootstrap_test(arr_n1, arr_n2, B=10000):
214	    """Paired bootstrap for micro F1 difference (n2 - n1)."""
215	    n = len(arr_n1)
216	    assert n == len(arr_n2)
217	
218	    a1 = np.array(arr_n1, dtype=np.int64)
219	    a2 = np.array(arr_n2, dtype=np.int64)
220	
221	    s1 = a1.sum(axis=0)
222	    s2 = a2.sum(axis=0)
223	    def _f1(s):
224	        tp, fp, fn = s[0], s[1], s[2]
225	        if tp == 0: return 0.0
226	        p = tp / (tp + fp); r = tp / (tp + fn)
227	        return 2*p*r/(p+r)
228	
229	    obs_diff = _f1(s2) - _f1(s1)
230	
231	    rng = np.random.RandomState(42)
232	    diffs = np.empty(B)
233	    for b in range(B):
234	        idx = rng.randint(0, n, size=n)
235	        bs1 = a1[idx].sum(axis=0)
236	        bs2 = a2[idx].sum(axis=0)
237	        diffs[b] = _f1(bs2) - _f1(bs1)
238	
239	    ci = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)))
240	    p_value = float(np.mean(diffs >= 0))  # H1: diff < 0 (inverse scaling)
241	    return {
242	        "obs_diff": float(obs_diff),
243	        "ci_95": ci,
244	        "p_value_inverse": p_value,  # small => significant inverse scaling
245	    }
246	
247	# ---- degeneracy ----
248	
249	def compute_degeneracy(instances, n):
250	    n_degen = 0
251	    for inst in instances:
252	        samples = inst["samples"][:n]
253	        esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
254	                 for s in samples]
255	        if len(set(esets)) == 1:
256	            n_degen += 1
257	    return n_degen / len(instances)
258	
259	# ---- main ----
260	
261	def main():
262	    os.makedirs(OUTPUT_DIR, exist_ok=True)
263	
264	    f1_by_n = {}
265	    inverse_summary = {}
266	
267	    for cfg_name, cfg in CONFIGS.items():
268	        path = cfg["path"]
269	        if not os.path.exists(path):
270	            print(f"SKIP {cfg_name}: {path} not found", flush=True)
271	            continue
272	
273	        print(f"\n{'='*70}", flush=True)
274	        print(f"  {cfg_name}  ({cfg['model']} / {cfg['dataset']})", flush=True)
275	        print(f"{'='*70}", flush=True)
276	
277	        t0 = time.time()
278	        instances = load_data(path, gold_filter=True)
279	        max_n = len(instances[0]["samples"])
280	        print(f"  Loaded {len(instances)} instances, N_max={max_n}  ({time.time()-t0:.1f}s)", flush=True)
281	
282	        n_vals = sorted(set(n for n in [2, 4, 6, 8, 16] if n <= max_n))
283	
284	        # greedy baseline
285	        greedy_tuples = [evaluate_instance(inst, max_n, "greedy") for inst in instances]
286	        greedy_f1 = micro_f1_from_tuples(greedy_tuples)
287	        print(f"  Greedy F1: {greedy_f1:.4f}", flush=True)
288	
289	        # pre-compute all (method, n) -> list of (tp, fp, fn)
290	        precomputed = {}
291	        for method in METHODS:
292	            for n in n_vals:
293	                t1 = time.time()
294	                tuples = [evaluate_instance(inst, n, method) for inst in instances]
295	                f1 = micro_f1_from_tuples(tuples)
296	                p, r, _ = micro_prf_from_tuples(tuples)
297	                precomputed[(method, n)] = {"tuples": tuples, "f1": f1, "p": p, "r": r}
298	                elapsed = time.time() - t1
299	                if elapsed > 2:
300	                    print(f"    {method} N={n}: F1={f1:.4f} ({elapsed:.1f}s)", flush=True)
301	
302	        # build result structure
303	        config_result = {
304	            "model": cfg["model"], "dataset": cfg["dataset"],
305	            "n_instances": len(instances), "max_n": max_n,
306	            "greedy_f1": greedy_f1, "N_values": n_vals,
307	            "methods": {},
308	        }
309	
310	        # degeneracy
311	        degen = {}
312	        for n in n_vals:
313	            degen[str(n)] = compute_degeneracy(instances, n)
314	        config_result["degeneracy_by_n"] = degen
315	
316	        print(f"\n  {'Method':<18}", end="", flush=True)
317	        for n in n_vals:
318	            print(f"  N={n:>2}", end="", flush=True)
319	        print("  Behavior", flush=True)
320	        print(f"  {'-'*75}", flush=True)
321	
322	        for method in METHODS:
323	            f1_dict = {}
324	            prf_dict = {}
325	            for n in n_vals:
326	                d = precomputed[(method, n)]
327	                f1_dict[str(n)] = d["f1"]
328	                prf_dict[str(n)] = {"P": d["p"], "R": d["r"], "F1": d["f1"]}
329	
330	            # classify behavior
331	            f1_list = [f1_dict[str(n)] for n in n_vals]
332	            has_drop = any(f1_list[i] - f1_list[i+1] > 0.001 for i in range(len(f1_list)-1))
333	            is_plateau = all(abs(f1_list[i] - f1_list[i+1]) <= 0.001 for i in range(len(f1_list)-1))
334	            if has_drop:
335	                behavior = "inverse_scaling"
336	            elif is_plateau:
337	                behavior = "plateau"
338	            else:
339	                behavior = "monotonic_increasing"
340	
341	            config_result["methods"][method] = {
342	                "f1_by_n": f1_dict,
343	                "prf_by_n": prf_dict,
344	                "behavior": behavior,
345	            }
346	
347	            vals = "  ".join(f"{f1_dict[str(n)]:.4f}" for n in n_vals)
348	            marker = " <<<" if behavior == "inverse_scaling" else ""
349	            print(f"  {method:<18} {vals}  {behavior}{marker}", flush=True)
350	
351	        print(f"  {'Degeneracy':<18}", end="", flush=True)
352	        print("  ".join(f"{degen[str(n)]:.3f}" for n in n_vals), flush=True)
353	
354	        # detect inverse scaling cases and run bootstrap
355	        inverse_cases = []
356	        for method in METHODS:
357	            f1s = config_result["methods"][method]["f1_by_n"]
358	            for i in range(len(n_vals) - 1):
359	                n1, n2 = n_vals[i], n_vals[i+1]
360	                drop = f1s[str(n1)] - f1s[str(n2)]
361	                if drop > 0.001:
362	                    case = {
363	                        "method": method, "n1": n1, "n2": n2,
364	                        "f1_n1": f1s[str(n1)], "f1_n2": f1s[str(n2)],
365	                        "drop_pp": drop * 100,
366	                    }
367	                    # bootstrap
368	                    B = 5000 if len(instances) > 10000 else 10000
369	                    bt = bootstrap_test(
370	                        precomputed[(method, n1)]["tuples"],
371	                        precomputed[(method, n2)]["tuples"],
372	                        B=B,
373	                    )
374	                    case["bootstrap"] = bt
375	                    case["significant"] = bt["ci_95"][1] < 0  # entire CI below 0
376	                    inverse_cases.append(case)
377	
378	        if inverse_cases:
379	            print(f"\n  ** {len(inverse_cases)} INVERSE SCALING TRANSITION(S) **", flush=True)
380	            n_sig = sum(1 for c in inverse_cases if c["significant"])
381	            print(f"  {n_sig} significant (95% CI entirely below 0)", flush=True)
382	            for c in inverse_cases:
383	                sig = "SIG" if c["significant"] else "ns"
384	                ci = c["bootstrap"]["ci_95"]
385	                print(f"    {c['method']:<18} N={c['n1']}→{c['n2']}: "
386	                      f"{c['f1_n1']:.4f}→{c['f1_n2']:.4f} (↓{c['drop_pp']:.2f}pp)  "
387	                      f"CI=[{ci[0]*100:+.2f},{ci[1]*100:+.2f}]pp  {sig}", flush=True)
388	        else:
389	            print(f"\n  No inverse scaling transitions detected.", flush=True)
390	
391	        config_result["inverse_cases"] = inverse_cases
392	        f1_by_n[cfg_name] = config_result
393	
394	        inverse_summary[cfg_name] = {
395	            "model": cfg["model"], "dataset": cfg["dataset"],
396	            "n_instances": len(instances), "max_n": max_n,
397	            "greedy_f1": greedy_f1,
398	            "method_behaviors": {m: config_result["methods"][m]["behavior"] for m in METHODS},
399	            "n_inverse_transitions": len(inverse_cases),
400	            "n_significant": sum(1 for c in inverse_cases if c["significant"]),
401	            "inverse_cases": inverse_cases,
402	            "degeneracy_by_n": degen,
403	        }
404	
405	        print(f"  Total time: {time.time()-t0:.1f}s", flush=True)
406	
407	    # ---- save ----
408	    with open(os.path.join(OUTPUT_DIR, "f1_by_n.json"), "w") as f:
409	        # strip large tuples before saving
410	        save_data = {}
411	        for k, v in f1_by_n.items():
412	            sv = dict(v)
413	            for m in sv.get("methods", {}):
414	                sv["methods"][m] = {kk: vv for kk, vv in sv["methods"][m].items()}
415	            save_data[k] = sv
416	        json.dump(save_data, f, indent=2)
417	    print(f"\nSaved f1_by_n.json", flush=True)
418	
419	    with open(os.path.join(OUTPUT_DIR, "inverse_scaling_summary.json"), "w") as f:
420	        json.dump(inverse_summary, f, indent=2)
421	    print(f"Saved inverse_scaling_summary.json", flush=True)
422	
423	    # ---- summary stats ----
424	    total_configs = len(inverse_summary)
425	    total_transitions = sum(s["n_inverse_transitions"] for s in inverse_summary.values())
426	    total_sig = sum(s["n_significant"] for s in inverse_summary.values())
427	
428	    print(f"\n{'='*70}", flush=True)
429	    print(f"GLOBAL SUMMARY", flush=True)
430	    print(f"{'='*70}", flush=True)
431	    print(f"Configs analyzed: {total_configs}", flush=True)
432	    print(f"Total inverse scaling transitions: {total_transitions}", flush=True)
433	    print(f"Statistically significant: {total_sig}", flush=True)
434	
435	    # method-level summary
436	    method_inverse = {m: 0 for m in METHODS}
437	    method_sig = {m: 0 for m in METHODS}
438	    for s in inverse_summary.values():
439	        for c in s["inverse_cases"]:
440	            method_inverse[c["method"]] += 1
441	            if c["significant"]:
442	                method_sig[c["method"]] += 1
443	
444	    print(f"\nPer-method summary:", flush=True)
445	    print(f"  {'Method':<18} {'Inverse':>8} {'Signif':>8}", flush=True)
446	    for m in METHODS:
447	        print(f"  {m:<18} {method_inverse[m]:>8} {method_sig[m]:>8}", flush=True)
448	
449	    # ---- plot ----
450	    try:
451	        import matplotlib
452	        matplotlib.use("Agg")
453	        import matplotlib.pyplot as plt
454	
455	        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
456	        fig.suptitle("F1 vs N by Construction Method", fontsize=14, fontweight="bold")
457	
458	        colors = {
459	            "majority_vote": "#e41a1c", "lp_weighted": "#377eb8",
460	            "vc_weighted": "#4daf4a", "sj_weighted": "#984ea3",
461	            "theta2n": "#ff7f00", "uniform": "#a65628",
462	        }
463	        markers = {
464	            "majority_vote": "o", "lp_weighted": "s",
465	            "vc_weighted": "D", "sj_weighted": "^",
466	            "theta2n": "v", "uniform": "P",
467	        }
468	
469	        config_order = ["Qwen_SciERC", "Qwen_CoNLL", "Qwen_FewNERD",
470	                        "LLaMA_SciERC", "LLaMA_CoNLL", "LLaMA_FewNERD"]
471	
472	        for idx, cfg_name in enumerate(config_order):
473	            ax = axes[idx // 3][idx % 3]
474	            if cfg_name not in f1_by_n:
475	                ax.set_title(f"{cfg_name} (no data)")
476	                continue
477	
478	            data = f1_by_n[cfg_name]
479	            n_vals = data["N_values"]
480	
481	            # greedy reference
482	            ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
483	                       linewidth=1, alpha=0.7, label="greedy")
484	
485	            for method in METHODS:
486	                md = data["methods"][method]
487	                f1s = [md["f1_by_n"][str(n)] for n in n_vals]
488	                is_inv = md["behavior"] == "inverse_scaling"
489	                lw = 2.5 if is_inv else 1.5
490	                ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],
491	                        linewidth=lw, markersize=6, label=method,
492	                        linestyle="-" if not is_inv else "-")
493	
494	                # mark inverse drops
495	                if is_inv:
496	                    for i in range(len(n_vals)-1):
497	                        if f1s[i] - f1s[i+1] > 0.001:
498	                            ax.annotate("", xy=(n_vals[i+1], f1s[i+1]),
499	                                        xytext=(n_vals[i], f1s[i]),
500	                                        arrowprops=dict(arrowstyle="->", color="red",
501	                                                       lw=2, alpha=0.6))
502	
503	            ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
504	            ax.set_xlabel("N (samples)")
505	            ax.set_ylabel("Entity Micro F1")
506	            ax.set_xticks(n_vals)
507	            ax.grid(True, alpha=0.3)
508	            ax.set_ylim(bottom=max(0, min(data["greedy_f1"] - 0.15,
509	                        min(md["f1_by_n"][str(n)] for m, md in data["methods"].items()
510	                            for n in n_vals if str(n) in md["f1_by_n"]) - 0.02)))
511	
512	        # shared legend
513	        handles, labels = axes[0][0].get_legend_handles_labels()
514	        fig.legend(handles, labels, loc="lower center", ncol=7, fontsize=9,
515	                   bbox_to_anchor=(0.5, -0.02))
516	        plt.tight_layout(rect=[0, 0.04, 1, 0.96])
517	        fig_path = os.path.join(OUTPUT_DIR, "f1_vs_n_all_configs.png")
518	        plt.savefig(fig_path, dpi=150, bbox_inches="tight")
519	        print(f"\nSaved plot: {fig_path}", flush=True)
520	        plt.close()
521	
522	        # detailed plot for inverse scaling cases only
523	        inv_configs = [k for k, v in inverse_summary.items() if v["n_inverse_transitions"] > 0]
524	        if inv_configs:
525	            n_inv = len(inv_configs)
526	            fig2, axes2 = plt.subplots(1, n_inv, figsize=(7*n_inv, 5))
527	            if n_inv == 1:
528	                axes2 = [axes2]
529	            fig2.suptitle("Inverse Scaling Cases (F1 vs N)", fontsize=13, fontweight="bold")
530	
531	            for i, cfg_name in enumerate(inv_configs):
532	                ax = axes2[i]
533	                data = f1_by_n[cfg_name]
534	                n_vals = data["N_values"]
535	
536	                ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
537	                           linewidth=1, alpha=0.7, label="greedy")
538	
539	                inv_methods = set(c["method"] for c in data["inverse_cases"])
540	                for method in METHODS:
541	                    md = data["methods"][method]
542	                    f1s = [md["f1_by_n"][str(n)] for n in n_vals]
543	                    alpha = 1.0 if method in inv_methods else 0.3
544	                    lw = 2.5 if method in inv_methods else 1.0
545	                    ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],
546	                            linewidth=lw, markersize=7 if method in inv_methods else 4,
547	                            label=method, alpha=alpha)
548	
549	                    if method in inv_methods:
550	                        for j in range(len(n_vals)-1):
551	                            if f1s[j] - f1s[j+1] > 0.001:
552	                                sig_cases = [c for c in data["inverse_cases"]
553	                                            if c["method"] == method and c["n1"] == n_vals[j]]
554	                                is_sig = any(c["significant"] for c in sig_cases)
555	                                marker_txt = f"↓{(f1s[j]-f1s[j+1])*100:.1f}pp"
556	                                if is_sig:
557	                                    marker_txt += "*"
558	                                mid_x = (n_vals[j] + n_vals[j+1]) / 2
559	                                mid_y = (f1s[j] + f1s[j+1]) / 2
560	                                ax.annotate(marker_txt, xy=(mid_x, mid_y),
561	                                           fontsize=8, color="red", fontweight="bold",
562	                                           ha="center", va="bottom")
563	
564	                ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
565	                ax.set_xlabel("N (samples)")
566	                ax.set_ylabel("Entity Micro F1")
567	                ax.set_xticks(n_vals)
568	                ax.grid(True, alpha=0.3)
569	                ax.legend(fontsize=8, loc="best")
570	
571	            plt.tight_layout()
572	            fig2_path = os.path.join(OUTPUT_DIR, "inverse_scaling_detail.png")
573	            plt.savefig(fig2_path, dpi=150, bbox_inches="tight")
574	            print(f"Saved detail plot: {fig2_path}", flush=True)
575	            plt.close()
576	
577	    except Exception as e:
578	        print(f"Plotting error (non-fatal): {e}", flush=True)
579	
580	    # ---- analysis.md ----
581	    lines = ["# Inverse Scaling Analysis for Structured Self-Consistency\n"]
582	    lines.append(f"Date: {time.strftime('%Y-%m-%d')}\n")
583	    lines.append("## Question\n")
584	    lines.append("Does increasing the number of samples N ever *decrease* entity-level F1 ")
585	    lines.append("for any construction method? If so, which methods and under what conditions?\n")
586	
587	    lines.append("\n## Setup\n")
588	    lines.append(f"- Configs: {total_configs} (2 models × 3 datasets)\n")
589	    lines.append(f"- Methods: {', '.join(METHODS)}\n")
590	    lines.append("- Threshold: majority_vote uses θ=0.5 (fixed); lp/vc/sj_weighted and theta2n use θ=2/N (adaptive); uniform uses θ=0.25 (fixed)\n")
591	    lines.append("- Metric: entity-level micro F1 (pooled TP/FP/FN)\n")
592	    lines.append("- Significance: paired bootstrap (B=5000-10000), 95% CI\n")
593	
594	    lines.append("\n## Results\n")
595	    if total_transitions == 0:
596	        lines.append("**No inverse scaling detected in any configuration.**\n")
597	        lines.append("All methods show monotonically increasing or plateau behavior as N grows.\n")
598	    else:
599	        lines.append(f"**{total_transitions} inverse scaling transitions detected, {total_sig} statistically significant.**\n")
600	        lines.append("\n### Inverse Scaling Cases\n")
601	        lines.append("| Config | Method | N₁→N₂ | F1(N₁) | F1(N₂) | Drop | 95% CI | Sig? |\n")
602	        lines.append("|--------|--------|--------|--------|--------|------|--------|------|\n")
603	        for cfg_name, s in inverse_summary.items():
604	            for c in s["inverse_cases"]:
605	                ci = c["bootstrap"]["ci_95"]
606	                sig = "**YES**" if c["significant"] else "no"
607	                lines.append(
608	                    f"| {cfg_name} | {c['method']} | {c['n1']}→{c['n2']} | "
609	                    f"{c['f1_n1']:.4f} | {c['f1_n2']:.4f} | "
610	                    f"{c['drop_pp']:.2f}pp | [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] | {sig} |\n"
611	                )
612	
613	    lines.append("\n### Method Behavior Summary\n")
614	    lines.append("| Config | " + " | ".join(METHODS) + " |\n")
615	    lines.append("|--------" + "|--------" * len(METHODS) + "|\n")
616	    for cfg_name, s in inverse_summary.items():
617	        cells = []
618	        for m in METHODS:
619	            b = s["method_behaviors"][m]
620	            if b == "inverse_scaling":
621	                cells.append("**INVERSE**")
622	            elif b == "plateau":
623	                cells.append("plateau")
624	            else:
625	                cells.append("↑ mono")
626	        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")
627	
628	    lines.append("\n### Degeneracy by N\n")
629	    lines.append("| Config |" + " | ".join(f"N={n}" for n in [2,4,6,8,16]) + " |\n")
630	    lines.append("|--------" + "|------" * 5 + "|\n")
631	    for cfg_name, s in inverse_summary.items():
632	        cells = []
633	        for n in [2,4,6,8,16]:
634	            d = s["degeneracy_by_n"].get(str(n), None)
635	            cells.append(f"{d:.1%}" if d is not None else "—")
636	        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")
637	
638	    lines.append("\n## Mechanism Analysis\n")
639	    if total_transitions > 0:
640	        # check which methods show inverse scaling
641	        inv_methods = set()
642	        for s in inverse_summary.values():
643	            for c in s["inverse_cases"]:
644	                inv_methods.add(c["method"])
645	
646	        fixed_theta = inv_methods & {"majority_vote", "uniform"}
647	        adaptive_theta = inv_methods & {"lp_weighted", "vc_weighted", "sj_weighted", "theta2n"}
648	
649	        if fixed_theta and not adaptive_theta:
650	            lines.append("Inverse scaling occurs **only in fixed-threshold methods** (")
651	            lines.append(", ".join(sorted(fixed_theta)))
652	            lines.append("). Adaptive-threshold methods (θ=2/N) are immune.\n\n")
653	            lines.append("**Mechanism**: With fixed θ, the effective vote requirement scales with N. ")
654	            lines.append("At θ=0.5, an entity needs >N/2 votes. As N grows, correct-but-variable entities ")
655	            lines.append("fail to reach this threshold, causing recall degradation that outweighs ")
656	            lines.append("the precision benefits of additional samples.\n")
657	        elif adaptive_theta:
658	            lines.append("Inverse scaling occurs even in adaptive-threshold methods: ")
659	            lines.append(", ".join(sorted(adaptive_theta)))
660	            lines.append(". This suggests the issue goes beyond threshold choice.\n\n")
661	            lines.append("Possible mechanisms: (1) weight distortion at intermediate N; ")
662	            lines.append("(2) interaction between signal quality and N; ")
663	            lines.append("(3) boundary effects in entity aggregation.\n")
664	        else:
665	            lines.append("No clear pattern in affected methods.\n")
666	    else:
667	        lines.append("No inverse scaling detected. The construction methods are robust to increasing N.\n\n")
668	        lines.append("This is expected for adaptive-threshold methods (θ=2/N): as N grows, ")
669	        lines.append("the threshold decreases, compensating for any dilution of correct-but-rare entities. ")
670	        lines.append("For fixed-threshold methods (θ=0.5, θ=0.25), the monotonic increase suggests ")
671	        lines.append("that additional samples consistently improve the precision-recall tradeoff.\n")
672	
673	    lines.append("\n## Conclusion\n")
674	    if total_sig > 0:
675	        lines.append(f"We find {total_sig} statistically significant inverse scaling case(s). ")
676	        lines.append("This is the first reported inverse scaling finding in structured self-consistency. ")
677	        lines.append("The finding has implications for practitioners choosing aggregation methods ")
678	        lines.append("and sample budgets.\n")
679	    elif total_transitions > 0:
680	        lines.append(f"We observe {total_transitions} inverse scaling transition(s), but none ")
681	        lines.append("are statistically significant. The drops are within noise range.\n")
682	    else:
683	        lines.append("No inverse scaling is observed. Construction F1 monotonically increases ")
684	        lines.append("(or plateaus) with N across all tested configurations. ")
685	        lines.append("Structured self-consistency with entity-level construction is robust to sample budget.\n")
686	
687	    with open(os.path.join(OUTPUT_DIR, "analysis.md"), "w") as f:
688	        f.writelines(lines)
689	    print(f"Saved analysis.md", flush=True)
690	
691	    print("\nDONE", flush=True)
692	
693	
694	if __name__ == "__main__":
695	    main()
696	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "5bd2a4fe-816e-45db-b367-7d473947e76e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Inverse scaling test: check if F1 decreases as N increases for construction methods.\n\nFor each dataset×model×method, sub-sample N=16 (or N=8) samples to N=2,4,6,8,(16),\ncompute entity-level micro F1, detect inverse scaling (F1 drop > 0.1pp),\nand run paired bootstrap significance tests.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport sys\nimport time\nimport numpy as np\nfrom collections import defaultdict, Counter\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie\"\nOUTPUT_DIR = f\"{BASE}/artifacts/n_inverse_scaling\"\n\nCONFIGS = {\n    \"Qwen_SciERC\": {\n        \"path\": f\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\",\n        \"model\": \"Qwen3-8B-FT\", \"dataset\": \"SciERC\",\n    },\n    \"Qwen_CoNLL\": {\n        \"path\": f\"{BASE}/output/exp_002_conll_n16/samples.jsonl\",\n        \"model\": \"Qwen3-8B-FT\", \"dataset\": \"CoNLL\",\n    },\n    \"Qwen_FewNERD\": {\n        \"path\": f\"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl\",\n        \"model\": \"Qwen3-8B-FT\", \"dataset\": \"FewNERD\",\n    },\n    \"LLaMA_SciERC\": {\n        \"path\": f\"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl\",\n        \"model\": \"LLaMA-3.1-8B-FT\", \"dataset\": \"SciERC\",\n    },\n    \"LLaMA_CoNLL\": {\n        \"path\": f\"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl\",\n        \"model\": \"LLaMA-3.1-8B-FT\", \"dataset\": \"CoNLL\",\n    },\n    \"LLaMA_FewNERD\": {\n        \"path\": f\"{BASE}/output/llama_fewnerd_s42/samples.jsonl\",\n        \"model\": \"LLaMA-3.1-8B-FT\", \"dataset\": \"FewNERD\",\n    },\n}\n\nMETHODS = [\"majority_vote\", \"lp_weighted\", \"vc_weighted\", \"sj_weighted\", \"theta2n\", \"uniform\"]\n\n# ---- helpers ----\n\ndef entity_set(entities):\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\ndef load_data(path, gold_filter=True):\n    instances = []\n    with open(path) as f:\n        for line in f:\n            if not line.strip():\n                continue\n            obj = json.loads(line)\n            if gold_filter and not obj[\"gold\"].get(\"entities\", []):\n                continue\n            instances.append(obj)\n    return instances\n\n# ---- weight functions ----\n\ndef get_lp_weights(samples, inst):\n    logprobs_list = inst.get(\"logprobs\", None)\n    lps = []\n    for i, s in enumerate(samples):\n        lp = s.get(\"mean_logprob\", None)\n        if lp is None and logprobs_list is not None and i < len(logprobs_list):\n            lp = logprobs_list[i]\n        if lp is None or not math.isfinite(lp):\n            lp = -100.0\n        lps.append(lp)\n    max_lp = max(lps)\n    ws = [math.exp(lp - max_lp) for lp in lps]\n    total = sum(ws)\n    if total == 0:\n        return [1.0 / len(samples)] * len(samples)\n    return [w / total for w in ws]\n\ndef get_vc_weights(samples):\n    N = len(samples)\n    entity_counts = Counter()\n    for s in samples:\n        seen = set()\n        for e in s.get(\"entities\", []):\n            key = (e[\"start\"], e[\"end\"], e[\"type\"])\n            if key not in seen:\n                entity_counts[key] += 1\n                seen.add(key)\n    weights = []\n    for s in samples:\n        ents = set()\n        for e in s.get(\"entities\", []):\n            ents.add((e[\"start\"], e[\"end\"], e[\"type\"]))\n        if ents:\n            w = sum(entity_counts[k] for k in ents) / (N * len(ents))\n        else:\n            w = 1.0 / N\n        weights.append(w)\n    total = sum(weights)\n    if total == 0:\n        return [1.0 / N] * N\n    return [w / total for w in weights]\n\ndef get_sj_weights(samples):\n    N = len(samples)\n    sets = []\n    for s in samples:\n        es = frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n        sets.append(es)\n    weights = []\n    for i in range(N):\n        if N == 1:\n            weights.append(1.0)\n            continue\n        total_j = 0.0\n        for j in range(N):\n            if j == i:\n                continue\n            a, b = sets[i], sets[j]\n            if not a and not b:\n                total_j += 1.0\n            elif not a or not b:\n                pass\n            else:\n                total_j += len(a & b) / len(a | b)\n        weights.append(total_j / (N - 1))\n    total = sum(weights)\n    if total == 0:\n        return [1.0 / N] * N\n    return [w / total for w in weights]\n\n# ---- construction ----\n\ndef weighted_construction(samples, threshold, weights=None):\n    entity_counts = defaultdict(float)\n    N = len(samples)\n    for i, sample in enumerate(samples):\n        w = weights[i] if weights is not None else 1.0\n        seen = set()\n        for e in sample.get(\"entities\", []):\n            key = (e[\"start\"], e[\"end\"], e[\"type\"])\n            if key not in seen:\n                entity_counts[key] += w\n                seen.add(key)\n    total_weight = sum(weights) if weights is not None else N\n    constructed = set()\n    for key, count in entity_counts.items():\n        if count / total_weight >= threshold:\n            constructed.add(key)\n    return constructed\n\n# ---- evaluation ----\n\ndef evaluate_instance(inst, n, method):\n    \"\"\"Return (tp, fp, fn) for one instance at sample size n.\"\"\"\n    samples = inst[\"samples\"][:n]\n    gold = entity_set(inst[\"gold\"][\"entities\"])\n\n    if method == \"majority_vote\":\n        pred = weighted_construction(samples, threshold=0.5)\n    elif method == \"lp_weighted\":\n        ws = get_lp_weights(samples, inst)\n        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)\n    elif method == \"vc_weighted\":\n        ws = get_vc_weights(samples)\n        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)\n    elif method == \"sj_weighted\":\n        ws = get_sj_weights(samples)\n        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)\n    elif method == \"theta2n\":\n        pred = weighted_construction(samples, threshold=2.0/n)\n    elif method == \"uniform\":\n        pred = weighted_construction(samples, threshold=0.25)\n    elif method == \"greedy\":\n        pred = entity_set(inst[\"greedy\"][\"entities\"])\n    else:\n        raise ValueError(f\"Unknown: {method}\")\n\n    tp = len(pred & gold)\n    fp = len(pred - gold)\n    fn = len(gold - pred)\n    return tp, fp, fn\n\ndef micro_f1_from_tuples(tuples):\n    tp = sum(t[0] for t in tuples)\n    fp = sum(t[1] for t in tuples)\n    fn = sum(t[2] for t in tuples)\n    if tp == 0:\n        return 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    return 2 * p * r / (p + r)\n\ndef micro_prf_from_tuples(tuples):\n    tp = sum(t[0] for t in tuples)\n    fp = sum(t[1] for t in tuples)\n    fn = sum(t[2] for t in tuples)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / (tp + fp)\n    r = tp / (tp + fn)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n# ---- bootstrap ----\n\ndef bootstrap_test(arr_n1, arr_n2, B=10000):\n    \"\"\"Paired bootstrap for micro F1 difference (n2 - n1).\"\"\"\n    n = len(arr_n1)\n    assert n == len(arr_n2)\n\n    a1 = np.array(arr_n1, dtype=np.int64)\n    a2 = np.array(arr_n2, dtype=np.int64)\n\n    s1 = a1.sum(axis=0)\n    s2 = a2.sum(axis=0)\n    def _f1(s):\n        tp, fp, fn = s[0], s[1], s[2]\n        if tp == 0: return 0.0\n        p = tp / (tp + fp); r = tp / (tp + fn)\n        return 2*p*r/(p+r)\n\n    obs_diff = _f1(s2) - _f1(s1)\n\n    rng = np.random.RandomState(42)\n    diffs = np.empty(B)\n    for b in range(B):\n        idx = rng.randint(0, n, size=n)\n        bs1 = a1[idx].sum(axis=0)\n        bs2 = a2[idx].sum(axis=0)\n        diffs[b] = _f1(bs2) - _f1(bs1)\n\n    ci = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)))\n    p_value = float(np.mean(diffs >= 0))  # H1: diff < 0 (inverse scaling)\n    return {\n        \"obs_diff\": float(obs_diff),\n        \"ci_95\": ci,\n        \"p_value_inverse\": p_value,  # small => significant inverse scaling\n    }\n\n# ---- degeneracy ----\n\ndef compute_degeneracy(instances, n):\n    n_degen = 0\n    for inst in instances:\n        samples = inst[\"samples\"][:n]\n        esets = [frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n                 for s in samples]\n        if len(set(esets)) == 1:\n            n_degen += 1\n    return n_degen / len(instances)\n\n# ---- main ----\n\ndef main():\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\n\n    f1_by_n = {}\n    inverse_summary = {}\n\n    for cfg_name, cfg in CONFIGS.items():\n        path = cfg[\"path\"]\n        if not os.path.exists(path):\n            print(f\"SKIP {cfg_name}: {path} not found\", flush=True)\n            continue\n\n        print(f\"\\n{'='*70}\", flush=True)\n        print(f\"  {cfg_name}  ({cfg['model']} / {cfg['dataset']})\", flush=True)\n        print(f\"{'='*70}\", flush=True)\n\n        t0 = time.time()\n        instances = load_data(path, gold_filter=True)\n        max_n = len(instances[0][\"samples\"])\n        print(f\"  Loaded {len(instances)} instances, N_max={max_n}  ({time.time()-t0:.1f}s)\", flush=True)\n\n        n_vals = sorted(set(n for n in [2, 4, 6, 8, 16] if n <= max_n))\n\n        # greedy baseline\n        greedy_tuples = [evaluate_instance(inst, max_n, \"greedy\") for inst in instances]\n        greedy_f1 = micro_f1_from_tuples(greedy_tuples)\n        print(f\"  Greedy F1: {greedy_f1:.4f}\", flush=True)\n\n        # pre-compute all (method, n) -> list of (tp, fp, fn)\n        precomputed = {}\n        for method in METHODS:\n            for n in n_vals:\n                t1 = time.time()\n                tuples = [evaluate_instance(inst, n, method) for inst in instances]\n                f1 = micro_f1_from_tuples(tuples)\n                p, r, _ = micro_prf_from_tuples(tuples)\n                precomputed[(method, n)] = {\"tuples\": tuples, \"f1\": f1, \"p\": p, \"r\": r}\n                elapsed = time.time() - t1\n                if elapsed > 2:\n                    print(f\"    {method} N={n}: F1={f1:.4f} ({elapsed:.1f}s)\", flush=True)\n\n        # build result structure\n        config_result = {\n            \"model\": cfg[\"model\"], \"dataset\": cfg[\"dataset\"],\n            \"n_instances\": len(instances), \"max_n\": max_n,\n            \"greedy_f1\": greedy_f1, \"N_values\": n_vals,\n            \"methods\": {},\n        }\n\n        # degeneracy\n        degen = {}\n        for n in n_vals:\n            degen[str(n)] = compute_degeneracy(instances, n)\n        config_result[\"degeneracy_by_n\"] = degen\n\n        print(f\"\\n  {'Method':<18}\", end=\"\", flush=True)\n        for n in n_vals:\n            print(f\"  N={n:>2}\", end=\"\", flush=True)\n        print(\"  Behavior\", flush=True)\n        print(f\"  {'-'*75}\", flush=True)\n\n        for method in METHODS:\n            f1_dict = {}\n            prf_dict = {}\n            for n in n_vals:\n                d = precomputed[(method, n)]\n                f1_dict[str(n)] = d[\"f1\"]\n                prf_dict[str(n)] = {\"P\": d[\"p\"], \"R\": d[\"r\"], \"F1\": d[\"f1\"]}\n\n            # classify behavior\n            f1_list = [f1_dict[str(n)] for n in n_vals]\n            has_drop = any(f1_list[i] - f1_list[i+1] > 0.001 for i in range(len(f1_list)-1))\n            is_plateau = all(abs(f1_list[i] - f1_list[i+1]) <= 0.001 for i in range(len(f1_list)-1))\n            if has_drop:\n                behavior = \"inverse_scaling\"\n            elif is_plateau:\n                behavior = \"plateau\"\n            else:\n                behavior = \"monotonic_increasing\"\n\n            config_result[\"methods\"][method] = {\n                \"f1_by_n\": f1_dict,\n                \"prf_by_n\": prf_dict,\n                \"behavior\": behavior,\n            }\n\n            vals = \"  \".join(f\"{f1_dict[str(n)]:.4f}\" for n in n_vals)\n            marker = \" <<<\" if behavior == \"inverse_scaling\" else \"\"\n            print(f\"  {method:<18} {vals}  {behavior}{marker}\", flush=True)\n\n        print(f\"  {'Degeneracy':<18}\", end=\"\", flush=True)\n        print(\"  \".join(f\"{degen[str(n)]:.3f}\" for n in n_vals), flush=True)\n\n        # detect inverse scaling cases and run bootstrap\n        inverse_cases = []\n        for method in METHODS:\n            f1s = config_result[\"methods\"][method][\"f1_by_n\"]\n            for i in range(len(n_vals) - 1):\n                n1, n2 = n_vals[i], n_vals[i+1]\n                drop = f1s[str(n1)] - f1s[str(n2)]\n                if drop > 0.001:\n                    case = {\n                        \"method\": method, \"n1\": n1, \"n2\": n2,\n                        \"f1_n1\": f1s[str(n1)], \"f1_n2\": f1s[str(n2)],\n                        \"drop_pp\": drop * 100,\n                    }\n                    # bootstrap\n                    B = 5000 if len(instances) > 10000 else 10000\n                    bt = bootstrap_test(\n                        precomputed[(method, n1)][\"tuples\"],\n                        precomputed[(method, n2)][\"tuples\"],\n                        B=B,\n                    )\n                    case[\"bootstrap\"] = bt\n                    case[\"significant\"] = bt[\"ci_95\"][1] < 0  # entire CI below 0\n                    inverse_cases.append(case)\n\n        if inverse_cases:\n            print(f\"\\n  ** {len(inverse_cases)} INVERSE SCALING TRANSITION(S) **\", flush=True)\n            n_sig = sum(1 for c in inverse_cases if c[\"significant\"])\n            print(f\"  {n_sig} significant (95% CI entirely below 0)\", flush=True)\n            for c in inverse_cases:\n                sig = \"SIG\" if c[\"significant\"] else \"ns\"\n                ci = c[\"bootstrap\"][\"ci_95\"]\n                print(f\"    {c['method']:<18} N={c['n1']}→{c['n2']}: \"\n                      f\"{c['f1_n1']:.4f}→{c['f1_n2']:.4f} (↓{c['drop_pp']:.2f}pp)  \"\n                      f\"CI=[{ci[0]*100:+.2f},{ci[1]*100:+.2f}]pp  {sig}\", flush=True)\n        else:\n            print(f\"\\n  No inverse scaling transitions detected.\", flush=True)\n\n        config_result[\"inverse_cases\"] = inverse_cases\n        f1_by_n[cfg_name] = config_result\n\n        inverse_summary[cfg_name] = {\n            \"model\": cfg[\"model\"], \"dataset\": cfg[\"dataset\"],\n            \"n_instances\": len(instances), \"max_n\": max_n,\n            \"greedy_f1\": greedy_f1,\n            \"method_behaviors\": {m: config_result[\"methods\"][m][\"behavior\"] for m in METHODS},\n            \"n_inverse_transitions\": len(inverse_cases),\n            \"n_significant\": sum(1 for c in inverse_cases if c[\"significant\"]),\n            \"inverse_cases\": inverse_cases,\n            \"degeneracy_by_n\": degen,\n        }\n\n        print(f\"  Total time: {time.time()-t0:.1f}s\", flush=True)\n\n    # ---- save ----\n    with open(os.path.join(OUTPUT_DIR, \"f1_by_n.json\"), \"w\") as f:\n        # strip large tuples before saving\n        save_data = {}\n        for k, v in f1_by_n.items():\n            sv = dict(v)\n            for m in sv.get(\"methods\", {}):\n                sv[\"methods\"][m] = {kk: vv for kk, vv in sv[\"methods\"][m].items()}\n            save_data[k] = sv\n        json.dump(save_data, f, indent=2)\n    print(f\"\\nSaved f1_by_n.json\", flush=True)\n\n    with open(os.path.join(OUTPUT_DIR, \"inverse_scaling_summary.json\"), \"w\") as f:\n        json.dump(inverse_summary, f, indent=2)\n    print(f\"Saved inverse_scaling_summary.json\", flush=True)\n\n    # ---- summary stats ----\n    total_configs = len(inverse_summary)\n    total_transitions = sum(s[\"n_inverse_transitions\"] for s in inverse_summary.values())\n    total_sig = sum(s[\"n_significant\"] for s in inverse_summary.values())\n\n    print(f\"\\n{'='*70}\", flush=True)\n    print(f\"GLOBAL SUMMARY\", flush=True)\n    print(f\"{'='*70}\", flush=True)\n    print(f\"Configs analyzed: {total_configs}\", flush=True)\n    print(f\"Total inverse scaling transitions: {total_transitions}\", flush=True)\n    print(f\"Statistically significant: {total_sig}\", flush=True)\n\n    # method-level summary\n    method_inverse = {m: 0 for m in METHODS}\n    method_sig = {m: 0 for m in METHODS}\n    for s in inverse_summary.values():\n        for c in s[\"inverse_cases\"]:\n            method_inverse[c[\"method\"]] += 1\n            if c[\"significant\"]:\n                method_sig[c[\"method\"]] += 1\n\n    print(f\"\\nPer-method summary:\", flush=True)\n    print(f\"  {'Method':<18} {'Inverse':>8} {'Signif':>8}\", flush=True)\n    for m in METHODS:\n        print(f\"  {m:<18} {method_inverse[m]:>8} {method_sig[m]:>8}\", flush=True)\n\n    # ---- plot ----\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n\n        fig, axes = plt.subplots(2, 3, figsize=(18, 10))\n        fig.suptitle(\"F1 vs N by Construction Method\", fontsize=14, fontweight=\"bold\")\n\n        colors = {\n            \"majority_vote\": \"#e41a1c\", \"lp_weighted\": \"#377eb8\",\n            \"vc_weighted\": \"#4daf4a\", \"sj_weighted\": \"#984ea3\",\n            \"theta2n\": \"#ff7f00\", \"uniform\": \"#a65628\",\n        }\n        markers = {\n            \"majority_vote\": \"o\", \"lp_weighted\": \"s\",\n            \"vc_weighted\": \"D\", \"sj_weighted\": \"^\",\n            \"theta2n\": \"v\", \"uniform\": \"P\",\n        }\n\n        config_order = [\"Qwen_SciERC\", \"Qwen_CoNLL\", \"Qwen_FewNERD\",\n                        \"LLaMA_SciERC\", \"LLaMA_CoNLL\", \"LLaMA_FewNERD\"]\n\n        for idx, cfg_name in enumerate(config_order):\n            ax = axes[idx // 3][idx % 3]\n            if cfg_name not in f1_by_n:\n                ax.set_title(f\"{cfg_name} (no data)\")\n                continue\n\n            data = f1_by_n[cfg_name]\n            n_vals = data[\"N_values\"]\n\n            # greedy reference\n            ax.axhline(y=data[\"greedy_f1\"], color=\"gray\", linestyle=\"--\",\n                       linewidth=1, alpha=0.7, label=\"greedy\")\n\n            for method in METHODS:\n                md = data[\"methods\"][method]\n                f1s = [md[\"f1_by_n\"][str(n)] for n in n_vals]\n                is_inv = md[\"behavior\"] == \"inverse_scaling\"\n                lw = 2.5 if is_inv else 1.5\n                ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],\n                        linewidth=lw, markersize=6, label=method,\n                        linestyle=\"-\" if not is_inv else \"-\")\n\n                # mark inverse drops\n                if is_inv:\n                    for i in range(len(n_vals)-1):\n                        if f1s[i] - f1s[i+1] > 0.001:\n                            ax.annotate(\"\", xy=(n_vals[i+1], f1s[i+1]),\n                                        xytext=(n_vals[i], f1s[i]),\n                                        arrowprops=dict(arrowstyle=\"->\", color=\"red\",\n                                                       lw=2, alpha=0.6))\n\n            ax.set_title(f\"{data['model']} / {data['dataset']}\", fontsize=11)\n            ax.set_xlabel(\"N (samples)\")\n            ax.set_ylabel(\"Entity Micro F1\")\n            ax.set_xticks(n_vals)\n            ax.grid(True, alpha=0.3)\n            ax.set_ylim(bottom=max(0, min(data[\"greedy_f1\"] - 0.15,\n                        min(md[\"f1_by_n\"][str(n)] for m, md in data[\"methods\"].items()\n                            for n in n_vals if str(n) in md[\"f1_by_n\"]) - 0.02)))\n\n        # shared legend\n        handles, labels = axes[0][0].get_legend_handles_labels()\n        fig.legend(handles, labels, loc=\"lower center\", ncol=7, fontsize=9,\n                   bbox_to_anchor=(0.5, -0.02))\n        plt.tight_layout(rect=[0, 0.04, 1, 0.96])\n        fig_path = os.path.join(OUTPUT_DIR, \"f1_vs_n_all_configs.png\")\n        plt.savefig(fig_path, dpi=150, bbox_inches=\"tight\")\n        print(f\"\\nSaved plot: {fig_path}\", flush=True)\n        plt.close()\n\n        # detailed plot for inverse scaling cases only\n        inv_configs = [k for k, v in inverse_summary.items() if v[\"n_inverse_transitions\"] > 0]\n        if inv_configs:\n            n_inv = len(inv_configs)\n            fig2, axes2 = plt.subplots(1, n_inv, figsize=(7*n_inv, 5))\n            if n_inv == 1:\n                axes2 = [axes2]\n            fig2.suptitle(\"Inverse Scaling Cases (F1 vs N)\", fontsize=13, fontweight=\"bold\")\n\n            for i, cfg_name in enumerate(inv_configs):\n                ax = axes2[i]\n                data = f1_by_n[cfg_name]\n                n_vals = data[\"N_values\"]\n\n                ax.axhline(y=data[\"greedy_f1\"], color=\"gray\", linestyle=\"--\",\n                           linewidth=1, alpha=0.7, label=\"greedy\")\n\n                inv_methods = set(c[\"method\"] for c in data[\"inverse_cases\"])\n                for method in METHODS:\n                    md = data[\"methods\"][method]\n                    f1s = [md[\"f1_by_n\"][str(n)] for n in n_vals]\n                    alpha = 1.0 if method in inv_methods else 0.3\n                    lw = 2.5 if method in inv_methods else 1.0\n                    ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],\n                            linewidth=lw, markersize=7 if method in inv_methods else 4,\n                            label=method, alpha=alpha)\n\n                    if method in inv_methods:\n                        for j in range(len(n_vals)-1):\n                            if f1s[j] - f1s[j+1] > 0.001:\n                                sig_cases = [c for c in data[\"inverse_cases\"]\n                                            if c[\"method\"] == method and c[\"n1\"] == n_vals[j]]\n                                is_sig = any(c[\"significant\"] for c in sig_cases)\n                                marker_txt = f\"↓{(f1s[j]-f1s[j+1])*100:.1f}pp\"\n                                if is_sig:\n                                    marker_txt += \"*\"\n                                mid_x = (n_vals[j] + n_vals[j+1]) / 2\n                                mid_y = (f1s[j] + f1s[j+1]) / 2\n                                ax.annotate(marker_txt, xy=(mid_x, mid_y),\n                                           fontsize=8, color=\"red\", fontweight=\"bold\",\n                                           ha=\"center\", va=\"bottom\")\n\n                ax.set_title(f\"{data['model']} / {data['dataset']}\", fontsize=11)\n                ax.set_xlabel(\"N (samples)\")\n                ax.set_ylabel(\"Entity Micro F1\")\n                ax.set_xticks(n_vals)\n                ax.grid(True, alpha=0.3)\n                ax.legend(fontsize=8, loc=\"best\")\n\n            plt.tight_layout()\n            fig2_path = os.path.join(OUTPUT_DIR, \"inverse_scaling_detail.png\")\n            plt.savefig(fig2_path, dpi=150, bbox_inches=\"tight\")\n            print(f\"Saved detail plot: {fig2_path}\", flush=True)\n            plt.close()\n\n    except Exception as e:\n        print(f\"Plotting error (non-fatal): {e}\", flush=True)\n\n    # ---- analysis.md ----\n    lines = [\"# Inverse Scaling Analysis for Structured Self-Consistency\\n\"]\n    lines.append(f\"Date: {time.strftime('%Y-%m-%d')}\\n\")\n    lines.append(\"## Question\\n\")\n    lines.append(\"Does increasing the number of samples N ever *decrease* entity-level F1 \")\n    lines.append(\"for any construction method? If so, which methods and under what conditions?\\n\")\n\n    lines.append(\"\\n## Setup\\n\")\n    lines.append(f\"- Configs: {total_configs} (2 models × 3 datasets)\\n\")\n    lines.append(f\"- Methods: {', '.join(METHODS)}\\n\")\n    lines.append(\"- Threshold: majority_vote uses θ=0.5 (fixed); lp/vc/sj_weighted and theta2n use θ=2/N (adaptive); uniform uses θ=0.25 (fixed)\\n\")\n    lines.append(\"- Metric: entity-level micro F1 (pooled TP/FP/FN)\\n\")\n    lines.append(\"- Significance: paired bootstrap (B=5000-10000), 95% CI\\n\")\n\n    lines.append(\"\\n## Results\\n\")\n    if total_transitions == 0:\n        lines.append(\"**No inverse scaling detected in any configuration.**\\n\")\n        lines.append(\"All methods show monotonically increasing or plateau behavior as N grows.\\n\")\n    else:\n        lines.append(f\"**{total_transitions} inverse scaling transitions detected, {total_sig} statistically significant.**\\n\")\n        lines.append(\"\\n### Inverse Scaling Cases\\n\")\n        lines.append(\"| Config | Method | N₁→N₂ | F1(N₁) | F1(N₂) | Drop | 95% CI | Sig? |\\n\")\n        lines.append(\"|--------|--------|--------|--------|--------|------|--------|------|\\n\")\n        for cfg_name, s in inverse_summary.items():\n            for c in s[\"inverse_cases\"]:\n                ci = c[\"bootstrap\"][\"ci_95\"]\n                sig = \"**YES**\" if c[\"significant\"] else \"no\"\n                lines.append(\n                    f\"| {cfg_name} | {c['method']} | {c['n1']}→{c['n2']} | \"\n                    f\"{c['f1_n1']:.4f} | {c['f1_n2']:.4f} | \"\n                    f\"{c['drop_pp']:.2f}pp | [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] | {sig} |\\n\"\n                )\n\n    lines.append(\"\\n### Method Behavior Summary\\n\")\n    lines.append(\"| Config | \" + \" | \".join(METHODS) + \" |\\n\")\n    lines.append(\"|--------\" + \"|--------\" * len(METHODS) + \"|\\n\")\n    for cfg_name, s in inverse_summary.items():\n        cells = []\n        for m in METHODS:\n            b = s[\"method_behaviors\"][m]\n            if b == \"inverse_scaling\":\n                cells.append(\"**INVERSE**\")\n            elif b == \"plateau\":\n                cells.append(\"plateau\")\n            else:\n                cells.append(\"↑ mono\")\n        lines.append(f\"| {cfg_name} | \" + \" | \".join(cells) + \" |\\n\")\n\n    lines.append(\"\\n### Degeneracy by N\\n\")\n    lines.append(\"| Config |\" + \" | \".join(f\"N={n}\" for n in [2,4,6,8,16]) + \" |\\n\")\n    lines.append(\"|--------\" + \"|------\" * 5 + \"|\\n\")\n    for cfg_name, s in inverse_summary.items():\n        cells = []\n        for n in [2,4,6,8,16]:\n            d = s[\"degeneracy_by_n\"].get(str(n), None)\n            cells.append(f\"{d:.1%}\" if d is not None else \"—\")\n        lines.append(f\"| {cfg_name} | \" + \" | \".join(cells) + \" |\\n\")\n\n    lines.append(\"\\n## Mechanism Analysis\\n\")\n    if total_transitions > 0:\n        # check which methods show inverse scaling\n        inv_methods = set()\n        for s in inverse_summary.values():\n            for c in s[\"inverse_cases\"]:\n                inv_methods.add(c[\"method\"])\n\n        fixed_theta = inv_methods & {\"majority_vote\", \"uniform\"}\n        adaptive_theta = inv_methods & {\"lp_weighted\", \"vc_weighted\", \"sj_weighted\", \"theta2n\"}\n\n        if fixed_theta and not adaptive_theta:\n            lines.append(\"Inverse scaling occurs **only in fixed-threshold methods** (\")\n            lines.append(\", \".join(sorted(fixed_theta)))\n            lines.append(\"). Adaptive-threshold methods (θ=2/N) are immune.\\n\\n\")\n            lines.append(\"**Mechanism**: With fixed θ, the effective vote requirement scales with N. \")\n            lines.append(\"At θ=0.5, an entity needs >N/2 votes. As N grows, correct-but-variable entities \")\n            lines.append(\"fail to reach this threshold, causing recall degradation that outweighs \")\n            lines.append(\"the precision benefits of additional samples.\\n\")\n        elif adaptive_theta:\n            lines.append(\"Inverse scaling occurs even in adaptive-threshold methods: \")\n            lines.append(\", \".join(sorted(adaptive_theta)))\n            lines.append(\". This suggests the issue goes beyond threshold choice.\\n\\n\")\n            lines.append(\"Possible mechanisms: (1) weight distortion at intermediate N; \")\n            lines.append(\"(2) interaction between signal quality and N; \")\n            lines.append(\"(3) boundary effects in entity aggregation.\\n\")\n        else:\n            lines.append(\"No clear pattern in affected methods.\\n\")\n    else:\n        lines.append(\"No inverse scaling detected. The construction methods are robust to increasing N.\\n\\n\")\n        lines.append(\"This is expected for adaptive-threshold methods (θ=2/N): as N grows, \")\n        lines.append(\"the threshold decreases, compensating for any dilution of correct-but-rare entities. \")\n        lines.append(\"For fixed-threshold methods (θ=0.5, θ=0.25), the monotonic increase suggests \")\n        lines.append(\"that additional samples consistently improve the precision-recall tradeoff.\\n\")\n\n    lines.append(\"\\n## Conclusion\\n\")\n    if total_sig > 0:\n        lines.append(f\"We find {total_sig} statistically significant inverse scaling case(s). \")\n        lines.append(\"This is the first reported inverse scaling finding in structured self-consistency. \")\n        lines.append(\"The finding has implications for practitioners choosing aggregation methods \")\n        lines.append(\"and sample budgets.\\n\")\n    elif total_transitions > 0:\n        lines.append(f\"We observe {total_transitions} inverse scaling transition(s), but none \")\n        lines.append(\"are statistically significant. The drops are within noise range.\\n\")\n    else:\n        lines.append(\"No inverse scaling is observed. Construction F1 monotonically increases \")\n        lines.append(\"(or plateaus) with N across all tested configurations. \")\n        lines.append(\"Structured self-consistency with entity-level construction is robust to sample budget.\\n\")\n\n    with open(os.path.join(OUTPUT_DIR, \"analysis.md\"), \"w\") as f:\n        f.writelines(lines)\n    print(f\"Saved analysis.md\", flush=True)\n\n    print(\"\\nDONE\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 696,
      "startLine": 1,
      "totalLines": 696
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of:

1. Data format: JSONL with `text`, `samples` (list of dicts with `entities` list), `gold` (dict with `entities`), `greedy` (dict with `entities`). Each entity has `start`, `end`, `type`, `text`. Each sample can have `mean_logprob`.

2. Key utility functions from both files:
   - `entity_set(entities)` → set of (start, end, type) tuples
   - `compute_prf(pred, gold)` → (precision, recall, f1)
   - `majority_vote(instance, threshold)` → set of entity tuples
   - `weighted_construction(samples, threshold, weights)` → set of entity tuples
   - `load_samples/load_data` for loading JSONL

Now I'm writing the `run_asb.py` script with a four-phase approach: first subsampling from the full N=16 data down to smaller sizes like 2, 4, 8, and 16 with multiple random subsets each, then computing cheap features from just the N=2 samples, finding the optimal N per instance that achieves at least 95% of the maximum gain, and finally training on those optimized configurations.

Writing the evaluation pipeline...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "11303cf4-cd02-4484-bc33-8d6ed65a59a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8mSx72HtcZKLosqA9XPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11020,
      "cache_read_input_tokens": 34095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11020
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

_source line 15_

Now I have full context on the data format and utilities. Let me write the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "d38bcef9-89fc-400e-95ed-417367ea62f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8mSx72HtcZKLosqA9XPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11020,
      "cache_read_input_tokens": 34095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11020
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rym8hPAkNxDyknqB2ZwZQT`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/",
  "description": "List existing experiment directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "5ca88e1d-8fc8-4ae5-ba1d-22e71486c0be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CY8mSx72HtcZKLosqA9XPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11020,
      "cache_read_input_tokens": 34095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11020
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

_source line 17 · 2026-05-20T16:28:39.298Z_

<details><summary>↩ Tool result · `toolu_01Rym8hPAkNxDyknqB2ZwZQT`</summary>

```text
e_theta
esj
mrsc
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "d47dff42-90ee-401b-9af1-2ab795d7fa05",
  "tool_use_result": {
    "stdout": "e_theta\nesj\nmrsc",
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

<details open><summary>🔧 Tool call — Bash · `toolu_016P4motZBqkuqZEDTUn9kwM`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/asb",
  "description": "Create asb experiment directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "289fe762-78a4-46f2-bc85-3ce38f36d15c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LBaU9fPPdDjxDiG4gADP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 45115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
      },
      "output_tokens": 67,
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

_source line 19 · 2026-05-20T16:28:42.685Z_

<details><summary>↩ Tool result · `toolu_016P4motZBqkuqZEDTUn9kwM`</summary>

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
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "eed8ab96-2811-4fd7-a6c8-ab7cbe9f5e2d",
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_0195tPH3CqeyftCUbT9JZsMS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Adaptive Sample Budget (ASB) for structured self-consistency IE.\n\nCPU-only experiment. No GPU or model forward pass required.\nSubsamples existing N=16 inference data to N∈{2,4,8,16}, computes instance-level\nfeatures from cheap (N=2) subsamples, trains a predictor for optimal per-instance\nsample count, and evaluates adaptive allocation under a fixed total budget.\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nimport warnings\nfrom collections import defaultdict\nfrom itertools import combinations\n\nimport numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.model_selection import StratifiedKFold\nfrom sklearn.metrics import f1_score, classification_report\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\nN_VALUES = [2, 4, 8, 16]\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_samples(path, max_instances=0):\n    data = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                data.append(json.loads(line))\n                if 0 < max_instances <= len(data):\n                    break\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Entity helpers\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities):\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred, gold):\n    if not gold and not pred:\n        return 1.0, 1.0, 1.0\n    if not pred or not gold:\n        return 0.0, 0.0, 0.0\n    tp = len(pred & gold)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred)\n    r = tp / len(gold)\n    return p, r, 2 * p * r / (p + r)\n\n\ndef majority_vote(samples, threshold=0.5):\n    counts = defaultdict(int)\n    N = len(samples)\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Subsampling\n# ---------------------------------------------------------------------------\n\ndef subsample_f1(instance, n, n_subsamples, rng, gold):\n    \"\"\"Compute mean construction F1 over random subsets of size n.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    if n >= max_n:\n        pred = majority_vote(all_samples)\n        return compute_prf(pred, gold)[2]\n\n    f1s = []\n    for _ in range(n_subsamples):\n        idx = rng.choice(max_n, size=n, replace=False)\n        subset = [all_samples[i] for i in idx]\n        pred = majority_vote(subset)\n        f1s.append(compute_prf(pred, gold)[2])\n    return float(np.mean(f1s))\n\n\ndef subsample_oracle_f1(instance, n, n_subsamples, rng, gold):\n    \"\"\"Mean oracle F1 (best single sample) over random subsets of size n.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    if n >= max_n:\n        return max(\n            compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n            for s in all_samples\n        )\n\n    oracles = []\n    for _ in range(n_subsamples):\n        idx = rng.choice(max_n, size=n, replace=False)\n        subset = [all_samples[i] for i in idx]\n        oracles.append(max(\n            compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n            for s in subset\n        ))\n    return float(np.mean(oracles))\n\n\ndef compute_degeneracy(samples):\n    \"\"\"Fraction of sample pairs that are identical entity sets.\"\"\"\n    esets = [frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n             for s in samples]\n    n = len(esets)\n    if n < 2:\n        return 0.0\n    n_same = sum(1 for i, j in combinations(range(n), 2) if esets[i] == esets[j])\n    return n_same / (n * (n - 1) / 2)\n\n\ndef compute_lp_variance(samples):\n    \"\"\"Variance of mean_logprob across samples.\"\"\"\n    lps = []\n    for s in samples:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lps.append(lp)\n    if len(lps) < 2:\n        return 0.0\n    return float(np.var(lps))\n\n\ndef compute_agreement(samples):\n    \"\"\"Average pairwise Jaccard similarity of entity sets.\"\"\"\n    esets = [frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n             for s in samples]\n    n = len(esets)\n    if n < 2:\n        return 1.0\n    jaccards = []\n    for i, j in combinations(range(n), 2):\n        a, b = esets[i], esets[j]\n        if not a and not b:\n            jaccards.append(1.0)\n        elif not a or not b:\n            jaccards.append(0.0)\n        else:\n            jaccards.append(len(a & b) / len(a | b))\n    return float(np.mean(jaccards))\n\n\ndef compute_entity_count(samples):\n    \"\"\"Average entity count across samples.\"\"\"\n    return float(np.mean([len(s.get(\"entities\", [])) for s in samples]))\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Instance features (from N=2 cheap subsamples)\n# ---------------------------------------------------------------------------\n\ndef compute_instance_features(instance, n_subsamples, rng):\n    \"\"\"Compute cheap features from small subsamples.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    n_feat = min(2, max_n)\n\n    degen_vals = []\n    lp_var_vals = []\n    agree_vals = []\n    ent_count_vals = []\n\n    n_trials = n_subsamples if n_feat < max_n else 1\n    for _ in range(n_trials):\n        if n_feat < max_n:\n            idx = rng.choice(max_n, size=n_feat, replace=False)\n            subset = [all_samples[i] for i in idx]\n        else:\n            subset = all_samples[:n_feat]\n        degen_vals.append(compute_degeneracy(subset))\n        lp_var_vals.append(compute_lp_variance(subset))\n        agree_vals.append(compute_agreement(subset))\n        ent_count_vals.append(compute_entity_count(subset))\n\n    text_length = len(instance.get(\"text\", \"\"))\n\n    features = {\n        \"degen_rate_n2\": float(np.mean(degen_vals)),\n        \"lp_variance_n2\": float(np.mean(lp_var_vals)),\n        \"agreement_n2\": float(np.mean(agree_vals)),\n        \"entity_count_n2\": float(np.mean(ent_count_vals)),\n        \"text_length\": text_length,\n    }\n\n    if \"greedy\" in instance and \"gold\" in instance:\n        greedy_ents = entity_set(instance[\"greedy\"].get(\"entities\", []))\n        gold_ents = entity_set(instance[\"gold\"][\"entities\"])\n        features[\"greedy_f1\"] = compute_prf(greedy_ents, gold_ents)[2]\n\n    return features\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Optimal N labels\n# ---------------------------------------------------------------------------\n\ndef find_optimal_n(f1_by_n, gain_ratio=0.95):\n    \"\"\"Find smallest N achieving ≥ gain_ratio of max F1 gain over N=2.\"\"\"\n    f1_min_n = min(N_VALUES)\n    f1_at_min = f1_by_n.get(f1_min_n, 0.0)\n    max_f1 = max(f1_by_n.values())\n    max_gain = max_f1 - f1_at_min\n\n    if max_gain <= 1e-6:\n        return f1_min_n\n\n    target = f1_at_min + gain_ratio * max_gain\n    for n in sorted(N_VALUES):\n        if f1_by_n.get(n, 0.0) >= target - 1e-9:\n            return n\n    return max(N_VALUES)\n\n\n# ---------------------------------------------------------------------------\n# Phase 4: Predictor training\n# ---------------------------------------------------------------------------\n\ndef train_and_evaluate(X, y, seed=42):\n    \"\"\"5-fold CV for multiple classifiers. Returns dict of results.\"\"\"\n    models = {\n        \"LogisticRegression\": LogisticRegression(\n            max_iter=1000, random_state=seed, multi_class=\"multinomial\",\n        ),\n        \"RandomForest\": RandomForestClassifier(\n            n_estimators=100, max_depth=5, random_state=seed,\n        ),\n        \"MLP\": MLPClassifier(\n            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,\n        ),\n    }\n\n    unique_classes = np.unique(y)\n    if len(unique_classes) < 2:\n        return {name: {\"macro_f1\": 0.0, \"note\": \"single class\"} for name in models}\n\n    n_splits = min(5, min(np.bincount(y)[np.bincount(y) > 0]))\n    if n_splits < 2:\n        n_splits = 2\n\n    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)\n    results = {}\n\n    for name, model in models.items():\n        fold_f1s = []\n        all_preds = np.zeros_like(y)\n        all_true = np.zeros_like(y)\n\n        for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):\n            X_train, X_test = X[train_idx], X[test_idx]\n            y_train, y_test = y[train_idx], y[test_idx]\n\n            scaler = StandardScaler()\n            X_train_s = scaler.fit_transform(X_train)\n            X_test_s = scaler.transform(X_test)\n\n            model_copy = type(model)(**model.get_params())\n            model_copy.fit(X_train_s, y_train)\n            preds = model_copy.predict(X_test_s)\n\n            fold_f1 = f1_score(y_test, preds, average=\"macro\", zero_division=0)\n            fold_f1s.append(fold_f1)\n            all_preds[test_idx] = preds\n            all_true[test_idx] = y_test\n\n        overall_f1 = f1_score(all_true, all_preds, average=\"macro\", zero_division=0)\n        results[name] = {\n            \"macro_f1\": round(float(overall_f1), 4),\n            \"fold_f1s\": [round(f, 4) for f in fold_f1s],\n            \"mean_fold_f1\": round(float(np.mean(fold_f1s)), 4),\n            \"std_fold_f1\": round(float(np.std(fold_f1s)), 4),\n        }\n\n    return results\n\n\ndef train_best_model(X, y, best_name, seed=42):\n    \"\"\"Train the best model on all data, return fitted model + scaler.\"\"\"\n    constructors = {\n        \"LogisticRegression\": lambda: LogisticRegression(\n            max_iter=1000, random_state=seed, multi_class=\"multinomial\",\n        ),\n        \"RandomForest\": lambda: RandomForestClassifier(\n            n_estimators=100, max_depth=5, random_state=seed,\n        ),\n        \"MLP\": lambda: MLPClassifier(\n            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,\n        ),\n    }\n    scaler = StandardScaler()\n    X_s = scaler.fit_transform(X)\n    model = constructors[best_name]()\n    model.fit(X_s, y)\n    return model, scaler\n\n\n# ---------------------------------------------------------------------------\n# Phase 5: Budget-constrained evaluation\n# ---------------------------------------------------------------------------\n\ndef adaptive_allocation(predicted_ns, budget_per_instance, n_instances):\n    \"\"\"Adjust predicted N values to meet total budget constraint.\"\"\"\n    total_budget = budget_per_instance * n_instances\n    alloc = np.array(predicted_ns, dtype=float)\n\n    current_total = alloc.sum()\n\n    if current_total > total_budget:\n        # trim: repeatedly reduce the largest allocations\n        while alloc.sum() > total_budget:\n            excess = alloc.sum() - total_budget\n            max_idx = np.where(alloc == alloc.max())[0]\n            reduce_each = min(excess / len(max_idx), 2.0)\n            for idx in max_idx:\n                alloc[idx] = max(2, alloc[idx] - reduce_each)\n                if alloc.sum() <= total_budget:\n                    break\n\n    elif current_total < total_budget:\n        # distribute surplus to instances with highest predicted N (most uncertain)\n        surplus = total_budget - current_total\n        uncertainty_order = np.argsort(-np.array(predicted_ns))\n        for idx in uncertainty_order:\n            if surplus <= 0:\n                break\n            add = min(surplus, 16 - alloc[idx])\n            alloc[idx] += add\n            surplus -= add\n\n    # snap to valid N values\n    valid = np.array(N_VALUES)\n    snapped = []\n    for a in alloc:\n        snapped.append(int(valid[np.argmin(np.abs(valid - a))]))\n    return snapped\n\n\ndef evaluate_allocation(instances, allocations, n_subsamples, rng):\n    \"\"\"Evaluate construction F1 under given per-instance N allocations.\"\"\"\n    f1s = []\n    for inst, n_alloc in zip(instances, allocations):\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        f1 = subsample_f1(inst, n_alloc, n_subsamples, rng, gold)\n        f1s.append(f1)\n    return float(np.mean(f1s))\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    ap = argparse.ArgumentParser(\n        description=\"Adaptive Sample Budget (ASB) — CPU-only experiment\"\n    )\n    ap.add_argument(\"--data_paths\", type=str, required=True,\n                    help=\"Comma-separated N≥16 inference JSONL paths\")\n    ap.add_argument(\"--dataset_names\", type=str, required=True,\n                    help=\"Comma-separated dataset names (same order as data_paths)\")\n    ap.add_argument(\"--output_dir\", type=str, required=True)\n    ap.add_argument(\"--n_subsamples\", type=int, default=10,\n                    help=\"Random subsets per N value (default: 10)\")\n    ap.add_argument(\"--budget_per_instance\", type=int, default=8,\n                    help=\"Average budget per instance (default: 8)\")\n    ap.add_argument(\"--max_instances\", type=int, default=0,\n                    help=\"Cap instances per dataset for debugging (0=all)\")\n    ap.add_argument(\"--seed\", type=int, default=42)\n    args = ap.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    rng = np.random.RandomState(args.seed)\n\n    data_paths = [p.strip() for p in args.data_paths.split(\",\")]\n    dataset_names = [n.strip() for n in args.dataset_names.split(\",\")]\n    assert len(data_paths) == len(dataset_names), \\\n        f\"Mismatch: {len(data_paths)} paths vs {len(dataset_names)} names\"\n\n    all_results = {}\n\n    for dpath, dname in zip(data_paths, dataset_names):\n        print(f\"\\n{'='*70}\")\n        print(f\"  Dataset: {dname}\")\n        print(f\"  Path: {dpath}\")\n        print(f\"{'='*70}\")\n\n        if not os.path.exists(dpath):\n            print(f\"  SKIP: file not found\")\n            continue\n\n        t0 = time.time()\n        instances = load_samples(dpath, args.max_instances)\n        # filter to instances with gold\n        instances = [inst for inst in instances if inst.get(\"gold\", {}).get(\"entities\")]\n        max_n = len(instances[0][\"samples\"]) if instances else 0\n        print(f\"  Loaded {len(instances)} instances (with gold), max_n={max_n}\")\n\n        if max_n < max(N_VALUES):\n            valid_ns = [n for n in N_VALUES if n <= max_n]\n            print(f\"  Warning: max_n={max_n} < 16, using N_VALUES={valid_ns}\")\n        else:\n            valid_ns = N_VALUES\n\n        # ---- Phase 1: Compute F1 at each N for every instance ----\n        print(\"\\n  Phase 1: Subsampling F1 at each N ...\")\n        inst_f1_by_n = []\n        for i, inst in enumerate(instances):\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            f1_dict = {}\n            for n in valid_ns:\n                f1_dict[n] = subsample_f1(inst, n, args.n_subsamples, rng, gold)\n            inst_f1_by_n.append(f1_dict)\n            if (i + 1) % 500 == 0:\n                print(f\"    {i+1}/{len(instances)} instances processed\")\n\n        # aggregate F1 by N\n        mean_f1_by_n = {}\n        for n in valid_ns:\n            mean_f1_by_n[n] = float(np.mean([d[n] for d in inst_f1_by_n]))\n        print(f\"  Mean F1 by N: { {n: f'{v:.4f}' for n, v in mean_f1_by_n.items()} }\")\n\n        # ---- Phase 2: Instance features ----\n        print(\"\\n  Phase 2: Computing instance features (from N=2) ...\")\n        features_list = []\n        for i, inst in enumerate(instances):\n            feat = compute_instance_features(inst, args.n_subsamples, rng)\n            features_list.append(feat)\n\n        feature_names = sorted(features_list[0].keys())\n        X = np.array([[f[k] for k in feature_names] for f in features_list])\n        print(f\"  Features: {feature_names}\")\n        print(f\"  Feature matrix: {X.shape}\")\n\n        # ---- Phase 3: Optimal N labels ----\n        print(\"\\n  Phase 3: Computing optimal N labels ...\")\n        optimal_ns = []\n        for f1_dict in inst_f1_by_n:\n            optimal_ns.append(find_optimal_n(f1_dict, gain_ratio=0.95))\n        optimal_ns_arr = np.array(optimal_ns)\n\n        # map to class indices for sklearn\n        n_to_class = {n: i for i, n in enumerate(valid_ns)}\n        y = np.array([n_to_class[n] for n in optimal_ns])\n\n        dist = {n: int((optimal_ns_arr == n).sum()) for n in valid_ns}\n        print(f\"  Optimal N distribution: {dist}\")\n        print(f\"  Mean optimal N: {optimal_ns_arr.mean():.2f}\")\n\n        # ---- Phase 4: Predictor training ----\n        print(\"\\n  Phase 4: Training predictors (5-fold CV) ...\")\n        cv_results = train_and_evaluate(X, y, seed=args.seed)\n\n        best_model_name = max(cv_results, key=lambda k: cv_results[k][\"macro_f1\"])\n        print(f\"  CV Results:\")\n        for name, res in cv_results.items():\n            marker = \" <-- best\" if name == best_model_name else \"\"\n            print(f\"    {name}: macro_F1={res['macro_f1']:.4f} \"\n                  f\"(±{res.get('std_fold_f1', 0):.4f}){marker}\")\n\n        # train final model on all data\n        model, scaler = train_best_model(X, y, best_model_name, seed=args.seed)\n        predicted_classes = model.predict(scaler.transform(X))\n        class_to_n = {i: n for n, i in n_to_class.items()}\n        predicted_ns = [class_to_n[c] for c in predicted_classes]\n\n        # ---- Phase 5: Budget-constrained evaluation ----\n        print(f\"\\n  Phase 5: Budget-constrained evaluation (avg budget={args.budget_per_instance}) ...\")\n\n        # adaptive allocation\n        adapted_ns = adaptive_allocation(\n            predicted_ns, args.budget_per_instance, len(instances)\n        )\n        adaptive_f1 = evaluate_allocation(\n            instances, adapted_ns, args.n_subsamples, rng\n        )\n        adaptive_total = sum(adapted_ns)\n        adaptive_avg_n = adaptive_total / len(instances)\n\n        # uniform baseline\n        uniform_n = args.budget_per_instance\n        uniform_ns = [uniform_n] * len(instances)\n        uniform_f1 = evaluate_allocation(\n            instances, uniform_ns, args.n_subsamples, rng\n        )\n\n        # oracle adaptive (uses true optimal N, then adjusts to budget)\n        oracle_adapted = adaptive_allocation(\n            optimal_ns, args.budget_per_instance, len(instances)\n        )\n        oracle_f1 = evaluate_allocation(\n            instances, oracle_adapted, args.n_subsamples, rng\n        )\n        oracle_avg_n = sum(oracle_adapted) / len(instances)\n\n        # greedy baseline\n        greedy_f1s = []\n        for inst in instances:\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            g_ents = entity_set(inst.get(\"greedy\", inst[\"samples\"][0]).get(\"entities\", []))\n            greedy_f1s.append(compute_prf(g_ents, gold)[2])\n        greedy_f1 = float(np.mean(greedy_f1s))\n\n        # N=16 (all samples) baseline\n        full_f1 = mean_f1_by_n.get(max(valid_ns), 0.0)\n\n        print(f\"\\n  Results:\")\n        print(f\"    Greedy (N=1):         F1={greedy_f1:.4f}\")\n        print(f\"    Uniform N={uniform_n}:         F1={uniform_f1:.4f}\")\n        print(f\"    Adaptive (predicted): F1={adaptive_f1:.4f}  avg_N={adaptive_avg_n:.2f}\")\n        print(f\"    Oracle adaptive:      F1={oracle_f1:.4f}  avg_N={oracle_avg_n:.2f}\")\n        print(f\"    Full N={max(valid_ns)}:           F1={full_f1:.4f}\")\n        print(f\"    Δ(adaptive - uniform): {adaptive_f1 - uniform_f1:+.4f}\")\n        print(f\"    Δ(oracle - uniform):   {oracle_f1 - uniform_f1:+.4f}\")\n\n        # allocation distribution\n        adapted_dist = {n: int(sum(1 for a in adapted_ns if a == n)) for n in valid_ns}\n        print(f\"    Adaptive allocation dist: {adapted_dist}\")\n        print(f\"    Adaptive total budget: {adaptive_total} \"\n              f\"(target: {args.budget_per_instance * len(instances)})\")\n\n        # feature importance (from RF)\n        if best_model_name == \"RandomForest\":\n            importances = model.feature_importances_\n        else:\n            # train RF just for feature importance\n            rf_temp = RandomForestClassifier(\n                n_estimators=100, max_depth=5, random_state=args.seed\n            )\n            rf_temp.fit(scaler.transform(X), y)\n            importances = rf_temp.feature_importances_\n\n        feat_imp = sorted(zip(feature_names, importances), key=lambda x: -x[1])\n        print(f\"\\n  Feature importance (RF):\")\n        for fname, imp in feat_imp:\n            print(f\"    {fname}: {imp:.4f}\")\n\n        elapsed = time.time() - t0\n\n        # ---- Build dataset result ----\n        ds_result = {\n            \"dataset\": dname,\n            \"data_path\": dpath,\n            \"n_instances\": len(instances),\n            \"max_n\": max_n,\n            \"n_subsamples\": args.n_subsamples,\n            \"budget_per_instance\": args.budget_per_instance,\n            \"seed\": args.seed,\n            \"elapsed_seconds\": round(elapsed, 1),\n            \"mean_f1_by_n\": {str(n): round(v, 4) for n, v in mean_f1_by_n.items()},\n            \"optimal_n_distribution\": {str(n): int(c) for n, c in dist.items()},\n            \"mean_optimal_n\": round(float(optimal_ns_arr.mean()), 2),\n            \"cv_results\": cv_results,\n            \"best_model\": best_model_name,\n            \"feature_importance\": {fn: round(float(imp), 4) for fn, imp in feat_imp},\n            \"evaluation\": {\n                \"greedy_f1\": round(greedy_f1, 4),\n                \"uniform_f1\": round(uniform_f1, 4),\n                \"adaptive_f1\": round(adaptive_f1, 4),\n                \"oracle_adaptive_f1\": round(oracle_f1, 4),\n                \"full_n_f1\": round(full_f1, 4),\n                \"delta_adaptive_vs_uniform\": round(adaptive_f1 - uniform_f1, 4),\n                \"delta_oracle_vs_uniform\": round(oracle_f1 - uniform_f1, 4),\n                \"adaptive_avg_n\": round(adaptive_avg_n, 2),\n                \"oracle_avg_n\": round(oracle_avg_n, 2),\n                \"adaptive_allocation_dist\": {str(n): int(c) for n, c in adapted_dist.items()},\n                \"adaptive_total_budget\": adaptive_total,\n            },\n        }\n        all_results[dname] = ds_result\n\n        # save per-instance details\n        per_instance = []\n        for i, inst in enumerate(instances):\n            per_instance.append({\n                \"text\": inst.get(\"text\", \"\")[:100],\n                \"features\": features_list[i],\n                \"f1_by_n\": {str(n): round(inst_f1_by_n[i][n], 4) for n in valid_ns},\n                \"optimal_n\": optimal_ns[i],\n                \"predicted_n\": predicted_ns[i],\n                \"adapted_n\": adapted_ns[i],\n            })\n\n        detail_path = os.path.join(args.output_dir, f\"instance_details_{dname}.jsonl\")\n        with open(detail_path, \"w\") as f:\n            for item in per_instance:\n                f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n        print(f\"\\n  Saved instance details: {detail_path}\")\n\n    # ---- Save aggregate results ----\n    out_path = os.path.join(args.output_dir, \"asb_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n    # ---- Print summary ----\n    print(f\"\\n{'='*70}\")\n    print(\"ASB Adaptive Sample Budget — Summary\")\n    print(f\"{'='*70}\")\n    for dname, res in all_results.items():\n        ev = res[\"evaluation\"]\n        print(f\"\\n  {dname}:\")\n        print(f\"    Instances: {res['n_instances']}\")\n        print(f\"    Uniform N={args.budget_per_instance}: F1={ev['uniform_f1']:.4f}\")\n        print(f\"    Adaptive:         F1={ev['adaptive_f1']:.4f} (Δ={ev['delta_adaptive_vs_uniform']:+.4f})\")\n        print(f\"    Oracle:           F1={ev['oracle_adaptive_f1']:.4f} (Δ={ev['delta_oracle_vs_uniform']:+.4f})\")\n        print(f\"    Best predictor: {res['best_model']} (macro_F1={res['cv_results'][res['best_model']]['macro_f1']:.4f})\")\n        print(f\"    Optimal N dist: {res['optimal_n_distribution']}\")\n\n    print(f\"\\n  NOTE: This is a CPU-only experiment. No GPU required.\")\n    print(\"DONE\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "ab551df7-8b90-42c7-afea-265299d227d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZjksiT3HAqJh5pPMSdWHw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 45621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
      },
      "output_tokens": 59,
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

_source line 21 · 2026-05-20T16:30:26.286Z_

<details><summary>↩ Tool result · `toolu_0195tPH3CqeyftCUbT9JZsMS`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "09d8e3de-9f2a-415b-abbd-9fa20eaae47b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Adaptive Sample Budget (ASB) for structured self-consistency IE.\n\nCPU-only experiment. No GPU or model forward pass required.\nSubsamples existing N=16 inference data to N∈{2,4,8,16}, computes instance-level\nfeatures from cheap (N=2) subsamples, trains a predictor for optimal per-instance\nsample count, and evaluates adaptive allocation under a fixed total budget.\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nimport warnings\nfrom collections import defaultdict\nfrom itertools import combinations\n\nimport numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neural_network import MLPClassifier\nfrom sklearn.model_selection import StratifiedKFold\nfrom sklearn.metrics import f1_score, classification_report\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\nN_VALUES = [2, 4, 8, 16]\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_samples(path, max_instances=0):\n    data = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                data.append(json.loads(line))\n                if 0 < max_instances <= len(data):\n                    break\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Entity helpers\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities):\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred, gold):\n    if not gold and not pred:\n        return 1.0, 1.0, 1.0\n    if not pred or not gold:\n        return 0.0, 0.0, 0.0\n    tp = len(pred & gold)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred)\n    r = tp / len(gold)\n    return p, r, 2 * p * r / (p + r)\n\n\ndef majority_vote(samples, threshold=0.5):\n    counts = defaultdict(int)\n    N = len(samples)\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Subsampling\n# ---------------------------------------------------------------------------\n\ndef subsample_f1(instance, n, n_subsamples, rng, gold):\n    \"\"\"Compute mean construction F1 over random subsets of size n.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    if n >= max_n:\n        pred = majority_vote(all_samples)\n        return compute_prf(pred, gold)[2]\n\n    f1s = []\n    for _ in range(n_subsamples):\n        idx = rng.choice(max_n, size=n, replace=False)\n        subset = [all_samples[i] for i in idx]\n        pred = majority_vote(subset)\n        f1s.append(compute_prf(pred, gold)[2])\n    return float(np.mean(f1s))\n\n\ndef subsample_oracle_f1(instance, n, n_subsamples, rng, gold):\n    \"\"\"Mean oracle F1 (best single sample) over random subsets of size n.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    if n >= max_n:\n        return max(\n            compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n            for s in all_samples\n        )\n\n    oracles = []\n    for _ in range(n_subsamples):\n        idx = rng.choice(max_n, size=n, replace=False)\n        subset = [all_samples[i] for i in idx]\n        oracles.append(max(\n            compute_prf(entity_set(s.get(\"entities\", [])), gold)[2]\n            for s in subset\n        ))\n    return float(np.mean(oracles))\n\n\ndef compute_degeneracy(samples):\n    \"\"\"Fraction of sample pairs that are identical entity sets.\"\"\"\n    esets = [frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n             for s in samples]\n    n = len(esets)\n    if n < 2:\n        return 0.0\n    n_same = sum(1 for i, j in combinations(range(n), 2) if esets[i] == esets[j])\n    return n_same / (n * (n - 1) / 2)\n\n\ndef compute_lp_variance(samples):\n    \"\"\"Variance of mean_logprob across samples.\"\"\"\n    lps = []\n    for s in samples:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lps.append(lp)\n    if len(lps) < 2:\n        return 0.0\n    return float(np.var(lps))\n\n\ndef compute_agreement(samples):\n    \"\"\"Average pairwise Jaccard similarity of entity sets.\"\"\"\n    esets = [frozenset((e[\"start\"], e[\"end\"], e[\"type\"]) for e in s.get(\"entities\", []))\n             for s in samples]\n    n = len(esets)\n    if n < 2:\n        return 1.0\n    jaccards = []\n    for i, j in combinations(range(n), 2):\n        a, b = esets[i], esets[j]\n        if not a and not b:\n            jaccards.append(1.0)\n        elif not a or not b:\n            jaccards.append(0.0)\n        else:\n            jaccards.append(len(a & b) / len(a | b))\n    return float(np.mean(jaccards))\n\n\ndef compute_entity_count(samples):\n    \"\"\"Average entity count across samples.\"\"\"\n    return float(np.mean([len(s.get(\"entities\", [])) for s in samples]))\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Instance features (from N=2 cheap subsamples)\n# ---------------------------------------------------------------------------\n\ndef compute_instance_features(instance, n_subsamples, rng):\n    \"\"\"Compute cheap features from small subsamples.\"\"\"\n    all_samples = instance[\"samples\"]\n    max_n = len(all_samples)\n    n_feat = min(2, max_n)\n\n    degen_vals = []\n    lp_var_vals = []\n    agree_vals = []\n    ent_count_vals = []\n\n    n_trials = n_subsamples if n_feat < max_n else 1\n    for _ in range(n_trials):\n        if n_feat < max_n:\n            idx = rng.choice(max_n, size=n_feat, replace=False)\n            subset = [all_samples[i] for i in idx]\n        else:\n            subset = all_samples[:n_feat]\n        degen_vals.append(compute_degeneracy(subset))\n        lp_var_vals.append(compute_lp_variance(subset))\n        agree_vals.append(compute_agreement(subset))\n        ent_count_vals.append(compute_entity_count(subset))\n\n    text_length = len(instance.get(\"text\", \"\"))\n\n    features = {\n        \"degen_rate_n2\": float(np.mean(degen_vals)),\n        \"lp_variance_n2\": float(np.mean(lp_var_vals)),\n        \"agreement_n2\": float(np.mean(agree_vals)),\n        \"entity_count_n2\": float(np.mean(ent_count_vals)),\n        \"text_length\": text_length,\n    }\n\n    if \"greedy\" in instance and \"gold\" in instance:\n        greedy_ents = entity_set(instance[\"greedy\"].get(\"entities\", []))\n        gold_ents = entity_set(instance[\"gold\"][\"entities\"])\n        features[\"greedy_f1\"] = compute_prf(greedy_ents, gold_ents)[2]\n\n    return features\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Optimal N labels\n# ---------------------------------------------------------------------------\n\ndef find_optimal_n(f1_by_n, gain_ratio=0.95):\n    \"\"\"Find smallest N achieving ≥ gain_ratio of max F1 gain over N=2.\"\"\"\n    f1_min_n = min(N_VALUES)\n    f1_at_min = f1_by_n.get(f1_min_n, 0.0)\n    max_f1 = max(f1_by_n.values())\n    max_gain = max_f1 - f1_at_min\n\n    if max_gain <= 1e-6:\n        return f1_min_n\n\n    target = f1_at_min + gain_ratio * max_gain\n    for n in sorted(N_VALUES):\n        if f1_by_n.get(n, 0.0) >= target - 1e-9:\n            return n\n    return max(N_VALUES)\n\n\n# ---------------------------------------------------------------------------\n# Phase 4: Predictor training\n# ---------------------------------------------------------------------------\n\ndef train_and_evaluate(X, y, seed=42):\n    \"\"\"5-fold CV for multiple classifiers. Returns dict of results.\"\"\"\n    models = {\n        \"LogisticRegression\": LogisticRegression(\n            max_iter=1000, random_state=seed, multi_class=\"multinomial\",\n        ),\n        \"RandomForest\": RandomForestClassifier(\n            n_estimators=100, max_depth=5, random_state=seed,\n        ),\n        \"MLP\": MLPClassifier(\n            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,\n        ),\n    }\n\n    unique_classes = np.unique(y)\n    if len(unique_classes) < 2:\n        return {name: {\"macro_f1\": 0.0, \"note\": \"single class\"} for name in models}\n\n    n_splits = min(5, min(np.bincount(y)[np.bincount(y) > 0]))\n    if n_splits < 2:\n        n_splits = 2\n\n    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)\n    results = {}\n\n    for name, model in models.items():\n        fold_f1s = []\n        all_preds = np.zeros_like(y)\n        all_true = np.zeros_like(y)\n\n        for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):\n            X_train, X_test = X[train_idx], X[test_idx]\n            y_train, y_test = y[train_idx], y[test_idx]\n\n            scaler = StandardScaler()\n            X_train_s = scaler.fit_transform(X_train)\n            X_test_s = scaler.transform(X_test)\n\n            model_copy = type(model)(**model.get_params())\n            model_copy.fit(X_train_s, y_train)\n            preds = model_copy.predict(X_test_s)\n\n            fold_f1 = f1_score(y_test, preds, average=\"macro\", zero_division=0)\n            fold_f1s.append(fold_f1)\n            all_preds[test_idx] = preds\n            all_true[test_idx] = y_test\n\n        overall_f1 = f1_score(all_true, all_preds, average=\"macro\", zero_division=0)\n        results[name] = {\n            \"macro_f1\": round(float(overall_f1), 4),\n            \"fold_f1s\": [round(f, 4) for f in fold_f1s],\n            \"mean_fold_f1\": round(float(np.mean(fold_f1s)), 4),\n            \"std_fold_f1\": round(float(np.std(fold_f1s)), 4),\n        }\n\n    return results\n\n\ndef train_best_model(X, y, best_name, seed=42):\n    \"\"\"Train the best model on all data, return fitted model + scaler.\"\"\"\n    constructors = {\n        \"LogisticRegression\": lambda: LogisticRegression(\n            max_iter=1000, random_state=seed, multi_class=\"multinomial\",\n        ),\n        \"RandomForest\": lambda: RandomForestClassifier(\n            n_estimators=100, max_depth=5, random_state=seed,\n        ),\n        \"MLP\": lambda: MLPClassifier(\n            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,\n        ),\n    }\n    scaler = StandardScaler()\n    X_s = scaler.fit_transform(X)\n    model = constructors[best_name]()\n    model.fit(X_s, y)\n    return model, scaler\n\n\n# ---------------------------------------------------------------------------\n# Phase 5: Budget-constrained evaluation\n# ---------------------------------------------------------------------------\n\ndef adaptive_allocation(predicted_ns, budget_per_instance, n_instances):\n    \"\"\"Adjust predicted N values to meet total budget constraint.\"\"\"\n    total_budget = budget_per_instance * n_instances\n    alloc = np.array(predicted_ns, dtype=float)\n\n    current_total = alloc.sum()\n\n    if current_total > total_budget:\n        # trim: repeatedly reduce the largest allocations\n        while alloc.sum() > total_budget:\n            excess = alloc.sum() - total_budget\n            max_idx = np.where(alloc == alloc.max())[0]\n            reduce_each = min(excess / len(max_idx), 2.0)\n            for idx in max_idx:\n                alloc[idx] = max(2, alloc[idx] - reduce_each)\n                if alloc.sum() <= total_budget:\n                    break\n\n    elif current_total < total_budget:\n        # distribute surplus to instances with highest predicted N (most uncertain)\n        surplus = total_budget - current_total\n        uncertainty_order = np.argsort(-np.array(predicted_ns))\n        for idx in uncertainty_order:\n            if surplus <= 0:\n                break\n            add = min(surplus, 16 - alloc[idx])\n            alloc[idx] += add\n            surplus -= add\n\n    # snap to valid N values\n    valid = np.array(N_VALUES)\n    snapped = []\n    for a in alloc:\n        snapped.append(int(valid[np.argmin(np.abs(valid - a))]))\n    return snapped\n\n\ndef evaluate_allocation(instances, allocations, n_subsamples, rng):\n    \"\"\"Evaluate construction F1 under given per-instance N allocations.\"\"\"\n    f1s = []\n    for inst, n_alloc in zip(instances, allocations):\n        gold = entity_set(inst[\"gold\"][\"entities\"])\n        f1 = subsample_f1(inst, n_alloc, n_subsamples, rng, gold)\n        f1s.append(f1)\n    return float(np.mean(f1s))\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    ap = argparse.ArgumentParser(\n        description=\"Adaptive Sample Budget (ASB) — CPU-only experiment\"\n    )\n    ap.add_argument(\"--data_paths\", type=str, required=True,\n                    help=\"Comma-separated N≥16 inference JSONL paths\")\n    ap.add_argument(\"--dataset_names\", type=str, required=True,\n                    help=\"Comma-separated dataset names (same order as data_paths)\")\n    ap.add_argument(\"--output_dir\", type=str, required=True)\n    ap.add_argument(\"--n_subsamples\", type=int, default=10,\n                    help=\"Random subsets per N value (default: 10)\")\n    ap.add_argument(\"--budget_per_instance\", type=int, default=8,\n                    help=\"Average budget per instance (default: 8)\")\n    ap.add_argument(\"--max_instances\", type=int, default=0,\n                    help=\"Cap instances per dataset for debugging (0=all)\")\n    ap.add_argument(\"--seed\", type=int, default=42)\n    args = ap.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    rng = np.random.RandomState(args.seed)\n\n    data_paths = [p.strip() for p in args.data_paths.split(\",\")]\n    dataset_names = [n.strip() for n in args.dataset_names.split(\",\")]\n    assert len(data_paths) == len(dataset_names), \\\n        f\"Mismatch: {len(data_paths)} paths vs {len(dataset_names)} names\"\n\n    all_results = {}\n\n    for dpath, dname in zip(data_paths, dataset_names):\n        print(f\"\\n{'='*70}\")\n        print(f\"  Dataset: {dname}\")\n        print(f\"  Path: {dpath}\")\n        print(f\"{'='*70}\")\n\n        if not os.path.exists(dpath):\n            print(f\"  SKIP: file not found\")\n            continue\n\n        t0 = time.time()\n        instances = load_samples(dpath, args.max_instances)\n        # filter to instances with gold\n        instances = [inst for inst in instances if inst.get(\"gold\", {}).get(\"entities\")]\n        max_n = len(instances[0][\"samples\"]) if instances else 0\n        print(f\"  Loaded {len(instances)} instances (with gold), max_n={max_n}\")\n\n        if max_n < max(N_VALUES):\n            valid_ns = [n for n in N_VALUES if n <= max_n]\n            print(f\"  Warning: max_n={max_n} < 16, using N_VALUES={valid_ns}\")\n        else:\n            valid_ns = N_VALUES\n\n        # ---- Phase 1: Compute F1 at each N for every instance ----\n        print(\"\\n  Phase 1: Subsampling F1 at each N ...\")\n        inst_f1_by_n = []\n        for i, inst in enumerate(instances):\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            f1_dict = {}\n            for n in valid_ns:\n                f1_dict[n] = subsample_f1(inst, n, args.n_subsamples, rng, gold)\n            inst_f1_by_n.append(f1_dict)\n            if (i + 1) % 500 == 0:\n                print(f\"    {i+1}/{len(instances)} instances processed\")\n\n        # aggregate F1 by N\n        mean_f1_by_n = {}\n        for n in valid_ns:\n            mean_f1_by_n[n] = float(np.mean([d[n] for d in inst_f1_by_n]))\n        print(f\"  Mean F1 by N: { {n: f'{v:.4f}' for n, v in mean_f1_by_n.items()} }\")\n\n        # ---- Phase 2: Instance features ----\n        print(\"\\n  Phase 2: Computing instance features (from N=2) ...\")\n        features_list = []\n        for i, inst in enumerate(instances):\n            feat = compute_instance_features(inst, args.n_subsamples, rng)\n            features_list.append(feat)\n\n        feature_names = sorted(features_list[0].keys())\n        X = np.array([[f[k] for k in feature_names] for f in features_list])\n        print(f\"  Features: {feature_names}\")\n        print(f\"  Feature matrix: {X.shape}\")\n\n        # ---- Phase 3: Optimal N labels ----\n        print(\"\\n  Phase 3: Computing optimal N labels ...\")\n        optimal_ns = []\n        for f1_dict in inst_f1_by_n:\n            optimal_ns.append(find_optimal_n(f1_dict, gain_ratio=0.95))\n        optimal_ns_arr = np.array(optimal_ns)\n\n        # map to class indices for sklearn\n        n_to_class = {n: i for i, n in enumerate(valid_ns)}\n        y = np.array([n_to_class[n] for n in optimal_ns])\n\n        dist = {n: int((optimal_ns_arr == n).sum()) for n in valid_ns}\n        print(f\"  Optimal N distribution: {dist}\")\n        print(f\"  Mean optimal N: {optimal_ns_arr.mean():.2f}\")\n\n        # ---- Phase 4: Predictor training ----\n        print(\"\\n  Phase 4: Training predictors (5-fold CV) ...\")\n        cv_results = train_and_evaluate(X, y, seed=args.seed)\n\n        best_model_name = max(cv_results, key=lambda k: cv_results[k][\"macro_f1\"])\n        print(f\"  CV Results:\")\n        for name, res in cv_results.items():\n            marker = \" <-- best\" if name == best_model_name else \"\"\n            print(f\"    {name}: macro_F1={res['macro_f1']:.4f} \"\n                  f\"(±{res.get('std_fold_f1', 0):.4f}){marker}\")\n\n        # train final model on all data\n        model, scaler = train_best_model(X, y, best_model_name, seed=args.seed)\n        predicted_classes = model.predict(scaler.transform(X))\n        class_to_n = {i: n for n, i in n_to_class.items()}\n        predicted_ns = [class_to_n[c] for c in predicted_classes]\n\n        # ---- Phase 5: Budget-constrained evaluation ----\n        print(f\"\\n  Phase 5: Budget-constrained evaluation (avg budget={args.budget_per_instance}) ...\")\n\n        # adaptive allocation\n        adapted_ns = adaptive_allocation(\n            predicted_ns, args.budget_per_instance, len(instances)\n        )\n        adaptive_f1 = evaluate_allocation(\n            instances, adapted_ns, args.n_subsamples, rng\n        )\n        adaptive_total = sum(adapted_ns)\n        adaptive_avg_n = adaptive_total / len(instances)\n\n        # uniform baseline\n        uniform_n = args.budget_per_instance\n        uniform_ns = [uniform_n] * len(instances)\n        uniform_f1 = evaluate_allocation(\n            instances, uniform_ns, args.n_subsamples, rng\n        )\n\n        # oracle adaptive (uses true optimal N, then adjusts to budget)\n        oracle_adapted = adaptive_allocation(\n            optimal_ns, args.budget_per_instance, len(instances)\n        )\n        oracle_f1 = evaluate_allocation(\n            instances, oracle_adapted, args.n_subsamples, rng\n        )\n        oracle_avg_n = sum(oracle_adapted) / len(instances)\n\n        # greedy baseline\n        greedy_f1s = []\n        for inst in instances:\n            gold = entity_set(inst[\"gold\"][\"entities\"])\n            g_ents = entity_set(inst.get(\"greedy\", inst[\"samples\"][0]).get(\"entities\", []))\n            greedy_f1s.append(compute_prf(g_ents, gold)[2])\n        greedy_f1 = float(np.mean(greedy_f1s))\n\n        # N=16 (all samples) baseline\n        full_f1 = mean_f1_by_n.get(max(valid_ns), 0.0)\n\n        print(f\"\\n  Results:\")\n        print(f\"    Greedy (N=1):         F1={greedy_f1:.4f}\")\n        print(f\"    Uniform N={uniform_n}:         F1={uniform_f1:.4f}\")\n        print(f\"    Adaptive (predicted): F1={adaptive_f1:.4f}  avg_N={adaptive_avg_n:.2f}\")\n        print(f\"    Oracle adaptive:      F1={oracle_f1:.4f}  avg_N={oracle_avg_n:.2f}\")\n        print(f\"    Full N={max(valid_ns)}:           F1={full_f1:.4f}\")\n        print(f\"    Δ(adaptive - uniform): {adaptive_f1 - uniform_f1:+.4f}\")\n        print(f\"    Δ(oracle - uniform):   {oracle_f1 - uniform_f1:+.4f}\")\n\n        # allocation distribution\n        adapted_dist = {n: int(sum(1 for a in adapted_ns if a == n)) for n in valid_ns}\n        print(f\"    Adaptive allocation dist: {adapted_dist}\")\n        print(f\"    Adaptive total budget: {adaptive_total} \"\n              f\"(target: {args.budget_per_instance * len(instances)})\")\n\n        # feature importance (from RF)\n        if best_model_name == \"RandomForest\":\n            importances = model.feature_importances_\n        else:\n            # train RF just for feature importance\n            rf_temp = RandomForestClassifier(\n                n_estimators=100, max_depth=5, random_state=args.seed\n            )\n            rf_temp.fit(scaler.transform(X), y)\n            importances = rf_temp.feature_importances_\n\n        feat_imp = sorted(zip(feature_names, importances), key=lambda x: -x[1])\n        print(f\"\\n  Feature importance (RF):\")\n        for fname, imp in feat_imp:\n            print(f\"    {fname}: {imp:.4f}\")\n\n        elapsed = time.time() - t0\n\n        # ---- Build dataset result ----\n        ds_result = {\n            \"dataset\": dname,\n            \"data_path\": dpath,\n            \"n_instances\": len(instances),\n            \"max_n\": max_n,\n            \"n_subsamples\": args.n_subsamples,\n            \"budget_per_instance\": args.budget_per_instance,\n            \"seed\": args.seed,\n            \"elapsed_seconds\": round(elapsed, 1),\n            \"mean_f1_by_n\": {str(n): round(v, 4) for n, v in mean_f1_by_n.items()},\n            \"optimal_n_distribution\": {str(n): int(c) for n, c in dist.items()},\n            \"mean_optimal_n\": round(float(optimal_ns_arr.mean()), 2),\n            \"cv_results\": cv_results,\n            \"best_model\": best_model_name,\n            \"feature_importance\": {fn: round(float(imp), 4) for fn, imp in feat_imp},\n            \"evaluation\": {\n                \"greedy_f1\": round(greedy_f1, 4),\n                \"uniform_f1\": round(uniform_f1, 4),\n                \"adaptive_f1\": round(adaptive_f1, 4),\n                \"oracle_adaptive_f1\": round(oracle_f1, 4),\n                \"full_n_f1\": round(full_f1, 4),\n                \"delta_adaptive_vs_uniform\": round(adaptive_f1 - uniform_f1, 4),\n                \"delta_oracle_vs_uniform\": round(oracle_f1 - uniform_f1, 4),\n                \"adaptive_avg_n\": round(adaptive_avg_n, 2),\n                \"oracle_avg_n\": round(oracle_avg_n, 2),\n                \"adaptive_allocation_dist\": {str(n): int(c) for n, c in adapted_dist.items()},\n                \"adaptive_total_budget\": adaptive_total,\n            },\n        }\n        all_results[dname] = ds_result\n\n        # save per-instance details\n        per_instance = []\n        for i, inst in enumerate(instances):\n            per_instance.append({\n                \"text\": inst.get(\"text\", \"\")[:100],\n                \"features\": features_list[i],\n                \"f1_by_n\": {str(n): round(inst_f1_by_n[i][n], 4) for n in valid_ns},\n                \"optimal_n\": optimal_ns[i],\n                \"predicted_n\": predicted_ns[i],\n                \"adapted_n\": adapted_ns[i],\n            })\n\n        detail_path = os.path.join(args.output_dir, f\"instance_details_{dname}.jsonl\")\n        with open(detail_path, \"w\") as f:\n            for item in per_instance:\n                f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n        print(f\"\\n  Saved instance details: {detail_path}\")\n\n    # ---- Save aggregate results ----\n    out_path = os.path.join(args.output_dir, \"asb_results.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n    # ---- Print summary ----\n    print(f\"\\n{'='*70}\")\n    print(\"ASB Adaptive Sample Budget — Summary\")\n    print(f\"{'='*70}\")\n    for dname, res in all_results.items():\n        ev = res[\"evaluation\"]\n        print(f\"\\n  {dname}:\")\n        print(f\"    Instances: {res['n_instances']}\")\n        print(f\"    Uniform N={args.budget_per_instance}: F1={ev['uniform_f1']:.4f}\")\n        print(f\"    Adaptive:         F1={ev['adaptive_f1']:.4f} (Δ={ev['delta_adaptive_vs_uniform']:+.4f})\")\n        print(f\"    Oracle:           F1={ev['oracle_adaptive_f1']:.4f} (Δ={ev['delta_oracle_vs_uniform']:+.4f})\")\n        print(f\"    Best predictor: {res['best_model']} (macro_F1={res['cv_results'][res['best_model']]['macro_f1']:.4f})\")\n        print(f\"    Optimal N dist: {res['optimal_n_distribution']}\")\n\n    print(f\"\\n  NOTE: This is a CPU-only experiment. No GPU required.\")\n    print(\"DONE\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

语法检查：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "7c5dced3-23a5-4f97-8bb3-ab8d054da20b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDDw7f8PApfvLj4MokH2SU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7849,
      "cache_read_input_tokens": 45750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7849
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Ky9To4a5kmQZZ8ydG33ua9`</summary>

```json
{
  "command": "python3 -m py_compile artifacts/experiments/asb/run_asb.py && echo \"SYNTAX OK\"",
  "description": "Check Python syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "cf56a854-e57b-4072-93bf-5320a11a8601",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDDw7f8PApfvLj4MokH2SU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7849,
      "cache_read_input_tokens": 45750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7849
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

_source line 24 · 2026-05-20T16:30:32.768Z_

<details><summary>↩ Tool result · `toolu_01Ky9To4a5kmQZZ8ydG33ua9`</summary>

```text
SYNTAX OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "76eef970-9947-4be8-b758-7432cb2e9c6e",
  "tool_use_result": {
    "stdout": "SYNTAX OK",
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

_source line 25_

脚本已写入 `artifacts/experiments/asb/run_asb.py`，语法正确。

**产出概要：**
- 5 个 Phase 完整实现：subsampling → instance features → optimal N labels → predictor 训练 (LR/RF/MLP, 5-fold CV) → budget-constrained evaluation
- 支持多数据集（逗号分隔 `--data_paths` / `--dataset_names`）
- 输出 `asb_results.json`（聚合结果）+ `instance_details_{dataset}.jsonl`（逐 instance 细节）
- 包含 oracle adaptive baseline 和 feature importance 分析
- **CPU-only 实验，不需要 GPU**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "uuid": "e341d36e-2201-4b64-9d97-8a8e018f9d9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196PW3wzsm3FhD6ykrmcHEd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 53599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 222
      },
      "output_tokens": 4,
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

_source line 26_

脚本已写入 `artifacts/experiments/asb/run_asb.py`，语法正确。

**产出概要：**
- 5 个 Phase 完整实现：subsampling → instance features → optimal N labels → predictor 训练 (LR/RF/MLP, 5-fold CV) → budget-constrained evaluation
- 支持多数据集（逗号分隔 `--data_paths` / `--dataset_names`）
- 输出 `asb_results.json`（聚合结果）+ `instance_details_{dataset}.jsonl`（逐 instance 细节）
- 包含 oracle adaptive baseline 和 feature importance 分析
- **CPU-only 实验，不需要 GPU**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 150671,
  "duration_api_ms": 154163,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "5f669952-6b4a-4bbf-badf-9b0aeea94e27",
  "total_cost_usd": 0.623735,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 41980,
    "cache_read_input_tokens": 261578,
    "output_tokens": 9130,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41980,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 196,
        "cache_read_input_tokens": 53599,
        "cache_creation_input_tokens": 222,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 222
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2206,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0022760000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 9130,
      "cacheReadInputTokens": 261578,
      "cacheCreationInputTokens": 41980,
      "webSearchRequests": 0,
      "costUSD": 0.6214590000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6085a982-c101-4a2f-9c4c-7f0e708a33c1"
}
```

</details>

---
