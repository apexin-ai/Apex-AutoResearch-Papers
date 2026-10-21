# eval test eval 14b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_eval_test_eval_14b_rsft_s42_20260521T183005.jsonl`
- **Structured JSON:** [`ddf496ce88277bebbcd7.json`](../../sessions/dd/ddf496ce88277bebbcd7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-21T18:31:00.534112+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:31:00.534525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:31:00.534704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/rsft_output_14b/adapter_config.json /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_config.json /root/autodl-tmp/models/Qwen/Qwen3-14B/config.json /root/autodl-tmp/data/re-docred-repo/data/test_revised.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/rsft_output_14b/adapter_config.json /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_config.json /root/autodl-tmp/models/Qwen/Qwen3-14B/config.json /root/autodl-tmp/data/re-docred-repo/data/test_revised.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T18:31:00.534880+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 3207228 May 16 14:35 /root/autodl-tmp/data/re-docred-repo/data/test_revised.json\\n-rw-r--r-- 1 root root     728 May 18 19:21 /root/autodl-tmp/models/Qwen/Qwen3-14B/config.json\\n-rw-r--r-- 1 root root    1118 May 21 04:23 /root/autodl-tmp/rsft_output_14b/adapter_config.json\\n-rw-r--r-- 1 root root    1118 May 19 15:17 /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:31:00.535029+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T18:31:00.535160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB\\n1, 0 MiB, 97887 MiB\\n2, 0 MiB, 97887 MiB\\n3, 11767 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:31:00.535336+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T18:31:00.535470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:31:00.535588+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit training job",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit training job",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T18:31:00.535705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T18:31:00.535816+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit training",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit training",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:31:00.535927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T18:31:00.536065+00:00_

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
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
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

_source line 14 · 2026-05-21T18:31:00.536193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T18:31:00.536353+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_14b_rsft_s42",
  "field": "hypothesis",
  "value": "Re-DocRED test set eval: Qwen3-14B RSFT s42 (CED k1, nested LoRA) on test_revised.json (500 docs)。dev ign_f1=0.5886 (项目最高)。验证 dev 性能是否泛化到 test set，建立 test set scaling 最高基线。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_14b_rsft_s42",
    "field": "hypothesis",
    "value": "Re-DocRED test set eval: Qwen3-14B RSFT s42 (CED k1, nested LoRA) on test_revised.json (500 docs)。dev ign_f1=0.5886 (项目最高)。验证 dev 性能是否泛化到 test set，建立 test set scaling 最高基线。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T18:31:00.536532+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_14b_rsft_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:07:51.916Z\", \"updated_at\": \"2026-05-21T18:30:47.660Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.test_inference ... --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"97434\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_14b_rsft_s42.log\", \"submitted_at\": \"2026-05-21T10:07:51.113Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-14B + SFT + RSFT (nested LoRA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"re-docred test_revised\", \"wall_clock_seconds\": 20731.5, \"gpu_hours\": 5.76}, \"reproduce\": {\"finished_at\": \"2026-05-21T15:28:02.945Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T15:28:09.943953+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.3849, \"ign_f1\": 0.3849, \"evi_f1\": 0.2688, \"evi_f1_tp\": 0.6025, \"edcr\": 0.7865, \"truncated\": \"67/500\", \"format_ok\": \"499/500\", \"n_docs\": 500, \"inference_time_s\": 19080, \"codalab_generated\": true}, \"log_path\": \"~/runs/faith-evidence-ie/test_eval_14b_rsft_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_eval_14b_rsft_s42\", \"hypothesis\": \"Re-DocRED test set eval: Qwen3-14B RSFT s42 (CED k1, nested LoRA) on test_revised.json (500 docs)。dev ign_f1=0.5886 (项目最高)。验证 dev 性能是否泛化到 test set，建立 test set scaling 最高基线。\", \"completed_at\": \"2026-05-21T15:53:22.637Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6509}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T18:31:00.536728+00:00_

该实验已经完成过了。Registry 显示 `test_eval_14b_rsft_s42` 状态为 **DONE (success)**，结果如下：

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.3849 |
| f1 | 0.3849 |
| evi_f1 | 0.2688 |
| evi_f1_tp | 0.6025 |
| edcr | 0.7865 |
| format_ok | 499/500 |
| truncated | 67/500 |
| inference_time | ~5.3h |

之前在 cuda:1 上跑的，已于 2026-05-21T15:28 完成，wall clock 约 5.76 GPU-hours。CodaLab 提交文件也已生成。

不需要重新提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_test_eval_14b_rsft_s42_20260521T183005"
}
```

</details>

---
