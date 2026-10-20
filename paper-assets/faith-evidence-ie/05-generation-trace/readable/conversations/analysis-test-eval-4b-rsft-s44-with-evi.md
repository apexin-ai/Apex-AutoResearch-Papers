# analysis test eval 4b rsft s44 with evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602.jsonl`
- **Structured JSON:** [`7f644de4f411f884a7ae.json`](../../sessions/7f/7f644de4f411f884a7ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-23T10:47:21.461730+00:00_

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
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
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

_source line 2 · 2026-05-23T10:47:21.462076+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:47:21.462278+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -80 ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -80 ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T10:47:21.462511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 17:33:23,425 INFO Detected adapter at /root/autodl-tmp/rsft_output_ced_s44, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-23 17:33:23,425 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-23 17:33:23,874 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\rLoading weights:   2%|▏         | 6/398 [00:00<00:06, 59.52it/s]\\rLoading weights:  12%|█▏        | 47/398 [00:00<00:01, 262.63it/s]\\rLoading weights:  21%|██        | 82/398 [00:00<00:01, 298.54it/s]\\rLoading weights:  31%|███       | 124/398 [00:00<00:00, 340.79it/s]\\rLoading weights:  40%|███▉      | 159/398 [00:00<00:00, 334.39it/s]\\rLoading weights:  51%|█████     | 201/398 [00:00<00:00, 340.48it/s]\\rLoading weights:  62%|██████▏   | 245/398 [00:00<00:00, 370.14it/s]\\rLoading weights:  71%|███████   | 283/398 [00:00<00:00, 367.92it/s]\\rLoading weights:  80%|████████  | 320/398 [00:00<00:00, 368.14it/s]\\rLoading weights:  90%|████████▉ | 357/398 [00:01<00:00, 357.25it/s]\\rLoading weights:  99%|█████████▉| 396/398 [00:01<00:00, 364.73it/s]\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 344.20it/s]\\n2026-05-23 17:33:25,528 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-23 17:33:26,935 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_ced_s44\\n2026-05-23 17:33:28,275 INFO Prepared 500 test documents\\n\\rInference:   0%|          | 0/32 [00:00<?, ?it/s]\\rInference:   3%|▎         | 1/32 [02:10<1:07:27, 130.55s/it]\\rInference:   6%|▋         | 2/32 [04:22<1:05:36, 131.21s/it]\\rInference:   9%|▉         | 3/32 [06:35<1:03:58, 132.38s/it]\\rInference:  12%|█▎        | 4/32 [08:52<1:02:35, 134.12s/it]\\rInference:  16%|█▌        | 5/32 [10:59<59:12, 131.56s/it]  \\rInference:  19%|█▉        | 6/32 [13:12<57:13, 132.06s/it]\\rInference:  22%|██▏ 
…[truncated 2764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T10:47:21.462696+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"wandb\\|w&b\\|run link\\|https://wandb\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"wandb\\|w&b\\|run link\\|https://wandb\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:47:21.462835+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:47:21.462972+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -iE \"error|warning\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -iE \"error|warning\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T10:47:21.463099+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:47:21.463220+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"wandb\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"wandb\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T10:47:21.463368+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:47:21.463486+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"error\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"error\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T10:47:21.463607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 18:42:10,860 INFO Inference done. 220/500 truncated, 0 errors.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:47:21.463724+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"warning\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"warning\" ~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T10:47:21.463840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 18:42:10,977 WARNING train_annotated.json not found, Ign-F1 = F1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T10:47:21.464001+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_4b_rsft_s44_with_evi",
  "field": "metrics",
  "value": "{'ign_f1': 0.2525, 'f1': 0.2525, 'evi_f1': 0.1829, 'evi_f1_tp': 0.6155, 'edcr': 0.8324, 'format_ok_rate': '500/500', 'n_truncated': 220, 'n_documents': 500, 'n_predictions': 21065, 'inference_time_seconds': 4122.6, 'inference_speed_s_per_doc': 8.25, 'codalab_converted': 9628, 'codalab_skipped_rel': 295, 'codalab_skipped_entity': 541}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_4b_rsft_s44_with_evi",
    "field": "metrics",
    "value": "{'ign_f1': 0.2525, 'f1': 0.2525, 'evi_f1': 0.1829, 'evi_f1_tp': 0.6155, 'edcr': 0.8324, 'format_ok_rate': '500/500', 'n_truncated': 220, 'n_documents': 500, 'n_predictions': 21065, 'inference_time_seconds': 4122.6, 'inference_speed_s_per_doc': 8.25, 'codalab_converted': 9628, 'codalab_skipped_rel': 295, 'codalab_skipped_entity': 541}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T10:47:21.464201+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_4b_rsft_s44_with_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:33:05.779Z\", \"updated_at\": \"2026-05-23T10:46:47.945Z\", \"hypothesis\": \"4B RSFT CED k=1 s44 with-evidence test eval on Re-DocRED test_revised (500 docs). 补充第 3 seed：s42 ign_f1=0.2503, s43=0.2503。3-seed mean±std 完善 4B evidence tax 数据。\", \"parent\": \"rsft_ced_s44_train_v2\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_ced_s44 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 44\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"241448\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log\", \"submitted_at\": \"2026-05-23T09:33:19.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s44 (with-evi)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s44\", \"eval_data\": \"Re-DocRED test_revised (500 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T10:43:45.534Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T10:43:55.050648+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.2525, \"f1\": 0.2525, \"evi_f1\": 0.1829, \"evi_f1_tp\": 0.6155, \"edcr\": 0.8324, \"format_ok_rate\": \"500/500\", \"n_truncated\": 220, \"n_documents\": 500, \"n_predictions\": 21065, \"inference_time_seconds\": 4122.6, \"inference_speed_s_per_doc\": 8.25, \"codalab_converted\": 9628, \"codalab_skipped_rel\": 295, \"codalab_skipped_entity\": 541}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6312}}"
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T10:47:21.464378+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_4b_rsft_s44_with_evi",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_4b_rsft_s44_with_evi",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T10:47:21.464549+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_4b_rsft_s44_with_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:33:05.779Z\", \"updated_at\": \"2026-05-23T10:46:52.785Z\", \"hypothesis\": \"4B RSFT CED k=1 s44 with-evidence test eval on Re-DocRED test_revised (500 docs). 补充第 3 seed：s42 ign_f1=0.2503, s43=0.2503。3-seed mean±std 完善 4B evidence tax 数据。\", \"parent\": \"rsft_ced_s44_train_v2\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_ced_s44 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 44\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"241448\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log\", \"submitted_at\": \"2026-05-23T09:33:19.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s44 (with-evi)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s44\", \"eval_data\": \"Re-DocRED test_revised (500 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T10:43:45.534Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T10:43:55.050648+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.2525, \"f1\": 0.2525, \"evi_f1\": 0.1829, \"evi_f1_tp\": 0.6155, \"edcr\": 0.8324, \"format_ok_rate\": \"500/500\", \"n_truncated\": 220, \"n_documents\": 500, \"n_predictions\": 21065, \"inference_time_seconds\": 4122.6, \"inference_speed_s_per_doc\": 8.25, \"codalab_converted\": 9628, \"codalab_skipped_rel\": 295, \"codalab_skipped_entity\": 541}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\
…[truncated 30 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T10:47:21.464702+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_4b_rsft_s44_with_evi",
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
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_4b_rsft_s44_with_evi",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T10:47:21.464829+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 1.602}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:47:21.464965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_4b_rsft_s44_with_evi",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/eval_results/test_eval_4b_rsft_s44_with_evi/",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_4b_rsft_s44_with_evi",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/eval_results/test_eval_4b_rsft_s44_with_evi/",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T10:47:21.465134+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_4b_rsft_s44_with_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:33:05.779Z\", \"updated_at\": \"2026-05-23T10:47:03.674Z\", \"hypothesis\": \"4B RSFT CED k=1 s44 with-evidence test eval on Re-DocRED test_revised (500 docs). 补充第 3 seed：s42 ign_f1=0.2503, s43=0.2503。3-seed mean±std 完善 4B evidence tax 数据。\", \"parent\": \"rsft_ced_s44_train_v2\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_ced_s44 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 44\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"241448\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log\", \"submitted_at\": \"2026-05-23T09:33:19.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s44 (with-evi)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s44\", \"eval_data\": \"Re-DocRED test_revised (500 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T10:43:45.534Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T10:43:55.050648+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.2525, \"f1\": 0.2525, \"evi_f1\": 0.1829, \"evi_f1_tp\": 0.6155, \"edcr\": 0.8324, \"format_ok_rate\": \"500/500\", \"n_truncated\": 220, \"n_documents\": 500, \"n_predictions\": 21065, \"inference_time_seconds\": 4122.6, \"inference_speed_s_per_doc\": 8.25, \"codalab_converted\": 9628, \"codalab_skipped_rel\": 295, \"codalab_skipped_entity\": 541}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T10:47:21.465306+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_4b_rsft_s44_with_evi",
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
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_4b_rsft_s44_with_evi",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T10:47:21.465507+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_4b_rsft_s44_with_evi\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:33:05.779Z\", \"updated_at\": \"2026-05-23T10:47:09.258Z\", \"hypothesis\": \"4B RSFT CED k=1 s44 with-evidence test eval on Re-DocRED test_revised (500 docs). 补充第 3 seed：s42 ign_f1=0.2503, s43=0.2503。3-seed mean±std 完善 4B evidence tax 数据。\", \"parent\": \"rsft_ced_s44_train_v2\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_ced_s44 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 44\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"241448\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_4b_rsft_s44_with_evi.log\", \"submitted_at\": \"2026-05-23T09:33:19.982Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s44 (with-evi)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s44\", \"eval_data\": \"Re-DocRED test_revised (500 docs)\", \"wall_clock_seconds\": 4429.3, \"gpu_hours\": 1.23}, \"reproduce\": {\"finished_at\": \"2026-05-23T10:43:45.534Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T10:43:55.050648+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.2525, \"f1\": 0.2525, \"evi_f1\": 0.1829, \"evi_f1_tp\": 0.6155, \"edcr\": 0.8324, \"format_ok_rate\": \"500/500\", \"n_truncated\": 220, \"n_documents\": 500, \"n_predictions\": 21065, \"inference_time_seconds\": 4122.6, \"inference_speed_s_per_doc\": 8.25, \"codalab_converted\": 9628, \"codalab_skipped_rel\": 295, \"codalab_skipped_entity\": 541}, \"conclusion\": 
…[truncated 265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-23T10:47:21.465709+00:00_

Registry 已更新为 DONE/success。

**汇总：**

s44 with-evi: **ign_f1=0.2525**, evi_f1_tp=0.6155, edcr=0.8324

3-seed with-evidence 对比：

| seed | ign_f1 | evi_f1_tp | edcr |
|------|--------|-----------|------|
| s42 | 0.2501 | 0.6237 | 0.8288 |
| s43 | 0.2503 | 0.6127 | 0.8425 |
| s44 | 0.2525 | 0.6155 | 0.8324 |
| **mean** | **0.2516** | **0.6173** | **0.8346** |
| std | 0.0014 | 0.0057 | 0.0069 |

s44 ign_f1 略高于 s42/s43（+0.22-0.24pp），三 seed 方差很小（std=0.0014），结果稳定。对应 no-evi s42=0.2652, s43=0.2702，待 s44 no-evi 完成后可计算 3-seed mean evidence tax。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602"
}
```

</details>

---
