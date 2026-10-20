# debug matched ablation check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_debug_matched_ablation_check_20260519T040251.jsonl`
- **Structured JSON:** [`c74e278ff31db8d5dfa1.json`](../../sessions/c7/c74e278ff31db8d5dfa1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-19T04:03:43.122982+00:00_

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
  "session": "worker_debug_matched_ablation_check_20260519T040251",
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

_source line 2 · 2026-05-19T04:03:43.123414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T04:03:43.123592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -50 /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -50 /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T04:03:43.123768+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [6160/10500 passes, 896s, 6.9 pass/s, ETA 631s]\\n  [6300/10500 passes, 916s, 6.9 pass/s, ETA 611s]\\n  [6440/10500 passes, 937s, 6.9 pass/s, ETA 591s]\\n  [6580/10500 passes, 957s, 6.9 pass/s, ETA 570s]\\n  [6720/10500 passes, 978s, 6.9 pass/s, ETA 550s]\\n  [6860/10500 passes, 998s, 6.9 pass/s, ETA 530s]\\n  [7000/10500 passes, 1019s, 6.9 pass/s, ETA 509s]\\n\\n[Task 3/3] push_the_plate_to_the_front_of_the_stove\\n  Instruction: push the plate to the front of the stove\\n  [7140/10500 passes, 1039s, 6.9 pass/s, ETA 489s]\\n  [7280/10500 passes, 1059s, 6.9 pass/s, ETA 468s]\\n  [7420/10500 passes, 1079s, 6.9 pass/s, ETA 448s]\\n  [7560/10500 passes, 1100s, 6.9 pass/s, ETA 428s]\\n  [7700/10500 passes, 1120s, 6.9 pass/s, ETA 407s]\\n  [7840/10500 passes, 1141s, 6.9 pass/s, ETA 387s]\\n  [7980/10500 passes, 1161s, 6.9 pass/s, ETA 367s]\\n  [8120/10500 passes, 1181s, 6.9 pass/s, ETA 346s]\\n  [8260/10500 passes, 1201s, 6.9 pass/s, ETA 326s]\\n  [8400/10500 passes, 1222s, 6.9 pass/s, ETA 305s]\\n  [8540/10500 passes, 1242s, 6.9 pass/s, ETA 285s]\\n  [8680/10500 passes, 1262s, 6.9 pass/s, ETA 265s]\\n  [8820/10500 passes, 1282s, 6.9 pass/s, ETA 244s]\\n  [8960/10500 passes, 1303s, 6.9 pass/s, ETA 224s]\\n  [9100/10500 passes, 1323s, 6.9 pass/s, ETA 204s]\\n  [9240/10500 passes, 1344s, 6.9 pass/s, ETA 183s]\\n  [9380/10500 passes, 1364s, 6.9 pass/s, ETA 163s]\\n  [9520/10500 passes, 1384s, 6.9 pass/s, ETA 142s]\\n  [9660/10500 passes, 1405s, 6.9 pass/s, ETA 122s]\\n  [9800/10500 passes, 1425s, 6.9 pass/s, ETA 102s]\\n  [9940/10500 passes, 1445s, 6.9 pass/s, ETA 81s]\\n  [10080/10500 passes, 1466s, 6.9 pass/s, ETA 61s]\\n  [10220/10500 passes, 1486s, 6.9 pass/s, ETA 41s]\\n  [10360/10500 passes, 1506s, 6.9 pass/s, ETA 20s]\\n  [10500/10500 passes, 1527s, 6.9 pass/s, ETA 0s]\\n\\nComputing metrics...\\n  Random seed=42: token_d=3.412, traj_d=0.606\\n  Random seed=123: token_d=2.895, traj_d=0.568\\n  Random seed=456:
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T04:03:43.123946+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T04:03:43.124124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 4842 May 19 12:00 /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T04:03:43.124292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json')); print(json.dumps(d, indent=2)[:2000])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json')); print(json.dumps(d, indent=2)[:2000])\""
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T04:03:43.124433+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T04:03:43.124557+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T04:03:43.124764+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"random_24\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456,\\n      789,\\n      1024\\n    ],\\n    \\\"per_seed\\\": [\\n      {\\n        \\\"seed\\\": 42,\\n        \\\"heads\\\": [\\n          0,\\n          1,\\n          2,\\n          3,\\n          4,\\n          5,\\n          8,\\n          9,\\n          11,\\n          12,\\n          13,\\n          15,\\n          16,\\n          17,\\n          18,\\n          21,\\n          22,\\n          23,\\n          24,\\n          25,\\n          26,\\n          27,\\n          29,\\n          30\\n        ],\\n        \\\"token_d\\\": 3.411908037939124,\\n        \\\"traj_d\\\": 0.6060861623601432,\\n        \\\"traj_ci\\\": [\\n          0.5734082708269367,\\n          0.641663851081951\\n        ],\\n        \\\"mse_gt_baseline\\\": 0.49734446381652286,\\n        \\\"mse_gt_ablated\\\": 0.50397884399592\\n      },\\n      {\\n        \\\"seed\\\": 123,\\n        \\\"heads\\\": [\\n          0,\\n          1,\\n          3,\\n          4,\\n          5,\\n          7,\\n          8,\\n          9,\\n          10,\\n          11,\\n          12,\\n          14,\\n          15,\\n          16,\\n          18,\\n          20,\\n          21,\\n          22,\\n          23,\\n          24,\\n          25,\\n          26,\\n          27,\\n          31\\n        ],\\n        \\\"token_d\\\": 2.8952300934114135,\\n        \\\"traj_d\\\": 0.5677341221087594,\\n        \\\"traj_ci\\\": [\\n          0.5355516691083986,\\n          0.6010695863048189\\n        ],\\n        \\\"mse_gt_baseline\\\": 0.49734446381652286,\\n        \\\"mse_gt_ablated\\\": 0.5043645327750472\\n      },\\n      {\\n        \\\"seed\\\": 456,\\n        \\\"heads\\\": [\\n          0,\\n          1,\\n          2,\\n          3,\\n          4,\\n          6,\\n          7,\\n          8,\\n          9,\\n          12,\\n          13,\\n          16,\\n     
…[truncated 3940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T04:03:43.124952+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:CronDelete",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:CronDelete",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T04:03:43.125093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T04:03:43.125215+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "matched_ablation_controls",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "matched_ablation_controls",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T04:03:43.125357+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"matched_ablation_controls\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:01:26.947Z\", \"updated_at\": \"2026-05-19T04:03:28.643Z\", \"conclusion\": \"success\", \"metrics\": {\"instruction_dominant_24_traj_d\": 0.65, \"random_24_mean_traj_d\": 0.601, \"random_24_std_traj_d\": 0.021, \"image_dominant_24_traj_d\": 0.58, \"random_24_mean_token_d\": 3.056, \"random_24_std_token_d\": 0.305, \"image_dominant_24_token_d\": 2.169, \"total_forward_passes\": 10500, \"n_seeds\": 5}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"spec\": {\"command\": \"python3 matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 10500, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"hypothesis\": \"Ablating instruction-dominant attention heads causes greater trajectory deviation than ablating the same number of randomly-selected or image-dominant heads, because instruction-dominant heads carry unique language-grounding signals that cannot be compensated by other heads.\", \"completed_at\": \"2026-05-19T04:02:02.870Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0236}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T04:03:43.125524+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "matched_ablation_controls",
  "field": "metrics",
  "value": "{'random_24_mean_traj_d': 0.601, 'random_24_std_traj_d': 0.021, 'random_24_mean_token_d': 3.056, 'random_24_std_token_d': 0.305, 'image_dominant_24_traj_d': 0.58, 'image_dominant_24_token_d': 2.169, 'instruction_dominant_24_traj_d_ref': 0.65, 'n_tasks': 3, 'n_demos_per_task': 10, 'total_forward_passes': 10500}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "matched_ablation_controls",
    "field": "metrics",
    "value": "{'random_24_mean_traj_d': 0.601, 'random_24_std_traj_d': 0.021, 'random_24_mean_token_d': 3.056, 'random_24_std_token_d': 0.305, 'image_dominant_24_traj_d': 0.58, 'image_dominant_24_token_d': 2.169, 'instruction_dominant_24_traj_d_ref': 0.65, 'n_tasks': 3, 'n_demos_per_task': 10, 'total_forward_passes': 10500}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T04:03:43.125698+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"matched_ablation_controls\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:01:26.947Z\", \"updated_at\": \"2026-05-19T04:03:30.693Z\", \"conclusion\": \"success\", \"metrics\": {\"random_24_mean_traj_d\": 0.601, \"random_24_std_traj_d\": 0.021, \"random_24_mean_token_d\": 3.056, \"random_24_std_token_d\": 0.305, \"image_dominant_24_traj_d\": 0.58, \"image_dominant_24_token_d\": 2.169, \"instruction_dominant_24_traj_d_ref\": 0.65, \"n_tasks\": 3, \"n_demos_per_task\": 10, \"total_forward_passes\": 10500}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"spec\": {\"command\": \"python3 matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 10500, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"hypothesis\": \"Ablating instruction-dominant attention heads causes greater trajectory deviation than ablating the same number of randomly-selected or image-dominant heads, because instruction-dominant heads carry unique language-grounding signals that cannot be compensated by other heads.\", \"completed_at\": \"2026-05-19T04:02:02.870Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0391}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T04:03:43.125843+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "matched_ablation_controls",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "matched_ablation_controls",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T04:03:43.126011+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"matched_ablation_controls\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:01:26.947Z\", \"updated_at\": \"2026-05-19T04:03:31.468Z\", \"conclusion\": \"success\", \"metrics\": {\"random_24_mean_traj_d\": 0.601, \"random_24_std_traj_d\": 0.021, \"random_24_mean_token_d\": 3.056, \"random_24_std_token_d\": 0.305, \"image_dominant_24_traj_d\": 0.58, \"image_dominant_24_token_d\": 2.169, \"instruction_dominant_24_traj_d_ref\": 0.65, \"n_tasks\": 3, \"n_demos_per_task\": 10, \"total_forward_passes\": 10500}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"spec\": {\"command\": \"python3 matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 10500, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"hypothesis\": \"Ablating instruction-dominant attention heads causes greater trajectory deviation than ablating the same number of randomly-selected or image-dominant heads, because instruction-dominant heads carry unique language-grounding signals that cannot be compensated by other heads.\", \"completed_at\": \"2026-05-19T04:02:02.870Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0139}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T04:03:43.126148+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "matched_ablation_controls",
  "field": "log_path",
  "value": "/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "matched_ablation_controls",
    "field": "log_path",
    "value": "/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T04:03:43.126290+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"matched_ablation_controls\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:01:26.947Z\", \"updated_at\": \"2026-05-19T04:03:32.085Z\", \"conclusion\": \"success\", \"metrics\": {\"random_24_mean_traj_d\": 0.601, \"random_24_std_traj_d\": 0.021, \"random_24_mean_token_d\": 3.056, \"random_24_std_token_d\": 0.305, \"image_dominant_24_traj_d\": 0.58, \"image_dominant_24_token_d\": 2.169, \"instruction_dominant_24_traj_d_ref\": 0.65, \"n_tasks\": 3, \"n_demos_per_task\": 10, \"total_forward_passes\": 10500}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"spec\": {\"command\": \"python3 matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 10500, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"hypothesis\": \"Ablating instruction-dominant attention heads causes greater trajectory deviation than ablating the same number of randomly-selected or image-dominant heads, because instruction-dominant heads carry unique language-grounding signals that cannot be compensated by other heads.\", \"completed_at\": \"2026-05-19T04:02:02.870Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0135}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T04:03:43.126442+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "matched_ablation_controls",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "matched_ablation_controls",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T04:03:43.126563+00:00_

called CronDelete

<details open><summary>🔧 Tool call — CronDelete</summary>

```json
{
  "id": "matched_ablation_controls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "CronDelete",
  "tool_args": {
    "id": "matched_ablation_controls"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T04:03:43.126723+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"matched_ablation_controls\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:01:26.947Z\", \"updated_at\": \"2026-05-19T04:03:35.616Z\", \"conclusion\": \"success\", \"metrics\": {\"random_24_mean_traj_d\": 0.601, \"random_24_std_traj_d\": 0.021, \"random_24_mean_token_d\": 3.056, \"random_24_std_token_d\": 0.305, \"image_dominant_24_traj_d\": 0.58, \"image_dominant_24_token_d\": 2.169, \"instruction_dominant_24_traj_d_ref\": 0.65, \"n_tasks\": 3, \"n_demos_per_task\": 10, \"total_forward_passes\": 10500}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"spec\": {\"command\": \"python3 matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 10500, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"hypothesis\": \"Ablating instruction-dominant attention heads causes greater trajectory deviation than ablating the same number of randomly-selected or image-dominant heads, because instruction-dominant heads carry unique language-grounding signals that cannot be compensated by other heads.\", \"completed_at\": \"2026-05-19T04:02:02.870Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0567}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T04:03:43.126863+00:00_

&lt;tool_use_error>No scheduled job with id 'matched_ablation_controls'&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_matched_ablation_check_20260519T040251",
  "tool": "CronDelete",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T04:03:43.127049+00:00_

Cron 已不存在（可能已被清除或未在本 session 创建），无需处理。

**实验结果：成功**

| Condition | traj_d | token_d |
|---|---|---|
| **Instruction-dominant 24** (ref) | **0.650** | — |
| **Random 24** (5 seeds mean±std) | 0.601 ± 0.021 | 3.056 ± 0.305 |
| **Image-dominant 24** | 0.580 | 2.169 |

Instruction-dominant heads 的 ablation 造成的轨迹偏移 (0.650) 大于 random 控制组 (0.601) 和 image-dominant 控制组 (0.580)，且 random 控制组 5 seeds 的标准差仅 0.021，instruction-dominant 的 0.650 落在 random 分布的 ~2.4σ 之外。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_debug_matched_ablation_check_20260519T040251"
}
```

</details>

---
