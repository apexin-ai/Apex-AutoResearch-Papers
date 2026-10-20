# analysis test eval llama rsft s43 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223.jsonl`
- **Structured JSON:** [`f5820b3cc5373f13d569.json`](../../sessions/f5/f5820b3cc5373f13d569.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-23T10:22:47.956259+00:00_

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
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
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

_source line 2 · 2026-05-23T10:22:47.956630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:22:47.956806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_llama_rsft_s43_no_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_llama_rsft_s43_no_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T10:22:47.957051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/test_eval_llama_rsft_s43_no_evi/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/test_eval_llama_rsft_s43_no_evi/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T10:22:47.957310+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 17:12:03,821 INFO Detected adapter at /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43, base: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-23 17:12:03,821 INFO Loading tokenizer: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-23 17:12:04,561 INFO Loading model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:35,  8.26it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:38,  7.53it/s]\\rLoading weights:   5%|▌         | 15/291 [00:00<00:05, 51.85it/s]\\rLoading weights:  11%|█         | 32/291 [00:00<00:02, 87.56it/s]\\rLoading weights:  17%|█▋        | 49/291 [00:00<00:02, 110.04it/s]\\rLoading weights:  21%|██        | 61/291 [00:00<00:02, 112.53it/s]\\rLoading weights:  26%|██▋       | 77/291 [00:00<00:01, 122.41it/s]\\rLoading weights:  32%|███▏      | 94/291 [00:00<00:01, 131.45it/s]\\rLoading weights:  37%|███▋      | 108/291 [00:01<00:01, 130.22it/s]\\rLoading weights:  42%|████▏     | 123/291 [00:01<00:01, 130.25it/s]\\rLoading weights:  48%|████▊     | 140/291 [00:01<00:01, 136.20it/s]\\rLoading weights:  54%|█████▍    | 157/291 [00:01<00:00, 142.29it/s]\\rLoading weights:  59%|█████▉    | 172/291 [00:01<00:00, 140.49it/s]\\rLoading weights:  64%|██████▍   | 187/291 [00:01<00:00, 136.84it/s]\\rLoading weights:  70%|██████▉   | 203/291 [00:01<00:00, 138.39it/s]\\rLoading weights:  76%|███████▌  | 220/291 [00:01<00:00, 144.33it/s]\\rLoading weights:  81%|████████  | 235/291 [00:01<00:00, 141.64it/s]\\rLoading weights:  86%|████████▌ | 250/291 [00:02<00:00, 139.33it/s]\\rLoading weights:  91%|█████████▏| 266/291 [00:02<00:00, 141.86it/s]\\rLoading weights:  97%|█████████▋| 283/291 [00:02<00:00, 146.29it/s]\\rLoading weights: 100%|██████████| 291/291 [00:02<00:00, 125.79it/s]
…[truncated 3909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:22:47.957515+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8224\\ndrwxr-xr-x   2 root root     102 May 23 18:20 .\\ndrwxr-xr-x 176 root root   12288 May 23 17:42 ..\\n-rw-r--r--   1 root root  447220 May 23 18:20 codalab_submission.json\\n-rw-r--r--   1 root root 7948760 May 23 18:20 predictions.json\\n-rw-r--r--   1 root root    1722 May 23 18:20 test_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-23T10:22:47.957710+00:00_

## test_eval_llama_rsft_s43_no_evi Metrics

| Metric | 值 |
|--------|-----|
| **Ign-F1** | **0.3371** |
| F1 | 0.3371 |
| Precision | — (未单独输出，Ign-F1=F1 因 train_annotated.json 缺失) |
| Recall | — |
| Evi-F1 (DREEAM) | 0.0032 |
| Evi-F1 (TP) | 0.0035 |
| EDCR | 0.9640 |
| Documents | 500 |
| Predictions | 32541 |
| Format OK | 499/500 |
| Truncated | 306/500 |
| CodaLab converted | 9166 |
| CodaLab skipped (rel) | 432 |
| CodaLab skipped (entity) | 2183 |

结果目录包含：`predictions.json`、`codalab_submission.json`、`test_summary.json`

## s43 Evidence Tax

s43_no_evi - s43_with_evi = 0.3371 - 0.3488 = **-1.17pp**

## 对比 s42

| Seed | no-evi | with-evi | evidence tax |
|------|--------|----------|-------------|
| s42 | 0.3334 | 0.3599 | -2.65pp |
| s43 | 0.3371 | 0.3488 | -1.17pp |

s43 的 evidence tax（-1.17pp）比 s42（-2.65pp）小了约一半，with-evi 提升幅度更小。两个 seed 的 no-evi 基线接近（0.3334 vs 0.3371），差异主要来自 s43 的 with-evi 效果弱于 s42。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223"
}
```

</details>

---
