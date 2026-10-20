# analysis mvp2 sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_mvp2_sft_eval_r2_20260514T145314.jsonl`
- **Structured JSON:** [`92d23cc71d1ed1899d68.json`](../../sessions/92/92d23cc71d1ed1899d68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T14:54:23.072755+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T14:54:23.073254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T14:54:23.073517+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -200 ~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -200 ~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T14:54:23.073838+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 22:34:07,016 WARNING Failed to parse output for doc Vineeth Sreenivasan\\n2026-05-14 22:34:07,016 WARNING Failed to parse output for doc How to Save a Life (Grey's Anatomy)\\n2026-05-14 22:34:07,016 WARNING Failed to parse output for doc Pete Murray\\n2026-05-14 22:34:07,016 WARNING Failed to parse output for doc Howard the Duck (film)\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc X-Men Legends II: Rise of Apocalypse\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc Safdar Jung (film)\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc Odessa (Bee Gees album)\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc Sappy Records\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc George Nostrand\\n2026-05-14 22:34:07,017 WARNING Failed to parse output for doc Christian worship\\n2026-05-14 22:34:07,018 WARNING Failed to parse output for doc Ernst Anton Nicolai\\n2026-05-14 22:34:07,018 WARNING Failed to parse output for doc Marc Savoy\\n2026-05-14 22:34:07,018 WARNING Failed to parse output for doc Waldshut station\\n2026-05-14 22:34:07,018 WARNING Failed to parse output for doc Lloyd Fredendall\\n2026-05-14 22:34:07,018 WARNING Failed to parse output for doc Foix (river)\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Wayne Gretzky Drive\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Sibiu\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Silvan Elves\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Battle of Samugarh\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Sims-class destroyer\\n2026-05-14 22:34:07,019 WARNING Failed to parse output for doc Paul Beliën\\n2026-05-14 22:34:07,020 WARNING Failed to parse output for doc Two Doors Down\\n2026-05-14 22:34:07,020 WARNING Failed to parse output for doc United States Naval Forces Germany\\n2026-05-14 
…[truncated 6411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T14:54:23.074066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T14:54:23.074276+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7664\\ndrwxr-xr-x  2 root root      62 May 14 22:34 .\\ndrwxr-xr-x 22 root root    4096 May 14 20:45 ..\\n-rw-r--r--  1 root root    1226 May 14 22:34 metrics.json\\n-rw-r--r--  1 root root 7839031 May 14 22:34 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T14:54:23.074485+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'mvp2_sft_eval_r2'}",
  "project": "faith-evidence-ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'mvp2_sft_eval_r2'}",
    "project": "faith-evidence-ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T14:54:23.074666+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1003}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T14:54:23.074882+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_eval_results/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/sft_eval_results/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:54:23.075116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4042831453326794,\\n  \\\"recall\\\": 0.40704468768002633,\\n  \\\"f1\\\": 0.4056592167315973,\\n  \\\"ign_precision\\\": 0.4042831453326794,\\n  \\\"ign_recall\\\": 0.40704468768002633,\\n  \\\"ign_f1\\\": 0.4056592167315973,\\n  \\\"tp\\\": 4946,\\n  \\\"pred_count\\\": 12234,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8034592626308603,\\n  \\\"evi_recall\\\": 0.79242233794218,\\n  \\\"evi_f1\\\": 0.7979026352664649,\\n  \\\"n_evaluated\\\": 18460,\\n  \\\"edcr\\\": 0.7117758474299524,\\n  \\\"n_distractor_citations\\\": 21796,\\n  \\\"n_total_citations\\\": 30622,\\n  \\\"format_compliance_rate\\\": 0.6263959390862944,\\n  \\\"field_compliance_rate\\\": 0.6263959390862944,\\n  \\\"evidence_format_rate\\\": 0.6263959390862944,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 617,\\n  \\\"n_field_complete\\\": 617,\\n  \\\"n_evidence_valid\\\": 617,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 18815,\\n  \\\"n_truncated\\\": 367,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 6484.7,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/sft_eval_results\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:54:23.075345+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "fields": "['*']",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "fields": "['*']",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T14:54:23.075775+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mvp2_sft_eval_r2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:52:20.595Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}}, \"mvp2_sft_eval_r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:52:38.174Z\", \"updated_at\": \"2026-05-14T13:52:38.174Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"
…[truncated 12381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:54:23.076013+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp2_sft_eval_r2",
  "field": "metrics",
  "value": "{'rel_f1': 0.4057, 'ign_f1': 0.4057, 'evi_f1': 0.7979, 'edcr': 0.7118, 'precision': 0.4043, 'recall': 0.407, 'evi_precision': 0.8035, 'evi_recall': 0.7924, 'format_ok_rate': 0.998, 'format_compliance_rate': 0.626, 'n_parseable': 617, 'n_truncated': 367, 'n_predictions': 18815, 'inference_time_seconds': 6484.7}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp2_sft_eval_r2",
    "field": "metrics",
    "value": "{'rel_f1': 0.4057, 'ign_f1': 0.4057, 'evi_f1': 0.7979, 'edcr': 0.7118, 'precision': 0.4043, 'recall': 0.407, 'evi_precision': 0.8035, 'evi_recall': 0.7924, 'format_ok_rate': 0.998, 'format_compliance_rate': 0.626, 'n_parseable': 617, 'n_truncated': 367, 'n_predictions': 18815, 'inference_time_seconds': 6484.7}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:54:23.076202+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp2_sft_eval_r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:02.100Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1943}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T14:54:23.076424+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp2_sft_eval_r2",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/sft_eval_results/",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp2_sft_eval_r2",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/sft_eval_results/",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:54:23.076594+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp2_sft_eval_r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:06.879Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_results/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1645}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:54:23.076733+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp2_sft_eval_r2",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp2_sft_eval_r2",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T14:54:23.076934+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp2_sft_eval_r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:07.338Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 7701.4, \"gpu_hours\": 2.14}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_results/\", \"completed_at\": \"2026-05-14T14:54:07.338Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed
…[truncated 22 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T14:54:23.077134+00:00_

Registry 已更新为 DONE/success。以下是 mvp2_sft_eval_r2 的完整结果：

## SFT Baseline Eval 结果 (DocRED dev, 985 samples)

| 指标 | 数值 |
|------|------|
| **Rel-F1** | **0.4057** |
| **Ign-F1** | 0.4057 |
| **Precision** | 0.4043 |
| **Recall** | 0.4070 |
| **Evi-F1** | **0.7979** |
| Evi-Precision | 0.8035 |
| Evi-Recall | 0.7924 |
| **EDCR** | **0.7118** |
| Format OK | 983/985 (99.8%) |
| **Parse 成功率** | **617/985 (62.6%)** |
| 截断数 | 367/985 (37.3%) |
| 总预测数 | 18,815 |
| 推理耗时 | 6,484.7s (~108min) |

## 分析

**关键问题：截断率过高。** 367/985 (37.3%) 的输出在 max_new_tokens=1024 处被截断，导致 JSON 不完整、无法解析。这是 format_ok_rate (99.8%) 与实际 parse 成功率 (62.6%) 之间巨大差距的原因——模型生成了合法 JSON 格式，但被长度截断后变成不完整的输出。

**对 GRPO 实验的 baseline 参考意义：**
- Rel-F1=0.4057 是 GRPO 需要超越的关系抽取基线
- Evi-F1=0.7979 说明 SFT 模型已经学到了较好的证据定位能力
- EDCR=0.7118 表示约 71% 的引用是针对性的（非 distractor），GRPO 的 CED reward 目标是提升这个值
- 实际可用的只有 62.6% 的样本，**mvp2_sft_eval_r3（统一 eval 代码 + truncated JSON 修复）应能显著提升 parse 率，从而给出更准确的 baseline 数值**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mvp2_sft_eval_r2_20260514T145314"
}
```

</details>

---
