# code extract activations large

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_code_extract_activations_large_20260520T211034.log`
- **Structured JSON:** [`af22694b790d7a5d23d4.json`](../../sessions/af/af22694b790d7a5d23d4.json)

## Before a recorded user message

15 recorded events

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
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
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
  "uuid": "41e3e452-e153-4dbc-952f-d30d201447be",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
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
    "resetsAt": 1779322200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0e9575c1-c0e6-4a68-999d-7dcb4c447c76",
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Assistant

_source line 4_

Let me start by reading the existing `extract_activations.py` to understand the full code structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "20de35c2-8af1-4537-909e-179ad3869093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFZPavMtdg597Bd7rhoc4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12361
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

<details open><summary>🔧 Tool call — Read · `toolu_012iqU7uWRn41CLzSnw2yNe9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "6d086895-f7aa-4dc9-bacf-2ce97823a199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFZPavMtdg597Bd7rhoc4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12361
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

_source line 6 · 2026-05-20T21:10:43.815Z_

<details><summary>↩ Tool result · `toolu_012iqU7uWRn41CLzSnw2yNe9`</summary>

```text
1	"""
2	Extract residual-stream activations from LLM intermediate layers during MMLU inference.
3	
4	For each (layer, language) pair, saves a .pt file containing:
5	  - activations: Tensor(N, hidden_dim) — last-token hidden state after the transformer layer
6	  - labels: Tensor(N,) — 1 if model answered correctly, 0 otherwise
7	
8	English data: cais/mmlu (all subjects, dev split for few-shot)
9	Non-English:  CohereForAI/Global-MMLU (parallel translated questions)
10	
11	Usage:
12	  python extract_activations.py \
13	    --model Qwen/Qwen2.5-7B-Instruct \
14	    --languages en zh ar hi sw ko \
15	    --layers 0,4,8,12,16,20,24,28,31 \
16	    --output_dir ./activations
17	"""
18	
19	import argparse
20	import os
21	
22	import torch
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	from tqdm import tqdm
26	
27	
28	LETTERS = ["A", "B", "C", "D"]
29	
30	
31	def parse_args():
32	    p = argparse.ArgumentParser()
33	    p.add_argument("--model", required=True, help="HuggingFace model name or path")
34	    p.add_argument("--languages", nargs="+", default=["en", "zh", "ar", "hi", "sw", "ko"])
35	    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
36	                   help="Comma-separated transformer layer indices (0-indexed)")
37	    p.add_argument("--output_dir", default="./activations")
38	    p.add_argument("--n_shot", type=int, default=5)
39	    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
40	    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
41	    p.add_argument("--subjects", nargs="*", default=None,
42	                   help="Restrict to these MMLU subjects (default: all)")
43	    return p.parse_args()
44	
45	
46	# ---------------------------------------------------------------------------
47	# Data loading
48	# ---------------------------------------------------------------------------
49	
50	def load_mmlu(language, split="test"):
51	    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
52	    if language == "en":
53	        return load_dataset("cais/mmlu", "all", split=split)
54	    return load_dataset("CohereForAI/Global-MMLU", language, split=split)
55	
56	
57	def load_mmlu_dev(language):
58	    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
59	    for split_name in ["dev", "validation"]:
60	        try:
61	            return load_mmlu(language, split_name)
62	        except (ValueError, KeyError):
63	            continue
64	    raise RuntimeError(f"No dev/validation split found for '{language}'")
65	
66	
67	def normalize_row(row):
68	    """Normalize a dataset row to {question, choices, answer(int), subject}."""
69	    question = row.get("question", row.get("input", ""))
70	
71	    if "choices" in row and isinstance(row["choices"], list):
72	        choices = list(row["choices"])
73	    else:
74	        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]
75	
76	    answer = row.get("answer", row.get("target", 0))
77	    if isinstance(answer, str):
78	        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)
79	
80	    return {
81	        "question": question,
82	        "choices": choices,
83	        "answer": int(answer),
84	        "subject": row.get("subject", "unknown"),
85	    }
86	
87	
88	# ---------------------------------------------------------------------------
89	# Prompt formatting (standard n-shot MMLU)
90	# ---------------------------------------------------------------------------
91	
92	def _format_question(question, choices):
93	    parts = [f"{question}\n"]
94	    for i, c in enumerate(choices):
95	        parts.append(f"{LETTERS[i]}. {c}\n")
96	    return "".join(parts)
97	
98	
99	def build_prompt(row, few_shot_rows, n_shot):
100	    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
101	    subject_pretty = row["subject"].replace("_", " ")
102	    lines = [
103	        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
104	    ]
105	    for fs in few_shot_rows[:n_shot]:
106	        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
107	        lines.append(_format_question(fs["question"], fs["choices"]))
108	        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
109	    lines.append(_format_question(row["question"], row["choices"]))
110	    lines.append("Answer:")
111	    return "".join(lines)
112	
113	
114	# ---------------------------------------------------------------------------
115	# Main extraction loop
116	# ---------------------------------------------------------------------------
117	
118	def main():
119	    args = parse_args()
120	    layer_indices = sorted(int(x) for x in args.layers.split(","))
121	    os.makedirs(args.output_dir, exist_ok=True)
122	
123	    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
124	    print(f"Loading model: {args.model}  dtype={args.dtype}")
125	
126	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
127	    if tokenizer.pad_token is None:
128	        tokenizer.pad_token = tokenizer.eos_token
129	
130	    model = AutoModelForCausalLM.from_pretrained(
131	        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True,
132	    )
133	    model.eval()
134	
135	    n_model_layers = model.config.num_hidden_layers
136	    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
137	    for li in layer_indices:
138	        if li < 0 or li >= n_model_layers:
139	            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")
140	
141	    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
142	    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")
143	
144	    for lang in args.languages:
145	        print(f"\n{'='*50}")
146	        print(f"  Language: {lang}")
147	        print(f"{'='*50}")
148	
149	        test_ds = load_mmlu(lang, "test")
150	        dev_ds = load_mmlu_dev(lang)
151	
152	        if args.subjects:
153	            test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
154	            dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)
155	
156	        n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))
157	
158	        dev_by_subject: dict[str, list] = {}
159	        for r in dev_ds:
160	            dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
161	        dev_fallback = list(dev_ds)[:args.n_shot]
162	
163	        storage = {li: {"acts": [], "labels": []} for li in layer_indices}
164	
165	        for i in tqdm(range(n), desc=f"[{lang}]"):
166	            row = normalize_row(test_ds[i])
167	            few_shots = dev_by_subject.get(row["subject"], dev_fallback)
168	            prompt = build_prompt(row, few_shots, args.n_shot)
169	
170	            inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
171	                               max_length=4096).to(model.device)
172	
173	            with torch.no_grad():
174	                out = model(**inputs, output_hidden_states=True)
175	
176	            logits_last = out.logits[0, -1]
177	            choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
178	            pred = choice_logits.argmax().item()
179	            correct = int(pred == row["answer"])
180	
181	            # hidden_states[0] = embedding output; hidden_states[k+1] = layer k output
182	            for li in layer_indices:
183	                h = out.hidden_states[li + 1][0, -1].cpu().float()
184	                storage[li]["acts"].append(h)
185	                storage[li]["labels"].append(correct)
186	
187	            del out, inputs
188	            if (i + 1) % 200 == 0:
189	                torch.cuda.empty_cache()
190	
191	        for li in layer_indices:
192	            acts = torch.stack(storage[li]["acts"])
193	            labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
194	            path = os.path.join(args.output_dir, f"layer{li}_{lang}.pt")
195	            torch.save({"activations": acts, "labels": labels}, path)
196	            acc = labels.float().mean().item()
197	            print(f"  Layer {li:>2d}: N={len(labels):>5d}  model_acc={acc:.3f}  -> {path}")
198	
199	    print("\nExtraction complete.")
200	
201	
202	if __name__ == "__main__":
203	    main()
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "fa194187-d46c-4254-b455-939f7d630549",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py",
      "content": "\"\"\"\nExtract residual-stream activations from LLM intermediate layers during MMLU inference.\n\nFor each (layer, language) pair, saves a .pt file containing:\n  - activations: Tensor(N, hidden_dim) — last-token hidden state after the transformer layer\n  - labels: Tensor(N,) — 1 if model answered correctly, 0 otherwise\n\nEnglish data: cais/mmlu (all subjects, dev split for few-shot)\nNon-English:  CohereForAI/Global-MMLU (parallel translated questions)\n\nUsage:\n  python extract_activations.py \\\n    --model Qwen/Qwen2.5-7B-Instruct \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,4,8,12,16,20,24,28,31 \\\n    --output_dir ./activations\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (standard n-shot MMLU)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model, torch_dtype=dtype, device_map=\"auto\", trust_remote_code=True,\n    )\n    model.eval()\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    for lang in args.languages:\n        print(f\"\\n{'='*50}\")\n        print(f\"  Language: {lang}\")\n        print(f\"{'='*50}\")\n\n        test_ds = load_mmlu(lang, \"test\")\n        dev_ds = load_mmlu_dev(lang)\n\n        if args.subjects:\n            test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n            dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n        n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n        dev_by_subject: dict[str, list] = {}\n        for r in dev_ds:\n            dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n        dev_fallback = list(dev_ds)[:args.n_shot]\n\n        storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n\n        for i in tqdm(range(n), desc=f\"[{lang}]\"):\n            row = normalize_row(test_ds[i])\n            few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n            prompt = build_prompt(row, few_shots, args.n_shot)\n\n            inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                               max_length=4096).to(model.device)\n\n            with torch.no_grad():\n                out = model(**inputs, output_hidden_states=True)\n\n            logits_last = out.logits[0, -1]\n            choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n            pred = choice_logits.argmax().item()\n            correct = int(pred == row[\"answer\"])\n\n            # hidden_states[0] = embedding output; hidden_states[k+1] = layer k output\n            for li in layer_indices:\n                h = out.hidden_states[li + 1][0, -1].cpu().float()\n                storage[li][\"acts\"].append(h)\n                storage[li][\"labels\"].append(correct)\n\n            del out, inputs\n            if (i + 1) % 200 == 0:\n                torch.cuda.empty_cache()\n\n        for li in layer_indices:\n            acts = torch.stack(storage[li][\"acts\"])\n            labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n            path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n            acc = labels.float().mean().item()\n            print(f\"  Layer {li:>2d}: N={len(labels):>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
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
Now I have a clear picture of the existing code. Let me create the large model version with the specified changes:

1. `register_forward_hook` instead of `output_hidden_states=True`
2. Quantization support (INT4/INT8 via bitsandbytes)
3. Architecture-adaptive layer access
4. Memory optimizations (save_interval, empty_cache)
5. Compatible output format

Let me write the new file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "ff117448-0b46-4827-ba67-370b7421a343",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2975
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

_source line 8_

Now I'll create the large model version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "0b342e2f-ef00-44c9-860b-a573d128577e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2975
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

_source line 9_

<details open><summary>🔧 Tool call — Write · `toolu_01Mk7y3nvGBqVThR4dVuFw83`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n    \"\"\"\n    layers = get_layer_modules(model)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # Layer output is (hidden_states, ...) tuple or a bare tensor\n            h = output[0] if isinstance(output, tuple) else output\n            # Capture last token, detach and move to CPU immediately to free GPU memory\n            captured[layer_idx] = h[0, -1].detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= len(layers):\n            raise ValueError(f\"Layer index {li} out of range [0, {len(layers)})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "c7160af6-c6eb-49a1-80ae-0cad9bdaa718",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2975
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

_source line 10 · 2026-05-20T21:11:51.330Z_

<details><summary>↩ Tool result · `toolu_01Mk7y3nvGBqVThR4dVuFw83`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "bf252743-3230-4c87-b105-3ceb4f91ab31",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n    \"\"\"\n    layers = get_layer_modules(model)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # Layer output is (hidden_states, ...) tuple or a bare tensor\n            h = output[0] if isinstance(output, tuple) else output\n            # Capture last token, detach and move to CPU immediately to free GPU memory\n            captured[layer_idx] = h[0, -1].detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= len(layers):\n            raise ValueError(f\"Layer index {li} out of range [0, {len(layers)})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 11_

语法检查：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "c878462a-c376-432f-8cf6-e29566746abf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9Np97A5kFQH2EEo88nZWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4438,
      "cache_read_input_tokens": 27177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4438
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01XHijV6gLxe1nbAsQiU4MTb`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py').read()); print('OK')\"",
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
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "be63e0a6-6702-437f-89a7-30135862c561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9Np97A5kFQH2EEo88nZWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4438,
      "cache_read_input_tokens": 27177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4438
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

_source line 13 · 2026-05-20T21:11:55.938Z_

<details><summary>↩ Tool result · `toolu_01XHijV6gLxe1nbAsQiU4MTb`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "9d0d6db0-f76e-4798-a260-32801e7c1149",
  "tool_use_result": {
    "stdout": "OK",
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

文件已创建，语法正确。关键改动：

1. **Hook 替代 output_hidden_states** — 只对目标层注册 `register_forward_hook`，hook 中立即 `.detach().cpu().float()`，推理时不传 `output_hidden_states=True`。hooks 在 `finally` 块中清理。
2. **量化** — `--quantization int4/int8`，通过 `BitsAndBytesConfig` 配置 NF4 双重量化或 LLM.int8。
3. **架构自适应** — `get_layer_modules()` 依次尝试 `model.model.layers` / `model.transformer.h` / `model.gpt_neox.layers`。
4. **增量保存与断点续传** — `--save_interval N` 每 N 条保存一次；启动时自动检测已有 `.pt` 文件并从断点恢复。
5. **输出格式完全兼容** — 同样的 `layer{i}_{lang}.pt`，同样的 `{"activations", "labels"}` 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "uuid": "3c337bd0-cfda-4ba0-9b8f-90d733b619b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYPJapjrrNQKEQcyDLvyXV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 31615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 152
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

_source line 15_

文件已创建，语法正确。关键改动：

1. **Hook 替代 output_hidden_states** — 只对目标层注册 `register_forward_hook`，hook 中立即 `.detach().cpu().float()`，推理时不传 `output_hidden_states=True`。hooks 在 `finally` 块中清理。
2. **量化** — `--quantization int4/int8`，通过 `BitsAndBytesConfig` 配置 NF4 双重量化或 LLM.int8。
3. **架构自适应** — `get_layer_modules()` 依次尝试 `model.model.layers` / `model.transformer.h` / `model.gpt_neox.layers`。
4. **增量保存与断点续传** — `--save_interval N` 每 N 条保存一次；启动时自动检测已有 `.pt` 文件并从断点恢复。
5. **输出格式完全兼容** — 同样的 `layer{i}_{lang}.pt`，同样的 `{"activations", "labels"}` 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88010,
  "duration_api_ms": 88823,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "total_cost_usd": 0.297591,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 19926,
    "cache_read_input_tokens": 94835,
    "output_tokens": 4942,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19926,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 308,
        "cache_read_input_tokens": 31615,
        "cache_creation_input_tokens": 152,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 152
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1966,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0020559999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 4942,
      "cacheReadInputTokens": 94835,
      "cacheCreationInputTokens": 19926,
      "webSearchRequests": 0,
      "costUSD": 0.295535,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c0258030-1adc-477d-bb4c-ab062402437f"
}
```

</details>

---
