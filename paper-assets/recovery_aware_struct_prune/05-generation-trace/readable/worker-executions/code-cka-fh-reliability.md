# code cka fh reliability

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_code_cka_fh_reliability_20260515T031935.log`
- **Structured JSON:** [`b2a73e35fcc43d7d554b.json`](../../sessions/b2/b2a73e35fcc43d7d554b.json)

## Before a recorded user message

22 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
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
  "uuid": "af5c7f78-51c1-4576-b912-86a43a343f69",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778815200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d59e045b-3593-470c-a945-1bcb33bec9da",
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7"
}
```

---

### Assistant

_source line 4_

I'll start by reading the two key source files to understand the current implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "51aeee06-9402-44ae-abb1-d1207b113ab3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmUarVV8HJZWcn6X6evjzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
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

<details open><summary>🔧 Tool call — Read · `toolu_0168geaabRKUvWMpX9Sy3Nzg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "2ecaadf3-5252-4d85-bcdf-774bf3d31838",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmUarVV8HJZWcn6X6evjzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
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

_source line 6 · 2026-05-15T03:19:47.230Z_

<details><summary>↩ Tool result · `toolu_0168geaabRKUvWMpX9Sy3Nzg`</summary>

```text
1	"""
2	CKA Reliability Analysis for RASP.
3	
4	Validates the stability of cross-model CKA scores (original vs pruned) by:
5	1. Split-half reliability: Spearman rho between CKA scores on two data halves
6	2. Calibration size sensitivity: Spearman rho at different sample sizes vs full
7	
8	Addresses Claim 2: CKA-based structural scoring is reliable and stable.
9	"""
10	
11	import argparse
12	import json
13	import logging
14	import os
15	import random
16	import sys
17	
18	import numpy as np
19	import scipy.stats as stats
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
25	logger = logging.getLogger(__name__)
26	
27	
28	def set_seed(seed):
29	    random.seed(seed)
30	    np.random.seed(seed)
31	    torch.manual_seed(seed)
32	    torch.cuda.manual_seed_all(seed)
33	
34	
35	def linear_cka(X, Y):
36	    """Linear CKA between two activation matrices. X: [n, p], Y: [n, q]."""
37	    X = X - X.mean(0)
38	    Y = Y - Y.mean(0)
39	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
40	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
41	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
42	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
43	
44	
45	def load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):
46	    ds = load_dataset("openai/gsm8k", "main", split="train")
47	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
48	    encodings = []
49	    for example in ds:
50	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
51	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
52	        encodings.append(ids)
53	    return encodings
54	
55	
56	def collect_qproj_activations(model, calibration_data, device):
57	    """Collect per-head q_proj activations, mean-pooled over seq length.
58	    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.
59	    """
60	    n_layers = model.config.num_hidden_layers
61	    head_dim = model.config.hidden_size // model.config.num_attention_heads
62	
63	    q_outputs = {i: [] for i in range(n_layers)}
64	    hooks = []
65	
66	    def make_hook(layer_idx):
67	        def fn(module, inp, out):
68	            q_outputs[layer_idx].append(out.detach().cpu())
69	        return fn
70	
71	    for i in range(n_layers):
72	        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))
73	        hooks.append(h)
74	
75	    model.eval()
76	    with torch.no_grad():
77	        for idx, enc in enumerate(calibration_data):
78	            input_ids = enc["input_ids"].to(device)
79	            attention_mask = enc["attention_mask"].to(device)
80	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
81	            if (idx + 1) % 200 == 0:
82	                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")
83	
84	    for h in hooks:
85	        h.remove()
86	
87	    activations = {}
88	    for layer_idx in range(n_layers):
89	        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]
90	        n_heads = out_dim // head_dim
91	        per_head = []
92	        for t in q_outputs[layer_idx]:
93	            t = t.squeeze(0)  # [seq, n_heads * head_dim]
94	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
95	            t = t.mean(dim=0)  # [n_heads, head_dim]
96	            per_head.append(t)
97	        activations[layer_idx] = torch.stack(per_head, dim=0).float()
98	        q_outputs[layer_idx] = None
99	
100	    return activations
101	
102	
103	def load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):
104	    """Load structurally pruned model via base model reconstruction + saved weights."""
105	    meta_path = os.path.join(pruned_model_path, "pruning_metadata.pt")
106	    pruning_meta = torch.load(meta_path, map_location="cpu", weights_only=True)
107	
108	    src_dir = os.path.dirname(os.path.abspath(__file__))
109	    if src_dir not in sys.path:
110	        sys.path.insert(0, src_dir)
111	    from prune import prune_attention_heads, prune_mlp_channels
112	
113	    logging.getLogger("prune").setLevel(logging.WARNING)
114	    model = AutoModelForCausalLM.from_pretrained(
115	        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
116	    )
117	    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
118	    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])
119	
120	    safetensor_files = sorted(
121	        [f for f in os.listdir(pruned_model_path) if f.endswith(".safetensors")]
122	    )
123	    if safetensor_files:
124	        from safetensors.torch import load_file
125	        state_dict = {}
126	        for f in safetensor_files:
127	            state_dict.update(load_file(os.path.join(pruned_model_path, f)))
128	    else:
129	        state_dict = torch.load(
130	            os.path.join(pruned_model_path, "pytorch_model.bin"),
131	            map_location="cpu", weights_only=True,
132	        )
133	    model.load_state_dict(state_dict)
134	    model.to(device)
135	    return model, pruning_meta
136	
137	
138	def compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,
139	                      sample_indices=None):
140	    """Compute per-GQA-group CKA between original and pruned representations.
141	
142	    For each KV group, concatenates retained Q head activations from both models
143	    and computes linear CKA. Original uses all Q heads in the group, pruned uses
144	    only retained Q heads (CKA handles different feature dimensions).
145	
146	    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).
147	    """
148	    heads_per_kv = n_heads_orig // n_kv_heads
149	    n_layers = len(orig_acts)
150	    scores = {}
151	
152	    for layer_idx in range(n_layers):
153	        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]
154	        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]
155	        retained = keep_masks[layer_idx]
156	
157	        if sample_indices is not None:
158	            orig_layer = orig_layer[sample_indices]
159	            pruned_layer = pruned_layer[sample_indices]
160	
161	        for g in range(n_kv_heads):
162	            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))
163	            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]
164	
165	            if not pruned_positions:
166	                scores[(layer_idx, g)] = float("nan")
167	                continue
168	
169	            n = orig_layer.shape[0]
170	            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)
171	            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)
172	            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)
173	
174	    return scores
175	
176	
177	def scores_to_aligned_arrays(scores_a, scores_b):
178	    """Extract aligned non-NaN value arrays from two score dicts."""
179	    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))
180	    a_vals, b_vals = [], []
181	    for k in common:
182	        va, vb = scores_a[k], scores_b[k]
183	        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):
184	            continue
185	        a_vals.append(va)
186	        b_vals.append(vb)
187	    return np.array(a_vals), np.array(b_vals)
188	
189	
190	def main():
191	    parser = argparse.ArgumentParser(description="CKA Reliability Analysis for RASP scoring")
192	    parser.add_argument("--original_model", type=str, required=True)
193	    parser.add_argument("--pruned_model", type=str, required=True)
194	    parser.add_argument("--gpu_id", type=int, default=0)
195	    parser.add_argument("--num_samples", type=int, default=1024)
196	    parser.add_argument("--max_length", type=int, default=512)
197	    parser.add_argument("--n_splits", type=int, default=5)
198	    parser.add_argument("--output", type=str, required=True)
199	    parser.add_argument("--seed", type=int, default=42)
200	    parser.add_argument("--dtype", type=str, default="bfloat16",
201	                        choices=["float16", "bfloat16", "float32"])
202	    args = parser.parse_args()
203	
204	    set_seed(args.seed)
205	    device = torch.device(f"cuda:{args.gpu_id}" if torch.cuda.is_available() else "cpu")
206	    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
207	                   "float32": torch.float32}[args.dtype]
208	
209	    logger.info("Loading tokenizer and calibration data...")
210	    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)
211	    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,
212	                                             args.seed)
213	    n_total = len(calibration_data)
214	    logger.info(f"Loaded {n_total} calibration samples")
215	
216	    # --- Collect activations (load models one at a time to save GPU memory) ---
217	    logger.info("Loading original model...")
218	    orig_model = AutoModelForCausalLM.from_pretrained(
219	        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True
220	    )
221	    config = orig_model.config
222	    n_heads_orig = config.num_attention_heads
223	    n_kv_heads = config.num_key_value_heads
224	    n_layers = config.num_hidden_layers
225	    heads_per_kv = n_heads_orig // n_kv_heads
226	    logger.info(f"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV "
227	                f"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)")
228	
229	    logger.info("Collecting original model activations...")
230	    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)
231	    del orig_model
232	    torch.cuda.empty_cache()
233	    logger.info("Original model freed.")
234	
235	    logger.info("Loading pruned model...")
236	    pruned_model, pruning_meta = load_pruned_model_with_meta(
237	        args.original_model, args.pruned_model, torch_dtype, device
238	    )
239	    keep_masks = pruning_meta["attn_keep_masks"]
240	    logger.info("Collecting pruned model activations...")
241	    pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)
242	    del pruned_model
243	    torch.cuda.empty_cache()
244	    logger.info("Pruned model freed. All activations cached on CPU.")
245	
246	    # --- Phase 1: Full CKA scores ---
247	    logger.info("=" * 50)
248	    logger.info("Phase 1: Full CKA scores (N=%d)...", n_total)
249	    full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
250	                                    n_heads_orig, n_kv_heads)
251	    valid_scores = {k: v for k, v in full_scores.items()
252	                    if not (isinstance(v, float) and v != v)}
253	    vals = np.array(list(valid_scores.values()))
254	    logger.info(f"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}")
255	    logger.info(f"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, "
256	                f"range=[{vals.min():.4f}, {vals.max():.4f}]")
257	
258	    # --- Phase 2: Split-half reliability ---
259	    logger.info("=" * 50)
260	    logger.info("Phase 2: Split-half reliability (%d splits)...", args.n_splits)
261	    split_results = []
262	    for i in range(args.n_splits):
263	        rng = np.random.RandomState(args.seed + i)
264	        perm = rng.permutation(n_total)
265	        half = n_total // 2
266	        idx_a = sorted(perm[:half].tolist())
267	        idx_b = sorted(perm[half:2 * half].tolist())
268	
269	        scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,
270	                                     n_heads_orig, n_kv_heads, idx_a)
271	        scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,
272	                                     n_heads_orig, n_kv_heads, idx_b)
273	        arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)
274	        rho, p = stats.spearmanr(arr_a, arr_b)
275	        split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
276	                              "n_groups": len(arr_a)})
277	        logger.info(f"  Split {i}: rho={rho:.4f}, p={p:.2e}")
278	
279	    mean_rho = float(np.mean([r["rho"] for r in split_results]))
280	    std_rho = float(np.std([r["rho"] for r in split_results]))
281	
282	    # --- Phase 3: Calibration size sensitivity ---
283	    logger.info("=" * 50)
284	    logger.info("Phase 3: Calibration size sensitivity...")
285	    size_results = []
286	    for n_sub in [128, 256, 512]:
287	        if n_sub >= n_total:
288	            continue
289	        rng = np.random.RandomState(args.seed)
290	        sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())
291	
292	        sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
293	                                       n_heads_orig, n_kv_heads, sub_idx)
294	        ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)
295	        rho, p = stats.spearmanr(ref_vals, sub_vals)
296	        size_results.append({"n_samples": n_sub, "rho_vs_full": float(rho),
297	                             "p_value": float(p)})
298	        logger.info(f"  N={n_sub}: rho={rho:.4f} vs N={n_total}")
299	
300	    # --- Compile and save results ---
301	    per_group = {}
302	    for (l, g), v in full_scores.items():
303	        key = f"layer{l}_group{g}"
304	        per_group[key] = None if (isinstance(v, float) and v != v) else float(v)
305	
306	    output = {
307	        "config": {
308	            "original_model": args.original_model,
309	            "pruned_model": args.pruned_model,
310	            "num_samples": n_total,
311	            "n_layers": n_layers,
312	            "n_heads_original": n_heads_orig,
313	            "n_kv_heads": n_kv_heads,
314	            "heads_per_kv": heads_per_kv,
315	            "total_gqa_groups": n_layers * n_kv_heads,
316	            "valid_gqa_groups": len(valid_scores),
317	            "seed": args.seed,
318	        },
319	        "per_group_cka_scores": per_group,
320	        "cka_summary": {
321	            "mean": float(vals.mean()),
322	            "std": float(vals.std()),
323	            "min": float(vals.min()),
324	            "max": float(vals.max()),
325	            "median": float(np.median(vals)),
326	        },
327	        "split_half_reliability": {
328	            "per_split": split_results,
329	            "mean_rho": mean_rho,
330	            "std_rho": std_rho,
331	            "pass": mean_rho > 0.9,
332	        },
333	        "size_sensitivity": {
334	            "reference_n": n_total,
335	            "per_size": size_results,
336	            "all_pass_0.9": all(s["rho_vs_full"] > 0.9 for s in size_results),
337	        },
338	    }
339	
340	    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
341	    with open(args.output, "w") as f:
342	        json.dump(output, f, indent=2)
343	    logger.info(f"Results saved to {args.output}")
344	
345	    print(f"\n{'=' * 60}")
346	    print("CKA Reliability Analysis")
347	    print(f"{'=' * 60}")
348	    print(f"GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid")
349	    print(f"CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} "
350	          f"[{vals.min():.4f}, {vals.max():.4f}]")
351	    sh_pass = "PASS" if mean_rho > 0.9 else "FAIL"
352	    print(f"\nSplit-half reliability ({args.n_splits} splits):")
353	    print(f"  rho = {mean_rho:.4f} +/- {std_rho:.4f}  {sh_pass} (threshold: 0.9)")
354	    for r in split_results:
355	        print(f"    Split {r['split']}: rho={r['rho']:.4f}")
356	    print(f"\nSize sensitivity (vs N={n_total}):")
357	    for s in size_results:
358	        sv = "PASS" if s["rho_vs_full"] > 0.9 else "FAIL"
359	        print(f"  N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}")
360	    print(f"{'=' * 60}")
361	
362	
363	if __name__ == "__main__":
364	    main()
365	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "58188b1d-d4b7-43e0-a3a1-a4099b65d99e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
      "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of cross-model CKA scores (original vs pruned) by:\n1. Split-half reliability: Spearman rho between CKA scores on two data halves\n2. Calibration size sensitivity: Spearman rho at different sample sizes vs full\n\nAddresses Claim 2: CKA-based structural scoring is reliable and stable.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, required=True)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Collect activations (load models one at a time to save GPU memory) ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed.\")\n\n    logger.info(\"Loading pruned model...\")\n    pruned_model, pruning_meta = load_pruned_model_with_meta(\n        args.original_model, args.pruned_model, torch_dtype, device\n    )\n    keep_masks = pruning_meta[\"attn_keep_masks\"]\n    logger.info(\"Collecting pruned model activations...\")\n    pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n    del pruned_model\n    torch.cuda.empty_cache()\n    logger.info(\"Pruned model freed. All activations cached on CPU.\")\n\n    # --- Phase 1: Full CKA scores ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n    full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                    n_heads_orig, n_kv_heads)\n    valid_scores = {k: v for k, v in full_scores.items()\n                    if not (isinstance(v, float) and v != v)}\n    vals = np.array(list(valid_scores.values()))\n    logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n    logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n    # --- Phase 2: Split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n    split_results = []\n    for i in range(args.n_splits):\n        rng = np.random.RandomState(args.seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                     n_heads_orig, n_kv_heads, idx_a)\n        scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                     n_heads_orig, n_kv_heads, idx_b)\n        arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n        rho, p = stats.spearmanr(arr_a, arr_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_groups\": len(arr_a)})\n        logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n    mean_rho = float(np.mean([r[\"rho\"] for r in split_results]))\n    std_rho = float(np.std([r[\"rho\"] for r in split_results]))\n\n    # --- Phase 3: Calibration size sensitivity ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 3: Calibration size sensitivity...\")\n    size_results = []\n    for n_sub in [128, 256, 512]:\n        if n_sub >= n_total:\n            continue\n        rng = np.random.RandomState(args.seed)\n        sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n        sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                       n_heads_orig, n_kv_heads, sub_idx)\n        ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n        rho, p = stats.spearmanr(ref_vals, sub_vals)\n        size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                             \"p_value\": float(p)})\n        logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n    # --- Compile and save results ---\n    per_group = {}\n    for (l, g), v in full_scores.items():\n        key = f\"layer{l}_group{g}\"\n        per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"pruned_model\": args.pruned_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"valid_gqa_groups\": len(valid_scores),\n            \"seed\": args.seed,\n        },\n        \"per_group_cka_scores\": per_group,\n        \"cka_summary\": {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        },\n        \"split_half_reliability\": {\n            \"per_split\": split_results,\n            \"mean_rho\": mean_rho,\n            \"std_rho\": std_rho,\n            \"pass\": mean_rho > 0.9,\n        },\n        \"size_sensitivity\": {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        },\n    }\n\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n    print(f\"GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n    print(f\"CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n          f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n    sh_pass = \"PASS\" if mean_rho > 0.9 else \"FAIL\"\n    print(f\"\\nSplit-half reliability ({args.n_splits} splits):\")\n    print(f\"  rho = {mean_rho:.4f} +/- {std_rho:.4f}  {sh_pass} (threshold: 0.9)\")\n    for r in split_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n    print(f\"\\nSize sensitivity (vs N={n_total}):\")\n    for s in size_results:\n        sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n        print(f\"  N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 365,
      "startLine": 1,
      "totalLines": 365
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01NwDwYC8CC1JM8Ff1cyNvXE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "55167162-83a3-4730-bb98-92de7417b704",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PmUarVV8HJZWcn6X6evjzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
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

_source line 8 · 2026-05-15T03:19:47.549Z_

<details><summary>↩ Tool result · `toolu_01NwDwYC8CC1JM8Ff1cyNvXE`</summary>

```text
1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
59	        encodings.append(ids)
60	    return encodings
61	
62	
63	def collect_head_activations(model, tokenizer, calibration_data, device):
64	    """Run calibration data through model and collect per-head activations for each layer.
65	
66	    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
67	    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
68	    """
69	    config = model.config
70	    n_layers = config.num_hidden_layers
71	    n_heads = config.num_attention_heads
72	    head_dim = config.hidden_size // n_heads
73	
74	    layer_activations = {i: [] for i in range(n_layers)}
75	    hooks = []
76	
77	    def make_hook(layer_idx):
78	        def hook_fn(module, input, output):
79	            # output of attention: (hidden_states, attn_weights, past_kv)
80	            # We hook into q_proj to get query states, then reshape per-head
81	            pass
82	        return hook_fn
83	
84	    # Hook into each attention layer's output (the hidden_states after o_proj)
85	    # We instead hook the q_proj to capture per-head representations
86	    q_proj_outputs = {i: [] for i in range(n_layers)}
87	
88	    def make_q_hook(layer_idx):
89	        def hook_fn(module, input, output):
90	            # output shape: [batch, seq_len, n_heads * head_dim]
91	            q_proj_outputs[layer_idx].append(output.detach())
92	        return hook_fn
93	
94	    for i in range(n_layers):
95	        layer = model.model.layers[i]
96	        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
97	        hooks.append(h)
98	
99	    model.eval()
100	    with torch.no_grad():
101	        for batch_idx, enc in enumerate(calibration_data):
102	            input_ids = enc["input_ids"].to(device)
103	            attention_mask = enc["attention_mask"].to(device)
104	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
105	            if (batch_idx + 1) % 50 == 0:
106	                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
107	
108	    for h in hooks:
109	        h.remove()
110	
111	    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
112	    for layer_idx in range(n_layers):
113	        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
114	        per_head_list = []
115	        for t in tensors:
116	            t = t.squeeze(0)  # [seq, n_heads*head_dim]
117	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
118	            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
119	            per_head_list.append(t)
120	        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
121	        q_proj_outputs[layer_idx] = None  # free memory
122	
123	    return layer_activations
124	
125	
126	def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
127	    """Collect MLP intermediate activations grouped into channel groups.
128	
129	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
130	    """
131	    config = model.config
132	    n_layers = config.num_hidden_layers
133	    intermediate_size = config.intermediate_size
134	    group_size = intermediate_size // n_groups
135	
136	    gate_outputs = {i: [] for i in range(n_layers)}
137	    hooks = []
138	
139	    def make_gate_hook(layer_idx):
140	        def hook_fn(module, input, output):
141	            gate_outputs[layer_idx].append(output.detach())
142	        return hook_fn
143	
144	    for i in range(n_layers):
145	        layer = model.model.layers[i]
146	        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
147	        hooks.append(h)
148	
149	    model.eval()
150	    with torch.no_grad():
151	        for enc in calibration_data:
152	            input_ids = enc["input_ids"].to(device)
153	            attention_mask = enc["attention_mask"].to(device)
154	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
155	
156	    for h in hooks:
157	        h.remove()
158	
159	    layer_activations = {}
160	    for layer_idx in range(n_layers):
161	        tensors = gate_outputs[layer_idx]
162	        per_group_list = []
163	        for t in tensors:
164	            t = t.squeeze(0)  # [seq, intermediate_size]
165	            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
166	            # Truncate to exact multiple of group_size
167	            usable = n_groups * group_size
168	            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
169	            per_group_list.append(t)
170	        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
171	        gate_outputs[layer_idx] = None
172	
173	    return layer_activations
174	
175	
176	def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
177	    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.
178	
179	    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
180	    Returns: (overlap_scores, cka_matrices)
181	        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
182	        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
183	    """
184	    overlap_scores = {}
185	    cka_matrices = {}
186	    for layer_idx, acts in activations_dict.items():
187	        n_samples, n_structs, dim = acts.shape
188	        matrix = torch.zeros(n_structs, n_structs)
189	        for i in range(n_structs):
190	            matrix[i, i] = 1.0
191	            for j in range(i + 1, n_structs):
192	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
193	                matrix[i, j] = val
194	                matrix[j, i] = val
195	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
196	        overlap_scores[layer_idx] = scores
197	        cka_matrices[layer_idx] = matrix
198	        logger.info(
199	            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
200	            f"mean={scores.mean():.4f}"
201	        )
202	    return overlap_scores, cka_matrices
203	
204	
205	def main():
206	    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
207	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
208	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
209	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
210	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
211	    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
212	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
213	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
214	    args = parser.parse_args()
215	
216	    set_seed(args.seed)
217	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
218	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
219	    torch_dtype = dtype_map[args.dtype]
220	
221	    logger.info(f"Loading model from {args.model_path}")
222	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
223	    model = AutoModelForCausalLM.from_pretrained(
224	        args.model_path,
225	        torch_dtype=torch_dtype,
226	        device_map=device,
227	        trust_remote_code=True,
228	    )
229	
230	    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
231	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
232	
233	    logger.info("Collecting attention head activations...")
234	    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)
235	
236	    logger.info("Computing attention head overlap F(h)...")
237	    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
238	    del head_acts
239	    torch.cuda.empty_cache()
240	
241	    logger.info("Collecting MLP activations...")
242	    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)
243	
244	    logger.info("Computing MLP group overlap F(h)...")
245	    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
246	    del mlp_acts
247	    torch.cuda.empty_cache()
248	
249	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
250	    result = {
251	        "attn_overlap": attn_overlap,
252	        "mlp_overlap": mlp_overlap,
253	        "attn_cka_matrix": attn_cka_matrix,
254	        "mlp_cka_matrix": mlp_cka_matrix,
255	    }
256	    torch.save(result, args.output_path)
257	    logger.info(f"Saved CKA overlap scores to {args.output_path}")
258	
259	
260	if __name__ == "__main__":
261	    main()
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "ea830610-4c5b-491e-a909-4b613a597ea5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py",
      "content": "\"\"\"\nCKA Overlap Computation for RASP.\n\nComputes intra-layer functional overlap F(h) for each attention head and MLP channel group\nusing linear CKA (Centered Kernel Alignment via HSIC).\n\nInput:  model + calibration data (GSM8K train subset)\nOutput: per-structure F(h) scores saved as dict in .pt file\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\n\"\"\"\n\nimport argparse\nimport logging\nimport math\nimport os\nimport random\n\nimport numpy as np\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\n    \"\"\"Linear CKA between two activation matrices.\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\n    \"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    \"\"\"Load GSM8K train questions as calibration prompts.\"\"\"\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_head_activations(model, tokenizer, calibration_data, device):\n    \"\"\"Run calibration data through model and collect per-head activations for each layer.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]\n    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    head_dim = config.hidden_size // n_heads\n\n    layer_activations = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output of attention: (hidden_states, attn_weights, past_kv)\n            # We hook into q_proj to get query states, then reshape per-head\n            pass\n        return hook_fn\n\n    # Hook into each attention layer's output (the hidden_states after o_proj)\n    # We instead hook the q_proj to capture per-head representations\n    q_proj_outputs = {i: [] for i in range(n_layers)}\n\n    def make_q_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output shape: [batch, seq_len, n_heads * head_dim]\n            q_proj_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for batch_idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (batch_idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]\n    for layer_idx in range(n_layers):\n        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]\n        per_head_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, n_heads*head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq\n            per_head_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]\n        q_proj_outputs[layer_idx] = None  # free memory\n\n    return layer_activations\n\n\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\n    \"\"\"Collect MLP intermediate activations grouped into channel groups.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    intermediate_size = config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_gate_hook(layer_idx):\n        def hook_fn(module, input, output):\n            gate_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for enc in calibration_data:\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n\n    for h in hooks:\n        h.remove()\n\n    layer_activations = {}\n    for layer_idx in range(n_layers):\n        tensors = gate_outputs[layer_idx]\n        per_group_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq\n            # Truncate to exact multiple of group_size\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]\n            per_group_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]\n        gate_outputs[layer_idx] = None\n\n    return layer_activations\n\n\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\n    \"\"\"Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.\n\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\n    Returns: (overlap_scores, cka_matrices)\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\n    \"\"\"\n    overlap_scores = {}\n    cka_matrices = {}\n    for layer_idx, acts in activations_dict.items():\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        overlap_scores[layer_idx] = scores\n        cka_matrices[layer_idx] = matrix\n        logger.info(\n            f\"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], \"\n            f\"mean={scores.mean():.4f}\"\n        )\n    return overlap_scores, cka_matrices\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Compute CKA-based functional overlap scores for RASP\")\n    parser.add_argument(\"--model_path\", type=str, required=True, help=\"Path to pretrained model\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output .pt file for overlap scores\")\n    parser.add_argument(\"--n_samples\", type=int, default=512, help=\"Number of calibration samples\")\n    parser.add_argument(\"--max_length\", type=int, default=512, help=\"Max token length for calibration inputs\")\n    parser.add_argument(\"--mlp_groups\", type=int, default=28, help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\", choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    dtype_map = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16, \"float32\": torch.float32}\n    torch_dtype = dtype_map[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch_dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n\n    logger.info(f\"Loading {args.n_samples} calibration samples from GSM8K train\")\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\n\n    logger.info(\"Collecting attention head activations...\")\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\n\n    logger.info(\"Computing attention head overlap F(h)...\")\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \"attn_heads\")\n    del head_acts\n    torch.cuda.empty_cache()\n\n    logger.info(\"Collecting MLP activations...\")\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\n\n    logger.info(\"Computing MLP group overlap F(h)...\")\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \"mlp_groups\")\n    del mlp_acts\n    torch.cuda.empty_cache()\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    result = {\n        \"attn_overlap\": attn_overlap,\n        \"mlp_overlap\": mlp_overlap,\n        \"attn_cka_matrix\": attn_cka_matrix,\n        \"mlp_cka_matrix\": mlp_cka_matrix,\n    }\n    torch.save(result, args.output_path)\n    logger.info(f\"Saved CKA overlap scores to {args.output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 262,
      "startLine": 1,
      "totalLines": 262
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both files. Let me plan the modifications to `run_cka_reliability.py`:

1. Add `--mlp_groups` (default=28) and `--skip_cross_model` CLI args
2. Make `--pruned_model` not required (since `--skip_cross_model` doesn't need it)
3. Add Phase 4: F(h) split-half reliability for attention heads
4. Add Phase 5: F(h) split-half reliability for MLP groups
5. Add output JSON fields `fh_attn_reliability` and `fh_mlp_reliability`


6. For the split-half reliability phases, I'll leverage the existing activation collection methods—`collect_qproj_activations` already gives me per-head format, and I'll create a corresponding MLP activation collector. The split-half approach divides the calibration data in half, computes F(h) independently on each half, then measures the correlation between the resulting rankings using Spearman's ρ. The `compute_overlap` function from `cka_overlap.py` handles the F(h) computation, taking activations organized by layer and returning F values per structure.

For Phase 4 specifically, I'm starting with the original model's attention activations already in the right format, then for each data split I'll partition the samples and compute the pairwise CKA matrix among heads...

Computing CKA matrices across head pairs... what we need for F(h) computation. For the MLP layers, I'll need to add a collection function similar to what's in `cka_overlap.py`. Then I'll create a `compute_fh_scores` function that takes the activation tensors and computes F(h) values for a given sample subset, returning the scores per structure. I'm also planning to add a `compute_fh_reliability` function to handle the full pipeline.

Now I'm restructuring the main flow: I'll make the pruned model optional since it's only needed for cross-model comparisons, always load the original model and collect both attention and MLP activations, conditionally run the first three phases, and always execute the final two phases. The output JSON will be updated accordingly.

Writing the MLP collection function... Setting up forward hooks to capture gate outputs...

After collecting activations across the calibration data, I'm removing the hooks and processing the captured outputs by layer. For each layer, I'm averaging the gate projections across the sequence dimension, reshaping them into groups, and stacking them together to create the final activation tensors that will be used for computing FH scores.

Now I'm defining the function to compute F(h) scores, which takes the activation dictionary and optional sample indices, then builds a similarity matrix between structures in each layer using linear CKA.

Implementing the reliability check... Finishing the split analysis function and logging results for each iteration. Now I'm considering whether to collect activations in a single forward pass or run separate passes—doing two separate passes is simpler and less error-prone, though it means running the model twice, which would be inefficient if I also need MLP activations. I'm realizing the activation collection strategy needs to account for reusing data across phases. Since the cross-model phase already collects q_proj activations from both models, I can leverage those same activations for the attention F(h) phases rather than re-collecting them. The MLP phases will need their own forward pass to gather gate_proj activations, but I should structure this to minimize redundant model loads and forward passes. Writing the activation collection function... Setting up the forward hooks to capture activations from the attention and MLP layers, then running the calibration data through the model while tracking these outputs. After collecting all the activations, I'm processing the query projection outputs into a per-head format for further analysis.

Processing gate projections into groups...

Actually, I realize `collect_qproj_activations` already returns the exact format I need—a dictionary mapping layer indices to tensors with shape `[n_samples, n_heads, head_dim]`—so I can reuse it for the original model and apply the same cross-model CKA comparisons between original and pruned versions.

Now I'm planning the specific edits to make: I'll add the MLP activation collection function, implement the new scoring functions for Fisher-Hessian analysis, update the argument parser to support MLP grouping and optional pruned model paths, and restructure the main flow to handle both single-model and cross-model phases cleanly. I'm mapping out the restructured main flow now. The key changes are validating that the pruned model is required unless we're skipping cross-model analysis, collecting both q_proj and MLP activations from the original model in one pass, and then conditionally running the cross-model phases only if we have a pruned model available. After that comes a new phase 4 for F-H scores that wasn't in the original flow.

For step 4, I'm deciding between a combined activation collection function versus two separate passes—the combined approach is more efficient since the original model needs both activation types anyway, while the pruned model only needs q_proj. I should create a unified function for the original model but keep the existing separate function for the pruned model to avoid unnecessary changes downstream.

Now I'm weighing whether the complexity is worth it—with 1024 samples and each forward pass taking several minutes, saving one full inference pass is meaningful, so I'll go with the combined approach and hook both q_proj and gate_proj in a single function.

Let me think through the edge case with `--skip_cross_model`...

when it's enabled, I only need per-head activations for F(h), but when it's disabled, I need the original activations for both cross-model CKA and F(h), so the combined function handles both cases cleanly.

Actually, to keep changes minimal and reduce risk, I'll just add a separate `collect_mlp_activations` function and run two forward passes on the original model instead of trying to combine them. I'll collect both activations in two forward passes while keeping the model loaded, then delete it after—the code stays clean and it's a reasonable tradeoff. For the argparse changes, I need to make `--pruned_model` optional and add validation logic.

Now I'm mapping out the specific edits I need to make: inserting the new activation collection function after the existing one, adding the scoring functions, updating the argument parser to include new flags and make `--pruned_model` conditional, then validating the args before the main logic runs. I think using targeted edits is better than rewriting the whole file since the changes are scattered throughout.

Actually, given how many modifications are needed in the main function itself, I should just rewrite the entire file to avoid fragile edit operations. Let me compose the full modified version with all the new functions, updated argument parsing, and restructured main logic.

Writing the complete file... I'm setting up utility functions for a model analysis pipeline—defining a seed setter for reproducibility, implementing linear CKA to measure activation similarity between layers, and loading calibration data from the GSM8K dataset. Now I'm working on a function to collect Q-projection activations from the model...

Collecting activations... Writing activation collection code... Now I'm processing the gate outputs for each layer—squeezing and averaging them, then reshaping into groups before stacking them together as float tensors. After that I'm moving on to compute the F(h) scores across the structures using the activation dictionaries.

Computing the similarity matrix... Now I'm computing F(h) scores separately on each half of the split data, then extracting all the layer values and calculating their Spearman correlation to measure reliability across the splits.

Setting up the main function... Setting up the data pipeline and model loading...

Now I'm extracting the model architecture details—layer count, attention heads, and key-value head configuration—then collecting the activation patterns from both the query projections and MLP gate projections across the calibration dataset.

Freeing up memory after collecting activations, then building a configuration dictionary that captures all the key model parameters and settings. If cross-model comparison is enabled, I'll load the pruned model next to compare activation patterns between the original and compressed versions. Now I'm filtering out invalid scores and computing statistics across the valid groups to see how well the pruned model's attention patterns match the original. Then I'm moving into phase 2 to assess the reliability of these CKA scores by running multiple random splits of the calibration data.

For each split, I'm dividing the data in half, computing CKA scores separately for each half, and then calculating the Spearman correlation between the two halves to measure consistency.

Now I'm moving into phase 3 where I'm testing how sensitive the results are to different calibration set sizes—trying 128, 256, and 512 samples and skipping any that exceed the total available data.

For each subset size, I'm computing the CKA scores between the original and pruned activations, then comparing those scores against the full dataset using Spearman correlation to see how well the smaller calibration sets approximate the full results. After cleaning up memory, I'm preparing to add these cross-model findings to the final output.

Building output structure...

Now I'm moving into phase 4 to compute split-half reliability metrics specifically for attention heads, running the analysis across multiple splits to assess consistency. Still writing reliability checks... Printing the split-half reliability results with correlation coefficients and pass/fail status for each split, then checking the size sensitivity analysis to see how CKA scores hold up across different sample sizes, and finally moving into the attention head reliability metrics. Finishing the output formatting...

Now I'm thinking through the seeding strategy — Phase 2 uses `args.seed + i` for cross-model splits, and Phase 4-5 also use the same seed offset for their internal splits. That's actually fine since they're measuring different things, so having consistent split indices across phases makes them more comparable. Though I should double-check whether different seeds would be better here.

Actually, re-reading the requirements, it's clear I need to do n_splits iterations with the same seed-based approach and report mean reliability. The current plan of using `args.seed + i` consistently across phases works well. Let me write out the full implementation now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "600ce7e2-7bdc-49cc-8ab2-34a1ca465f10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGoNHr7v1C5njHKrprKUix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10047
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

_source line 10_

Now I have a clear picture of both files. I'll rewrite `run_cka_reliability.py` with the new phases and CLI args.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "f03af052-34af-4564-a580-b28c40a2bb67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGoNHr7v1C5njHKrprKUix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10047
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

_source line 11_

<details open><summary>🔧 Tool call — Write · `toolu_017HAhXpPCH9V3SRMNM9aBbV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
  "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of structural scoring by:\n1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)\n4.   F(h) split-half reliability for attention heads (intra-layer overlap)\n5.   F(h) split-half reliability for MLP groups (intra-layer overlap)\n\nPhases 1-3 address cross-model CKA stability.\nPhases 4-5 address intra-layer F(h) stability (Claim 2 core metric).\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef collect_mlp_activations(model, calibration_data, device, n_groups=28):\n    \"\"\"Collect MLP gate_proj activations grouped into channel groups.\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    intermediate_size = model.config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size]\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)\n            per_group.append(t)\n        activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef compute_fh_scores(acts_dict, sample_indices=None):\n    \"\"\"Compute intra-layer F(h) for each structure.\n    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]\n    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.\n    \"\"\"\n    fh = {}\n    for layer_idx, acts in acts_dict.items():\n        if sample_indices is not None:\n            acts = acts[sample_indices]\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        fh[layer_idx] = scores\n    return fh\n\n\ndef compute_fh_reliability(acts_dict, n_splits, seed, structure_name):\n    \"\"\"Split-half reliability of F(h) rankings across all layers.\n    Returns list of per-split result dicts with Spearman rho.\n    \"\"\"\n    n_total = next(iter(acts_dict.values())).shape[0]\n    split_results = []\n    for i in range(n_splits):\n        rng = np.random.RandomState(seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")\n        fh_a = compute_fh_scores(acts_dict, idx_a)\n        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")\n        fh_b = compute_fh_scores(acts_dict, idx_b)\n\n        vals_a, vals_b = [], []\n        for layer_idx in sorted(fh_a.keys()):\n            vals_a.extend(fh_a[layer_idx].tolist())\n            vals_b.extend(fh_b[layer_idx].tolist())\n\n        rho, p = stats.spearmanr(vals_a, vals_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_structures\": len(vals_a)})\n        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")\n    return split_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, default=None)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    parser.add_argument(\"--mlp_groups\", type=int, default=28,\n                        help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",\n                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")\n    args = parser.parse_args()\n\n    if not args.skip_cross_model and not args.pruned_model:\n        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Load original model and collect all activations ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model q_proj activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n\n    logger.info(\"Collecting original model MLP gate_proj activations...\")\n    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)\n\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed. All activations cached on CPU.\")\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"mlp_groups\": args.mlp_groups,\n            \"seed\": args.seed,\n        },\n    }\n\n    # --- Phase 1-3: Cross-model CKA (optional) ---\n    if not args.skip_cross_model:\n        logger.info(\"Loading pruned model...\")\n        pruned_model, pruning_meta = load_pruned_model_with_meta(\n            args.original_model, args.pruned_model, torch_dtype, device\n        )\n        keep_masks = pruning_meta[\"attn_keep_masks\"]\n        logger.info(\"Collecting pruned model activations...\")\n        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n        del pruned_model\n        torch.cuda.empty_cache()\n        logger.info(\"Pruned model freed.\")\n\n        # Phase 1: Full CKA scores\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                        n_heads_orig, n_kv_heads)\n        valid_scores = {k: v for k, v in full_scores.items()\n                        if not (isinstance(v, float) and v != v)}\n        vals = np.array(list(valid_scores.values()))\n        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n        # Phase 2: Split-half reliability (cross-model)\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n        cross_split_results = []\n        for i in range(args.n_splits):\n            rng = np.random.RandomState(args.seed + i)\n            perm = rng.permutation(n_total)\n            half = n_total // 2\n            idx_a = sorted(perm[:half].tolist())\n            idx_b = sorted(perm[half:2 * half].tolist())\n\n            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_a)\n            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_b)\n            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n            rho, p = stats.spearmanr(arr_a, arr_b)\n            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                                        \"n_groups\": len(arr_a)})\n            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))\n        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))\n\n        # Phase 3: Calibration size sensitivity\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 3: Calibration size sensitivity...\")\n        size_results = []\n        for n_sub in [128, 256, 512]:\n            if n_sub >= n_total:\n                continue\n            rng = np.random.RandomState(args.seed)\n            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                           n_heads_orig, n_kv_heads, sub_idx)\n            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n            rho, p = stats.spearmanr(ref_vals, sub_vals)\n            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                                 \"p_value\": float(p)})\n            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n        del pruned_acts\n        torch.cuda.empty_cache()\n\n        per_group = {}\n        for (l, g), v in full_scores.items():\n            key = f\"layer{l}_group{g}\"\n            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n        output[\"config\"][\"pruned_model\"] = args.pruned_model\n        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)\n        output[\"per_group_cka_scores\"] = per_group\n        output[\"cka_summary\"] = {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        }\n        output[\"split_half_reliability\"] = {\n            \"per_split\": cross_split_results,\n            \"mean_rho\": cross_mean_rho,\n            \"std_rho\": cross_std_rho,\n            \"pass\": cross_mean_rho > 0.9,\n        }\n        output[\"size_sensitivity\"] = {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        }\n\n    # --- Phase 4: F(h) attention head split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",\n                args.n_splits)\n    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")\n    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))\n    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))\n    attn_pass = attn_mean_rho > 0.9\n    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"\n                f\"{'PASS' if attn_pass else 'FAIL'}\")\n\n    output[\"fh_attn_reliability\"] = {\n        \"per_split\": attn_fh_results,\n        \"mean_rho\": attn_mean_rho,\n        \"std_rho\": attn_std_rho,\n        \"pass\": attn_pass,\n    }\n\n    del orig_acts\n    torch.cuda.empty_cache()\n\n    # --- Phase 5: F(h) MLP group split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)\n    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")\n    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_pass = mlp_mean_rho > 0.9\n    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"\n                f\"{'PASS' if mlp_pass else 'FAIL'}\")\n\n    output[\"fh_mlp_reliability\"] = {\n        \"per_split\": mlp_fh_results,\n        \"mean_rho\": mlp_mean_rho,\n        \"std_rho\": mlp_std_rho,\n        \"pass\": mlp_pass,\n    }\n\n    del orig_mlp_acts\n    torch.cuda.empty_cache()\n\n    # --- Save results ---\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    # --- Print summary ---\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n\n    if not args.skip_cross_model:\n        print(f\"\\nCross-model CKA (Phase 1-3):\")\n        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n              f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"\n        print(f\"  Split-half reliability ({args.n_splits} splits):\")\n        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"\n              f\"(threshold: 0.9)\")\n        for r in cross_split_results:\n            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")\n        print(f\"  Size sensitivity (vs N={n_total}):\")\n        for s in size_results:\n            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n\n    print(f\"\\nF(h) Attention head reliability (Phase 4):\")\n    ah_label = \"PASS\" if attn_pass else \"FAIL\"\n    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")\n    for r in attn_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"\\nF(h) MLP group reliability (Phase 5):\")\n    mh_label = \"PASS\" if mlp_pass else \"FAIL\"\n    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")\n    for r in mlp_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "37f1edc9-965b-418f-80ba-de21112f2fa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGoNHr7v1C5njHKrprKUix",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10047
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

_source line 12 · 2026-05-15T03:24:37.583Z_

<details><summary>↩ Tool result · `toolu_017HAhXpPCH9V3SRMNM9aBbV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "1e3ed86d-5c63-4a15-8b04-c4e236cf285a",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py",
    "content": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of structural scoring by:\n1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)\n4.   F(h) split-half reliability for attention heads (intra-layer overlap)\n5.   F(h) split-half reliability for MLP groups (intra-layer overlap)\n\nPhases 1-3 address cross-model CKA stability.\nPhases 4-5 address intra-layer F(h) stability (Claim 2 core metric).\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef collect_mlp_activations(model, calibration_data, device, n_groups=28):\n    \"\"\"Collect MLP gate_proj activations grouped into channel groups.\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    intermediate_size = model.config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            gate_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        per_group = []\n        for t in gate_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size]\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)\n            per_group.append(t)\n        activations[layer_idx] = torch.stack(per_group, dim=0).float()\n        gate_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef compute_fh_scores(acts_dict, sample_indices=None):\n    \"\"\"Compute intra-layer F(h) for each structure.\n    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]\n    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.\n    \"\"\"\n    fh = {}\n    for layer_idx, acts in acts_dict.items():\n        if sample_indices is not None:\n            acts = acts[sample_indices]\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        fh[layer_idx] = scores\n    return fh\n\n\ndef compute_fh_reliability(acts_dict, n_splits, seed, structure_name):\n    \"\"\"Split-half reliability of F(h) rankings across all layers.\n    Returns list of per-split result dicts with Spearman rho.\n    \"\"\"\n    n_total = next(iter(acts_dict.values())).shape[0]\n    split_results = []\n    for i in range(n_splits):\n        rng = np.random.RandomState(seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")\n        fh_a = compute_fh_scores(acts_dict, idx_a)\n        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")\n        fh_b = compute_fh_scores(acts_dict, idx_b)\n\n        vals_a, vals_b = [], []\n        for layer_idx in sorted(fh_a.keys()):\n            vals_a.extend(fh_a[layer_idx].tolist())\n            vals_b.extend(fh_b[layer_idx].tolist())\n\n        rho, p = stats.spearmanr(vals_a, vals_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_structures\": len(vals_a)})\n        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")\n    return split_results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, default=None)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    parser.add_argument(\"--mlp_groups\", type=int, default=28,\n                        help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",\n                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")\n    args = parser.parse_args()\n\n    if not args.skip_cross_model and not args.pruned_model:\n        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Load original model and collect all activations ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model q_proj activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n\n    logger.info(\"Collecting original model MLP gate_proj activations...\")\n    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)\n\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed. All activations cached on CPU.\")\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"mlp_groups\": args.mlp_groups,\n            \"seed\": args.seed,\n        },\n    }\n\n    # --- Phase 1-3: Cross-model CKA (optional) ---\n    if not args.skip_cross_model:\n        logger.info(\"Loading pruned model...\")\n        pruned_model, pruning_meta = load_pruned_model_with_meta(\n            args.original_model, args.pruned_model, torch_dtype, device\n        )\n        keep_masks = pruning_meta[\"attn_keep_masks\"]\n        logger.info(\"Collecting pruned model activations...\")\n        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n        del pruned_model\n        torch.cuda.empty_cache()\n        logger.info(\"Pruned model freed.\")\n\n        # Phase 1: Full CKA scores\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                        n_heads_orig, n_kv_heads)\n        valid_scores = {k: v for k, v in full_scores.items()\n                        if not (isinstance(v, float) and v != v)}\n        vals = np.array(list(valid_scores.values()))\n        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n        # Phase 2: Split-half reliability (cross-model)\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n        cross_split_results = []\n        for i in range(args.n_splits):\n            rng = np.random.RandomState(args.seed + i)\n            perm = rng.permutation(n_total)\n            half = n_total // 2\n            idx_a = sorted(perm[:half].tolist())\n            idx_b = sorted(perm[half:2 * half].tolist())\n\n            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_a)\n            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                         n_heads_orig, n_kv_heads, idx_b)\n            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n            rho, p = stats.spearmanr(arr_a, arr_b)\n            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                                        \"n_groups\": len(arr_a)})\n            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))\n        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))\n\n        # Phase 3: Calibration size sensitivity\n        logger.info(\"=\" * 50)\n        logger.info(\"Phase 3: Calibration size sensitivity...\")\n        size_results = []\n        for n_sub in [128, 256, 512]:\n            if n_sub >= n_total:\n                continue\n            rng = np.random.RandomState(args.seed)\n            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                           n_heads_orig, n_kv_heads, sub_idx)\n            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n            rho, p = stats.spearmanr(ref_vals, sub_vals)\n            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                                 \"p_value\": float(p)})\n            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n        del pruned_acts\n        torch.cuda.empty_cache()\n\n        per_group = {}\n        for (l, g), v in full_scores.items():\n            key = f\"layer{l}_group{g}\"\n            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n        output[\"config\"][\"pruned_model\"] = args.pruned_model\n        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)\n        output[\"per_group_cka_scores\"] = per_group\n        output[\"cka_summary\"] = {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        }\n        output[\"split_half_reliability\"] = {\n            \"per_split\": cross_split_results,\n            \"mean_rho\": cross_mean_rho,\n            \"std_rho\": cross_std_rho,\n            \"pass\": cross_mean_rho > 0.9,\n        }\n        output[\"size_sensitivity\"] = {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        }\n\n    # --- Phase 4: F(h) attention head split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",\n                args.n_splits)\n    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")\n    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))\n    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))\n    attn_pass = attn_mean_rho > 0.9\n    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"\n                f\"{'PASS' if attn_pass else 'FAIL'}\")\n\n    output[\"fh_attn_reliability\"] = {\n        \"per_split\": attn_fh_results,\n        \"mean_rho\": attn_mean_rho,\n        \"std_rho\": attn_std_rho,\n        \"pass\": attn_pass,\n    }\n\n    del orig_acts\n    torch.cuda.empty_cache()\n\n    # --- Phase 5: F(h) MLP group split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)\n    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")\n    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))\n    mlp_pass = mlp_mean_rho > 0.9\n    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"\n                f\"{'PASS' if mlp_pass else 'FAIL'}\")\n\n    output[\"fh_mlp_reliability\"] = {\n        \"per_split\": mlp_fh_results,\n        \"mean_rho\": mlp_mean_rho,\n        \"std_rho\": mlp_std_rho,\n        \"pass\": mlp_pass,\n    }\n\n    del orig_mlp_acts\n    torch.cuda.empty_cache()\n\n    # --- Save results ---\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    # --- Print summary ---\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n\n    if not args.skip_cross_model:\n        print(f\"\\nCross-model CKA (Phase 1-3):\")\n        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n              f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"\n        print(f\"  Split-half reliability ({args.n_splits} splits):\")\n        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"\n              f\"(threshold: 0.9)\")\n        for r in cross_split_results:\n            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")\n        print(f\"  Size sensitivity (vs N={n_total}):\")\n        for s in size_results:\n            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n\n    print(f\"\\nF(h) Attention head reliability (Phase 4):\")\n    ah_label = \"PASS\" if attn_pass else \"FAIL\"\n    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")\n    for r in attn_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"\\nF(h) MLP group reliability (Phase 5):\")\n    mh_label = \"PASS\" if mlp_pass else \"FAIL\"\n    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")\n    for r in mlp_fh_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 11,
        "newStart": 1,
        "newLines": 13,
        "lines": [
          " \"\"\"",
          " CKA Reliability Analysis for RASP.",
          " ",
          "-Validates the stability of cross-model CKA scores (original vs pruned) by:",
          "-1. Split-half reliability: Spearman rho between CKA scores on two data halves",
          "-2. Calibration size sensitivity: Spearman rho at different sample sizes vs full",
          "+Validates the stability of structural scoring by:",
          "+1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)",
          "+4.   F(h) split-half reliability for attention heads (intra-layer overlap)",
          "+5.   F(h) split-half reliability for MLP groups (intra-layer overlap)",
          " ",
          "-Addresses Claim 2: CKA-based structural scoring is reliable and stable.",
          "+Phases 1-3 address cross-model CKA stability.",
          "+Phases 4-5 address intra-layer F(h) stability (Claim 2 core metric).",
          " \"\"\"",
          " ",
          " import argparse"
        ]
      },
      {
        "oldStart": 100,
        "oldLines": 6,
        "newStart": 102,
        "newLines": 53,
        "lines": [
          "     return activations",
          " ",
          " ",
          "+def collect_mlp_activations(model, calibration_data, device, n_groups=28):",
          "+    \"\"\"Collect MLP gate_proj activations grouped into channel groups.",
          "+    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.",
          "+    \"\"\"",
          "+    n_layers = model.config.num_hidden_layers",
          "+    intermediate_size = model.config.intermediate_size",
          "+    group_size = intermediate_size // n_groups",
          "+",
          "+    gate_outputs = {i: [] for i in range(n_layers)}",
          "+    hooks = []",
          "+",
          "+    def make_hook(layer_idx):",
          "+        def fn(module, inp, out):",
          "+            gate_outputs[layer_idx].append(out.detach().cpu())",
          "+        return fn",
          "+",
          "+    for i in range(n_layers):",
          "+        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))",
          "+        hooks.append(h)",
          "+",
          "+    model.eval()",
          "+    with torch.no_grad():",
          "+        for idx, enc in enumerate(calibration_data):",
          "+            input_ids = enc[\"input_ids\"].to(device)",
          "+            attention_mask = enc[\"attention_mask\"].to(device)",
          "+            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)",
          "+            if (idx + 1) % 200 == 0:",
          "+                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")",
          "+",
          "+    for h in hooks:",
          "+        h.remove()",
          "+",
          "+    activations = {}",
          "+    for layer_idx in range(n_layers):",
          "+        per_group = []",
          "+        for t in gate_outputs[layer_idx]:",
          "+            t = t.squeeze(0)  # [seq, intermediate_size]",
          "+            t = t.mean(dim=0)  # [intermediate_size]",
          "+            usable = n_groups * group_size",
          "+            t = t[:usable].view(n_groups, group_size)",
          "+            per_group.append(t)",
          "+        activations[layer_idx] = torch.stack(per_group, dim=0).float()",
          "+        gate_outputs[layer_idx] = None",
          "+",
          "+    return activations",
          "+",
          "+",
          " def load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):",
          "     \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"",
          "     meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")"
        ]
      },
      {
        "oldStart": 187,
        "oldLines": 10,
        "newStart": 236,
        "newLines": 62,
        "lines": [
          "     return np.array(a_vals), np.array(b_vals)",
          " ",
          " ",
          "+def compute_fh_scores(acts_dict, sample_indices=None):",
          "+    \"\"\"Compute intra-layer F(h) for each structure.",
          "+    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]",
          "+    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.",
          "+    \"\"\"",
          "+    fh = {}",
          "+    for layer_idx, acts in acts_dict.items():",
          "+        if sample_indices is not None:",
          "+            acts = acts[sample_indices]",
          "+        n_samples, n_structs, dim = acts.shape",
          "+        matrix = torch.zeros(n_structs, n_structs)",
          "+        for i in range(n_structs):",
          "+            matrix[i, i] = 1.0",
          "+            for j in range(i + 1, n_structs):",
          "+                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())",
          "+                matrix[i, j] = val",
          "+                matrix[j, i] = val",
          "+        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)",
          "+        fh[layer_idx] = scores",
          "+    return fh",
          "+",
          "+",
          "+def compute_fh_reliability(acts_dict, n_splits, seed, structure_name):",
          "+    \"\"\"Split-half reliability of F(h) rankings across all layers.",
          "+    Returns list of per-split result dicts with Spearman rho.",
          "+    \"\"\"",
          "+    n_total = next(iter(acts_dict.values())).shape[0]",
          "+    split_results = []",
          "+    for i in range(n_splits):",
          "+        rng = np.random.RandomState(seed + i)",
          "+        perm = rng.permutation(n_total)",
          "+        half = n_total // 2",
          "+        idx_a = sorted(perm[:half].tolist())",
          "+        idx_b = sorted(perm[half:2 * half].tolist())",
          "+",
          "+        logger.info(f\"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...\")",
          "+        fh_a = compute_fh_scores(acts_dict, idx_a)",
          "+        logger.info(f\"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...\")",
          "+        fh_b = compute_fh_scores(acts_dict, idx_b)",
          "+",
          "+        vals_a, vals_b = [], []",
          "+        for layer_idx in sorted(fh_a.keys()):",
          "+            vals_a.extend(fh_a[layer_idx].tolist())",
          "+            vals_b.extend(fh_b[layer_idx].tolist())",
          "+",
          "+        rho, p = stats.spearmanr(vals_a, vals_b)",
          "+        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),",
          "+                              \"n_structures\": len(vals_a)})",
          "+        logger.info(f\"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}\")",
          "+    return split_results",
          "+",
          "+",
          " def main():",
          "     parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")",
          "     parser.add_argument(\"--original_model\", type=str, required=True)",
          "-    parser.add_argument(\"--pruned_model\", type=str, required=True)",
          "+    parser.add_argument(\"--pruned_model\", type=str, default=None)",
          "     parser.add_argument(\"--gpu_id\", type=int, default=0)",
          "     parser.add_argument(\"--num_samples\", type=int, default=1024)",
          "     parser.add_argument(\"--max_length\", type=int, default=512)"
        ]
      },
      {
        "oldStart": 199,
        "oldLines": 8,
        "newStart": 300,
        "newLines": 15,
        "lines": [
          "     parser.add_argument(\"--seed\", type=int, default=42)",
          "     parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",",
          "                         choices=[\"float16\", \"bfloat16\", \"float32\"])",
          "+    parser.add_argument(\"--mlp_groups\", type=int, default=28,",
          "+                        help=\"Number of MLP channel groups per layer\")",
          "+    parser.add_argument(\"--skip_cross_model\", action=\"store_true\",",
          "+                        help=\"Skip Phase 1-3 (cross-model CKA); only run F(h) reliability\")",
          "     args = parser.parse_args()",
          " ",
          "+    if not args.skip_cross_model and not args.pruned_model:",
          "+        parser.error(\"--pruned_model is required unless --skip_cross_model is set\")",
          "+",
          "     set_seed(args.seed)",
          "     device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")",
          "     torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,"
        ]
      },
      {
        "oldStart": 213,
        "oldLines": 7,
        "newStart": 321,
        "newLines": 7,
        "lines": [
          "     n_total = len(calibration_data)",
          "     logger.info(f\"Loaded {n_total} calibration samples\")",
          " ",
          "-    # --- Collect activations (load models one at a time to save GPU memory) ---",
          "+    # --- Load original model and collect all activations ---",
          "     logger.info(\"Loading original model...\")",
          "     orig_model = AutoModelForCausalLM.from_pretrained(",
          "         args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True"
        ]
      },
      {
        "oldStart": 226,
        "oldLines": 137,
        "newStart": 334,
        "newLines": 207,
        "lines": [
          "     logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"",
          "                 f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")",
          " ",
          "-    logger.info(\"Collecting original model activations...\")",
          "+    logger.info(\"Collecting original model q_proj activations...\")",
          "     orig_acts = collect_qproj_activations(orig_model, calibration_data, device)",
          "+",
          "+    logger.info(\"Collecting original model MLP gate_proj activations...\")",
          "+    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)",
          "+",
          "     del orig_model",
          "     torch.cuda.empty_cache()",
          "-    logger.info(\"Original model freed.\")",
          "+    logger.info(\"Original model freed. All activations cached on CPU.\")",
          " ",
          "-    logger.info(\"Loading pruned model...\")",
          "-    pruned_model, pruning_meta = load_pruned_model_with_meta(",
          "-        args.original_model, args.pruned_model, torch_dtype, device",
          "-    )",
          "-    keep_masks = pruning_meta[\"attn_keep_masks\"]",
          "-    logger.info(\"Collecting pruned model activations...\")",
          "-    pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)",
          "-    del pruned_model",
          "-    torch.cuda.empty_cache()",
          "-    logger.info(\"Pruned model freed. All activations cached on CPU.\")",
          "-",
          "-    # --- Phase 1: Full CKA scores ---",
          "-    logger.info(\"=\" * 50)",
          "-    logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)",
          "-    full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "-                                    n_heads_orig, n_kv_heads)",
          "-    valid_scores = {k: v for k, v in full_scores.items()",
          "-                    if not (isinstance(v, float) and v != v)}",
          "-    vals = np.array(list(valid_scores.values()))",
          "-    logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")",
          "-    logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"",
          "-                f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")",
          "-",
          "-    # --- Phase 2: Split-half reliability ---",
          "-    logger.info(\"=\" * 50)",
          "-    logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)",
          "-    split_results = []",
          "-    for i in range(args.n_splits):",
          "-        rng = np.random.RandomState(args.seed + i)",
          "-        perm = rng.permutation(n_total)",
          "-        half = n_total // 2",
          "-        idx_a = sorted(perm[:half].tolist())",
          "-        idx_b = sorted(perm[half:2 * half].tolist())",
          "-",
          "-        scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "-                                     n_heads_orig, n_kv_heads, idx_a)",
          "-        scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "-                                     n_heads_orig, n_kv_heads, idx_b)",
          "-        arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)",
          "-        rho, p = stats.spearmanr(arr_a, arr_b)",
          "-        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),",
          "-                              \"n_groups\": len(arr_a)})",
          "-        logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")",
          "-",
          "-    mean_rho = float(np.mean([r[\"rho\"] for r in split_results]))",
          "-    std_rho = float(np.std([r[\"rho\"] for r in split_results]))",
          "-",
          "-    # --- Phase 3: Calibration size sensitivity ---",
          "-    logger.info(\"=\" * 50)",
          "-    logger.info(\"Phase 3: Calibration size sensitivity...\")",
          "-    size_results = []",
          "-    for n_sub in [128, 256, 512]:",
          "-        if n_sub >= n_total:",
          "-            continue",
          "-        rng = np.random.RandomState(args.seed)",
          "-        sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())",
          "-",
          "-        sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "-                                       n_heads_orig, n_kv_heads, sub_idx)",
          "-        ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)",
          "-        rho, p = stats.spearmanr(ref_vals, sub_vals)",
          "-        size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),",
          "-                             \"p_value\": float(p)})",
          "-        logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")",
          "-",
          "-    # --- Compile and save results ---",
          "-    per_group = {}",
          "-    for (l, g), v in full_scores.items():",
          "-        key = f\"layer{l}_group{g}\"",
          "-        per_group[key] = None if (isinstance(v, float) and v != v) else float(v)",
          "-",
          "     output = {",
          "         \"config\": {",
          "             \"original_model\": args.original_model,",
          "-            \"pruned_model\": args.pruned_model,",
          "             \"num_samples\": n_total,",
          "             \"n_layers\": n_layers,",
          "             \"n_heads_original\": n_heads_orig,",
          "             \"n_kv_heads\": n_kv_heads,",
          "             \"heads_per_kv\": heads_per_kv,",
          "             \"total_gqa_groups\": n_layers * n_kv_heads,",
          "-            \"valid_gqa_groups\": len(valid_scores),",
          "+            \"mlp_groups\": args.mlp_groups,",
          "             \"seed\": args.seed,",
          "         },",
          "-        \"per_group_cka_scores\": per_group,",
          "-        \"cka_summary\": {",
          "+    }",
          "+",
          "+    # --- Phase 1-3: Cross-model CKA (optional) ---",
          "+    if not args.skip_cross_model:",
          "+        logger.info(\"Loading pruned model...\")",
          "+        pruned_model, pruning_meta = load_pruned_model_with_meta(",
          "+            args.original_model, args.pruned_model, torch_dtype, device",
          "+        )",
          "+        keep_masks = pruning_meta[\"attn_keep_masks\"]",
          "+        logger.info(\"Collecting pruned model activations...\")",
          "+        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)",
          "+        del pruned_model",
          "+        torch.cuda.empty_cache()",
          "+        logger.info(\"Pruned model freed.\")",
          "+",
          "+        # Phase 1: Full CKA scores",
          "+        logger.info(\"=\" * 50)",
          "+        logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)",
          "+        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "+                                        n_heads_orig, n_kv_heads)",
          "+        valid_scores = {k: v for k, v in full_scores.items()",
          "+                        if not (isinstance(v, float) and v != v)}",
          "+        vals = np.array(list(valid_scores.values()))",
          "+        logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")",
          "+        logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"",
          "+                    f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")",
          "+",
          "+        # Phase 2: Split-half reliability (cross-model)",
          "+        logger.info(\"=\" * 50)",
          "+        logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)",
          "+        cross_split_results = []",
          "+        for i in range(args.n_splits):",
          "+            rng = np.random.RandomState(args.seed + i)",
          "+            perm = rng.permutation(n_total)",
          "+            half = n_total // 2",
          "+            idx_a = sorted(perm[:half].tolist())",
          "+            idx_b = sorted(perm[half:2 * half].tolist())",
          "+",
          "+            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "+                                         n_heads_orig, n_kv_heads, idx_a)",
          "+            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "+                                         n_heads_orig, n_kv_heads, idx_b)",
          "+            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)",
          "+            rho, p = stats.spearmanr(arr_a, arr_b)",
          "+            cross_split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),",
          "+                                        \"n_groups\": len(arr_a)})",
          "+            logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")",
          "+",
          "+        cross_mean_rho = float(np.mean([r[\"rho\"] for r in cross_split_results]))",
          "+        cross_std_rho = float(np.std([r[\"rho\"] for r in cross_split_results]))",
          "+",
          "+        # Phase 3: Calibration size sensitivity",
          "+        logger.info(\"=\" * 50)",
          "+        logger.info(\"Phase 3: Calibration size sensitivity...\")",
          "+        size_results = []",
          "+        for n_sub in [128, 256, 512]:",
          "+            if n_sub >= n_total:",
          "+                continue",
          "+            rng = np.random.RandomState(args.seed)",
          "+            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())",
          "+",
          "+            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,",
          "+                                           n_heads_orig, n_kv_heads, sub_idx)",
          "+            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)",
          "+            rho, p = stats.spearmanr(ref_vals, sub_vals)",
          "+            size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),",
          "+                                 \"p_value\": float(p)})",
          "+            logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")",
          "+",
          "+        del pruned_acts",
          "+        torch.cuda.empty_cache()",
          "+",
          "+        per_group = {}",
          "+        for (l, g), v in full_scores.items():",
          "+            key = f\"layer{l}_group{g}\"",
          "+            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)",
          "+",
          "+        output[\"config\"][\"pruned_model\"] = args.pruned_model",
          "+        output[\"config\"][\"valid_gqa_groups\"] = len(valid_scores)",
          "+        output[\"per_group_cka_scores\"] = per_group",
          "+        output[\"cka_summary\"] = {",
          "             \"mean\": float(vals.mean()),",
          "             \"std\": float(vals.std()),",
          "             \"min\": float(vals.min()),",
          "             \"max\": float(vals.max()),",
          "             \"median\": float(np.median(vals)),",
          "-        },",
          "-        \"split_half_reliability\": {",
          "-            \"per_split\": split_results,",
          "-            \"mean_rho\": mean_rho,",
          "-            \"std_rho\": std_rho,",
          "-            \"pass\": mean_rho > 0.9,",
          "-        },",
          "-        \"size_sensitivity\": {",
          "+        }",
          "+        output[\"split_half_reliability\"] = {",
          "+            \"per_split\": cross_split_results,",
          "+            \"mean_rho\": cross_mean_rho,",
          "+            \"std_rho\": cross_std_rho,",
          "+            \"pass\": cross_mean_rho > 0.9,",
          "+        }",
          "+        output[\"size_sensitivity\"] = {",
          "             \"reference_n\": n_total,",
          "             \"per_size\": size_results,",
          "             \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),",
          "-        },",
          "+        }",
          "+",
          "+    # --- Phase 4: F(h) attention head split-half reliability ---",
          "+    logger.info(\"=\" * 50)",
          "+    logger.info(\"Phase 4: F(h) attention head split-half reliability (%d splits)...\",",
          "+                args.n_splits)",
          "+    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, \"attn_heads\")",
          "+    attn_mean_rho = float(np.mean([r[\"rho\"] for r in attn_fh_results]))",
          "+    attn_std_rho = float(np.std([r[\"rho\"] for r in attn_fh_results]))",
          "+    attn_pass = attn_mean_rho > 0.9",
          "+    logger.info(f\"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} \"",
          "+                f\"{'PASS' if attn_pass else 'FAIL'}\")",
          "+",
          "+    output[\"fh_attn_reliability\"] = {",
          "+        \"per_split\": attn_fh_results,",
          "+        \"mean_rho\": attn_mean_rho,",
          "+        \"std_rho\": attn_std_rho,",
          "+        \"pass\": attn_pass,",
          "     }",
          " ",
          "+    del orig_acts",
          "+    torch.cuda.empty_cache()",
          "+",
          "+    # --- Phase 5: F(h) MLP group split-half reliability ---",
          "+    logger.info(\"=\" * 50)",
          "+    logger.info(\"Phase 5: F(h) MLP group split-half reliability (%d splits)...\", args.n_splits)",
          "+    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, \"mlp_groups\")",
          "+    mlp_mean_rho = float(np.mean([r[\"rho\"] for r in mlp_fh_results]))",
          "+    mlp_std_rho = float(np.std([r[\"rho\"] for r in mlp_fh_results]))",
          "+    mlp_pass = mlp_mean_rho > 0.9",
          "+    logger.info(f\"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} \"",
          "+                f\"{'PASS' if mlp_pass else 'FAIL'}\")",
          "+",
          "+    output[\"fh_mlp_reliability\"] = {",
          "+        \"per_split\": mlp_fh_results,",
          "+        \"mean_rho\": mlp_mean_rho,",
          "+        \"std_rho\": mlp_std_rho,",
          "+        \"pass\": mlp_pass,",
          "+    }",
          "+",
          "+    del orig_mlp_acts",
          "+    torch.cuda.empty_cache()",
          "+",
          "+    # --- Save results ---",
          "     os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)",
          "     with open(args.output, \"w\") as f:",
          "         json.dump(output, f, indent=2)",
          "     logger.info(f\"Results saved to {args.output}\")",
          " ",
          "+    # --- Print summary ---",
          "     print(f\"\\n{'=' * 60}\")",
          "     print(\"CKA Reliability Analysis\")",
          "     print(f\"{'=' * 60}\")",
          "-    print(f\"GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")",
          "-    print(f\"CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"",
          "-          f\"[{vals.min():.4f}, {vals.max():.4f}]\")",
          "-    sh_pass = \"PASS\" if mean_rho > 0.9 else \"FAIL\"",
          "-    print(f\"\\nSplit-half reliability ({args.n_splits} splits):\")",
          "-    print(f\"  rho = {mean_rho:.4f} +/- {std_rho:.4f}  {sh_pass} (threshold: 0.9)\")",
          "-    for r in split_results:",
          "+",
          "+    if not args.skip_cross_model:",
          "+        print(f\"\\nCross-model CKA (Phase 1-3):\")",
          "+        print(f\"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")",
          "+        print(f\"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"",
          "+              f\"[{vals.min():.4f}, {vals.max():.4f}]\")",
          "+        sh_pass = \"PASS\" if cross_mean_rho > 0.9 else \"FAIL\"",
          "+        print(f\"  Split-half reliability ({args.n_splits} splits):\")",
          "+        print(f\"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} \"",
          "+              f\"(threshold: 0.9)\")",
          "+        for r in cross_split_results:",
          "+            print(f\"      Split {r['split']}: rho={r['rho']:.4f}\")",
          "+        print(f\"  Size sensitivity (vs N={n_total}):\")",
          "+        for s in size_results:",
          "+            sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"",
          "+            print(f\"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")",
          "+",
          "+    print(f\"\\nF(h) Attention head reliability (Phase 4):\")",
          "+    ah_label = \"PASS\" if attn_pass else \"FAIL\"",
          "+    print(f\"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)\")",
          "+    for r in attn_fh_results:",
          "         print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")",
          "-    print(f\"\\nSize sensitivity (vs N={n_total}):\")",
          "-    for s in size_results:",
          "-        sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"",
          "-        print(f\"  N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")",
          "+",
          "+    print(f\"\\nF(h) MLP group reliability (Phase 5):\")",
          "+    mh_label = \"PASS\" if mlp_pass else \"FAIL\"",
          "+    print(f\"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)\")",
          "+    for r in mlp_fh_results:",
          "+        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")",
          "+",
          "     print(f\"{'=' * 60}\")",
          " ",
          " "
        ]
      }
    ],
    "originalFile": "\"\"\"\nCKA Reliability Analysis for RASP.\n\nValidates the stability of cross-model CKA scores (original vs pruned) by:\n1. Split-half reliability: Spearman rho between CKA scores on two data halves\n2. Calibration size sensitivity: Spearman rho at different sample sizes vs full\n\nAddresses Claim 2: CKA-based structural scoring is reliable and stable.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\n\nimport numpy as np\nimport scipy.stats as stats\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s [%(levelname)s] %(message)s\")\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X, Y):\n    \"\"\"Linear CKA between two activation matrices. X: [n, p], Y: [n, q].\"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_qproj_activations(model, calibration_data, device):\n    \"\"\"Collect per-head q_proj activations, mean-pooled over seq length.\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.\n    \"\"\"\n    n_layers = model.config.num_hidden_layers\n    head_dim = model.config.hidden_size // model.config.num_attention_heads\n\n    q_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def fn(module, inp, out):\n            q_outputs[layer_idx].append(out.detach().cpu())\n        return fn\n\n    for i in range(n_layers):\n        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (idx + 1) % 200 == 0:\n                logger.info(f\"  Forward pass {idx + 1}/{len(calibration_data)}\")\n\n    for h in hooks:\n        h.remove()\n\n    activations = {}\n    for layer_idx in range(n_layers):\n        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]\n        n_heads = out_dim // head_dim\n        per_head = []\n        for t in q_outputs[layer_idx]:\n            t = t.squeeze(0)  # [seq, n_heads * head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim]\n            per_head.append(t)\n        activations[layer_idx] = torch.stack(per_head, dim=0).float()\n        q_outputs[layer_idx] = None\n\n    return activations\n\n\ndef load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):\n    \"\"\"Load structurally pruned model via base model reconstruction + saved weights.\"\"\"\n    meta_path = os.path.join(pruned_model_path, \"pruning_metadata.pt\")\n    pruning_meta = torch.load(meta_path, map_location=\"cpu\", weights_only=True)\n\n    src_dir = os.path.dirname(os.path.abspath(__file__))\n    if src_dir not in sys.path:\n        sys.path.insert(0, src_dir)\n    from prune import prune_attention_heads, prune_mlp_channels\n\n    logging.getLogger(\"prune\").setLevel(logging.WARNING)\n    model = AutoModelForCausalLM.from_pretrained(\n        base_model_path, torch_dtype=torch_dtype, device_map=\"cpu\", trust_remote_code=True\n    )\n    prune_attention_heads(model, pruning_meta[\"attn_keep_masks\"])\n    prune_mlp_channels(model, pruning_meta[\"mlp_keep_masks\"])\n\n    safetensor_files = sorted(\n        [f for f in os.listdir(pruned_model_path) if f.endswith(\".safetensors\")]\n    )\n    if safetensor_files:\n        from safetensors.torch import load_file\n        state_dict = {}\n        for f in safetensor_files:\n            state_dict.update(load_file(os.path.join(pruned_model_path, f)))\n    else:\n        state_dict = torch.load(\n            os.path.join(pruned_model_path, \"pytorch_model.bin\"),\n            map_location=\"cpu\", weights_only=True,\n        )\n    model.load_state_dict(state_dict)\n    model.to(device)\n    return model, pruning_meta\n\n\ndef compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,\n                      sample_indices=None):\n    \"\"\"Compute per-GQA-group CKA between original and pruned representations.\n\n    For each KV group, concatenates retained Q head activations from both models\n    and computes linear CKA. Original uses all Q heads in the group, pruned uses\n    only retained Q heads (CKA handles different feature dimensions).\n\n    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).\n    \"\"\"\n    heads_per_kv = n_heads_orig // n_kv_heads\n    n_layers = len(orig_acts)\n    scores = {}\n\n    for layer_idx in range(n_layers):\n        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]\n        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]\n        retained = keep_masks[layer_idx]\n\n        if sample_indices is not None:\n            orig_layer = orig_layer[sample_indices]\n            pruned_layer = pruned_layer[sample_indices]\n\n        for g in range(n_kv_heads):\n            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))\n            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]\n\n            if not pruned_positions:\n                scores[(layer_idx, g)] = float(\"nan\")\n                continue\n\n            n = orig_layer.shape[0]\n            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)\n            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)\n            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)\n\n    return scores\n\n\ndef scores_to_aligned_arrays(scores_a, scores_b):\n    \"\"\"Extract aligned non-NaN value arrays from two score dicts.\"\"\"\n    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))\n    a_vals, b_vals = [], []\n    for k in common:\n        va, vb = scores_a[k], scores_b[k]\n        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):\n            continue\n        a_vals.append(va)\n        b_vals.append(vb)\n    return np.array(a_vals), np.array(b_vals)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"CKA Reliability Analysis for RASP scoring\")\n    parser.add_argument(\"--original_model\", type=str, required=True)\n    parser.add_argument(\"--pruned_model\", type=str, required=True)\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--num_samples\", type=int, default=1024)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--n_splits\", type=int, default=5)\n    parser.add_argument(\"--output\", type=str, required=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\",\n                        choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(f\"cuda:{args.gpu_id}\" if torch.cuda.is_available() else \"cpu\")\n    torch_dtype = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16,\n                   \"float32\": torch.float32}[args.dtype]\n\n    logger.info(\"Loading tokenizer and calibration data...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)\n    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,\n                                             args.seed)\n    n_total = len(calibration_data)\n    logger.info(f\"Loaded {n_total} calibration samples\")\n\n    # --- Collect activations (load models one at a time to save GPU memory) ---\n    logger.info(\"Loading original model...\")\n    orig_model = AutoModelForCausalLM.from_pretrained(\n        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True\n    )\n    config = orig_model.config\n    n_heads_orig = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    n_layers = config.num_hidden_layers\n    heads_per_kv = n_heads_orig // n_kv_heads\n    logger.info(f\"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV \"\n                f\"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)\")\n\n    logger.info(\"Collecting original model activations...\")\n    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)\n    del orig_model\n    torch.cuda.empty_cache()\n    logger.info(\"Original model freed.\")\n\n    logger.info(\"Loading pruned model...\")\n    pruned_model, pruning_meta = load_pruned_model_with_meta(\n        args.original_model, args.pruned_model, torch_dtype, device\n    )\n    keep_masks = pruning_meta[\"attn_keep_masks\"]\n    logger.info(\"Collecting pruned model activations...\")\n    pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)\n    del pruned_model\n    torch.cuda.empty_cache()\n    logger.info(\"Pruned model freed. All activations cached on CPU.\")\n\n    # --- Phase 1: Full CKA scores ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 1: Full CKA scores (N=%d)...\", n_total)\n    full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                    n_heads_orig, n_kv_heads)\n    valid_scores = {k: v for k, v in full_scores.items()\n                    if not (isinstance(v, float) and v != v)}\n    vals = np.array(list(valid_scores.values()))\n    logger.info(f\"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}\")\n    logger.info(f\"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, \"\n                f\"range=[{vals.min():.4f}, {vals.max():.4f}]\")\n\n    # --- Phase 2: Split-half reliability ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 2: Split-half reliability (%d splits)...\", args.n_splits)\n    split_results = []\n    for i in range(args.n_splits):\n        rng = np.random.RandomState(args.seed + i)\n        perm = rng.permutation(n_total)\n        half = n_total // 2\n        idx_a = sorted(perm[:half].tolist())\n        idx_b = sorted(perm[half:2 * half].tolist())\n\n        scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                     n_heads_orig, n_kv_heads, idx_a)\n        scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                     n_heads_orig, n_kv_heads, idx_b)\n        arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)\n        rho, p = stats.spearmanr(arr_a, arr_b)\n        split_results.append({\"split\": i, \"rho\": float(rho), \"p_value\": float(p),\n                              \"n_groups\": len(arr_a)})\n        logger.info(f\"  Split {i}: rho={rho:.4f}, p={p:.2e}\")\n\n    mean_rho = float(np.mean([r[\"rho\"] for r in split_results]))\n    std_rho = float(np.std([r[\"rho\"] for r in split_results]))\n\n    # --- Phase 3: Calibration size sensitivity ---\n    logger.info(\"=\" * 50)\n    logger.info(\"Phase 3: Calibration size sensitivity...\")\n    size_results = []\n    for n_sub in [128, 256, 512]:\n        if n_sub >= n_total:\n            continue\n        rng = np.random.RandomState(args.seed)\n        sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())\n\n        sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,\n                                       n_heads_orig, n_kv_heads, sub_idx)\n        ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)\n        rho, p = stats.spearmanr(ref_vals, sub_vals)\n        size_results.append({\"n_samples\": n_sub, \"rho_vs_full\": float(rho),\n                             \"p_value\": float(p)})\n        logger.info(f\"  N={n_sub}: rho={rho:.4f} vs N={n_total}\")\n\n    # --- Compile and save results ---\n    per_group = {}\n    for (l, g), v in full_scores.items():\n        key = f\"layer{l}_group{g}\"\n        per_group[key] = None if (isinstance(v, float) and v != v) else float(v)\n\n    output = {\n        \"config\": {\n            \"original_model\": args.original_model,\n            \"pruned_model\": args.pruned_model,\n            \"num_samples\": n_total,\n            \"n_layers\": n_layers,\n            \"n_heads_original\": n_heads_orig,\n            \"n_kv_heads\": n_kv_heads,\n            \"heads_per_kv\": heads_per_kv,\n            \"total_gqa_groups\": n_layers * n_kv_heads,\n            \"valid_gqa_groups\": len(valid_scores),\n            \"seed\": args.seed,\n        },\n        \"per_group_cka_scores\": per_group,\n        \"cka_summary\": {\n            \"mean\": float(vals.mean()),\n            \"std\": float(vals.std()),\n            \"min\": float(vals.min()),\n            \"max\": float(vals.max()),\n            \"median\": float(np.median(vals)),\n        },\n        \"split_half_reliability\": {\n            \"per_split\": split_results,\n            \"mean_rho\": mean_rho,\n            \"std_rho\": std_rho,\n            \"pass\": mean_rho > 0.9,\n        },\n        \"size_sensitivity\": {\n            \"reference_n\": n_total,\n            \"per_size\": size_results,\n            \"all_pass_0.9\": all(s[\"rho_vs_full\"] > 0.9 for s in size_results),\n        },\n    }\n\n    os.makedirs(os.path.dirname(args.output) or \".\", exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    logger.info(f\"Results saved to {args.output}\")\n\n    print(f\"\\n{'=' * 60}\")\n    print(\"CKA Reliability Analysis\")\n    print(f\"{'=' * 60}\")\n    print(f\"GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid\")\n    print(f\"CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} \"\n          f\"[{vals.min():.4f}, {vals.max():.4f}]\")\n    sh_pass = \"PASS\" if mean_rho > 0.9 else \"FAIL\"\n    print(f\"\\nSplit-half reliability ({args.n_splits} splits):\")\n    print(f\"  rho = {mean_rho:.4f} +/- {std_rho:.4f}  {sh_pass} (threshold: 0.9)\")\n    for r in split_results:\n        print(f\"    Split {r['split']}: rho={r['rho']:.4f}\")\n    print(f\"\\nSize sensitivity (vs N={n_total}):\")\n    for s in size_results:\n        sv = \"PASS\" if s[\"rho_vs_full\"] > 0.9 else \"FAIL\"\n        print(f\"  N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}\")\n    print(f\"{'=' * 60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

Verifying `--help` output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "00091074-c51c-425c-a90e-0d826ef756af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RX3z8HgHiVbT6jcPF5tSst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21129,
      "cache_read_input_tokens": 34147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21129
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01RKyTACseeoqwr9ZnKdwrw9`</summary>

```json
{
  "command": "python src/run_cka_reliability.py --help",
  "description": "Verify argument parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "f3235f39-7296-421b-9194-0e888113f9c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RX3z8HgHiVbT6jcPF5tSst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21129,
      "cache_read_input_tokens": 34147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21129
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

_source line 15_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778833200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d5f57d74-c197-4306-ae62-91733a7b332e",
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7"
}
```

---

### Tool result

_source line 16 · 2026-05-15T03:24:41.186Z_

<details><summary>↩ Tool result · reported error · `toolu_01RKyTACseeoqwr9ZnKdwrw9`</summary>

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
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "ca5934ad-00df-4cb2-9f00-c488fb9cdfd4",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01GUwJiK6eotihTwakVH4hAs`</summary>

```json
{
  "command": "python3 src/run_cka_reliability.py --help",
  "description": "Verify argument parsing with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "01412767-d668-44af-bae2-69980af5ca12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNpcDUaNjQjfRtaN3HkW86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 55276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 18 · 2026-05-15T03:24:47.563Z_

<details><summary>↩ Tool result · reported error · `toolu_01GUwJiK6eotihTwakVH4hAs`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py", line 22, in &lt;module>
    import torch
ModuleNotFoundError: No module named 'torch'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "24fefc8e-6ae6-4d6f-8d61-e1f9fca7693e",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/run_cka_reliability.py\", line 22, in &lt;module>\n    import torch\nModuleNotFoundError: No module named 'torch'"
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_0164wV8TR8w1QWHN21uBpEC2`</summary>

```json
{
  "command": "python3 -c \"\nimport ast, sys\nwith open('src/run_cka_reliability.py') as f:\n    tree = ast.parse(f.read())\nprint('Syntax OK')\n# Check argparse args\nsource = open('src/run_cka_reliability.py').read()\nfor arg in ['--mlp_groups', '--skip_cross_model', '--original_model', '--pruned_model', '--output']:\n    if arg in source:\n        print(f'  Found arg: {arg}')\n    else:\n        print(f'  MISSING arg: {arg}')\n\"",
  "description": "Verify syntax and arg presence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "16c461b5-c628-4957-9584-273943b9a486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAZt4YTyHL7GbP9t78HPez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 55409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-15T03:24:54.451Z_

<details><summary>↩ Tool result · `toolu_0164wV8TR8w1QWHN21uBpEC2`</summary>

```text
Syntax OK
  Found arg: --mlp_groups
  Found arg: --skip_cross_model
  Found arg: --original_model
  Found arg: --pruned_model
  Found arg: --output
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "7c742930-1227-495d-8962-c019a0d649eb",
  "tool_use_result": {
    "stdout": "Syntax OK\n  Found arg: --mlp_groups\n  Found arg: --skip_cross_model\n  Found arg: --original_model\n  Found arg: --pruned_model\n  Found arg: --output",
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

_source line 21_

语法正确，所有新参数都在。

修改总结：
- **Phase 4** (`fh_attn_reliability`): 对原始模型 attention heads 做 split-half F(h) 排名 Spearman ρ，阈值 0.9
- **Phase 5** (`fh_mlp_reliability`): 对 MLP groups 做同样的 split-half F(h) reliability
- 新增 `collect_mlp_activations` 收集 gate_proj 激活（与 `cka_overlap.py` 一致）
- 新增 `compute_fh_scores` 计算 intra-layer pairwise CKA → F(h)
- 新增 `compute_fh_reliability` 做 n_splits 次 split-half 并报告 Spearman ρ
- `--pruned_model` 改为可选（`--skip_cross_model` 时不需要）
- `--mlp_groups` 默认 28
- 原始模型加载一次，两次 forward pass 分别收集 q_proj 和 gate_proj 激活
- Phase 1-3 保留不变，仅在未设 `--skip_cross_model` 时执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "uuid": "7f56ee24-99d8-442b-bcda-ad2ea726980e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjjHtBm52CBRBDCTvbKUTU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 55603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 281
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

_source line 22_

语法正确，所有新参数都在。

修改总结：
- **Phase 4** (`fh_attn_reliability`): 对原始模型 attention heads 做 split-half F(h) 排名 Spearman ρ，阈值 0.9
- **Phase 5** (`fh_mlp_reliability`): 对 MLP groups 做同样的 split-half F(h) reliability
- 新增 `collect_mlp_activations` 收集 gate_proj 激活（与 `cka_overlap.py` 一致）
- 新增 `compute_fh_scores` 计算 intra-layer pairwise CKA → F(h)
- 新增 `compute_fh_reliability` 做 n_splits 次 split-half 并报告 Spearman ρ
- `--pruned_model` 改为可选（`--skip_cross_model` 时不需要）
- `--mlp_groups` 默认 28
- 原始模型加载一次，两次 forward pass 分别收集 q_proj 和 gate_proj 激活
- Phase 1-3 保留不变，仅在未设 `--skip_cross_model` 时执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 321013,
  "duration_api_ms": 320274,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "007d1df2-9b8b-4278-8004-c15c7675e9a7",
  "total_cost_usd": 0.94866775,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 44043,
    "cache_read_input_tokens": 236376,
    "output_tokens": 22118,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44043,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 334,
        "cache_read_input_tokens": 55603,
        "cache_creation_input_tokens": 281,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 281
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2111,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002226,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 22118,
      "cacheReadInputTokens": 236376,
      "cacheCreationInputTokens": 44043,
      "webSearchRequests": 0,
      "costUSD": 0.9464417500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f4ac84c1-c57e-435b-815d-ecd7878546ba"
}
```

</details>

---
