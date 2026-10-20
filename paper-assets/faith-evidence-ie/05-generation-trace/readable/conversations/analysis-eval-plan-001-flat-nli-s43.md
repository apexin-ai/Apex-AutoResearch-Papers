# analysis eval plan 001 flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445.jsonl`
- **Structured JSON:** [`e7d2367506cef03c6389.json`](../../sessions/e7/e7d2367506cef03c6389.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T21:35:47.360387+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T21:35:47.360902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T21:35:47.361190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T21:35:47.361506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/rsft_flat_nli_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/rsft_flat_nli_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T21:35:47.361809+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 04:30:30,724 INFO Detected adapter at /root/autodl-tmp/rsft_output_flat_nli_s43, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 04:30:30,724 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 04:30:31,048 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 04:30:31,276 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.16it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.28it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.86it/s]\\n2026-05-16 04:30:32,920 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_flat_nli_s43\\n2026-05-16 04:30:36,040 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 04:30:36,364 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 04:30:36,548 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/62 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   2%|▏         | 1/62 [00:56<57:25, 56.49s/it]\\rInference:   3%|▎         | 2/62 [01:52<56:17, 56.29s/it]\\rInference:   5%|▍         | 3/62 [02:52<56:57, 57.92s/it]\\rInference:   6%|▋         | 4/62 [03:49<55:42, 57.64s/it]\\rInference:   8%|▊         | 5/62 [04:49<55:35, 58.51s/it]\\rInference:  10%|▉         | 6/62 [05:48<54:43, 58.64s/it]\\rInference:  11%|█▏        | 7/62 [06:46<53:38, 58.51s/it]\\rInference:  13%|█▎        | 8/62 [07:44<52:20, 58.15s/it]\\rInfer
…[truncated 4183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T21:35:47.362061+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7928\\ndrwxr-xr-x  2 root root      62 May 16 05:31 .\\ndrwxr-xr-x 37 root root    4096 May 16 05:10 ..\\n-rw-r--r--  1 root root    1469 May 16 05:31 metrics.json\\n-rw-r--r--  1 root root 8108011 May 16 05:31 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T21:35:47.362358+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T21:35:47.362715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.00196078431372549,\\n  \\\"recall\\\": 0.002633528104682742,\\n  \\\"f1\\\": 0.002247901373327245,\\n  \\\"ign_precision\\\": 0.00196078431372549,\\n  \\\"ign_recall\\\": 0.002633528104682742,\\n  \\\"ign_f1\\\": 0.002247901373327245,\\n  \\\"tp\\\": 32,\\n  \\\"pred_count\\\": 16320,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 1.0,\\n  \\\"evi_recall\\\": 0.7441860465116279,\\n  \\\"evi_f1\\\": 0.8533333333333333,\\n  \\\"n_evaluated\\\": 17230,\\n  \\\"edcr\\\": 0.9981751824817519,\\n  \\\"n_distractor_citations\\\": 17504,\\n  \\\"n_total_citations\\\": 17536,\\n  \\\"evi_joint_precision\\\": 0.0019154794684544474,\\n  \\\"evi_joint_recall\\\": 0.0016613882975961788,\\n  \\\"evi_f1_joint\\\": 0.0017794089026051659,\\n  \\\"evi_tp\\\": 32,\\n  \\\"evi_pred_total\\\": 16706,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9959390862944163,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 981,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 17285,\\n  \\\"n_truncated\\\": 251,\\n  \\\"n_format_ok\\\": 981,\\n  \\\"format_ok_rate\\\": 0.9959390862944163,\\n  \\\"inference_time_seconds\\\": 3669.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_flat_nli_s43\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_flat_nli_s43\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 43,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"met
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T21:35:47.363076+00:00_

## 评估结果: `eval_plan_001_flat_nli_s43`

### 关键指标

| 指标 | 值 | flat-NLI s42 | 差异 |
|------|-----|-------------|------|
| **rel_f1** | **0.0022** | 0.4539 | **-0.4517** |
| **ign_f1** | **0.0022** | — | — |
| **evi_f1** | 0.8533 | 0.8043 | +0.0490 |
| **edcr** | 0.9982 | 0.6431 | +0.3551 |
| precision | 0.0020 | — | — |
| recall | 0.0026 | — | — |
| evi_precision | 1.0000 | — | — |
| evi_recall | 0.7442 | — | — |
| format_ok_rate | 99.6% (981/985) | — | — |
| **field_compliance_rate** | **0.0%** | — | — |
| **evidence_format_rate** | **0.0%** | — | — |
| n_predictions | 17285 | — | — |
| n_truncated | 251/985 | — | — |
| inference_time_seconds | 3669.3 | — | — |
| TP | 32 / 16320 pred / 12151 gold | — | — |

### 诊断

**结果是灾难性的。** rel_f1 = 0.0022，比 s42 (0.4539) 下降 99.5%，比 CED RSFT mean (0.4596) 下降 99.5%。

**根因: 输出格式完全对不上。**
- `field_compliance_rate = 0.0%` — 所有预测的字段格式都不合规
- `evidence_format_rate = 0.0%` — 所有预测的 evidence 格式都不合规
- 模型输出能 parse（99.6% format_ok），但 relation/entity 字段内容与 gold 完全不匹配
- 16320 个预测只有 32 个 TP，命中率 0.2%
- EDCR = 0.9982 说明 17504/17536 个 citation 指向 distractor 句子

这**不是正常 seed 方差**——同 recipe 的 s42 有 rel_f1=0.4539，s43 几乎归零。最可能的原因：
1. s43 checkpoint 训练过程出了问题（训崩了/过拟合到错误模式）
2. 训练数据的 seed shuffle 导致 s43 收敛到退化解
3. LoRA adapter 保存不完整或加载了错误的 checkpoint

### 日志状态
- 进程正常结束，EXIT_CODE=0，无 OOM
- 251/985 文档被截断（25.5%，需关注但非主因）
- 无错误

### Registry 信息
- **checkpoint_path**: `/root/autodl-tmp/rsft_output_flat_nli_s43`
- **base_model**: `/root/autodl-tmp/models/Qwen3-4B`
- **log_path**: `~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log`
- **output_dir**: `/root/autodl-tmp/eval_results/rsft_flat_nli_s43/`

**建议检查 s43 的训练日志和 checkpoint，确认 adapter 是否正常。** 这个 seed 的结果不可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_plan_001_flat_nli_s43_20260515T213445"
}
```

</details>

---
