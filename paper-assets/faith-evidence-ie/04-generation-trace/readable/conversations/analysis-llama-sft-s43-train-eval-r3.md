# analysis llama sft s43 train eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644.jsonl`
- **Structured JSON:** [`7828616befab4a545496.json`](../../sessions/78/7828616befab4a545496.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T14:07:46.676020+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T14:07:46.676441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T14:07:46.676626+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T14:07:46.676870+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_output_llama_3_1_8b_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_output_llama_3_1_8b_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T14:07:46.677138+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 88%|████████▊ | 869/985 [01:03<00:07, 15.26it/s]\\u001b[A\\n\\r 88%|████████▊ | 871/985 [01:03<00:07, 14.57it/s]\\u001b[A\\n\\r 89%|████████▊ | 873/985 [01:03<00:07, 14.57it/s]\\u001b[A\\n\\r 89%|████████▉ | 875/985 [01:04<00:07, 13.81it/s]\\u001b[A\\n\\r 89%|████████▉ | 877/985 [01:04<00:07, 13.76it/s]\\u001b[A\\n\\r 89%|████████▉ | 879/985 [01:04<00:08, 13.21it/s]\\u001b[A\\n\\r 89%|████████▉ | 881/985 [01:04<00:08, 12.51it/s]\\u001b[A\\n\\r 90%|████████▉ | 883/985 [01:04<00:07, 13.05it/s]\\u001b[A\\n\\r 90%|████████▉ | 885/985 [01:04<00:07, 13.44it/s]\\u001b[A\\n\\r 90%|█████████ | 887/985 [01:05<00:07, 13.26it/s]\\u001b[A\\n\\r 90%|█████████ | 889/985 [01:05<00:07, 13.47it/s]\\u001b[A\\n\\r 90%|█████████ | 891/985 [01:05<00:06, 13.84it/s]\\u001b[A\\n\\r 91%|█████████ | 893/985 [01:05<00:06, 13.30it/s]\\u001b[A\\n\\r 91%|█████████ | 895/985 [01:05<00:06, 14.51it/s]\\u001b[A\\n\\r 91%|█████████ | 897/985 [01:05<00:06, 14.49it/s]\\u001b[A\\n\\r 91%|█████████▏| 899/985 [01:05<00:06, 13.25it/s]\\u001b[A\\n\\r 91%|█████████▏| 901/985 [01:06<00:06, 13.62it/s]\\u001b[A\\n\\r 92%|█████████▏| 903/985 [01:06<00:06, 13.61it/s]\\u001b[A\\n\\r 92%|█████████▏| 905/985 [01:06<00:07, 11.36it/s]\\u001b[A\\n\\r 92%|█████████▏| 907/985 [01:06<00:06, 11.55it/s]\\u001b[A\\n\\r 92%|█████████▏| 909/985 [01:06<00:07, 10.37it/s]\\u001b[A\\n\\r 92%|█████████▏| 911/985 [01:06<00:06, 11.57it/s]\\u001b[A\\n\\r 93%|█████████▎| 913/985 [01:07<00:06, 11.24it/s]\\u001b[A\\n\\r 93%|█████████▎| 915/985 [01:07<00:05, 12.22it/s]\\u001b[A\\n\\r 93%|█████████▎| 917/985 [01:07<00:05, 12.53it/s]\\u001b[A\\n\\r 93%|█████████▎| 919/985 [01:07<00:04, 13.90it/s]\\u001b[A\\n\\r 94%|█████████▎| 921/985 [01:07<00:04, 14.56it/s]\\u001b[A\\n\\r 94%|████████��▎| 923/985 [01:07<00:04, 12.82it/s]\\u001b[A\\n\\r 94%|█████████▍| 925/985 [01:07<00:04, 13.06it/s]\\u001b[A\\n\\r 94%|█████████▍| 927/985 [01:08<00:04, 14.18it/s]\\u001b[A\\n\\r 94%|█████████▍| 929
…[truncated 6984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T14:07:46.677361+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 672276\\ndrwx------  4 root root      4096 May 20 20:06 .\\ndrwxr-xr-x 80 root root      8192 May 20 12:32 ..\\n-rw-r--r--  1 root root      1522 May 20 20:06 README.md\\n-rw-r--r--  1 root root      1132 May 20 20:06 adapter_config.json\\n-rw-r--r--  1 root root 671149168 May 20 20:06 adapter_model.safetensors\\n-rw-r--r--  1 root root       384 May 20 20:06 chat_template.jinja\\ndrwxr-xr-x  2 root root      4096 May 20 19:38 checkpoint-190\\ndrwxr-xr-x  2 root root      4096 May 20 20:06 checkpoint-570\\n-rw-r--r--  1 root root  17209920 May 20 20:06 tokenizer.json\\n-rw-r--r--  1 root root       389 May 20 20:06 tokenizer_config.json\\n-rw-r--r--  1 root root      5777 May 20 20:06 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T14:07:46.677560+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_llama_s43_eval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_llama_s43_eval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:07:46.677749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5168863583183839,\\n  \\\"recall\\\": 0.5453872109291417,\\n  \\\"f1\\\": 0.5307544449783758,\\n  \\\"ign_precision\\\": 0.49165261382799325,\\n  \\\"ign_recall\\\": 0.5388596248036226,\\n  \\\"ign_f1\\\": 0.5141748600149906,\\n  \\\"tp\\\": 6627,\\n  \\\"pred_count\\\": 12821,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8761566501542201,\\n  \\\"evi_recall\\\": 0.7786360993437993,\\n  \\\"evi_f1\\\": 0.8245228252264931,\\n  \\\"n_evaluated\\\": 15504,\\n  \\\"edcr\\\": 0.5865566973933753,\\n  \\\"n_distractor_citations\\\": 13299,\\n  \\\"n_total_citations\\\": 22673,\\n  \\\"evi_joint_precision\\\": 0.42544993930437536,\\n  \\\"evi_joint_recall\\\": 0.4185140958413374,\\n  \\\"evi_f1_joint\\\": 0.42195351758793975,\\n  \\\"evi_tp\\\": 8061,\\n  \\\"evi_pred_total\\\": 18947,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8071065989847716,\\n  \\\"evidence_format_rate\\\": 0.8060913705583757,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 795,\\n  \\\"n_evidence_valid\\\": 794,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15548,\\n  \\\"n_truncated\\\": 190,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 6971.8,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_llama_s43_eval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T14:07:46.677920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"wandb\\|run_id\\|run_name\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"wandb\\|run_id\\|run_name\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:07:46.678055+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T14:07:46.678185+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep \"train_loss\\|training_loss\\|'loss'\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep \"train_loss\\|training_loss\\|'loss'\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T14:07:46.678352+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T14:07:46.678508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"wandb\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"wandb\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T14:07:46.678642+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T14:07:46.678763+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep \"train_loss\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep \"train_loss\" /root/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T14:07:46.678887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'train_runtime': '2577', 'train_samples_per_second': '3.524', 'train_steps_per_second': '0.221', 'train_loss': '0.521', 'epoch': '3'}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T14:07:46.679051+00:00_

没有 wandb 记录。所有数据已收集完毕。

## 结果

- **conclusion**: success
- **ign_f1**: 0.5142
- **evi_f1**: 0.4220 (joint) / 0.8245 (TP)
- **edcr**: 0.5866
- **re_p** (ign_precision): 0.4917
- **re_r** (ign_recall): 0.5389
- **train_loss_final**: 0.521
- **checkpoint_path**: `/root/autodl-tmp/sft_output_llama_3_1_8b_s43/` (adapter_model.safetensors 640MB, checkpoint-190, checkpoint-570)
- **log_path**: `~/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log`
- **wandb_run_id**: 无（未启用 wandb）

## 对比

| Seed | ign_f1 | evi_f1 (joint) | edcr |
|------|--------|----------------|------|
| s42 (SFT) | 0.5384 | — | — |
| **s43 (SFT)** | **0.5142** | **0.4220** | **0.5866** |
| RSFT 3-seed mean | 0.5654 ± 0.0052 | — | — |

s43 ign_f1 = 0.5142，比 s42 (0.5384) 低 **0.0242**（-4.5%）。两个 SFT seed 目前 mean = 0.5263，与 RSFT mean 0.5654 差距 0.0391。

SFT 两个 seed 之间的差异 (0.0242) 已经明显大于 RSFT 3-seed 的 std (0.0052)，初步支持 "SFT variance > RSFT variance" 的 claim。还需要 s44 完成 3-seed 统计才能做正式对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644"
}
```

</details>

---
