# analysis alpha sweep a025 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_alpha_sweep_a025_s43_20260515T173716.jsonl`
- **Structured JSON:** [`4ce776ecc1e504d10d64.json`](../../sessions/4c/4ce776ecc1e504d10d64.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T17:38:32.780218+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:38:32.780521+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:38:32.780673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -50 ~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -50 ~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T17:38:32.780801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T17:38:32.780997+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 24%|██▍       | 1200/5000 [01:16<04:03, 15.62it/s]\\r 24%|██▍       | 1202/5000 [01:17<04:03, 15.58it/s]\\r 24%|██▍       | 1204/5000 [01:17<04:03, 15.57it/s]\\r 24%|██▍       | 1206/5000 [01:17<04:04, 15.54it/s]\\r 24%|██▍       | 1208/5000 [01:17<04:04, 15.50it/s]\\r 24%|██▍       | 1210/5000 [01:17<04:05, 15.46it/s]\\r 24%|██▍       | 1212/5000 [01:17<04:07, 15.32it/s]\\r 24%|██▍       | 1214/5000 [01:17<04:06, 15.35it/s]\\r 24%|██▍       | 1216/5000 [01:17<04:04, 15.45it/s]\\r 24%|██▍       | 1218/5000 [01:18<04:05, 15.39it/s]\\r 24%|██▍       | 1220/5000 [01:18<04:04, 15.49it/s]\\r 24%|██▍       | 1222/5000 [01:18<04:02, 15.56it/s]\\r 24%|██▍       | 1224/5000 [01:18<04:01, 15.63it/s]\\r 25%|██▍       | 1226/5000 [01:18<04:00, 15.68it/s]\\r 25%|██▍       | 1228/5000 [01:18<04:00, 15.71it/s]\\r 25%|██▍       | 1230/5000 [01:18<03:59, 15.71it/s]\\r 25%|██▍       | 1232/5000 [01:18<04:01, 15.63it/s]\\r 25%|██��       | 1234/5000 [01:19<04:01, 15.61it/s]\\r 25%|██▍       | 1236/5000 [01:19<04:00, 15.67it/s]\\r 25%|██▍       | 1238/5000 [01:19<03:59, 15.71it/s]\\r 25%|██▍       | 1240/5000 [01:19<03:59, 15.72it/s]\\r 25%|██▍       | 1242/5000 [01:19<03:58, 15.74it/s]\\r 25%|██▍       | 1244/5000 [01:19<03:58, 15.76it/s]\\r 25%|██▍       | 1246/5000 [01:19<03:57, 15.78it/s]\\r 25%|██▍       | 1248/5000 [01:20<03:57, 15.79it/s]\\r 25%|██▌       | 1250/5000 [01:20<03:57, 15.80it/s]\\r 25%|██▌       | 1252/5000 [01:20<03:57, 15.81it/s]\\r 25%|██▌       | 1254/5000 [01:20<03:57, 15.79it/s]\\r 25%|██▌       | 1256/5000 [01:20<03:57, 15.76it/s]\\r 25%|██▌       | 1258/5000 [01:20<03:57, 15.75it/s]\\r 25%|██▌       | 1260/5000 [01:20<03:57, 15.76it/s]\\r 25%|██▌       | 1262/5000 [01:20<03:57, 15.74it/s]\\r 25%|██▌       | 1264/5000 [01:21<03:58, 15.70it/s]\\r 25%|██▌       | 1266/5000 [01:21<03:58, 15.63it/s]\\r 25%|██▌       | 1268/5000 [01:21<03:59, 15.61it/s]\\r 25%|██▌       | 1270/5000 [01:21<03:58, 15.64it/s
…[truncated 6481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:38:32.781168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20\\ndrwxr-xr-x 13 root root 4096 May 16 01:36 .\\ndrwxr-xr-x  8 root root 4096 May 15 21:16 ..\\n-rw-r--r--  1 root root    2 May 16 01:36 EXIT_CODE\\n-rw-r--r--  1 root root 4026 May 16 01:36 all_metrics.json\\n-rw-r--r--  1 root root  400 May 15 21:16 config.json\\ndrwxr-xr-x  3 root root   60 May 15 21:32 gen_0\\ndrwxr-xr-x  5 root root  101 May 15 21:53 gen_1\\ndrwxr-xr-x  5 root root  101 May 16 01:36 gen_10\\ndrwxr-xr-x  5 root root  101 May 15 22:18 gen_2\\ndrwxr-xr-x  5 root root  101 May 15 22:42 gen_3\\ndrwxr-xr-x  5 root root  101 May 15 23:08 gen_4\\ndrwxr-xr-x  5 root root  101 May 15 23:32 gen_5\\ndrwxr-xr-x  5 root root  101 May 15 23:57 gen_6\\ndrwxr-xr-x  5 root root  101 May 16 00:22 gen_7\\ndrwxr-xr-x  5 root root  101 May 16 00:46 gen_8\\ndrwxr-xr-x  5 root root  101 May 16 01:11 gen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:38:32.781374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:38:32.781585+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010826090501434389,\\n    \\\"distinct_1\\\": 0.09833431219002871,\\n    \\\"distinct_2\\\": 0.5131779657560506,\\n    \\\"distinct_3\\\": 0.8056693041846806,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03350582133330568,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.99525113296896,\\n    \\\"self_bleu\\\": 0.010964385056351856,\\n    \\\"distinct_1\\\": 0.09963439966763606,\\n    \\\"distinct_2\\\": 0.5176943722008492,\\n    \\\"distinct_3\\\": 0.8097101738292286,\\n    \\\"ece\\\": 0.0076778173530561425,\\n    \\\"effective_rank\\\": 49.62792201994895,\\n    \\\"perplexity\\\": 19.454806645474676,\\n    \\\"mauve\\\": 0.029947808319125253,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0369130246796425,\\n    \\\"self_bleu\\\": 0.011788819903809158,\\n    \\\"distinct_1\\\": 0.08071966174022462,\\n    \\\"distinct_2\\\": 0.4266967830681214,\\n    \\\"distinct_3\\\": 0.710895917840981,\\n    \\\"ece\\\": 0.010119364189508782,\\n    \\\"effective_rank\\\": 49.98154412868931,\\n    \\\"perplexity\\\": 20.217124992357697,\\n    \\\"mauve\\\": 0.03296418724600133,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0516011917111325,\\n    \\\"self_bleu\\\": 0.01191989821438278,\\n    \\\"distinct_1\\\": 0.07245097273224471,\\n    \\\"distinct_2\\\": 0.37007867863644534,\\n    \\\"distinct_3\\\": 0.6218551739225553,\\n    \\\"ece\\\": 0.009433239364880504,\\n    \\\"effective_rank\\\": 50.41024162592397,\\n    \\\"perplexity\\\": 20.71042459817368,\\n    \\\"mauve\\\": 0.031549757237980286,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0337417115694487,\\n    \\\"self_bleu\\\": 0.010952384795367334,\\n    \\\"distinct_1\\\"
…[truncated 3112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:38:32.781768+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43 -name \"*.json\" -not -name \"all_metrics.json\" -not -name \"config.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43 -name \"*.json\" -not -name \"all_metrics.json\" -not -name \"config.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:38:32.781947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_2/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_3/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/r
…[truncated 5933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:38:32.782122+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a025_s43",
  "field": "conclusion",
  "value": "success",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a025_s43",
    "field": "conclusion",
    "value": "success",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:38:32.782292+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a025_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:38:01.529Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"progress\": \"gen 5/10 step 3606/5000, ~57%\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:36:22.072334+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1481}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:38:32.782463+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a025_s43",
  "field": "metrics",
  "value": "{'gen0': {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.09833, 'distinct_2': 0.5132, 'distinct_3': 0.8057, 'effective_rank': 46.61, 'mauve': 0.03351}, 'gen10': {'token_entropy': 3.0723, 'ece': 0.02146, 'perplexity': 21.899, 'distinct_1': 0.05849, 'distinct_2': 0.2236, 'distinct_3': 0.333, 'effective_rank': 45.37, 'mauve': 0.01871}, 'drift_pct': {'token_entropy': -5, 'ece': 98.6, 'perplexity': -18.7, 'distinct_1': -40.5, 'distinct_2': -56.4, 'distinct_3': -58.7, 'effective_rank': -2.7, 'mauve': -44.2}}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a025_s43",
    "field": "metrics",
    "value": "{'gen0': {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.09833, 'distinct_2': 0.5132, 'distinct_3': 0.8057, 'effective_rank': 46.61, 'mauve': 0.03351}, 'gen10': {'token_entropy': 3.0723, 'ece': 0.02146, 'perplexity': 21.899, 'distinct_1': 0.05849, 'distinct_2': 0.2236, 'distinct_3': 0.333, 'effective_rank': 45.37, 'mauve': 0.01871}, 'drift_pct': {'token_entropy': -5, 'ece': 98.6, 'perplexity': -18.7, 'distinct_1': -40.5, 'distinct_2': -56.4, 'distinct_3': -58.7, 'effective_rank': -2.7, 'mauve': -44.2}}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T17:38:32.782643+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a025_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:38:08.974Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.09833, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.03351}, \"gen10\": {\"token_entropy\": 3.0723, \"ece\": 0.02146, \"perplexity\": 21.899, \"distinct_1\": 0.058
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:38:32.782805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a025_s43",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a025_s43",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:38:32.782960+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a025_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:38:09.717Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.09833, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.03351}, \"gen10\": {\"token_entropy\": 3.0723, \"ece\": 0.02146, \"perplexity\": 21.899, \"distinct_1\": 0.058
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:38:32.783094+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a025_s43",
  "field": "log_path",
  "value": "~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a025_s43",
    "field": "log_path",
    "value": "~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T17:38:32.783242+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a025_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:38:10.647Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.09833, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.03351}, \"gen10\": {\"token_entropy\": 3.0723, \"ece\": 0.02146, \"perplexity\": 21.899, \"distinct_1\": 0.058
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T17:38:32.783462+00:00_

Registry 已更新。

---

## 1. Gen 0–10 完整指标表

| Gen | token_entropy | ECE | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve |
|-----|-------------|-------|-----------|-----------|-----------|-----------|---------|-------|
| 0 | 3.2342 | 0.0108 | 26.949 | 0.0983 | 0.5132 | 0.8057 | 46.61 | 0.0335 |
| 1 | 2.9953 | 0.0077 | 19.455 | 0.0996 | 0.5177 | 0.8097 | 49.63 | 0.0299 |
| 2 | 3.0369 | 0.0101 | 20.217 | 0.0807 | 0.4267 | 0.7109 | 49.98 | 0.0330 |
| 3 | 3.0516 | 0.0094 | 20.710 | 0.0725 | 0.3701 | 0.6219 | 50.41 | 0.0315 |
| 4 | 3.0337 | 0.0144 | 20.920 | 0.0664 | 0.3131 | 0.5166 | 50.44 | 0.0272 |
| 5 | 3.0467 | 0.0155 | 21.116 | 0.0640 | 0.2858 | 0.4653 | 49.59 | 0.0242 |
| 6 | 3.0428 | 0.0188 | 21.478 | 0.0621 | 0.2636 | 0.4179 | 49.67 | 0.0219 |
| 7 | 3.0554 | 0.0184 | 21.671 | 0.0611 | 0.2540 | 0.3976 | 47.47 | 0.0226 |
| 8 | 3.0878 | 0.0185 | 21.923 | 0.0597 | 0.2389 | 0.3647 | 47.07 | 0.0194 |
| 9 | 3.0691 | 0.0203 | 21.845 | 0.0593 | 0.2317 | 0.3476 | 45.61 | 0.0193 |
| 10 | 3.0723 | 0.0215 | 21.899 | 0.0585 | 0.2236 | 0.3330 | 45.37 | 0.0187 |

## 2. Seed=42 vs Seed=43 对比

| Metric | seed=42 drift | seed=43 drift | 比值 (43/42) |
|--------|-------------|-------------|------------|
| token_entropy | **-4.1%** | **-5.0%** | 1.22x |
| ECE | **+79.7%** | **+98.6%** | 1.24x |
| perplexity | **-17.2%** | **-18.7%** | 1.09x |
| distinct_1 | **-40.3%** | **-40.5%** | 1.00x |
| distinct_2 | **-57.1%** | **-56.4%** | 0.99x |
| distinct_3 | **-59.9%** | **-58.7%** | 0.98x |

## 3. Conclusion: **success**

所有 6 项指标 drift 方向完全一致（entropy↓、ECE↑、perplexity↓、diversity 三指标↓）。diversity 三指标幅度几乎完全复现（偏差 <2%）。entropy 和 ECE 的幅度 seed=43 略大（~22-24%），但均在 ±50% 判定阈值以内。perplexity drift 也高度吻合（偏差 9%）。

α=0.25 低污染设置下的温和 collapse 模式在 seed=43 上完全复现。无 lead-lag 分析结果（本次 run 未包含 Granger/TY 检验）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_alpha_sweep_a025_s43_20260515T173716"
}
```

</details>

---
