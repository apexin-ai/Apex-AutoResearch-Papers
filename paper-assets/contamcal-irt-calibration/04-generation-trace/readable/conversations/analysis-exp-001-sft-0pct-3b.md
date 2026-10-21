# analysis exp 001 sft 0pct 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_exp_001_sft_0pct_3B_20260513T232449.jsonl`
- **Structured JSON:** [`12c448069273583e335b.json`](../../sessions/12/12c448069273583e335b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-13T23:25:56.585307+00:00_

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
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
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

_source line 2 · 2026-05-13T23:25:56.587591+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T23:25:56.587850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -100 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T23:25:56.588069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -lh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -lh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T23:25:56.589404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.1303, 'grad_norm': 0.2764390707015991, 'learning_rate': 4.608171039984928e-05, 'entropy': 1.120458220038563, 'num_tokens': 13611325.0, 'mean_token_accuracy': 0.7498776899650693, 'epoch': 0.7}\\n{'loss': 1.1552, 'grad_norm': 0.2421015202999115, 'learning_rate': 4.519330080430687e-05, 'entropy': 1.1199896147474646, 'num_tokens': 13671165.0, 'mean_token_accuracy': 0.7453760346397758, 'epoch': 0.7}\\n{'loss': 1.2505, 'grad_norm': 0.24319444596767426, 'learning_rate': 4.43110316777793e-05, 'entropy': 1.1977826829999685, 'num_tokens': 13734267.0, 'mean_token_accuracy': 0.7376854928210378, 'epoch': 0.7}\\n{'loss': 1.1776, 'grad_norm': 0.21019788086414337, 'learning_rate': 4.343500186851533e-05, 'entropy': 1.1083951861597598, 'num_tokens': 13798330.0, 'mean_token_accuracy': 0.7447790406644345, 'epoch': 0.71}\\n{'loss': 1.0939, 'grad_norm': 0.23173126578330994, 'learning_rate': 4.256530952571889e-05, 'entropy': 1.117940972559154, 'num_tokens': 13857896.0, 'mean_token_accuracy': 0.7448570001870394, 'epoch': 0.71}\\n{'loss': 1.0945, 'grad_norm': 0.32466545701026917, 'learning_rate': 4.170205208855281e-05, 'entropy': 1.0382787698879838, 'num_tokens': 13921550.0, 'mean_token_accuracy': 0.7638347741216421, 'epoch': 0.71}\\n{'loss': 1.0432, 'grad_norm': 0.24764545261859894, 'learning_rate': 4.0845326275221595e-05, 'entropy': 1.1130314365029335, 'num_tokens': 13988306.0, 'mean_token_accuracy': 0.7443742077797652, 'epoch': 0.72}\\n{'loss': 1.0762, 'grad_norm': 0.23637720942497253, 'learning_rate': 3.9995228072135483e-05, 'entropy': 1.0974379411898554, 'num_tokens': 14047116.0, 'mean_token_accuracy': 0.754358972236514, 'epoch': 0.72}\\n{'loss': 1.0624, 'grad_norm': 0.47976866364479065, 'learning_rate': 3.9151852723156156e-05, 'entropy': 1.0965063862502575, 'num_tokens': 14110302.0, 'mean_token_accuracy': 0.74907311424613, 'epoch': 0.72}\\n{'loss': 1.1222, 'grad_norm': 0.44703197479248047, 'learning_rate': 3.8315294718
…[truncated 6281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T23:25:56.589780+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8.0K\\ndrwxr-xr-x 3 root root 4.0K May 14 07:20 lora_adapter\\n-rw-r--r-- 1 root root  306 May 14 07:20 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T23:25:56.589978+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "du -sh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "du -sh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T23:25:56.590185+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"488M\\t/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T23:25:56.590390+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -lh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -lh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T23:25:56.590585+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 130M\\n-rw-r--r-- 1 root root 1.5K May 14 07:20 README.md\\n-rw-r--r-- 1 root root 1.1K May 14 07:20 adapter_config.json\\n-rw-r--r-- 1 root root 115M May 14 07:20 adapter_model.safetensors\\n-rw-r--r-- 1 root root  605 May 14 07:20 added_tokens.json\\n-rw-r--r-- 1 root root 2.4K May 14 07:20 chat_template.jinja\\ndrwxr-xr-x 2 root root 4.0K May 14 07:20 checkpoint-3125\\n-rw-r--r-- 1 root root 1.6M May 14 07:20 merges.txt\\n-rw-r--r-- 1 root root  502 May 14 07:20 special_tokens_map.json\\n-rw-r--r-- 1 root root  11M May 14 07:20 tokenizer.json\\n-rw-r--r-- 1 root root 4.6K May 14 07:20 tokenizer_config.json\\n-rw-r--r-- 1 root root 6.3K May 14 07:20 training_args.bin\\n-rw-r--r-- 1 root root 2.7M May 14 07:20 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T23:25:56.590767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "du -sh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "du -sh /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T23:25:56.590938+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"488M\\t/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T23:25:56.591123+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -c \"^{\" ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -c \"^{\" ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T23:25:56.591292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"306\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T23:25:56.593684+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_0pct_3B",
  "field": "metrics",
  "value": "{'steps': '3125/3125', 'final_loss': 1.0736, 'mean_train_loss': 1.1306, 'token_accuracy': 0.734, 'training_time_min': 214.7, 'checkpoint_size_mb': 488, 'adapter_size_mb': 115, 'exit_code': 0}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_0pct_3B",
    "field": "metrics",
    "value": "{'steps': '3125/3125', 'final_loss': 1.0736, 'mean_train_loss': 1.1306, 'token_accuracy': 0.734, 'training_time_min': 214.7, 'checkpoint_size_mb': 488, 'adapter_size_mb': 115, 'exit_code': 0}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T23:25:56.593966+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_0pct_3B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:44.815Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2967}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T23:25:56.594167+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_0pct_3B",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_0pct_3B",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T23:25:56.594415+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_0pct_3B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:46.281Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2385}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T23:25:56.594621+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_0pct_3B",
  "field": "log_path",
  "value": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_0pct_3B",
    "field": "log_path",
    "value": "~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T23:25:56.594834+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_0pct_3B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:47.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2221}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T23:25:56.595019+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_0pct_3B",
  "field": "conclusion",
  "value": "success",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_0pct_3B",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T23:25:56.595226+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_0pct_3B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:48.129Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2069}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T23:25:56.596869+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_0pct_3B",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_0pct_3B",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T23:25:56.597138+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_0pct_3B\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:44:40.471Z\", \"updated_at\": \"2026-05-13T23:25:49.016Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"210666\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13268.6, \"gpu_hours\": 3.69}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"metrics\": {\"steps\": \"3125/3125\", \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"token_accuracy\": 0.734, \"training_time_min\": 214.7, \"checkpoint_size_mb\": 488, \"adapter_size_mb\": 115, \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:25:49.016Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3174}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T23:25:56.597433+00:00_

Registry 已全部更新完成，status=DONE, conclusion=success。

三个模型 clean baseline 对比：

| 模型 | Final Loss | Mean Loss | Token Acc | 训练时间 |
|------|-----------|-----------|-----------|---------|
| 0.5B | 1.4894 | 1.5388 | 0.682 | 52.9 min |
| 1.5B | 1.2039 | 1.2599 | 0.711 | 101.5 min |
| **3B** | **1.0736** | **1.1306** | **0.734** | **214.7 min** |

符合预期：模型越大，loss 越低、accuracy 越高，训练时间大致线性增长。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_001_sft_0pct_3B_20260513T232449"
}
```

</details>

---
