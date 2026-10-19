# code data split and deploy updates

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_code_data_split_and_deploy_updates_20260520T221347.log`
- **Structured JSON:** [`c9b64f63e99085c753c0.json`](../../sessions/c9/c9b64f63e99085c753c0.json)

## Before a recorded user message

59 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "1e594da5-419c-4e00-a8ce-0e943b545e19",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
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
    "resetsAt": 1779325800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a5840295-1b01-432e-9932-149f91a29e68",
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current code to understand the structure before making modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "87d07a6c-3cb7-46af-b80e-2ac71987481c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRHxkUoDHeRWKouLtERf1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12331,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12331
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01VcWwfPEdQkL8Pbaq4r2Sr7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "65cd3d6c-4bc1-4524-92bb-7d6f9ef1fa31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRHxkUoDHeRWKouLtERf1E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12331,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12331
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

_source line 6 · 2026-05-20T22:14:10.046Z_

<details><summary>↩ Tool result · `toolu_01VcWwfPEdQkL8Pbaq4r2Sr7`</summary>

```text
1	"""
2	Extract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).
3	
4	Differences from extract_activations.py:
5	  - Uses register_forward_hook instead of output_hidden_states=True.
6	    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,
7	    which is prohibitive for 94-layer models. Hooks capture only the target layers.
8	  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).
9	  - Incremental saving via --save_interval to survive OOM or interruption.
10	  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).
11	
12	Output format is identical to extract_activations.py:
13	  layer{i}_{lang}.pt  ->  {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}
14	
15	Dependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm
16	
17	Usage:
18	  python extract_activations_large.py \
19	    --model Qwen/Qwen3-235B-A22B \
20	    --languages en zh ar hi sw ko \
21	    --layers 0,8,16,24,32,48,64,80,93 \
22	    --output_dir ./activations \
23	    --quantization int4 \
24	    --save_interval 200
25	"""
26	
27	import argparse
28	import os
29	
30	import torch
31	from datasets import load_dataset
32	from transformers import AutoModelForCausalLM, AutoTokenizer
33	from tqdm import tqdm
34	
35	
36	LETTERS = ["A", "B", "C", "D"]
37	
38	
39	def parse_args():
40	    p = argparse.ArgumentParser()
41	    p.add_argument("--model", required=True, help="HuggingFace model name or path")
42	    p.add_argument("--languages", nargs="+", default=["en", "zh", "ar", "hi", "sw", "ko"])
43	    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
44	                   help="Comma-separated transformer layer indices (0-indexed)")
45	    p.add_argument("--output_dir", default="./activations")
46	    p.add_argument("--n_shot", type=int, default=5)
47	    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
48	    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
49	    p.add_argument("--subjects", nargs="*", default=None,
50	                   help="Restrict to these MMLU subjects (default: all)")
51	    p.add_argument("--quantization", default="none", choices=["none", "int4", "int8"],
52	                   help="Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)")
53	    p.add_argument("--save_interval", type=int, default=500,
54	                   help="Incrementally save every N samples (0 = only save at end)")
55	    return p.parse_args()
56	
57	
58	# ---------------------------------------------------------------------------
59	# Data loading (identical to extract_activations.py)
60	# ---------------------------------------------------------------------------
61	
62	def load_mmlu(language, split="test"):
63	    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
64	    if language == "en":
65	        return load_dataset("cais/mmlu", "all", split=split)
66	    return load_dataset("CohereForAI/Global-MMLU", language, split=split)
67	
68	
69	def load_mmlu_dev(language):
70	    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
71	    for split_name in ["dev", "validation"]:
72	        try:
73	            return load_mmlu(language, split_name)
74	        except (ValueError, KeyError):
75	            continue
76	    raise RuntimeError(f"No dev/validation split found for '{language}'")
77	
78	
79	def normalize_row(row):
80	    """Normalize a dataset row to {question, choices, answer(int), subject}."""
81	    question = row.get("question", row.get("input", ""))
82	
83	    if "choices" in row and isinstance(row["choices"], list):
84	        choices = list(row["choices"])
85	    else:
86	        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]
87	
88	    answer = row.get("answer", row.get("target", 0))
89	    if isinstance(answer, str):
90	        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)
91	
92	    return {
93	        "question": question,
94	        "choices": choices,
95	        "answer": int(answer),
96	        "subject": row.get("subject", "unknown"),
97	    }
98	
99	
100	# ---------------------------------------------------------------------------
101	# Prompt formatting (identical to extract_activations.py)
102	# ---------------------------------------------------------------------------
103	
104	def _format_question(question, choices):
105	    parts = [f"{question}\n"]
106	    for i, c in enumerate(choices):
107	        parts.append(f"{LETTERS[i]}. {c}\n")
108	    return "".join(parts)
109	
110	
111	def build_prompt(row, few_shot_rows, n_shot):
112	    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
113	    subject_pretty = row["subject"].replace("_", " ")
114	    lines = [
115	        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
116	    ]
117	    for fs in few_shot_rows[:n_shot]:
118	        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
119	        lines.append(_format_question(fs["question"], fs["choices"]))
120	        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
121	    lines.append(_format_question(row["question"], row["choices"]))
122	    lines.append("Answer:")
123	    return "".join(lines)
124	
125	
126	# ---------------------------------------------------------------------------
127	# Model loading with quantization support
128	# ---------------------------------------------------------------------------
129	
130	def load_model(model_name, dtype, quantization):
131	    """Load model with optional INT4/INT8 quantization via bitsandbytes."""
132	    kwargs = dict(device_map="auto", trust_remote_code=True)
133	
134	    if quantization == "int4":
135	        from transformers import BitsAndBytesConfig
136	        kwargs["quantization_config"] = BitsAndBytesConfig(
137	            load_in_4bit=True,
138	            bnb_4bit_compute_dtype=torch.bfloat16,
139	            bnb_4bit_quant_type="nf4",
140	            bnb_4bit_use_double_quant=True,
141	        )
142	    elif quantization == "int8":
143	        from transformers import BitsAndBytesConfig
144	        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
145	    else:
146	        kwargs["torch_dtype"] = dtype
147	
148	    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
149	    model.eval()
150	    return model
151	
152	
153	# ---------------------------------------------------------------------------
154	# Architecture-adaptive layer access
155	# ---------------------------------------------------------------------------
156	
157	def get_layer_modules(model):
158	    """Return the nn.ModuleList of transformer layers, adapting to model architecture.
159	
160	    Tries common attribute paths used by different model families:
161	      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)
162	      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)
163	      - model.gpt_neox.layers   (GPT-NeoX variants)
164	    """
165	    candidates = [
166	        ("model.model.layers", lambda m: m.model.layers),
167	        ("model.transformer.h", lambda m: m.transformer.h),
168	        ("model.gpt_neox.layers", lambda m: m.gpt_neox.layers),
169	    ]
170	    for path_name, accessor in candidates:
171	        try:
172	            layers = accessor(model)
173	            if hasattr(layers, "__len__") and len(layers) > 0:
174	                print(f"  Layer access path: {path_name}  ({len(layers)} layers)")
175	                return layers
176	        except AttributeError:
177	            continue
178	    raise RuntimeError(
179	        "Cannot locate transformer layers. "
180	        "Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers"
181	    )
182	
183	
184	# ---------------------------------------------------------------------------
185	# Forward hook machinery
186	# ---------------------------------------------------------------------------
187	
188	def get_final_norm(model):
189	    """Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).
190	
191	    Used to apply post-norm on the last layer's hook output, matching the behavior of
192	    output_hidden_states=True which returns post-norm activations for the final layer.
193	    """
194	    candidates = [
195	        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma
196	        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J
197	        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX
198	    ]
199	    for accessor in candidates:
200	        try:
201	            norm = accessor(model)
202	            if norm is not None:
203	                return norm
204	        except AttributeError:
205	            continue
206	    return None
207	
208	
209	def register_activation_hooks(model, layer_indices, captured):
210	    """Register forward hooks on target layers to capture last-token hidden states.
211	
212	    Why hooks instead of output_hidden_states=True:
213	      output_hidden_states materializes ALL layers' hidden states in memory at once.
214	      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)
215	      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific
216	      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.
217	
218	    Post-norm on last layer:
219	      output_hidden_states returns post-norm activations for the final layer (i.e., after
220	      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency
221	      with MVP experiments that used output_hidden_states, we apply the final norm to the
222	      last layer's hook output. All other layers return pre-norm (direct layer output).
223	    """
224	    layers = get_layer_modules(model)
225	    n_layers = len(layers)
226	    final_norm = get_final_norm(model)
227	    max_target_layer = max(layer_indices)
228	    handles = []
229	
230	    def make_hook(layer_idx):
231	        def hook_fn(module, input, output):
232	            h = output[0] if isinstance(output, tuple) else output
233	            h = h[0, -1]
234	            # Apply final norm on the last transformer layer to match output_hidden_states behavior
235	            if layer_idx == n_layers - 1 and final_norm is not None:
236	                with torch.no_grad():
237	                    h = final_norm(h.unsqueeze(0)).squeeze(0)
238	            captured[layer_idx] = h.detach().cpu().float()
239	        return hook_fn
240	
241	    for li in layer_indices:
242	        if li < 0 or li >= n_layers:
243	            raise ValueError(f"Layer index {li} out of range [0, {n_layers})")
244	        handles.append(layers[li].register_forward_hook(make_hook(li)))
245	
246	    return handles
247	
248	
249	def remove_hooks(handles):
250	    for h in handles:
251	        h.remove()
252	
253	
254	# ---------------------------------------------------------------------------
255	# Incremental save / load
256	# ---------------------------------------------------------------------------
257	
258	def save_layer_data(storage, layer_indices, lang, output_dir):
259	    """Save accumulated activations for all target layers."""
260	    for li in layer_indices:
261	        if not storage[li]["acts"]:
262	            continue
263	        acts = torch.stack(storage[li]["acts"])
264	        labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
265	        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
266	        torch.save({"activations": acts, "labels": labels}, path)
267	
268	
269	def load_existing_progress(layer_indices, lang, output_dir):
270	    """Load previously saved data to support resumption after interruption."""
271	    storage = {li: {"acts": [], "labels": []} for li in layer_indices}
272	    n_existing = 0
273	    for li in layer_indices:
274	        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
275	        if os.path.exists(path):
276	            data = torch.load(path, weights_only=True)
277	            storage[li]["acts"] = list(data["activations"].unbind(0))
278	            storage[li]["labels"] = data["labels"].tolist()
279	            n_existing = max(n_existing, len(storage[li]["labels"]))
280	    return storage, n_existing
281	
282	
283	# ---------------------------------------------------------------------------
284	# Main extraction loop
285	# ---------------------------------------------------------------------------
286	
287	def main():
288	    args = parse_args()
289	    layer_indices = sorted(int(x) for x in args.layers.split(","))
290	    os.makedirs(args.output_dir, exist_ok=True)
291	
292	    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
293	    print(f"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}")
294	
295	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
296	    if tokenizer.pad_token is None:
297	        tokenizer.pad_token = tokenizer.eos_token
298	
299	    model = load_model(args.model, dtype, args.quantization)
300	
301	    n_model_layers = model.config.num_hidden_layers
302	    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
303	    for li in layer_indices:
304	        if li < 0 or li >= n_model_layers:
305	            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")
306	
307	    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
308	    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")
309	
310	    # Register hooks once — they persist across forward calls
311	    captured = {}
312	    handles = register_activation_hooks(model, layer_indices, captured)
313	
314	    try:
315	        for lang in args.languages:
316	            print(f"\n{'='*50}")
317	            print(f"  Language: {lang}")
318	            print(f"{'='*50}")
319	
320	            test_ds = load_mmlu(lang, "test")
321	            dev_ds = load_mmlu_dev(lang)
322	
323	            if args.subjects:
324	                test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
325	                dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)
326	
327	            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))
328	
329	            dev_by_subject: dict[str, list] = {}
330	            for r in dev_ds:
331	                dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
332	            dev_fallback = list(dev_ds)[:args.n_shot]
333	
334	            # Try to resume from existing partial results
335	            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)
336	            if n_existing > 0:
337	                print(f"  Resuming from sample {n_existing} (found existing data)")
338	
339	            for i in tqdm(range(n_existing, n), desc=f"[{lang}]", initial=n_existing, total=n):
340	                row = normalize_row(test_ds[i])
341	                few_shots = dev_by_subject.get(row["subject"], dev_fallback)
342	                prompt = build_prompt(row, few_shots, args.n_shot)
343	
344	                inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
345	                                   max_length=4096).to(model.device)
346	
347	                with torch.no_grad():
348	                    # No output_hidden_states — hooks capture what we need
349	                    out = model(**inputs)
350	
351	                logits_last = out.logits[0, -1]
352	                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
353	                pred = choice_logits.argmax().item()
354	                correct = int(pred == row["answer"])
355	
356	                for li in layer_indices:
357	                    storage[li]["acts"].append(captured[li])
358	                    storage[li]["labels"].append(correct)
359	
360	                captured.clear()
361	                del out, inputs
362	
363	                if (i + 1) % 100 == 0:
364	                    torch.cuda.empty_cache()
365	
366	                # Incremental save
367	                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:
368	                    save_layer_data(storage, layer_indices, lang, args.output_dir)
369	                    print(f"  [checkpoint] saved at sample {i + 1}")
370	
371	            # Final save for this language
372	            save_layer_data(storage, layer_indices, lang, args.output_dir)
373	            for li in layer_indices:
374	                n_samples = len(storage[li]["labels"])
375	                if n_samples > 0:
376	                    acc = sum(storage[li]["labels"]) / n_samples
377	                    path = os.path.join(args.output_dir, f"layer{li}_{lang}.pt")
378	                    print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}")
379	
380	    finally:
381	        # Always clean up hooks, even if an exception occurs
382	        remove_hooks(handles)
383	
384	    print("\nExtraction complete.")
385	
386	
387	if __name__ == "__main__":
388	    main()
389	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "de3d8cb1-6207-439c-942c-929ba57f0497",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
      "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 389,
      "startLine": 1,
      "totalLines": 389
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the current code. Let me implement the modifications:

1. Add `--split_ratio` and `--split_seed` CLI arguments
2. Update default languages to 20
3. Implement stratified split logic in main()
4. Save split files (train/eval) when split is active
5. Ensure cross-language consistency of split indices

Key design decisions:
- Do the split on the first language, save indices, reuse for all subsequent languages
- Modify `save_layer_data` to support saving train/eval subsets
- Keep backward compatibility when split_ratio=0

Let me write the modified code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "498ef424-da7c-4bcf-a3ef-35896738de5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCfpRZmxMoPvmzEq8QrZyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5528,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5528
      },
      "output_tokens": 9,
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

_source line 8_

Now I'll implement the modifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "ec5e1a8b-3499-427c-a1c7-bb5fe2236915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCfpRZmxMoPvmzEq8QrZyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5528,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5528
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01FPXo61PwFHjzwFroyN9bUP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])",
  "new_string": "    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "cd0d4185-4e65-4702-b113-49d208c61699",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCfpRZmxMoPvmzEq8QrZyu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5528,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5528
      },
      "output_tokens": 9,
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

_source line 10 · 2026-05-20T22:14:21.365Z_

<details><summary>↩ Tool result · `toolu_01FPXo61PwFHjzwFroyN9bUP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "e86713d1-02aa-4f16-946d-ccbabc7adb76",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])",
    "newString": "    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 7,
        "newStart": 39,
        "newLines": 9,
        "lines": [
          " def parse_args():",
          "     p = argparse.ArgumentParser()",
          "     p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")",
          "-    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])",
          "+    p.add_argument(\"--languages\", nargs=\"+\",",
          "+                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",",
          "+                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])",
          "     p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",",
          "                    help=\"Comma-separated transformer layer indices (0-indexed)\")",
          "     p.add_argument(\"--output_dir\", default=\"./activations\")"
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01CWkxMFJkXKyQpq1oMRKS9C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()",
  "new_string": "    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "1463d917-b700-4852-aef5-9d1f6f57cf02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5cbkMo8gyTEE3oRp5bqv5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 29700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 488
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

_source line 12 · 2026-05-20T22:14:26.517Z_

<details><summary>↩ Tool result · `toolu_01CWkxMFJkXKyQpq1oMRKS9C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "bccdb242-d1af-434e-bf32-39e68bf3b4a6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()",
    "newString": "    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 54,
        "oldLines": 6,
        "newStart": 54,
        "newLines": 10,
        "lines": [
          "                    help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")",
          "     p.add_argument(\"--save_interval\", type=int, default=500,",
          "                    help=\"Incrementally save every N samples (0 = only save at end)\")",
          "+    p.add_argument(\"--split_ratio\", type=float, default=0.0,",
          "+                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")",
          "+    p.add_argument(\"--split_seed\", type=int, default=42,",
          "+                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")",
          "     return p.parse_args()",
          " ",
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

### Assistant

_source line 13_

Now I need to modify `save_layer_data` to support saving train/eval splits, and update `main()` with the split logic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "19625ce2-801b-4e1b-8d7e-14cceeeda2cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKy5PRchsoKxU2HFJ273e3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 30188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01C5CcV3nHn19s4pMHGufzan`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "def save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)",
  "new_string": "def save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "5f08a2cc-745b-430d-87c6-1928b732f64f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKy5PRchsoKxU2HFJ273e3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 30188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
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

_source line 15 · 2026-05-20T22:14:36.771Z_

<details><summary>↩ Tool result · `toolu_01C5CcV3nHn19s4pMHGufzan`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "a7b7c479-a0b0-4e9f-ba71-7c6b4687172a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "def save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)",
    "newString": "def save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 261,
        "oldLines": 17,
        "newStart": 261,
        "newLines": 32,
        "lines": [
          " # Incremental save / load",
          " # ---------------------------------------------------------------------------",
          " ",
          "-def save_layer_data(storage, layer_indices, lang, output_dir):",
          "-    \"\"\"Save accumulated activations for all target layers.\"\"\"",
          "+def save_layer_data(storage, layer_indices, lang, output_dir,",
          "+                    train_indices=None, eval_indices=None):",
          "+    \"\"\"Save accumulated activations for all target layers.",
          "+",
          "+    If train_indices/eval_indices are provided, saves separate train/eval files",
          "+    instead of a single file.",
          "+    \"\"\"",
          "     for li in layer_indices:",
          "         if not storage[li][\"acts\"]:",
          "             continue",
          "         acts = torch.stack(storage[li][\"acts\"])",
          "         labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)",
          "-        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")",
          "-        torch.save({\"activations\": acts, \"labels\": labels}, path)",
          " ",
          "+        if train_indices is not None and eval_indices is not None:",
          "+            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:",
          "+                idx = [i for i in indices if i < len(acts)]",
          "+                if not idx:",
          "+                    continue",
          "+                idx_t = torch.tensor(idx, dtype=torch.long)",
          "+                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")",
          "+                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)",
          "+        else:",
          "+            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")",
          "+            torch.save({\"activations\": acts, \"labels\": labels}, path)",
          " ",
          "+",
          " def load_existing_progress(layer_indices, lang, output_dir):",
          "     \"\"\"Load previously saved data to support resumption after interruption.\"\"\"",
          "     storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}"
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

_source line 16_

Now update `main()` to handle the split logic. I need to add the split computation after data loading, and pass indices to `save_layer_data`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "55b96e86-0f55-4399-a75e-90371da1908e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmZzw4RzYNZ1Q9tec8Ldcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 30596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 689
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01Phr75cmraq9oLrBPLnWdQx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:",
  "new_string": "    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "8903d2ac-2cd4-4cfc-875a-7e80e1337249",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmZzw4RzYNZ1Q9tec8Ldcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 30596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 689
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

_source line 18 · 2026-05-20T22:14:42.698Z_

<details><summary>↩ Tool result · `toolu_01Phr75cmraq9oLrBPLnWdQx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "8bc49880-28c3-454d-9283-fb1c2a622272",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:",
    "newString": "    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 328,
        "oldLines": 12,
        "newStart": 328,
        "newLines": 16,
        "lines": [
          "     answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]",
          "     print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")",
          " ",
          "+    # Split indices: computed once on the first language, reused for all",
          "+    split_train_indices = None",
          "+    split_eval_indices = None",
          "+",
          "     # Register hooks once — they persist across forward calls",
          "     captured = {}",
          "     handles = register_activation_hooks(model, layer_indices, captured)",
          " ",
          "     try:",
          "-        for lang in args.languages:",
          "+        for lang_idx, lang in enumerate(args.languages):",
          "             print(f\"\\n{'='*50}\")",
          "             print(f\"  Language: {lang}\")",
          "             print(f\"{'='*50}\")"
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

_source line 19_

Now add split computation after `n` is determined and before the extraction loop:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "89219f82-fa0c-4c65-a3f2-72932d409e20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJA1xYLVn49uWZAWCyaujM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 31285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
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

<details open><summary>🔧 Tool call — Edit · `toolu_017ypxW7bpRgNdF6ABLfrqm1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}",
  "new_string": "            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            # Compute split on first language, reuse for all subsequent languages\n            if args.split_ratio > 0 and split_train_indices is None:\n                from sklearn.model_selection import train_test_split\n                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]\n                split_train_indices, split_eval_indices = train_test_split(\n                    list(range(n)), train_size=args.split_ratio,\n                    stratify=subjects, random_state=args.split_seed,\n                )\n                split_path = os.path.join(args.output_dir, \"split_indices.pt\")\n                torch.save({\n                    \"train\": split_train_indices, \"eval\": split_eval_indices,\n                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,\n                    \"n_total\": n, \"first_lang\": lang,\n                }, split_path)\n                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")\n\n            dev_by_subject: dict[str, list] = {}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "9d9e9cc0-bcb7-48a6-80ea-5aec059b99b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJA1xYLVn49uWZAWCyaujM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 31285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
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

_source line 21 · 2026-05-20T22:14:57.296Z_

<details><summary>↩ Tool result · `toolu_017ypxW7bpRgNdF6ABLfrqm1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "53d0efb6-930b-42a6-9839-c76ff649186a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}",
    "newString": "            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            # Compute split on first language, reuse for all subsequent languages\n            if args.split_ratio > 0 and split_train_indices is None:\n                from sklearn.model_selection import train_test_split\n                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]\n                split_train_indices, split_eval_indices = train_test_split(\n                    list(range(n)), train_size=args.split_ratio,\n                    stratify=subjects, random_state=args.split_seed,\n                )\n                split_path = os.path.join(args.output_dir, \"split_indices.pt\")\n                torch.save({\n                    \"train\": split_train_indices, \"eval\": split_eval_indices,\n                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,\n                    \"n_total\": n, \"first_lang\": lang,\n                }, split_path)\n                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")\n\n            dev_by_subject: dict[str, list] = {}",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 351,
        "oldLines": 6,
        "newStart": 351,
        "newLines": 22,
        "lines": [
          " ",
          "             n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))",
          " ",
          "+            # Compute split on first language, reuse for all subsequent languages",
          "+            if args.split_ratio > 0 and split_train_indices is None:",
          "+                from sklearn.model_selection import train_test_split",
          "+                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]",
          "+                split_train_indices, split_eval_indices = train_test_split(",
          "+                    list(range(n)), train_size=args.split_ratio,",
          "+                    stratify=subjects, random_state=args.split_seed,",
          "+                )",
          "+                split_path = os.path.join(args.output_dir, \"split_indices.pt\")",
          "+                torch.save({",
          "+                    \"train\": split_train_indices, \"eval\": split_eval_indices,",
          "+                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,",
          "+                    \"n_total\": n, \"first_lang\": lang,",
          "+                }, split_path)",
          "+                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")",
          "+",
          "             dev_by_subject: dict[str, list] = {}",
          "             for r in dev_ds:",
          "                 dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)"
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

_source line 22_

Now update the `save_layer_data` calls and the final summary to pass split indices:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "df5858af-254b-41e6-a075-223ae69a0c54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPsM1y9Zs5irtyUzQ5kVA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 31659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

<details open><summary>🔧 Tool call — Edit · `toolu_01CMCx9MgFkD3ndjsKuSDn3p`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "old_string": "                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")",
  "new_string": "                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir,\n                                    split_train_indices, split_eval_indices)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir,\n                            split_train_indices, split_eval_indices)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    if split_train_indices is not None:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt\")\n                    else:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "19408894-4dd3-4f1e-a349-95547302cd5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPsM1y9Zs5irtyUzQ5kVA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 31659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 701
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

_source line 24 · 2026-05-20T22:15:14.086Z_

<details><summary>↩ Tool result · `toolu_01CMCx9MgFkD3ndjsKuSDn3p`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "b278d633-9a43-4bdd-8371-edf32a4ac48e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "oldString": "                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")",
    "newString": "                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir,\n                                    split_train_indices, split_eval_indices)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir,\n                            split_train_indices, split_eval_indices)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    if split_train_indices is not None:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt\")\n                    else:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt\")",
    "originalFile": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            # Compute split on first language, reuse for all subsequent languages\n            if args.split_ratio > 0 and split_train_indices is None:\n                from sklearn.model_selection import train_test_split\n                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]\n                split_train_indices, split_eval_indices = train_test_split(\n                    list(range(n)), train_size=args.split_ratio,\n                    stratify=subjects, random_state=args.split_seed,\n                )\n                split_path = os.path.join(args.output_dir, \"split_indices.pt\")\n                torch.save({\n                    \"train\": split_train_indices, \"eval\": split_eval_indices,\n                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,\n                    \"n_total\": n, \"first_lang\": lang,\n                }, split_path)\n                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 406,
        "oldLines": 17,
        "newStart": 406,
        "newLines": 21,
        "lines": [
          " ",
          "                 # Incremental save",
          "                 if args.save_interval > 0 and (i + 1) % args.save_interval == 0:",
          "-                    save_layer_data(storage, layer_indices, lang, args.output_dir)",
          "+                    save_layer_data(storage, layer_indices, lang, args.output_dir,",
          "+                                    split_train_indices, split_eval_indices)",
          "                     print(f\"  [checkpoint] saved at sample {i + 1}\")",
          " ",
          "             # Final save for this language",
          "-            save_layer_data(storage, layer_indices, lang, args.output_dir)",
          "+            save_layer_data(storage, layer_indices, lang, args.output_dir,",
          "+                            split_train_indices, split_eval_indices)",
          "             for li in layer_indices:",
          "                 n_samples = len(storage[li][\"labels\"])",
          "                 if n_samples > 0:",
          "                     acc = sum(storage[li][\"labels\"]) / n_samples",
          "-                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")",
          "-                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")",
          "+                    if split_train_indices is not None:",
          "+                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt\")",
          "+                    else:",
          "+                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt\")",
          " ",
          "     finally:",
          "         # Always clean up hooks, even if an exception occurs"
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

_source line 25_

Let me verify the final state of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "f2e512ad-77e4-450a-b3ec-f014ee352724",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPviQGm9ZGMM5erjjX8AyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 32360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 762
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01DNc1EieE7DreqZFSEjyRkX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "7f51dd3d-a1e6-43b4-a162-0a126d398eaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPviQGm9ZGMM5erjjX8AyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 32360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 762
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

_source line 27 · 2026-05-20T22:15:17.618Z_

<details><summary>↩ Tool result · `toolu_01DNc1EieE7DreqZFSEjyRkX`</summary>

```text
1	"""
2	Extract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).
3	
4	Differences from extract_activations.py:
5	  - Uses register_forward_hook instead of output_hidden_states=True.
6	    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,
7	    which is prohibitive for 94-layer models. Hooks capture only the target layers.
8	  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).
9	  - Incremental saving via --save_interval to survive OOM or interruption.
10	  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).
11	
12	Output format is identical to extract_activations.py:
13	  layer{i}_{lang}.pt  ->  {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}
14	
15	Dependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm
16	
17	Usage:
18	  python extract_activations_large.py \
19	    --model Qwen/Qwen3-235B-A22B \
20	    --languages en zh ar hi sw ko \
21	    --layers 0,8,16,24,32,48,64,80,93 \
22	    --output_dir ./activations \
23	    --quantization int4 \
24	    --save_interval 200
25	"""
26	
27	import argparse
28	import os
29	
30	import torch
31	from datasets import load_dataset
32	from transformers import AutoModelForCausalLM, AutoTokenizer
33	from tqdm import tqdm
34	
35	
36	LETTERS = ["A", "B", "C", "D"]
37	
38	
39	def parse_args():
40	    p = argparse.ArgumentParser()
41	    p.add_argument("--model", required=True, help="HuggingFace model name or path")
42	    p.add_argument("--languages", nargs="+",
43	                   default=["en", "zh", "ar", "hi", "sw", "ko", "es", "fr", "de", "ru",
44	                            "tr", "bn", "ja", "pt", "vi", "te", "id", "pl", "nl", "uk"])
45	    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
46	                   help="Comma-separated transformer layer indices (0-indexed)")
47	    p.add_argument("--output_dir", default="./activations")
48	    p.add_argument("--n_shot", type=int, default=5)
49	    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
50	    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
51	    p.add_argument("--subjects", nargs="*", default=None,
52	                   help="Restrict to these MMLU subjects (default: all)")
53	    p.add_argument("--quantization", default="none", choices=["none", "int4", "int8"],
54	                   help="Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)")
55	    p.add_argument("--save_interval", type=int, default=500,
56	                   help="Incrementally save every N samples (0 = only save at end)")
57	    p.add_argument("--split_ratio", type=float, default=0.0,
58	                   help="If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval")
59	    p.add_argument("--split_seed", type=int, default=42,
60	                   help="Random seed for train/eval split (ensures reproducibility across languages)")
61	    return p.parse_args()
62	
63	
64	# ---------------------------------------------------------------------------
65	# Data loading (identical to extract_activations.py)
66	# ---------------------------------------------------------------------------
67	
68	def load_mmlu(language, split="test"):
69	    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
70	    if language == "en":
71	        return load_dataset("cais/mmlu", "all", split=split)
72	    return load_dataset("CohereForAI/Global-MMLU", language, split=split)
73	
74	
75	def load_mmlu_dev(language):
76	    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
77	    for split_name in ["dev", "validation"]:
78	        try:
79	            return load_mmlu(language, split_name)
80	        except (ValueError, KeyError):
81	            continue
82	    raise RuntimeError(f"No dev/validation split found for '{language}'")
83	
84	
85	def normalize_row(row):
86	    """Normalize a dataset row to {question, choices, answer(int), subject}."""
87	    question = row.get("question", row.get("input", ""))
88	
89	    if "choices" in row and isinstance(row["choices"], list):
90	        choices = list(row["choices"])
91	    else:
92	        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]
93	
94	    answer = row.get("answer", row.get("target", 0))
95	    if isinstance(answer, str):
96	        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)
97	
98	    return {
99	        "question": question,
100	        "choices": choices,
101	        "answer": int(answer),
102	        "subject": row.get("subject", "unknown"),
103	    }
104	
105	
106	# ---------------------------------------------------------------------------
107	# Prompt formatting (identical to extract_activations.py)
108	# ---------------------------------------------------------------------------
109	
110	def _format_question(question, choices):
111	    parts = [f"{question}\n"]
112	    for i, c in enumerate(choices):
113	        parts.append(f"{LETTERS[i]}. {c}\n")
114	    return "".join(parts)
115	
116	
117	def build_prompt(row, few_shot_rows, n_shot):
118	    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
119	    subject_pretty = row["subject"].replace("_", " ")
120	    lines = [
121	        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
122	    ]
123	    for fs in few_shot_rows[:n_shot]:
124	        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
125	        lines.append(_format_question(fs["question"], fs["choices"]))
126	        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
127	    lines.append(_format_question(row["question"], row["choices"]))
128	    lines.append("Answer:")
129	    return "".join(lines)
130	
131	
132	# ---------------------------------------------------------------------------
133	# Model loading with quantization support
134	# ---------------------------------------------------------------------------
135	
136	def load_model(model_name, dtype, quantization):
137	    """Load model with optional INT4/INT8 quantization via bitsandbytes."""
138	    kwargs = dict(device_map="auto", trust_remote_code=True)
139	
140	    if quantization == "int4":
141	        from transformers import BitsAndBytesConfig
142	        kwargs["quantization_config"] = BitsAndBytesConfig(
143	            load_in_4bit=True,
144	            bnb_4bit_compute_dtype=torch.bfloat16,
145	            bnb_4bit_quant_type="nf4",
146	            bnb_4bit_use_double_quant=True,
147	        )
148	    elif quantization == "int8":
149	        from transformers import BitsAndBytesConfig
150	        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
151	    else:
152	        kwargs["torch_dtype"] = dtype
153	
154	    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
155	    model.eval()
156	    return model
157	
158	
159	# ---------------------------------------------------------------------------
160	# Architecture-adaptive layer access
161	# ---------------------------------------------------------------------------
162	
163	def get_layer_modules(model):
164	    """Return the nn.ModuleList of transformer layers, adapting to model architecture.
165	
166	    Tries common attribute paths used by different model families:
167	      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)
168	      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)
169	      - model.gpt_neox.layers   (GPT-NeoX variants)
170	    """
171	    candidates = [
172	        ("model.model.layers", lambda m: m.model.layers),
173	        ("model.transformer.h", lambda m: m.transformer.h),
174	        ("model.gpt_neox.layers", lambda m: m.gpt_neox.layers),
175	    ]
176	    for path_name, accessor in candidates:
177	        try:
178	            layers = accessor(model)
179	            if hasattr(layers, "__len__") and len(layers) > 0:
180	                print(f"  Layer access path: {path_name}  ({len(layers)} layers)")
181	                return layers
182	        except AttributeError:
183	            continue
184	    raise RuntimeError(
185	        "Cannot locate transformer layers. "
186	        "Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers"
187	    )
188	
189	
190	# ---------------------------------------------------------------------------
191	# Forward hook machinery
192	# ---------------------------------------------------------------------------
193	
194	def get_final_norm(model):
195	    """Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).
196	
197	    Used to apply post-norm on the last layer's hook output, matching the behavior of
198	    output_hidden_states=True which returns post-norm activations for the final layer.
199	    """
200	    candidates = [
201	        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma
202	        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J
203	        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX
204	    ]
205	    for accessor in candidates:
206	        try:
207	            norm = accessor(model)
208	            if norm is not None:
209	                return norm
210	        except AttributeError:
211	            continue
212	    return None
213	
214	
215	def register_activation_hooks(model, layer_indices, captured):
216	    """Register forward hooks on target layers to capture last-token hidden states.
217	
218	    Why hooks instead of output_hidden_states=True:
219	      output_hidden_states materializes ALL layers' hidden states in memory at once.
220	      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)
221	      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific
222	      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.
223	
224	    Post-norm on last layer:
225	      output_hidden_states returns post-norm activations for the final layer (i.e., after
226	      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency
227	      with MVP experiments that used output_hidden_states, we apply the final norm to the
228	      last layer's hook output. All other layers return pre-norm (direct layer output).
229	    """
230	    layers = get_layer_modules(model)
231	    n_layers = len(layers)
232	    final_norm = get_final_norm(model)
233	    max_target_layer = max(layer_indices)
234	    handles = []
235	
236	    def make_hook(layer_idx):
237	        def hook_fn(module, input, output):
238	            h = output[0] if isinstance(output, tuple) else output
239	            h = h[0, -1]
240	            # Apply final norm on the last transformer layer to match output_hidden_states behavior
241	            if layer_idx == n_layers - 1 and final_norm is not None:
242	                with torch.no_grad():
243	                    h = final_norm(h.unsqueeze(0)).squeeze(0)
244	            captured[layer_idx] = h.detach().cpu().float()
245	        return hook_fn
246	
247	    for li in layer_indices:
248	        if li < 0 or li >= n_layers:
249	            raise ValueError(f"Layer index {li} out of range [0, {n_layers})")
250	        handles.append(layers[li].register_forward_hook(make_hook(li)))
251	
252	    return handles
253	
254	
255	def remove_hooks(handles):
256	    for h in handles:
257	        h.remove()
258	
259	
260	# ---------------------------------------------------------------------------
261	# Incremental save / load
262	# ---------------------------------------------------------------------------
263	
264	def save_layer_data(storage, layer_indices, lang, output_dir,
265	                    train_indices=None, eval_indices=None):
266	    """Save accumulated activations for all target layers.
267	
268	    If train_indices/eval_indices are provided, saves separate train/eval files
269	    instead of a single file.
270	    """
271	    for li in layer_indices:
272	        if not storage[li]["acts"]:
273	            continue
274	        acts = torch.stack(storage[li]["acts"])
275	        labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
276	
277	        if train_indices is not None and eval_indices is not None:
278	            for suffix, indices in [("train", train_indices), ("eval", eval_indices)]:
279	                idx = [i for i in indices if i < len(acts)]
280	                if not idx:
281	                    continue
282	                idx_t = torch.tensor(idx, dtype=torch.long)
283	                path = os.path.join(output_dir, f"layer{li}_{lang}_{suffix}.pt")
284	                torch.save({"activations": acts[idx_t], "labels": labels[idx_t]}, path)
285	        else:
286	            path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
287	            torch.save({"activations": acts, "labels": labels}, path)
288	
289	
290	def load_existing_progress(layer_indices, lang, output_dir):
291	    """Load previously saved data to support resumption after interruption."""
292	    storage = {li: {"acts": [], "labels": []} for li in layer_indices}
293	    n_existing = 0
294	    for li in layer_indices:
295	        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
296	        if os.path.exists(path):
297	            data = torch.load(path, weights_only=True)
298	            storage[li]["acts"] = list(data["activations"].unbind(0))
299	            storage[li]["labels"] = data["labels"].tolist()
300	            n_existing = max(n_existing, len(storage[li]["labels"]))
301	    return storage, n_existing
302	
303	
304	# ---------------------------------------------------------------------------
305	# Main extraction loop
306	# ---------------------------------------------------------------------------
307	
308	def main():
309	    args = parse_args()
310	    layer_indices = sorted(int(x) for x in args.layers.split(","))
311	    os.makedirs(args.output_dir, exist_ok=True)
312	
313	    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
314	    print(f"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}")
315	
316	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
317	    if tokenizer.pad_token is None:
318	        tokenizer.pad_token = tokenizer.eos_token
319	
320	    model = load_model(args.model, dtype, args.quantization)
321	
322	    n_model_layers = model.config.num_hidden_layers
323	    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
324	    for li in layer_indices:
325	        if li < 0 or li >= n_model_layers:
326	            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")
327	
328	    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
329	    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")
330	
331	    # Split indices: computed once on the first language, reused for all
332	    split_train_indices = None
333	    split_eval_indices = None
334	
335	    # Register hooks once — they persist across forward calls
336	    captured = {}
337	    handles = register_activation_hooks(model, layer_indices, captured)
338	
339	    try:
340	        for lang_idx, lang in enumerate(args.languages):
341	            print(f"\n{'='*50}")
342	            print(f"  Language: {lang}")
343	            print(f"{'='*50}")
344	
345	            test_ds = load_mmlu(lang, "test")
346	            dev_ds = load_mmlu_dev(lang)
347	
348	            if args.subjects:
349	                test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
350	                dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)
351	
352	            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))
353	
354	            # Compute split on first language, reuse for all subsequent languages
355	            if args.split_ratio > 0 and split_train_indices is None:
356	                from sklearn.model_selection import train_test_split
357	                subjects = [normalize_row(test_ds[i])["subject"] for i in range(n)]
358	                split_train_indices, split_eval_indices = train_test_split(
359	                    list(range(n)), train_size=args.split_ratio,
360	                    stratify=subjects, random_state=args.split_seed,
361	                )
362	                split_path = os.path.join(args.output_dir, "split_indices.pt")
363	                torch.save({
364	                    "train": split_train_indices, "eval": split_eval_indices,
365	                    "split_ratio": args.split_ratio, "seed": args.split_seed,
366	                    "n_total": n, "first_lang": lang,
367	                }, split_path)
368	                print(f"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})")
369	
370	            dev_by_subject: dict[str, list] = {}
371	            for r in dev_ds:
372	                dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
373	            dev_fallback = list(dev_ds)[:args.n_shot]
374	
375	            # Try to resume from existing partial results
376	            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)
377	            if n_existing > 0:
378	                print(f"  Resuming from sample {n_existing} (found existing data)")
379	
380	            for i in tqdm(range(n_existing, n), desc=f"[{lang}]", initial=n_existing, total=n):
381	                row = normalize_row(test_ds[i])
382	                few_shots = dev_by_subject.get(row["subject"], dev_fallback)
383	                prompt = build_prompt(row, few_shots, args.n_shot)
384	
385	                inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
386	                                   max_length=4096).to(model.device)
387	
388	                with torch.no_grad():
389	                    # No output_hidden_states — hooks capture what we need
390	                    out = model(**inputs)
391	
392	                logits_last = out.logits[0, -1]
393	                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
394	                pred = choice_logits.argmax().item()
395	                correct = int(pred == row["answer"])
396	
397	                for li in layer_indices:
398	                    storage[li]["acts"].append(captured[li])
399	                    storage[li]["labels"].append(correct)
400	
401	                captured.clear()
402	                del out, inputs
403	
404	                if (i + 1) % 100 == 0:
405	                    torch.cuda.empty_cache()
406	
407	                # Incremental save
408	                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:
409	                    save_layer_data(storage, layer_indices, lang, args.output_dir,
410	                                    split_train_indices, split_eval_indices)
411	                    print(f"  [checkpoint] saved at sample {i + 1}")
412	
413	            # Final save for this language
414	            save_layer_data(storage, layer_indices, lang, args.output_dir,
415	                            split_train_indices, split_eval_indices)
416	            for li in layer_indices:
417	                n_samples = len(storage[li]["labels"])
418	                if n_samples > 0:
419	                    acc = sum(storage[li]["labels"]) / n_samples
420	                    if split_train_indices is not None:
421	                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt")
422	                    else:
423	                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt")
424	
425	    finally:
426	        # Always clean up hooks, even if an exception occurs
427	        remove_hooks(handles)
428	
429	    print("\nExtraction complete.")
430	
431	
432	if __name__ == "__main__":
433	    main()
434	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "1fa1a8bf-fd66-4b7c-b7f2-c73309576033",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
      "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            # Compute split on first language, reuse for all subsequent languages\n            if args.split_ratio > 0 and split_train_indices is None:\n                from sklearn.model_selection import train_test_split\n                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]\n                split_train_indices, split_eval_indices = train_test_split(\n                    list(range(n)), train_size=args.split_ratio,\n                    stratify=subjects, random_state=args.split_seed,\n                )\n                split_path = os.path.join(args.output_dir, \"split_indices.pt\")\n                torch.save({\n                    \"train\": split_train_indices, \"eval\": split_eval_indices,\n                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,\n                    \"n_total\": n, \"first_lang\": lang,\n                }, split_path)\n                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir,\n                                    split_train_indices, split_eval_indices)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir,\n                            split_train_indices, split_eval_indices)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    if split_train_indices is not None:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt\")\n                    else:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 434,
      "startLine": 1,
      "totalLines": 434
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

代码修改完成。现在部署到服务器。先加载 SSH 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "d42a1b9b-ff98-4c43-93bb-2ebca07ca2d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DWYLJ6PRSQsJoCbKc2V99",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6337,
      "cache_read_input_tokens": 33122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6337
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

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YSZPKrw2cJ6145fqrNPpez`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "b8e6eec9-810b-4250-8f85-b7e639bad10f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DWYLJ6PRSQsJoCbKc2V99",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6337,
      "cache_read_input_tokens": 33122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6337
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

_source line 30 · 2026-05-20T22:15:22.274Z_

<details><summary>↩ Tool result · `toolu_01YSZPKrw2cJ6145fqrNPpez`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "bf849074-bf85-44db-b6c8-50b4f933c118",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I need to deploy the file to the server. I'll read the file content and use ssh_execute to write it via cat heredoc. The file is ~434 lines, so I'll need to be careful with the heredoc delimiter.

Let me deploy to both locations:
1. `/root/xling_calib_direction/code/extract_activations_large.py`
2. `/root/xling_calib_direction/extract_activations_large.py`

I'll read the file content and construct the ssh_execute command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "2decf5f8-c0bc-46a0-af80-73a28376722d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sWLYWv1n6VRfQ1NUJcYBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 39459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 695
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Read · `toolu_01S8YCDSzG1hrZojFXzGoA63`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "9b83dae1-aab3-475f-befb-a51a13e216d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sWLYWv1n6VRfQ1NUJcYBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 39459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 695
      },
      "output_tokens": 22,
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

_source line 33 · 2026-05-20T22:15:41.293Z_

<details><summary>↩ Tool result · `toolu_01S8YCDSzG1hrZojFXzGoA63`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "75eb2d27-5beb-4c67-b58d-961bda84948a",
  "tool_use_result": {
    "type": "file_unchanged",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py"
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_013SRkfAFHa3TSNhnsXPdMNf`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py | base64 -w0",
  "description": "Base64 encode file for safe transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "0e72c4c8-56de-4a35-9081-b90396603913",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rPAJjRqbSWjeA3bNd84rj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 40154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
      },
      "output_tokens": 70,
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

_source line 35 · 2026-05-20T22:15:46.717Z_

<details><summary>↩ Tool result · `toolu_013SRkfAFHa3TSNhnsXPdMNf`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "41302407-dbeb-4029-a6f1-5d86194a1f9c",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
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

部署到服务器两个路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "483b3436-3fca-42cf-a6bf-fff5539557e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNv3x2BFRq33X7bCefQuUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20392,
      "cache_read_input_tokens": 40426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20392
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

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KakuPSWrtwqfAkGaVY3F8h`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "mkdir -p /root/xling_calib_direction/code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "8683a2f8-f7c2-4922-a307-30b44e7c7dc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNv3x2BFRq33X7bCefQuUJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20392,
      "cache_read_input_tokens": 40426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20392
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

_source line 38 · 2026-05-20T22:15:58.713Z_

<details><summary>↩ Tool result · `toolu_01KakuPSWrtwqfAkGaVY3F8h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "48aaf0cd-4c69-4114-aedc-14a534ee2272",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.99}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01PGCdnLemPABATKCSANFMBR`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "description": "Read file content for heredoc transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "8a5f94ae-edcd-40c7-8ae9-343cefeff237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fp18qPJk9w8NxiwJByLxzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 60818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
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

_source line 40 · 2026-05-20T22:16:04.231Z_

<details><summary>↩ Tool result · `toolu_01PGCdnLemPABATKCSANFMBR`</summary>

```text
"""
Extract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).

Differences from extract_activations.py:
  - Uses register_forward_hook instead of output_hidden_states=True.
    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,
    which is prohibitive for 94-layer models. Hooks capture only the target layers.
  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).
  - Incremental saving via --save_interval to survive OOM or interruption.
  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).

Output format is identical to extract_activations.py:
  layer{i}_{lang}.pt  ->  {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}

Dependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm

Usage:
  python extract_activations_large.py \
    --model Qwen/Qwen3-235B-A22B \
    --languages en zh ar hi sw ko \
    --layers 0,8,16,24,32,48,64,80,93 \
    --output_dir ./activations \
    --quantization int4 \
    --save_interval 200
"""

import argparse
import os

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm


LETTERS = ["A", "B", "C", "D"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="HuggingFace model name or path")
    p.add_argument("--languages", nargs="+",
                   default=["en", "zh", "ar", "hi", "sw", "ko", "es", "fr", "de", "ru",
                            "tr", "bn", "ja", "pt", "vi", "te", "id", "pl", "nl", "uk"])
    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
                   help="Comma-separated transformer layer indices (0-indexed)")
    p.add_argument("--output_dir", default="./activations")
    p.add_argument("--n_shot", type=int, default=5)
    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
    p.add_argument("--subjects", nargs="*", default=None,
                   help="Restrict to these MMLU subjects (default: all)")
    p.add_argument("--quantization", default="none", choices=["none", "int4", "int8"],
                   help="Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)")
    p.add_argument("--save_interval", type=int, default=500,
                   help="Incrementally save every N samples (0 = only save at end)")
    p.add_argument("--split_ratio", type=float, default=0.0,
                   help="If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval")
    p.add_argument("--split_seed", type=int, default=42,
                   help="Random seed for train/eval split (ensures reproducibility across languages)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading (identical to extract_activations.py)
# ---------------------------------------------------------------------------

def load_mmlu(language, split="test"):
    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
    if language == "en":
        return load_dataset("cais/mmlu", "all", split=split)
    return load_dataset("CohereForAI/Global-MMLU", language, split=split)


def load_mmlu_dev(language):
    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
    for split_name in ["dev", "validation"]:
        try:
            return load_mmlu(language, split_name)
        except (ValueError, KeyError):
            continue
    raise RuntimeError(f"No dev/validation split found for '{language}'")


def normalize_row(row):
    """Normalize a dataset row to {question, choices, answer(int), subject}."""
    question = row.get("question", row.get("input", ""))

    if "choices" in row and isinstance(row["choices"], list):
        choices = list(row["choices"])
    else:
        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]

    answer = row.get("answer", row.get("target", 0))
    if isinstance(answer, str):
        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)

    return {
        "question": question,
        "choices": choices,
        "answer": int(answer),
        "subject": row.get("subject", "unknown"),
    }


# ---------------------------------------------------------------------------
# Prompt formatting (identical to extract_activations.py)
# ---------------------------------------------------------------------------

def _format_question(question, choices):
    parts = [f"{question}\n"]
    for i, c in enumerate(choices):
        parts.append(f"{LETTERS[i]}. {c}\n")
    return "".join(parts)


def build_prompt(row, few_shot_rows, n_shot):
    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
    subject_pretty = row["subject"].replace("_", " ")
    lines = [
        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
    ]
    for fs in few_shot_rows[:n_shot]:
        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
        lines.append(_format_question(fs["question"], fs["choices"]))
        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
    lines.append(_format_question(row["question"], row["choices"]))
    lines.append("Answer:")
    return "".join(lines)


# ---------------------------------------------------------------------------
# Model loading with quantization support
# ---------------------------------------------------------------------------

def load_model(model_name, dtype, quantization):
    """Load model with optional INT4/INT8 quantization via bitsandbytes."""
    kwargs = dict(device_map="auto", trust_remote_code=True)

    if quantization == "int4":
        from transformers import BitsAndBytesConfig
        kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    elif quantization == "int8":
        from transformers import BitsAndBytesConfig
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
    else:
        kwargs["torch_dtype"] = dtype

    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    model.eval()
    return model


# ---------------------------------------------------------------------------
# Architecture-adaptive layer access
# ---------------------------------------------------------------------------

def get_layer_modules(model):
    """Return the nn.ModuleList of transformer layers, adapting to model architecture.

    Tries common attribute paths used by different model families:
      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)
      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)
      - model.gpt_neox.layers   (GPT-NeoX variants)
    """
    candidates = [
        ("model.model.layers", lambda m: m.model.layers),
        ("model.transformer.h", lambda m: m.transformer.h),
        ("model.gpt_neox.layers", lambda m: m.gpt_neox.layers),
    ]
    for path_name, accessor in candidates:
        try:
            layers = accessor(model)
            if hasattr(layers, "__len__") and len(layers) > 0:
                print(f"  Layer access path: {path_name}  ({len(layers)} layers)")
                return layers
        except AttributeError:
            continue
    raise RuntimeError(
        "Cannot locate transformer layers. "
        "Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers"
    )


# ---------------------------------------------------------------------------
# Forward hook machinery
# ---------------------------------------------------------------------------

def get_final_norm(model):
    """Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).

    Used to apply post-norm on the last layer's hook output, matching the behavior of
    output_hidden_states=True which returns post-norm activations for the final layer.
    """
    candidates = [
        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma
        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J
        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX
    ]
    for accessor in candidates:
        try:
            norm = accessor(model)
            if norm is not None:
                return norm
        except AttributeError:
            continue
    return None


def register_activation_hooks(model, layer_indices, captured):
    """Register forward hooks on target layers to capture last-token hidden states.

    Why hooks instead of output_hidden_states=True:
      output_hidden_states materializes ALL layers' hidden states in memory at once.
      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)
      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific
      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.

    Post-norm on last layer:
      output_hidden_states returns post-norm activations for the final layer (i.e., after
      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency
      with MVP experiments that used output_hidden_states, we apply the final norm to the
      last layer's hook output. All other layers return pre-norm (direct layer output).
    """
    layers = get_layer_modules(model)
    n_layers = len(layers)
    final_norm = get_final_norm(model)
    max_target_layer = max(layer_indices)
    handles = []

    def make_hook(layer_idx):
        def hook_fn(module, input, output):
            h = output[0] if isinstance(output, tuple) else output
            h = h[0, -1]
            # Apply final norm on the last transformer layer to match output_hidden_states behavior
            if layer_idx == n_layers - 1 and final_norm is not None:
                with torch.no_grad():
                    h = final_norm(h.unsqueeze(0)).squeeze(0)
            captured[layer_idx] = h.detach().cpu().float()
        return hook_fn

    for li in layer_indices:
        if li < 0 or li >= n_layers:
            raise ValueError(f"Layer index {li} out of range [0, {n_layers})")
        handles.append(layers[li].register_forward_hook(make_hook(li)))

    return handles


def remove_hooks(handles):
    for h in handles:
        h.remove()


# ---------------------------------------------------------------------------
# Incremental save / load
# ---------------------------------------------------------------------------

def save_layer_data(storage, layer_indices, lang, output_dir,
                    train_indices=None, eval_indices=None):
    """Save accumulated activations for all target layers.

    If train_indices/eval_indices are provided, saves separate train/eval files
    instead of a single file.
    """
    for li in layer_indices:
        if not storage[li]["acts"]:
            continue
        acts = torch.stack(storage[li]["acts"])
        labels = torch.tensor(storage[li]["labels"], dtype=torch.long)

        if train_indices is not None and eval_indices is not None:
            for suffix, indices in [("train", train_indices), ("eval", eval_indices)]:
                idx = [i for i in indices if i < len(acts)]
                if not idx:
                    continue
                idx_t = torch.tensor(idx, dtype=torch.long)
                path = os.path.join(output_dir, f"layer{li}_{lang}_{suffix}.pt")
                torch.save({"activations": acts[idx_t], "labels": labels[idx_t]}, path)
        else:
            path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
            torch.save({"activations": acts, "labels": labels}, path)


def load_existing_progress(layer_indices, lang, output_dir):
    """Load previously saved data to support resumption after interruption."""
    storage = {li: {"acts": [], "labels": []} for li in layer_indices}
    n_existing = 0
    for li in layer_indices:
        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
        if os.path.exists(path):
            data = torch.load(path, weights_only=True)
            storage[li]["acts"] = list(data["activations"].unbind(0))
            storage[li]["labels"] = data["labels"].tolist()
            n_existing = max(n_existing, len(storage[li]["labels"]))
    return storage, n_existing


# ---------------------------------------------------------------------------
# Main extraction loop
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    layer_indices = sorted(int(x) for x in args.layers.split(","))
    os.makedirs(args.output_dir, exist_ok=True)

    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
    print(f"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}")

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = load_model(args.model, dtype, args.quantization)

    n_model_layers = model.config.num_hidden_layers
    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
    for li in layer_indices:
        if li < 0 or li >= n_model_layers:
            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")

    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")

    # Split indices: computed once on the first language, reused for all
    split_train_indices = None
    split_eval_indices = None

    # Register hooks once — they persist across forward calls
    captured = {}
    handles = register_activation_hooks(model, layer_indices, captured)

    try:
        for lang_idx, lang in enumerate(args.languages):
            print(f"\n{'='*50}")
            print(f"  Language: {lang}")
            print(f"{'='*50}")

            test_ds = load_mmlu(lang, "test")
            dev_ds = load_mmlu_dev(lang)

            if args.subjects:
                test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
                dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)

            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))

            # Compute split on first language, reuse for all subsequent languages
            if args.split_ratio > 0 and split_train_indices is None:
                from sklearn.model_selection import train_test_split
                subjects = [normalize_row(test_ds[i])["subject"] for i in range(n)]
                split_train_indices, split_eval_indices = train_test_split(
                    list(range(n)), train_size=args.split_ratio,
                    stratify=subjects, random_state=args.split_seed,
                )
                split_path = os.path.join(args.output_dir, "split_indices.pt")
                torch.save({
                    "train": split_train_indices, "eval": split_eval_indices,
                    "split_ratio": args.split_ratio, "seed": args.split_seed,
                    "n_total": n, "first_lang": lang,
                }, split_path)
                print(f"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})")

            dev_by_subject: dict[str, list] = {}
            for r in dev_ds:
                dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
            dev_fallback = list(dev_ds)[:args.n_shot]

            # Try to resume from existing partial results
            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)
            if n_existing > 0:
                print(f"  Resuming from sample {n_existing} (found existing data)")

            for i in tqdm(range(n_existing, n), desc=f"[{lang}]", initial=n_existing, total=n):
                row = normalize_row(test_ds[i])
                few_shots = dev_by_subject.get(row["subject"], dev_fallback)
                prompt = build_prompt(row, few_shots, args.n_shot)

                inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                                   max_length=4096).to(model.device)

                with torch.no_grad():
                    # No output_hidden_states — hooks capture what we need
                    out = model(**inputs)

                logits_last = out.logits[0, -1]
                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
                pred = choice_logits.argmax().item()
                correct = int(pred == row["answer"])

                for li in layer_indices:
                    storage[li]["acts"].append(captured[li])
                    storage[li]["labels"].append(correct)

                captured.clear()
                del out, inputs

                if (i + 1) % 100 == 0:
                    torch.cuda.empty_cache()

                # Incremental save
                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:
                    save_layer_data(storage, layer_indices, lang, args.output_dir,
                                    split_train_indices, split_eval_indices)
                    print(f"  [checkpoint] saved at sample {i + 1}")

            # Final save for this language
            save_layer_data(storage, layer_indices, lang, args.output_dir,
                            split_train_indices, split_eval_indices)
            for li in layer_indices:
                n_samples = len(storage[li]["labels"])
                if n_samples > 0:
                    acc = sum(storage[li]["labels"]) / n_samples
                    if split_train_indices is not None:
                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt")
                    else:
                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt")

    finally:
        # Always clean up hooks, even if an exception occurs
        remove_hooks(handles)

    print("\nExtraction complete.")


if __name__ == "__main__":
    main()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "c2b7600e-ecae-4cc4-bbc9-507c5470d81f",
  "tool_use_result": {
    "stdout": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\",\n                   default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\", \"es\", \"fr\", \"de\", \"ru\",\n                            \"tr\", \"bn\", \"ja\", \"pt\", \"vi\", \"te\", \"id\", \"pl\", \"nl\", \"uk\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    p.add_argument(\"--split_ratio\", type=float, default=0.0,\n                   help=\"If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval\")\n    p.add_argument(\"--split_seed\", type=int, default=42,\n                   help=\"Random seed for train/eval split (ensures reproducibility across languages)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef get_final_norm(model):\n    \"\"\"Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).\n\n    Used to apply post-norm on the last layer's hook output, matching the behavior of\n    output_hidden_states=True which returns post-norm activations for the final layer.\n    \"\"\"\n    candidates = [\n        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma\n        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J\n        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX\n    ]\n    for accessor in candidates:\n        try:\n            norm = accessor(model)\n            if norm is not None:\n                return norm\n        except AttributeError:\n            continue\n    return None\n\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n\n    Post-norm on last layer:\n      output_hidden_states returns post-norm activations for the final layer (i.e., after\n      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency\n      with MVP experiments that used output_hidden_states, we apply the final norm to the\n      last layer's hook output. All other layers return pre-norm (direct layer output).\n    \"\"\"\n    layers = get_layer_modules(model)\n    n_layers = len(layers)\n    final_norm = get_final_norm(model)\n    max_target_layer = max(layer_indices)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            h = output[0] if isinstance(output, tuple) else output\n            h = h[0, -1]\n            # Apply final norm on the last transformer layer to match output_hidden_states behavior\n            if layer_idx == n_layers - 1 and final_norm is not None:\n                with torch.no_grad():\n                    h = final_norm(h.unsqueeze(0)).squeeze(0)\n            captured[layer_idx] = h.detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= n_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_layers})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir,\n                    train_indices=None, eval_indices=None):\n    \"\"\"Save accumulated activations for all target layers.\n\n    If train_indices/eval_indices are provided, saves separate train/eval files\n    instead of a single file.\n    \"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n\n        if train_indices is not None and eval_indices is not None:\n            for suffix, indices in [(\"train\", train_indices), (\"eval\", eval_indices)]:\n                idx = [i for i in indices if i < len(acts)]\n                if not idx:\n                    continue\n                idx_t = torch.tensor(idx, dtype=torch.long)\n                path = os.path.join(output_dir, f\"layer{li}_{lang}_{suffix}.pt\")\n                torch.save({\"activations\": acts[idx_t], \"labels\": labels[idx_t]}, path)\n        else:\n            path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Split indices: computed once on the first language, reused for all\n    split_train_indices = None\n    split_eval_indices = None\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang_idx, lang in enumerate(args.languages):\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            # Compute split on first language, reuse for all subsequent languages\n            if args.split_ratio > 0 and split_train_indices is None:\n                from sklearn.model_selection import train_test_split\n                subjects = [normalize_row(test_ds[i])[\"subject\"] for i in range(n)]\n                split_train_indices, split_eval_indices = train_test_split(\n                    list(range(n)), train_size=args.split_ratio,\n                    stratify=subjects, random_state=args.split_seed,\n                )\n                split_path = os.path.join(args.output_dir, \"split_indices.pt\")\n                torch.save({\n                    \"train\": split_train_indices, \"eval\": split_eval_indices,\n                    \"split_ratio\": args.split_ratio, \"seed\": args.split_seed,\n                    \"n_total\": n, \"first_lang\": lang,\n                }, split_path)\n                print(f\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\")\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir,\n                                    split_train_indices, split_eval_indices)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir,\n                            split_train_indices, split_eval_indices)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    if split_train_indices is not None:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt\")\n                    else:\n                        print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()",
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I need to deploy this to the server using ssh_execute with a heredoc. The file contains special characters like backticks and dollar signs in f-strings, so I should use base64 encoding for safe transfer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "1cb5955a-dc45-4819-a59e-06bbdc9f52b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkD6Djo7483DoJBrH11657",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5396,
      "cache_read_input_tokens": 61120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5396
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

_source line 42_

用 base64 方式安全传输到服务器两个路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "088f74ea-2faa-4719-9dfd-8265ecc48263",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkD6Djo7483DoJBrH11657",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5396,
      "cache_read_input_tokens": 61120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5396
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_0173tqATANzCjNefFBKVSAsx`</summary>

```json
{
  "command": "B64=$(cat /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py | base64 -w0) && echo \"${#B64} chars\"",
  "description": "Get base64 encoded content length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "aa5ba24c-a8b9-4ffa-b739-72f6737b9100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkD6Djo7483DoJBrH11657",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5396,
      "cache_read_input_tokens": 61120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5396
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

_source line 44 · 2026-05-20T22:16:12.451Z_

<details><summary>↩ Tool result · `toolu_0173tqATANzCjNefFBKVSAsx`</summary>

```text
24748 chars
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "7010f287-6907-49d4-9d09-71569c6cb4f9",
  "tool_use_result": {
    "stdout": "24748 chars",
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01FjjBmdWAmwz8bEaVj15M98`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "echo 'IiIiCkV4dHJhY3QgcmVzaWR1YWwtc3RyZWFtIGFjdGl2YXRpb25zIGZyb20gKmxhcmdlKiBMTE1zIChRd2VuMy0yMzVCLUEyMkIsIExsYW1hIDQgU2NvdXQsIGV0Yy4pLgoKRGlmZmVyZW5jZXMgZnJvbSBleHRyYWN0X2FjdGl2YXRpb25zLnB5OgogIC0gVXNlcyByZWdpc3Rlcl9mb3J3YXJkX2hvb2sgaW5zdGVhZCBvZiBvdXRwdXRfaGlkZGVuX3N0YXRlcz1UcnVlLgogICAgUmVhc29uOiBvdXRwdXRfaGlkZGVuX3N0YXRlcyByZXR1cm5zIEFMTCBsYXllcnMnIGhpZGRlbiBzdGF0ZXMgc2ltdWx0YW5lb3VzbHksCiAgICB3aGljaCBpcyBwcm9oaWJpdGl2ZSBmb3IgOTQtbGF5ZXIgbW9kZWxzLiBIb29rcyBjYXB0dXJlIG9ubHkgdGhlIHRhcmdldCBsYXllcnMuCiAgLSBTdXBwb3J0cyBJTlQ0L0lOVDggcXVhbnRpemF0aW9uIHZpYSBiaXRzYW5kYnl0ZXMgKC0tcXVhbnRpemF0aW9uIGludDQvaW50OCkuCiAgLSBJbmNyZW1lbnRhbCBzYXZpbmcgdmlhIC0tc2F2ZV9pbnRlcnZhbCB0byBzdXJ2aXZlIE9PTSBvciBpbnRlcnJ1cHRpb24uCiAgLSBBcmNoaXRlY3R1cmUtYWRhcHRpdmUgbGF5ZXIgYWNjZXNzIChtb2RlbC5tb2RlbC5sYXllcnMgLyBtb2RlbC50cmFuc2Zvcm1lci5oKS4KCk91dHB1dCBmb3JtYXQgaXMgaWRlbnRpY2FsIHRvIGV4dHJhY3RfYWN0aXZhdGlvbnMucHk6CiAgbGF5ZXJ7aX1fe2xhbmd9LnB0ICAtPiAgeyJhY3RpdmF0aW9ucyI6IFRlbnNvcihOLCBoaWRkZW5fZGltKSwgImxhYmVscyI6IFRlbnNvcihOLCl9CgpEZXBlbmRlbmNpZXM6IHRvcmNoLCB0cmFuc2Zvcm1lcnMsIGRhdGFzZXRzLCBiaXRzYW5kYnl0ZXMgKGZvciBxdWFudGl6YXRpb24pLCB0cWRtCgpVc2FnZToKICBweXRob24gZXh0cmFjdF9hY3RpdmF0aW9uc19sYXJnZS5weSBcCiAgICAtLW1vZGVsIFF3ZW4vUXdlbjMtMjM1Qi1BMjJCIFwKICAgIC0tbGFuZ3VhZ2VzIGVuIHpoIGFyIGhpIHN3IGtvIFwKICAgIC0tbGF5ZXJzIDAsOCwxNiwyNCwzMiw0OCw2NCw4MCw5MyBcCiAgICAtLW91dHB1dF9kaXIgLi9hY3RpdmF0aW9ucyBcCiAgICAtLXF1YW50aXphdGlvbiBpbnQ0IFwKICAgIC0tc2F2ZV9pbnRlcnZhbCAyMDAKIiIiCgppbXBvcnQgYXJncGFyc2UKaW1wb3J0IG9zCgppbXBvcnQgdG9yY2gKZnJvbSBkYXRhc2V0cyBpbXBvcnQgbG9hZF9kYXRhc2V0CmZyb20gdHJhbnNmb3JtZXJzIGltcG9ydCBBdXRvTW9kZWxGb3JDYXVzYWxMTSwgQXV0b1Rva2VuaXplcgpmcm9tIHRxZG0gaW1wb3J0IHRxZG0KCgpMRVRURVJTID0gWyJBIiwgIkIiLCAiQyIsICJEIl0KCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKCkKICAgIHAuYWRkX2FyZ3VtZW50KCItLW1vZGVsIiwgcmVxdWlyZWQ9VHJ1ZSwgaGVscD0iSHVnZ2luZ0ZhY2UgbW9kZWwgbmFtZSBvciBwYXRoIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxhbmd1YWdlcyIsIG5hcmdzPSIrIiwKICAgICAgICAgICAgICAgICAgIGRlZmF1bHQ9WyJlbiIsICJ6aCIsICJhciIsICJoaSIsICJzdyIsICJrbyIsICJlcyIsICJmciIsICJkZSIsICJydSIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAidHIiLCAiYm4iLCAiamEiLCAicHQiLCAidmkiLCAidGUiLCAiaWQiLCAicGwiLCAibmwiLCAidWsiXSkKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxheWVycyIsIGRlZmF1bHQ9IjAsNCw4LDEyLDE2LDIwLDI0LDI4LDMxIiwKICAgICAgICAgICAgICAgICAgIGhlbHA9IkNvbW1hLXNlcGFyYXRlZCB0cmFuc2Zvcm1lciBsYXllciBpbmRpY2VzICgwLWluZGV4ZWQpIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW91dHB1dF9kaXIiLCBkZWZhdWx0PSIuL2FjdGl2YXRpb25zIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW5fc2hvdCIsIHR5cGU9aW50LCBkZWZhdWx0PTUpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1tYXhfc2FtcGxlcyIsIHR5cGU9aW50LCBkZWZhdWx0PTAsIGhlbHA9IjAgPSBhbGwgdGVzdCBzYW1wbGVzIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWR0eXBlIiwgZGVmYXVsdD0iYmZsb2F0MTYiLCBjaG9pY2VzPVsiZmxvYXQxNiIsICJiZmxvYXQxNiJdKQogICAgcC5hZGRfYXJndW1lbnQoIi0tc3ViamVjdHMiLCBuYXJncz0iKiIsIGRlZmF1bHQ9Tm9uZSwKICAgICAgICAgICAgICAgICAgIGhlbHA9IlJlc3RyaWN0IHRvIHRoZXNlIE1NTFUgc3ViamVjdHMgKGRlZmF1bHQ6IGFsbCkiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcXVhbnRpemF0aW9uIiwgZGVmYXVsdD0ibm9uZSIsIGNob2ljZXM9WyJub25lIiwgImludDQiLCAiaW50OCJdLAogICAgICAgICAgICAgICAgICAgaGVscD0iUXVhbnRpemF0aW9uOiBub25lIChmdWxsIHByZWNpc2lvbiksIGludDQgKE5GNCA0LWJpdCksIGludDggKExMTS5pbnQ4KSIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1zYXZlX2ludGVydmFsIiwgdHlwZT1pbnQsIGRlZmF1bHQ9NTAwLAogICAgICAgICAgICAgICAgICAgaGVscD0iSW5jcmVtZW50YWxseSBzYXZlIGV2ZXJ5IE4gc2FtcGxlcyAoMCA9IG9ubHkgc2F2ZSBhdCBlbmQpIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLXNwbGl0X3JhdGlvIiwgdHlwZT1mbG9hdCwgZGVmYXVsdD0wLjAsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJJZiA+IDAsIHNwbGl0IHRlc3QgZGF0YSBpbnRvIHRyYWluL2V2YWwuIEUuZy4sIDAuNyA9IDcwJSUgdHJhaW4sIDMwJSUgZXZhbCIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1zcGxpdF9zZWVkIiwgdHlwZT1pbnQsIGRlZmF1bHQ9NDIsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJSYW5kb20gc2VlZCBmb3IgdHJhaW4vZXZhbCBzcGxpdCAoZW5zdXJlcyByZXByb2R1Y2liaWxpdHkgYWNyb3NzIGxhbmd1YWdlcykiKQogICAgcmV0dXJuIHAucGFyc2VfYXJncygpCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBEYXRhIGxvYWRpbmcgKGlkZW50aWNhbCB0byBleHRyYWN0X2FjdGl2YXRpb25zLnB5KQojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGxvYWRfbW1sdShsYW5ndWFnZSwgc3BsaXQ9InRlc3QiKToKICAgICIiIkxvYWQgYW4gTU1MVSBzcGxpdC4gRW5nbGlzaCBmcm9tIGNhaXMvbW1sdSwgb3RoZXJzIGZyb20gR2xvYmFsLU1NTFUuIiIiCiAgICBpZiBsYW5ndWFnZSA9PSAiZW4iOgogICAgICAgIHJldHVybiBsb2FkX2RhdGFzZXQoImNhaXMvbW1sdSIsICJhbGwiLCBzcGxpdD1zcGxpdCkKICAgIHJldHVybiBsb2FkX2RhdGFzZXQoIkNvaGVyZUZvckFJL0dsb2JhbC1NTUxVIiwgbGFuZ3VhZ2UsIHNwbGl0PXNwbGl0KQoKCmRlZiBsb2FkX21tbHVfZGV2KGxhbmd1YWdlKToKICAgICIiIkxvYWQgZmV3LXNob3QgZXhlbXBsYXJzICh0cnkgJ2RldicgZmlyc3QsIHRoZW4gJ3ZhbGlkYXRpb24nKS4iIiIKICAgIGZvciBzcGxpdF9uYW1lIGluIFsiZGV2IiwgInZhbGlkYXRpb24iXToKICAgICAgICB0cnk6CiAgICAgICAgICAgIHJldHVybiBsb2FkX21tbHUobGFuZ3VhZ2UsIHNwbGl0X25hbWUpCiAgICAgICAgZXhjZXB0IChWYWx1ZUVycm9yLCBLZXlFcnJvcik6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICByYWlzZSBSdW50aW1lRXJyb3IoZiJObyBkZXYvdmFsaWRhdGlvbiBzcGxpdCBmb3VuZCBmb3IgJ3tsYW5ndWFnZX0nIikKCgpkZWYgbm9ybWFsaXplX3Jvdyhyb3cpOgogICAgIiIiTm9ybWFsaXplIGEgZGF0YXNldCByb3cgdG8ge3F1ZXN0aW9uLCBjaG9pY2VzLCBhbnN3ZXIoaW50KSwgc3ViamVjdH0uIiIiCiAgICBxdWVzdGlvbiA9IHJvdy5nZXQoInF1ZXN0aW9uIiwgcm93LmdldCgiaW5wdXQiLCAiIikpCgogICAgaWYgImNob2ljZXMiIGluIHJvdyBhbmQgaXNpbnN0YW5jZShyb3dbImNob2ljZXMiXSwgbGlzdCk6CiAgICAgICAgY2hvaWNlcyA9IGxpc3Qocm93WyJjaG9pY2VzIl0pCiAgICBlbHNlOgogICAgICAgIGNob2ljZXMgPSBbcm93LmdldChmIm9wdGlvbl97bC5sb3dlcigpfSIsICIiKSBmb3IgbCBpbiBMRVRURVJTXQoKICAgIGFuc3dlciA9IHJvdy5nZXQoImFuc3dlciIsIHJvdy5nZXQoInRhcmdldCIsIDApKQogICAgaWYgaXNpbnN0YW5jZShhbnN3ZXIsIHN0cik6CiAgICAgICAgYW5zd2VyID0gTEVUVEVSUy5pbmRleChhbnN3ZXIudXBwZXIoKSkgaWYgYW5zd2VyLnVwcGVyKCkgaW4gTEVUVEVSUyBlbHNlIGludChhbnN3ZXIpCgogICAgcmV0dXJuIHsKICAgICAgICAicXVlc3Rpb24iOiBxdWVzdGlvbiwKICAgICAgICAiY2hvaWNlcyI6IGNob2ljZXMsCiAgICAgICAgImFuc3dlciI6IGludChhbnN3ZXIpLAogICAgICAgICJzdWJqZWN0Ijogcm93LmdldCgic3ViamVjdCIsICJ1bmtub3duIiksCiAgICB9CgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBQcm9tcHQgZm9ybWF0dGluZyAoaWRlbnRpY2FsIHRvIGV4dHJhY3RfYWN0aXZhdGlvbnMucHkpCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgX2Zvcm1hdF9xdWVzdGlvbihxdWVzdGlvbiwgY2hvaWNlcyk6CiAgICBwYXJ0cyA9IFtmIntxdWVzdGlvbn1cbiJdCiAgICBmb3IgaSwgYyBpbiBlbnVtZXJhdGUoY2hvaWNlcyk6CiAgICAgICAgcGFydHMuYXBwZW5kKGYie0xFVFRFUlNbaV19LiB7Y31cbiIpCiAgICByZXR1cm4gIiIuam9pbihwYXJ0cykKCgpkZWYgYnVpbGRfcHJvbXB0KHJvdywgZmV3X3Nob3Rfcm93cywgbl9zaG90KToKICAgICIiIkJ1aWxkIGFuIG4tc2hvdCBNTUxVIHByb21wdCBmb3IgKnJvdyogdXNpbmcgKmZld19zaG90X3Jvd3MqIGFzIGV4ZW1wbGFycy4iIiIKICAgIHN1YmplY3RfcHJldHR5ID0gcm93WyJzdWJqZWN0Il0ucmVwbGFjZSgiXyIsICIgIikKICAgIGxpbmVzID0gWwogICAgICAgIGYiVGhlIGZvbGxvd2luZyBhcmUgbXVsdGlwbGUgY2hvaWNlIHF1ZXN0aW9ucyAod2l0aCBhbnN3ZXJzKSBhYm91dCB7c3ViamVjdF9wcmV0dHl9LlxuXG4iCiAgICBdCiAgICBmb3IgZnMgaW4gZmV3X3Nob3Rfcm93c1s6bl9zaG90XToKICAgICAgICBmcyA9IG5vcm1hbGl6ZV9yb3coZnMpIGlmICJjaG9pY2VzIiBub3QgaW4gZnMgb3Igbm90IGlzaW5zdGFuY2UoZnMuZ2V0KCJhbnN3ZXIiKSwgaW50KSBlbHNlIGZzCiAgICAgICAgbGluZXMuYXBwZW5kKF9mb3JtYXRfcXVlc3Rpb24oZnNbInF1ZXN0aW9uIl0sIGZzWyJjaG9pY2VzIl0pKQogICAgICAgIGxpbmVzLmFwcGVuZChmIkFuc3dlcjoge0xFVFRFUlNbZnNbJ2Fuc3dlciddXX1cblxuIikKICAgIGxpbmVzLmFwcGVuZChfZm9ybWF0X3F1ZXN0aW9uKHJvd1sicXVlc3Rpb24iXSwgcm93WyJjaG9pY2VzIl0pKQogICAgbGluZXMuYXBwZW5kKCJBbnN3ZXI6IikKICAgIHJldHVybiAiIi5qb2luKGxpbmVzKQoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgTW9kZWwgbG9hZGluZyB3aXRoIHF1YW50aXphdGlvbiBzdXBwb3J0CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgbG9hZF9tb2RlbChtb2RlbF9uYW1lLCBkdHlwZSwgcXVhbnRpemF0aW9uKToKICAgICIiIkxvYWQgbW9kZWwgd2l0aCBvcHRpb25hbCBJTlQ0L0lOVDggcXVhbnRpemF0aW9uIHZpYSBiaXRzYW5kYnl0ZXMuIiIiCiAgICBrd2FyZ3MgPSBkaWN0KGRldmljZV9tYXA9ImF1dG8iLCB0cnVzdF9yZW1vdGVfY29kZT1UcnVlKQoKICAgIGlmIHF1YW50aXphdGlvbiA9PSAiaW50NCI6CiAgICAgICAgZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEJpdHNBbmRCeXRlc0NvbmZpZwogICAgICAgIGt3YXJnc1sicXVhbnRpemF0aW9uX2NvbmZpZyJdID0gQml0c0FuZEJ5dGVzQ29uZmlnKAogICAgICAgICAgICBsb2FkX2luXzRiaXQ9VHJ1ZSwKICAgICAgICAgICAgYm5iXzRiaXRfY29tcHV0ZV9kdHlwZT10b3JjaC5iZmxvYXQxNiwKICAgICAgICAgICAgYm5iXzRiaXRfcXVhbnRfdHlwZT0ibmY0IiwKICAgICAgICAgICAgYm5iXzRiaXRfdXNlX2RvdWJsZV9xdWFudD1UcnVlLAogICAgICAgICkKICAgIGVsaWYgcXVhbnRpemF0aW9uID09ICJpbnQ4IjoKICAgICAgICBmcm9tIHRyYW5zZm9ybWVycyBpbXBvcnQgQml0c0FuZEJ5dGVzQ29uZmlnCiAgICAgICAga3dhcmdzWyJxdWFudGl6YXRpb25fY29uZmlnIl0gPSBCaXRzQW5kQnl0ZXNDb25maWcobG9hZF9pbl84Yml0PVRydWUpCiAgICBlbHNlOgogICAgICAgIGt3YXJnc1sidG9yY2hfZHR5cGUiXSA9IGR0eXBlCgogICAgbW9kZWwgPSBBdXRvTW9kZWxGb3JDYXVzYWxMTS5mcm9tX3ByZXRyYWluZWQobW9kZWxfbmFtZSwgKiprd2FyZ3MpCiAgICBtb2RlbC5ldmFsKCkKICAgIHJldHVybiBtb2RlbAoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgQXJjaGl0ZWN0dXJlLWFkYXB0aXZlIGxheWVyIGFjY2VzcwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGdldF9sYXllcl9tb2R1bGVzKG1vZGVsKToKICAgICIiIlJldHVybiB0aGUgbm4uTW9kdWxlTGlzdCBvZiB0cmFuc2Zvcm1lciBsYXllcnMsIGFkYXB0aW5nIHRvIG1vZGVsIGFyY2hpdGVjdHVyZS4KCiAgICBUcmllcyBjb21tb24gYXR0cmlidXRlIHBhdGhzIHVzZWQgYnkgZGlmZmVyZW50IG1vZGVsIGZhbWlsaWVzOgogICAgICAtIG1vZGVsLm1vZGVsLmxheWVycyAgICAgIChRd2VuLCBMbGFtYSwgTWlzdHJhbCwgR2VtbWEsIGV0Yy4pCiAgICAgIC0gbW9kZWwudHJhbnNmb3JtZXIuaCAgICAgKEdQVC0yLCBHUFQtSiwgR1BULU5lb1gpCiAgICAgIC0gbW9kZWwuZ3B0X25lb3gubGF5ZXJzICAgKEdQVC1OZW9YIHZhcmlhbnRzKQogICAgIiIiCiAgICBjYW5kaWRhdGVzID0gWwogICAgICAgICgibW9kZWwubW9kZWwubGF5ZXJzIiwgbGFtYmRhIG06IG0ubW9kZWwubGF5ZXJzKSwKICAgICAgICAoIm1vZGVsLnRyYW5zZm9ybWVyLmgiLCBsYW1iZGEgbTogbS50cmFuc2Zvcm1lci5oKSwKICAgICAgICAoIm1vZGVsLmdwdF9uZW94LmxheWVycyIsIGxhbWJkYSBtOiBtLmdwdF9uZW94LmxheWVycyksCiAgICBdCiAgICBmb3IgcGF0aF9uYW1lLCBhY2Nlc3NvciBpbiBjYW5kaWRhdGVzOgogICAgICAgIHRyeToKICAgICAgICAgICAgbGF5ZXJzID0gYWNjZXNzb3IobW9kZWwpCiAgICAgICAgICAgIGlmIGhhc2F0dHIobGF5ZXJzLCAiX19sZW5fXyIpIGFuZCBsZW4obGF5ZXJzKSA+IDA6CiAgICAgICAgICAgICAgICBwcmludChmIiAgTGF5ZXIgYWNjZXNzIHBhdGg6IHtwYXRoX25hbWV9ICAoe2xlbihsYXllcnMpfSBsYXllcnMpIikKICAgICAgICAgICAgICAgIHJldHVybiBsYXllcnMKICAgICAgICBleGNlcHQgQXR0cmlidXRlRXJyb3I6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICByYWlzZSBSdW50aW1lRXJyb3IoCiAgICAgICAgIkNhbm5vdCBsb2NhdGUgdHJhbnNmb3JtZXIgbGF5ZXJzLiAiCiAgICAgICAgIlN1cHBvcnRlZCBwYXRoczogbW9kZWwubW9kZWwubGF5ZXJzLCBtb2RlbC50cmFuc2Zvcm1lci5oLCBtb2RlbC5ncHRfbmVveC5sYXllcnMiCiAgICApCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBGb3J3YXJkIGhvb2sgbWFjaGluZXJ5CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgZ2V0X2ZpbmFsX25vcm0obW9kZWwpOgogICAgIiIiUmV0dXJuIHRoZSBtb2RlbCdzIGZpbmFsIG5vcm1hbGl6YXRpb24gbGF5ZXIgKFJNU05vcm0vTGF5ZXJOb3JtIGFmdGVyIGxhc3QgdHJhbnNmb3JtZXIgYmxvY2spLgoKICAgIFVzZWQgdG8gYXBwbHkgcG9zdC1ub3JtIG9uIHRoZSBsYXN0IGxheWVyJ3MgaG9vayBvdXRwdXQsIG1hdGNoaW5nIHRoZSBiZWhhdmlvciBvZgogICAgb3V0cHV0X2hpZGRlbl9zdGF0ZXM9VHJ1ZSB3aGljaCByZXR1cm5zIHBvc3Qtbm9ybSBhY3RpdmF0aW9ucyBmb3IgdGhlIGZpbmFsIGxheWVyLgogICAgIiIiCiAgICBjYW5kaWRhdGVzID0gWwogICAgICAgIGxhbWJkYSBtOiBtLm1vZGVsLm5vcm0sICAgICAgICMgUXdlbiwgTGxhbWEsIE1pc3RyYWwsIEdlbW1hCiAgICAgICAgbGFtYmRhIG06IG0udHJhbnNmb3JtZXIubG5fZiwgICMgR1BULTIsIEdQVC1KCiAgICAgICAgbGFtYmRhIG06IG0uZ3B0X25lb3guZmluYWxfbGF5ZXJfbm9ybSwgICMgR1BULU5lb1gKICAgIF0KICAgIGZvciBhY2Nlc3NvciBpbiBjYW5kaWRhdGVzOgogICAgICAgIHRyeToKICAgICAgICAgICAgbm9ybSA9IGFjY2Vzc29yKG1vZGVsKQogICAgICAgICAgICBpZiBub3JtIGlzIG5vdCBOb25lOgogICAgICAgICAgICAgICAgcmV0dXJuIG5vcm0KICAgICAgICBleGNlcHQgQXR0cmlidXRlRXJyb3I6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICByZXR1cm4gTm9uZQoKCmRlZiByZWdpc3Rlcl9hY3RpdmF0aW9uX2hvb2tzKG1vZGVsLCBsYXllcl9pbmRpY2VzLCBjYXB0dXJlZCk6CiAgICAiIiJSZWdpc3RlciBmb3J3YXJkIGhvb2tzIG9uIHRhcmdldCBsYXllcnMgdG8gY2FwdHVyZSBsYXN0LXRva2VuIGhpZGRlbiBzdGF0ZXMuCgogICAgV2h5IGhvb2tzIGluc3RlYWQgb2Ygb3V0cHV0X2hpZGRlbl9zdGF0ZXM9VHJ1ZToKICAgICAgb3V0cHV0X2hpZGRlbl9zdGF0ZXMgbWF0ZXJpYWxpemVzIEFMTCBsYXllcnMnIGhpZGRlbiBzdGF0ZXMgaW4gbWVtb3J5IGF0IG9uY2UuCiAgICAgIEZvciBhIDk0LWxheWVyIG1vZGVsIGxpa2UgUXdlbjMtMjM1QiwgdGhpcyBtZWFucyA5NCAqIChiYXRjaCAqIHNlcV9sZW4gKiBoaWRkZW5fZGltKQogICAgICB0ZW5zb3JzIGtlcHQgYWxpdmUg4oCUIGVhc2lseSA1MCsgR0IgZXh0cmEgVlJBTS4gSG9va3Mgb25seSBjYXB0dXJlIHRoZSBzcGVjaWZpYwogICAgICBsYXllcnMgd2UgbmVlZCBhbmQgaW1tZWRpYXRlbHkgZGV0YWNoL21vdmUgdG8gQ1BVLCBrZWVwaW5nIHBlYWsgVlJBTSBtaW5pbWFsLgoKICAgIFBvc3Qtbm9ybSBvbiBsYXN0IGxheWVyOgogICAgICBvdXRwdXRfaGlkZGVuX3N0YXRlcyByZXR1cm5zIHBvc3Qtbm9ybSBhY3RpdmF0aW9ucyBmb3IgdGhlIGZpbmFsIGxheWVyIChpLmUuLCBhZnRlcgogICAgICB0aGUgbW9kZWwncyBmaW5hbCBSTVNOb3JtL0xheWVyTm9ybSkuIFRvIG1hdGNoIHRoaXMgYmVoYXZpb3IgYW5kIGVuc3VyZSBjb25zaXN0ZW5jeQogICAgICB3aXRoIE1WUCBleHBlcmltZW50cyB0aGF0IHVzZWQgb3V0cHV0X2hpZGRlbl9zdGF0ZXMsIHdlIGFwcGx5IHRoZSBmaW5hbCBub3JtIHRvIHRoZQogICAgICBsYXN0IGxheWVyJ3MgaG9vayBvdXRwdXQuIEFsbCBvdGhlciBsYXllcnMgcmV0dXJuIHByZS1ub3JtIChkaXJlY3QgbGF5ZXIgb3V0cHV0KS4KICAgICIiIgogICAgbGF5ZXJzID0gZ2V0X2xheWVyX21vZHVsZXMobW9kZWwpCiAgICBuX2xheWVycyA9IGxlbihsYXllcnMpCiAgICBmaW5hbF9ub3JtID0gZ2V0X2ZpbmFsX25vcm0obW9kZWwpCiAgICBtYXhfdGFyZ2V0X2xheWVyID0gbWF4KGxheWVyX2luZGljZXMpCiAgICBoYW5kbGVzID0gW10KCiAgICBkZWYgbWFrZV9ob29rKGxheWVyX2lkeCk6CiAgICAgICAgZGVmIGhvb2tfZm4obW9kdWxlLCBpbnB1dCwgb3V0cHV0KToKICAgICAgICAgICAgaCA9IG91dHB1dFswXSBpZiBpc2luc3RhbmNlKG91dHB1dCwgdHVwbGUpIGVsc2Ugb3V0cHV0CiAgICAgICAgICAgIGggPSBoWzAsIC0xXQogICAgICAgICAgICAjIEFwcGx5IGZpbmFsIG5vcm0gb24gdGhlIGxhc3QgdHJhbnNmb3JtZXIgbGF5ZXIgdG8gbWF0Y2ggb3V0cHV0X2hpZGRlbl9zdGF0ZXMgYmVoYXZpb3IKICAgICAgICAgICAgaWYgbGF5ZXJfaWR4ID09IG5fbGF5ZXJzIC0gMSBhbmQgZmluYWxfbm9ybSBpcyBub3QgTm9uZToKICAgICAgICAgICAgICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOgogICAgICAgICAgICAgICAgICAgIGggPSBmaW5hbF9ub3JtKGgudW5zcXVlZXplKDApKS5zcXVlZXplKDApCiAgICAgICAgICAgIGNhcHR1cmVkW2xheWVyX2lkeF0gPSBoLmRldGFjaCgpLmNwdSgpLmZsb2F0KCkKICAgICAgICByZXR1cm4gaG9va19mbgoKICAgIGZvciBsaSBpbiBsYXllcl9pbmRpY2VzOgogICAgICAgIGlmIGxpIDwgMCBvciBsaSA+PSBuX2xheWVyczoKICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmIkxheWVyIGluZGV4IHtsaX0gb3V0IG9mIHJhbmdlIFswLCB7bl9sYXllcnN9KSIpCiAgICAgICAgaGFuZGxlcy5hcHBlbmQobGF5ZXJzW2xpXS5yZWdpc3Rlcl9mb3J3YXJkX2hvb2sobWFrZV9ob29rKGxpKSkpCgogICAgcmV0dXJuIGhhbmRsZXMKCgpkZWYgcmVtb3ZlX2hvb2tzKGhhbmRsZXMpOgogICAgZm9yIGggaW4gaGFuZGxlczoKICAgICAgICBoLnJlbW92ZSgpCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBJbmNyZW1lbnRhbCBzYXZlIC8gbG9hZAojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIHNhdmVfbGF5ZXJfZGF0YShzdG9yYWdlLCBsYXllcl9pbmRpY2VzLCBsYW5nLCBvdXRwdXRfZGlyLAogICAgICAgICAgICAgICAgICAgIHRyYWluX2luZGljZXM9Tm9uZSwgZXZhbF9pbmRpY2VzPU5vbmUpOgogICAgIiIiU2F2ZSBhY2N1bXVsYXRlZCBhY3RpdmF0aW9ucyBmb3IgYWxsIHRhcmdldCBsYXllcnMuCgogICAgSWYgdHJhaW5faW5kaWNlcy9ldmFsX2luZGljZXMgYXJlIHByb3ZpZGVkLCBzYXZlcyBzZXBhcmF0ZSB0cmFpbi9ldmFsIGZpbGVzCiAgICBpbnN0ZWFkIG9mIGEgc2luZ2xlIGZpbGUuCiAgICAiIiIKICAgIGZvciBsaSBpbiBsYXllcl9pbmRpY2VzOgogICAgICAgIGlmIG5vdCBzdG9yYWdlW2xpXVsiYWN0cyJdOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGFjdHMgPSB0b3JjaC5zdGFjayhzdG9yYWdlW2xpXVsiYWN0cyJdKQogICAgICAgIGxhYmVscyA9IHRvcmNoLnRlbnNvcihzdG9yYWdlW2xpXVsibGFiZWxzIl0sIGR0eXBlPXRvcmNoLmxvbmcpCgogICAgICAgIGlmIHRyYWluX2luZGljZXMgaXMgbm90IE5vbmUgYW5kIGV2YWxfaW5kaWNlcyBpcyBub3QgTm9uZToKICAgICAgICAgICAgZm9yIHN1ZmZpeCwgaW5kaWNlcyBpbiBbKCJ0cmFpbiIsIHRyYWluX2luZGljZXMpLCAoImV2YWwiLCBldmFsX2luZGljZXMpXToKICAgICAgICAgICAgICAgIGlkeCA9IFtpIGZvciBpIGluIGluZGljZXMgaWYgaSA8IGxlbihhY3RzKV0KICAgICAgICAgICAgICAgIGlmIG5vdCBpZHg6CiAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgIGlkeF90ID0gdG9yY2gudGVuc29yKGlkeCwgZHR5cGU9dG9yY2gubG9uZykKICAgICAgICAgICAgICAgIHBhdGggPSBvcy5wYXRoLmpvaW4ob3V0cHV0X2RpciwgZiJsYXllcntsaX1fe2xhbmd9X3tzdWZmaXh9LnB0IikKICAgICAgICAgICAgICAgIHRvcmNoLnNhdmUoeyJhY3RpdmF0aW9ucyI6IGFjdHNbaWR4X3RdLCAibGFiZWxzIjogbGFiZWxzW2lkeF90XX0sIHBhdGgpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCBmImxheWVye2xpfV97bGFuZ30ucHQiKQogICAgICAgICAgICB0b3JjaC5zYXZlKHsiYWN0aXZhdGlvbnMiOiBhY3RzLCAibGFiZWxzIjogbGFiZWxzfSwgcGF0aCkKCgpkZWYgbG9hZF9leGlzdGluZ19wcm9ncmVzcyhsYXllcl9pbmRpY2VzLCBsYW5nLCBvdXRwdXRfZGlyKToKICAgICIiIkxvYWQgcHJldmlvdXNseSBzYXZlZCBkYXRhIHRvIHN1cHBvcnQgcmVzdW1wdGlvbiBhZnRlciBpbnRlcnJ1cHRpb24uIiIiCiAgICBzdG9yYWdlID0ge2xpOiB7ImFjdHMiOiBbXSwgImxhYmVscyI6IFtdfSBmb3IgbGkgaW4gbGF5ZXJfaW5kaWNlc30KICAgIG5fZXhpc3RpbmcgPSAwCiAgICBmb3IgbGkgaW4gbGF5ZXJfaW5kaWNlczoKICAgICAgICBwYXRoID0gb3MucGF0aC5qb2luKG91dHB1dF9kaXIsIGYibGF5ZXJ7bGl9X3tsYW5nfS5wdCIpCiAgICAgICAgaWYgb3MucGF0aC5leGlzdHMocGF0aCk6CiAgICAgICAgICAgIGRhdGEgPSB0b3JjaC5sb2FkKHBhdGgsIHdlaWdodHNfb25seT1UcnVlKQogICAgICAgICAgICBzdG9yYWdlW2xpXVsiYWN0cyJdID0gbGlzdChkYXRhWyJhY3RpdmF0aW9ucyJdLnVuYmluZCgwKSkKICAgICAgICAgICAgc3RvcmFnZVtsaV1bImxhYmVscyJdID0gZGF0YVsibGFiZWxzIl0udG9saXN0KCkKICAgICAgICAgICAgbl9leGlzdGluZyA9IG1heChuX2V4aXN0aW5nLCBsZW4oc3RvcmFnZVtsaV1bImxhYmVscyJdKSkKICAgIHJldHVybiBzdG9yYWdlLCBuX2V4aXN0aW5nCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyBNYWluIGV4dHJhY3Rpb24gbG9vcAojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIG1haW4oKToKICAgIGFyZ3MgPSBwYXJzZV9hcmdzKCkKICAgIGxheWVyX2luZGljZXMgPSBzb3J0ZWQoaW50KHgpIGZvciB4IGluIGFyZ3MubGF5ZXJzLnNwbGl0KCIsIikpCiAgICBvcy5tYWtlZGlycyhhcmdzLm91dHB1dF9kaXIsIGV4aXN0X29rPVRydWUpCgogICAgZHR5cGUgPSB0b3JjaC5iZmxvYXQxNiBpZiBhcmdzLmR0eXBlID09ICJiZmxvYXQxNiIgZWxzZSB0b3JjaC5mbG9hdDE2CiAgICBwcmludChmIkxvYWRpbmcgbW9kZWw6IHthcmdzLm1vZGVsfSAgZHR5cGU9e2FyZ3MuZHR5cGV9ICBxdWFudGl6YXRpb249e2FyZ3MucXVhbnRpemF0aW9ufSIpCgogICAgdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoYXJncy5tb2RlbCwgdHJ1c3RfcmVtb3RlX2NvZGU9VHJ1ZSkKICAgIGlmIHRva2VuaXplci5wYWRfdG9rZW4gaXMgTm9uZToKICAgICAgICB0b2tlbml6ZXIucGFkX3Rva2VuID0gdG9rZW5pemVyLmVvc190b2tlbgoKICAgIG1vZGVsID0gbG9hZF9tb2RlbChhcmdzLm1vZGVsLCBkdHlwZSwgYXJncy5xdWFudGl6YXRpb24pCgogICAgbl9tb2RlbF9sYXllcnMgPSBtb2RlbC5jb25maWcubnVtX2hpZGRlbl9sYXllcnMKICAgIHByaW50KGYiTW9kZWwgaGFzIHtuX21vZGVsX2xheWVyc30gdHJhbnNmb3JtZXIgbGF5ZXJzOyBleHRyYWN0aW5nOiB7bGF5ZXJfaW5kaWNlc30iKQogICAgZm9yIGxpIGluIGxheWVyX2luZGljZXM6CiAgICAgICAgaWYgbGkgPCAwIG9yIGxpID49IG5fbW9kZWxfbGF5ZXJzOgogICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGYiTGF5ZXIgaW5kZXgge2xpfSBvdXQgb2YgcmFuZ2UgWzAsIHtuX21vZGVsX2xheWVyc30pIikKCiAgICBhbnN3ZXJfdG9rZW5faWRzID0gW3Rva2VuaXplci5lbmNvZGUobCwgYWRkX3NwZWNpYWxfdG9rZW5zPUZhbHNlKVswXSBmb3IgbCBpbiBMRVRURVJTXQogICAgcHJpbnQoZiJBbnN3ZXIgdG9rZW4gSURzOiB7IHtsOiB0aWQgZm9yIGwsIHRpZCBpbiB6aXAoTEVUVEVSUywgYW5zd2VyX3Rva2VuX2lkcyl9IH0iKQoKICAgICMgU3BsaXQgaW5kaWNlczogY29tcHV0ZWQgb25jZSBvbiB0aGUgZmlyc3QgbGFuZ3VhZ2UsIHJldXNlZCBmb3IgYWxsCiAgICBzcGxpdF90cmFpbl9pbmRpY2VzID0gTm9uZQogICAgc3BsaXRfZXZhbF9pbmRpY2VzID0gTm9uZQoKICAgICMgUmVnaXN0ZXIgaG9va3Mgb25jZSDigJQgdGhleSBwZXJzaXN0IGFjcm9zcyBmb3J3YXJkIGNhbGxzCiAgICBjYXB0dXJlZCA9IHt9CiAgICBoYW5kbGVzID0gcmVnaXN0ZXJfYWN0aXZhdGlvbl9ob29rcyhtb2RlbCwgbGF5ZXJfaW5kaWNlcywgY2FwdHVyZWQpCgogICAgdHJ5OgogICAgICAgIGZvciBsYW5nX2lkeCwgbGFuZyBpbiBlbnVtZXJhdGUoYXJncy5sYW5ndWFnZXMpOgogICAgICAgICAgICBwcmludChmIlxueyc9Jyo1MH0iKQogICAgICAgICAgICBwcmludChmIiAgTGFuZ3VhZ2U6IHtsYW5nfSIpCiAgICAgICAgICAgIHByaW50KGYieyc9Jyo1MH0iKQoKICAgICAgICAgICAgdGVzdF9kcyA9IGxvYWRfbW1sdShsYW5nLCAidGVzdCIpCiAgICAgICAgICAgIGRldl9kcyA9IGxvYWRfbW1sdV9kZXYobGFuZykKCiAgICAgICAgICAgIGlmIGFyZ3Muc3ViamVjdHM6CiAgICAgICAgICAgICAgICB0ZXN0X2RzID0gdGVzdF9kcy5maWx0ZXIobGFtYmRhIHg6IHguZ2V0KCJzdWJqZWN0IikgaW4gYXJncy5zdWJqZWN0cykKICAgICAgICAgICAgICAgIGRldl9kcyA9IGRldl9kcy5maWx0ZXIobGFtYmRhIHg6IHguZ2V0KCJzdWJqZWN0IikgaW4gYXJncy5zdWJqZWN0cykKCiAgICAgICAgICAgIG4gPSBsZW4odGVzdF9kcykgaWYgYXJncy5tYXhfc2FtcGxlcyA8PSAwIGVsc2UgbWluKGFyZ3MubWF4X3NhbXBsZXMsIGxlbih0ZXN0X2RzKSkKCiAgICAgICAgICAgICMgQ29tcHV0ZSBzcGxpdCBvbiBmaXJzdCBsYW5ndWFnZSwgcmV1c2UgZm9yIGFsbCBzdWJzZXF1ZW50IGxhbmd1YWdlcwogICAgICAgICAgICBpZiBhcmdzLnNwbGl0X3JhdGlvID4gMCBhbmQgc3BsaXRfdHJhaW5faW5kaWNlcyBpcyBOb25lOgogICAgICAgICAgICAgICAgZnJvbSBza2xlYXJuLm1vZGVsX3NlbGVjdGlvbiBpbXBvcnQgdHJhaW5fdGVzdF9zcGxpdAogICAgICAgICAgICAgICAgc3ViamVjdHMgPSBbbm9ybWFsaXplX3Jvdyh0ZXN0X2RzW2ldKVsic3ViamVjdCJdIGZvciBpIGluIHJhbmdlKG4pXQogICAgICAgICAgICAgICAgc3BsaXRfdHJhaW5faW5kaWNlcywgc3BsaXRfZXZhbF9pbmRpY2VzID0gdHJhaW5fdGVzdF9zcGxpdCgKICAgICAgICAgICAgICAgICAgICBsaXN0KHJhbmdlKG4pKSwgdHJhaW5fc2l6ZT1hcmdzLnNwbGl0X3JhdGlvLAogICAgICAgICAgICAgICAgICAgIHN0cmF0aWZ5PXN1YmplY3RzLCByYW5kb21fc3RhdGU9YXJncy5zcGxpdF9zZWVkLAogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgc3BsaXRfcGF0aCA9IG9zLnBhdGguam9pbihhcmdzLm91dHB1dF9kaXIsICJzcGxpdF9pbmRpY2VzLnB0IikKICAgICAgICAgICAgICAgIHRvcmNoLnNhdmUoewogICAgICAgICAgICAgICAgICAgICJ0cmFpbiI6IHNwbGl0X3RyYWluX2luZGljZXMsICJldmFsIjogc3BsaXRfZXZhbF9pbmRpY2VzLAogICAgICAgICAgICAgICAgICAgICJzcGxpdF9yYXRpbyI6IGFyZ3Muc3BsaXRfcmF0aW8sICJzZWVkIjogYXJncy5zcGxpdF9zZWVkLAogICAgICAgICAgICAgICAgICAgICJuX3RvdGFsIjogbiwgImZpcnN0X2xhbmciOiBsYW5nLAogICAgICAgICAgICAgICAgfSwgc3BsaXRfcGF0aCkKICAgICAgICAgICAgICAgIHByaW50KGYiICBTcGxpdDoge2xlbihzcGxpdF90cmFpbl9pbmRpY2VzKX0gdHJhaW4gKyB7bGVuKHNwbGl0X2V2YWxfaW5kaWNlcyl9IGV2YWwgIChzYXZlZCB0byB7c3BsaXRfcGF0aH0pIikKCiAgICAgICAgICAgIGRldl9ieV9zdWJqZWN0OiBkaWN0W3N0ciwgbGlzdF0gPSB7fQogICAgICAgICAgICBmb3IgciBpbiBkZXZfZHM6CiAgICAgICAgICAgICAgICBkZXZfYnlfc3ViamVjdC5zZXRkZWZhdWx0KHIuZ2V0KCJzdWJqZWN0IiwgInVua25vd24iKSwgW10pLmFwcGVuZChyKQogICAgICAgICAgICBkZXZfZmFsbGJhY2sgPSBsaXN0KGRldl9kcylbOmFyZ3Mubl9zaG90XQoKICAgICAgICAgICAgIyBUcnkgdG8gcmVzdW1lIGZyb20gZXhpc3RpbmcgcGFydGlhbCByZXN1bHRzCiAgICAgICAgICAgIHN0b3JhZ2UsIG5fZXhpc3RpbmcgPSBsb2FkX2V4aXN0aW5nX3Byb2dyZXNzKGxheWVyX2luZGljZXMsIGxhbmcsIGFyZ3Mub3V0cHV0X2RpcikKICAgICAgICAgICAgaWYgbl9leGlzdGluZyA+IDA6CiAgICAgICAgICAgICAgICBwcmludChmIiAgUmVzdW1pbmcgZnJvbSBzYW1wbGUge25fZXhpc3Rpbmd9IChmb3VuZCBleGlzdGluZyBkYXRhKSIpCgogICAgICAgICAgICBmb3IgaSBpbiB0cWRtKHJhbmdlKG5fZXhpc3RpbmcsIG4pLCBkZXNjPWYiW3tsYW5nfV0iLCBpbml0aWFsPW5fZXhpc3RpbmcsIHRvdGFsPW4pOgogICAgICAgICAgICAgICAgcm93ID0gbm9ybWFsaXplX3Jvdyh0ZXN0X2RzW2ldKQogICAgICAgICAgICAgICAgZmV3X3Nob3RzID0gZGV2X2J5X3N1YmplY3QuZ2V0KHJvd1sic3ViamVjdCJdLCBkZXZfZmFsbGJhY2spCiAgICAgICAgICAgICAgICBwcm9tcHQgPSBidWlsZF9wcm9tcHQocm93LCBmZXdfc2hvdHMsIGFyZ3Mubl9zaG90KQoKICAgICAgICAgICAgICAgIGlucHV0cyA9IHRva2VuaXplcihwcm9tcHQsIHJldHVybl90ZW5zb3JzPSJwdCIsIHRydW5jYXRpb249VHJ1ZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhfbGVuZ3RoPTQwOTYpLnRvKG1vZGVsLmRldmljZSkKCiAgICAgICAgICAgICAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKToKICAgICAgICAgICAgICAgICAgICAjIE5vIG91dHB1dF9oaWRkZW5fc3RhdGVzIOKAlCBob29rcyBjYXB0dXJlIHdoYXQgd2UgbmVlZAogICAgICAgICAgICAgICAgICAgIG91dCA9IG1vZGVsKCoqaW5wdXRzKQoKICAgICAgICAgICAgICAgIGxvZ2l0c19sYXN0ID0gb3V0LmxvZ2l0c1swLCAtMV0KICAgICAgICAgICAgICAgIGNob2ljZV9sb2dpdHMgPSB0b3JjaC50ZW5zb3IoW2xvZ2l0c19sYXN0W3RpZF0uaXRlbSgpIGZvciB0aWQgaW4gYW5zd2VyX3Rva2VuX2lkc10pCiAgICAgICAgICAgICAgICBwcmVkID0gY2hvaWNlX2xvZ2l0cy5hcmdtYXgoKS5pdGVtKCkKICAgICAgICAgICAgICAgIGNvcnJlY3QgPSBpbnQocHJlZCA9PSByb3dbImFuc3dlciJdKQoKICAgICAgICAgICAgICAgIGZvciBsaSBpbiBsYXllcl9pbmRpY2VzOgogICAgICAgICAgICAgICAgICAgIHN0b3JhZ2VbbGldWyJhY3RzIl0uYXBwZW5kKGNhcHR1cmVkW2xpXSkKICAgICAgICAgICAgICAgICAgICBzdG9yYWdlW2xpXVsibGFiZWxzIl0uYXBwZW5kKGNvcnJlY3QpCgogICAgICAgICAgICAgICAgY2FwdHVyZWQuY2xlYXIoKQogICAgICAgICAgICAgICAgZGVsIG91dCwgaW5wdXRzCgogICAgICAgICAgICAgICAgaWYgKGkgKyAxKSAlIDEwMCA9PSAwOgogICAgICAgICAgICAgICAgICAgIHRvcmNoLmN1ZGEuZW1wdHlfY2FjaGUoKQoKICAgICAgICAgICAgICAgICMgSW5jcmVtZW50YWwgc2F2ZQogICAgICAgICAgICAgICAgaWYgYXJncy5zYXZlX2ludGVydmFsID4gMCBhbmQgKGkgKyAxKSAlIGFyZ3Muc2F2ZV9pbnRlcnZhbCA9PSAwOgogICAgICAgICAgICAgICAgICAgIHNhdmVfbGF5ZXJfZGF0YShzdG9yYWdlLCBsYXllcl9pbmRpY2VzLCBsYW5nLCBhcmdzLm91dHB1dF9kaXIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNwbGl0X3RyYWluX2luZGljZXMsIHNwbGl0X2V2YWxfaW5kaWNlcykKICAgICAgICAgICAgICAgICAgICBwcmludChmIiAgW2NoZWNrcG9pbnRdIHNhdmVkIGF0IHNhbXBsZSB7aSArIDF9IikKCiAgICAgICAgICAgICMgRmluYWwgc2F2ZSBmb3IgdGhpcyBsYW5ndWFnZQogICAgICAgICAgICBzYXZlX2xheWVyX2RhdGEoc3RvcmFnZSwgbGF5ZXJfaW5kaWNlcywgbGFuZywgYXJncy5vdXRwdXRfZGlyLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgc3BsaXRfdHJhaW5faW5kaWNlcywgc3BsaXRfZXZhbF9pbmRpY2VzKQogICAgICAgICAgICBmb3IgbGkgaW4gbGF5ZXJfaW5kaWNlczoKICAgICAgICAgICAgICAgIG5fc2FtcGxlcyA9IGxlbihzdG9yYWdlW2xpXVsibGFiZWxzIl0pCiAgICAgICAgICAgICAgICBpZiBuX3NhbXBsZXMgPiAwOgogICAgICAgICAgICAgICAgICAgIGFjYyA9IHN1bShzdG9yYWdlW2xpXVsibGFiZWxzIl0pIC8gbl9zYW1wbGVzCiAgICAgICAgICAgICAgICAgICAgaWYgc3BsaXRfdHJhaW5faW5kaWNlcyBpcyBub3QgTm9uZToKICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiIgIExheWVyIHtsaTo+MmR9OiBOPXtuX3NhbXBsZXM6PjVkfSAgbW9kZWxfYWNjPXthY2M6LjNmfSAgLT4gbGF5ZXJ7bGl9X3tsYW5nfV97e3RyYWluLGV2YWx9fS5wdCIpCiAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZiIgIExheWVyIHtsaTo+MmR9OiBOPXtuX3NhbXBsZXM6PjVkfSAgbW9kZWxfYWNjPXthY2M6LjNmfSAgLT4gbGF5ZXJ7bGl9X3tsYW5nfS5wdCIpCgogICAgZmluYWxseToKICAgICAgICAjIEFsd2F5cyBjbGVhbiB1cCBob29rcywgZXZlbiBpZiBhbiBleGNlcHRpb24gb2NjdXJzCiAgICAgICAgcmVtb3ZlX2hvb2tzKGhhbmRsZXMpCgogICAgcHJpbnQoIlxuRXh0cmFjdGlvbiBjb21wbGV0ZS4iKQoKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK' | base64 -d > /root/xling_calib_direction/code/extract_activations_large.py && cp /root/xling_calib_direction/code/extract_activations_large.py /root/xling_calib_direction/extract_activations_large.py && echo \"DEPLOYED OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "e52d59fd-75fe-476b-8975-c65e93429664",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198Pwp1eod1k84p9VR34MS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 66516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 46 · 2026-05-20T22:23:34.459Z_

<details><summary>↩ Tool result · `toolu_01FjjBmdWAmwz8bEaVj15M98`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DEPLOYED OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "e85e27bb-7143-455a-aa53-6f8dd60d97e6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DEPLOYED OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DEPLOYED OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

验证部署。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "06be293c-0c09-43c4-bc58-2a9d3e9849b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iyNjQErGJ5tKEQfRFkH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20515,
      "cache_read_input_tokens": 66750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20515
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TbsYYCcSpScfGFfboK3DQ6`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "grep -n \"split_ratio\\|split_seed\\|train_indices\\|eval_indices\" /root/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "36a9d4a0-f8e3-4f62-96e5-cad339a7025b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018iyNjQErGJ5tKEQfRFkH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20515,
      "cache_read_input_tokens": 66750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20515
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

_source line 49 · 2026-05-20T22:23:40.144Z_

<details><summary>↩ Tool result · `toolu_01TbsYYCcSpScfGFfboK3DQ6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "f40c66bf-c205-4e71-8ae1-038065a1eac7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0164xk2VT1KrC351CiB2krCL`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "grep -n \"split_ratio\\|split_seed\\|train_indices\\|eval_indices\" /root/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "1a1409c1-aeec-4eec-8abf-1cf37878258a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DG7LC3rYDfFLDGjYHnNKHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 87265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 69,
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

_source line 51 · 2026-05-20T22:23:43.457Z_

<details><summary>↩ Tool result · `toolu_0164xk2VT1KrC351CiB2krCL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "8152dca5-a1f7-4744-9ef0-d0b05e1cf7cc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014BFh5hETxXtrdUiP8upr9h`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "grep -n -E \"split_ratio|split_seed|train_indices|eval_indices\" /root/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "62de62cc-e098-459b-9ff2-a6cb0662b7d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yvCFtVqfNzUtd7WycuKDM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 87509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
      },
      "output_tokens": 69,
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

_source line 53 · 2026-05-20T22:23:58.029Z_

<details><summary>↩ Tool result · `toolu_014BFh5hETxXtrdUiP8upr9h`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "393f08b1-556a-4961-a89a-79e5158dd6bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HvTbW7UtUYdzznJwYgxEqp`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "grep -n -e split_ratio -e split_seed -e train_indices -e eval_indices /root/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "9e460e0d-e4eb-4e1e-acfa-aa21a2cb387b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWC9BrcfnpqgU43AM7k8xd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 87747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 55 · 2026-05-20T22:24:02.204Z_

<details><summary>↩ Tool result · `toolu_01HvTbW7UtUYdzznJwYgxEqp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"57:    p.add_argument(\\\"--split_ratio\\\", type=float, default=0.0,\\n59:    p.add_argument(\\\"--split_seed\\\", type=int, default=42,\\n265:                    train_indices=None, eval_indices=None):\\n268:    If train_indices/eval_indices are provided, saves separate train/eval files\\n277:        if train_indices is not None and eval_indices is not None:\\n278:            for suffix, indices in [(\\\"train\\\", train_indices), (\\\"eval\\\", eval_indices)]:\\n332:    split_train_indices = None\\n333:    split_eval_indices = None\\n355:            if args.split_ratio > 0 and split_train_indices is None:\\n358:                split_train_indices, split_eval_indices = train_test_split(\\n359:                    list(range(n)), train_size=args.split_ratio,\\n360:                    stratify=subjects, random_state=args.split_seed,\\n364:                    \\\"train\\\": split_train_indices, \\\"eval\\\": split_eval_indices,\\n365:                    \\\"split_ratio\\\": args.split_ratio, \\\"seed\\\": args.split_seed,\\n368:                print(f\\\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\\\")\\n410:                                    split_train_indices, split_eval_indices)\\n415:                            split_train_indices, split_eval_indices)\\n420:                    if split_train_indices is not None:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "83bd270d-29a2-4127-92e4-29eae1b56ed4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"57:    p.add_argument(\\\\\\\"--split_ratio\\\\\\\", type=float, default=0.0,\\\\n59:    p.add_argument(\\\\\\\"--split_seed\\\\\\\", type=int, default=42,\\\\n265:                    train_indices=None, eval_indices=None):\\\\n268:    If train_indices/eval_indices are provided, saves separate train/eval files\\\\n277:        if train_indices is not None and eval_indices is not None:\\\\n278:            for suffix, indices in [(\\\\\\\"train\\\\\\\", train_indices), (\\\\\\\"eval\\\\\\\", eval_indices)]:\\\\n332:    split_train_indices = None\\\\n333:    split_eval_indices = None\\\\n355:            if args.split_ratio > 0 and split_train_indices is None:\\\\n358:                split_train_indices, split_eval_indices = train_test_split(\\\\n359:                    list(range(n)), train_size=args.split_ratio,\\\\n360:                    stratify=subjects, random_state=args.split_seed,\\\\n364:                    \\\\\\\"train\\\\\\\": split_train_indices, \\\\\\\"eval\\\\\\\": split_eval_indices,\\\\n365:                    \\\\\\\"split_ratio\\\\\\\": args.split_ratio, \\\\\\\"seed\\\\\\\": args.split_seed,\\\\n368:                print(f\\\\\\\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\\\\\\\")\\\\n410:                                    split_train_indices, split_eval_indices)\\\\n415:                            split_train_indices, split_eval_indices)\\\\n420:                    if split_train_indices is not None:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"57:    p.add_argument(\\\"--split_ratio\\\", type=float, default=0.0,\\n59:    p.add_argument(\\\"--split_seed\\\", type=int, default=42,\\n265:                    train_indices=None, eval_indices=None):\\n268:    If train_indices/eval_indices are provided, saves separate train/eval files\\n277:        if train_indices is not None and eval_indices is not None:\\n278:            for suffix, indices in [(\\\"train\\\", train_indices), (\\\"eval\\\", eval_indices)]:\\n332:    split_train_indices = None\\n333:    split_eval_indices = None\\n355:            if args.split_ratio > 0 and split_train_indices is None:\\n358:                split_train_indices, split_eval_indices = train_test_split(\\n359:                    list(range(n)), train_size=args.split_ratio,\\n360:                    stratify=subjects, random_state=args.split_seed,\\n364:                    \\\"train\\\": split_train_indices, \\\"eval\\\": split_eval_indices,\\n365:                    \\\"split_ratio\\\": args.split_ratio, \\\"seed\\\": args.split_seed,\\n368:                print(f\\\"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})\\\")\\n410:                                    split_train_indices, split_eval_indices)\\n415:                            split_train_indices, split_eval_indices)\\n420:                    if split_train_indices is not None:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01ParieLfXgWguCf4tAPYFKV`</summary>

```json
{
  "server": "westd-13176",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/xling_calib_direction/code/extract_activations_large.py --help 2>&1 | grep -A1 split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "4634120f-8e32-4ea5-8382-e6ca9dea8ffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P39RkxBXBBGHBkz7m2axxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 87984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 642
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

_source line 57 · 2026-05-20T22:24:10.830Z_

<details><summary>↩ Tool result · `toolu_01ParieLfXgWguCf4tAPYFKV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"                                    [--split_ratio SPLIT_RATIO]\\n                                    [--split_seed SPLIT_SEED]\\n\\n--\\n  --split_ratio SPLIT_RATIO\\n                        If > 0, split test data into train/eval. E.g., 0.7 =\\n                        70% train, 30% eval\\n  --split_seed SPLIT_SEED\\n                        Random seed for train/eval split (ensures\\n                        reproducibility across languages)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.73}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "3be67b5f-2910-4eee-8d76-a9d9f60105ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"                                    [--split_ratio SPLIT_RATIO]\\\\n                                    [--split_seed SPLIT_SEED]\\\\n\\\\n--\\\\n  --split_ratio SPLIT_RATIO\\\\n                        If > 0, split test data into train/eval. E.g., 0.7 =\\\\n                        70% train, 30% eval\\\\n  --split_seed SPLIT_SEED\\\\n                        Random seed for train/eval split (ensures\\\\n                        reproducibility across languages)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.73}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"                                    [--split_ratio SPLIT_RATIO]\\n                                    [--split_seed SPLIT_SEED]\\n\\n--\\n  --split_ratio SPLIT_RATIO\\n                        If > 0, split test data into train/eval. E.g., 0.7 =\\n                        70% train, 30% eval\\n  --split_seed SPLIT_SEED\\n                        Random seed for train/eval split (ensures\\n                        reproducibility across languages)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.73}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

两项任务完成。

### 任务 A: 代码修改

修改的文件：`extract_activations_large.py`

| 行号 | 修改内容 |
|------|----------|
| 42-44 | `--languages` 默认值扩展为 20 语言 |
| 57-60 | 新增 `--split_ratio` 和 `--split_seed` 参数 |
| 264-287 | `save_layer_data()` 增加 `train_indices`/`eval_indices` 参数，支持分别保存 train/eval 文件 |
| 331-333 | `main()` 中初始化 `split_train_indices`/`split_eval_indices = None` |
| 340 | 循环改为 `enumerate(args.languages)` |
| 354-368 | 第一个语言时基于 subject 做 stratified split，保存 `split_indices.pt`，后续语言复用同一组 indices |
| 409-410, 414-415 | `save_layer_data` 调用传入 split indices |
| 420-422 | 打印输出适配 train/eval 文件名 |

关键设计：split 在第一个语言时计算一次，所有语言复用相同 indices（因为 GlobalMMLU test[i] 是 parallel translation），确保跨语言一致性。`split_ratio=0` 时行为完全不变。

### 任务 B: 服务器部署确认

grep 输出确认 `split_ratio`/`split_seed`/`train_indices`/`eval_indices` 均存在于服务器文件中（20 处匹配）。

`--help` 输出：
```
--split_ratio SPLIT_RATIO
                    If > 0, split test data into train/eval. E.g., 0.7 = 70% train, 30% eval
--split_seed SPLIT_SEED
                    Random seed for train/eval split (ensures reproducibility across languages)
```

文件已部署到两个路径：
- `/root/xling_calib_direction/code/extract_activations_large.py`
- `/root/xling_calib_direction/extract_activations_large.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "uuid": "4fe2b0f4-035c-468e-a621-1ad658c6373f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HWE7mjVoW5VrGimex5Dpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 88626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 456
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

_source line 59_

两项任务完成。

### 任务 A: 代码修改

修改的文件：`extract_activations_large.py`

| 行号 | 修改内容 |
|------|----------|
| 42-44 | `--languages` 默认值扩展为 20 语言 |
| 57-60 | 新增 `--split_ratio` 和 `--split_seed` 参数 |
| 264-287 | `save_layer_data()` 增加 `train_indices`/`eval_indices` 参数，支持分别保存 train/eval 文件 |
| 331-333 | `main()` 中初始化 `split_train_indices`/`split_eval_indices = None` |
| 340 | 循环改为 `enumerate(args.languages)` |
| 354-368 | 第一个语言时基于 subject 做 stratified split，保存 `split_indices.pt`，后续语言复用同一组 indices |
| 409-410, 414-415 | `save_layer_data` 调用传入 split indices |
| 420-422 | 打印输出适配 train/eval 文件名 |

关键设计：split 在第一个语言时计算一次，所有语言复用相同 indices（因为 GlobalMMLU test[i] 是 parallel translation），确保跨语言一致性。`split_ratio=0` 时行为完全不变。

### 任务 B: 服务器部署确认

grep 输出确认 `split_ratio`/`split_seed`/`train_indices`/`eval_indices` 均存在于服务器文件中（20 处匹配）。

`--help` 输出：
```
--split_ratio SPLIT_RATIO
                    If > 0, split test data into train/eval. E.g., 0.7 = 70% train, 30% eval
--split_seed SPLIT_SEED
                    Random seed for train/eval split (ensures reproducibility across languages)
```

文件已部署到两个路径：
- `/root/xling_calib_direction/code/extract_activations_large.py`
- `/root/xling_calib_direction/extract_activations_large.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 640095,
  "duration_api_ms": 634522,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "2ff0f05d-01ab-4ba1-a5ca-be2c354a4fbe",
  "total_cost_usd": 1.66718475,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 77241,
    "cache_read_input_tokens": 1069297,
    "output_tokens": 25907,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 77241,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 613,
        "cache_read_input_tokens": 88626,
        "cache_creation_input_tokens": 456,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 456
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1880,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00198,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 25907,
      "cacheReadInputTokens": 1069297,
      "cacheCreationInputTokens": 77241,
      "webSearchRequests": 0,
      "costUSD": 1.66520475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "64990628-be15-404d-bcc0-b64c0304982b"
}
```

</details>

---
