# analysis arc easy per example full

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_analysis_arc-easy-per-example-full_20260520T092702.jsonl`
- **Structured JSON:** [`aa54caa747755f2a5367.json`](../../sessions/aa/aa54caa747755f2a5367.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-20T09:35:58.392981+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T09:35:58.393313+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:35:58.393484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -5 /root/entrainment_gated_ft/lm_eval_clean/arc_easy/GatedDeltaNet_1.3b_pure/samples/arc_easy.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -5 /root/entrainment_gated_ft/lm_eval_clean/arc_easy/GatedDeltaNet_1.3b_pure/samples/arc_easy.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T09:35:58.393619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/arc_easy/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/arc_easy/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:35:58.393789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T09:35:58.393925+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/entrainment_gated_ft/lm_eval_clean/arc_easy/GatedDeltaNet_1.3b_pure/samples/arc_easy.jsonl' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 2.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T09:35:58.394063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.3B-100B-GatedDeltaNet-hybrid-12-1\\n1.3B-100B-GatedDeltaNet-hybrid-12-1_eval.log\\n1.3B-100B-GatedDeltaNet-hybrid-24-1\\n1.3B-100B-GatedDeltaNet-hybrid-24-1_eval.log\\n1.3B-100B-GatedDeltaNet-hybrid-3-1\\n1.3B-100B-GatedDeltaNet-hybrid-3-1_eval.log\\n1.3B-100B-GatedDeltaNet-hybrid-6-1\\n1.3B-100B-GatedDeltaNet-hybrid-6-1_eval.log\\n1.3B-100B-GatedDeltaNet-pure\\n1.3B-100B-GatedDeltaNet-pure_eval.log\\n1.3B-100B-HGRN2-hybrid-12-1\\n1.3B-100B-HGRN2-hybrid-12-1_eval.log\\n1.3B-100B-HGRN2-hybrid-24-1\\n1.3B-100B-HGRN2-hybrid-24-1_eval.log\\n1.3B-100B-HGRN2-hybrid-3-1\\n1.3B-100B-HGRN2-hybrid-3-1_eval.log\\n1.3B-100B-HGRN2-hybrid-6-1\\n1.3B-100B-HGRN2-hybrid-6-1_eval.log\\n1.3B-100B-HGRN2-pure\\n1.3B-100B-HGRN2-pure_eval.log\\n1.3B-100B-RetNet-hybrid-12-1\\n1.3B-100B-RetNet-hybrid-12-1_eval.log\\n1.3B-100B-RetNet-hybrid-24-1\\n1.3B-100B-RetNet-hybrid-24-1_eval.log\\n1.3B-100B-RetNet-hybrid-3-1\\n1.3B-100B-RetNet-hybrid-3-1_eval.log\\n1.3B-100B-RetNet-hybrid-6-1\\n1.3B-100B-RetNet-hybrid-6-1_eval.log\\n1.3B-100B-RetNet-pure\\n1.3B-100B-RetNet-pure_eval.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T09:35:58.394210+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.3B-100B-GatedDeltaNet-hybrid-12-1.json\\n1.3B-100B-GatedDeltaNet-hybrid-12-1_final.log\\n1.3B-100B-GatedDeltaNet-hybrid-24-1_results.json\\n1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json\\n1.3B-100B-GatedDeltaNet-hybrid-6-1_results.json\\n1.3B-100B-GatedDeltaNet-pure.json\\n1.3B-100B-GatedDeltaNet-pure.log\\n1.3B-100B-GatedDeltaNet-pure_final.log\\n1.3B-100B-GatedDeltaNet-pure_lambada_only.json\\n1.3B-100B-GatedDeltaNet-pure_results.json\\n1.3B-100B-HGRN2-hybrid-12-1.json\\n1.3B-100B-HGRN2-hybrid-24-1.json\\n1.3B-100B-HGRN2-hybrid-3-1.json\\n1.3B-100B-HGRN2-hybrid-6-1.json\\n1.3B-100B-HGRN2-pure.json\\n1.3B-100B-RetNet-hybrid-12-1.json\\n1.3B-100B-RetNet-hybrid-24-1.json\\n1.3B-100B-RetNet-hybrid-3-1.json\\n1.3B-100B-RetNet-hybrid-6-1.json\\n1.3B-100B-RetNet-pure.json\\n1.3B-100B-RetNet-pure_final.log\\n1.3B-100B-RetNet-pure_results.json\\n1.3b\\n340m\\narc_easy\\ndebug\\neval_all.log\\neval_h24.log\\neval_remaining.log\\nexp007\\nexp011\\nfigures\\ngdn_pure_validation.log\\nhgrn2_debug.log\\nhgrn2_debug_lambada.log\\nmultiseed\\nremaining.log\\nretnet_hybrid12_eval.log\\nretnet_pure.log\\nretnet_pure_final.log\\nretnet_pure_v2.log\\nretnet_redownload_eval.log\\nretnet_reeval.log\\nsummary_all_1.3b.csv\\ntransformer_1.3B_baseline.json\\ntransformer_1.3B_baseline_final.log\\nvalidation.log\\nvalidation2.log\\nxstorycloze\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:35:58.394380+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/arc_easy/ -name \"*.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/arc_easy/ -name \"*.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T09:35:58.394508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"lambada_openai.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -name \"lambada_openai.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T09:35:58.394661+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-hybrid-24-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-hybrid-12-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-hybrid-6-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-hybrid-3-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-RetNet-pure/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-RetNet-hybrid-24-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-RetNet-hybrid-12-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-RetNet-hybrid-6-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-RetNet-hybrid-3-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-HGRN2-pure/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-HGRN2-hybrid-24-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-HGRN2-hybrid-12-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-HGRN2-hybrid-6-1/samples/arc_easy.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-HGRN2-hybrid-3-1/samples/arc_easy.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:35:58.394837+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/RetNet-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/RetNet-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/RetNet-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/RetNet-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/RetNet-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/HGRN2-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/HGRN2-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/HGRN2-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/HGRN2-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/HGRN2-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/Transformer/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_cl
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T09:35:58.395019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T09:35:58.395144+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:35:58.395260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T09:35:58.395458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"id\\\": \\\"Mercury_417466\\\", \\\"question\\\": \\\"Which statement best explains why photosynthesis is the foundation of most food webs?\\\", \\\"choices\\\": {\\\"text\\\": [\\\"Sunlight is the source of energy for nearly all ecosystems.\\\", \\\"Most ecosystems are found on land instead of in water.\\\", \\\"Carbon dioxide is more available than other gases.\\\", \\\"The producers in all ecosystems are plants.\\\"], \\\"label\\\": [\\\"A\\\", \\\"B\\\", \\\"C\\\", \\\"D\\\"]}, \\\"answerKey\\\": \\\"A\\\"}, \\\"target\\\": 0, \\\"arguments\\\": [[\\\"Question: Which statement best explains why photosynthesis is the foundation of most food webs?\\\\nAnswer:\\\", \\\" Sunlight is the source of energy for nearly all ecosystems.\\\"], [\\\"Question: Which statement best explains why photosynthesis is the foundation of most food webs?\\\\nAnswer:\\\", \\\" Most ecosystems are found on land instead of in water.\\\"], [\\\"Question: Which statement best explains why photosynthesis is the foundation of most food webs?\\\\nAnswer:\\\", \\\" Carbon dioxide is more available than other gases.\\\"], [\\\"Question: Which statement best explains why photosynthesis is the foundation of most food webs?\\\\nAnswer:\\\", \\\" The producers in all ecosystems are plants.\\\"]], \\\"resps\\\": [[[-20.5, false]], [[-29.0, false]], [[-23.875, false]], [[-23.375, false]]], \\\"filtered_resps\\\": [[-20.5, false], [-29.0, false], [-23.875, false], [-23.375, false]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"acc\\\", \\\"acc_norm\\\"], \\\"doc_hash\\\": \\\"b91fe1a8fdc40a80b9364f6256ac729d010ba076b02e75a362c2cf7ad3303bdf\\\", \\\"prompt_hash\\\": \\\"f804da9f5e214341d08d56228bb255177a0e5740f82e61b45887fcb5dc5c08ce\\\", \\\"target_hash\\\": \\\"5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9\\\", \\\"acc\\\": 1.0, \\\"acc_norm\\\": 1.0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\
…[truncated 1745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T09:35:58.395691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"text\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about signs\\\"}, \\\"target\\\": \\\" signs\\\", \\\"arguments\\\": [[\\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about\\\", \\\" signs\\\"]], \\\"resps\\\": [[[-1.828125, false]]], \\\"filtered_resps\\\": [[-1.828125, false]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"perplexity\\\", \\\"acc\\\"], \\\"doc_hash\\\": \\\"d5d2ee0c7bb2325b1a3b782dd2f946222c370109812c56acc7da70b662a6a60c\\\", \\\"prompt_hash\\\": \\\"8d638394e95544a75ea75bfa8cedd5fb71d5e65dfac9758cad35a0d5fa6e296c\\\", \\\"target_hash\\\": \\\"697dfd086e17614160f34474ccf8681ad12ae5839865fc979ac177eb5bba0a48\\\", \\\"perplexity\\\": -1.828125, \\\"acc\\\": 0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\": {\\\"text\\\": \\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. We won't be that long.\\\\\\\"\\\\n\\\\nShane gripped her arm and started leading her to the dock.\\\\n\\\\n\\\\\\\"I can make it there on my own, Shane\\\"}, \\\"target\\\": \\\" Shane\\\", \\\"arguments\\\": [[\\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. 
…[truncated 775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T09:35:58.395857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2376 /root/entrainment_gated_ft/lm_eval_clean/arc_easy/1.3B-100B-GatedDeltaNet-pure/samples/arc_easy.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T09:35:58.396011+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/1.3b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T09:35:58.396135+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T09:35:58.396254+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T09:35:58.396376+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"GDN-h24-1-logsamples\\nGDN-h3-1-logsamples\\nGDN-h6-1-logsamples\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T09:35:58.396499+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"GDN-h12-1\\nGDN-pure\\nHGRN2-h12-1\\nHGRN2-h24-1\\nHGRN2-h3-1\\nHGRN2-h6-1\\nHGRN2-pure\\nRetNet-h12-1\\nRetNet-h24-1\\nRetNet-h3-1\\nRetNet-h6-1\\nRetNet-pure\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.22}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T09:35:58.396615+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T09:35:58.396984+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat > /root/entrainment_gated_ft/per_example_analysis.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Full per-example analysis for ARC-Easy + LAMBADA (Parts A-F).\"\"\"\nimport json\nimport numpy as np\nfrom itertools import permutations as iterperms\n\nnp.random.seed(42)\n\nARCHS = [\"GDN\", \"RetNet\", \"HGRN2\"]\nRATIOS = [\"pure\", \"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"]\nHYBRID_RATIOS = [\"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"]\nARCH_PAIRS = [(\"GDN\", \"RetNet\"), (\"GDN\", \"HGRN2\"), (\"RetNet\", \"HGRN2\")]\nN_PERM = 10000\nOUT_DIR = \"/root/entrainment_gated_ft\"\n\n# === Paths ===\nARC_BASE = \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy\"\nARC_ARCH_MAP = {\"GDN\": \"GatedDeltaNet\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}\n\ndef arc_path(arch, ratio):\n    a = ARC_ARCH_MAP[arch]\n    if ratio == \"pure\":\n        return f\"{ARC_BASE}/1.3B-100B-{a}-pure/samples/arc_easy.jsonl\"\n    num = ratio.split(\"-\")[0][1:]\n    return f\"{ARC_BASE}/1.3B-100B-{a}-hybrid-{num}-1/samples/arc_easy.jsonl\"\n\nLAMB_EXP = \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b\"\nLAMB_EXTRA = \"/root/entrainment_gated_ft/lm_eval_clean/1.3b\"\n\ndef lambada_path(arch, ratio):\n    if arch == \"GDN\" and ratio in [\"h24-1\", \"h6-1\", \"h3-1\"]:\n        return f\"{LAMB_EXTRA}/GDN-{ratio}-logsamples/samples/lambada_openai.jsonl\"\n    name = {\"GDN\": \"GDN\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}[arch]\n    return f\"{LAMB_EXP}/{name}-{ratio}/samples/lambada_openai.jsonl\"\n\ndef load_jsonl(path):\n    data = []\n    with open(path) as f:\n        for line in f:\n            data.append(json.loads(line))\n    return data\n\n# === Load ===\nprint(\"Loading data...\")\narc_data = {}\nlambada_raw = {}\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        arc_data[(arch, ratio)] = load_jsonl(arc_path(arch, ratio))\n        lambada_raw[(arch, ratio)] = load_jsonl(lambada_path(arch, ratio))\n\nN_ARC = len(arc_data[(\"GDN\", \"pure\")])\nN_LAMB = len(lambada_raw[(\"GDN\", \"pure\")])\nprint(f\"ARC-Easy: {N_ARC}, LAMBADA: {N_LAMB}\")\n\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        assert len(arc_data[(arch, ratio)]) == N_ARC, f\"ARC mismatch {arch}/{ratio}: {len(arc_data[(arch,ratio)])} != {N_ARC}\"\n        assert len(lambada_raw[(arch, ratio)]) == N_LAMB, f\"LAMB mismatch {arch}/{ratio}: {len(lambada_raw[(arch,ratio)])} != {N_LAMB}\"\n\n# Verify doc_id alignment\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        for i in range(min(5, N_ARC)):\n            assert arc_data[(arch, ratio)][i][\"doc_id\"] == i, f\"ARC doc_id mismatch {arch}/{ratio} idx={i}\"\n        for i in range(min(5, N_LAMB)):\n            assert lambada_raw[(arch, ratio)][i][\"doc_id\"] == i, f\"LAMB doc_id mismatch {arch}/{ratio} idx={i}\"\n\n# Extract arrays\narc_accs = {}; arc_lp = {}\nlamb_accs = {}; lamb_lp = {}\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        s = arc_data[(arch, ratio)]\n        arc_accs[(arch, ratio)] = np.array([x[\"acc\"] for x in s])\n        arc_lp[(arch, ratio)] = np.array([x[\"filtered_resps\"][x[\"target\"]][0] for x in s])\n        s2 = lambada_raw[(arch, ratio)]\n        lamb_accs[(arch, ratio)] = np.array([float(x[\"acc\"]) for x in s2])\n        lamb_lp[(arch, ratio)] = np.array([x[\"filtered_resps\"][0][0] for x in s2])\n\nprint(\"\\nOverall accuracies:\")\nfor bname, ad in [(\"ARC\", arc_accs), (\"LAMB\", lamb_accs)]:\n    for arch in ARCHS:\n        vals = \" \".join(f\"{r}={np.mean(ad[(arch,r)]):.4f}\" for r in RATIOS)\n        print(f\"  {bname} {arch}: {vals}\")\n\n# ============ A. Per-Example Classification ============\nprint(\"\\n=== A. Per-Example Classification ===\")\npe = {}\nfor arch in ARCHS:\n    pe[arch] = {}\n    pure = arc_accs[(arch, \"pure\")]\n    for ratio in HYBRID_RATIOS:\n        hyb = arc_accs[(arch, ratio)]\n        h = int(np.sum((pure == 0) & (hyb == 1)))\n        r = int(np.sum((pure == 1) & (hyb == 0)))\n        sr = int(np.sum((pure == 1) & (hyb == 1)))\n        sw = int(np.sum((pure == 0) & (hyb == 0)))\n        pe[arch][ratio] = {\n            \"n_helped\": h, \"n_hurt\": r,\n            \"n_stayed_right\": sr, \"n_stayed_wrong\": sw,\n            \"net_effect\": h - r\n        }\n        print(f\"  {arch:6s} {ratio:5s}: helped={h:3d} hurt={r:3d} stayed_right={sr:4d} stayed_wrong={sw:4d} net={h-r:+d}\")\n\n# ============ B & C. Jaccard Analysis ============\nprint(\"\\n=== B & C. Jaccard Analysis ===\")\n\ndef jaccard(a, b):\n    u = a | b\n    return len(a & b) / len(u) if len(u) > 0 else 0.0\n\ndef get_sets(arch, ratio, accs):\n    p = accs[(arch, \"pure\")]\n    h = accs[(arch, ratio)]\n    helped = set(np.where((p == 0) & (h == 1))[0])\n    hurt = set(np.where((p == 1) & (h == 0))[0])\n    return helped, hurt\n\ndef j_null_calc(sA, sB, N):\n    ei = sA * sB / N\n    eu = sA + sB - ei\n    return ei / eu if eu > 0 else 0.0\n\ndef j_max_calc(sA, sB):\n    mn = min(sA, sB)\n    d = sA + sB - mn\n    return mn / d if d > 0 else 0.0\n\ndef perm_test(setA, setB, N, n_perm):\n    obs = jaccard(setA, setB)\n    la, lb = len(setA), len(setB)\n    if la == 0 or lb == 0:\n        return 1.0\n    cnt = 0\n    for _ in range(n_perm):\n        pa = set(np.random.choice(N, la, replace=False))\n        pb = set(np.random.choice(N, lb, replace=False))\n        if jaccard(pa, pb) >= obs:\n            cnt += 1\n    return cnt / n_perm\n\njacc = {}\njacc_null = {}\nfor ratio in HYBRID_RATIOS:\n    jacc[ratio] = {}\n    jacc_null[ratio] = {}\n    for a1, a2 in ARCH_PAIRS:\n        pk = f\"{a1}-{a2}\"\n        h1, r1 = get_sets(a1, ratio, arc_accs)\n        h2, r2 = get_sets(a2, ratio, arc_accs)\n        jh = jaccard(h1, h2)\n        jr = jaccard(r1, r2)\n        jacc[ratio][pk] = {\n            \"helped_jaccard\": round(jh, 4), \"hurt_jaccard\": round(jr, 4),\n            \"helped_sizes\": [len(h1), len(h2)], \"hurt_sizes\": [len(r1), len(r2)],\n            \"helped_intersection\": len(h1 & h2), \"hurt_intersection\": len(r1 & r2)\n        }\n        print(f\"  {ratio:5s} {pk:14s}: J_helped={jh:.4f}(|A|={len(h1)},|B|={len(h2)},∩={len(h1&h2)})  J_hurt={jr:.4f}(|A|={len(r1)},|B|={len(r2)},∩={len(r1&r2)})\")\n\n        for st, s1, s2 in [(\"helped\", h1, h2), (\"hurt\", r1, r2)]:\n            jo = jaccard(s1, s2)\n            jn = j_null_calc(len(s1), len(s2), N_ARC)\n            jm = j_max_calc(len(s1), len(s2))\n            nes = (jo - jn) / (jm - jn) if (jm - jn) > 1e-10 else 0.0\n            pv = perm_test(s1, s2, N_ARC, N_PERM)\n            jacc_null[ratio][f\"{pk}_{st}\"] = {\n                \"J_obs\": round(jo, 4), \"J_null\": round(jn, 4), \"J_max\": round(jm, 4),\n                \"normalized_ES\": round(nes, 4), \"p_value_permutation\": round(pv, 4),\n                \"n_permutations\": N_PERM, \"sizes\": [len(s1), len(s2)]\n            }\n            sig = \"***\" if pv < 0.001 else \"**\" if pv < 0.01 else \"*\" if pv < 0.05 else \"ns\"\n            print(f\"         {st:7s}: J_obs={jo:.4f} J_null={jn:.4f} J_max={jm:.4f} NES={nes:.4f} p={pv:.4f} {sig}\")\n\n# ============ D. Convergence sigma ============\nprint(\"\\n=== D. Convergence sigma ===\")\n\ndef spearman(x, y):\n    n = len(x)\n    rx = np.argsort(np.argsort(x)).astype(float)\n    ry = np.argsort(np.argsort(y)).astype(float)\n    d = rx - ry\n    return 1.0 - 6.0 * np.sum(d**2) / (n * (n**2 - 1))\n\nconv = {}\nmsigs = []\nfor ratio in RATIOS:\n    stack = np.stack([arc_accs[(a, ratio)] for a in ARCHS])\n    sig = np.std(stack, axis=0)\n    ms = float(np.mean(sig))\n    conv[ratio] = {\n        \"mean_sigma\": round(ms, 6),\n        \"median_sigma\": round(float(np.median(sig)), 6),\n        \"n_unanimous_correct\": int(np.sum(np.all(stack == 1, axis=0))),\n        \"n_unanimous_wrong\": int(np.sum(np.all(stack == 0, axis=0))),\n        \"n_split\": int(np.sum((np.sum(stack, axis=0) > 0) & (np.sum(stack, axis=0) < 3)))\n    }\n    msigs.append(ms)\n    print(f\"  {ratio:5s}: mean_sigma={ms:.6f} split={conv[ratio]['n_split']} unan_right={conv[ratio]['n_unanimous_correct']} unan_wrong={conv[ratio]['n_unanimous_wrong']}\")\n\nranks = np.arange(1, 6, dtype=float)\nmsigs_arr = np.array(msigs)\nrho = spearman(ranks, msigs_arr)\n\ncnt_rho = 0\ntot_rho = 0\nfor perm in iterperms(range(5)):\n    ps = msigs_arr[list(perm)]\n    r = spearman(ranks, ps)\n    if abs(r) >= abs(rho) - 1e-10:\n        cnt_rho += 1\n    tot_rho += 1\np_rho = cnt_rho / tot_rho\nconv[\"spearman\"] = {\"rho\": round(float(rho), 4), \"p_exact_two_tailed\": round(p_rho, 4), \"n_permutations\": tot_rho}\nprint(f\"  Spearman rho={rho:.4f}, p_exact={p_rho:.4f} (n_perm={tot_rho})\")\n\n# ============ E. Multiplicity Metrics ============\nprint(\"\\n=== E. Formal Predictive Multiplicity (Marx et al. 2020) ===\")\n\ndef compute_mult(accs_d, lp_d, N, name):\n    res = {}\n    for ratio in RATIOS:\n        stack = np.stack([accs_d[(a, ratio)] for a in ARCHS])\n        lps = np.stack([lp_d[(a, ratio)] for a in ARCHS])\n        nc = np.sum(stack, axis=0)\n        unan = (nc == 0) | (nc == 3)\n        alpha = float(1.0 - np.mean(unan))\n\n        ac_mask = (nc == 3)\n        n_cc = int(np.sum(ac_mask))\n        if n_cc > 0:\n            lpc = lps[:, ac_mask]\n            spreads = np.max(lpc, axis=0) - np.min(lpc, axis=0)\n            delta = float(np.mean(spreads))\n            delta_std = float(np.std(spreads))\n            delta_median = float(np.median(spreads))\n        else:\n            delta = delta_std = delta_median = None\n\n        dist = {\n            \"0_of_3\": int(np.sum(nc == 0)),\n            \"1_of_3\": int(np.sum(nc == 1)),\n            \"2_of_3\": int(np.sum(nc == 2)),\n            \"3_of_3\": int(np.sum(nc == 3))\n        }\n\n        res[ratio] = {\n            \"ambiguity_alpha\": round(alpha, 6),\n            \"discrepancy_delta_mean\": round(delta, 6) if delta is not None else None,\n            \"discrepancy_delta_std\": round(delta_std, 6) if delta_std is not None else None,\n            \"discrepancy_delta_median\": round(delta_median, 6) if delta_median is not None else None,\n            \"n_concordant_correct\": n_cc,\n            \"disagreement_distribution\": dist,\n            \"n_samples\": N\n        }\n        d_s = f\"{delta:.4f}\" if delta is not None else \"N/A\"\n        print(f\"  {name:4s} {ratio:5s}: alpha={alpha:.4f} delta={d_s} n_cc={n_cc} dist=[{dist['0_of_3']},{dist['1_of_3']},{dist['2_of_3']},{dist['3_of_3']}]\")\n    return res\n\nmult_arc = compute_mult(arc_accs, arc_lp, N_ARC, \"ARC\")\nmult_lamb = compute_mult(lamb_accs, lamb_lp, N_LAMB, \"LAMB\")\n\n# ============ F. Save ============\nprint(\"\\n=== Saving results ===\")\n\nr1 = {\n    \"benchmark\": \"arc_easy\", \"n_samples\": N_ARC,\n    \"architectures\": ARCHS, \"ratios\": RATIOS,\n    \"per_example_classification\": pe,\n    \"convergence_sigma\": conv\n}\np1 = f\"{OUT_DIR}/arc_easy_per_example.json\"\nwith open(p1, \"w\") as f:\n    json.dump(r1, f, indent=2)\nprint(f\"  {p1}\")\n\nr2 = {\n    \"description\": \"Formal Predictive Multiplicity Metrics (Marx et al. 2020)\",\n    \"model_set\": \"3 architectures (GDN, RetNet, HGRN2) at each attention ratio\",\n    \"arc_easy\": {\"n_samples\": N_ARC, \"metrics\": mult_arc},\n    \"lambada\": {\"n_samples\": N_LAMB, \"metrics\": mult_lamb}\n}\np2 = f\"{OUT_DIR}/formal_multiplicity_metrics.json\"\nwith open(p2, \"w\") as f:\n    json.dump(r2, f, indent=2)\nprint(f\"  {p2}\")\n\nr3 = {\n    \"benchmark\": \"arc_easy\", \"n_samples\": N_ARC,\n    \"jaccard_similarity\": jacc, \"jaccard_null_model\": jacc_null\n}\np3 = f\"{OUT_DIR}/arc_easy_jaccard_analysis.json\"\nwith open(p3, \"w\") as f:\n    json.dump(r3, f, indent=2)\nprint(f\"  {p3}\")\n\nprint(\"\\nAll done!\")\nPYEOF\necho \"Script written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat > /root/entrainment_gated_ft/per_example_analysis.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Full per-example analysis for ARC-Easy + LAMBADA (Parts A-F).\"\"\"\nimport json\nimport numpy as np\nfrom itertools import permutations as iterperms\n\nnp.random.seed(42)\n\nARCHS = [\"GDN\", \"RetNet\", \"HGRN2\"]\nRATIOS = [\"pure\", \"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"]\nHYBRID_RATIOS = [\"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"]\nARCH_PAIRS = [(\"GDN\", \"RetNet\"), (\"GDN\", \"HGRN2\"), (\"RetNet\", \"HGRN2\")]\nN_PERM = 10000\nOUT_DIR = \"/root/entrainment_gated_ft\"\n\n# === Paths ===\nARC_BASE = \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy\"\nARC_ARCH_MAP = {\"GDN\": \"GatedDeltaNet\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}\n\ndef arc_path(arch, ratio):\n    a = ARC_ARCH_MAP[arch]\n    if ratio == \"pure\":\n        return f\"{ARC_BASE}/1.3B-100B-{a}-pure/samples/arc_easy.jsonl\"\n    num = ratio.split(\"-\")[0][1:]\n    return f\"{ARC_BASE}/1.3B-100B-{a}-hybrid-{num}-1/samples/arc_easy.jsonl\"\n\nLAMB_EXP = \"/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b\"\nLAMB_EXTRA = \"/root/entrainment_gated_ft/lm_eval_clean/1.3b\"\n\ndef lambada_path(arch, ratio):\n    if arch == \"GDN\" and ratio in [\"h24-1\", \"h6-1\", \"h3-1\"]:\n        return f\"{LAMB_EXTRA}/GDN-{ratio}-logsamples/samples/lambada_openai.jsonl\"\n    name = {\"GDN\": \"GDN\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}[arch]\n    return f\"{LAMB_EXP}/{name}-{ratio}/samples/lambada_openai.jsonl\"\n\ndef load_jsonl(path):\n    data = []\n    with open(path) as f:\n        for line in f:\n            data.append(json.loads(line))\n    return data\n\n# === Load ===\nprint(\"Loading data...\")\narc_data = {}\nlambada_raw = {}\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        arc_data[(arch, ratio)] = load_jsonl(arc_path(arch, ratio))\n        lambada_raw[(arch, ratio)] = load_jsonl(lambada_path(arch, ratio))\n\nN_ARC = len(arc_data[(\"GDN\", \"pure\")])\nN_LAMB = len(lambada_raw[(\"GDN\", \"pure\")])\nprint(f\"ARC-Easy: {N_ARC}, LAMBADA: {N_LAMB}\")\n\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        assert len(arc_data[(arch, ratio)]) == N_ARC, f\"ARC mismatch {arch}/{ratio}: {len(arc_data[(arch,ratio)])} != {N_ARC}\"\n        assert len(lambada_raw[(arch, ratio)]) == N_LAMB, f\"LAMB mismatch {arch}/{ratio}: {len(lambada_raw[(arch,ratio)])} != {N_LAMB}\"\n\n# Verify doc_id alignment\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        for i in range(min(5, N_ARC)):\n            assert arc_data[(arch, ratio)][i][\"doc_id\"] == i, f\"ARC doc_id mismatch {arch}/{ratio} idx={i}\"\n        for i in range(min(5, N_LAMB)):\n            assert lambada_raw[(arch, ratio)][i][\"doc_id\"] == i, f\"LAMB doc_id mismatch {arch}/{ratio} idx={i}\"\n\n# Extract arrays\narc_accs = {}; arc_lp = {}\nlamb_accs = {}; lamb_lp = {}\nfor arch in ARCHS:\n    for ratio in RATIOS:\n        s = arc_data[(arch, ratio)]\n        arc_accs[(arch, ratio)] = np.array([x[\"acc\"] for x in s])\n        arc_lp[(arch, ratio)] = np.array([x[\"filtered_resps\"][x[\"target\"]][0] for x in s])\n        s2 = lambada_raw[(arch, ratio)]\n        lamb_accs[(arch, ratio)] = np.array([float(x[\"acc\"]) for x in s2])\n        lamb_lp[(arch, ratio)] = np.array([x[\"filtered_resps\"][0][0] for x in s2])\n\nprint(\"\\nOverall accuracies:\")\nfor bname, ad in [(\"ARC\", arc_accs), (\"LAMB\", lamb_accs)]:\n    for arch in ARCHS:\n        vals = \" \".join(f\"{r}={np.mean(ad[(arch,r)]):.4f}\" for r in RATIOS)\n        print(f\"  {bname} {arch}: {vals}\")\n\n# ============ A. Per-Example Classification ============\nprint(\"\\n=== A. Per-Example Classification ===\")\npe = {}\nfor arch in ARCHS:\n    pe[arch] = {}\n    pure = arc_accs[(arch, \"pure\")]\n    for ratio in HYBRID_RATIOS:\n        hyb = arc_accs[(arch, ratio)]\n        h = int(np.sum((pure == 0) & (hyb == 1)))\n        r = int(np.sum((pure == 1) & (hyb == 0)))\n        sr = int(np.sum((pure == 1) & (hyb == 1)))\n        sw = int(np.sum((pure == 0) & (hyb == 0)))\n        pe[arch][ratio] = {\n            \"n_helped\": h, \"n_hurt\": r,\n            \"n_stayed_right\": sr, \"n_stayed_wrong\": sw,\n            \"net_effect\": h - r\n        }\n        print(f\"  {arch:6s} {ratio:5s}: helped={h:3d} hurt={r:3d} stayed_right={sr:4d} stayed_wrong={sw:4d} net={h-r:+d}\")\n\n# ============ B & C. Jaccard Analysis ============\nprint(\"\\n=== B & C. Jaccard Analysis ===\")\n\ndef jaccard(a, b):\n    u = a | b\n    return len(a & b) / len(u) if len(u) > 0 else 0.0\n\ndef get_sets(arch, ratio, accs):\n    p = accs[(arch, \"pure\")]\n    h = accs[(arch, ratio)]\n    helped = set(np.where((p == 0) & (h == 1))[0])\n    hurt = set(np.where((p == 1) & (h == 0))[0])\n    return helped, hurt\n\ndef j_null_calc(sA, sB, N):\n    ei = sA * sB / N\n    eu = sA + sB - ei\n    return ei / eu if eu > 0 else 0.0\n\ndef j_max_calc(sA, sB):\n    mn = min(sA, sB)\n    d = sA + sB - mn\n    return mn / d if d > 0 else 0.0\n\ndef perm_test(setA, setB, N, n_perm):\n    obs = jaccard(setA, setB)\n    la, lb = len(setA), len(setB)\n    if la == 0 or lb == 0:\n        return 1.0\n    cnt = 0\n    for _ in range(n_perm):\n        pa = set(np.random.choice(N, la, replace=False))\n        pb = set(np.random.choice(N, lb, replace=False))\n        if jaccard(pa, pb) >= obs:\n            cnt += 1\n    return cnt / n_perm\n\njacc = {}\njacc_null = {}\nfor ratio in HYBRID_RATIOS:\n    jacc[ratio] = {}\n    jacc_null[ratio] = {}\n    for a1, a2 in ARCH_PAIRS:\n        pk = f\"{a1}-{a2}\"\n        h1, r1 = get_sets(a1, ratio, arc_accs)\n        h2, r2 = get_sets(a2, ratio, arc_accs)\n        jh = jaccard(h1, h2)\n        jr = jaccard(r1, r2)\n        jacc[ratio][pk] = {\n            \"helped_jaccard\": round(jh, 4), \"hurt_jaccard\": round(jr, 4),\n            \"helped_sizes\": [len(h1), len(h2)], \"hurt_sizes\": [len(r1), len(r2)],\n            \"helped_intersection\": len(h1 & h2), \"hurt_intersection\": len(r1 & r2)\n        }\n        print(f\"  {ratio:5s} {pk:14s}: J_helped={jh:.4f}(|A|={len(h1)},|B|={len(h2)},∩={len(h1&h2)})  J_hurt={jr:.4f}(|A|={len(r1)},|B|={len(r2)},∩={len(r1&r2)})\")\n\n        for st, s1, s2 in [(\"helped\", h1, h2), (\"hurt\", r1, r2)]:\n            jo = jaccard(s1, s2)\n            jn = j_null_calc(len(s1), len(s2), N_ARC)\n            jm = j_max_calc(len(s1), len(s2))\n            nes = (jo - jn) / (jm - jn) if (jm - jn) > 1e-10 else 0.0\n            pv = perm_test(s1, s2, N_ARC, N_PERM)\n            jacc_null[ratio][f\"{pk}_{st}\"] = {\n                \"J_obs\": round(jo, 4), \"J_null\": round(jn, 4), \"J_max\": round(jm, 4),\n                \"normalized_ES\": round(nes, 4), \"p_value_permutation\": round(pv, 4),\n                \"n_permutations\": N_PERM, \"sizes\": [len(s1), len(s2)]\n            }\n            sig = \"***\" if pv < 0.001 else \"**\" if pv < 0.01 else \"*\" if pv < 0.05 else \"ns\"\n            print(f\"         {st:7s}: J_obs={jo:.4f} J_null={jn:.4f} J_max={jm:.4f} NES={nes:.4f} p={pv:.4f} {sig}\")\n\n# ============ D. Convergence sigma ============\nprint(\"\\n=== D. Convergence sigma ===\")\n\ndef spearman(x, y):\n    n = len(x)\n    rx = np.argsort(np.argsort(x)).astype(float)\n    ry = np.argsort(np.argsort(y)).astype(float)\n    d = rx - ry\n    return 1.0 - 6.0 * np.sum(d**2) / (n * (n**2 - 1))\n\nconv = {}\nmsigs = []\nfor ratio in RATIOS:\n    stack = np.stack([arc_accs[(a, ratio)] for a in ARCHS])\n    sig = np.std(stack, axis=0)\n    ms = float(np.mean(sig))\n    conv[ratio] = {\n        \"mean_sigma\": round(ms, 6),\n        \"median_sigma\": round(float(np.median(sig)), 6),\n        \"n_unanimous_correct\": int(np.sum(np.all(stack == 1, axis=0))),\n        \"n_unanimous_wrong\": int(np.sum(np.all(stack == 0, axis=0))),\n        \"n_split\": int(np.sum((np.sum(stack, axis=0) > 0) & (np.sum(stack, axis=0) < 3)))\n    }\n    msigs.append(ms)\n    print(f\"  {ratio:5s}: mean_sigma={ms:.6f} split={conv[ratio]['n_split']} unan_right={conv[ratio]['n_unanimous_correct']} unan_wrong={conv[ratio]['n_unanimous_wrong']}\")\n\nranks = np.arange(1, 6, dtype=float)\nmsigs_arr = np.array(msigs)\nrho = spearman(ranks, msigs_arr)\n\ncnt_rho = 0\ntot_rho = 0\nfor perm in iterperms(range(5)):\n    ps = msigs_arr[list(perm)]\n    r = spearman(ranks, ps)\n    if abs(r) >= abs(rho) - 1e-10:\n        cnt_rho += 1\n    tot_rho += 1\np_rho = cnt_rho / tot_rho\nconv[\"spearman\"] = {\"rho\": round(float(rho), 4), \"p_exact_two_tailed\": round(p_rho, 4), \"n_permutations\": tot_rho}\nprint(f\"  Spearman rho={rho:.4f}, p_exact={p_rho:.4f} (n_perm={tot_rho})\")\n\n# ============ E. Multiplicity Metrics ============\nprint(\"\\n=== E. Formal Predictive Multiplicity (Marx et al. 2020) ===\")\n\ndef compute_mult(accs_d, lp_d, N, name):\n    res = {}\n    for ratio in RATIOS:\n        stack = np.stack([accs_d[(a, ratio)] for a in ARCHS])\n        lps = np.stack([lp_d[(a, ratio)] for a in ARCHS])\n        nc = np.sum(stack, axis=0)\n        unan = (nc == 0) | (nc == 3)\n        alpha = float(1.0 - np.mean(unan))\n\n        ac_mask = (nc == 3)\n        n_cc = int(np.sum(ac_mask))\n        if n_cc > 0:\n            lpc = lps[:, ac_mask]\n            spreads = np.max(lpc, axis=0) - np.min(lpc, axis=0)\n            delta = float(np.mean(spreads))\n            delta_std = float(np.std(spreads))\n            delta_median = float(np.median(spreads))\n        else:\n            delta = delta_std = delta_median = None\n\n        dist = {\n            \"0_of_3\": int(np.sum(nc == 0)),\n            \"1_of_3\": int(np.sum(nc == 1)),\n            \"2_of_3\": int(np.sum(nc == 2)),\n            \"3_of_3\": int(np.sum(nc == 3))\n        }\n\n        res[ratio] = {\n            \"ambiguity_alpha\": round(alpha, 6),\n            \"discrepancy_delta_mean\": round(delta, 6) if delta is not None else None,\n            \"discrepancy_delta_std\": round(delta_std, 6) if delta_std is not None else None,\n            \"discrepancy_delta_median\": round(delta_median, 6) if delta_median is not None else None,\n            \"n_concordant_correct\": n_cc,\n            \"disagreement_distribution\": dist,\n            \"n_samples\": N\n        }\n        d_s = f\"{delta:.4f}\" if delta is not None else \"N/A\"\n        print(f\"  {name:4s} {ratio:5s}: alpha={alpha:.4f} delta={d_s} n_cc={n_cc} dist=[{dist['0_of_3']},{dist['1_of_3']},{dist['2_of_3']},{dist['3_of_3']}]\")\n    return res\n\nmult_arc = compute_mult(arc_accs, arc_lp, N_ARC, \"ARC\")\nmult_lamb = compute_mult(lamb_accs, lamb_lp, N_LAMB, \"LAMB\")\n\n# ============ F. Save ============\nprint(\"\\n=== Saving results ===\")\n\nr1 = {\n    \"benchmark\": \"arc_easy\", \"n_samples\": N_ARC,\n    \"architectures\": ARCHS, \"ratios\": RATIOS,\n    \"per_example_classification\": pe,\n    \"convergence_sigma\": conv\n}\np1 = f\"{OUT_DIR}/arc_easy_per_example.json\"\nwith open(p1, \"w\") as f:\n    json.dump(r1, f, indent=2)\nprint(f\"  {p1}\")\n\nr2 = {\n    \"description\": \"Formal Predictive Multiplicity Metrics (Marx et al. 2020)\",\n    \"model_set\": \"3 architectures (GDN, RetNet, HGRN2) at each attention ratio\",\n    \"arc_easy\": {\"n_samples\": N_ARC, \"metrics\": mult_arc},\n    \"lambada\": {\"n_samples\": N_LAMB, \"metrics\": mult_lamb}\n}\np2 = f\"{OUT_DIR}/formal_multiplicity_metrics.json\"\nwith open(p2, \"w\") as f:\n    json.dump(r2, f, indent=2)\nprint(f\"  {p2}\")\n\nr3 = {\n    \"benchmark\": \"arc_easy\", \"n_samples\": N_ARC,\n    \"jaccard_similarity\": jacc, \"jaccard_null_model\": jacc_null\n}\np3 = f\"{OUT_DIR}/arc_easy_jaccard_analysis.json\"\nwith open(p3, \"w\") as f:\n    json.dump(r3, f, indent=2)\nprint(f\"  {p3}\")\n\nprint(\"\\nAll done!\")\nPYEOF\necho \"Script written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T09:35:58.397265+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T09:35:58.397433+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && python per_example_analysis.py 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && python per_example_analysis.py 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T09:35:58.397663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\nARC-Easy: 2376, LAMBADA: 5153\\n\\nOverall accuracies:\\n  ARC GDN: pure=0.7121 h24-1=0.7092 h12-1=0.6995 h6-1=0.7176 h3-1=0.7083\\n  ARC RetNet: pure=0.7130 h24-1=0.7088 h12-1=0.7201 h6-1=0.7180 h3-1=0.6961\\n  ARC HGRN2: pure=0.7130 h24-1=0.7302 h12-1=0.7332 h6-1=0.7412 h3-1=0.7205\\n  LAMB GDN: pure=0.5434 h24-1=0.5399 h12-1=0.5358 h6-1=0.5096 h3-1=0.5133\\n  LAMB RetNet: pure=0.5174 h24-1=0.5152 h12-1=0.5067 h6-1=0.4968 h3-1=0.5024\\n  LAMB HGRN2: pure=0.4840 h24-1=0.4999 h12-1=0.5032 h6-1=0.5112 h3-1=0.5143\\n\\n=== A. Per-Example Classification ===\\n  GDN    h24-1: helped=178 hurt=185 stayed_right=1507 stayed_wrong= 506 net=-7\\n  GDN    h12-1: helped=176 hurt=206 stayed_right=1486 stayed_wrong= 508 net=-30\\n  GDN    h6-1 : helped=170 hurt=157 stayed_right=1535 stayed_wrong= 514 net=+13\\n  GDN    h3-1 : helped=171 hurt=180 stayed_right=1512 stayed_wrong= 513 net=-9\\n  RetNet h24-1: helped=158 hurt=168 stayed_right=1526 stayed_wrong= 524 net=-10\\n  RetNet h12-1: helped=163 hurt=146 stayed_right=1548 stayed_wrong= 519 net=+17\\n  RetNet h6-1 : helped=159 hurt=147 stayed_right=1547 stayed_wrong= 523 net=+12\\n  RetNet h3-1 : helped=144 hurt=184 stayed_right=1510 stayed_wrong= 538 net=-40\\n  HGRN2  h24-1: helped=160 hurt=119 stayed_right=1575 stayed_wrong= 522 net=+41\\n  HGRN2  h12-1: helped=159 hurt=111 stayed_right=1583 stayed_wrong= 523 net=+48\\n  HGRN2  h6-1 : helped=185 hurt=118 stayed_right=1576 stayed_wrong= 497 net=+67\\n  HGRN2  h3-1 : helped=164 hurt=146 stayed_right=1548 stayed_wrong= 518 net=+18\\n\\n=== B & C. Jaccard Analysis ===\\n  h24-1 GDN-RetNet    : J_helped=0.0667(|A|=178,|B|=158,∩=21)  J_hurt=0.0795(|A|=185,|B|=168,∩=26)\\n         helped : J_obs=0.0667 J_null=0.0365 J_max=0.8876 NES=0.0354 p=0.0064 **\\n         hurt   : J_obs=0.0795 J_null=0.0385 J_max=0.9081 NES=0.0472 p=0.0005 ***\\n  h24-1 GDN-HGRN2     : J_helped=0.0833(|A|=178,|B|=160,∩=26)  J_hurt=0.1095
…[truncated 4491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T09:35:58.397905+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "arc_easy_per_example",
  "type": "data",
  "description": "ARC-Easy per-example classification (helped/hurt/stayed) + cross-architecture convergence sigma with Spearman test",
  "project": "entrainment_gated_ft",
  "source_path": "/root/entrainment_gated_ft/arc_easy_per_example.json",
  "tags": "['arc_easy', 'per_example', 'convergence']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "arc_easy_per_example",
    "type": "data",
    "description": "ARC-Easy per-example classification (helped/hurt/stayed) + cross-architecture convergence sigma with Spearman test",
    "project": "entrainment_gated_ft",
    "source_path": "/root/entrainment_gated_ft/arc_easy_per_example.json",
    "tags": "['arc_easy', 'per_example', 'convergence']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T09:35:58.398065+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/entrainment_gated_ft/arc_easy_per_example.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T09:35:58.398197+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "formal_multiplicity_metrics",
  "type": "data",
  "description": "Formal Predictive Multiplicity (Marx et al. 2020): ambiguity alpha + discrepancy delta for ARC-Easy and LAMBADA",
  "project": "entrainment_gated_ft",
  "source_path": "/root/entrainment_gated_ft/formal_multiplicity_metrics.json",
  "tags": "['multiplicity', 'arc_easy', 'lambada', 'ambiguity', 'discrepancy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "formal_multiplicity_metrics",
    "type": "data",
    "description": "Formal Predictive Multiplicity (Marx et al. 2020): ambiguity alpha + discrepancy delta for ARC-Easy and LAMBADA",
    "project": "entrainment_gated_ft",
    "source_path": "/root/entrainment_gated_ft/formal_multiplicity_metrics.json",
    "tags": "['multiplicity', 'arc_easy', 'lambada', 'ambiguity', 'discrepancy']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T09:35:58.398326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/entrainment_gated_ft/formal_multiplicity_metrics.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T09:35:58.398445+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "arc_easy_jaccard_analysis",
  "type": "data",
  "description": "ARC-Easy cross-architecture Jaccard similarity with null model, normalized ES, and 10K permutation tests",
  "project": "entrainment_gated_ft",
  "source_path": "/root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
  "tags": "['arc_easy', 'jaccard', 'permutation_test', 'null_model']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "arc_easy_jaccard_analysis",
    "type": "data",
    "description": "ARC-Easy cross-architecture Jaccard similarity with null model, normalized ES, and 10K permutation tests",
    "project": "entrainment_gated_ft",
    "source_path": "/root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
    "tags": "['arc_easy', 'jaccard', 'permutation_test', 'null_model']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T09:35:58.398567+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T09:35:58.398748+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/arc_easy_per_example.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/arc_easy_per_example.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T09:35:58.398880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/formal_multiplicity_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/formal_multiplicity_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T09:35:58.399085+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_easy\\\",\\n  \\\"n_samples\\\": 2376,\\n  \\\"architectures\\\": [\\n    \\\"GDN\\\",\\n    \\\"RetNet\\\",\\n    \\\"HGRN2\\\"\\n  ],\\n  \\\"ratios\\\": [\\n    \\\"pure\\\",\\n    \\\"h24-1\\\",\\n    \\\"h12-1\\\",\\n    \\\"h6-1\\\",\\n    \\\"h3-1\\\"\\n  ],\\n  \\\"per_example_classification\\\": {\\n    \\\"GDN\\\": {\\n      \\\"h24-1\\\": {\\n        \\\"n_helped\\\": 178,\\n        \\\"n_hurt\\\": 185,\\n        \\\"n_stayed_right\\\": 1507,\\n        \\\"n_stayed_wrong\\\": 506,\\n        \\\"net_effect\\\": -7\\n      },\\n      \\\"h12-1\\\": {\\n        \\\"n_helped\\\": 176,\\n        \\\"n_hurt\\\": 206,\\n        \\\"n_stayed_right\\\": 1486,\\n        \\\"n_stayed_wrong\\\": 508,\\n        \\\"net_effect\\\": -30\\n      },\\n      \\\"h6-1\\\": {\\n        \\\"n_helped\\\": 170,\\n        \\\"n_hurt\\\": 157,\\n        \\\"n_stayed_right\\\": 1535,\\n        \\\"n_stayed_wrong\\\": 514,\\n        \\\"net_effect\\\": 13\\n      },\\n      \\\"h3-1\\\": {\\n        \\\"n_helped\\\": 171,\\n        \\\"n_hurt\\\": 180,\\n        \\\"n_stayed_right\\\": 1512,\\n        \\\"n_stayed_wrong\\\": 513,\\n        \\\"net_effect\\\": -9\\n      }\\n    },\\n    \\\"RetNet\\\": {\\n      \\\"h24-1\\\": {\\n        \\\"n_helped\\\": 158,\\n        \\\"n_hurt\\\": 168,\\n        \\\"n_stayed_right\\\": 1526,\\n        \\\"n_stayed_wrong\\\": 524,\\n        \\\"net_effect\\\": -10\\n      },\\n      \\\"h12-1\\\": {\\n        \\\"n_helped\\\": 163,\\n        \\\"n_hurt\\\": 146,\\n        \\\"n_stayed_right\\\": 1548,\\n        \\\"n_stayed_wrong\\\": 519,\\n        \\\"net_effect\\\": 17\\n      },\\n      \\\"h6-1\\\": {\\n        \\\"n_helped\\\": 159,\\n        \\\"n_hurt\\\": 147,\\n        \\\"n_stayed_right\\\": 1547,\\n        \\\"n_stayed_wrong\\\": 523,\\n        \\\"net_effect\\\": 12\\n      },\\n      \\\"h3-1\\\": {\\n        \\\"n_helped\\\": 144,\\n        
…[truncated 2405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T09:35:58.399291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T09:35:58.399539+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Formal Predictive Multiplicity Metrics (Marx et al. 2020)\\\",\\n  \\\"model_set\\\": \\\"3 architectures (GDN, RetNet, HGRN2) at each attention ratio\\\",\\n  \\\"arc_easy\\\": {\\n    \\\"n_samples\\\": 2376,\\n    \\\"metrics\\\": {\\n      \\\"pure\\\": {\\n        \\\"ambiguity_alpha\\\": 0.204545,\\n        \\\"discrepancy_delta_mean\\\": 2.547774,\\n        \\\"discrepancy_delta_std\\\": 1.60719,\\n        \\\"discrepancy_delta_median\\\": 2.195312,\\n        \\\"n_concordant_correct\\\": 1434,\\n        \\\"disagreement_distribution\\\": {\\n          \\\"0_of_3\\\": 456,\\n          \\\"1_of_3\\\": 194,\\n          \\\"2_of_3\\\": 292,\\n          \\\"3_of_3\\\": 1434\\n        },\\n        \\\"n_samples\\\": 2376\\n      },\\n      \\\"h24-1\\\": {\\n        \\\"ambiguity_alpha\\\": 0.226431,\\n        \\\"discrepancy_delta_mean\\\": 2.981579,\\n        \\\"discrepancy_delta_std\\\": 1.794458,\\n        \\\"discrepancy_delta_median\\\": 2.625,\\n        \\\"n_concordant_correct\\\": 1421,\\n        \\\"disagreement_distribution\\\": {\\n          \\\"0_of_3\\\": 417,\\n          \\\"1_of_3\\\": 235,\\n          \\\"2_of_3\\\": 303,\\n          \\\"3_of_3\\\": 1421\\n        },\\n        \\\"n_samples\\\": 2376\\n      },\\n      \\\"h12-1\\\": {\\n        \\\"ambiguity_alpha\\\": 0.223064,\\n        \\\"discrepancy_delta_mean\\\": 3.124677,\\n        \\\"discrepancy_delta_std\\\": 1.788919,\\n        \\\"discrepancy_delta_median\\\": 2.8125,\\n        \\\"n_concordant_correct\\\": 1427,\\n        \\\"disagreement_distribution\\\": {\\n          \\\"0_of_3\\\": 419,\\n          \\\"1_of_3\\\": 226,\\n          \\\"2_of_3\\\": 304,\\n          \\\"3_of_3\\\": 1427\\n        },\\n        \\\"n_samples\\\": 2376\\n      },\\n      \\\"h6-1\\\": {\\n        \\\"ambiguity_alpha\\\": 0.201178,\\n        \\\"discrepancy_delta_mean\\\": 2.321217,\\n        \\\"discrepancy_delta_s
…[truncated 3621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T09:35:58.399942+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_easy\\\",\\n  \\\"n_samples\\\": 2376,\\n  \\\"jaccard_similarity\\\": {\\n    \\\"h24-1\\\": {\\n      \\\"GDN-RetNet\\\": {\\n        \\\"helped_jaccard\\\": 0.0667,\\n        \\\"hurt_jaccard\\\": 0.0795,\\n        \\\"helped_sizes\\\": [\\n          178,\\n          158\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          185,\\n          168\\n        ],\\n        \\\"helped_intersection\\\": 21,\\n        \\\"hurt_intersection\\\": 26\\n      },\\n      \\\"GDN-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.0833,\\n        \\\"hurt_jaccard\\\": 0.1095,\\n        \\\"helped_sizes\\\": [\\n          178,\\n          160\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          185,\\n          119\\n        ],\\n        \\\"helped_intersection\\\": 26,\\n        \\\"hurt_intersection\\\": 30\\n      },\\n      \\\"RetNet-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.0743,\\n        \\\"hurt_jaccard\\\": 0.0913,\\n        \\\"helped_sizes\\\": [\\n          158,\\n          160\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          168,\\n          119\\n        ],\\n        \\\"helped_intersection\\\": 22,\\n        \\\"hurt_intersection\\\": 24\\n      }\\n    },\\n    \\\"h12-1\\\": {\\n      \\\"GDN-RetNet\\\": {\\n        \\\"helped_jaccard\\\": 0.0935,\\n        \\\"hurt_jaccard\\\": 0.1282,\\n        \\\"helped_sizes\\\": [\\n          176,\\n          163\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          206,\\n          146\\n        ],\\n        \\\"helped_intersection\\\": 29,\\n        \\\"hurt_intersection\\\": 40\\n      },\\n      \\\"GDN-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.1167,\\n        \\\"hurt_jaccard\\\": 0.0856,\\n        \\\"helped_sizes\\\": [\\n          176,\\n          159\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          206,\\n          111\\n        ],\\n        \\\"helped_intersection\\\": 35,\\n        \\\"h
…[truncated 8260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T09:35:58.400150+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westb-48145:/root/entrainment_gated_ft/arc_easy_per_example.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
  "description": "SCP arc_easy_per_example.json from server to local artifacts",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westb-48145:/root/entrainment_gated_ft/arc_easy_per_example.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
    "description": "SCP arc_easy_per_example.json from server to local artifacts",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T09:35:58.400285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westb-48145:/root/entrainment_gated_ft/formal_multiplicity_metrics.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
  "description": "SCP formal_multiplicity_metrics.json from server to local artifacts",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westb-48145:/root/entrainment_gated_ft/formal_multiplicity_metrics.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
    "description": "SCP formal_multiplicity_metrics.json from server to local artifacts",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T09:35:58.400415+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westb-48145:/root/entrainment_gated_ft/arc_easy_jaccard_analysis.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
  "description": "SCP arc_easy_jaccard_analysis.json from server to local artifacts",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westb-48145:/root/entrainment_gated_ft/arc_easy_jaccard_analysis.json /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ 2>&1",
    "description": "SCP arc_easy_jaccard_analysis.json from server to local artifacts",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T09:35:58.400549+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
root@connect.westb.seetacloud.com: Permission denied (publickey,password).
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T09:35:58.400687+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(scp westb-48145:/root/entrainment_gated_…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T09:35:58.400810+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(scp westb-48145:/root/entrainment_gated_…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T09:35:58.400975+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -c /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -c /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T09:35:58.401103+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"10369 /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T09:35:58.401237+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -150 /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -150 /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T09:35:58.401421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_easy\\\",\\n  \\\"n_samples\\\": 2376,\\n  \\\"jaccard_similarity\\\": {\\n    \\\"h24-1\\\": {\\n      \\\"GDN-RetNet\\\": {\\n        \\\"helped_jaccard\\\": 0.0667,\\n        \\\"hurt_jaccard\\\": 0.0795,\\n        \\\"helped_sizes\\\": [\\n          178,\\n          158\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          185,\\n          168\\n        ],\\n        \\\"helped_intersection\\\": 21,\\n        \\\"hurt_intersection\\\": 26\\n      },\\n      \\\"GDN-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.0833,\\n        \\\"hurt_jaccard\\\": 0.1095,\\n        \\\"helped_sizes\\\": [\\n          178,\\n          160\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          185,\\n          119\\n        ],\\n        \\\"helped_intersection\\\": 26,\\n        \\\"hurt_intersection\\\": 30\\n      },\\n      \\\"RetNet-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.0743,\\n        \\\"hurt_jaccard\\\": 0.0913,\\n        \\\"helped_sizes\\\": [\\n          158,\\n          160\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          168,\\n          119\\n        ],\\n        \\\"helped_intersection\\\": 22,\\n        \\\"hurt_intersection\\\": 24\\n      }\\n    },\\n    \\\"h12-1\\\": {\\n      \\\"GDN-RetNet\\\": {\\n        \\\"helped_jaccard\\\": 0.0935,\\n        \\\"hurt_jaccard\\\": 0.1282,\\n        \\\"helped_sizes\\\": [\\n          176,\\n          163\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          206,\\n          146\\n        ],\\n        \\\"helped_intersection\\\": 29,\\n        \\\"hurt_intersection\\\": 40\\n      },\\n      \\\"GDN-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.1167,\\n        \\\"hurt_jaccard\\\": 0.0856,\\n        \\\"helped_sizes\\\": [\\n          176,\\n          159\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          206,\\n          111\\n        ],\\n        \\\"helped_intersection\\\": 35,\\n        \\\"h
…[truncated 2013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T09:35:58.401593+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "tail -n +151 /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "tail -n +151 /root/entrainment_gated_ft/arc_easy_jaccard_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T09:35:58.401889+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      },\\n      \\\"GDN-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.1056,\\n        \\\"hurt_jaccard\\\": 0.0976,\\n        \\\"helped_sizes\\\": [\\n          171,\\n          164\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          180,\\n          146\\n        ],\\n        \\\"helped_intersection\\\": 32,\\n        \\\"hurt_intersection\\\": 29\\n      },\\n      \\\"RetNet-HGRN2\\\": {\\n        \\\"helped_jaccard\\\": 0.0883,\\n        \\\"hurt_jaccard\\\": 0.134,\\n        \\\"helped_sizes\\\": [\\n          144,\\n          164\\n        ],\\n        \\\"hurt_sizes\\\": [\\n          184,\\n          146\\n        ],\\n        \\\"helped_intersection\\\": 25,\\n        \\\"hurt_intersection\\\": 39\\n      }\\n    }\\n  },\\n  \\\"jaccard_null_model\\\": {\\n    \\\"h24-1\\\": {\\n      \\\"GDN-RetNet_helped\\\": {\\n        \\\"J_obs\\\": 0.0667,\\n        \\\"J_null\\\": 0.0365,\\n        \\\"J_max\\\": 0.8876,\\n        \\\"normalized_ES\\\": 0.0354,\\n        \\\"p_value_permutation\\\": 0.0064,\\n        \\\"n_permutations\\\": 10000,\\n        \\\"sizes\\\": [\\n          178,\\n          158\\n        ]\\n      },\\n      \\\"GDN-RetNet_hurt\\\": {\\n        \\\"J_obs\\\": 0.0795,\\n        \\\"J_null\\\": 0.0385,\\n        \\\"J_max\\\": 0.9081,\\n        \\\"normalized_ES\\\": 0.0472,\\n        \\\"p_value_permutation\\\": 0.0005,\\n        \\\"n_permutations\\\": 10000,\\n        \\\"sizes\\\": [\\n          185,\\n          168\\n        ]\\n      },\\n      \\\"GDN-HGRN2_helped\\\": {\\n        \\\"J_obs\\\": 0.0833,\\n        \\\"J_null\\\": 0.0368,\\n        \\\"J_max\\\": 0.8989,\\n        \\\"normalized_ES\\\": 0.054,\\n        \\\"p_value_permutation\\\": 0.0002,\\n        \\\"n_permutations\\\": 10000,\\n        \\\"sizes\\\": [\\n          178,\\n          160\\n        ]\\n      },\\n      \\\"GDN-HGRN2_hurt\\\": {\\n        \\\"J_obs\\\": 0.1095,\\n        \\\"J_null\\\": 
…[truncated 7368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T09:35:58.402089+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
  "description": "List local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
    "description": "List local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T09:35:58.402226+00:00_

__pycache__
_project
d009_assessment.md
dream_reports
eval_composition.py
eval_composition_modified.py
exp-001
exp-003
exp-003-p2
exp-004
exp-007
exp-010
exp003_p2_data_check.md
exp007_data_check.md
exp007_script_ready.md
lm_eval_1.3b_results.md
manifest.yaml
null_jaccard_results.json
paper_agent_inputs.md
paper_data
per_example_data_audit.md
review_issues.yaml
review_reports
synthetic_task_design.md
wang_7b_search_results.md
wang_et_al_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T09:35:58.402367+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_per_example.json",
  "content": "{\n  \"benchmark\": \"arc_easy\",\n  \"n_samples\": 2376,\n  \"architectures\": [\"GDN\", \"RetNet\", \"HGRN2\"],\n  \"ratios\": [\"pure\", \"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"],\n  \"per_example_classification\": {\n    \"GDN\": {\n      \"h24-1\": {\"n_helped\": 178, \"n_hurt\": 185, \"n_stayed_right\": 1507, \"n_stayed_wrong\": 506, \"net_effect\": -7},\n      \"h12-1\": {\"n_helped\": 176, \"n_hurt\": 206, \"n_stayed_right\": 1486, \"n_stayed_wrong\": 508, \"net_effect\": -30},\n      \"h6-1\": {\"n_helped\": 170, \"n_hurt\": 157, \"n_stayed_right\": 1535, \"n_stayed_wrong\": 514, \"net_effect\": 13},\n      \"h3-1\": {\"n_helped\": 171, \"n_hurt\": 180, \"n_stayed_right\": 1512, \"n_stayed_wrong\": 513, \"net_effect\": -9}\n    },\n    \"RetNet\": {\n      \"h24-1\": {\"n_helped\": 158, \"n_hurt\": 168, \"n_stayed_right\": 1526, \"n_stayed_wrong\": 524, \"net_effect\": -10},\n      \"h12-1\": {\"n_helped\": 163, \"n_hurt\": 146, \"n_stayed_right\": 1548, \"n_stayed_wrong\": 519, \"net_effect\": 17},\n      \"h6-1\": {\"n_helped\": 159, \"n_hurt\": 147, \"n_stayed_right\": 1547, \"n_stayed_wrong\": 523, \"net_effect\": 12},\n      \"h3-1\": {\"n_helped\": 144, \"n_hurt\": 184, \"n_stayed_right\": 1510, \"n_stayed_wrong\": 538, \"net_effect\": -40}\n    },\n    \"HGRN2\": {\n      \"h24-1\": {\"n_helped\": 160, \"n_hurt\": 119, \"n_stayed_right\": 1575, \"n_stayed_wrong\": 522, \"net_effect\": 41},\n      \"h12-1\": {\"n_helped\": 159, \"n_hurt\": 111, \"n_stayed_right\": 1583, \"n_stayed_wrong\": 523, \"net_effect\": 48},\n      \"h6-1\": {\"n_helped\": 185, \"n_hurt\": 118, \"n_stayed_right\": 1576, \"n_stayed_wrong\": 497, \"net_effect\": 67},\n      \"h3-1\": {\"n_helped\": 164, \"n_hurt\": 146, \"n_stayed_right\": 1548, \"n_stayed_wrong\": 518, \"net_effect\": 18}\n    }\n  },\n  \"convergence_sigma\": {\n    \"pure\": {\"mean_sigma\": 0.096424, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1434, \"n_unanimous_wrong\": 456, \"n_split\": 486},\n    \"h24-1\": {\"mean_sigma\": 0.106741, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1421, \"n_unanimous_wrong\": 417, \"n_split\": 538},\n    \"h12-1\": {\"mean_sigma\": 0.105153, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1427, \"n_unanimous_wrong\": 419, \"n_split\": 530},\n    \"h6-1\": {\"mean_sigma\": 0.094836, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1469, \"n_unanimous_wrong\": 429, \"n_split\": 478},\n    \"h3-1\": {\"mean_sigma\": 0.099003, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1432, \"n_unanimous_wrong\": 445, \"n_split\": 499},\n    \"spearman\": {\"rho\": -0.2, \"p_exact_two_tailed\": 0.7833, \"n_permutations\": 120}\n  }\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_per_example.json",
    "content": "{\n  \"benchmark\": \"arc_easy\",\n  \"n_samples\": 2376,\n  \"architectures\": [\"GDN\", \"RetNet\", \"HGRN2\"],\n  \"ratios\": [\"pure\", \"h24-1\", \"h12-1\", \"h6-1\", \"h3-1\"],\n  \"per_example_classification\": {\n    \"GDN\": {\n      \"h24-1\": {\"n_helped\": 178, \"n_hurt\": 185, \"n_stayed_right\": 1507, \"n_stayed_wrong\": 506, \"net_effect\": -7},\n      \"h12-1\": {\"n_helped\": 176, \"n_hurt\": 206, \"n_stayed_right\": 1486, \"n_stayed_wrong\": 508, \"net_effect\": -30},\n      \"h6-1\": {\"n_helped\": 170, \"n_hurt\": 157, \"n_stayed_right\": 1535, \"n_stayed_wrong\": 514, \"net_effect\": 13},\n      \"h3-1\": {\"n_helped\": 171, \"n_hurt\": 180, \"n_stayed_right\": 1512, \"n_stayed_wrong\": 513, \"net_effect\": -9}\n    },\n    \"RetNet\": {\n      \"h24-1\": {\"n_helped\": 158, \"n_hurt\": 168, \"n_stayed_right\": 1526, \"n_stayed_wrong\": 524, \"net_effect\": -10},\n      \"h12-1\": {\"n_helped\": 163, \"n_hurt\": 146, \"n_stayed_right\": 1548, \"n_stayed_wrong\": 519, \"net_effect\": 17},\n      \"h6-1\": {\"n_helped\": 159, \"n_hurt\": 147, \"n_stayed_right\": 1547, \"n_stayed_wrong\": 523, \"net_effect\": 12},\n      \"h3-1\": {\"n_helped\": 144, \"n_hurt\": 184, \"n_stayed_right\": 1510, \"n_stayed_wrong\": 538, \"net_effect\": -40}\n    },\n    \"HGRN2\": {\n      \"h24-1\": {\"n_helped\": 160, \"n_hurt\": 119, \"n_stayed_right\": 1575, \"n_stayed_wrong\": 522, \"net_effect\": 41},\n      \"h12-1\": {\"n_helped\": 159, \"n_hurt\": 111, \"n_stayed_right\": 1583, \"n_stayed_wrong\": 523, \"net_effect\": 48},\n      \"h6-1\": {\"n_helped\": 185, \"n_hurt\": 118, \"n_stayed_right\": 1576, \"n_stayed_wrong\": 497, \"net_effect\": 67},\n      \"h3-1\": {\"n_helped\": 164, \"n_hurt\": 146, \"n_stayed_right\": 1548, \"n_stayed_wrong\": 518, \"net_effect\": 18}\n    }\n  },\n  \"convergence_sigma\": {\n    \"pure\": {\"mean_sigma\": 0.096424, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1434, \"n_unanimous_wrong\": 456, \"n_split\": 486},\n    \"h24-1\": {\"mean_sigma\": 0.106741, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1421, \"n_unanimous_wrong\": 417, \"n_split\": 538},\n    \"h12-1\": {\"mean_sigma\": 0.105153, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1427, \"n_unanimous_wrong\": 419, \"n_split\": 530},\n    \"h6-1\": {\"mean_sigma\": 0.094836, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1469, \"n_unanimous_wrong\": 429, \"n_split\": 478},\n    \"h3-1\": {\"mean_sigma\": 0.099003, \"median_sigma\": 0.0, \"n_unanimous_correct\": 1432, \"n_unanimous_wrong\": 445, \"n_split\": 499},\n    \"spearman\": {\"rho\": -0.2, \"p_exact_two_tailed\": 0.7833, \"n_permutations\": 120}\n  }\n}"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T09:35:58.402528+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_per_example.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T09:35:58.402680+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/formal_multiplicity_metrics.json",
  "content": "{\n  \"description\": \"Formal Predictive Multiplicity Metrics (Marx et al. 2020)\",\n  \"model_set\": \"3 architectures (GDN, RetNet, HGRN2) at each attention ratio\",\n  \"arc_easy\": {\n    \"n_samples\": 2376,\n    \"metrics\": {\n      \"pure\": {\"ambiguity_alpha\": 0.204545, \"discrepancy_delta_mean\": 2.547774, \"discrepancy_delta_std\": 1.60719, \"discrepancy_delta_median\": 2.195312, \"n_concordant_correct\": 1434, \"disagreement_distribution\": {\"0_of_3\": 456, \"1_of_3\": 194, \"2_of_3\": 292, \"3_of_3\": 1434}, \"n_samples\": 2376},\n      \"h24-1\": {\"ambiguity_alpha\": 0.226431, \"discrepancy_delta_mean\": 2.981579, \"discrepancy_delta_std\": 1.794458, \"discrepancy_delta_median\": 2.625, \"n_concordant_correct\": 1421, \"disagreement_distribution\": {\"0_of_3\": 417, \"1_of_3\": 235, \"2_of_3\": 303, \"3_of_3\": 1421}, \"n_samples\": 2376},\n      \"h12-1\": {\"ambiguity_alpha\": 0.223064, \"discrepancy_delta_mean\": 3.124677, \"discrepancy_delta_std\": 1.788919, \"discrepancy_delta_median\": 2.8125, \"n_concordant_correct\": 1427, \"disagreement_distribution\": {\"0_of_3\": 419, \"1_of_3\": 226, \"2_of_3\": 304, \"3_of_3\": 1427}, \"n_samples\": 2376},\n      \"h6-1\": {\"ambiguity_alpha\": 0.201178, \"discrepancy_delta_mean\": 2.321217, \"discrepancy_delta_std\": 1.510742, \"discrepancy_delta_median\": 2.0, \"n_concordant_correct\": 1469, \"disagreement_distribution\": {\"0_of_3\": 429, \"1_of_3\": 191, \"2_of_3\": 287, \"3_of_3\": 1469}, \"n_samples\": 2376},\n      \"h3-1\": {\"ambiguity_alpha\": 0.210017, \"discrepancy_delta_mean\": 2.663469, \"discrepancy_delta_std\": 1.86627, \"discrepancy_delta_median\": 2.1875, \"n_concordant_correct\": 1432, \"disagreement_distribution\": {\"0_of_3\": 445, \"1_of_3\": 245, \"2_of_3\": 254, \"3_of_3\": 1432}, \"n_samples\": 2376}\n    }\n  },\n  \"lambada\": {\n    \"n_samples\": 5153,\n    \"metrics\": {\n      \"pure\": {\"ambiguity_alpha\": 0.306618, \"discrepancy_delta_mean\": 0.609696, \"discrepancy_delta_std\": 0.453239, \"discrepancy_delta_median\": 0.507812, \"n_concordant_correct\": 1854, \"disagreement_distribution\": {\"0_of_3\": 1719, \"1_of_3\": 762, \"2_of_3\": 818, \"3_of_3\": 1854}, \"n_samples\": 5153},\n      \"h24-1\": {\"ambiguity_alpha\": 0.300019, \"discrepancy_delta_mean\": 0.579046, \"discrepancy_delta_std\": 0.432728, \"discrepancy_delta_median\": 0.492188, \"n_concordant_correct\": 1886, \"disagreement_distribution\": {\"0_of_3\": 1721, \"1_of_3\": 737, \"2_of_3\": 809, \"3_of_3\": 1886}, \"n_samples\": 5153},\n      \"h12-1\": {\"ambiguity_alpha\": 0.315932, \"discrepancy_delta_mean\": 0.545544, \"discrepancy_delta_std\": 0.409817, \"discrepancy_delta_median\": 0.464111, \"n_concordant_correct\": 1824, \"disagreement_distribution\": {\"0_of_3\": 1701, \"1_of_3\": 763, \"2_of_3\": 865, \"3_of_3\": 1824}, \"n_samples\": 5153},\n      \"h6-1\": {\"ambiguity_alpha\": 0.293615, \"discrepancy_delta_mean\": 0.531844, \"discrepancy_delta_std\": 0.404355, \"discrepancy_delta_median\": 0.436768, \"n_concordant_correct\": 1828, \"disagreement_distribution\": {\"0_of_3\": 1812, \"1_of_3\": 690, \"2_of_3\": 823, \"3_of_3\": 1828}, \"n_samples\": 5153},\n      \"h3-1\": {\"ambiguity_alpha\": 0.295944, \"discrepancy_delta_mean\": 0.549026, \"discrepancy_delta_std\": 0.433378, \"discrepancy_delta_median\": 0.442871, \"n_concordant_correct\": 1860, \"disagreement_distribution\": {\"0_of_3\": 1768, \"1_of_3\": 746, \"2_of_3\": 779, \"3_of_3\": 1860}, \"n_samples\": 5153}\n    }\n  }\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/formal_multiplicity_metrics.json",
    "content": "{\n  \"description\": \"Formal Predictive Multiplicity Metrics (Marx et al. 2020)\",\n  \"model_set\": \"3 architectures (GDN, RetNet, HGRN2) at each attention ratio\",\n  \"arc_easy\": {\n    \"n_samples\": 2376,\n    \"metrics\": {\n      \"pure\": {\"ambiguity_alpha\": 0.204545, \"discrepancy_delta_mean\": 2.547774, \"discrepancy_delta_std\": 1.60719, \"discrepancy_delta_median\": 2.195312, \"n_concordant_correct\": 1434, \"disagreement_distribution\": {\"0_of_3\": 456, \"1_of_3\": 194, \"2_of_3\": 292, \"3_of_3\": 1434}, \"n_samples\": 2376},\n      \"h24-1\": {\"ambiguity_alpha\": 0.226431, \"discrepancy_delta_mean\": 2.981579, \"discrepancy_delta_std\": 1.794458, \"discrepancy_delta_median\": 2.625, \"n_concordant_correct\": 1421, \"disagreement_distribution\": {\"0_of_3\": 417, \"1_of_3\": 235, \"2_of_3\": 303, \"3_of_3\": 1421}, \"n_samples\": 2376},\n      \"h12-1\": {\"ambiguity_alpha\": 0.223064, \"discrepancy_delta_mean\": 3.124677, \"discrepancy_delta_std\": 1.788919, \"discrepancy_delta_median\": 2.8125, \"n_concordant_correct\": 1427, \"disagreement_distribution\": {\"0_of_3\": 419, \"1_of_3\": 226, \"2_of_3\": 304, \"3_of_3\": 1427}, \"n_samples\": 2376},\n      \"h6-1\": {\"ambiguity_alpha\": 0.201178, \"discrepancy_delta_mean\": 2.321217, \"discrepancy_delta_std\": 1.510742, \"discrepancy_delta_median\": 2.0, \"n_concordant_correct\": 1469, \"disagreement_distribution\": {\"0_of_3\": 429, \"1_of_3\": 191, \"2_of_3\": 287, \"3_of_3\": 1469}, \"n_samples\": 2376},\n      \"h3-1\": {\"ambiguity_alpha\": 0.210017, \"discrepancy_delta_mean\": 2.663469, \"discrepancy_delta_std\": 1.86627, \"discrepancy_delta_median\": 2.1875, \"n_concordant_correct\": 1432, \"disagreement_distribution\": {\"0_of_3\": 445, \"1_of_3\": 245, \"2_of_3\": 254, \"3_of_3\": 1432}, \"n_samples\": 2376}\n    }\n  },\n  \"lambada\": {\n    \"n_samples\": 5153,\n    \"metrics\": {\n      \"pure\": {\"ambiguity_alpha\": 0.306618, \"discrepancy_delta_mean\": 0.609696, \"discrepancy_delta_std\": 0.453239, \"discrepancy_delta_median\": 0.507812, \"n_concordant_correct\": 1854, \"disagreement_distribution\": {\"0_of_3\": 1719, \"1_of_3\": 762, \"2_of_3\": 818, \"3_of_3\": 1854}, \"n_samples\": 5153},\n      \"h24-1\": {\"ambiguity_alpha\": 0.300019, \"discrepancy_delta_mean\": 0.579046, \"discrepancy_delta_std\": 0.432728, \"discrepancy_delta_median\": 0.492188, \"n_concordant_correct\": 1886, \"disagreement_distribution\": {\"0_of_3\": 1721, \"1_of_3\": 737, \"2_of_3\": 809, \"3_of_3\": 1886}, \"n_samples\": 5153},\n      \"h12-1\": {\"ambiguity_alpha\": 0.315932, \"discrepancy_delta_mean\": 0.545544, \"discrepancy_delta_std\": 0.409817, \"discrepancy_delta_median\": 0.464111, \"n_concordant_correct\": 1824, \"disagreement_distribution\": {\"0_of_3\": 1701, \"1_of_3\": 763, \"2_of_3\": 865, \"3_of_3\": 1824}, \"n_samples\": 5153},\n      \"h6-1\": {\"ambiguity_alpha\": 0.293615, \"discrepancy_delta_mean\": 0.531844, \"discrepancy_delta_std\": 0.404355, \"discrepancy_delta_median\": 0.436768, \"n_concordant_correct\": 1828, \"disagreement_distribution\": {\"0_of_3\": 1812, \"1_of_3\": 690, \"2_of_3\": 823, \"3_of_3\": 1828}, \"n_samples\": 5153},\n      \"h3-1\": {\"ambiguity_alpha\": 0.295944, \"discrepancy_delta_mean\": 0.549026, \"discrepancy_delta_std\": 0.433378, \"discrepancy_delta_median\": 0.442871, \"n_concordant_correct\": 1860, \"disagreement_distribution\": {\"0_of_3\": 1768, \"1_of_3\": 746, \"2_of_3\": 779, \"3_of_3\": 1860}, \"n_samples\": 5153}\n    }\n  }\n}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T09:35:58.402855+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/formal_multiplicity_metrics.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T09:35:58.403013+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_jaccard_analysis.json",
  "content": "{\n  \"benchmark\": \"arc_easy\",\n  \"n_samples\": 2376,\n  \"jaccard_similarity\": {\n    \"h24-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0667, \"hurt_jaccard\": 0.0795, \"helped_sizes\": [178, 158], \"hurt_sizes\": [185, 168], \"helped_intersection\": 21, \"hurt_intersection\": 26},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.0833, \"hurt_jaccard\": 0.1095, \"helped_sizes\": [178, 160], \"hurt_sizes\": [185, 119], \"helped_intersection\": 26, \"hurt_intersection\": 30},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0743, \"hurt_jaccard\": 0.0913, \"helped_sizes\": [158, 160], \"hurt_sizes\": [168, 119], \"helped_intersection\": 22, \"hurt_intersection\": 24}\n    },\n    \"h12-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0935, \"hurt_jaccard\": 0.1282, \"helped_sizes\": [176, 163], \"hurt_sizes\": [206, 146], \"helped_intersection\": 29, \"hurt_intersection\": 40},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.1167, \"hurt_jaccard\": 0.0856, \"helped_sizes\": [176, 159], \"hurt_sizes\": [206, 111], \"helped_intersection\": 35, \"hurt_intersection\": 25},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0842, \"hurt_jaccard\": 0.0844, \"helped_sizes\": [163, 159], \"hurt_sizes\": [146, 111], \"helped_intersection\": 25, \"hurt_intersection\": 20}\n    },\n    \"h6-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0894, \"hurt_jaccard\": 0.0896, \"helped_sizes\": [170, 159], \"hurt_sizes\": [157, 147], \"helped_intersection\": 27, \"hurt_intersection\": 25},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.0991, \"hurt_jaccard\": 0.087, \"helped_sizes\": [170, 185], \"hurt_sizes\": [157, 118], \"helped_intersection\": 32, \"hurt_intersection\": 22},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0921, \"hurt_jaccard\": 0.0861, \"helped_sizes\": [159, 185], \"hurt_sizes\": [147, 118], \"helped_intersection\": 29, \"hurt_intersection\": 21}\n    },\n    \"h3-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.1131, \"hurt_jaccard\": 0.1131, \"helped_sizes\": [171, 144], \"hurt_sizes\": [180, 184], \"helped_intersection\": 32, \"hurt_intersection\": 37},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.1056, \"hurt_jaccard\": 0.0976, \"helped_sizes\": [171, 164], \"hurt_sizes\": [180, 146], \"helped_intersection\": 32, \"hurt_intersection\": 29},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0883, \"hurt_jaccard\": 0.134, \"helped_sizes\": [144, 164], \"hurt_sizes\": [184, 146], \"helped_intersection\": 25, \"hurt_intersection\": 39}\n    }\n  },\n  \"jaccard_null_model\": {\n    \"h24-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0667, \"J_null\": 0.0365, \"J_max\": 0.8876, \"normalized_ES\": 0.0354, \"p_value_permutation\": 0.0064, \"n_permutations\": 10000, \"sizes\": [178, 158]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.0795, \"J_null\": 0.0385, \"J_max\": 0.9081, \"normalized_ES\": 0.0472, \"p_value_permutation\": 0.0005, \"n_permutations\": 10000, \"sizes\": [185, 168]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.0833, \"J_null\": 0.0368, \"J_max\": 0.8989, \"normalized_ES\": 0.054, \"p_value_permutation\": 0.0002, \"n_permutations\": 10000, \"sizes\": [178, 160]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.1095, \"J_null\": 0.0314, \"J_max\": 0.6432, \"normalized_ES\": 0.1276, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [185, 119]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0743, \"J_null\": 0.0346, \"J_max\": 0.9875, \"normalized_ES\": 0.0417, \"p_value_permutation\": 0.0011, \"n_permutations\": 10000, \"sizes\": [158, 160]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0913, \"J_null\": 0.0302, \"J_max\": 0.7083, \"normalized_ES\": 0.09, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [168, 119]}\n    },\n    \"h12-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0935, \"J_null\": 0.0369, \"J_max\": 0.9261, \"normalized_ES\": 0.0637, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [176, 163]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.1282, \"J_null\": 0.0373, \"J_max\": 0.7087, \"normalized_ES\": 0.1354, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [206, 146]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.1167, \"J_null\": 0.0364, \"J_max\": 0.9034, \"normalized_ES\": 0.0925, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [176, 159]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.0856, \"J_null\": 0.0313, \"J_max\": 0.5388, \"normalized_ES\": 0.107, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [206, 111]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0842, \"J_null\": 0.0351, \"J_max\": 0.9755, \"normalized_ES\": 0.0522, \"p_value_permutation\": 0.0001, \"n_permutations\": 10000, \"sizes\": [163, 159]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0844, \"J_null\": 0.0273, \"J_max\": 0.7603, \"normalized_ES\": 0.0779, \"p_value_permutation\": 0.0001, \"n_permutations\": 10000, \"sizes\": [146, 111]}\n    },\n    \"h6-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0894, \"J_null\": 0.0358, \"J_max\": 0.9353, \"normalized_ES\": 0.0596, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [170, 159]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.0896, \"J_null\": 0.033, \"J_max\": 0.9363, \"normalized_ES\": 0.0627, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [157, 147]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.0991, \"J_null\": 0.0387, \"J_max\": 0.9189, \"normalized_ES\": 0.0686, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [170, 185]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.087, \"J_null\": 0.0292, \"J_max\": 0.7516, \"normalized_ES\": 0.08, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [157, 118]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0921, \"J_null\": 0.0373, \"J_max\": 0.8595, \"normalized_ES\": 0.0666, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [159, 185]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0861, \"J_null\": 0.0283, \"J_max\": 0.8027, \"normalized_ES\": 0.0746, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [147, 118]}\n    },\n    \"h3-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.1131, \"J_null\": 0.034, \"J_max\": 0.8421, \"normalized_ES\": 0.0978, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [171, 144]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.1131, \"J_null\": 0.0398, \"J_max\": 0.9783, \"normalized_ES\": 0.0781, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [180, 184]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.1056, \"J_null\": 0.0365, \"J_max\": 0.9591, \"normalized_ES\": 0.0749, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [171, 164]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.0976, \"J_null\": 0.0351, \"J_max\": 0.8111, \"normalized_ES\": 0.0806, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [180, 146]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0883, \"J_null\": 0.0333, \"J_max\": 0.878, \"normalized_ES\": 0.0651, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [144, 164]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.134, \"J_null\": 0.0355, \"J_max\": 0.7935, \"normalized_ES\": 0.13, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [184, 146]}\n    }\n  }\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_jaccard_analysis.json",
    "content": "{\n  \"benchmark\": \"arc_easy\",\n  \"n_samples\": 2376,\n  \"jaccard_similarity\": {\n    \"h24-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0667, \"hurt_jaccard\": 0.0795, \"helped_sizes\": [178, 158], \"hurt_sizes\": [185, 168], \"helped_intersection\": 21, \"hurt_intersection\": 26},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.0833, \"hurt_jaccard\": 0.1095, \"helped_sizes\": [178, 160], \"hurt_sizes\": [185, 119], \"helped_intersection\": 26, \"hurt_intersection\": 30},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0743, \"hurt_jaccard\": 0.0913, \"helped_sizes\": [158, 160], \"hurt_sizes\": [168, 119], \"helped_intersection\": 22, \"hurt_intersection\": 24}\n    },\n    \"h12-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0935, \"hurt_jaccard\": 0.1282, \"helped_sizes\": [176, 163], \"hurt_sizes\": [206, 146], \"helped_intersection\": 29, \"hurt_intersection\": 40},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.1167, \"hurt_jaccard\": 0.0856, \"helped_sizes\": [176, 159], \"hurt_sizes\": [206, 111], \"helped_intersection\": 35, \"hurt_intersection\": 25},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0842, \"hurt_jaccard\": 0.0844, \"helped_sizes\": [163, 159], \"hurt_sizes\": [146, 111], \"helped_intersection\": 25, \"hurt_intersection\": 20}\n    },\n    \"h6-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.0894, \"hurt_jaccard\": 0.0896, \"helped_sizes\": [170, 159], \"hurt_sizes\": [157, 147], \"helped_intersection\": 27, \"hurt_intersection\": 25},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.0991, \"hurt_jaccard\": 0.087, \"helped_sizes\": [170, 185], \"hurt_sizes\": [157, 118], \"helped_intersection\": 32, \"hurt_intersection\": 22},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0921, \"hurt_jaccard\": 0.0861, \"helped_sizes\": [159, 185], \"hurt_sizes\": [147, 118], \"helped_intersection\": 29, \"hurt_intersection\": 21}\n    },\n    \"h3-1\": {\n      \"GDN-RetNet\": {\"helped_jaccard\": 0.1131, \"hurt_jaccard\": 0.1131, \"helped_sizes\": [171, 144], \"hurt_sizes\": [180, 184], \"helped_intersection\": 32, \"hurt_intersection\": 37},\n      \"GDN-HGRN2\": {\"helped_jaccard\": 0.1056, \"hurt_jaccard\": 0.0976, \"helped_sizes\": [171, 164], \"hurt_sizes\": [180, 146], \"helped_intersection\": 32, \"hurt_intersection\": 29},\n      \"RetNet-HGRN2\": {\"helped_jaccard\": 0.0883, \"hurt_jaccard\": 0.134, \"helped_sizes\": [144, 164], \"hurt_sizes\": [184, 146], \"helped_intersection\": 25, \"hurt_intersection\": 39}\n    }\n  },\n  \"jaccard_null_model\": {\n    \"h24-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0667, \"J_null\": 0.0365, \"J_max\": 0.8876, \"normalized_ES\": 0.0354, \"p_value_permutation\": 0.0064, \"n_permutations\": 10000, \"sizes\": [178, 158]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.0795, \"J_null\": 0.0385, \"J_max\": 0.9081, \"normalized_ES\": 0.0472, \"p_value_permutation\": 0.0005, \"n_permutations\": 10000, \"sizes\": [185, 168]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.0833, \"J_null\": 0.0368, \"J_max\": 0.8989, \"normalized_ES\": 0.054, \"p_value_permutation\": 0.0002, \"n_permutations\": 10000, \"sizes\": [178, 160]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.1095, \"J_null\": 0.0314, \"J_max\": 0.6432, \"normalized_ES\": 0.1276, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [185, 119]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0743, \"J_null\": 0.0346, \"J_max\": 0.9875, \"normalized_ES\": 0.0417, \"p_value_permutation\": 0.0011, \"n_permutations\": 10000, \"sizes\": [158, 160]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0913, \"J_null\": 0.0302, \"J_max\": 0.7083, \"normalized_ES\": 0.09, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [168, 119]}\n    },\n    \"h12-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0935, \"J_null\": 0.0369, \"J_max\": 0.9261, \"normalized_ES\": 0.0637, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [176, 163]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.1282, \"J_null\": 0.0373, \"J_max\": 0.7087, \"normalized_ES\": 0.1354, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [206, 146]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.1167, \"J_null\": 0.0364, \"J_max\": 0.9034, \"normalized_ES\": 0.0925, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [176, 159]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.0856, \"J_null\": 0.0313, \"J_max\": 0.5388, \"normalized_ES\": 0.107, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [206, 111]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0842, \"J_null\": 0.0351, \"J_max\": 0.9755, \"normalized_ES\": 0.0522, \"p_value_permutation\": 0.0001, \"n_permutations\": 10000, \"sizes\": [163, 159]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0844, \"J_null\": 0.0273, \"J_max\": 0.7603, \"normalized_ES\": 0.0779, \"p_value_permutation\": 0.0001, \"n_permutations\": 10000, \"sizes\": [146, 111]}\n    },\n    \"h6-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.0894, \"J_null\": 0.0358, \"J_max\": 0.9353, \"normalized_ES\": 0.0596, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [170, 159]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.0896, \"J_null\": 0.033, \"J_max\": 0.9363, \"normalized_ES\": 0.0627, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [157, 147]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.0991, \"J_null\": 0.0387, \"J_max\": 0.9189, \"normalized_ES\": 0.0686, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [170, 185]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.087, \"J_null\": 0.0292, \"J_max\": 0.7516, \"normalized_ES\": 0.08, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [157, 118]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0921, \"J_null\": 0.0373, \"J_max\": 0.8595, \"normalized_ES\": 0.0666, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [159, 185]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.0861, \"J_null\": 0.0283, \"J_max\": 0.8027, \"normalized_ES\": 0.0746, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [147, 118]}\n    },\n    \"h3-1\": {\n      \"GDN-RetNet_helped\": {\"J_obs\": 0.1131, \"J_null\": 0.034, \"J_max\": 0.8421, \"normalized_ES\": 0.0978, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [171, 144]},\n      \"GDN-RetNet_hurt\": {\"J_obs\": 0.1131, \"J_null\": 0.0398, \"J_max\": 0.9783, \"normalized_ES\": 0.0781, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [180, 184]},\n      \"GDN-HGRN2_helped\": {\"J_obs\": 0.1056, \"J_null\": 0.0365, \"J_max\": 0.9591, \"normalized_ES\": 0.0749, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [171, 164]},\n      \"GDN-HGRN2_hurt\": {\"J_obs\": 0.0976, \"J_null\": 0.0351, \"J_max\": 0.8111, \"normalized_ES\": 0.0806, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [180, 146]},\n      \"RetNet-HGRN2_helped\": {\"J_obs\": 0.0883, \"J_null\": 0.0333, \"J_max\": 0.878, \"normalized_ES\": 0.0651, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [144, 164]},\n      \"RetNet-HGRN2_hurt\": {\"J_obs\": 0.134, \"J_null\": 0.0355, \"J_max\": 0.7935, \"normalized_ES\": 0.13, \"p_value_permutation\": 0.0, \"n_permutations\": 10000, \"sizes\": [184, 146]}\n    }\n  }\n}"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T09:35:58.403229+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_jaccard_analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T09:35:58.403367+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "arc_easy_per_example",
  "type": "data",
  "description": "ARC-Easy per-example classification (helped/hurt/stayed) + cross-architecture convergence sigma with Spearman test",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_per_example.json",
  "tags": "['arc_easy', 'per_example', 'convergence']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "arc_easy_per_example",
    "type": "data",
    "description": "ARC-Easy per-example classification (helped/hurt/stayed) + cross-architecture convergence sigma with Spearman test",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_per_example.json",
    "tags": "['arc_easy', 'per_example', 'convergence']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T09:35:58.403512+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_fc3e36\", \"name\": \"arc_easy_per_example\", \"type\": \"data\", \"description\": \"ARC-Easy per-example classification (helped/hurt/stayed) + cross-architecture convergence sigma with Spearman test\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/arc_easy_per_example.json\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T09:35:34.620815+00:00\", \"tags\": [\"arc_easy\", \"per_example\", \"convergence\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T09:35:58.403655+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "formal_multiplicity_metrics",
  "type": "data",
  "description": "Formal Predictive Multiplicity (Marx et al. 2020): ambiguity alpha + discrepancy delta for ARC-Easy and LAMBADA",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/formal_multiplicity_metrics.json",
  "tags": "['multiplicity', 'arc_easy', 'lambada', 'ambiguity', 'discrepancy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "formal_multiplicity_metrics",
    "type": "data",
    "description": "Formal Predictive Multiplicity (Marx et al. 2020): ambiguity alpha + discrepancy delta for ARC-Easy and LAMBADA",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/formal_multiplicity_metrics.json",
    "tags": "['multiplicity', 'arc_easy', 'lambada', 'ambiguity', 'discrepancy']"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T09:35:58.403806+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_4ba617\", \"name\": \"formal_multiplicity_metrics\", \"type\": \"data\", \"description\": \"Formal Predictive Multiplicity (Marx et al. 2020): ambiguity alpha + discrepancy delta for ARC-Easy and LAMBADA\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/formal_multiplicity_metrics.json\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T09:35:37.041991+00:00\", \"tags\": [\"multiplicity\", \"arc_easy\", \"lambada\", \"ambiguity\", \"discrepancy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T09:35:58.403940+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "arc_easy_jaccard_analysis",
  "type": "data",
  "description": "ARC-Easy cross-architecture Jaccard similarity with null model, normalized ES, and 10K permutation tests",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_jaccard_analysis.json",
  "tags": "['arc_easy', 'jaccard', 'permutation_test', 'null_model']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "arc_easy_jaccard_analysis",
    "type": "data",
    "description": "ARC-Easy cross-architecture Jaccard similarity with null model, normalized ES, and 10K permutation tests",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arc_easy_jaccard_analysis.json",
    "tags": "['arc_easy', 'jaccard', 'permutation_test', 'null_model']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T09:35:58.404081+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_04d552\", \"name\": \"arc_easy_jaccard_analysis\", \"type\": \"data\", \"description\": \"ARC-Easy cross-architecture Jaccard similarity with null model, normalized ES, and 10K permutation tests\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/arc_easy_jaccard_analysis.json\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T09:35:38.854585+00:00\", \"tags\": [\"arc_easy\", \"jaccard\", \"permutation_test\", \"null_model\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-20T09:35:58.404257+00:00_

三个 artifacts 全部注册完成。以下是关键结果摘要：

### A. Per-Example Classification (ARC-Easy, N=2376)

| Arch | Ratio | Helped | Hurt | Net |
|------|-------|--------|------|-----|
| GDN | h24-1 | 178 | 185 | **-7** |
| GDN | h12-1 | 176 | 206 | **-30** |
| GDN | h6-1 | 170 | 157 | **+13** |
| GDN | h3-1 | 171 | 180 | **-9** |
| RetNet | h24-1 | 158 | 168 | **-10** |
| RetNet | h12-1 | 163 | 146 | **+17** |
| RetNet | h6-1 | 159 | 147 | **+12** |
| RetNet | h3-1 | 144 | 184 | **-40** |
| HGRN2 | h24-1 | 160 | 119 | **+41** |
| HGRN2 | h12-1 | 159 | 111 | **+48** |
| HGRN2 | h6-1 | 185 | 118 | **+67** |
| HGRN2 | h3-1 | 164 | 146 | **+18** |

HGRN2 在所有 ratio 下 attention 层都有正向 net effect；GDN/RetNet 混合。

### B-C. Jaccard + Null Model

所有 24 个 Jaccard 比较均显著高于 null model（22/24 p<0.001，2/24 p<0.01）。Normalized ES 范围 0.035–0.135，说明跨架构 helped/hurt 重叠虽然显著但绝对幅度低——不同架构倾向于在不同样本上受 attention 影响。

### D. Convergence σ

mean σ 在 pure(0.0964) → h24-1(0.1067) → h12-1(0.1052) → h6-1(0.0948) → h3-1(0.0990) 之间无单调趋势。Spearman ρ=-0.20, p=0.78 (ns)——attention ratio 与跨架构分歧无显著线性关系。

### E. Multiplicity Metrics

| Benchmark | Ratio | α (ambiguity) | δ (discrepancy) |
|-----------|-------|---------------|-----------------|
| ARC-Easy | pure | 0.205 | 2.55 |
| ARC-Easy | h24-1 | 0.226 | 2.98 |
| ARC-Easy | h12-1 | 0.223 | 3.12 |
| ARC-Easy | h6-1 | 0.201 | 2.32 |
| ARC-Easy | h3-1 | 0.210 | 2.66 |
| LAMBADA | pure | 0.307 | 0.61 |
| LAMBADA | h24-1 | 0.300 | 0.58 |
| LAMBADA | h12-1 | 0.316 | 0.55 |
| LAMBADA | h6-1 | 0.294 | 0.53 |
| LAMBADA | h3-1 | 0.296 | 0.55 |

LAMBADA 的 α 高于 ARC-Easy（~0.30 vs ~0.21），但 δ 低得多（~0.55 vs ~2.7），说明 LAMBADA 上架构间分歧更频繁，但一致正确时 confidence 更接近。ARC-Easy 上 h12-1 的 δ 最高（3.12），表明该 ratio 下即使都答对，3 个架构的 confidence 差异最大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_arc-easy-per-example-full_20260520T092702"
}
```

</details>

---
