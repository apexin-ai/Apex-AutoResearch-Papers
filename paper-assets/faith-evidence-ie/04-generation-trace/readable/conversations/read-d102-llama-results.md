# read d102 llama results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_read_d102_llama_results_20260518T112149.jsonl`
- **Structured JSON:** [`b407d1cca526842b9a7d.json`](../../sessions/b4/b407d1cca526842b9a7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-18T11:22:20.973838+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T11:22:20.974279+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T11:22:20.974582+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/eval_results -path \"*llama*\" -name \"metrics.json\" -mmin -180 2>/dev/null; echo \"---\"; ls -lt /root/autodl-tmp/eval_results/ | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/eval_results -path \"*llama*\" -name \"metrics.json\" -mmin -180 2>/dev/null; echo \"---\"; ls -lt /root/autodl-tmp/eval_results/ | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T11:22:20.974869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/d102_llama_k1_s42/metrics.json\\n---\\ntotal 1472\\n-rw-r--r-- 1 root root  20822 May 18 18:52 d102_llama_k1_s42.log\\ndrwxr-xr-x 2 root root     62 May 18 18:52 d102_llama_k1_s42\\n-rw-r--r-- 1 root root  20647 May 18 18:14 d102_1_7b_k1_s42.log\\ndrwxr-xr-x 2 root root     50 May 18 18:14 d102_1_7b_k1_s42\\ndrwxr-xr-x 2 root root      6 May 18 16:27 d102_8b_k1_s43\\ndrwxr-xr-x 2 root root      6 May 18 16:27 d102_8b_k1_s42\\n-rw-r--r-- 1 root root  15689 May 18 12:09 qualitative_case_study.json\\ndrwxr-xr-x 2 root root     81 May 18 03:51 plan_006_qwen3_1_7b_rsft_test\\n-rw-r--r-- 1 root root  21123 May 18 03:00 plan_006_qwen3_8b_rsft_test.log\\ndrwxr-xr-x 2 root root     97 May 18 03:00 plan_006_qwen3_8b_rsft_test\\n-rw-r--r-- 1 root root 388230 May 18 02:46 fig_edcr_relations.png\\n-rw-r--r-- 1 root root  33324 May 18 02:46 fig_edcr_relations.pdf\\n-rw-r--r-- 1 root root   1707 May 18 02:46 plot_fig_edcr_relations.py\\ndrwxr-xr-x 2 root root     62 May 18 02:35 plan_006_llama_rsft_seed43_eval_r2\\n-rw-r--r-- 1 root root  21042 May 18 02:29 plan_006_llama_rsft_test.log\\ndrwxr-xr-x 2 root root     97 May 18 02:29 plan_006_llama_rsft_test\\n-rw-r--r-- 1 root root  20683 May 18 00:44 plan_006_qwen3_1_7b_rsft_seed43_eval.log\\ndrwxr-xr-x 2 root root     62 May 18 00:44 plan_006_qwen3_1_7b_rsft_seed43_eval\\ndrwxr-xr-x 2 root root      6 May 18 00:00 plan_006_llama_rsft_seed43_eval\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:22:20.975027+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d102_llama_k1_s42/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d102_llama_k1_s42/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T11:22:20.975215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5875197867199867,\\n  \\\"recall\\\": 0.5803637560694593,\\n  \\\"f1\\\": 0.5839198476442825,\\n  \\\"ign_precision\\\": 0.565481039008055,\\n  \\\"ign_recall\\\": 0.5773958044543018,\\n  \\\"ign_f1\\\": 0.5713763145861911,\\n  \\\"tp\\\": 7052,\\n  \\\"pred_count\\\": 12003,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8036892621475705,\\n  \\\"evi_recall\\\": 0.8449349625541979,\\n  \\\"evi_f1\\\": 0.8237961646362553,\\n  \\\"n_evaluated\\\": 14227,\\n  \\\"edcr\\\": 0.5798510388083105,\\n  \\\"n_distractor_citations\\\": 14792,\\n  \\\"n_total_citations\\\": 25510,\\n  \\\"evi_joint_precision\\\": 0.45292645360030803,\\n  \\\"evi_joint_recall\\\": 0.48855199626187634,\\n  \\\"evi_f1_joint\\\": 0.4700651896995279,\\n  \\\"evi_tp\\\": 9410,\\n  \\\"evi_pred_total\\\": 20776,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.8395939086294416,\\n  \\\"evidence_format_rate\\\": 0.8395939086294416,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 827,\\n  \\\"n_evidence_valid\\\": 827,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 14627,\\n  \\\"n_truncated\\\": 158,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 8667.7,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d102_llama_k1_s42\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n 
…[truncated 140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_read_d102_llama_results_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-18T11:22:20.975500+00:00_

D102 LLaMA-3.1-8B k=1 s42 结果：

| 指标 | k=1 (本次) | k=3 (旧) | 变化 |
|------|-----------|----------|------|
| rel_f1 | **0.5839** | 0.3936 | +19.03 |
| ign_f1 | **0.5714** | 0.3801 | +19.13 |
| evi_f1 | **0.8238** | 0.8026 | +2.12 |
| edcr | **0.5799** | 0.6696 | -8.97 |
| evi_f1_joint | **0.4701** | — | — |

格式/数量：
- n_predictions: 14,627
- n_truncated: 158
- n_format_ok: 984/985 (99.9%)
- field_compliance: 83.96%

k=1 的 rel_f1/ign_f1 大幅提升（+19 pts），evi_f1 小幅提升。edcr 下降约 9 pts，说明 k=1 模型的 evidence 精度相对关系抽取精度的比例下降了（关系抽取精度从 0.588 vs k=3 可能更低，但关系召回大幅提升拉高了 F1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_read_d102_llama_results_20260518T112149"
}
```

</details>

---
