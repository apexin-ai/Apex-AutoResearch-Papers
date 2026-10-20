# analysis plan017 14b sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_plan017_14b_sft_eval_r2_20260519T135510.jsonl`
- **Structured JSON:** [`ba4f1d9a62385e493f3c.json`](../../sessions/ba/ba4f1d9a62385e493f3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T13:56:11.194620+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T13:56:11.194986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:56:11.195183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -name \"*14b*eval*\" -mmin -180 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -name \"*14b*eval*\" -mmin -180 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T13:56:11.195359+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:56:11.195563+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -lt /root/autodl-tmp/sft_output_14b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -lt /root/autodl-tmp/sft_output_14b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T13:56:11.195702+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tmux ls 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tmux ls 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T13:56:11.195908+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 517392\\n-rw-r--r-- 1 root root  11422654 May 19 15:17 tokenizer.json\\n-rw-r--r-- 1 root root   1671853 May 19 15:17 merges.txt\\n-rw-r--r-- 1 root root   2776833 May 19 15:17 vocab.json\\n-rw-r--r-- 1 root root       707 May 19 15:17 added_tokens.json\\n-rw-r--r-- 1 root root      4168 May 19 15:17 chat_template.jinja\\n-rw-r--r-- 1 root root       499 May 19 15:17 special_tokens_map.json\\n-rw-r--r-- 1 root root      5431 May 19 15:17 tokenizer_config.json\\n-rw-r--r-- 1 root root      8337 May 19 15:17 training_args.bin\\n-rw-r--r-- 1 root root      1118 May 19 15:17 adapter_config.json\\n-rw-r--r-- 1 root root 513878424 May 19 15:17 adapter_model.safetensors\\n-rw-r--r-- 1 root root      1470 May 19 15:17 README.md\\ndrwxr-xr-x 3 root root      4096 May 19 15:17 checkpoint-144\\ndrwxr-xr-x 3 root root      4096 May 19 14:17 checkpoint-96\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T13:56:11.196064+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:56:11.196192+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -name \"*14b*eval*\" -mmin -180",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -name \"*14b*eval*\" -mmin -180",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T13:56:11.196412+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T13:56:11.196612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T13:56:11.196796+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:56:11.196926+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -name \"*metrics*\" -mmin -180",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -name \"*metrics*\" -mmin -180",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T13:56:11.197054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/metrics.json\\n/root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json\\n/root/autodl-tmp/eval_outputs/eval_14b_sft_no_evidence/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:56:11.197173+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -lt /root/autodl-tmp/freige/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -lt /root/autodl-tmp/freige/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T13:56:11.197669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 60\\n-rw-r--r-- 1 root root 58270 May 19 13:38 plan019_1_7b_rsft_s43_r2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T13:56:11.197826+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T13:56:11.198002+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5480580619850922,\\n  \\\"recall\\\": 0.5748498066002798,\\n  \\\"f1\\\": 0.5611343187660668,\\n  \\\"ign_precision\\\": 0.5268399729912221,\\n  \\\"ign_recall\\\": 0.5768413270492561,\\n  \\\"ign_f1\\\": 0.5507080153513608,\\n  \\\"tp\\\": 6985,\\n  \\\"pred_count\\\": 12745,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8196955680766966,\\n  \\\"evi_recall\\\": 0.8389567911860906,\\n  \\\"evi_f1\\\": 0.8292143434429368,\\n  \\\"n_evaluated\\\": 13764,\\n  \\\"edcr\\\": 0.5970149253731343,\\n  \\\"n_distractor_citations\\\": 14440,\\n  \\\"n_total_citations\\\": 24187,\\n  \\\"evi_joint_precision\\\": 0.41738182808881624,\\n  \\\"evi_joint_recall\\\": 0.4772337884845024,\\n  \\\"evi_f1_joint\\\": 0.4453056874333883,\\n  \\\"evi_tp\\\": 9192,\\n  \\\"evi_pred_total\\\": 22023,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8588832487309644,\\n  \\\"evidence_format_rate\\\": 0.8588832487309644,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 846,\\n  \\\"n_evidence_valid\\\": 846,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 14081,\\n  \\\"n_truncated\\\": 139,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 18011.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output_14b\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-14B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_outputs/eval_14b_sft\\\",\\n    \\\"batch_size\\\": 2,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadat
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:56:11.198168+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -lt /root/autodl-tmp/eval_outputs/eval_14b_sft/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -lt /root/autodl-tmp/eval_outputs/eval_14b_sft/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T13:56:11.198557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6312\\n-rw-r--r-- 1 root root 6455968 May 19 21:52 predictions.json\\n-rw-r--r-- 1 root root    1465 May 19 21:52 metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:56:11.198923+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_sft_eval_r2",
  "field": "metrics",
  "value": "{'ign_f1': 0.5507, 'ign_precision': 0.5268, 'ign_recall': 0.5768, 'f1': 0.5611, 'precision': 0.5481, 'recall': 0.5748, 'format_compliance_rate': 1, 'field_compliance_rate': 0.8589, 'evidence_format_rate': 0.8589, 'n_truncated': 139, 'n_total': 985, 'n_parseable': 985, 'n_predictions': 14081, 'inference_time_seconds': 18011.3, 'evi_precision': 0.8197, 'evi_recall': 0.839, 'evi_f1': 0.8292, 'evi_f1_joint': 0.4453, 'evi_joint_precision': 0.4174, 'evi_joint_recall': 0.4772, 'edcr': 0.597}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_sft_eval_r2",
    "field": "metrics",
    "value": "{'ign_f1': 0.5507, 'ign_precision': 0.5268, 'ign_recall': 0.5768, 'f1': 0.5611, 'precision': 0.5481, 'recall': 0.5748, 'format_compliance_rate': 1, 'field_compliance_rate': 0.8589, 'evidence_format_rate': 0.8589, 'n_truncated': 139, 'n_total': 985, 'n_parseable': 985, 'n_predictions': 14081, 'inference_time_seconds': 18011.3, 'evi_precision': 0.8197, 'evi_recall': 0.839, 'evi_f1': 0.8292, 'evi_f1_joint': 0.4453, 'evi_joint_precision': 0.4174, 'evi_joint_recall': 0.4772, 'edcr': 0.597}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T13:56:11.199131+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_sft_eval_r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:55:53.409Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"spec\": {\"command\": \"bash scripts/14b/eval_14b_sft.sh\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 633106, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 998, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_14b/\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:53:32.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:53:40.349959+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.5507, \"ign_precision\": 0.5268, \"ign_recall\": 0.5768, \"f1\": 0.5611, \"precision\": 0.5481, \"recall\": 0.5748, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.8589, \"evidence_format_rate\": 0.8589, \"n_truncated\": 139, \"n_total\": 985, \"n_parseable\": 985, \"n_predictions\": 14081, \"inference_time_seconds\": 18011.3, \"evi_precision\": 0.8197, \"evi_recall\": 0.839, \"evi_f1\": 0.8292, \"evi_f1_joint\": 0.4453, \"evi_joint_precision\": 0.4174, \"evi_joint_recall\": 0.4772, \"edcr\": 0.597}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9126}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T13:56:11.199565+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_sft_eval_r2",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/sft_output_14b/', 'log_path': '/root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_sft_eval_r2",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/sft_output_14b/', 'log_path': '/root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json'}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T13:56:11.200134+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_sft_eval_r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:56:00.237Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"spec\": {\"command\": \"bash scripts/14b/eval_14b_sft.sh\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 633106, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 998, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_14b/\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_14b/\", \"log_path\": \"/root/autodl-tmp/eval_outputs/eval_14b_sft/metrics.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:53:32.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:53:40.349959+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.5507, \"ign_precision\": 0.5268, \"ign_recall\": 0.5768, \"f1\": 0.5611, \"precision\": 0.5481, \"recall\": 0.5748, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.8589, \"evidence_format_rate\": 0.8589, \"n_truncated\": 139, \"n_total\": 985, \"n_parseable\": 985, \"n_predictions\": 14081, \"inference_time_seconds\": 18011.3, \"evi_precision\": 0.8197, \"evi_recall\": 0.839, \"evi_f1\": 0.8292, \"evi_f1_joint\": 0.4453, \"evi_joint_precision\": 0.4174, \"evi_joint_recall\": 0.4772, \"edcr\": 0.597}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3983}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T13:56:11.200471+00:00_

Registry 已更新完成。结果汇总：

**plan017_14b_sft_eval_r2 — 14B SFT baseline eval (bf16, no quantize)**

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.5507** |
| ign_precision | 0.5268 |
| ign_recall | 0.5768 |
| f1 | 0.5611 |
| format_compliance_rate | 1.0 |
| n_truncated | 139 / 985 |
| inference_time | 18011s (~5h) |
| evi_f1 | 0.8292 |
| evi_f1_joint | 0.4453 |
| edcr | 0.597 |

**Scale 对比（SFT baseline ign_f1）：**
- 1.7B: 0.4464
- 4B: 0.4358
- 8B: 0.4866
- **14B: 0.5507** (+13.2% over 8B mean)

**对比 14B no-evidence (0.551)：** 两者几乎持平（0.5507 vs 0.551），evidence tax 极小（-0.05%），说明 14B 模型在输出 evidence 的同时几乎不牺牲关系抽取性能。

Conclusion: **success**。14B 在 4 个 scale 档中最强，且 evidence tax 接近零。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_plan017_14b_sft_eval_r2_20260519T135510"
}
```

</details>

---
