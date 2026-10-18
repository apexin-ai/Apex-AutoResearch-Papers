# gpu yi15 phase5 fix rerun

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_gpu_yi15_phase5_fix_rerun_20260514T182903.jsonl`
- **Structured JSON:** [`6f82cc9a76a146e3b0e3.json`](../../sessions/6f/6f82cc9a76a146e3b0e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T18:29:57.626504+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T18:29:57.626847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T18:29:57.627010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "ps aux | grep yi15",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "ps aux | grep yi15",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T18:29:57.627148+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T18:29:57.627273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "ls -la /root/ratekv/yi15_profiling_results.json /root/ratekv/yi15_k_ablation_results.json /root/ratekv/yi15_full_results.json 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "ls -la /root/ratekv/yi15_profiling_results.json /root/ratekv/yi15_k_ablation_results.json /root/ratekv/yi15_full_results.json 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T18:29:57.627396+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:29:57.627513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "tail -50 /root/ratekv/yi15_pipeline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "tail -50 /root/ratekv/yi15_pipeline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:29:57.627629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_yi15_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/run_yi15_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T18:29:57.627798+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/ratekv/yi15_pipeline.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:29:57.628037+00:00_

1	"""Yi-1.5-9B Full Pipeline: profiling + MCKP + k ablation.
2	GQA 8:1 (4 KV heads/layer, 48 layers, 192 total heads).
3	Llama-compatible architecture — uses standard profiler and eval code.
4	Tests whether high GQA ratio → high heterogeneity generalizes beyond Qwen.
5	"""
6	import os
7	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
8	os.environ["HF_DATASETS_OFFLINE"] = "1"
9	
10	import argparse
11	import json
12	import math
13	import time
14	import torch
15	from transformers import AutoConfig
16	from full_bitwidth_profiler import FullBitwidthProfiler
17	from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
18	from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
19	
20	
21	def main():
22	    parser = argparse.ArgumentParser()
23	    parser.add_argument("--model", type=str, required=True)
24	    parser.add_argument("--calibration_data", type=str, default="calibration_data.json")
25	    parser.add_argument("--output", type=str, default="yi15_full_results.json")
26	    parser.add_argument("--budget", type=float, default=0.25)
27	    parser.add_argument("--initial_k", type=int, default=8)
28	    parser.add_argument("--gpu", type=str, default="cuda:1")
29	    args = parser.parse_args()
30	
31	    device = args.gpu
32	    t0 = time.time()
33	
34	    # Validate architecture
35	    config = AutoConfig.from_pretrained(args.model)
36	    num_layers = config.num_hidden_layers
37	    num_kv_heads = config.num_key_value_heads
38	    num_q_heads = config.num_attention_heads
39	    gqa_ratio = num_q_heads // num_kv_heads
40	    total_kv_heads = num_layers * num_kv_heads
41	
42	    print(f"Yi-1.5-9B: {num_layers} layers, {num_kv_heads} KV heads/layer, "
43	          f"GQA {gqa_ratio}:1, {total_kv_heads} total KV heads")
44	    assert num_kv_heads == 4, f"Expected 4 KV heads, got {num_kv_heads}"
45	    assert num_layers == 48, f"Expected 48 layers, got {num_layers}"
46	
47	    # ========== Phase 1: Profiling ====
…[truncated 10927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:29:57.628238+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "ls -la /root/ratekv/yi15_profiling_results.json /root/ratekv/yi15_k_ablation_results.json /root/ratekv/yi15_full_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "ls -la /root/ratekv/yi15_profiling_results.json /root/ratekv/yi15_k_ablation_results.json /root/ratekv/yi15_full_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:29:57.628379+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  2842 May 15 01:04 /root/ratekv/yi15_full_results.json\\n-rw-r--r-- 1 root root  1184 May 15 01:04 /root/ratekv/yi15_k_ablation_results.json\\n-rw-r--r-- 1 root root 30174 May 15 00:57 /root/ratekv/yi15_profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T18:29:57.628505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "grep -n 'solve_ratequant_greedy\\|solve_greedy_ratequant\\|from solver import' /root/ratekv/run_yi15_full_pipeline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "grep -n 'solve_ratequant_greedy\\|solve_greedy_ratequant\\|from solver import' /root/ratekv/run_yi15_full_pipeline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T18:29:57.628626+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T18:29:57.628769+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "find /root/ratekv -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "find /root/ratekv -name \"*.log\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T18:29:57.628913+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "find /root/runs -name \"*yi15*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "find /root/runs -name \"*yi15*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T18:29:57.629131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/ratekv/mvp_run.log\\n/root/ratekv/mvp_sanity.log\\n/root/ratekv/ppl_mvp_fast.log\\n/root/ratekv/targeted_hybrid_smoke.log\\n/root/ratekv/targeted_hybrid.log\\n/root/ratekv/full_bitwidth.log\\n/root/ratekv/manual_test.log\\n/root/ratekv/budget_matched.log\\n/root/ratekv/exp_c.log\\n/root/ratekv/exp_c_no2bit.log\\n/root/ratekv/exp_d.log\\n/root/ratekv/exp_e.log\\n/root/ratekv/budget_sweep.log\\n/root/ratekv/c4_cross_dataset.log\\n/root/ratekv/c4_phase2_4.log\\n/root/ratekv/llama_pipeline.log\\n/root/ratekv/exp_e_eval.log\\n/root/ratekv/exp_e_eval_fix.log\\n/root/ratekv/exp_c_bf16_eval.log\\n/root/ratekv/exp_e_phase23.log\\n/root/ratekv/llama_eval_fix.log\\n/root/ratekv/mistral_pipeline.log\\n/root/ratekv/llama_recovery.log\\n/root/ratekv/llama_eval_fix2.log\\n/root/ratekv/llama_eval_bf16.log\\n/root/ratekv/llama_hires_pipeline.log\\n/root/ratekv/mistral_hires_pipeline.log\\n/root/ratekv/llama_aggressive_stdout.log\\n/root/ratekv/llama_aggressive.log\\n/root/ratekv/mistral_aggressive_tmux.log\\n/root/ratekv/mistral_aggressive.log\\n/root/ratekv/downstream_eval.log\\n/root/ratekv/kv_separation.log\\n/root/ratekv/l0_heuristic.log\\n/root/ratekv/l0_heuristic_corrected.log\\n/root/ratekv/bf16_reeval.log\\n/root/ratekv/mckp_reeval.log\\n/root/ratekv/hires_reeval.log\\n/root/ratekv/downstream_eval_mckp.log\\n/root/ratekv/mistral_remaining.log\\n/root/ratekv/hires_reeval_v2.log\\n/root/ratekv/mistral_constrained16.log\\n/root/ratekv/mistral_k_ablation.log\\n/root/ratekv/llama_k_ablation.log\\n/root/ratekv/multi_seed.log\\n/root/ratekv/cross_domain.log\\n/root/ratekv/c4_cross_dataset_eval_v2.log\\n/root/ratekv/runtime_benchmark.log\\n/root/ratekv/c4_rerun.log\\n/root/ratekv/multi_seed_lowres.log\\n/root/ratekv/oracle_comparison.log\\n/root/ratekv/d041_llama_heuristic_k2.log\\n/root/ratekv/mistral_heuristic_k4.log\\n/root/ratekv/mistral_c4_cross_dataset.log\\n/root/ratekv/llama_c4_cross_dataset.log\\n/root/ratekv/yi1
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T18:29:57.629290+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/ratekv/yi15_9b_full_pipeline.log\\n/root/runs/ratekv/yi15_9b_rerun.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T18:29:57.629513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "cat /root/ratekv/yi15_full_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "cat /root/ratekv/yi15_full_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T18:29:57.629836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B\\\",\\n  \\\"model_name\\\": \\\"Yi-1.5-9B\\\",\\n  \\\"model_type\\\": \\\"llama\\\",\\n  \\\"architecture\\\": {\\n    \\\"num_layers\\\": 48,\\n    \\\"num_kv_heads\\\": 4,\\n    \\\"num_attention_heads\\\": 32,\\n    \\\"head_dim\\\": 128,\\n    \\\"hidden_size\\\": 4096,\\n    \\\"gqa_ratio\\\": 8,\\n    \\\"total_kv_heads\\\": 192\\n  },\\n  \\\"verdict\\\": \\\"FAIL\\\",\\n  \\\"baseline_calibration_ppl\\\": 7.3460602946725135,\\n  \\\"baseline_wikitext2_ppl\\\": 7.0156955527784906,\\n  \\\"mckp_wikitext2_ppl\\\": 7.312944087440416,\\n  \\\"uniform4bit_wikitext2_ppl\\\": 7.217114011084877,\\n  \\\"mckp_improvement_over_uniform\\\": -0.09583007635553908,\\n  \\\"initial_k\\\": 8,\\n  \\\"bit_distribution\\\": {\\n    \\\"4\\\": 180,\\n    \\\"2\\\": 8,\\n    \\\"8\\\": 4\\n  },\\n  \\\"mckp_actual_memory_ratio\\\": 0.25,\\n  \\\"k_ablation\\\": [\\n    {\\n      \\\"max_2bit\\\": 2,\\n      \\\"ppl\\\": 7.2209,\\n      \\\"n_2bit_actual\\\": 2,\\n      \\\"total_distortion\\\": 1.3169696168865412,\\n      \\\"actual_memory_ratio\\\": 0.25\\n    },\\n    {\\n      \\\"max_2bit\\\": 4,\\n      \\\"ppl\\\": 7.2788,\\n      \\\"n_2bit_actual\\\": 4,\\n      \\\"total_distortion\\\": 1.3052035630492984,\\n      \\\"actual_memory_ratio\\\": 0.25\\n    },\\n    {\\n      \\\"max_2bit\\\": 6,\\n      \\\"ppl\\\": 7.2874,\\n      \\\"n_2bit_actual\\\": 6,\\n      \\\"total_distortion\\\": 1.293878878732155,\\n      \\\"actual_memory_ratio\\\": 0.25\\n    },\\n    {\\n      \\\"max_2bit\\\": 8,\\n      \\\"ppl\\\": 7.3129,\\n      \\\"n_2bit_actual\\\": 8,\\n      \\\"total_distortion\\\": 1.285005079654228,\\n      \\\"actual_memory_ratio\\\": 0.25\\n    },\\n    {\\n      \\\"max_2bit\\\": 10,\\n      \\\"ppl\\\": 7.4164,\\n      \\\"n_2bit_actual\\\": 10,\\n      \\\"total_distortion\\\": 1.2757068427970006,\\n      \\\"actual_memory_ratio\\\":
…[truncated 1818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:29:57.630073+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "tail -60 /root/runs/ratekv/yi15_9b_rerun.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "tail -60 /root/runs/ratekv/yi15_9b_rerun.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T18:29:57.630333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  chunk 650/661, running ppl=7.65\\nk=14: PPL=7.6612, n_2bit=14\\n\\n--- k=16 ---\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Thu May 14 03:51:25 2026).\\nEvaluating perplexity on 338838 tokens, stride=512, 661 chunks\\n  chunk 50/661, running ppl=7.34\\n  chunk 100/661, running ppl=7.89\\n  chunk 150/661, running ppl=7.98\\n  chunk 200/661, running ppl=7.65\\n  chunk 250/661, running ppl=7.69\\n  chunk 300/661, running ppl=7.59\\n  chunk 350/661, running ppl=7.48\\n  chunk 400/661, running ppl=7.48\\n  chunk 450/661, running ppl=7.77\\n  chunk 500/661, running ppl=7.74\\n  chunk 550/661, running ppl=7.74\\n  chunk 600/661, running ppl=7.68\\n  chunk 650/661, running ppl=7.68\\nk=16: PPL=7.6925, n_2bit=16\\n\\nBest k=2 with PPL=7.2209\\n\\n============================================================\\nPHASE 4: Heterogeneity Analysis\\n============================================================\\nTop-5% concentration: 0.4934 (9 heads)\\nLayer 0 mean delta(2bit): 0.006346\\nOther layers mean delta(2bit): 0.087716\\nL0 dominance ratio: 0.07x\\nHeads with positive delta: 192/192\\nCV of delta(2bit): 4.7938\\n\\nTop-5 most sensitive heads:\\n  L4H3: 2bit=+5.6523, 4bit=+0.0048, 8bit=+0.0040\\n  L8H2: 2bit=+1.0317, 4bit=+0.0129, 8bit=+0.0073\\n  L2H0: 2bit=+0.3833, 4bit=+0.0053, 8bit=+0.0053\\n  L34H0: 2bit=+0.2213, 4bit=+0.0057, 8bit=+0.0056\\n  L39H2: 2bit=+0.2094, 4bit=+0.0099, 8bit=+0.0035\\n\\nMCKP total distortion: 1.285005\\n\\n============================================================\\nRESULTS — Yi-1.5-9B\\n============================================================\\n\\nMethod                                PPL   Delta vs
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T18:29:57.630619+00:00_

Pipeline 已重跑完成，`yi15_full_results.json` 完整。无需再修复或重跑。

## Yi-1.5-9B 完整结果

### 架构
- 48 layers, 4 KV heads/layer, GQA 8:1, 192 total KV heads, head_dim=128

### PPL
| Method | WikiText-2 PPL | Delta vs Uniform |
|--------|---------|---------|
| Baseline (bf16) | 7.0157 | — |
| MCKP (k=8) | 7.3129 | **-0.0958** |
| Uniform 4-bit | 7.2171 | — |

**Verdict: FAIL** — MCKP 比 uniform 4-bit 还差 0.096，没有任何改善。

### Bit Distribution (k=8)
- 4-bit: 180 heads, 2-bit: 8 heads, 8-bit: 4 heads

### K Ablation
| k | PPL | n_2bit |
|---|-----|--------|
| 2 | **7.2209** | 2 |
| 4 | 7.2788 | 4 |
| 6 | 7.2874 | 6 |
| 8 | 7.3129 | 8 |
| 10 | 7.4164 | 10 |
| 12 | 7.5869 | 12 |
| 14 | 7.6612 | 14 |
| 16 | 7.6925 | 16 |

Best k=2 (PPL=7.2209)，但仍不如 uniform 4-bit（7.2171）。PPL 随 k 单调递增——更多 2-bit heads 只会更差。

### Heterogeneity Analysis (Claim 3 相关)
- **Top-5% concentration: 0.4934** (9 heads / 192 total)
- CV of delta(2bit): 4.7938
- Layer 0 dominance ratio: 0.07x (layer 0 反而是最不敏感的)
- All 192 heads have positive delta
- Most sensitive head: **L4H3** (delta_2bit = +5.6523，极端异常值)

### 与其他模型对比
| Model | GQA Ratio | Top-5% Conc. | MCKP vs Uniform | Verdict |
|-------|-----------|-------------|-----------------|---------|
| Qwen2.5-7B | 7:1 | ~0.42 (std) / ~0.59 (hires) | PASS | PASS |
| Yi-1.5-9B | 8:1 | **0.4934** | -0.096 | FAIL |

Yi 的 top-5% concentration (0.4934) 确实比 Qwen standard 的 ~0.42 更高，符合"高 GQA ratio → 高 heterogeneity"的趋势。但 MCKP 无法利用这个 heterogeneity——因为 sensitivity 过度集中在少数 outlier heads（L4H3 贡献了 delta_2bit 总量的极大比例），使得 MCKP 的 2-bit allocation 几乎无处可用而不严重损害质量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_gpu_yi15_phase5_fix_rerun_20260514T182903"
}
```

</details>

---
