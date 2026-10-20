# Research conversation: I need to check 5 compounding sweep scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ for corr

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5d42d85a37f4f722.jsonl`
- **Structured JSON:** [`dca85a0ec8575876ca50.json`](../../sessions/dc/dca85a0ec8575876ca50.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-16T03:14:29.400Z_

I need to check 5 compounding sweep scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/ for correct parameters. For each of these files, find the lines containing: model path, k_values/k_list, profile path, and the attention patching import/function used:

1. run_yi_compounding_sweep.py
2. run_gemma2_compounding_sweep.py
3. run_codellama_compounding_sweep.py
4. run_phi3_compounding_sweep.py
5. run_internlm2_compounding_sweep.py

Report: model path, k values list, profile file path, and attention patching method for each script. Be concise.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "ab7c1ecd-129a-4a25-8a7c-5b1662378c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-16T03:14:30.844Z_

I'll search for these 5 compounding sweep scripts and extract the required parameters for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab7c1ecd-129a-4a25-8a7c-5b1662378c4b",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X5yTsF6F766er7TMXk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29163274-2c1d-4992-ad58-0a872a428aa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Eq43fBpQawQByhz4QY6ax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20779,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20779,
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

_source line 3 · 2026-05-16T03:14:30.985Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N2HBkUa89G9wsZTnbtt48g`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_*_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29163274-2c1d-4992-ad58-0a872a428aa8",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X5yTsF6F766er7TMXk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21f3469a-986f-43ff-866b-5648c8657872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Eq43fBpQawQByhz4QY6ax",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20779,
      "cache_read_input_tokens": 0,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20779,
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

_source line 4 · 2026-05-16T03:14:31.013Z_

<details><summary>↩ Tool result · `toolu_01N2HBkUa89G9wsZTnbtt48g`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_medium_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_yi_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_codellama_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_gemma2_compounding_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_internlm2_compounding_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f3469a-986f-43ff-866b-5648c8657872",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "f1631482-7ef2-40c5-8192-2516857930ed",
  "sourceToolAssistantUUID": "21f3469a-986f-43ff-866b-5648c8657872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T03:14:32.298Z_

Now let me read each of the 5 scripts to extract the required parameters:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1631482-7ef2-40c5-8192-2516857930ed",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c65cadd5-eb96-407b-9e4b-e71d1f482eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1186,
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

_source line 6 · 2026-05-16T03:14:33.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_0112dybMpHKPD9wFeeJ9EsC3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_yi_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c65cadd5-eb96-407b-9e4b-e71d1f482eee",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbddb966-4719-4a5a-a47b-149261956426",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1186,
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

_source line 7 · 2026-05-16T03:14:33.406Z_

<details><summary>↩ Tool result · `toolu_0112dybMpHKPD9wFeeJ9EsC3`</summary>

```text
1	"""Yi-1.5-9B compounding sweep — measure super-additivity of 2-bit deltas.
2	
3	Architecture: 32 layers x 8 KV heads (GQA 4:1), 256 total KV heads.
4	Progressively apply 2-bit quantization to increasing numbers of heads
5	(sorted by individual delta, most sensitive first) and measure joint PPL.
6	"""
7	import os
8	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
9	os.environ["HF_DATASETS_OFFLINE"] = "1"
10	
11	import argparse
12	import json
13	import math
14	import time
15	import torch
16	import torch.nn.functional as F
17	from transformers import AutoModelForCausalLM, AutoTokenizer
18	from eval_ppl import patch_attention, restore_attention
19	
20	MODEL_PATH = "/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B"
21	PROFILE_PATH = "yi15_hires_bf16_2bitonly_profiles.json"
22	OUTPUT_PATH = "artifacts/yi_compounding_sweep.json"
23	
24	
25	def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
26	    with open(path) as f:
27	        samples = json.load(f)
28	    all_ids = []
29	    for s in samples:
30	        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
31	        if len(tokens) >= seq_len:
32	            all_ids.append(tokens[:seq_len])
33	        if len(all_ids) >= num_samples:
34	            break
35	    if not all_ids:
36	        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
37	    return torch.tensor(all_ids, dtype=torch.long, device=device)
38	
39	
40	def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
41	    total_loss = 0.0
42	    total_tokens = 0
43	    n = input_ids.shape[0]
44	    with torch.no_grad():
45	        for start in range(0, n, batch_size):
46	            end = min(start + batch_size, n)
47	            batch = input_ids[start:end]
48	            outputs = model(
49	                batch, use_cache=False,
50	                cache_position=torch.arange(seq_len, device=device)
51	            )
52	            shift_logits = outputs.logits[:, :-1].contiguous()
53	            shift_labels = batch[:, 1:].contiguous()
54	            loss = F.cross_entropy(
55	                shift_logits.float().view(-1, shift_logits.shape[-1]),
56	                shift_labels.view(-1),
57	                reduction="sum"
58	            )
59	            total_loss += loss.item()
60	            total_tokens += shift_labels.numel()
61	            del outputs, shift_logits, loss
62	            torch.cuda.empty_cache()
63	    return math.exp(total_loss / total_tokens)
64	
65	
66	def main():
67	    parser = argparse.ArgumentParser(description="Yi-1.5-9B compounding sweep")
68	    parser.add_argument("--gpu", type=str, default="cuda:0")
69	    parser.add_argument("--num_samples", type=int, default=64)
70	    parser.add_argument("--seq_len", type=int, default=2048)
71	    parser.add_argument("--batch_size", type=int, default=2)
72	    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
73	    args = parser.parse_args()
74	
75	    device = args.gpu
76	    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
77	    t0 = time.time()
78	
79	    print("Loading profiles...")
80	    with open(PROFILE_PATH) as f:
81	        raw = json.load(f)
82	    profiles = raw["profiles"] if "profiles" in raw else raw
83	
84	    head_deltas = []
85	    for l_str in sorted(profiles.keys(), key=int):
86	        for h_str in sorted(profiles[l_str].keys(), key=int):
87	            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
88	            head_deltas.append({
89	                "layer": int(l_str),
90	                "head": int(h_str),
91	                "key": f"{l_str},{h_str}",
92	                "delta_2bit": d2,
93	            })
94	    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)
95	
96	    total_kv_heads = len(head_deltas)
97	    k_values = [k for k in k_values if k <= total_kv_heads]
98	    print(f"Total KV heads: {total_kv_heads}")
99	    print(f"Sweep k values: {k_values}")
100	    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")
101	
102	    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
103	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
104	    model = AutoModelForCausalLM.from_pretrained(
105	        MODEL_PATH, torch_dtype=torch.bfloat16, attn_implementation="eager"
106	    )
107	    model = model.to(device)
108	    model.eval()
109	    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")
110	
111	    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
112	    input_ids = load_calibration_data(
113	        tokenizer, args.calibration_data,
114	        args.num_samples, args.seq_len, device)
115	    print(f"Loaded {input_ids.shape[0]} sequences")
116	
117	    print("\nMeasuring baseline PPL...")
118	    baseline_ppl = compute_ppl_batched(
119	        model, input_ids, args.seq_len, args.batch_size, device)
120	    print(f"Baseline PPL: {baseline_ppl:.4f}")
121	
122	    results = []
123	    for k in k_values:
124	        print(f"\n--- k={k} ---")
125	        if k == 0:
126	            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
127	            results.append({
128	                "k": 0,
129	                "heads": [],
130	                "sum_individual_delta": 0.0,
131	                "joint_ppl": round(baseline_ppl, 4),
132	                "joint_delta": 0.0,
133	                "predicted_ppl": round(baseline_ppl, 4),
134	                "super_additive_ratio": 1.0,
135	            })
136	            continue
137	
138	        top_k = head_deltas[:k]
139	        allocation = {h["key"]: ["quant", 2] for h in top_k}
140	        sum_individual = sum(h["delta_2bit"] for h in top_k)
141	
142	        orig_fwds = patch_attention(model, allocation)
143	        joint_ppl = compute_ppl_batched(
144	            model, input_ids, args.seq_len, args.batch_size, device)
145	        restore_attention(model, orig_fwds)
146	
147	        joint_delta = joint_ppl - baseline_ppl
148	        predicted_ppl = baseline_ppl + sum_individual
149	        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')
150	
151	        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
152	              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")
153	
154	        results.append({
155	            "k": k,
156	            "heads": [h["key"] for h in top_k],
157	            "sum_individual_delta": round(sum_individual, 6),
158	            "joint_ppl": round(joint_ppl, 4),
159	            "joint_delta": round(joint_delta, 6),
160	            "predicted_ppl": round(predicted_ppl, 4),
161	            "super_additive_ratio": round(ratio, 4),
162	        })
163	
164	    elapsed = time.time() - t0
165	
166	    output = {
167	        "experiment": "yi_compounding_sweep",
168	        "model": MODEL_PATH,
169	        "model_name": "Yi-1.5-9B",
170	        "baseline_ppl_measured": round(baseline_ppl, 4),
171	        "calibration": {
172	            "path": args.calibration_data,
173	            "num_samples": args.num_samples,
174	            "seq_len": args.seq_len,
175	        },
176	        "total_kv_heads": total_kv_heads,
177	        "results": results,
178	        "top_heads": [
179	            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
180	            for h in head_deltas[:10]
181	        ],
182	        "timing_seconds": round(elapsed, 1),
183	    }
184	
185	    os.makedirs("artifacts", exist_ok=True)
186	    with open(OUTPUT_PATH, "w") as f:
187	        json.dump(output, f, indent=2)
188	    print(f"\nJSON saved to {OUTPUT_PATH}")
189	
190	    print(f"\n{'='*70}")
191	    print("COMPOUNDING SWEEP — Yi-1.5-9B (256 KV heads)")
192	    print(f"{'='*70}")
193	    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
194	    print("-" * 70)
195	    for r in results:
196	        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
197	              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
198	              f"{r['super_additive_ratio']:>8.4f}")
199	    print(f"\nTotal time: {elapsed/60:.1f}min")
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
  "parentUuid": "dbddb966-4719-4a5a-a47b-149261956426",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "60215e56-4943-41c6-98b3-5dc2536241b0",
  "sourceToolAssistantUUID": "dbddb966-4719-4a5a-a47b-149261956426",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T03:14:33.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_0178nASgkeh7cLuvQjVw3yB9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_gemma2_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60215e56-4943-41c6-98b3-5dc2536241b0",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d71a0510-589b-496b-bcd5-2761a18127b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1186,
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

_source line 9 · 2026-05-16T03:14:33.529Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DGAGPynHqUCkZTr2vLxCyN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_codellama_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d71a0510-589b-496b-bcd5-2761a18127b5",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "db7e157d-5f99-4708-b8e4-4bc756fca4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1186,
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

_source line 10 · 2026-05-16T03:14:33.534Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RzQUEzNw11wFSUTEUw8HsD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_phi3_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db7e157d-5f99-4708-b8e4-4bc756fca4a5",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84906634-7811-485f-82cb-8722198da4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1186,
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

_source line 11 · 2026-05-16T03:14:33.540Z_

<details><summary>↩ Tool result · `toolu_0178nASgkeh7cLuvQjVw3yB9`</summary>

```text
1	"""Gemma-2-9B compounding sweep — measure super-additivity of 2-bit deltas.
2	
3	Architecture: 42 layers x 8 KV heads (GQA), 336 total KV heads.
4	Progressively apply 2-bit quantization to increasing numbers of heads
5	(sorted by individual delta, most sensitive first) and measure joint PPL.
6	
7	Gemma-2 specifics:
8	  - Uses patch_attention_gemma2 (handles head_dim=256, attn_logit_softcapping,
9	    sliding_window via attention_mask).
10	  - Calibration sequences prepend BOS (Gemma-2's tokenizer expects BOS as first token).
11	"""
12	import os
13	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
14	os.environ["HF_DATASETS_OFFLINE"] = "1"
15	
16	import argparse
17	import json
18	import math
19	import time
20	import torch
21	import torch.nn.functional as F
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	from run_gemma2_full_pipeline import patch_attention_gemma2, restore_attention
24	
25	MODEL_PATH = "/root/autodl-tmp/.hf_cache/google/gemma-2-9b"
26	PROFILE_PATH = "gemma2_hires_bf16_2bitonly_profiles.json"
27	OUTPUT_PATH = "artifacts/gemma2_compounding_sweep.json"
28	
29	
30	def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
31	    """Load calibration with BOS prepended (Gemma-2 requires BOS)."""
32	    with open(path) as f:
33	        samples = json.load(f)
34	    bos_id = tokenizer.bos_token_id
35	    if bos_id is None:
36	        raise RuntimeError("Gemma-2 tokenizer missing BOS token id")
37	    all_ids = []
38	    for s in samples:
39	        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
40	        if len(tokens) >= seq_len - 1:
41	            all_ids.append([bos_id] + tokens[:seq_len - 1])
42	        if len(all_ids) >= num_samples:
43	            break
44	    if not all_ids:
45	        raise RuntimeError(f"No calibration seqs with >= {seq_len - 1} tokens")
46	    return torch.tensor(all_ids, dtype=torch.long, device=device)
47	
48	
49	def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
50	    total_loss = 0.0
51	    total_tokens = 0
52	    n = input_ids.shape[0]
53	    with torch.no_grad():
54	        for start in range(0, n, batch_size):
55	            end = min(start + batch_size, n)
56	            batch = input_ids[start:end]
57	            outputs = model(
58	                batch, use_cache=False,
59	                cache_position=torch.arange(seq_len, device=device)
60	            )
61	            shift_logits = outputs.logits[:, :-1].contiguous()
62	            shift_labels = batch[:, 1:].contiguous()
63	            loss = F.cross_entropy(
64	                shift_logits.float().view(-1, shift_logits.shape[-1]),
65	                shift_labels.view(-1),
66	                reduction="sum"
67	            )
68	            total_loss += loss.item()
69	            total_tokens += shift_labels.numel()
70	            del outputs, shift_logits, loss
71	            torch.cuda.empty_cache()
72	    return math.exp(total_loss / total_tokens)
73	
74	
75	def main():
76	    parser = argparse.ArgumentParser(description="Gemma-2-9B compounding sweep")
77	    parser.add_argument("--gpu", type=str, default="cuda:0")
78	    parser.add_argument("--num_samples", type=int, default=64)
79	    parser.add_argument("--seq_len", type=int, default=2048)
80	    parser.add_argument("--batch_size", type=int, default=2)
81	    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
82	    args = parser.parse_args()
83	
84	    device = args.gpu
85	    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
86	    t0 = time.time()
87	
88	    print("Loading profiles...")
89	    with open(PROFILE_PATH) as f:
90	        raw = json.load(f)
91	    profiles = raw["profiles"] if "profiles" in raw else raw
92	
93	    head_deltas = []
94	    for l_str in sorted(profiles.keys(), key=int):
95	        for h_str in sorted(profiles[l_str].keys(), key=int):
96	            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
97	            head_deltas.append({
98	                "layer": int(l_str),
99	                "head": int(h_str),
100	                "key": f"{l_str},{h_str}",
101	                "delta_2bit": d2,
102	            })
103	    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)
104	
105	    total_kv_heads = len(head_deltas)
106	    k_values = [k for k in k_values if k <= total_kv_heads]
107	    print(f"Total KV heads: {total_kv_heads}")
108	    print(f"Sweep k values: {k_values}")
109	    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")
110	
111	    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
112	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
113	    model = AutoModelForCausalLM.from_pretrained(
114	        MODEL_PATH, torch_dtype=torch.bfloat16, attn_implementation="eager"
115	    )
116	    model = model.to(device)
117	    model.eval()
118	    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")
119	
120	    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
121	    input_ids = load_calibration_data(
122	        tokenizer, args.calibration_data,
123	        args.num_samples, args.seq_len, device)
124	    print(f"Loaded {input_ids.shape[0]} sequences")
125	
126	    print("\nMeasuring baseline PPL...")
127	    baseline_ppl = compute_ppl_batched(
128	        model, input_ids, args.seq_len, args.batch_size, device)
129	    print(f"Baseline PPL: {baseline_ppl:.4f}")
130	
131	    results = []
132	    for k in k_values:
133	        print(f"\n--- k={k} ---")
134	        if k == 0:
135	            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
136	            results.append({
137	                "k": 0,
138	                "heads": [],
139	                "sum_individual_delta": 0.0,
140	                "joint_ppl": round(baseline_ppl, 4),
141	                "joint_delta": 0.0,
142	                "predicted_ppl": round(baseline_ppl, 4),
143	                "super_additive_ratio": 1.0,
144	            })
145	            continue
146	
147	        top_k = head_deltas[:k]
148	        allocation = {h["key"]: ["quant", 2] for h in top_k}
149	        sum_individual = sum(h["delta_2bit"] for h in top_k)
150	
151	        orig_fwds = patch_attention_gemma2(model, allocation)
152	        joint_ppl = compute_ppl_batched(
153	            model, input_ids, args.seq_len, args.batch_size, device)
154	        restore_attention(model, orig_fwds)
155	
156	        joint_delta = joint_ppl - baseline_ppl
157	        predicted_ppl = baseline_ppl + sum_individual
158	        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')
159	
160	        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
161	              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")
162	
163	        results.append({
164	            "k": k,
165	            "heads": [h["key"] for h in top_k],
166	            "sum_individual_delta": round(sum_individual, 6),
167	            "joint_ppl": round(joint_ppl, 4),
168	            "joint_delta": round(joint_delta, 6),
169	            "predicted_ppl": round(predicted_ppl, 4),
170	            "super_additive_ratio": round(ratio, 4),
171	        })
172	
173	    elapsed = time.time() - t0
174	
175	    output = {
176	        "experiment": "gemma2_compounding_sweep",
177	        "model": MODEL_PATH,
178	        "model_name": "Gemma-2-9B",
179	        "baseline_ppl_measured": round(baseline_ppl, 4),
180	        "calibration": {
181	            "path": args.calibration_data,
182	            "num_samples": args.num_samples,
183	            "seq_len": args.seq_len,
184	        },
185	        "total_kv_heads": total_kv_heads,
186	        "results": results,
187	        "top_heads": [
188	            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
189	            for h in head_deltas[:10]
190	        ],
191	        "timing_seconds": round(elapsed, 1),
192	    }
193	
194	    os.makedirs("artifacts", exist_ok=True)
195	    with open(OUTPUT_PATH, "w") as f:
196	        json.dump(output, f, indent=2)
197	    print(f"\nJSON saved to {OUTPUT_PATH}")
198	
199	    print(f"\n{'='*70}")
200	    print("COMPOUNDING SWEEP — Gemma-2-9B (336 KV heads)")
201	    print(f"{'='*70}")
202	    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
203	    print("-" * 70)
204	    for r in results:
205	        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
206	              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
207	              f"{r['super_additive_ratio']:>8.4f}")
208	    print(f"\nTotal time: {elapsed/60:.1f}min")
209	
210	
211	if __name__ == "__main__":
212	    main()
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d71a0510-589b-496b-bcd5-2761a18127b5",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "67f3e3ee-926f-4e09-859c-06966d65caa1",
  "sourceToolAssistantUUID": "d71a0510-589b-496b-bcd5-2761a18127b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:14:33.543Z_

<details><summary>↩ Tool result · `toolu_01DGAGPynHqUCkZTr2vLxCyN`</summary>

```text
1	"""CodeLlama-7B compounding sweep — measure super-additivity of 2-bit deltas.
2	
3	Architecture: 32 layers x 32 KV heads (MHA, no GQA), 1024 total KV heads.
4	Progressively apply 2-bit quantization to increasing numbers of heads
5	(sorted by individual delta, most sensitive first) and measure joint PPL.
6	"""
7	import os
8	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
9	os.environ["HF_DATASETS_OFFLINE"] = "1"
10	
11	import argparse
12	import json
13	import math
14	import time
15	import torch
16	import torch.nn.functional as F
17	from transformers import AutoModelForCausalLM, AutoTokenizer
18	from eval_ppl import patch_attention, restore_attention
19	
20	MODEL_PATH = "/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf"
21	PROFILE_PATH = "artifacts/codellama_profiles_hires.json"
22	OUTPUT_PATH = "artifacts/codellama_compounding_sweep.json"
23	
24	
25	def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
26	    with open(path) as f:
27	        samples = json.load(f)
28	    all_ids = []
29	    for s in samples:
30	        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
31	        if len(tokens) >= seq_len:
32	            all_ids.append(tokens[:seq_len])
33	        if len(all_ids) >= num_samples:
34	            break
35	    if not all_ids:
36	        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
37	    return torch.tensor(all_ids, dtype=torch.long, device=device)
38	
39	
40	def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
41	    total_loss = 0.0
42	    total_tokens = 0
43	    n = input_ids.shape[0]
44	    with torch.no_grad():
45	        for start in range(0, n, batch_size):
46	            end = min(start + batch_size, n)
47	            batch = input_ids[start:end]
48	            outputs = model(
49	                batch, use_cache=False,
50	                cache_position=torch.arange(seq_len, device=device)
51	            )
52	            shift_logits = outputs.logits[:, :-1].contiguous()
53	            shift_labels = batch[:, 1:].contiguous()
54	            loss = F.cross_entropy(
55	                shift_logits.float().view(-1, shift_logits.shape[-1]),
56	                shift_labels.view(-1),
57	                reduction="sum"
58	            )
59	            total_loss += loss.item()
60	            total_tokens += shift_labels.numel()
61	            del outputs, shift_logits, loss
62	            torch.cuda.empty_cache()
63	    return math.exp(total_loss / total_tokens)
64	
65	
66	def main():
67	    parser = argparse.ArgumentParser(description="CodeLlama-7B compounding sweep")
68	    parser.add_argument("--gpu", type=str, default="cuda:0")
69	    parser.add_argument("--num_samples", type=int, default=64)
70	    parser.add_argument("--seq_len", type=int, default=2048)
71	    parser.add_argument("--batch_size", type=int, default=2)
72	    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
73	    args = parser.parse_args()
74	
75	    device = args.gpu
76	    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
77	    t0 = time.time()
78	
79	    print("Loading profiles...")
80	    with open(PROFILE_PATH) as f:
81	        raw = json.load(f)
82	    profiles = raw["profiles"] if "profiles" in raw else raw
83	
84	    head_deltas = []
85	    for l_str in sorted(profiles.keys(), key=int):
86	        for h_str in sorted(profiles[l_str].keys(), key=int):
87	            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
88	            head_deltas.append({
89	                "layer": int(l_str),
90	                "head": int(h_str),
91	                "key": f"{l_str},{h_str}",
92	                "delta_2bit": d2,
93	            })
94	    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)
95	
96	    total_kv_heads = len(head_deltas)
97	    k_values = [k for k in k_values if k <= total_kv_heads]
98	    print(f"Total KV heads: {total_kv_heads} (MHA: 32L x 32H)")
99	    print(f"Sweep k values: {k_values}")
100	    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")
101	
102	    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
103	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
104	    model = AutoModelForCausalLM.from_pretrained(
105	        MODEL_PATH, torch_dtype=torch.bfloat16, attn_implementation="eager"
106	    )
107	    model = model.to(device)
108	    model.eval()
109	    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")
110	
111	    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
112	    input_ids = load_calibration_data(
113	        tokenizer, args.calibration_data,
114	        args.num_samples, args.seq_len, device)
115	    print(f"Loaded {input_ids.shape[0]} sequences")
116	
117	    print("\nMeasuring baseline PPL...")
118	    baseline_ppl = compute_ppl_batched(
119	        model, input_ids, args.seq_len, args.batch_size, device)
120	    print(f"Baseline PPL: {baseline_ppl:.4f}")
121	
122	    results = []
123	    for k in k_values:
124	        print(f"\n--- k={k} ---")
125	        if k == 0:
126	            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
127	            results.append({
128	                "k": 0,
129	                "heads": [],
130	                "sum_individual_delta": 0.0,
131	                "joint_ppl": round(baseline_ppl, 4),
132	                "joint_delta": 0.0,
133	                "predicted_ppl": round(baseline_ppl, 4),
134	                "super_additive_ratio": 1.0,
135	            })
136	            continue
137	
138	        top_k = head_deltas[:k]
139	        allocation = {h["key"]: ["quant", 2] for h in top_k}
140	        sum_individual = sum(h["delta_2bit"] for h in top_k)
141	
142	        orig_fwds = patch_attention(model, allocation)
143	        joint_ppl = compute_ppl_batched(
144	            model, input_ids, args.seq_len, args.batch_size, device)
145	        restore_attention(model, orig_fwds)
146	
147	        joint_delta = joint_ppl - baseline_ppl
148	        predicted_ppl = baseline_ppl + sum_individual
149	        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')
150	
151	        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
152	              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")
153	
154	        results.append({
155	            "k": k,
156	            "heads": [h["key"] for h in top_k],
157	            "sum_individual_delta": round(sum_individual, 6),
158	            "joint_ppl": round(joint_ppl, 4),
159	            "joint_delta": round(joint_delta, 6),
160	            "predicted_ppl": round(predicted_ppl, 4),
161	            "super_additive_ratio": round(ratio, 4),
162	        })
163	
164	    elapsed = time.time() - t0
165	
166	    output = {
167	        "experiment": "codellama_compounding_sweep",
168	        "model": MODEL_PATH,
169	        "model_name": "CodeLlama-7B",
170	        "baseline_ppl_measured": round(baseline_ppl, 4),
171	        "calibration": {
172	            "path": args.calibration_data,
173	            "num_samples": args.num_samples,
174	            "seq_len": args.seq_len,
175	        },
176	        "total_kv_heads": total_kv_heads,
177	        "results": results,
178	        "top_heads": [
179	            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
180	            for h in head_deltas[:10]
181	        ],
182	        "timing_seconds": round(elapsed, 1),
183	    }
184	
185	    os.makedirs("artifacts", exist_ok=True)
186	    with open(OUTPUT_PATH, "w") as f:
187	        json.dump(output, f, indent=2)
188	    print(f"\nJSON saved to {OUTPUT_PATH}")
189	
190	    print(f"\n{'='*70}")
191	    print("COMPOUNDING SWEEP — CodeLlama-7B (1024 KV heads, MHA)")
192	    print(f"{'='*70}")
193	    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
194	    print("-" * 70)
195	    for r in results:
196	        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
197	              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
198	              f"{r['super_additive_ratio']:>8.4f}")
199	    print(f"\nTotal time: {elapsed/60:.1f}min")
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
  "parentUuid": "db7e157d-5f99-4708-b8e4-4bc756fca4a5",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "70de387c-fb2f-4296-acf8-1bdf8e2ccdfe",
  "sourceToolAssistantUUID": "db7e157d-5f99-4708-b8e4-4bc756fca4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T03:14:33.542Z_

<details><summary>↩ Tool result · `toolu_01RzQUEzNw11wFSUTEUw8HsD`</summary>

```text
1	"""Phi-3-medium-14B compounding sweep — measure super-additivity of 2-bit deltas.
2	
3	Architecture: 40 layers x 10 KV heads (GQA 4:1), 400 total KV heads.
4	Progressively apply 2-bit quantization to increasing numbers of heads
5	(sorted by individual delta, most sensitive first) and measure joint PPL.
6	Uses eval_ppl.patch_attention (Phi-3's fused qkv_proj is handled there).
7	"""
8	import os
9	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
10	os.environ["HF_DATASETS_OFFLINE"] = "1"
11	
12	import argparse
13	import json
14	import math
15	import time
16	import torch
17	import torch.nn.functional as F
18	from transformers import AutoModelForCausalLM, AutoTokenizer
19	from eval_ppl import patch_attention, restore_attention
20	
21	MODEL_PATH = "/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct"
22	PROFILE_PATH = "artifacts/phi3_medium_profiles_hires.json"
23	OUTPUT_PATH = "artifacts/phi3_compounding_sweep.json"
24	
25	
26	def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
27	    with open(path) as f:
28	        samples = json.load(f)
29	    all_ids = []
30	    for s in samples:
31	        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
32	        if len(tokens) >= seq_len:
33	            all_ids.append(tokens[:seq_len])
34	        if len(all_ids) >= num_samples:
35	            break
36	    if not all_ids:
37	        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
38	    return torch.tensor(all_ids, dtype=torch.long, device=device)
39	
40	
41	def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
42	    total_loss = 0.0
43	    total_tokens = 0
44	    n = input_ids.shape[0]
45	    with torch.no_grad():
46	        for start in range(0, n, batch_size):
47	            end = min(start + batch_size, n)
48	            batch = input_ids[start:end]
49	            outputs = model(
50	                batch, use_cache=False,
51	                cache_position=torch.arange(seq_len, device=device)
52	            )
53	            shift_logits = outputs.logits[:, :-1].contiguous()
54	            shift_labels = batch[:, 1:].contiguous()
55	            loss = F.cross_entropy(
56	                shift_logits.float().view(-1, shift_logits.shape[-1]),
57	                shift_labels.view(-1),
58	                reduction="sum"
59	            )
60	            total_loss += loss.item()
61	            total_tokens += shift_labels.numel()
62	            del outputs, shift_logits, loss
63	            torch.cuda.empty_cache()
64	    return math.exp(total_loss / total_tokens)
65	
66	
67	def main():
68	    parser = argparse.ArgumentParser(description="Phi-3-medium-14B compounding sweep")
69	    parser.add_argument("--gpu", type=str, default="cuda:0")
70	    parser.add_argument("--num_samples", type=int, default=64)
71	    parser.add_argument("--seq_len", type=int, default=2048)
72	    parser.add_argument("--batch_size", type=int, default=1)
73	    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
74	    args = parser.parse_args()
75	
76	    device = args.gpu
77	    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
78	    t0 = time.time()
79	
80	    print("Loading profiles...")
81	    with open(PROFILE_PATH) as f:
82	        raw = json.load(f)
83	    profiles = raw["profiles"] if "profiles" in raw else raw
84	
85	    head_deltas = []
86	    for l_str in sorted(profiles.keys(), key=int):
87	        for h_str in sorted(profiles[l_str].keys(), key=int):
88	            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
89	            head_deltas.append({
90	                "layer": int(l_str),
91	                "head": int(h_str),
92	                "key": f"{l_str},{h_str}",
93	                "delta_2bit": d2,
94	            })
95	    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)
96	
97	    total_kv_heads = len(head_deltas)
98	    k_values = [k for k in k_values if k <= total_kv_heads]
99	    print(f"Total KV heads: {total_kv_heads}")
100	    print(f"Sweep k values: {k_values}")
101	    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")
102	
103	    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
104	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
105	    model = AutoModelForCausalLM.from_pretrained(
106	        MODEL_PATH, torch_dtype=torch.bfloat16,
107	        attn_implementation="eager", trust_remote_code=True
108	    )
109	    model = model.to(device)
110	    model.eval()
111	    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")
112	
113	    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
114	    input_ids = load_calibration_data(
115	        tokenizer, args.calibration_data,
116	        args.num_samples, args.seq_len, device)
117	    print(f"Loaded {input_ids.shape[0]} sequences")
118	
119	    print("\nMeasuring baseline PPL...")
120	    baseline_ppl = compute_ppl_batched(
121	        model, input_ids, args.seq_len, args.batch_size, device)
122	    print(f"Baseline PPL: {baseline_ppl:.4f}")
123	
124	    results = []
125	    for k in k_values:
126	        print(f"\n--- k={k} ---")
127	        if k == 0:
128	            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
129	            results.append({
130	                "k": 0,
131	                "heads": [],
132	                "sum_individual_delta": 0.0,
133	                "joint_ppl": round(baseline_ppl, 4),
134	                "joint_delta": 0.0,
135	                "predicted_ppl": round(baseline_ppl, 4),
136	                "super_additive_ratio": 1.0,
137	            })
138	            continue
139	
140	        top_k = head_deltas[:k]
141	        allocation = {h["key"]: ["quant", 2] for h in top_k}
142	        sum_individual = sum(h["delta_2bit"] for h in top_k)
143	
144	        orig_fwds = patch_attention(model, allocation)
145	        joint_ppl = compute_ppl_batched(
146	            model, input_ids, args.seq_len, args.batch_size, device)
147	        restore_attention(model, orig_fwds)
148	
149	        joint_delta = joint_ppl - baseline_ppl
150	        predicted_ppl = baseline_ppl + sum_individual
151	        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')
152	
153	        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
154	              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")
155	
156	        results.append({
157	            "k": k,
158	            "heads": [h["key"] for h in top_k],
159	            "sum_individual_delta": round(sum_individual, 6),
160	            "joint_ppl": round(joint_ppl, 4),
161	            "joint_delta": round(joint_delta, 6),
162	            "predicted_ppl": round(predicted_ppl, 4),
163	            "super_additive_ratio": round(ratio, 4),
164	        })
165	
166	    elapsed = time.time() - t0
167	
168	    output = {
169	        "experiment": "phi3_compounding_sweep",
170	        "model": MODEL_PATH,
171	        "model_name": "Phi-3-medium-14B",
172	        "baseline_ppl_measured": round(baseline_ppl, 4),
173	        "calibration": {
174	            "path": args.calibration_data,
175	            "num_samples": args.num_samples,
176	            "seq_len": args.seq_len,
177	        },
178	        "total_kv_heads": total_kv_heads,
179	        "results": results,
180	        "top_heads": [
181	            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
182	            for h in head_deltas[:10]
183	        ],
184	        "timing_seconds": round(elapsed, 1),
185	    }
186	
187	    os.makedirs("artifacts", exist_ok=True)
188	    with open(OUTPUT_PATH, "w") as f:
189	        json.dump(output, f, indent=2)
190	    print(f"\nJSON saved to {OUTPUT_PATH}")
191	
192	    print(f"\n{'='*70}")
193	    print("COMPOUNDING SWEEP — Phi-3-medium-14B (400 KV heads)")
194	    print(f"{'='*70}")
195	    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
196	    print("-" * 70)
197	    for r in results:
198	        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
199	              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
200	              f"{r['super_additive_ratio']:>8.4f}")
201	    print(f"\nTotal time: {elapsed/60:.1f}min")
202	
203	
204	if __name__ == "__main__":
205	    main()
206	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84906634-7811-485f-82cb-8722198da4e5",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "35324e9a-cd4b-45b5-b679-360d3967b8c4",
  "sourceToolAssistantUUID": "84906634-7811-485f-82cb-8722198da4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T03:14:33.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BzYYG5AhhQi6rNckhYeMR3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_internlm2_compounding_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35324e9a-cd4b-45b5-b679-360d3967b8c4",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X66FQ8cFBP5frYii2y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d048ff8d-adce-4477-a50b-edfef361976b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JDsWyvM3p4ktauuWFhGjm1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 20779,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1186
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 398,
          "cache_read_input_tokens": 20779,
          "cache_creation_input_tokens": 1186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1186,
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

_source line 15 · 2026-05-16T03:14:33.825Z_

<details><summary>↩ Tool result · `toolu_01BzYYG5AhhQi6rNckhYeMR3`</summary>

```text
1	"""InternLM2-7B compounding sweep — measure super-additivity of 2-bit deltas.
2	
3	Architecture: 32 layers x 8 KV heads (GQA), 256 total KV heads.
4	Progressively apply 2-bit quantization to increasing numbers of heads
5	(sorted by individual delta, most sensitive first) and measure joint PPL.
6	
7	InternLM2 uses fused wqkv projection — custom patch_attention_internlm2 handles
8	the QKV splitting: [Q_groups (ng dims), K (2nd-to-last), V (last)].
9	"""
10	import os
11	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
12	os.environ["HF_DATASETS_OFFLINE"] = "1"
13	
14	import argparse
15	import json
16	import math
17	import time
18	import torch
19	import torch.nn.functional as F
20	from einops import rearrange
21	from transformers import AutoModelForCausalLM, AutoTokenizer
22	from utils import quantize_per_channel, quantize_per_token, repeat_kv
23	
24	MODEL_PATH = "/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2-7b"
25	PROFILE_PATH = "artifacts/internlm2_profiles_hires.json"
26	OUTPUT_PATH = "artifacts/internlm2_compounding_sweep.json"
27	
28	
29	def rotate_half(x):
30	    x1 = x[..., : x.shape[-1] // 2]
31	    x2 = x[..., x.shape[-1] // 2 :]
32	    return torch.cat((-x2, x1), dim=-1)
33	
34	
35	def apply_rotary_pos_emb(q, k, cos, sin, position_ids=None, unsqueeze_dim=1):
36	    cos = cos.unsqueeze(unsqueeze_dim)
37	    sin = sin.unsqueeze(unsqueeze_dim)
38	    q_embed = (q * cos) + (rotate_half(q) * sin)
39	    k_embed = (k * cos) + (rotate_half(k) * sin)
40	    return q_embed, k_embed
41	
42	
43	def patch_attention_internlm2(model, allocations):
44	    config = model.config
45	    num_kv_heads = config.num_key_value_heads
46	    num_q_heads = config.num_attention_heads
47	    head_dim = config.hidden_size // num_q_heads
48	    n_groups = num_q_heads // num_kv_heads
49	
50	    original_forwards = {}
51	
52	    for layer_idx, layer in enumerate(model.model.layers):
53	        attn = layer.attention
54	
55	        head_allocs = {}
56	        for h in range(num_kv_heads):
57	            key = f"{layer_idx},{h}"
58	            if key in allocations:
59	                atype, param = allocations[key]
60	                head_allocs[h] = (atype, param)
61	            else:
62	                head_allocs[h] = ("full", 16)
63	
64	        all_full = all(a[0] == "full" for a in head_allocs.values())
65	        if all_full:
66	            continue
67	
68	        original_forwards[layer_idx] = attn.forward
69	
70	        def make_forward(orig_attn, h_allocs, n_kv=num_kv_heads, ng=n_groups, hd=head_dim):
71	            def compressed_forward(hidden_states, attention_mask=None, position_ids=None,
72	                                   past_key_value=None, output_attentions=False,
73	                                   use_cache=False, cache_position=None, **kwargs):
74	                bsz, q_len, _ = hidden_states.size()
75	
76	                qkv_states = orig_attn.wqkv(hidden_states)
77	                qkv_states = rearrange(
78	                    qkv_states,
79	                    "b q (h gs d) -> b q h gs d",
80	                    gs=2 + ng,
81	                    d=hd,
82	                )
83	
84	                query_states = qkv_states[..., :ng, :]
85	                query_states = rearrange(query_states, "b q h gs d -> b q (h gs) d").transpose(1, 2)
86	                key_states = qkv_states[..., -2, :].transpose(1, 2)
87	                value_states = qkv_states[..., -1, :].transpose(1, 2)
88	
89	                cos, sin = orig_attn.rotary_emb(value_states, position_ids)
90	                query_states, key_states = apply_rotary_pos_emb(
91	                    query_states, key_states, cos, sin, position_ids
92	                )
93	
94	                for h in range(n_kv):
95	                    atype, param = h_allocs[h]
96	                    if atype == "quant" and int(param) < 16:
97	                        bits = int(param)
98	                        key_states[:, h] = quantize_per_channel(key_states[:, h:h + 1], bits).squeeze(1)
99	                        value_states[:, h] = quantize_per_token(value_states[:, h:h + 1], bits).squeeze(1)
100	
101	                key_exp = repeat_kv(key_states, ng)
102	                value_exp = repeat_kv(value_states, ng)
103	
104	                attn_weights = torch.matmul(query_states, key_exp.transpose(2, 3)) / math.sqrt(hd)
105	
106	                if attention_mask is not None:
107	                    causal_mask = attention_mask[:, :, :, :key_exp.shape[-2]]
108	                    attn_weights = attn_weights + causal_mask
109	                else:
110	                    causal = torch.triu(
111	                        torch.full((q_len, q_len), float("-inf"),
112	                                   device=attn_weights.device, dtype=attn_weights.dtype),
113	                        diagonal=1,
114	                    )
115	                    attn_weights = attn_weights + causal
116	
117	                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)
118	                attn_output = torch.matmul(attn_weights, value_exp)
119	
120	                attn_output = attn_output.transpose(1, 2).contiguous()
121	                attn_output = attn_output.reshape(bsz, q_len, -1)
122	                attn_output = orig_attn.wo(attn_output)
123	
124	                if not output_attentions:
125	                    attn_weights = None
126	
127	                return attn_output, attn_weights, past_key_value
128	
129	            return compressed_forward
130	
131	        attn.forward = make_forward(attn, head_allocs)
132	
133	    return original_forwards
134	
135	
136	def restore_attention_internlm2(model, original_forwards):
137	    for layer_idx, fwd in original_forwards.items():
138	        model.model.layers[layer_idx].attention.forward = fwd
139	
140	
141	def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
142	    with open(path) as f:
143	        samples = json.load(f)
144	    all_ids = []
145	    for s in samples:
146	        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
147	        if len(tokens) >= seq_len:
148	            all_ids.append(tokens[:seq_len])
149	        if len(all_ids) >= num_samples:
150	            break
151	    if not all_ids:
152	        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
153	    return torch.tensor(all_ids, dtype=torch.long, device=device)
154	
155	
156	def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
157	    total_loss = 0.0
158	    total_tokens = 0
159	    n = input_ids.shape[0]
160	    with torch.no_grad():
161	        for start in range(0, n, batch_size):
162	            end = min(start + batch_size, n)
163	            batch = input_ids[start:end]
164	            outputs = model(
165	                batch, use_cache=False,
166	                cache_position=torch.arange(seq_len, device=device)
167	            )
168	            shift_logits = outputs.logits[:, :-1].contiguous()
169	            shift_labels = batch[:, 1:].contiguous()
170	            loss = F.cross_entropy(
171	                shift_logits.float().view(-1, shift_logits.shape[-1]),
172	                shift_labels.view(-1),
173	                reduction="sum"
174	            )
175	            total_loss += loss.item()
176	            total_tokens += shift_labels.numel()
177	            del outputs, shift_logits, loss
178	            torch.cuda.empty_cache()
179	    return math.exp(total_loss / total_tokens)
180	
181	
182	def main():
183	    parser = argparse.ArgumentParser(description="InternLM2-7B compounding sweep")
184	    parser.add_argument("--gpu", type=str, default="cuda:0")
185	    parser.add_argument("--num_samples", type=int, default=64)
186	    parser.add_argument("--seq_len", type=int, default=2048)
187	    parser.add_argument("--batch_size", type=int, default=2)
188	    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
189	    args = parser.parse_args()
190	
191	    device = args.gpu
192	    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
193	    t0 = time.time()
194	
195	    print("Loading profiles...")
196	    with open(PROFILE_PATH) as f:
197	        raw = json.load(f)
198	    profiles = raw["profiles"] if "profiles" in raw else raw
199	
200	    head_deltas = []
201	    for l_str in sorted(profiles.keys(), key=int):
202	        for h_str in sorted(profiles[l_str].keys(), key=int):
203	            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
204	            head_deltas.append({
205	                "layer": int(l_str),
206	                "head": int(h_str),
207	                "key": f"{l_str},{h_str}",
208	                "delta_2bit": d2,
209	            })
210	    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)
211	
212	    total_kv_heads = len(head_deltas)
213	    k_values = [k for k in k_values if k <= total_kv_heads]
214	    print(f"Total KV heads: {total_kv_heads}")
215	    print(f"Sweep k values: {k_values}")
216	    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")
217	
218	    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
219	    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
220	    model = AutoModelForCausalLM.from_pretrained(
221	        MODEL_PATH, torch_dtype=torch.bfloat16,
222	        attn_implementation="eager", trust_remote_code=True
223	    )
224	    model = model.to(device)
225	    model.eval()
226	    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")
227	
228	    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
229	    input_ids = load_calibration_data(
230	        tokenizer, args.calibration_data,
231	        args.num_samples, args.seq_len, device)
232	    print(f"Loaded {input_ids.shape[0]} sequences")
233	
234	    print("\nMeasuring baseline PPL...")
235	    baseline_ppl = compute_ppl_batched(
236	        model, input_ids, args.seq_len, args.batch_size, device)
237	    print(f"Baseline PPL: {baseline_ppl:.4f}")
238	
239	    results = []
240	    for k in k_values:
241	        print(f"\n--- k={k} ---")
242	        if k == 0:
243	            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
244	            results.append({
245	                "k": 0,
246	                "heads": [],
247	                "sum_individual_delta": 0.0,
248	                "joint_ppl": round(baseline_ppl, 4),
249	                "joint_delta": 0.0,
250	                "predicted_ppl": round(baseline_ppl, 4),
251	                "super_additive_ratio": 1.0,
252	            })
253	            continue
254	
255	        top_k = head_deltas[:k]
256	        allocation = {h["key"]: ["quant", 2] for h in top_k}
257	        sum_individual = sum(h["delta_2bit"] for h in top_k)
258	
259	        orig_fwds = patch_attention_internlm2(model, allocation)
260	        joint_ppl = compute_ppl_batched(
261	            model, input_ids, args.seq_len, args.batch_size, device)
262	        restore_attention_internlm2(model, orig_fwds)
263	
264	        joint_delta = joint_ppl - baseline_ppl
265	        predicted_ppl = baseline_ppl + sum_individual
266	        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')
267	
268	        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
269	              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")
270	
271	        results.append({
272	            "k": k,
273	            "heads": [h["key"] for h in top_k],
274	            "sum_individual_delta": round(sum_individual, 6),
275	            "joint_ppl": round(joint_ppl, 4),
276	            "joint_delta": round(joint_delta, 6),
277	            "predicted_ppl": round(predicted_ppl, 4),
278	            "super_additive_ratio": round(ratio, 4),
279	        })
280	
281	    elapsed = time.time() - t0
282	
283	    output = {
284	        "experiment": "internlm2_compounding_sweep",
285	        "model": MODEL_PATH,
286	        "model_name": "InternLM2-7B",
287	        "baseline_ppl_measured": round(baseline_ppl, 4),
288	        "calibration": {
289	            "path": args.calibration_data,
290	            "num_samples": args.num_samples,
291	            "seq_len": args.seq_len,
292	        },
293	        "total_kv_heads": total_kv_heads,
294	        "results": results,
295	        "top_heads": [
296	            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
297	            for h in head_deltas[:10]
298	        ],
299	        "timing_seconds": round(elapsed, 1),
300	    }
301	
302	    os.makedirs("artifacts", exist_ok=True)
303	    with open(OUTPUT_PATH, "w") as f:
304	        json.dump(output, f, indent=2)
305	    print(f"\nJSON saved to {OUTPUT_PATH}")
306	
307	    print(f"\n{'='*70}")
308	    print("COMPOUNDING SWEEP — InternLM2-7B (256 KV heads)")
309	    print(f"{'='*70}")
310	    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
311	    print("-" * 70)
312	    for r in results:
313	        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
314	              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
315	              f"{r['super_additive_ratio']:>8.4f}")
316	    print(f"\nTotal time: {elapsed/60:.1f}min")
317	
318	
319	if __name__ == "__main__":
320	    main()
321	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d048ff8d-adce-4477-a50b-edfef361976b",
  "isSidechain": true,
  "promptId": "3d869325-27a7-4061-a19a-025b5eb7af5b",
  "agentId": "a5d42d85a37f4f722",
  "type": "user",
  "uuid": "b460275e-0a69-422a-b72d-f06a3bc92875",
  "sourceToolAssistantUUID": "d048ff8d-adce-4477-a50b-edfef361976b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T03:14:41.963Z_

## Summary

Here are the parameter checks for the 5 compounding sweep scripts:

**1. run_yi_compounding_sweep.py**
- Model path: `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B` (line 20)
- K values: `[0, 2, 4, 8, 16, 32, 64, 128, 256]` (line 76)
- Profile path: `yi15_hires_bf16_2bitonly_profiles.json` (line 21)
- Attention patching: `patch_attention, restore_attention` from `eval_ppl` (line 18)

**2. run_gemma2_compounding_sweep.py**
- Model path: `/root/autodl-tmp/.hf_cache/google/gemma-2-9b` (line 25)
- K values: `[0, 2, 4, 8, 16, 32, 64, 128, 256]` (line 85)
- Profile path: `gemma2_hires_bf16_2bitonly_profiles.json` (line 26)
- Attention patching: `patch_attention_gemma2, restore_attention` from `run_gemma2_full_pipeline` (line 23)

**3. run_codellama_compounding_sweep.py**
- Model path: `/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf` (line 20)
- K values: `[0, 2, 4, 8, 16, 32, 64, 128, 256]` (line 76)
- Profile path: `artifacts/codellama_profiles_hires.json` (line 21)
- Attention patching: `patch_attention, restore_attention` from `eval_ppl` (line 18)

**4. run_phi3_compounding_sweep.py**
- Model path: `/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct` (line 21)
- K values: `[0, 2, 4, 8, 16, 32, 64, 128, 256]` (line 77)
- Profile path: `artifacts/phi3_medium_profiles_hires.json` (line 22)
- Attention patching: `patch_attention, restore_attention` from `eval_ppl` (line 19)

**5. run_internlm2_compounding_sweep.py**
- Model path: `/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2-7b` (line 24)
- K values: `[0, 2, 4, 8, 16, 32, 64, 128, 256]` (line 192)
- Profile path: `artifacts/internlm2_profiles_hires.json` (line 25)
- Attention patching: `patch_attention_internlm2, restore_attention_internlm2` (custom implementations at lines 43-138)

All scripts use identical k_values lists. The patching methods are script-specific: generic `eval_ppl` functions for Yi/CodeLlama/Phi3, specialized Gemma2 variant, and custom InternLM2 implementation with fused QKV handling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b460275e-0a69-422a-b72d-f06a3bc92875",
  "isSidechain": true,
  "agentId": "a5d42d85a37f4f722",
  "requestId": "req_011Cb5X6JQ9YtgdjiRD5XnU3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed3ecd4d-0ed1-4c68-ac24-6ecac127f3c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/reviewer_fe2ad71b",
  "sessionId": "bf3403d6-3f63-4747-ae88-4c3a1f0ae77d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "curried-splashing-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LFnYFQjybwoqipCky2D7ut",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17541,
      "cache_read_input_tokens": 21965,
      "output_tokens": 837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 837,
          "cache_read_input_tokens": 21965,
          "cache_creation_input_tokens": 17541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17541,
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
