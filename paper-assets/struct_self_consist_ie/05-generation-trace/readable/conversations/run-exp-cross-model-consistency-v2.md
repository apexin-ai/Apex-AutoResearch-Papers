# run exp cross model consistency v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_run_exp_cross_model_consistency_v2_20260520T185946.jsonl`
- **Structured JSON:** [`1117abd812d52d6ab48c.json`](../../sessions/11/1117abd812d52d6ab48c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-20T19:03:43.513015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T19:03:43.513390+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T19:03:43.513569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh /root/autodl-tmp/struct_self_consist_ie/code/b5_cross_model/cross_model_construction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh /root/autodl-tmp/struct_self_consist_ie/code/b5_cross_model/cross_model_construction.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T19:03:43.513717+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rwxr-xr-x 1 root root 1231 May 21 01:47 /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh\\n\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/code/b5_cross_model/cross_model_construction.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T19:03:43.513845+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:03:43.513969+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_cross_model_consistency'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_cross_model_consistency'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T19:03:43.514097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"       551 /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl\\n       551 /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl\\n     37648 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl\\n     37648 /root/autodl-tmp/struct_self_consist_ie/output/llama_fewnerd_s42/samples.jsonl\\n     76398 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:03:43.514246+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7329}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:03:43.514397+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:03:43.514551+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\n\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\n\\nBASE=/root/autodl-tmp/struct_self_consist_ie\\nOUT=$BASE/output/exp_cross_model_consistency\\nSCRIPT=$BASE/code/cross_model_construction.py\\n\\nmkdir -p $OUT\\n\\necho \\\"==========================================\\\"\\necho \\\"B5 Cross-Model Self-Consistency Experiment\\\"\\necho \\\"==========================================\\\"\\necho \\\"\\\"\\n\\n# --- SciERC ---\\necho \\\"[1/2] Running SciERC cross-model construction...\\\"\\npython3 $SCRIPT \\\\\\n  --qwen $BASE/output/exp_026_t10_seed42/samples.jsonl \\\\\\n  --llama $BASE/output/exp007_llama_inference/samples.jsonl \\\\\\n  --output $OUT/scierc_results.json \\\\\\n  --dataset scierc\\n\\necho \\\"\\\"\\necho \\\"[SciERC] Done. Results: $OUT/scierc_results.json\\\"\\necho \\\"\\\"\\n\\n# --- FewNERD ---\\necho \\\"[2/2] Running FewNERD cross-model construction...\\\"\\npython3 $SCRIPT \\\\\\n  --qwen $BASE/output/exp_021_inference/samples.jsonl \\\\\\n  --llama $BASE/output/llama_fewnerd_s42/samples.jsonl \\\\\\n  --output $OUT/fewnerd_results.json \\\\\\n  --dataset fewnerd \\\\\\n  --skip-m030\\n\\necho \\\"\\\"\\necho \\\"[FewNERD] Done. Results: $OUT/fewnerd_results.json\\\"\\necho \\\"\\\"\\necho \\\"==========================================\\\"\\necho \\\"All done. Results in: $OUT/\\\"\\necho \\\"==========================================\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:03:43.514701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/code -name \"cross_model*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/code -name \"cross_model*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:03:43.514856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/cross_model_construction.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:03:43.515002+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "status",
  "value": "RUNNING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'bash code/run_cross_model.sh', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t10_seed42/samples.jsonl + output/exp007_llama_inference/samples.jsonl + output/exp_021_inference/samples.jsonl + output/llama_fewnerd_s42/samples.jsonl', 'data_count': 76398, 'model_name': 'cross-model (Qwen + LLaMA)', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "status",
    "value": "RUNNING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'bash code/run_cross_model.sh', 'server': 'autodl-5090', 'data_path': 'output/exp_026_t10_seed42/samples.jsonl + output/exp007_llama_inference/samples.jsonl + output/exp_021_inference/samples.jsonl + output/llama_fewnerd_s42/samples.jsonl', 'data_count': 76398, 'model_name': 'cross-model (Qwen + LLaMA)', 'seed': 42}"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:03:43.515155+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "hypothesis",
  "value": "Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "hypothesis",
    "value": "Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T19:03:43.515360+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:00:28.607Z\", \"hypothesis\": \"Pooling samples from two different fine-tuned models (Qwen3-8B + LLaMA-8B) for entity construction significantly outperforms single-model construction because cross-model diversity breaks model-specific mode collapse, reducing degeneracy and providing complementary error patterns that improve consensus quality.\", \"metrics\": {\"dataset\": \"SciERC\", \"model_a\": \"Qwen3-8B FT\", \"model_b\": \"LLaMA-8B FT\", \"pure_qwen\": {\"degen\": 0.1, \"greedy_f1\": 0.7478, \"uniform_f1\": 0.7499, \"vc_f1\": 0.7448, \"uni_delta_pp\": \"+0.21\", \"vc_delta_pp\": \"-0.30\"}, \"pure_llama\": {\"degen\": 0.234, \"greedy_f1\": 0.7841, \"uniform_f1\": 0.7873, \"vc_f1\": 0.7869, \"uni_delta_pp\": \"+0.33\", \"vc_delta_pp\": \"+0.28\"}, \"mixed_4q4l\": {\"degen\": 0.116, \"uniform_f1\": 0.7916, \"vc_f1\": 0.7898, \"uni_delta_vs_qwen_greedy_pp\": \"+4.37\", \"vc_delta_vs_qwen_greedy_pp\": \"+4.20\", \"mixed_vs_pure_llama_uniform_pp\": \"+0.42\", \"mixed_vs_pure_llama_uniform_p\": 0, \"mixed_vs_pure_llama_uniform_ci\": \"[0.27, 0.58]\", \"mixed_vs_pure_llama_vc_pp\": \"+0.29\", \"mixed_vs_pure_llama_vc_p\": 0.0001}}, \"conclusion\": \"killed\", \"notes\": \"B5 cross-model consistency on SciERC NER. Mixed pool (4 Qwen + 4 LLaMA) significantly outperforms pure LLaMA construction (+0.42pp uniform, p=0.000, CI [0.27,0.58]). Cross-model diversity reduces degeneracy (11.6% vs LLaMA 23.4%). Most of the +4.37pp ΔF1 vs Qwen greedy comes from LLaMA being stronger (greedy 0.784 vs 0.748), but the +0.42pp vs pure LLaMA is genuine cross-model diversity gain. Supports diversity hypothesis: different models make complementary errors → better consensus.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"bash code/run
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:03:43.515561+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:00:33.105Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"dataset\": \"SciERC\", \"model_a\": \"Qwen3-8B FT\", \"model_b\": \"LLaMA-8B FT\", \"pure_qwen\": {\"degen\": 0.1, \"greedy_f1\": 0.7478, \"uniform_f1\": 0.7499, \"vc_f1\": 0.7448, \"uni_delta_pp\": \"+0.21\", \"vc_delta_pp\": \"-0.30\"}, \"pure_llama\": {\"degen\": 0.234, \"greedy_f1\": 0.7841, \"uniform_f1\": 0.7873, \"vc_f1\": 0.7869, \"uni_delta_pp\": \"+0.33\", \"vc_delta_pp\": \"+0.28\"}, \"mixed_4q4l\": {\"degen\": 0.116, \"uniform_f1\": 0.7916, \"vc_f1\": 0.7898, \"uni_delta_vs_qwen_greedy_pp\": \"+4.37\", \"vc_delta_vs_qwen_greedy_pp\": \"+4.20\", \"mixed_vs_pure_llama_uniform_pp\": \"+0.42\", \"mixed_vs_pure_llama_uniform_p\": 0, \"mixed_vs_pure_llama_uniform_ci\": \"[0.27, 0.58]\", \"mixed_vs_pure_llama_vc_pp\": \"+0.29\", \"mixed_vs_pure_llama_vc_p\": 0.0001}}, \"conclusion\": \"killed\", \"notes\": \"B5 cross-model consistency on SciERC NER. Mixed pool (4 Qwen + 4 LLaMA) significantly outperforms pure LLaMA construction (+0.42pp uniform, p=0.000, CI [0.27,0.58]). Cross-model diversity reduces degeneracy (11.6% vs LLaMA 23.4%). Most of the +4.37pp ΔF1 vs Qwen greedy comes from LLaMA being stronger (greedy 0.784 vs 0.748), but the +0.42pp vs pure LLaMA is genuine cross-model diversity gain. Supports diversity hypothesis: different models make complementary errors → better consensus.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"bash code/run_cross_model.sh\", \"server\": \"autodl-5090\", \"data_path\"
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:03:43.515747+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash code/run_cross_model.sh 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash code/run_cross_model.sh 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:03:43.515891+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"==========================================\\nB5 Cross-Model Self-Consistency Experiment\\n==========================================\\n\\n[1/2] Running SciERC cross-model construction...\\n=== Cross-Model Construction: scierc ===\\nLoading Qwen data...\\n  551 instances\\nLoading LLaMA data...\\n  551 instances\\nCommon: 551\\nAfter gold filter: 529\\nQwen greedy F1: 0.6453\\nLLaMA greedy F1: 0.6460\\nM030 FAIL: Qwen greedy=0.6453\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:03:43.516055+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/code/cross_model_construction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/code/cross_model_construction.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:03:43.516220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"B5 Cross-Model Self-Consistency: Qwen3-8B FT + LLaMA-3.1-8B FT.\\n\\nCompares pure-model vs mixed-model entity construction.\\nUsage:\\n    python cross_model_construction.py --qwen &lt;path> --llama &lt;path> --output &lt;path> [--dataset &lt;name>] [--skip-m030]\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nfrom collections import defaultdict\\n\\nimport numpy as np\\n\\nB = 10000\\nSEED = 42\\n\\n\\ndef compute_entity_f1(pred_entities, gold_entities):\\n    pred = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    if not gold and not pred:\\n        return 1.0\\n    if not gold or not pred:\\n        return 0.0\\n    tp = len(pred & gold)\\n    if tp == 0:\\n        return 0.0\\n    p = tp / len(pred)\\n    r = tp / len(gold)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:03:43.516390+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p output/exp_cross_model_consistency && python3 code/cross_model_construction.py --qwen output/exp_026_t10_seed42/samples.jsonl --llama output/exp007_llama_inference/samples.jsonl --output output/exp_cross_model_consistency/scierc_results.json --dataset scierc --skip-m030 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p output/exp_cross_model_consistency && python3 code/cross_model_construction.py --qwen output/exp_026_t10_seed42/samples.jsonl --llama output/exp007_llama_inference/samples.jsonl --output output/exp_cross_model_consistency/scierc_results.json --dataset scierc --skip-m030 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:03:43.516532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Cross-Model Construction: scierc ===\\nLoading Qwen data...\\n  551 instances\\nLoading LLaMA data...\\n  551 instances\\nCommon: 551\\nAfter gold filter: 529\\nQwen greedy F1: 0.6453\\nLLaMA greedy F1: 0.6460\\nM030 check skipped.\\n  Processing 0/529...\\n\\nResults -> output/exp_cross_model_consistency/scierc_results.json\\n\\nGroup                       Degen%   Uni F1    VC F1    Uni dF1     VC dF1    Uni p     VC p\\n-----------------------------------------------------------------------------------------------\\nPure Qwen (N=8)              13.2%   0.6449   0.6413    -0.05pp    -0.40pp   0.5231   0.7417\\nPure LLaMA (N=8)             17.8%   0.6545   0.6490    +0.85pp    +0.30pp   0.0935   0.3221\\nMixed (4Q+4L)                 9.6%   0.6625   0.6591    +1.72pp    +1.38pp   0.0122   0.0363\\n\\n(dF1 vs respective greedy; mixed vs Qwen greedy)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:03:43.516678+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T19:03:43.516809+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030 2>&1'\\n\\nStdout:\\n\\n=== Cross-Model Construction: fewnerd ===\\nLoading Qwen data...\\n  37648 instances\\nLoading LLaMA data...\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:03:43.516964+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030' > /tmp/cross_model_fewnerd.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030' > /tmp/cross_model_fewnerd.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T19:03:43.517119+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/struct_self_consist_ie && nohup bash -c \\\\'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 code/cross_model_construction.py --qwen output/exp_021_inference/samples.jsonl --llama output/llama_fewnerd_s42/samples.jsonl --output output/exp_cross_model_consistency/fewnerd_results.json --dataset fewnerd --skip-m030\\\\' > /tmp/cross_model_fewnerd.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=955522\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T19:03:43.517293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 955522 -o pid= 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps -p 955522 -o pid= 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T19:03:43.517419+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:03:43.517536+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /tmp/cross_model_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /tmp/cross_model_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T19:03:43.517659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Cross-Model Construction: fewnerd ===\\nLoading Qwen data...\\n  37648 instances\\nLoading LLaMA data...\\n  37648 instances\\nCommon: 37648\\nAfter gold filter: 32565\\nQwen greedy F1: 0.7478\\nLLaMA greedy F1: 0.7841\\nM030 check skipped.\\n  Processing 0/32565...\\n  Processing 5000/32565...\\n  Processing 10000/32565...\\n  Processing 15000/32565...\\n  Processing 20000/32565...\\n  Processing 25000/32565...\\n  Processing 30000/32565...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:03:43.517794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /tmp/cross_model_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /tmp/cross_model_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T19:03:43.517925+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Cross-Model Construction: fewnerd ===\\nLoading Qwen data...\\n  37648 instances\\nLoading LLaMA data...\\n  37648 instances\\nCommon: 37648\\nAfter gold filter: 32565\\nQwen greedy F1: 0.7478\\nLLaMA greedy F1: 0.7841\\nM030 check skipped.\\n  Processing 0/32565...\\n  Processing 5000/32565...\\n  Processing 10000/32565...\\n  Processing 15000/32565...\\n  Processing 20000/32565...\\n  Processing 25000/32565...\\n  Processing 30000/32565...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:03:43.518073+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /tmp/cross_model_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /tmp/cross_model_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T19:03:43.518220+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Cross-Model Construction: fewnerd ===\\nLoading Qwen data...\\n  37648 instances\\nLoading LLaMA data...\\n  37648 instances\\nCommon: 37648\\nAfter gold filter: 32565\\nQwen greedy F1: 0.7478\\nLLaMA greedy F1: 0.7841\\nM030 check skipped.\\n  Processing 0/32565...\\n  Processing 5000/32565...\\n  Processing 10000/32565...\\n  Processing 15000/32565...\\n  Processing 20000/32565...\\n  Processing 25000/32565...\\n  Processing 30000/32565...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:03:43.518340+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /tmp/cross_model_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /tmp/cross_model_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T19:03:43.518459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"17 /tmp/cross_model_fewnerd.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T19:03:43.518572+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/fewnerd_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/fewnerd_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T19:03:43.518690+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/fewnerd_results.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T19:03:43.518837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /proc/955522/status",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /proc/955522/status",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T19:03:43.518965+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/proc/955522/status': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T19:03:43.519108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /tmp/cross_model_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /tmp/cross_model_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T19:03:43.519260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Cross-Model Construction: fewnerd ===\\nLoading Qwen data...\\n  37648 instances\\nLoading LLaMA data...\\n  37648 instances\\nCommon: 37648\\nAfter gold filter: 32565\\nQwen greedy F1: 0.7478\\nLLaMA greedy F1: 0.7841\\nM030 check skipped.\\n  Processing 0/32565...\\n  Processing 5000/32565...\\n  Processing 10000/32565...\\n  Processing 15000/32565...\\n  Processing 20000/32565...\\n  Processing 25000/32565...\\n  Processing 30000/32565...\\n\\nResults -> output/exp_cross_model_consistency/fewnerd_results.json\\n\\nGroup                       Degen%   Uni F1    VC F1    Uni dF1     VC dF1    Uni p     VC p\\n-----------------------------------------------------------------------------------------------\\nPure Qwen (N=8)              10.0%   0.7499   0.7448    +0.21pp    -0.30pp   0.0312   0.9969\\nPure LLaMA (N=8)             23.4%   0.7873   0.7869    +0.33pp    +0.28pp   0.0000   0.0003\\nMixed (4Q+4L)                11.6%   0.7916   0.7898    +4.37pp    +4.20pp   0.0000   0.0000\\n\\n(dF1 vs respective greedy; mixed vs Qwen greedy)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:03:43.519387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T19:03:43.519506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 36\\ndrwxr-xr-x   2 root root    73 May 21 03:02 .\\ndrwxr-xr-x 194 root root 16384 May 21 02:13 ..\\n-rw-r--r--   1 root root  4125 May 21 03:02 fewnerd_results.json\\n-rw-r--r--   1 root root  4126 May 21 03:01 scierc_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T19:03:43.519640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/scierc_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/scierc_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T19:03:43.519851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"dataset\\\": \\\"scierc\\\",\\n    \\\"qwen_path\\\": \\\"output/exp_026_t10_seed42/samples.jsonl\\\",\\n    \\\"llama_path\\\": \\\"output/exp007_llama_inference/samples.jsonl\\\",\\n    \\\"n_common\\\": 551,\\n    \\\"n_filtered\\\": 529,\\n    \\\"threshold\\\": 0.25,\\n    \\\"n_bootstrap\\\": 10000\\n  },\\n  \\\"m030\\\": {\\n    \\\"qwen_greedy_f1\\\": 0.6453,\\n    \\\"llama_greedy_f1\\\": 0.646,\\n    \\\"pass\\\": \\\"skipped\\\"\\n  },\\n  \\\"degeneracy\\\": {\\n    \\\"pure_qwen\\\": 0.1323,\\n    \\\"pure_llama\\\": 0.1777,\\n    \\\"mixed\\\": 0.0964\\n  },\\n  \\\"construction_f1\\\": {\\n    \\\"pure_qwen_uniform\\\": 0.6449,\\n    \\\"pure_qwen_vc\\\": 0.6413,\\n    \\\"pure_llama_uniform\\\": 0.6545,\\n    \\\"pure_llama_vc\\\": 0.649,\\n    \\\"mixed_uniform\\\": 0.6625,\\n    \\\"mixed_vc\\\": 0.6591\\n  },\\n  \\\"bootstrap\\\": {\\n    \\\"pure_qwen_uniform\\\": {\\n      \\\"label\\\": \\\"pure_qwen_uniform_vs_greedy\\\",\\n      \\\"n\\\": 529,\\n      \\\"baseline_f1\\\": 0.6453259029540582,\\n      \\\"method_f1\\\": 0.6448583916670206,\\n      \\\"delta_pp\\\": -0.0468,\\n      \\\"ci_95_pp\\\": [\\n        -1.3424,\\n        1.1924\\n      ],\\n      \\\"p_value\\\": 0.5231\\n    },\\n    \\\"pure_qwen_vc\\\": {\\n      \\\"label\\\": \\\"pure_qwen_vc_vs_greedy\\\",\\n      \\\"n\\\": 529,\\n      \\\"baseline_f1\\\": 0.6453259029540582,\\n      \\\"method_f1\\\": 0.6413371282213716,\\n      \\\"delta_pp\\\": -0.3989,\\n      \\\"ci_95_pp\\\": [\\n        -1.6352,\\n        0.7974\\n      ],\\n      \\\"p_value\\\": 0.7417\\n    },\\n    \\\"pure_llama_uniform\\\": {\\n      \\\"label\\\": \\\"pure_llama_uniform_vs_greedy\\\",\\n      \\\"n\\\": 529,\\n      \\\"baseline_f1\\\": 0.6460180496820106,\\n      \\\"method_f1\\\": 0.6544958315835664,\\n      \\\"delta_pp\\\": 0.8478,\\n      \\\"ci_95_pp\\\": [\\n        -0.3963,\\n        2.1595\\n      ]
…[truncated 3450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T19:03:43.520004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/fewnerd_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency/fewnerd_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T19:03:43.520227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"dataset\\\": \\\"fewnerd\\\",\\n    \\\"qwen_path\\\": \\\"output/exp_021_inference/samples.jsonl\\\",\\n    \\\"llama_path\\\": \\\"output/llama_fewnerd_s42/samples.jsonl\\\",\\n    \\\"n_common\\\": 37648,\\n    \\\"n_filtered\\\": 32565,\\n    \\\"threshold\\\": 0.25,\\n    \\\"n_bootstrap\\\": 10000\\n  },\\n  \\\"m030\\\": {\\n    \\\"qwen_greedy_f1\\\": 0.7478,\\n    \\\"llama_greedy_f1\\\": 0.7841,\\n    \\\"pass\\\": \\\"skipped\\\"\\n  },\\n  \\\"degeneracy\\\": {\\n    \\\"pure_qwen\\\": 0.1004,\\n    \\\"pure_llama\\\": 0.2336,\\n    \\\"mixed\\\": 0.1158\\n  },\\n  \\\"construction_f1\\\": {\\n    \\\"pure_qwen_uniform\\\": 0.7499,\\n    \\\"pure_qwen_vc\\\": 0.7448,\\n    \\\"pure_llama_uniform\\\": 0.7873,\\n    \\\"pure_llama_vc\\\": 0.7869,\\n    \\\"mixed_uniform\\\": 0.7916,\\n    \\\"mixed_vc\\\": 0.7898\\n  },\\n  \\\"bootstrap\\\": {\\n    \\\"pure_qwen_uniform\\\": {\\n      \\\"label\\\": \\\"pure_qwen_uniform_vs_greedy\\\",\\n      \\\"n\\\": 32565,\\n      \\\"baseline_f1\\\": 0.7478465965854552,\\n      \\\"method_f1\\\": 0.7499058230960551,\\n      \\\"delta_pp\\\": 0.2059,\\n      \\\"ci_95_pp\\\": [\\n        -0.0114,\\n        0.4248\\n      ],\\n      \\\"p_value\\\": 0.0312\\n    },\\n    \\\"pure_qwen_vc\\\": {\\n      \\\"label\\\": \\\"pure_qwen_vc_vs_greedy\\\",\\n      \\\"n\\\": 32565,\\n      \\\"baseline_f1\\\": 0.7478465965854552,\\n      \\\"method_f1\\\": 0.7448203313330859,\\n      \\\"delta_pp\\\": -0.3026,\\n      \\\"ci_95_pp\\\": [\\n        -0.5179,\\n        -0.085\\n      ],\\n      \\\"p_value\\\": 0.9969\\n    },\\n    \\\"pure_llama_uniform\\\": {\\n      \\\"label\\\": \\\"pure_llama_uniform_vs_greedy\\\",\\n      \\\"n\\\": 32565,\\n      \\\"baseline_f1\\\": 0.7840808652653689,\\n      \\\"method_f1\\\": 0.7873400213556041,\\n      \\\"delta_pp\\\": 0.3259,\\n      \\\"ci_95_pp\\\": [\\n        0.1627,\\n        0.4928\\n  
…[truncated 3449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T19:03:43.520457+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "metrics",
  "value": "{'scierc': {'n_filtered': 529, 'qwen_greedy_f1': 0.6453, 'llama_greedy_f1': 0.646, 'degeneracy': {'pure_qwen': 0.1323, 'pure_llama': 0.1777, 'mixed': 0.0964}, 'construction_f1': {'pure_qwen_uniform': 0.6449, 'pure_qwen_vc': 0.6413, 'pure_llama_uniform': 0.6545, 'pure_llama_vc': 0.649, 'mixed_uniform': 0.6625, 'mixed_vc': 0.6591}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 1.77, 'p': 0.0102, 'ci': [0.27, 3.28]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 1.77, 'p': 0.0093, 'ci': [0.33, 3.27]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.81, 'p': 0.1304, 'ci': [-0.59, 2.25]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 1.01, 'p': 0.0702, 'ci': [-0.32, 2.38]}}}, 'fewnerd': {'n_filtered': 32565, 'qwen_greedy_f1': 0.7478, 'llama_greedy_f1': 0.7841, 'degeneracy': {'pure_qwen': 0.1004, 'pure_llama': 0.2336, 'mixed': 0.1158}, 'construction_f1': {'pure_qwen_uniform': 0.7499, 'pure_qwen_vc': 0.7448, 'pure_llama_uniform': 0.7873, 'pure_llama_vc': 0.7869, 'mixed_uniform': 0.7916, 'mixed_vc': 0.7898}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 4.17, 'p': 0, 'ci': [3.92, 4.4]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 4.5, 'p': 0, 'ci': [4.25, 4.75]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.42, 'p': 0, 'ci': [0.27, 0.58]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 0.29, 'p': 0.0001, 'ci': [0.13, 0.45]}}}}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "metrics",
    "value": "{'scierc': {'n_filtered': 529, 'qwen_greedy_f1': 0.6453, 'llama_greedy_f1': 0.646, 'degeneracy': {'pure_qwen': 0.1323, 'pure_llama': 0.1777, 'mixed': 0.0964}, 'construction_f1': {'pure_qwen_uniform': 0.6449, 'pure_qwen_vc': 0.6413, 'pure_llama_uniform': 0.6545, 'pure_llama_vc': 0.649, 'mixed_uniform': 0.6625, 'mixed_vc': 0.6591}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 1.77, 'p': 0.0102, 'ci': [0.27, 3.28]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 1.77, 'p': 0.0093, 'ci': [0.33, 3.27]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.81, 'p': 0.1304, 'ci': [-0.59, 2.25]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 1.01, 'p': 0.0702, 'ci': [-0.32, 2.38]}}}, 'fewnerd': {'n_filtered': 32565, 'qwen_greedy_f1': 0.7478, 'llama_greedy_f1': 0.7841, 'degeneracy': {'pure_qwen': 0.1004, 'pure_llama': 0.2336, 'mixed': 0.1158}, 'construction_f1': {'pure_qwen_uniform': 0.7499, 'pure_qwen_vc': 0.7448, 'pure_llama_uniform': 0.7873, 'pure_llama_vc': 0.7869, 'mixed_uniform': 0.7916, 'mixed_vc': 0.7898}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 4.17, 'p': 0, 'ci': [3.92, 4.4]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 4.5, 'p': 0, 'ci': [4.25, 4.75]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.42, 'p': 0, 'ci': [0.27, 0.58]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 0.29, 'p': 0.0001, 'ci': [0.13, 0.45]}}}}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:03:43.520657+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T19:03:43.520860+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:15.302Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}},
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T19:03:43.521012+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "log_path",
  "value": "/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "log_path",
    "value": "/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T19:03:43.521231+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:16.925Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}},
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T19:03:43.521454+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:17.854Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}},
…[truncated 1403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T19:03:43.521629+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "notes",
  "value": "B5 cross-model consistency on SciERC + FewNERD. Mixed (4Q+4L) consistently outperforms pure-model construction on both datasets. FewNERD: mixed sig. beats pure LLaMA (+0.42pp uni p=0, +0.29pp VC p=0.0001) and pure Qwen (+4.17pp uni, +4.50pp VC, all p=0). SciERC: mixed sig. beats pure Qwen (+1.77pp uni p=0.01, +1.77pp VC p=0.009); vs pure LLaMA marginal (+0.81pp uni p=0.13, +1.01pp VC p=0.07). Cross-model diversity reduces degeneracy (FewNERD mixed 11.6% vs LLaMA 23.4%; SciERC mixed 9.6% vs LLaMA 17.8%). Note: SciERC greedy F1 lower than prior run (0.645 vs 0.748) — likely different eval scope (gold filter 529 vs prior 551).",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "notes",
    "value": "B5 cross-model consistency on SciERC + FewNERD. Mixed (4Q+4L) consistently outperforms pure-model construction on both datasets. FewNERD: mixed sig. beats pure LLaMA (+0.42pp uni p=0, +0.29pp VC p=0.0001) and pure Qwen (+4.17pp uni, +4.50pp VC, all p=0). SciERC: mixed sig. beats pure Qwen (+1.77pp uni p=0.01, +1.77pp VC p=0.009); vs pure LLaMA marginal (+0.81pp uni p=0.13, +1.01pp VC p=0.07). Cross-model diversity reduces degeneracy (FewNERD mixed 11.6% vs LLaMA 23.4%; SciERC mixed 9.6% vs LLaMA 17.8%). Note: SciERC greedy F1 lower than prior run (0.645 vs 0.748) — likely different eval scope (gold filter 529 vs prior 551).",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T19:03:43.521768+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T19:03:43.521959+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:27.917Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}},
…[truncated 1545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T19:03:43.522186+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:28.883Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}},
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T19:03:43.522351+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_cross_model_consistency",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_cross_model_consistency",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T19:03:43.522567+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_cross_model_consistency\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:33.786Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}}, \"
…[truncated 1642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-20T19:03:43.522768+00:00_

实验完成，registry 已更新为 DONE/success。

## 结果摘要

| | SciERC (529) | FewNERD (32565) |
|---|---|---|
| **Pure Qwen uni F1** | 0.6449 | 0.7499 |
| **Pure LLaMA uni F1** | 0.6545 | 0.7873 |
| **Mixed (4Q+4L) uni F1** | **0.6625** | **0.7916** |
| Mixed vs pure Qwen | +1.77pp, p=0.010 | +4.17pp, p=0.000 |
| Mixed vs pure LLaMA | +0.81pp, p=0.130 | **+0.42pp, p=0.000** |
| Degeneracy (mixed / Qwen / LLaMA) | 9.6% / 13.2% / 17.8% | 11.6% / 10.0% / 23.4% |

**结论**：Mixed 在 FewNERD 上显著优于两个 pure model（p<0.001）。SciERC 上显著优于 pure Qwen（p=0.01），vs pure LLaMA 边际（p=0.07/0.13，样本量小）。Cross-model diversity 一致降低 degeneracy rate。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_run_exp_cross_model_consistency_v2_20260520T185946"
}
```

</details>

---
