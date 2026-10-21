# analysis eval llama rsft s44 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342.jsonl`
- **Structured JSON:** [`4f1600b30a180a82841b.json`](../../sessions/4f/4f1600b30a180a82841b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-20T16:44:18.950656+00:00_

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
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
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

_source line 2 · 2026-05-20T16:44:18.951069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T16:44:18.951272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/runs/faith-evidence-ie/eval_llama_rsft_s44_no_evidence.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/runs/faith-evidence-ie/eval_llama_rsft_s44_no_evidence.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T16:44:18.951571+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 22:50:54,839 INFO Detected adapter at /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44, base: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-20 22:50:54,839 INFO Loading tokenizer: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-20 22:50:55,680 INFO Loading model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:50,  5.75it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:49,  5.89it/s]\\rLoading weights:   5%|▍         | 14/291 [00:00<00:06, 41.49it/s]\\rLoading weights:   9%|▉         | 27/291 [00:00<00:03, 67.82it/s]\\rLoading weights:  14%|█▎        | 40/291 [00:00<00:02, 86.04it/s]\\rLoading weights:  18%|█▊        | 51/291 [00:00<00:02, 89.19it/s]\\rLoading weights:  23%|██▎       | 67/291 [00:00<00:02, 108.03it/s]\\rLoading weights:  27%|██▋       | 79/291 [00:00<00:01, 107.18it/s]\\rLoading weights:  32%|███▏      | 94/291 [00:01<00:01, 114.88it/s]\\rLoading weights:  36%|███▋      | 106/291 [00:01<00:01, 105.41it/s]\\rLoading weights:  42%|████▏     | 121/291 [00:01<00:01, 116.98it/s]\\rLoading weights:  46%|████▌     | 134/291 [00:01<00:01, 114.54it/s]\\rLoading weights:  51%|█████     | 148/291 [00:01<00:01, 120.04it/s]\\rLoading weights:  55%|█████▌    | 161/291 [00:01<00:01, 115.08it/s]\\rLoading weights:  60%|██████    | 176/291 [00:01<00:00, 118.85it/s]\\rLoading weights:  65%|██████▍   | 189/291 [00:01<00:00, 117.27it/s]\\rLoading weights:  69%|██████▉   | 202/291 [00:02<00:00, 117.90it/s]\\rLoading weights:  74%|███████▎  | 214/291 [00:02<00:00, 112.66it/s]\\rLoading weights:  78%|███████▊  | 226/291 [00:02<00:00, 100.96it/s]\\rLoading weights:  85%|████████▍ | 247/291 [00:02<00:00, 125.55it/s]\\rLoading weights:  89%|████████▉ | 260/291 [00:02<00:00, 122.13it/s]\\r
…[truncated 6446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T16:44:18.951765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T16:44:18.951956+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5711188927797232,\\n  \\\"recall\\\": 0.5637396099086495,\\n  \\\"f1\\\": 0.5674052598881756,\\n  \\\"ign_precision\\\": 0.5487804878048781,\\n  \\\"ign_recall\\\": 0.5614083726088162,\\n  \\\"ign_f1\\\": 0.5550226120323422,\\n  \\\"tp\\\": 6850,\\n  \\\"pred_count\\\": 11994,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 1.0,\\n  \\\"evi_recall\\\": 0.0004877029192503309,\\n  \\\"evi_f1\\\": 0.0009749303621169917,\\n  \\\"n_evaluated\\\": 22,\\n  \\\"edcr\\\": 0.6818181818181818,\\n  \\\"n_distractor_citations\\\": 15,\\n  \\\"n_total_citations\\\": 22,\\n  \\\"evi_joint_precision\\\": 0.3333333333333333,\\n  \\\"evi_joint_recall\\\": 5.191838429988059e-05,\\n  \\\"evi_f1_joint\\\": 0.00010382059800664452,\\n  \\\"evi_tp\\\": 1,\\n  \\\"evi_pred_total\\\": 3,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 18089,\\n  \\\"n_truncated\\\": 178,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 6555.2,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}
…[truncated 104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T16:44:18.952158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/eval_llama_rsft_s44_no_evidence/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T16:44:18.952328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6588\\ndrwxr-xr-x   2 root root      62 May 21 00:40 .\\ndrwxr-xr-x 118 root root    8192 May 21 00:13 ..\\n-rw-r--r--   1 root root    1528 May 21 00:40 metrics.json\\n-rw-r--r--   1 root root 6727260 May 21 00:40 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T16:44:18.952510+00:00_

没有 format-OK subset 文件。全部指标如下：

```
ign_f1=0.5550
f1=0.5674
evi_f1=0.0010 (TP-only)
evi_f1_joint=0.0001
edcr=0.6818
format_compliance=0.9990 (984/985)
n_truncated=178
n_predictions=18089
inference_time=6555.2s
n_documents=985
n_format_ok=984
```

补充：
- `no_evidence=true` 已确认传入
- evi_f1 ≈ 0 符合预期（no-evidence 模型几乎不输出 evidence）
- format-OK subset 指标不存在，eval 脚本未生成该子集（984/985 几乎全量，差异可忽略）

**Evidence tax 计算（LLaMA RSFT 3-seed）：**

| seed | with-evi ign_f1 | no-evi ign_f1 | tax (pp) |
|------|----------------|---------------|----------|
| s42 | 0.5714 | 0.5526 | +1.88 |
| s43 | 0.5662 | 0.5546 | +1.16 |
| s44 | 0.5587 | 0.5550 | +0.37 |

**Mean evidence tax = +1.14 pp, std = 0.76 pp**

3 个 seed 均为正 tax（with-evidence > no-evidence），表明 evidence 训练对关系抽取性能有一致的正向贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342"
}
```

</details>

---
