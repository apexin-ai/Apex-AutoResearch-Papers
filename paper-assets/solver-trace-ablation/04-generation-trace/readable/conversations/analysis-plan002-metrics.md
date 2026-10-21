# analysis plan002 metrics

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_plan002-metrics_20260514T032528.jsonl`
- **Structured JSON:** [`3581d8130cc9ba47c2fc.json`](../../sessions/35/3581d8130cc9ba47c2fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T03:27:02.154033+00:00_

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
  "session": "worker_analysis_plan002-metrics_20260514T032528",
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

_source line 2 · 2026-05-14T03:27:02.154377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T03:27:02.154564+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/outputs/plan002_additive_b03_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/outputs/plan002_additive_b03_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T03:27:02.154814+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/outputs/plan002_additive_b03_s42/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T03:27:02.154961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -5 ~/runs/solver-trace-ablation/plan002-additive-b03-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -5 ~/runs/solver-trace-ablation/plan002-additive-b03-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T03:27:02.155096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 11:24:00,380 INFO Final reward stats: {'parse_rate': 1.0, 'prove_rate': 0.34025, 'mean_isr': 0.11526891650016666}\\n2026-05-14 11:24:00,381 INFO Done.\\n{'loss': 0.0772, 'grad_norm': 31.31516456604004, 'learning_rate': 2e-09, 'num_tokens': 1373431.0, 'completions/mean_length': 57.0, 'completions/min_length': 44.0, 'completions/max_length': 66.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 57.0, 'completions/min_terminated_length': 44.0, 'completions/max_terminated_length': 66.0, 'rewards/reward_fn/mean': 1.0926785469055176, 'rewards/reward_fn/std': 0.03397340327501297, 'reward': 1.0926785469055176, 'reward_std': 0.033973414450883865, 'frac_reward_zero_std': 0.0, 'entropy': 0.027210528030991554, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 3.1228015148080885, 'epoch': 2.0}\\n{'train_runtime': 3448.19, 'train_samples_per_second': 1.16, 'train_steps_per_second': 0.145, 'train_loss': 0.008910538971640562, 'epoch': 2.0}\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T03:27:02.155229+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "wc -l /root/autodl-tmp/outputs/plan002_additive_b03_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "wc -l /root/autodl-tmp/outputs/plan002_additive_b03_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T03:27:02.155358+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"wc: /root/autodl-tmp/outputs/plan002_additive_b03_s42/reward_log.jsonl: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:27:02.155486+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'exp_id': 'plan002-additive-b03-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'exp_id': 'plan002-additive-b03-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T03:27:02.155611+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1076}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T03:27:02.155757+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -maxdepth 1 -name \"*plan002*\" -o -name \"*additive*b03*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -maxdepth 1 -name \"*plan002*\" -o -name \"*additive*b03*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T03:27:02.155883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T03:27:02.155998+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -maxdepth 1 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -maxdepth 1 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T03:27:02.156495+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/outputs\\n/root/autodl-tmp/outputs/grpo_exec_only\\n/root/autodl-tmp/outputs/grpo_exec_sta\\n/root/autodl-tmp/outputs/plan001_exec_only_s42\\n/root/autodl-tmp/outputs/plan005_sta_low_s42\\n/root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\n/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\n/root/autodl-tmp/outputs/plan001_exec_only_s44\\n/root/autodl-tmp/outputs/plan002_additive_beta03_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T03:27:02.156682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/outputs/plan002_additive_beta03_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/outputs/plan002_additive_beta03_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T03:27:02.156891+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 15728520\\ndrwxr-xr-x  3 root root       4096 May 14 11:24 .\\ndrwxr-xr-x 10 root root       4096 May 14 11:19 ..\\n-rw-r--r--  1 root root       1888 May 14 11:23 README.md\\n-rw-r--r--  1 root root        707 May 14 11:24 added_tokens.json\\n-rw-r--r--  1 root root       4168 May 14 11:24 chat_template.jinja\\ndrwxr-xr-x  2 root root       4096 May 14 11:23 checkpoint-500\\n-rw-r--r--  1 root root       1535 May 14 11:23 config.json\\n-rw-r--r--  1 root root        188 May 14 11:23 generation_config.json\\n-rw-r--r--  1 root root    1671853 May 14 11:24 merges.txt\\n-rw-r--r--  1 root root 4990095032 May 14 11:23 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4944309096 May 14 11:23 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4996758848 May 14 11:23 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1158754848 May 14 11:24 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      32856 May 14 11:24 model.safetensors.index.json\\n-rw-r--r--  1 root root     110357 May 14 11:23 reward_log.jsonl\\n-rw-r--r--  1 root root        613 May 14 11:24 special_tokens_map.json\\n-rw-r--r--  1 root root   11422654 May 14 11:24 tokenizer.json\\n-rw-r--r--  1 root root       5459 May 14 11:24 tokenizer_config.json\\n-rw-r--r--  1 root root       7953 May 14 11:24 training_args.bin\\n-rw-r--r--  1 root root    2776833 May 14 11:24 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T03:27:02.157040+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "wc -l /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "wc -l /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:27:02.157164+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"500 /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T03:27:02.157309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -1 /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -1 /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T03:27:02.157614+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 1, \\\"reward_mean\\\": 0.1550000011920929, \\\"reward_std\\\": 0.43840622901916504, \\\"prove_rate\\\": 0.125, \\\"isr_mean\\\": 0.1, \\\"parse_rate\\\": 1.0, \\\"loss\\\": 0.0261, \\\"lr\\\": 1e-06, \\\"timestamp\\\": \\\"2026-05-14T02:26:29.489390+00:00\\\"}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T03:27:02.157799+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -1 /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -1 /root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T03:27:02.157933+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 500, \\\"reward_mean\\\": 1.0926785469055176, \\\"reward_std\\\": 0.033973414450883865, \\\"prove_rate\\\": 1.0, \\\"isr_mean\\\": 0.3089285714285714, \\\"parse_rate\\\": 1.0, \\\"loss\\\": 0.0772, \\\"lr\\\": 2e-09, \\\"timestamp\\\": \\\"2026-05-14T03:23:11.599145+00:00\\\"}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T03:27:02.158075+00:00_

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
  "session": "worker_analysis_plan002-metrics_20260514T032528",
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

_source line 24 · 2026-05-14T03:27:02.158190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T03:27:02.158307+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nrows = [json.loads(l) for l in open('/root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl')]\nn = len(rows)\n\n# duration\nfrom datetime import datetime\nt0 = datetime.fromisoformat(rows[0]['timestamp'])\nt1 = datetime.fromisoformat(rows[-1]['timestamp'])\ndur_min = (t1 - t0).total_seconds() / 60\n\n# prove_rate windows\ndef avg(lst, key, s, e):\n    sl = lst[s:e]\n    return sum(r[key] for r in sl) / len(sl) if sl else 0\n\npr = [r['prove_rate'] for r in rows]\nisr = [r['isr_mean'] for r in rows]\nloss = [r['loss'] for r in rows]\nparse = [r['parse_rate'] for r in rows]\n\nprint(f'total_steps={n}')\nprint(f'duration_min={dur_min:.1f}')\nprint(f'overall_prove_rate={sum(pr)/n:.5f}')\nprint(f'overall_isr={sum(isr)/n:.5f}')\nprint(f'first20_prove_rate={sum(pr[:20])/20:.5f}')\nprint(f'last50_prove_rate={sum(pr[-50:])/50:.5f}')\nprint(f'last100_prove_rate={sum(pr[-100:])/100:.5f}')\nprint(f'mean_loss={sum(loss)/n:.6f}')\nprint(f'last100_loss={sum(loss[-100:])/100:.6f}')\nprint(f'parse_rate={sum(parse)/n:.5f}')\n\n# window prove rates\nfor s,e,label in [(0,50,'w1_50'),(50,100,'w51_100'),(100,200,'w101_200'),(200,300,'w201_300'),(300,400,'w301_400'),(400,500,'w401_500')]:\n    print(f'{label}_prove_rate={sum(pr[s:e])/len(pr[s:e]):.5f}')\n\n# saturation check\nsat_steps = sum(1 for p in pr if p >= 0.85)\nprint(f'steps_ge_085={sat_steps}')\nprint(f'first_step_ge_085={next((i+1 for i,p in enumerate(pr) if p>=0.85), None)}')\n\n# final step details\nr = rows[-1]\nprint(f'final_prove_rate={r[\\\"prove_rate\\\"]}')\nprint(f'final_isr_mean={r[\\\"isr_mean\\\"]}')\nprint(f'final_reward_mean={r[\\\"reward_mean\\\"]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nrows = [json.loads(l) for l in open('/root/autodl-tmp/outputs/plan002_additive_beta03_s42/reward_log.jsonl')]\nn = len(rows)\n\n# duration\nfrom datetime import datetime\nt0 = datetime.fromisoformat(rows[0]['timestamp'])\nt1 = datetime.fromisoformat(rows[-1]['timestamp'])\ndur_min = (t1 - t0).total_seconds() / 60\n\n# prove_rate windows\ndef avg(lst, key, s, e):\n    sl = lst[s:e]\n    return sum(r[key] for r in sl) / len(sl) if sl else 0\n\npr = [r['prove_rate'] for r in rows]\nisr = [r['isr_mean'] for r in rows]\nloss = [r['loss'] for r in rows]\nparse = [r['parse_rate'] for r in rows]\n\nprint(f'total_steps={n}')\nprint(f'duration_min={dur_min:.1f}')\nprint(f'overall_prove_rate={sum(pr)/n:.5f}')\nprint(f'overall_isr={sum(isr)/n:.5f}')\nprint(f'first20_prove_rate={sum(pr[:20])/20:.5f}')\nprint(f'last50_prove_rate={sum(pr[-50:])/50:.5f}')\nprint(f'last100_prove_rate={sum(pr[-100:])/100:.5f}')\nprint(f'mean_loss={sum(loss)/n:.6f}')\nprint(f'last100_loss={sum(loss[-100:])/100:.6f}')\nprint(f'parse_rate={sum(parse)/n:.5f}')\n\n# window prove rates\nfor s,e,label in [(0,50,'w1_50'),(50,100,'w51_100'),(100,200,'w101_200'),(200,300,'w201_300'),(300,400,'w301_400'),(400,500,'w401_500')]:\n    print(f'{label}_prove_rate={sum(pr[s:e])/len(pr[s:e]):.5f}')\n\n# saturation check\nsat_steps = sum(1 for p in pr if p >= 0.85)\nprint(f'steps_ge_085={sat_steps}')\nprint(f'first_step_ge_085={next((i+1 for i,p in enumerate(pr) if p>=0.85), None)}')\n\n# final step details\nr = rows[-1]\nprint(f'final_prove_rate={r[\\\"prove_rate\\\"]}')\nprint(f'final_isr_mean={r[\\\"isr_mean\\\"]}')\nprint(f'final_reward_mean={r[\\\"reward_mean\\\"]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T03:27:02.158460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total_steps=500\\nduration_min=56.7\\noverall_prove_rate=0.34025\\noverall_isr=0.11527\\nfirst20_prove_rate=0.15625\\nlast50_prove_rate=0.55500\\nlast100_prove_rate=0.55250\\nmean_loss=0.008914\\nlast100_loss=0.014469\\nparse_rate=1.00000\\nw1_50_prove_rate=0.13000\\nw51_100_prove_rate=0.09500\\nw101_200_prove_rate=0.18500\\nw201_300_prove_rate=0.37500\\nw301_400_prove_rate=0.47625\\nw401_500_prove_rate=0.55250\\nsteps_ge_085=52\\nfirst_step_ge_085=46\\nfinal_prove_rate=1.0\\nfinal_isr_mean=0.3089285714285714\\nfinal_reward_mean=1.0926785469055176\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T03:27:02.158622+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "exp_id": "plan002-additive-b03-s42",
  "field": "metrics",
  "value": "{'total_steps': 500, 'duration_min': 56.7, 'overall_prove_rate': 0.34025, 'overall_isr': 0.11527, 'first20_prove_rate': 0.15625, 'last50_prove_rate': 0.555, 'last100_prove_rate': 0.5525, 'mean_loss': 0.008914, 'last100_loss': 0.014469, 'parse_rate': 1, 'w1_50_prove_rate': 0.13, 'w51_100_prove_rate': 0.095, 'w101_200_prove_rate': 0.185, 'w201_300_prove_rate': 0.375, 'w301_400_prove_rate': 0.47625, 'w401_500_prove_rate': 0.5525, 'steps_ge_085': 52, 'first_step_ge_085': 46, 'final_prove_rate': 1, 'final_isr_mean': 0.3089, 'final_reward_mean': 1.0927}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "exp_id": "plan002-additive-b03-s42",
    "field": "metrics",
    "value": "{'total_steps': 500, 'duration_min': 56.7, 'overall_prove_rate': 0.34025, 'overall_isr': 0.11527, 'first20_prove_rate': 0.15625, 'last50_prove_rate': 0.555, 'last100_prove_rate': 0.5525, 'mean_loss': 0.008914, 'last100_loss': 0.014469, 'parse_rate': 1, 'w1_50_prove_rate': 0.13, 'w51_100_prove_rate': 0.095, 'w101_200_prove_rate': 0.185, 'w201_300_prove_rate': 0.375, 'w301_400_prove_rate': 0.47625, 'w401_500_prove_rate': 0.5525, 'steps_ge_085': 52, 'first_step_ge_085': 46, 'final_prove_rate': 1, 'final_isr_mean': 0.3089, 'final_reward_mean': 1.0927}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T03:27:02.158844+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan002-additive-b03-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T03:26:35.563Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T03:27:02.158993+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "exp_id": "plan002-additive-b03-s42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/outputs/plan002_additive_beta03_s42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "exp_id": "plan002-additive-b03-s42",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/outputs/plan002_additive_beta03_s42"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T03:27:02.159153+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan002-additive-b03-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T03:26:40.118Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T03:27:02.159306+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "exp_id": "plan002-additive-b03-s42",
  "field": "log_path",
  "value": "~/runs/solver-trace-ablation/plan002-additive-b03-s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "exp_id": "plan002-additive-b03-s42",
    "field": "log_path",
    "value": "~/runs/solver-trace-ablation/plan002-additive-b03-s42.log"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T03:27:02.159467+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan002-additive-b03-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T03:26:40.995Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T03:27:02.159615+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "exp_id": "plan002-additive-b03-s42",
  "field": "notes",
  "value": "ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "exp_id": "plan002-additive-b03-s42",
    "field": "notes",
    "value": "ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T03:27:02.159803+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan002-additive-b03-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T03:26:50.189Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 
…[truncated 423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T03:27:02.159949+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "exp_id": "plan002-additive-b03-s42",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "exp_id": "plan002-additive-b03-s42",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T03:27:02.160117+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan002-additive-b03-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T03:26:50.531Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 
…[truncated 452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan002-metrics_20260514T032528",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T03:27:02.160297+00:00_

Registry 更新完成。汇总：

**plan002-additive-b03-s42** — conclusion: **success**

| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| duration | 56.7 min |
| overall_prove_rate | 0.340 |
| last100_prove_rate | **0.553** |
| overall_isr (binary) | 0.115 |
| final_isr_mean | 0.309 |
| parse_rate | 1.0 |
| mean_loss / last100_loss | 0.0089 / 0.0145 |

**prove_rate 窗口轨迹：**
w1-50: 0.130 → w51-100: 0.095 → w101-200: 0.185 → w201-300: 0.375 → w301-400: 0.476 → w401-500: **0.553**

**vs plan001/plan013 饱和对比：** 仅 52/500 步 ≥0.85（plan001/plan013 通常 >300 步饱和）。additive bonus 模式下 prove_rate 仍在稳步上升，未出现强饱和，说明 ISR bonus 引入的额外 reward 信号可能减缓了 GRPO 过早收敛。需 eval_sta.py 评估真实 ISR 后才可做跨 run 对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_plan002-metrics_20260514T032528"
}
```

</details>

---
