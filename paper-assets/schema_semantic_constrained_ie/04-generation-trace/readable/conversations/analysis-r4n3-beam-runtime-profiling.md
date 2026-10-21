# analysis r4n3 beam runtime profiling

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_r4n3_beam_runtime_profiling_20260518T120631.jsonl`
- **Structured JSON:** [`def31c622e2f07f57df2.json`](../../sessions/de/def31c622e2f07f57df2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-18T12:10:01.460656+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T12:10:01.461061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T12:10:01.461251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -lh /root/schema_semantic_constrained_ie/outputs/ "
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "ls -lh /root/schema_semantic_constrained_ie/outputs/ "
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T12:10:01.461384+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -lh /root/schema_semantic_constrained_ie/logs/ "
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "ls -lh /root/schema_semantic_constrained_ie/logs/ "
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T12:10:01.461616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 326M\\n-rw-r--r-- 1 root root  659 May 16 20:31 analysis_llama_docred_ft_grammar_only.json\\n-rw-r--r-- 1 root root  660 May 15 23:01 analysis_llama_docred_full_s1_mt6144_v2.json\\n-rw-r--r-- 1 root root  653 May 15 04:27 analysis_llama_docred_full_s1_v2.json\\n-rw-r--r-- 1 root root  663 May 15 22:09 analysis_llama_docred_unconstrained_mt6144_v2.json\\n-rw-r--r-- 1 root root  647 May 17 15:36 analysis_llama_docred_unconstrained_v2.json\\n-rw-r--r-- 1 root root  663 May 16 12:54 analysis_w5_llama_docred_lora_constrained_v2.json\\n-rw-r--r-- 1 root root 121K May 17 08:37 beam_search_50.jsonl\\n-rw-r--r-- 1 root root  21K May 17 08:32 beam_search_dryrun_10.jsonl\\n-rw-r--r-- 1 root root  27K May 17 09:39 beam_search_full_551.log\\n-rw-r--r-- 1 root root 1.3M May 17 09:39 beam_search_scierc_full_551.jsonl\\n-rw-r--r-- 1 root root 2.7K May 17 21:57 bootstrap_ci_ft_composability.json\\n-rw-r--r-- 1 root root 7.9K May 15 02:19 bootstrap_ci_results.json\\n-rw-r--r-- 1 root root 2.9K May 15 06:56 bootstrap_ci_results_llama.json\\n-rw-r--r-- 1 root root 9.6K May 15 02:51 bootstrap_ci_results_v2.json\\ndrwxr-xr-x 2 root root 4.0K May 15 22:56 cf_analysis\\ndrwxr-xr-x 2 root root  185 May 15 22:52 cf_analysis_w1_pilot\\n-rw-r--r-- 1 root root  40K May 14 10:16 cf_violation_analysis.json\\n-rw-r--r-- 1 root root 5.7K May 14 04:11 comparison_minimal_vs_schema_informed.json\\n-rw-r--r-- 1 root root  16K May 18 00:34 debug_final.log\\n-rw-r--r-- 1 root root  16K May 18 00:16 debug_semantic.log\\n-rw-r--r-- 1 root root 7.3K May 18 00:18 debug_semantic2.log\\n-rw-r--r-- 1 root root 5.2K May 17 20:25 doc_length_breakdown.json\\n-rw-r--r-- 1 root root  10M May 15 02:18 docred_full_s1.jsonl\\n-rw-r--r-- 1 root root 497K May 17 15:06 docred_full_s1_consensus_50.jsonl\\n-rw-r--r-- 1 root root 988K May 14 11:15 docred_full_s1_dryrun.jsonl\\n-rw-r--r-- 1 root root  11M May 14 15:36 docred_grammar_only.jsonl\\n-rw-r--r-- 1 root r
…[truncated 6416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T12:10:01.461828+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 448K\\n-rw-r--r-- 1 root root 3.4K May 17 08:37 beam_50.log\\n-rw-r--r-- 1 root root 1.6K May 17 08:32 beam_dryrun_10.log\\n-rw-r--r-- 1 root root  27K May 17 17:25 beam_k2.log\\n-rw-r--r-- 1 root root  27K May 17 17:41 beam_k8.log\\n-rw-r--r-- 1 root root 1.6K May 17 13:13 dryrun_consensus_10.log\\n-rw-r--r-- 1 root root 1.6K May 17 13:16 dryrun_consensus_10_v2.log\\n-rw-r--r-- 1 root root 5.7K May 18 07:37 llama_constrained_retry.log\\n-rw-r--r-- 1 root root 2.7K May 18 11:14 llama_grammar_only.log\\n-rw-r--r-- 1 root root  32K May 18 14:30 llama_grammar_only_246.log\\n-rw-r--r-- 1 root root 1.6K May 18 12:08 llama_grammar_only_restart.log\\n-rw-r--r-- 1 root root  25K May 18 03:26 llama_restart.log\\n-rw-r--r-- 1 root root 5.3K May 18 10:44 llama_retry_16k.log\\n-rw-r--r-- 1 root root  36K May 18 07:22 mistral_constrained_full.log\\n-rw-r--r-- 1 root root  35K May 18 08:29 mistral_constrained_v2_full.log\\n-rw-r--r-- 1 root root  31K May 18 18:28 mistral_grammar_only_v3.log\\n-rw-r--r-- 1 root root 5.0K May 18 11:33 mistral_v2_retry_16k.log\\n-rw-r--r-- 1 root root 1.4K May 18 15:10 mistral_v3_full.log\\n-rw-r--r-- 1 root root 4.1K May 18 08:24 qwen_constrained_retry.log\\n-rw-r--r-- 1 root root 2.1K May 18 09:44 qwen_grammar_only.log\\n-rw-r--r-- 1 root root 3.6K May 18 13:39 qwen_retry_16k.log\\n-rw-r--r-- 1 root root  14K May 18 18:14 qwen_v3_full.log\\n-rw-r--r-- 1 root root  27K May 17 18:23 w10_qwen_scierc_ft_beam_k4.log\\n-rw-r--r-- 1 root root  46K May 16 00:55 w5_llama_lora_scierc_training.log\\n-rw-r--r-- 1 root root  66K May 16 01:38 w5_llama_lora_scierc_unconstrained_eval.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T12:10:01.462024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -3 /root/schema_semantic_constrained_ie/outputs/beam_search_scierc_full_551.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -3 /root/schema_semantic_constrained_ie/outputs/beam_search_scierc_full_551.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T12:10:01.462225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/beam_search_full_551.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/outputs/beam_search_full_551.log"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T12:10:01.462363+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/logs/beam_50.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/logs/beam_50.log"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T12:10:01.462697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"X96-1059_sent0\\\", \\\"input_text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\"}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\"}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"OtherScientificTerm\\\", \\\"tail_type\\\": \\\"Material\\\"}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Used-for\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}], \\\"raw_output\\\": \\\"{\\\\n  \\\\\\\"entities\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"Recognition of proper nouns in Japanese text\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"morphological analysis in Japanese text processing\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"1\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"2\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificT
…[truncated 7555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T12:10:01.462911+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/logs/beam_k2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/logs/beam_k2.log"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T12:10:01.463045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/logs/beam_k8.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "cat /root/schema_semantic_constrained_ie/logs/beam_k8.log"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T12:10:01.463261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nMode: full_s1\\nDataset: scierc\\nModel: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B\\nDevice: cuda:0\\nDecoding: beam search (num_beams=4)\\nSamples: 551\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:03,  1.31it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.35it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.37it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:02<00:00,  1.48it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.95it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.66it/s]\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\nModel loaded\\nGrammar compiled (full schema)\\n[1/551] X96-1059_sent0: OK E=4 R=1 6.8s\\n[2/551] X96-1059_sent1: OK E=2 R=1 3.1s\\n[3/551] X96-1059_sent2: OK E=4 R=3 6.1s\\n[4/551] X96-1059_sent3: OK E=7 R=5 8.9s\\n[5/551] X96-1059_sent4: OK E=2 R=1 2.2s\\n[6/551] X96-1059_sent5: OK E=4 R=3 4.7s\\n[7/551] X96-1059_sent6: OK E=2 R=1 4.4s\\n[8/551] X96-1059_sent7: OK E=4 R=3 5.0s\\n[9/551] X96-1059_sent8: OK E=4 R=3 4.7s\\n[10/551] ICCV_2001_47_abs_sent0: OK E=3 R=2 5.2s\\n[11/551] ICCV_2001_47_abs_sent1: OK E=4 R=3 4.9s\\n[12/551] ICCV_2001_47_abs_sent2: OK E=6 R=4 5.8s\\n[13/551] ICCV_2001_47_abs_sent3: OK E=6 R=3 8.0s\\n[14/551] ICCV_2001_47_abs_sent4: OK E=3 R=2 3.8s\\n[15/551] ICCV_2001_47_abs_sent5: OK E=2 R=1 6.4s\\n[16/551] INTERSPEECH_2013_21_abs_sent0: OK E=3 R=2 3.8s\\n[17/551] INTERSPEECH_2013_21_abs_sent1: OK E=3 R=2 3.8s\\n[18/551] INTERSPEECH_2013_21_abs_sent2: OK E=3 R=2 3.7s\\n[19/551] INTERSPEEC
…[truncated 6537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T12:10:01.463480+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nMode: full_s1\\nDataset: scierc\\nModel: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B\\nDevice: cuda:0\\nDecoding: beam search (num_beams=4)\\nSamples: 50\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:03,  1.32it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.35it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.37it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:02<00:00,  1.48it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.95it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.66it/s]\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\nModel loaded\\nGrammar compiled (full schema)\\n[1/50] X96-1059_sent0: OK E=4 R=1 6.9s\\n[2/50] X96-1059_sent1: OK E=2 R=1 3.2s\\n[3/50] X96-1059_sent2: OK E=4 R=3 6.1s\\n[4/50] X96-1059_sent3: OK E=7 R=5 9.0s\\n[5/50] X96-1059_sent4: OK E=2 R=1 2.2s\\n[6/50] X96-1059_sent5: OK E=4 R=3 4.7s\\n[7/50] X96-1059_sent6: OK E=2 R=1 4.5s\\n[8/50] X96-1059_sent7: OK E=4 R=3 5.1s\\n[9/50] X96-1059_sent8: OK E=4 R=3 4.7s\\n[10/50] ICCV_2001_47_abs_sent0: OK E=3 R=2 5.3s\\n[11/50] ICCV_2001_47_abs_sent1: OK E=4 R=3 5.0s\\n[12/50] ICCV_2001_47_abs_sent2: OK E=6 R=4 5.8s\\n[13/50] ICCV_2001_47_abs_sent3: OK E=6 R=3 8.1s\\n[14/50] ICCV_2001_47_abs_sent4: OK E=3 R=2 3.8s\\n[15/50] ICCV_2001_47_abs_sent5: OK E=2 R=1 6.4s\\n[16/50] INTERSPEECH_2013_21_abs_sent0: OK E=3 R=2 3.8s\\n[17/50] INTERSPEECH_2013_21_abs_sent1: OK E=3 R=2 3.9s\\n[18/50] INTERSPEECH_2013_21_abs_sent2: OK E=3 R=2 3.7s\\n[19/50] INTERSPEECH_2013_21_abs_sent3:
…[truncated 1611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T12:10:01.463750+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nMode: full_s1\\nDataset: scierc\\nModel: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B\\nDevice: cuda:0\\nDecoding: beam search (num_beams=2)\\nSamples: 551\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:03,  1.29it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.33it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.36it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:02<00:00,  1.47it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.94it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.64it/s]\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\nModel loaded\\nGrammar compiled (full schema)\\n[1/551] X96-1059_sent0: OK E=4 R=1 4.3s\\n[2/551] X96-1059_sent1: OK E=2 R=1 2.2s\\n[3/551] X96-1059_sent2: OK E=4 R=3 5.0s\\n[4/551] X96-1059_sent3: OK E=7 R=5 8.1s\\n[5/551] X96-1059_sent4: OK E=2 R=1 2.2s\\n[6/551] X96-1059_sent5: OK E=4 R=3 4.4s\\n[7/551] X96-1059_sent6: OK E=4 R=4 4.4s\\n[8/551] X96-1059_sent7: OK E=4 R=3 4.9s\\n[9/551] X96-1059_sent8: OK E=4 R=3 3.7s\\n[10/551] ICCV_2001_47_abs_sent0: OK E=3 R=2 4.2s\\n[11/551] ICCV_2001_47_abs_sent1: OK E=4 R=3 4.8s\\n[12/551] ICCV_2001_47_abs_sent2: OK E=6 R=4 5.6s\\n[13/551] ICCV_2001_47_abs_sent3: OK E=6 R=3 6.7s\\n[14/551] ICCV_2001_47_abs_sent4: OK E=3 R=2 3.7s\\n[15/551] ICCV_2001_47_abs_sent5: OK E=2 R=1 2.3s\\n[16/551] INTERSPEECH_2013_21_abs_sent0: OK E=2 R=1 2.7s\\n[17/551] INTERSPEECH_2013_21_abs_sent1: OK E=3 R=2 3.7s\\n[18/551] INTERSPEECH_2013_21_abs_sent2: OK E=3 R=2 3.7s\\n[19/551] INTERSPEEC
…[truncated 6538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T12:10:01.463998+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nMode: full_s1\\nDataset: scierc\\nModel: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B\\nDevice: cuda:1\\nDecoding: beam search (num_beams=8)\\nSamples: 551\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:02,  1.33it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.34it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.36it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:02<00:00,  1.48it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.95it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.66it/s]\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\nModel loaded\\nGrammar compiled (full schema)\\n[1/551] X96-1059_sent0: OK E=4 R=1 7.6s\\n[2/551] X96-1059_sent1: OK E=2 R=1 3.5s\\n[3/551] X96-1059_sent2: OK E=4 R=3 5.8s\\n[4/551] X96-1059_sent3: OK E=7 R=5 10.2s\\n[5/551] X96-1059_sent4: OK E=2 R=1 2.4s\\n[6/551] X96-1059_sent5: OK E=4 R=3 5.2s\\n[7/551] X96-1059_sent6: OK E=5 R=3 6.2s\\n[8/551] X96-1059_sent7: OK E=4 R=3 6.0s\\n[9/551] X96-1059_sent8: OK E=4 R=3 5.2s\\n[10/551] ICCV_2001_47_abs_sent0: OK E=3 R=2 5.9s\\n[11/551] ICCV_2001_47_abs_sent1: OK E=4 R=3 6.4s\\n[12/551] ICCV_2001_47_abs_sent2: OK E=6 R=5 8.3s\\n[13/551] ICCV_2001_47_abs_sent3: OK E=6 R=3 8.9s\\n[14/551] ICCV_2001_47_abs_sent4: OK E=3 R=2 4.1s\\n[15/551] ICCV_2001_47_abs_sent5: OK E=2 R=1 7.6s\\n[16/551] INTERSPEECH_2013_21_abs_sent0: OK E=2 R=1 5.5s\\n[17/551] INTERSPEECH_2013_21_abs_sent1: OK E=3 R=2 6.2s\\n[18/551] INTERSPEECH_2013_21_abs_sent2: OK E=3 R=2 4.2s\\n[19/551] INTERSPEE
…[truncated 6537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T12:10:01.464181+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie/outputs -name \"*.jsonl\" -newer /root/schema_semantic_constrained_ie/outputs/dry_run.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "find /root/schema_semantic_constrained_ie/outputs -name \"*.jsonl\" -newer /root/schema_semantic_constrained_ie/outputs/dry_run.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T12:10:01.464317+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -1 /root/schema_semantic_constrained_ie/outputs/scierc_full_s1.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -1 /root/schema_semantic_constrained_ie/outputs/scierc_full_s1.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T12:10:01.464439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -1 /root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -1 /root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T12:10:01.464721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_docred.jsonl\\n/root/schema_semantic_constrained_ie/outputs/raw_outputs.jsonl\\n/root/schema_semantic_constrained_ie/outputs/raw_outputs_schema.jsonl\\n/root/schema_semantic_constrained_ie/outputs/raw_outputs_docred_schema.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_unconstrained.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_grammar_only.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_semantic_only.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_full_s1.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_full_s2.jsonl\\n/root/schema_semantic_constrained_ie/outputs/dryrun_phase2_grammar.jsonl\\n/root/schema_semantic_constrained_ie/outputs/posthoc_scierc.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_s2_fixed.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_s2_fixed2.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_grammar_only.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_unconstrained.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_s2_dryrun.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_s2_pilot50.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_grammar_only_partial_183.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s2.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_semantic_only.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_semantic_only_v2.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl\\n/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1.jsonl\\n/root/schema_semantic_constrained_ie/outputs/docred_grammar_only.jsonl\\n/root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl\\n/root/schema_semantic_constrained_ie/outputs/test_fix_full_s1.jsonl\\n/root/schema_semantic_constrained
…[truncated 6406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T12:10:01.464950+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/schema_semantic_constrained_ie/outputs/scierc_full_s1.jsonl' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 3.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T12:10:01.465252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"Skai TV\\\", \\\"input_text\\\": \\\"Skai TV is a Greek free - to - air television network based in Piraeus . It is part of the Skai Group , one of the largest media groups in the country . It was relaunched in its present form on 1st of April 2006 in the Athens metropolitan area , and gradually spread its coverage nationwide . Besides digital terrestrial transmission , it is available on the subscription - based encrypted services of Nova and Cosmote TV . Skai TV is also a member of Digea , a consortium of private television networks introducing digital terrestrial transmission in Greece . At launch , Skai TV opted for dubbing all foreign language content into Greek , instead of using subtitles . This is very uncommon in Greece for anything except documentaries ( using voiceover dubbing ) and children 's programmes ( using lip - synced dubbing ) , so after intense criticism the station switched to using subtitles for almost all foreign shows .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Skai TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Piraeus\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Skai Group\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"1st of April 2006\\\", \\\"type\\\": \\\"TIME\\\"}, {\\\"text\\\": \\\"Athens\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Nova\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Cosmote TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Digea\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greece\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"MISC\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Piraeus\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\\", \\\"head_type\\\": \\\"LOC\\\", \\\"tail_type\\\": \\\"LOC\\\"}, {\\\"head\\\": \\\"Skai Group\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\
…[truncated 6428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T12:10:01.465455+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json, statistics\n\nfiles = {\n    'Qwen SciERC beam k=4 (551)': 'outputs/beam_search_scierc_full_551.jsonl',\n    'Qwen SciERC beam k=2 (551)': 'outputs/scierc_qwen_beam_k2_551.jsonl',\n    'Qwen SciERC beam k=8 (551)': 'outputs/scierc_qwen_beam_k8_551.jsonl',\n    'Qwen SciERC FT beam k=4': 'outputs/w10_qwen_scierc_ft_beam_k4.jsonl',\n    'Qwen DocRED beam k=4 (50)': 'outputs/w9_qwen_docred_beam_50.jsonl',\n    'Llama DocRED beam k=4 (50)': 'outputs/docred_llama_beam_50.jsonl',\n    'Qwen DocRED greedy matched50': 'outputs/qwen_docred_greedy_matched50.jsonl',\n    'Llama DocRED greedy matched50': 'outputs/llama_docred_greedy_matched50.jsonl',\n    'Llama SciERC beam k=4 (551)': 'outputs/llama_scierc_beam_full_s1_551.jsonl',\n    'Qwen SciERC greedy (phase2_full_s1_v2)': 'outputs/phase2_scierc_full_s1_v2.jsonl',\n    'Qwen SciERC greedy (phase2_full_s1)': 'outputs/phase2_scierc_full_s1.jsonl',\n    'Llama SciERC greedy (full_s1)': 'outputs/llama_scierc_full_s1.jsonl',\n}\n\nfor name, fpath in files.items():\n    try:\n        times = []\n        with open(fpath) as f:\n            for line in f:\n                d = json.loads(line)\n                t = d.get('inference_time_seconds') or d.get('time_seconds') or d.get('generation_time')\n                if t is not None:\n                    times.append(float(t))\n        if times:\n            total = sum(times)\n            avg = statistics.mean(times)\n            med = statistics.median(times)\n            n = len(times)\n            # check decoding strategy from first line\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            strat = first.get('decoding_strategy', 'unknown')\n            beams = first.get('num_beams', '?')\n            print(f'{name} | n={n} | strategy={strat} beams={beams} | total={total:.1f}s | avg={avg:.3f}s | median={med:.3f}s | min={min(times):.3f}s | max={max(times):.3f}s')\n        else:\n            # check what keys exist\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            print(f'{name} | NO TIMING DATA | keys: {list(first.keys())[:10]}')\n    except FileNotFoundError:\n        print(f'{name} | FILE NOT FOUND')\n    except Exception as e:\n        print(f'{name} | ERROR: {e}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json, statistics\n\nfiles = {\n    'Qwen SciERC beam k=4 (551)': 'outputs/beam_search_scierc_full_551.jsonl',\n    'Qwen SciERC beam k=2 (551)': 'outputs/scierc_qwen_beam_k2_551.jsonl',\n    'Qwen SciERC beam k=8 (551)': 'outputs/scierc_qwen_beam_k8_551.jsonl',\n    'Qwen SciERC FT beam k=4': 'outputs/w10_qwen_scierc_ft_beam_k4.jsonl',\n    'Qwen DocRED beam k=4 (50)': 'outputs/w9_qwen_docred_beam_50.jsonl',\n    'Llama DocRED beam k=4 (50)': 'outputs/docred_llama_beam_50.jsonl',\n    'Qwen DocRED greedy matched50': 'outputs/qwen_docred_greedy_matched50.jsonl',\n    'Llama DocRED greedy matched50': 'outputs/llama_docred_greedy_matched50.jsonl',\n    'Llama SciERC beam k=4 (551)': 'outputs/llama_scierc_beam_full_s1_551.jsonl',\n    'Qwen SciERC greedy (phase2_full_s1_v2)': 'outputs/phase2_scierc_full_s1_v2.jsonl',\n    'Qwen SciERC greedy (phase2_full_s1)': 'outputs/phase2_scierc_full_s1.jsonl',\n    'Llama SciERC greedy (full_s1)': 'outputs/llama_scierc_full_s1.jsonl',\n}\n\nfor name, fpath in files.items():\n    try:\n        times = []\n        with open(fpath) as f:\n            for line in f:\n                d = json.loads(line)\n                t = d.get('inference_time_seconds') or d.get('time_seconds') or d.get('generation_time')\n                if t is not None:\n                    times.append(float(t))\n        if times:\n            total = sum(times)\n            avg = statistics.mean(times)\n            med = statistics.median(times)\n            n = len(times)\n            # check decoding strategy from first line\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            strat = first.get('decoding_strategy', 'unknown')\n            beams = first.get('num_beams', '?')\n            print(f'{name} | n={n} | strategy={strat} beams={beams} | total={total:.1f}s | avg={avg:.3f}s | median={med:.3f}s | min={min(times):.3f}s | max={max(times):.3f}s')\n        else:\n            # check what keys exist\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            print(f'{name} | NO TIMING DATA | keys: {list(first.keys())[:10]}')\n    except FileNotFoundError:\n        print(f'{name} | FILE NOT FOUND')\n    except Exception as e:\n        print(f'{name} | ERROR: {e}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T12:10:01.465643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen SciERC beam k=4 (551) | n=551 | strategy=beam beams=4 | total=3259.4s | avg=5.915s | median=5.506s | min=0.797s | max=16.941s\\nQwen SciERC beam k=2 (551) | n=551 | strategy=beam beams=2 | total=2969.7s | avg=5.390s | median=5.058s | min=0.741s | max=15.454s\\nQwen SciERC beam k=8 (551) | n=551 | strategy=beam beams=8 | total=3890.4s | avg=7.061s | median=6.642s | min=2.003s | max=21.063s\\nQwen SciERC FT beam k=4 | n=551 | strategy=beam beams=4 | total=2041.3s | avg=3.705s | median=3.324s | min=0.570s | max=19.431s\\nQwen DocRED beam k=4 (50) | n=50 | strategy=beam beams=4 | total=1567.6s | avg=31.352s | median=24.506s | min=13.527s | max=129.328s\\nLlama DocRED beam k=4 (50) | n=50 | strategy=beam beams=4 | total=1039.2s | avg=20.783s | median=16.970s | min=9.666s | max=48.718s\\nQwen DocRED greedy matched50 | n=50 | strategy=unknown beams=? | total=925.9s | avg=18.519s | median=18.126s | min=9.451s | max=33.095s\\nLlama DocRED greedy matched50 | n=50 | strategy=unknown beams=? | total=1060.9s | avg=21.219s | median=15.958s | min=6.732s | max=66.405s\\nLlama SciERC beam k=4 (551) | n=551 | strategy=beam beams=4 | total=2652.5s | avg=4.814s | median=4.631s | min=0.658s | max=15.984s\\nQwen SciERC greedy (phase2_full_s1_v2) | n=551 | strategy=unknown beams=? | total=3725.2s | avg=6.761s | median=5.981s | min=0.666s | max=20.371s\\nQwen SciERC greedy (phase2_full_s1) | n=7 | strategy=unknown beams=? | total=72.9s | avg=10.419s | median=9.881s | min=5.357s | max=17.481s\\nLlama SciERC greedy (full_s1) | n=550 | strategy=unknown beams=? | total=2379.1s | avg=4.326s | median=3.694s | min=0.206s | max=27.285s\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T12:10:01.465863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -1 /root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -1 /root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T12:10:01.466171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -1 /root/schema_semantic_constrained_ie/outputs/llama_scierc_full_s1.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -1 /root/schema_semantic_constrained_ie/outputs/llama_scierc_full_s1.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T12:10:01.466428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "command": "head -1 /root/schema_semantic_constrained_ie/outputs/qwen_docred_greedy_matched50.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "command": "head -1 /root/schema_semantic_constrained_ie/outputs/qwen_docred_greedy_matched50.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T12:10:01.466702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"X96-1059_sent0\\\", \\\"input_text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\"}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\"}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"OtherScientificTerm\\\", \\\"tail_type\\\": \\\"Material\\\"}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Used-for\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}], \\\"raw_output\\\": \\\"{\\\\n  \\\\\\\"entities\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"Recognition of proper nouns in Japanese text\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"morphological analysis in Japanese text processing\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"1\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\"\\\\n    },\\\\n    {\\\\n      \\\\\\\"text\\\\\\\": \\\\\\\"2\\\\\\\",\\\\n      \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificT
…[truncated 1298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T12:10:01.467029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"X96-1059_sent0\\\", \\\"input_text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\"}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\"}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\"}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Part-of\\\", \\\"head_type\\\": \\\"OtherScientificTerm\\\", \\\"tail_type\\\": \\\"Material\\\"}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Used-for\\\", \\\"head_type\\\": \\\"Task\\\", \\\"tail_type\\\": \\\"Task\\\"}], \\\"raw_output\\\": \\\"{\\\\n  \\\\\\\"entities\\\\\\\": [\\\\n    {\\\\\\\"text\\\\\\\": \\\\\\\"Japanese\\\\\\\", \\\\\\\"type\\\\\\\": \\\\\\\"Generic\\\\\\\"},\\\\n    {\\\\\\\"text\\\\\\\": \\\\\\\"text\\\\\\\", \\\\\\\"type\\\\\\\": \\\\\\\"Generic\\\\\\\"},\\\\n    {\\\\\\\"text\\\\\\\": \\\\\\\"problem\\\\\\\", \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\"},\\\\n    {\\\\\\\"text\\\\\\\": \\\\\\\"morphological analysis\\\\\\\", \\\\\\\"type\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\"},\\\\n    {\\\\\\\"text\\\\\\\": \\\\\\\"Japanese text processing\\\\\\\", \\\\\\\"type\\\\\\\": \\\\\\\"Task\\\\\\\"}\\\\n  ],\\\\n  \\\\\\\"relati
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T12:10:01.467559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": \\\"Skai TV\\\", \\\"input_text\\\": \\\"Skai TV is a Greek free - to - air television network based in Piraeus . It is part of the Skai Group , one of the largest media groups in the country . It was relaunched in its present form on 1st of April 2006 in the Athens metropolitan area , and gradually spread its coverage nationwide . Besides digital terrestrial transmission , it is available on the subscription - based encrypted services of Nova and Cosmote TV . Skai TV is also a member of Digea , a consortium of private television networks introducing digital terrestrial transmission in Greece . At launch , Skai TV opted for dubbing all foreign language content into Greek , instead of using subtitles . This is very uncommon in Greece for anything except documentaries ( using voiceover dubbing ) and children 's programmes ( using lip - synced dubbing ) , so after intense criticism the station switched to using subtitles for almost all foreign shows .\\\", \\\"gold_entities\\\": [{\\\"text\\\": \\\"Skai TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Piraeus\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Skai Group\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"1st of April 2006\\\", \\\"type\\\": \\\"TIME\\\"}, {\\\"text\\\": \\\"Athens\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Nova\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Cosmote TV\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Digea\\\", \\\"type\\\": \\\"ORG\\\"}, {\\\"text\\\": \\\"Greece\\\", \\\"type\\\": \\\"LOC\\\"}, {\\\"text\\\": \\\"Greek\\\", \\\"type\\\": \\\"MISC\\\"}], \\\"gold_relations\\\": [{\\\"head\\\": \\\"Piraeus\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\\", \\\"head_type\\\": \\\"LOC\\\", \\\"tail_type\\\": \\\"LOC\\\"}, {\\\"head\\\": \\\"Skai Group\\\", \\\"tail\\\": \\\"Greece\\\", \\\"type\\\": \\\"P17\\
…[truncated 9885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T12:10:01.467847+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16980",
  "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json, statistics\n\nfiles = {\n    'Qwen DocRED greedy full (full_s1)': 'outputs/docred_full_s1.jsonl',\n    'Llama DocRED greedy full': 'outputs/llama_docred_full_s1.jsonl',\n    'Llama DocRED greedy mt6144': 'outputs/llama_docred_full_s1_mt6144.jsonl',\n}\n\nfor name, fpath in files.items():\n    try:\n        times = []\n        count = 0\n        with open(fpath) as f:\n            for line in f:\n                count += 1\n                d = json.loads(line)\n                t = d.get('inference_time_seconds') or d.get('time_seconds') or d.get('generation_time')\n                if t is not None:\n                    times.append(float(t))\n        if times:\n            print(f'{name} | n={count} (timed={len(times)}) | total={sum(times):.1f}s | avg={statistics.mean(times):.3f}s | median={statistics.median(times):.3f}s')\n        else:\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            print(f'{name} | n={count} | NO TIMING | keys={list(first.keys())[:10]}')\n    except Exception as e:\n        print(f'{name} | ERROR: {e}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16980",
    "command": "cd /root/schema_semantic_constrained_ie && python3 -c \"\nimport json, statistics\n\nfiles = {\n    'Qwen DocRED greedy full (full_s1)': 'outputs/docred_full_s1.jsonl',\n    'Llama DocRED greedy full': 'outputs/llama_docred_full_s1.jsonl',\n    'Llama DocRED greedy mt6144': 'outputs/llama_docred_full_s1_mt6144.jsonl',\n}\n\nfor name, fpath in files.items():\n    try:\n        times = []\n        count = 0\n        with open(fpath) as f:\n            for line in f:\n                count += 1\n                d = json.loads(line)\n                t = d.get('inference_time_seconds') or d.get('time_seconds') or d.get('generation_time')\n                if t is not None:\n                    times.append(float(t))\n        if times:\n            print(f'{name} | n={count} (timed={len(times)}) | total={sum(times):.1f}s | avg={statistics.mean(times):.3f}s | median={statistics.median(times):.3f}s')\n        else:\n            with open(fpath) as f:\n                first = json.loads(f.readline())\n            print(f'{name} | n={count} | NO TIMING | keys={list(first.keys())[:10]}')\n    except Exception as e:\n        print(f'{name} | ERROR: {e}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T12:10:01.468021+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen DocRED greedy full (full_s1) | n=998 (timed=998) | total=20354.0s | avg=20.395s | median=18.812s\\nLlama DocRED greedy full | n=998 (timed=998) | total=20483.4s | avg=20.524s | median=15.790s\\nLlama DocRED greedy mt6144 | n=998 (timed=998) | total=23763.5s | avg=23.811s | median=15.791s\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T12:10:01.468210+00:00_

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
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
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

_source line 34 · 2026-05-18T12:10:01.468347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T12:10:01.468492+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_n3_runtime_profiling.md",
  "content": "# R4-N3: Beam Search vs Greedy Per-Document Runtime Profiling\n\n## Data Sources\n\nAll experiments run on westd-16980 with grammar-constrained decoding.\n\n### Files Used\n\n| Experiment | Output File | Docs |\n|---|---|---|\n| Qwen SciERC greedy constrained | `phase2_scierc_full_s1_v2.jsonl` | 551 |\n| Qwen SciERC beam k=2 | `scierc_qwen_beam_k2_551.jsonl` | 551 |\n| Qwen SciERC beam k=4 | `beam_search_scierc_full_551.jsonl` | 551 |\n| Qwen SciERC beam k=8 | `scierc_qwen_beam_k8_551.jsonl` | 551 |\n| Qwen SciERC FT beam k=4 | `w10_qwen_scierc_ft_beam_k4.jsonl` | 551 |\n| Llama SciERC greedy constrained | `llama_scierc_full_s1.jsonl` | 550 |\n| Llama SciERC beam k=4 | `llama_scierc_beam_full_s1_551.jsonl` | 551 |\n| Qwen DocRED greedy (matched 50) | `qwen_docred_greedy_matched50.jsonl` | 50 |\n| Qwen DocRED beam k=4 | `w9_qwen_docred_beam_50.jsonl` | 50 |\n| Llama DocRED greedy (matched 50) | `llama_docred_greedy_matched50.jsonl` | 50 |\n| Llama DocRED beam k=4 | `docred_llama_beam_50.jsonl` | 50 |\n\n---\n\n## SciERC Runtime (551 docs, sentence-level)\n\n| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |\n|-------|----------|---|-----------|-----------------|--------------------|---------|---------| \n| Qwen-3-8B | greedy | 1 | 3725.2 | 6.761 | 5.981 | 0.666 | 20.371 |\n| Qwen-3-8B | beam | 2 | 2969.7 | 5.390 | 5.058 | 0.741 | 15.454 |\n| Qwen-3-8B | beam | 4 | 3259.4 | 5.915 | 5.506 | 0.797 | 16.941 |\n| Qwen-3-8B | beam | 8 | 3890.4 | 7.061 | 6.642 | 2.003 | 21.063 |\n| Qwen-3-8B (FT) | beam | 4 | 2041.3 | 3.705 | 3.324 | 0.570 | 19.431 |\n| Llama-3.1-8B | greedy | 1 | 2379.1 | 4.326 | 3.694 | 0.206 | 27.285 |\n| Llama-3.1-8B | beam | 4 | 2652.5 | 4.814 | 4.631 | 0.658 | 15.984 |\n\n### SciERC Overhead Analysis\n\n| Comparison | Avg Overhead | Median Overhead |\n|---|---|---|\n| Qwen beam k=4 vs greedy | 0.87x (faster) | 0.92x (faster) |\n| Qwen beam k=2 vs greedy | 0.80x (faster) | 0.85x (faster) |\n| Qwen beam k=8 vs greedy | 1.04x | 1.11x |\n| Llama beam k=4 vs greedy | 1.11x | 1.25x |\n\n**Caveat**: Qwen greedy run (`phase2_scierc_full_s1_v2`) was from an earlier experiment wave (May 14-15) while beam runs are from May 17. Different GPU thermal states, background processes, or codebase optimizations between runs could explain the anomalous result where beam k=2/4 appear faster than greedy. The Llama comparison (1.11x overhead) is more consistent with expectations.\n\n---\n\n## DocRED Runtime (50 matched docs, document-level)\n\n| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |\n|-------|----------|---|-----------|-----------------|--------------------|---------|---------| \n| Qwen-3-8B | greedy | 1 | 925.9 | 18.519 | 18.126 | 9.451 | 33.095 |\n| Qwen-3-8B | beam | 4 | 1567.6 | 31.352 | 24.506 | 13.527 | 129.328 |\n| Llama-3.1-8B | greedy | 1 | 1060.9 | 21.219 | 15.958 | 6.732 | 66.405 |\n| Llama-3.1-8B | beam | 4 | 1039.2 | 20.783 | 16.970 | 9.666 | 48.718 |\n\n### DocRED Overhead Analysis (matched 50-doc subset)\n\n| Comparison | Avg Overhead | Median Overhead |\n|---|---|---|\n| Qwen beam k=4 vs greedy | **1.69x** | **1.35x** |\n| Llama beam k=4 vs greedy | 0.98x (comparable) | 1.06x |\n\n**Qwen DocRED** shows the clearest beam overhead: 1.69x average, 1.35x median. The difference between mean and median indicates beam search has high-variance tail latency (max 129.3s vs greedy max 33.1s).\n\n**Llama DocRED** shows negligible overhead on average, but the greedy run has a high-variance tail (max 66.4s) that inflates its mean.\n\n---\n\n## Beam Width Scaling (Qwen SciERC, 551 docs)\n\n| k | Per-doc Avg (s) | Relative to k=2 |\n|---|-----------------|------------------|\n| 2 | 5.390 | 1.00x |\n| 4 | 5.915 | 1.10x |\n| 8 | 7.061 | 1.31x |\n\nBeam width scaling is sub-linear: doubling k from 2 to 4 adds ~10% latency; from 4 to 8 adds ~19%.\n\n---\n\n## Fine-tuned vs Zero-shot Beam (Qwen SciERC, k=4)\n\n| Setting | Per-doc Avg (s) | Per-doc Median (s) |\n|---|---|---|\n| Zero-shot beam k=4 | 5.915 | 5.506 |\n| Fine-tuned beam k=4 | 3.705 | 3.324 |\n| Speedup | **1.60x** | **1.66x** |\n\nFine-tuning reduces beam search latency by ~37%, likely because the model produces more confident token distributions, leading to earlier convergence.\n\n---\n\n## Summary for Paper\n\n**Recommended numbers to cite (most reliable comparisons):**\n\n1. **Qwen DocRED beam k=4 overhead**: 1.69x avg / 1.35x median over greedy (matched 50-doc subset, same GPU, close temporal proximity)\n2. **Beam width scaling** (SciERC): k=2 to k=4 adds 10%, k=4 to k=8 adds 19% (sub-linear)\n3. **FT speedup**: Fine-tuned beam k=4 is 1.6x faster than zero-shot beam k=4\n\n**Key finding**: Beam search (k=4) adds moderate latency overhead (~1.3-1.7x on document-level tasks), scaling sub-linearly with beam width. The overhead is more pronounced on longer documents (DocRED) where each beam candidate generates substantially more tokens.\n\n**Caveats**:\n- SciERC greedy vs beam comparison is confounded by different run dates; the matched DocRED 50-doc comparison is the most controlled\n- Llama DocRED shows near-zero overhead, possibly due to different tokenization efficiency or variance in greedy tail latency\n- For a clean SciERC comparison, a fresh greedy run on the same GPU session as beam runs would be ideal\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_n3_runtime_profiling.md",
    "content": "# R4-N3: Beam Search vs Greedy Per-Document Runtime Profiling\n\n## Data Sources\n\nAll experiments run on westd-16980 with grammar-constrained decoding.\n\n### Files Used\n\n| Experiment | Output File | Docs |\n|---|---|---|\n| Qwen SciERC greedy constrained | `phase2_scierc_full_s1_v2.jsonl` | 551 |\n| Qwen SciERC beam k=2 | `scierc_qwen_beam_k2_551.jsonl` | 551 |\n| Qwen SciERC beam k=4 | `beam_search_scierc_full_551.jsonl` | 551 |\n| Qwen SciERC beam k=8 | `scierc_qwen_beam_k8_551.jsonl` | 551 |\n| Qwen SciERC FT beam k=4 | `w10_qwen_scierc_ft_beam_k4.jsonl` | 551 |\n| Llama SciERC greedy constrained | `llama_scierc_full_s1.jsonl` | 550 |\n| Llama SciERC beam k=4 | `llama_scierc_beam_full_s1_551.jsonl` | 551 |\n| Qwen DocRED greedy (matched 50) | `qwen_docred_greedy_matched50.jsonl` | 50 |\n| Qwen DocRED beam k=4 | `w9_qwen_docred_beam_50.jsonl` | 50 |\n| Llama DocRED greedy (matched 50) | `llama_docred_greedy_matched50.jsonl` | 50 |\n| Llama DocRED beam k=4 | `docred_llama_beam_50.jsonl` | 50 |\n\n---\n\n## SciERC Runtime (551 docs, sentence-level)\n\n| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |\n|-------|----------|---|-----------|-----------------|--------------------|---------|---------| \n| Qwen-3-8B | greedy | 1 | 3725.2 | 6.761 | 5.981 | 0.666 | 20.371 |\n| Qwen-3-8B | beam | 2 | 2969.7 | 5.390 | 5.058 | 0.741 | 15.454 |\n| Qwen-3-8B | beam | 4 | 3259.4 | 5.915 | 5.506 | 0.797 | 16.941 |\n| Qwen-3-8B | beam | 8 | 3890.4 | 7.061 | 6.642 | 2.003 | 21.063 |\n| Qwen-3-8B (FT) | beam | 4 | 2041.3 | 3.705 | 3.324 | 0.570 | 19.431 |\n| Llama-3.1-8B | greedy | 1 | 2379.1 | 4.326 | 3.694 | 0.206 | 27.285 |\n| Llama-3.1-8B | beam | 4 | 2652.5 | 4.814 | 4.631 | 0.658 | 15.984 |\n\n### SciERC Overhead Analysis\n\n| Comparison | Avg Overhead | Median Overhead |\n|---|---|---|\n| Qwen beam k=4 vs greedy | 0.87x (faster) | 0.92x (faster) |\n| Qwen beam k=2 vs greedy | 0.80x (faster) | 0.85x (faster) |\n| Qwen beam k=8 vs greedy | 1.04x | 1.11x |\n| Llama beam k=4 vs greedy | 1.11x | 1.25x |\n\n**Caveat**: Qwen greedy run (`phase2_scierc_full_s1_v2`) was from an earlier experiment wave (May 14-15) while beam runs are from May 17. Different GPU thermal states, background processes, or codebase optimizations between runs could explain the anomalous result where beam k=2/4 appear faster than greedy. The Llama comparison (1.11x overhead) is more consistent with expectations.\n\n---\n\n## DocRED Runtime (50 matched docs, document-level)\n\n| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |\n|-------|----------|---|-----------|-----------------|--------------------|---------|---------| \n| Qwen-3-8B | greedy | 1 | 925.9 | 18.519 | 18.126 | 9.451 | 33.095 |\n| Qwen-3-8B | beam | 4 | 1567.6 | 31.352 | 24.506 | 13.527 | 129.328 |\n| Llama-3.1-8B | greedy | 1 | 1060.9 | 21.219 | 15.958 | 6.732 | 66.405 |\n| Llama-3.1-8B | beam | 4 | 1039.2 | 20.783 | 16.970 | 9.666 | 48.718 |\n\n### DocRED Overhead Analysis (matched 50-doc subset)\n\n| Comparison | Avg Overhead | Median Overhead |\n|---|---|---|\n| Qwen beam k=4 vs greedy | **1.69x** | **1.35x** |\n| Llama beam k=4 vs greedy | 0.98x (comparable) | 1.06x |\n\n**Qwen DocRED** shows the clearest beam overhead: 1.69x average, 1.35x median. The difference between mean and median indicates beam search has high-variance tail latency (max 129.3s vs greedy max 33.1s).\n\n**Llama DocRED** shows negligible overhead on average, but the greedy run has a high-variance tail (max 66.4s) that inflates its mean.\n\n---\n\n## Beam Width Scaling (Qwen SciERC, 551 docs)\n\n| k | Per-doc Avg (s) | Relative to k=2 |\n|---|-----------------|------------------|\n| 2 | 5.390 | 1.00x |\n| 4 | 5.915 | 1.10x |\n| 8 | 7.061 | 1.31x |\n\nBeam width scaling is sub-linear: doubling k from 2 to 4 adds ~10% latency; from 4 to 8 adds ~19%.\n\n---\n\n## Fine-tuned vs Zero-shot Beam (Qwen SciERC, k=4)\n\n| Setting | Per-doc Avg (s) | Per-doc Median (s) |\n|---|---|---|\n| Zero-shot beam k=4 | 5.915 | 5.506 |\n| Fine-tuned beam k=4 | 3.705 | 3.324 |\n| Speedup | **1.60x** | **1.66x** |\n\nFine-tuning reduces beam search latency by ~37%, likely because the model produces more confident token distributions, leading to earlier convergence.\n\n---\n\n## Summary for Paper\n\n**Recommended numbers to cite (most reliable comparisons):**\n\n1. **Qwen DocRED beam k=4 overhead**: 1.69x avg / 1.35x median over greedy (matched 50-doc subset, same GPU, close temporal proximity)\n2. **Beam width scaling** (SciERC): k=2 to k=4 adds 10%, k=4 to k=8 adds 19% (sub-linear)\n3. **FT speedup**: Fine-tuned beam k=4 is 1.6x faster than zero-shot beam k=4\n\n**Key finding**: Beam search (k=4) adds moderate latency overhead (~1.3-1.7x on document-level tasks), scaling sub-linearly with beam width. The overhead is more pronounced on longer documents (DocRED) where each beam candidate generates substantially more tokens.\n\n**Caveats**:\n- SciERC greedy vs beam comparison is confounded by different run dates; the matched DocRED 50-doc comparison is the most controlled\n- Llama DocRED shows near-zero overhead, possibly due to different tokenization efficiency or variance in greedy tail latency\n- For a clean SciERC comparison, a fresh greedy run on the same GPU session as beam runs would be ideal\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T12:10:01.468714+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r4_n3_runtime_profiling.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T12:10:01.468863+00:00_

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
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
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

_source line 38 · 2026-05-18T12:10:01.468990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T12:10:01.469124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T12:10:01.469246+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T12:10:01.469414+00:00_

Report written to `artifacts/r4_n3_runtime_profiling.md`.

## 结果总结

### 最可靠的对比: Qwen DocRED (matched 50-doc subset, 同 GPU 近时运行)

| | Greedy | Beam k=4 | Overhead |
|---|---|---|---|
| Per-doc avg | 18.5s | 31.4s | **1.69x** |
| Per-doc median | 18.1s | 24.5s | **1.35x** |

Beam 的 tail latency 显著更高 (max 129s vs 33s)。

### Beam width scaling (Qwen SciERC, 551 docs)

| k | Avg (s) | 相对 k=2 |
|---|---|---|
| 2 | 5.39 | 1.00x |
| 4 | 5.92 | 1.10x |
| 8 | 7.06 | 1.31x |

**Sub-linear scaling**: k 翻倍只增加 10-19% latency。

### Fine-tuned beam 加速

FT beam k=4 比 ZS beam k=4 快 **1.6x** (avg 3.7s vs 5.9s)，因为 FT 模型 token 分布更集中，beam 更早收敛。

### Caveats

- SciERC greedy baseline 跑的时间比 beam 早 2-3 天，不是严格控制变量对比 (Qwen greedy 反而比 beam k=4 慢，不合理)
- Llama DocRED beam vs greedy 几乎无差异 (0.98x)，可能因 greedy tail variance 大
- **建议**: 论文引用 Qwen DocRED 的 1.69x/1.35x 作为 beam overhead；如需 clean SciERC 数据，需重跑 greedy baseline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r4n3_beam_runtime_profiling_20260518T120631"
}
```

</details>

---
