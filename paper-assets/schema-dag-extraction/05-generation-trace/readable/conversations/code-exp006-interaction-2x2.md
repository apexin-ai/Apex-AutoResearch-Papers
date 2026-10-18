# code exp006 interaction 2x2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_code_exp006_interaction_2x2_20260515T173024.jsonl`
- **Structured JSON:** [`77150e7bda831b343ac8.json`](../../sessions/77/77150e7bda831b343ac8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-15T17:37:32.950306+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:37:32.950758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:37:32.951052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/run_experiment.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/run_experiment.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T17:37:32.951240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -la /root/schema-dag-extraction/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T17:37:32.951580+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Main experiment orchestrator.\\n\\nv2 changes (2026-05-14): Added --prompt_version and --eval_mode support.\\n\\nModes:\\n  dry_run: 100 test samples, count=6, low/high/1 random — pipeline verification\\n  exp1: Count Baseline — solo baseline (count=1) + random batches at 2/6/12/22/44/66 types, 5 random each\\n  exp2: Confusability Controlled — count=6,12, low/high BCS + 25 random each\\nDependencies: all src/ modules, vllm\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Schema-DAG Extraction MVP Experiment\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Path to model directory\\\")\\n    parser.add_argument(\\\"--model_name\\\", default=None,\\n                        help=\\\"Short model name for output files (default: derived from model_path)\\\")\\n    parser.add_argument(\\\"--gpu_memory_utilization\\\", type=float, default=0.95,\\n                        help=\\\"vLLM GPU memory utilization (default: 0.95)\\\")\\n    parser.add_argument(\\\"--data_dir\\\", default=\\\"/root/schema-dag-extraction/data\\\", help=\\\"Data directory\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"/root/schema-dag-extraction/artifacts\\\", help=\\\"Output directory\\\")\\n    parser.add_argument(\\\"--dataset\\\", choices=[\\\"fewnerd\\\", \\\"maven\\\", \\\"fewrel\\\"], default=\\\"fewnerd\\\",\\n                        help=\\\"Dataset: fewnerd (NER), maven (event detection), or fewrel (RE)\\\")\\n    parser.add_argument(\\\"--data_path\\\", default=None, help=\\\"Custom data path (parquet for maven)\\\")\\n    parser.add_argument(\\\"--types_file\\\", required=True, help=\\\"Type definitions JSON path\\\")\\n    parser.add_argument(\\\"--embeddings_path\\\", default=N
…[truncated 7205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:37:32.951857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 88\\ndrwxr-xr-x  2 root root 4096 May 16 01:21 .\\ndrwxr-xr-x 10 root root 4096 May 16 01:21 ..\\n-rwxr-xr-x  1 root root  937 May 16 00:18 auto_start_exp012_awq.sh\\n-rw-r--r--  1 root root 4689 May 15 03:41 compute_e5_embeddings.py\\n-rw-r--r--  1 root root 2344 May 15 19:40 compute_fewrel_qwen3_embeddings.py\\n-rw-r--r--  1 root root 1985 May 15 19:02 compute_maven_minilm.py\\n-rw-r--r--  1 root root 2412 May 15 13:33 compute_maven_qwen3_embeddings.py\\n-rw-r--r--  1 root root 6226 May 16 00:56 diagnose_llama8b_freeform.py\\n-rw-r--r--  1 root root 1883 May 16 00:56 patch_chat_template.py\\n-rwxr-xr-x  1 root root 1091 May 15 15:44 run_exp008.sh\\n-rwxr-xr-x  1 root root  973 May 15 23:46 run_exp012_llama.sh\\n-rwxr-xr-x  1 root root  935 May 16 00:21 run_exp012_llama8b.sh\\n-rwxr-xr-x  1 root root 1639 May 16 01:21 run_exp012_llama8b_r2.sh\\n-rwxr-xr-x  1 root root  954 May 16 00:25 run_exp012_llama_8b.sh\\n-rwxr-xr-x  1 root root  861 May 16 00:11 run_exp012_llama_awq.sh\\n-rwxr-xr-x  1 root root  624 May 16 00:10 run_fewrel_40rel.sh\\n-rwxr-xr-x  1 root root 1307 May 15 18:59 run_sdgd_maven_minilm.sh\\n-rwxr-xr-x  1 root root 1808 May 15 20:11 run_sdgd_v2_fewnerd.sh\\n-rwxr-xr-x  1 root root 1844 May 15 20:11 run_sdgd_v2_maven_minilm.sh\\n-rwxr-xr-x  1 root root  268 May 15 18:27 submit_exp012.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:37:32.952078+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "find /root/schema-dag-extraction -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:37:32.952333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-ACE/bert_crf.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-ACE/crf.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-ACE/run_ACE.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-ACE/utils_ACE.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-MAVEN/bert_crf.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-MAVEN/crf.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-MAVEN/run_maven.py\\n/root/schema-dag-extraction/data/maven/baselines/BERT+CRF/BERT-CRF-MAVEN/utils_maven.py\\n/root/schema-dag-extraction/data/maven/baselines/DMBERT/get_submission.py\\n/root/schema-dag-extraction/data/maven/baselines/DMBERT/model.py\\n/root/schema-dag-extraction/data/maven/baselines/DMBERT/run_ee.py\\n/root/schema-dag-extraction/data/maven/baselines/DMBERT/utils_ee.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/clear.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/formatter/BilstmFormatter.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/formatter/CrfFormatter.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/formatter/DmcnnFormatter.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/formatter/__init__.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/main.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/model/Bilstm.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/model/Crf.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/model/Dmcnn.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/model/__init__.py\\n/root/schema-dag-extraction/data/maven/baselines/DMCNN_BiLSTM_(CRF)/model/layers/crf.py\\n/root/s
…[truncated 4460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:37:32.952546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -la /root/schema-dag-extraction/data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:37:32.952740+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 2404\\ndrwxr-xr-x  7 root root   4096 May 15 13:12 .\\ndrwxr-xr-x 10 root root   4096 May 16 01:21 ..\\n-rw-r--r--  1 root root   6996 May 15 00:42 few_nerd_type_stats.json\\ndrwxr-xr-x  2 root root     62 May 15 12:35 fewrel\\ndrwxr-xr-x  2 root root     58 May 15 12:37 fewrel_parquet\\n-rw-r--r--  1 root root  91892 May 15 02:14 heatmap.pdf\\n-rw-r--r--  1 root root  83463 May 15 03:44 heatmap_e5_a_name_def.pdf\\n-rw-r--r--  1 root root  84151 May 15 03:44 heatmap_e5_b_name_only.pdf\\ndrwxr-xr-x  4 root root   4096 May 15 11:31 maven\\ndrwxr-xr-x  2 root root     35 May 15 11:34 maven_parquet\\n-rw-r--r--  1 root root 758702 May 15 13:12 maven_scs_matrix.json\\n-rw-r--r--  1 root root 118312 May 15 13:12 maven_sim_matrix.pt\\ndrwxr-xr-x  2 root root     89 May 15 00:41 parquet\\n-rw-r--r--  1 root root  20926 May 15 02:14 sim_matrix.pt\\n-rw-r--r--  1 root root 684417 May 15 02:13 type_embeddings.pt\\n-rw-r--r--  1 root root 579659 May 15 03:44 type_embeddings_e5.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:37:32.952962+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -la /root/schema-dag-extraction/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:37:32.953192+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 87792\\ndrwxr-xr-x 16 root root     4096 May 16 00:26 .\\ndrwxr-xr-x 10 root root     4096 May 16 01:21 ..\\n-rw-r--r--  1 root root      821 May 15 03:26 batch_config_dry_run.json\\n-rw-r--r--  1 root root    32311 May 15 10:54 batch_config_exp1.json\\n-rw-r--r--  1 root root    19664 May 15 12:13 batch_config_exp2.json\\n-rw-r--r--  1 root root      710 May 15 14:01 batch_config_maven_dry_run.json\\n-rw-r--r--  1 root root     2231 May 15 23:15 bootstrap_ci.json\\n-rw-r--r--  1 root root    17694 May 15 16:03 embedding_ablation_fewnerd.json\\n-rw-r--r--  1 root root     2185 May 15 03:31 eval_dry_run.json\\n-rw-r--r--  1 root root    29774 May 15 12:13 eval_exp1.json\\n-rw-r--r--  1 root root    18069 May 15 13:02 eval_exp2.json\\n-rw-r--r--  1 root root      970 May 15 14:03 eval_maven_dry_run.json\\ndrwxr-xr-x  2 root root     4096 May 15 15:17 exp004\\n-rw-r--r--  1 root root   829417 May 15 15:06 exp004_exp1.log\\n-rw-r--r--  1 root root    86554 May 15 15:15 exp004_exp2.log\\ndrwxr-xr-x  2 root root      119 May 15 21:45 exp007\\ndrwxr-xr-x  2 root root     4096 May 15 20:07 exp008\\ndrwxr-xr-x  2 root root       40 May 15 15:44 exp008_dryrun\\ndrwxr-xr-x  2 root root     4096 May 15 18:15 exp008_dryrun2\\n-rw-r--r--  1 root root     8315 May 15 18:06 exp008_run.log\\n-rw-r--r--  1 root root   661588 May 15 19:16 exp008_run2.log\\ndrwxr-xr-x  2 root root     4096 May 15 23:11 exp008_v2\\ndrwxr-xr-x  2 root root     4096 May 16 00:45 exp012\\ndrwxr-xr-x  2 root root     4096 May 16 00:24 exp012_dryrun\\ndrwxr-xr-x  2 root root       74 May 16 00:26 exp012_llama_8b\\n-rw-r--r--  1 root root      797 May 15 23:25 exp015_scs_validation.json\\ndrwxr-xr-x  2 root root      174 May 15 19:03 exp_maven_minilm\\n-rw-r--r--  1 root root   122805 May 15 16:03 fewnerd_bcs_matrix_minilm.pt\\ndrwxr-xr-x  2 root root      110 May 16 00:11 fewrel_40rel\\n-rw-r--r--  1 root root    48553 May 15 23:10 fewrel_80rel_er
…[truncated 1413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:37:32.953444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/select_type_batches.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/select_type_batches.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T17:37:32.953734+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Type batch selection strategies based on BCS.\\n\\nInput: Similarity matrix .pt\\nOutput: JSON with low/high/random type batches and their BCS scores\\nDependencies: torch\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport random\\nfrom pathlib import Path\\n\\nimport torch\\n\\nfrom compute_bcs import compute_bcs\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef select_low_bcs(n: int, sim_matrix: torch.Tensor, type_names: list, type_to_idx: dict) -> list:\\n    \\\"\\\"\\\"Greedily select n types to minimize batch BCS.\\n\\n    Start from the pair with lowest similarity, then add the type whose\\n    max similarity to any already-selected type is lowest (consistent with BCS = max).\\n    \\\"\\\"\\\"\\n    if n > len(type_names):\\n        return list(type_names)\\n\\n    num_types = len(type_names)\\n\\n    # Find the pair with minimum similarity\\n    min_val = float(\\\"inf\\\")\\n    min_i, min_j = 0, 1\\n    for i in range(num_types):\\n        for j in range(i + 1, num_types):\\n            val = sim_matrix[i, j].item()\\n            if val < min_val:\\n                min_val = val\\n                min_i, min_j = i, j\\n\\n    selected_indices = [min_i, min_j]\\n\\n    while len(selected_indices) < n:\\n        best_idx = -1\\n        best_max_sim = float(\\\"inf\\\")\\n        for cand in range(num_types):\\n            if cand in selected_indices:\\n                continue\\n            max_sim = max(sim_matrix[cand, s].item() for s in selected_indices)\\n            if max_sim < best_max_sim:\\n                best_max_sim = max_sim\\n                best_idx = cand\\n        selected_indices.append(best_idx)\\n\\n    return [type_names[i] for i in selected_indices]\\n\\n\\ndef select_high_bcs(n: int, sim_matrix: torch.Tensor, type_names: list, type_to_idx: dict) -> list:\\n    \\\"\\\"\\\"Greedily select n types to maximize batch BCS.\\n\\n    Start from the p
…[truncated 4327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:37:32.953984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/compute_bcs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/compute_bcs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:37:32.954255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute pairwise cosine similarity matrix and BCS scores.\\n\\nInput: Type embeddings .pt file\\nOutput: Similarity matrix .pt, heatmap PDF\\nDependencies: torch, matplotlib, seaborn\\n\\\"\\\"\\\"\\nimport argparse\\nimport logging\\nfrom pathlib import Path\\n\\nimport torch\\nimport torch.nn.functional as F\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_embeddings(path: str) -> dict:\\n    \\\"\\\"\\\"Load {type_name: tensor} from .pt file.\\\"\\\"\\\"\\n    return torch.load(path, map_location=\\\"cpu\\\", weights_only=True)\\n\\n\\ndef compute_similarity_matrix(embeddings: dict) -> tuple:\\n    \\\"\\\"\\\"Compute pairwise cosine similarity matrix.\\n\\n    Returns:\\n        (sim_matrix, type_names, type_to_idx) where sim_matrix is N×N tensor.\\n    \\\"\\\"\\\"\\n    type_names = sorted(embeddings.keys())\\n    type_to_idx = {name: i for i, name in enumerate(type_names)}\\n\\n    vecs = torch.stack([embeddings[name] for name in type_names]).float()\\n    vecs = F.normalize(vecs, dim=1)\\n    sim_matrix = vecs @ vecs.T  # N×N cosine similarity\\n\\n    return sim_matrix, type_names, type_to_idx\\n\\n\\ndef compute_bcs(type_subset: list, sim_matrix: torch.Tensor, type_to_idx: dict) -> float:\\n    \\\"\\\"\\\"Compute Batch Confusability Score for a subset of types.\\n\\n    BCS = max pairwise cosine similarity (IDEA_BRIEF definition).\\n\\n    Args:\\n        type_subset: List of type names in the batch.\\n        sim_matrix: Full N×N similarity matrix.\\n        type_to_idx: Mapping from type name to matrix index.\\n\\n    Returns:\\n        BCS value (float).\\n    \\\"\\\"\\\"\\n    if len(type_subset) < 2:\\n        return 0.0\\n\\n    indices = [type_to_idx[t] for t in type_subset]\\n    max_sim = float(\\\"-inf\\\")\\n    for i in range(len(indices)):\\n        for j in range(i + 1, len(indices)):\\n            val = sim_matrix[indices[i], indices[j]].item()\\n            if v
…[truncated 2320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:37:32.954484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/run_extraction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/run_extraction.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T17:37:32.954905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Constrained JSON decoding NER extraction using vLLM.\\n\\nv2 changes (2026-05-14): Added prompt_version support (v1=with offsets, v2=text+type only).\\n\\nInput: Few-NERD test data, type batch config, LLM model\\nOutput: JSON with extraction results per (sample, batch) pair\\nDependencies: vllm, transformers\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport time\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Set\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\n# --- v1: original schema/prompt with start/end offsets ---\\n\\ndef build_json_schema_v1(batch_types: list) -> dict:\\n    \\\"\\\"\\\"Build JSON schema with start/end offsets (v1).\\\"\\\"\\\"\\n    return {\\n        \\\"type\\\": \\\"array\\\",\\n        \\\"items\\\": {\\n            \\\"type\\\": \\\"object\\\",\\n            \\\"properties\\\": {\\n                \\\"text\\\": {\\\"type\\\": \\\"string\\\"},\\n                \\\"type\\\": {\\\"type\\\": \\\"string\\\", \\\"enum\\\": sorted(batch_types)},\\n                \\\"start\\\": {\\\"type\\\": \\\"integer\\\"},\\n                \\\"end\\\": {\\\"type\\\": \\\"integer\\\"},\\n            },\\n            \\\"required\\\": [\\\"text\\\", \\\"type\\\", \\\"start\\\", \\\"end\\\"],\\n        },\\n    }\\n\\n\\ndef build_prompt_v1(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str:\\n    \\\"\\\"\\\"Build NER extraction prompt requesting start/end offsets (v1).\\\"\\\"\\\"\\n    type_desc_lines = []\\n    for t in sorted(type_subset):\\n        defn = type_definitions.get(t, t)\\n        type_desc_lines.append(f\\\"- {t}: {defn}\\\")\\n    type_desc = \\\"\\\\n\\\".join(type_desc_lines)\\n\\n    return (\\n        f\\\"Extract all named entities from the following text. \\\"\\n        f\\\"Only extract entities of the following types:\\\\n{type_desc}\\\\n\\\\n\\\"\\n        f\\\"Text: {input_text}\\\\n\\
…[truncated 7491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:37:32.955157+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T17:37:32.955544+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Evaluate NER extraction results against ground truth.\\n\\nv2 changes (2026-05-14): Added text_match eval mode (no offset dependency).\\n\\nInput: Extraction results JSON, Few-NERD ground truth\\nOutput: Per-batch metrics JSON (F1, precision, recall, BCS)\\nDependencies: few_nerd_utils\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Set\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef load_predictions(path: str) -> List[Dict]:\\n    with open(path, \\\"r\\\") as f:\\n        return json.load(f)\\n\\n\\ndef _exact_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:\\n    \\\"\\\"\\\"Exact span match: start, end, and type must all match.\\\"\\\"\\\"\\n    return (pred.get(\\\"start\\\") == gold[\\\"start\\\"]\\n            and pred.get(\\\"end\\\") == gold[\\\"end\\\"]\\n            and pred.get(\\\"type\\\") == gold[\\\"type\\\"])\\n\\n\\ndef _relaxed_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:\\n    \\\"\\\"\\\"Relaxed match: type must match and text spans must overlap.\\\"\\\"\\\"\\n    if pred.get(\\\"type\\\") != gold[\\\"type\\\"]:\\n        return False\\n    p_start, p_end = pred.get(\\\"start\\\", -1), pred.get(\\\"end\\\", -1)\\n    g_start, g_end = gold[\\\"start\\\"], gold[\\\"end\\\"]\\n    return p_start < g_end and p_end > g_start\\n\\n\\ndef _text_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:\\n    \\\"\\\"\\\"Text-based match: type must match, texts must overlap via substring.\\n\\n    Validates pred text appears in source text (not hallucinated).\\n    Match if either text contains the other (handles boundary differences).\\n    \\\"\\\"\\\"\\n    if pred.get(\\\"type\\\") != gold[\\\"type\\\"]:\\n        return False\\n    pred_text = pred.get(\\\"text\\\", \\\"\\\").strip()\\n    gold_text = gold.get(\\\"text\\\", \\\"\\\").strip()\\n    if
…[truncated 7405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:37:32.955776+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/few_nerd_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/few_nerd_utils.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T17:37:32.956100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Few-NERD data loading and preprocessing utilities.\\n\\nInput: Few-NERD dataset (token-level annotation, 66 fine-grained entity types)\\n       Loaded from local parquet files; falls back to HF Hub if parquet missing.\\nOutput: List of {\\\"text\\\": str, \\\"entities\\\": [{\\\"text\\\": str, \\\"type\\\": str, \\\"start\\\": int, \\\"end\\\": int}]}\\nDependencies: datasets\\n\\\"\\\"\\\"\\nimport json\\nimport logging\\nimport os\\nfrom typing import Dict, List, Optional, Set\\n\\nfrom datasets import load_dataset\\n\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_DATA_DIR = \\\"/root/schema-dag-extraction/data/parquet\\\"\\n\\n\\ndef load_few_nerd(\\n    split: str = \\\"test\\\",\\n    max_samples: Optional[int] = None,\\n    data_dir: str = DEFAULT_DATA_DIR,\\n) -> List[Dict]:\\n    \\\"\\\"\\\"Load Few-NERD and convert token-level tags to span-level entities.\\n\\n    Args:\\n        split: Dataset split (\\\"train\\\", \\\"validation\\\", \\\"test\\\").\\n        max_samples: If set, only return first N samples.\\n        data_dir: Directory containing {split}.parquet files.\\n\\n    Returns:\\n        List of dicts with \\\"text\\\" (reconstructed sentence) and \\\"entities\\\" (span-level).\\n    \\\"\\\"\\\"\\n    parquet_path = os.path.join(data_dir, f\\\"{split}.parquet\\\")\\n    if os.path.exists(parquet_path):\\n        logger.info(\\\"Loading Few-NERD from local parquet: %s\\\", parquet_path)\\n        ds = load_dataset(\\\"parquet\\\", data_files=parquet_path, split=\\\"train\\\")\\n    else:\\n        logger.info(\\\"Local parquet not found, falling back to HF Hub\\\")\\n        ds = load_dataset(\\\"DFKI-SLT/few-nerd\\\", \\\"supervised\\\", split=split, trust_remote_code=True)\\n\\n    tag_names = ds.features[\\\"fine_ner_tags\\\"].feature.names\\n\\n    samples = []\\n    for i, example in enumerate(ds):\\n        if max_samples is not None and i >= max_samples:\\n         
…[truncated 4279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:37:32.956353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/autodl-tmp/models/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls /root/autodl-tmp/models/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:37:32.956538+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama-3.1-8b-instruct\\nllama-3.1-8b-instruct-ms\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:37:32.956709+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/scripts/run_exp008.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/scripts/run_exp008.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:37:32.956941+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nCOMMON=\\\"--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp008\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: SDGD-zero =====\\\"\\npython3 src/run_sdgd_experiment.py --mode sdgd_zero $COMMON\\necho \\\"===== [$(date)] SDGD-zero done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: single_pass =====\\\"\\npython3 src/run_sdgd_experiment.py --mode single_pass $COMMON\\necho \\\"===== [$(date)] single_pass done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: random_batch =====\\\"\\npython3 src/run_sdgd_experiment.py --mode random_batch $COMMON\\necho \\\"===== [$(date)] random_batch done =====\\\"\\n\\necho \\\"===== [$(date)] Starting exp-008: per_type =====\\\"\\npython3 src/run_sdgd_experiment.py --mode per_type $COMMON\\necho \\\"===== [$(date)] per_type done =====\\\"\\n\\necho \\\"===== [$(date)] All exp-008 modes completed =====\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:37:32.957145+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_fewnerd.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/scripts/run_sdgd_v2_fewnerd.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T17:37:32.957379+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh\\nconda activate base\\ncd /root/schema-dag-extraction\\n\\nTYPES_FILE=configs/few_nerd_types.json\\nSIM_MATRIX=artifacts/sim_matrix.pt\\nMODEL_PATH=/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\nOUTPUT_DIR=artifacts/exp008_v2\\nMAX_SAMPLES=1000\\nTASK=ner\\nMIN_BATCH_SIZE=8\\nMERGE_STRATEGY=confidence\\nCONFIDENCE_THRESHOLD=-1.0\\n\\nmkdir -p ${OUTPUT_DIR}\\n\\necho \\\"===== [$(date)] SDGD-zero v2 — FewNERD =====\\\"\\necho \\\"  min_batch_size=${MIN_BATCH_SIZE}, merge=${MERGE_STRATEGY}, threshold=${CONFIDENCE_THRESHOLD}\\\"\\n\\n# ========== Stage 1: CPU Decomposition ==========\\necho \\\"===== [$(date)] Stage 1: CPU Decomposition =====\\\"\\n\\nfor MODE in sdgd_zero single_pass random_batch per_type; do\\n  EXTRA_ARGS=\\\"\\\"\\n  if [ \\\"${MODE}\\\" = \\\"sdgd_zero\\\" ]; then\\n    EXTRA_ARGS=\\\"--min_batch_size ${MIN_BATCH_SIZE}\\\"\\n  fi\\n  echo \\\"  Decomposing: ${MODE} ${EXTRA_ARGS}\\\"\\n  python3 src/sdgd_decompose_cpu.py \\\\\\n    --mode ${MODE} \\\\\\n    --types_file ${TYPES_FILE} \\\\\\n    --sim_matrix_path ${SIM_MATRIX} \\\\\\n    --output ${OUTPUT_DIR}/decomposition_${MODE}.json \\\\\\n    ${EXTRA_ARGS}\\ndone\\n\\n# ========== Stage 2: GPU Extraction ==========\\necho \\\"===== [$(date)] Stage 2: GPU Extraction (confidence merge) =====\\\"\\n\\npython3 src/sdgd_extract_gpu.py \\\\\\n  --decompositions \\\\\\n    ${OUTPUT_DIR}/decomposition_sdgd_zero.json \\\\\\n    ${OUTPUT_DIR}/decomposition_single_pass.json \\\\\\n    ${OUTPUT_DIR}/decomposition_random_batch.json \\\\\\n    ${OUTPUT_DIR}/decomposition_per_type.json \\\\\\n  --model_path ${MODEL_PATH} \\\\\\n  --types_file ${TYPES_FILE} \\\\\\n  --dataset fewnerd \\\\\\n  --prompt_version v2 \\\\\\n  --max_samples ${MAX_SAMPLES} \\\\\\n  --output_dir ${OUTPUT_DIR} \\\\\\n  --max_model_len 4096 \\\\\\n  --task ${TASK} \\\\\\n  --merge_strategy ${MERGE_STRATEGY} \\\\\\n
…[truncated 204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:37:32.957614+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction/data -name \"*.json\" -maxdepth 1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "find /root/schema-dag-extraction/data -name \"*.json\" -maxdepth 1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T17:37:32.957807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/data/few_nerd_type_stats.json\\n/root/schema-dag-extraction/data/maven_scs_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T17:37:32.958031+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /root/schema-dag-extraction/configs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls /root/schema-dag-extraction/configs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T17:37:32.958221+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"few_nerd_types.json\\nfewrel_relation_types.json\\nmaven_event_types.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T17:37:32.958396+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True); print('keys:', list(d.keys())); print('shape:', d['sim_matrix'].shape); print('num types:', len(d['type_names'])); print('types:', d['type_names'][:10])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True); print('keys:', list(d.keys())); print('shape:', d['sim_matrix'].shape); print('num types:', len(d['type_names'])); print('types:', d['type_names'][:10])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T17:37:32.958573+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T17:37:32.958746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -30 /root/schema-dag-extraction/configs/few_nerd_types.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -30 /root/schema-dag-extraction/configs/few_nerd_types.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T17:37:32.959010+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"person-actor\\\": \\\"A person who performs in movies, TV shows, theater, or other entertainment productions.\\\",\\n  \\\"person-artist/author\\\": \\\"A person who creates artistic or literary works, including writers, painters, sculptors, musicians as creators, and other creative professionals.\\\",\\n  \\\"person-athlete\\\": \\\"A person who competes in sports or athletic events, whether professional or amateur.\\\",\\n  \\\"person-director\\\": \\\"A person who directs movies, TV shows, theater productions, or other media content.\\\",\\n  \\\"person-other\\\": \\\"A person who does not fit into the other specific person subcategories, such as historical figures, activists, or ordinary individuals mentioned by name.\\\",\\n  \\\"person-politician\\\": \\\"A person who holds or campaigns for political office, or is primarily known for political activities.\\\",\\n  \\\"person-scholar\\\": \\\"A person primarily known for academic or scientific work, including professors, researchers, and intellectuals.\\\",\\n  \\\"person-soldier\\\": \\\"A person who serves or served in a military or armed force, including officers, generals, and enlisted personnel.\\\",\\n  \\\"organization-company\\\": \\\"A commercial business entity, corporation, or firm engaged in trade, manufacturing, or services for profit.\\\",\\n  \\\"organization-education\\\": \\\"An educational institution such as a university, college, school, or research institute.\\\",\\n  \\\"organization-government/governmentagency\\\": \\\"A government body, department, ministry, or agency that exercises governmental authority or provides public services.\\\",\\n  \\\"organization-media/newspaper\\\": \\\"A media organization, news outlet, newspaper, magazine, broadcasting network, or publishing house.\\\",\\n  \\\"organization-other\\\": \\\"An organization that does not fit into the other specific organization subcategories, such as NGOs, fou
…[truncated 2378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T17:37:32.959238+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True); print('shape:', d['sim_matrix'].shape); print('types:', d['type_names'])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True); print('shape:', d['sim_matrix'].shape); print('types:', d['type_names'])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T17:37:32.959436+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T17:37:32.959610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "wc -l /root/schema-dag-extraction/configs/few_nerd_types.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "wc -l /root/schema-dag-extraction/configs/few_nerd_types.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T17:37:32.959781+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"68 /root/schema-dag-extraction/configs/few_nerd_types.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T17:37:32.959995+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True)\nprint('shape:', d['sim_matrix'].shape)\nprint('num_types:', len(d['type_names']))\nprint('types:', d['type_names'])\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch\nd = torch.load('/root/schema-dag-extraction/artifacts/sim_matrix.pt', map_location='cpu', weights_only=True)\nprint('shape:', d['sim_matrix'].shape)\nprint('num_types:', len(d['type_names']))\nprint('types:', d['type_names'])\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T17:37:32.960200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"shape: torch.Size([66, 66])\\nnum_types: 66\\ntypes: ['art-broadcastprogram', 'art-film', 'art-music', 'art-other', 'art-painting', 'art-writtenart', 'building-airport', 'building-hospital', 'building-hotel', 'building-library', 'building-other', 'building-restaurant', 'building-sportsfacility', 'building-theater', 'event-attack/battle/war/militaryconflict', 'event-disaster', 'event-election', 'event-other', 'event-protest', 'event-sportsevent', 'location-GPE', 'location-bodiesofwater', 'location-island', 'location-mountain', 'location-other', 'location-park', 'location-road/railway/highway/transit', 'organization-company', 'organization-education', 'organization-government/governmentagency', 'organization-media/newspaper', 'organization-other', 'organization-politicalparty', 'organization-religion', 'organization-showorganization', 'organization-sportsleague', 'organization-sportsteam', 'other-astronomything', 'other-award', 'other-biologything', 'other-chemicalthing', 'other-currency', 'other-disease', 'other-educationaldegree', 'other-god', 'other-language', 'other-law', 'other-livingthing', 'other-medical', 'person-actor', 'person-artist/author', 'person-athlete', 'person-director', 'person-other', 'person-politician', 'person-scholar', 'person-soldier', 'product-airplane', 'product-car', 'product-food', 'product-game', 'product-other', 'product-ship', 'product-software', 'product-train', 'product-weapon']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T17:37:32.960675+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat > /root/schema-dag-extraction/scripts/run_exp006_interaction.py << 'PYTHON_EOF'\n#!/usr/bin/env python3\n\"\"\"Exp-006: 2×2 Factorial — Count × Confusability Interaction on NER.\n\nTests whether count × BCS effects are additive or multiplicative.\n4 conditions (low/high count × low/high BCS), 10 batches each.\nHypothesis: if multiplicative, high_count + high_BCS degradation exceeds\nthe sum of the two main effects.\n\nInput:\n  - Few-NERD test data (parquet in data/parquet/)\n  - Qwen3-32B-FP8 model\n  - Pre-computed cosine similarity matrix (sim_matrix.pt)\nOutput (all in artifacts/exp006/):\n  - batch_config.json — 4-cell batch definitions with BCS scores\n  - predictions.json — raw model extraction outputs\n  - eval_results.json — per-batch text_match F1/P/R metrics\n  - interaction_analysis.json — cell means, main effects, interaction term\nDependencies: src/ modules (run_extraction, evaluate, compute_bcs, few_nerd_utils), vllm, torch\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport random\nimport sys\nimport time\nfrom pathlib import Path\n\nlogger = logging.getLogger(__name__)\n\nPROJECT_ROOT = Path(__file__).resolve().parent.parent\n\n\ndef build_factorial_batches(sim_matrix, type_names, type_to_idx,\n                            low_count, high_count, batches_per_cell,\n                            pool_size, seed):\n    \"\"\"Build 2×2 factorial batch config by selecting BCS extremes from random pools.\n\n    For each count level, generates a large random pool of type batches,\n    sorts by BCS, and picks the lowest and highest N as the two BCS conditions.\n\n    Args:\n        sim_matrix: N×N cosine similarity tensor.\n        type_names: list of type name strings (active types only).\n        type_to_idx: dict mapping type name to sim_matrix row/col index.\n        low_count: number of types for the low-count condition.\n        high_count: number of types for the high-count condition.\n        batches_per_cell: how many batches per factorial cell.\n        pool_size: random batches to sample per count level before selecting extremes.\n        seed: random seed.\n\n    Returns:\n        batch_config dict with keys \"low_count\"/\"high_count\", each containing\n        \"low_bcs\" and \"high_bcs\" lists of {\"types\": [...], \"bcs\": float}.\n    \"\"\"\n    from compute_bcs import compute_bcs\n\n    batch_config = {}\n\n    for count, count_label in [(low_count, \"low_count\"), (high_count, \"high_count\")]:\n        rng = random.Random(seed + count)\n        pool = []\n        seen = set()\n        max_attempts = pool_size * 20\n\n        for _ in range(max_attempts):\n            if len(pool) >= pool_size:\n                break\n            chosen = tuple(sorted(rng.sample(type_names, count)))\n            if chosen in seen:\n                continue\n            seen.add(chosen)\n            bcs = compute_bcs(list(chosen), sim_matrix, type_to_idx)\n            pool.append({\"types\": list(chosen), \"bcs\": bcs})\n\n        pool.sort(key=lambda x: x[\"bcs\"])\n\n        low_bcs_batches = pool[:batches_per_cell]\n        high_bcs_batches = pool[-batches_per_cell:]\n\n        logger.info(\"  %s (count=%d): pool=%d, low_bcs=[%.4f, %.4f], high_bcs=[%.4f, %.4f]\",\n                     count_label, count, len(pool),\n                     low_bcs_batches[0][\"bcs\"], low_bcs_batches[-1][\"bcs\"],\n                     high_bcs_batches[0][\"bcs\"], high_bcs_batches[-1][\"bcs\"])\n\n        batch_config[count_label] = {\n            \"low_bcs\": low_bcs_batches,\n            \"high_bcs\": high_bcs_batches,\n        }\n\n    return batch_config\n\n\ndef compute_interaction_analysis(eval_results):\n    \"\"\"Compute 2×2 factorial analysis from evaluation results.\n\n    Groups batch results into 4 cells, computes cell means for text_match F1,\n    derives main effects and interaction term, and runs a contrast significance test.\n\n    Args:\n        eval_results: dict from evaluate_all(), mapping batch_id -> metrics.\n\n    Returns:\n        dict with cell_means, main_effects, interaction (with optional t-test).\n    \"\"\"\n    cells = {\n        \"low_count/low_bcs\": [],\n        \"low_count/high_bcs\": [],\n        \"high_count/low_bcs\": [],\n        \"high_count/high_bcs\": [],\n    }\n\n    for bid, metrics in eval_results.items():\n        parts = bid.split(\"/\")\n        if len(parts) >= 2:\n            cell_key = f\"{parts[0]}/{parts[1]}\"\n            if cell_key in cells:\n                cells[cell_key].append(metrics)\n\n    cell_means = {}\n    for key, batch_metrics in cells.items():\n        if not batch_metrics:\n            logger.warning(\"No results for cell %s\", key)\n            continue\n        f1s = [m[\"text_match\"][\"f1\"] for m in batch_metrics]\n        precs = [m[\"text_match\"][\"precision\"] for m in batch_metrics]\n        recs = [m[\"text_match\"][\"recall\"] for m in batch_metrics]\n        bcs_vals = [m[\"bcs\"] for m in batch_metrics]\n        mean_f1 = sum(f1s) / len(f1s)\n        std_f1 = (sum((x - mean_f1) ** 2 for x in f1s) / len(f1s)) ** 0.5\n        cell_means[key] = {\n            \"mean_f1\": mean_f1,\n            \"std_f1\": std_f1,\n            \"se_f1\": std_f1 / len(f1s) ** 0.5 if len(f1s) > 1 else 0.0,\n            \"mean_precision\": sum(precs) / len(precs),\n            \"mean_recall\": sum(recs) / len(recs),\n            \"mean_bcs\": sum(bcs_vals) / len(bcs_vals),\n            \"n_batches\": len(f1s),\n            \"f1_values\": f1s,\n        }\n\n    def get_f1(key):\n        return cell_means.get(key, {}).get(\"mean_f1\", 0.0)\n\n    def get_se(key):\n        return cell_means.get(key, {}).get(\"se_f1\", 0.0)\n\n    ll = get_f1(\"low_count/low_bcs\")\n    lh = get_f1(\"low_count/high_bcs\")\n    hl = get_f1(\"high_count/low_bcs\")\n    hh = get_f1(\"high_count/high_bcs\")\n\n    # Main effects (marginal means difference)\n    count_effect = (hl + hh) / 2 - (ll + lh) / 2\n    bcs_effect = (lh + hh) / 2 - (ll + hl) / 2\n\n    # Interaction: does BCS effect differ between count levels?\n    bcs_effect_at_low_count = lh - ll\n    bcs_effect_at_high_count = hh - hl\n    interaction = bcs_effect_at_high_count - bcs_effect_at_low_count\n\n    # Interaction < 0 means BCS hurts MORE at high count (super-additive / multiplicative)\n    if interaction < -0.005:\n        interpretation = \"Super-additive (multiplicative): BCS effect amplified at high count\"\n    elif interaction > 0.005:\n        interpretation = \"Sub-additive: BCS effect attenuated at high count\"\n    else:\n        interpretation = \"Approximately additive: BCS and count effects are independent\"\n\n    analysis = {\n        \"cell_means\": cell_means,\n        \"cell_f1_summary\": {\n            \"low_count_low_bcs\": ll,\n            \"low_count_high_bcs\": lh,\n            \"high_count_low_bcs\": hl,\n            \"high_count_high_bcs\": hh,\n        },\n        \"main_effects\": {\n            \"count_effect\": count_effect,\n            \"bcs_effect\": bcs_effect,\n            \"count_effect_interpretation\": \"high_count marginal mean - low_count marginal mean\",\n            \"bcs_effect_interpretation\": \"high_bcs marginal mean - low_bcs marginal mean\",\n        },\n        \"interaction\": {\n            \"bcs_effect_at_low_count\": bcs_effect_at_low_count,\n            \"bcs_effect_at_high_count\": bcs_effect_at_high_count,\n            \"interaction_term\": interaction,\n            \"formula\": \"(HH - HL) - (LH - LL)\",\n            \"interpretation\": interpretation,\n        },\n    }\n\n    # Contrast significance test via SE propagation\n    se_ll = get_se(\"low_count/low_bcs\")\n    se_lh = get_se(\"low_count/high_bcs\")\n    se_hl = get_se(\"high_count/low_bcs\")\n    se_hh = get_se(\"high_count/high_bcs\")\n    se_interaction = (se_ll**2 + se_lh**2 + se_hl**2 + se_hh**2) ** 0.5\n\n    if se_interaction > 0:\n        z_stat = interaction / se_interaction\n        # Two-tailed p-value approximation (normal)\n        p_value = 2 * (1 - _norm_cdf(abs(z_stat)))\n        analysis[\"interaction\"][\"z_test\"] = {\n            \"z_statistic\": z_stat,\n            \"se_interaction\": se_interaction,\n            \"p_value\": p_value,\n            \"significant_005\": p_value < 0.05,\n        }\n\n    return analysis\n\n\ndef _norm_cdf(x):\n    \"\"\"Standard normal CDF approximation (no scipy dependency).\"\"\"\n    return 0.5 * (1 + math.erf(x / math.sqrt(2)))\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Exp-006: Count × Confusability 2×2 factorial interaction design\"\n    )\n    parser.add_argument(\"--model_path\", default=\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\",\n                        help=\"Path to Qwen3-32B-FP8 model\")\n    parser.add_argument(\"--types_file\", default=\"configs/few_nerd_types.json\",\n                        help=\"Type definitions JSON\")\n    parser.add_argument(\"--sim_matrix_path\", default=\"artifacts/sim_matrix.pt\",\n                        help=\"Pre-computed similarity matrix\")\n    parser.add_argument(\"--output_dir\", default=\"artifacts/exp006\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--max_samples\", type=int, default=1000,\n                        help=\"Max test samples from Few-NERD\")\n    parser.add_argument(\"--max_model_len\", type=int, default=4096,\n                        help=\"vLLM max model length\")\n    parser.add_argument(\"--gpu_memory_utilization\", type=float, default=0.95,\n                        help=\"vLLM GPU memory utilization\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--low_count\", type=int, default=6,\n                        help=\"Number of types in low-count condition\")\n    parser.add_argument(\"--high_count\", type=int, default=22,\n                        help=\"Number of types in high-count condition\")\n    parser.add_argument(\"--batches_per_cell\", type=int, default=10,\n                        help=\"Number of random batches per factorial cell\")\n    parser.add_argument(\"--pool_size\", type=int, default=500,\n                        help=\"Random pool size for selecting BCS extremes\")\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Build and validate batches only, skip model extraction\")\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\n    random.seed(args.seed)\n\n    sys.path.insert(0, str(PROJECT_ROOT / \"src\"))\n\n    # Suppress CUDA init during imports (vLLM must init CUDA itself)\n    orig_cuda = os.environ.get(\"CUDA_VISIBLE_DEVICES\")\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = \"\"\n\n    import torch\n    from few_nerd_utils import load_few_nerd, load_type_definitions, get_all_types\n    from compute_bcs import compute_bcs\n    from evaluate import evaluate_all\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # --- Step 1: Load data ---\n    logger.info(\"Loading Few-NERD test data (max_samples=%s)...\", args.max_samples)\n    samples = load_few_nerd(split=\"test\", max_samples=args.max_samples)\n    type_definitions = load_type_definitions(args.types_file)\n    active_types = sorted(get_all_types(samples))\n    logger.info(\"Loaded %d samples, %d active entity types\", len(samples), len(active_types))\n\n    # --- Step 2: Load similarity matrix ---\n    logger.info(\"Loading similarity matrix from %s\", args.sim_matrix_path)\n    sim_data = torch.load(args.sim_matrix_path, map_location=\"cpu\", weights_only=True)\n    sim_matrix = sim_data[\"sim_matrix\"]\n    type_to_idx = sim_data[\"type_to_idx\"]\n\n    # Filter to types present in both test data and sim matrix\n    active_type_names = sorted(t for t in active_types if t in type_to_idx)\n    logger.info(\"Active types in sim matrix: %d / %d\", len(active_type_names), len(active_types))\n\n    if args.high_count > len(active_type_names):\n        logger.warning(\"high_count=%d exceeds active types=%d, clamping\",\n                        args.high_count, len(active_type_names))\n        args.high_count = len(active_type_names)\n\n    # --- Step 3: Build factorial batches ---\n    logger.info(\"Building 2×2 factorial batches (pool_size=%d)...\", args.pool_size)\n    batch_config = build_factorial_batches(\n        sim_matrix=sim_matrix,\n        type_names=active_type_names,\n        type_to_idx=type_to_idx,\n        low_count=args.low_count,\n        high_count=args.high_count,\n        batches_per_cell=args.batches_per_cell,\n        pool_size=args.pool_size,\n        seed=args.seed,\n    )\n\n    batch_config_path = output_dir / \"batch_config.json\"\n    with open(batch_config_path, \"w\") as f:\n        json.dump(batch_config, f, indent=2)\n    logger.info(\"Saved batch config to %s\", batch_config_path)\n\n    # Print batch summary\n    total_batches = 0\n    for count_key, strategies in batch_config.items():\n        for strat_key, batches in strategies.items():\n            n = len(batches)\n            total_batches += n\n            bcs_vals = [b[\"bcs\"] for b in batches]\n            logger.info(\"  %s/%s: %d batches, BCS=[%.4f, %.4f], mean=%.4f\",\n                         count_key, strat_key, n, min(bcs_vals), max(bcs_vals),\n                         sum(bcs_vals) / len(bcs_vals))\n    logger.info(\"Total: %d batches × %d samples = %d extractions\",\n                total_batches, len(samples), total_batches * len(samples))\n\n    if args.dry_run:\n        logger.info(\"DRY RUN complete — batch config saved, skipping extraction.\")\n        return\n\n    # --- Step 4: Run extraction ---\n    if orig_cuda is not None:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = orig_cuda\n    elif \"CUDA_VISIBLE_DEVICES\" in os.environ:\n        del os.environ[\"CUDA_VISIBLE_DEVICES\"]\n\n    from run_extraction import run_extraction\n\n    logger.info(\"Starting vLLM extraction with %s ...\", args.model_path)\n    t0 = time.time()\n    results = run_extraction(\n        model_path=args.model_path,\n        samples=samples,\n        batch_config=batch_config,\n        type_definitions=type_definitions,\n        max_model_len=args.max_model_len,\n        prompt_version=\"v2\",\n        task=\"ner\",\n        gpu_memory_utilization=args.gpu_memory_utilization,\n    )\n    extraction_time = time.time() - t0\n    logger.info(\"Extraction done in %.1fs, %d result entries\", extraction_time, len(results))\n\n    predictions_path = output_dir / \"predictions.json\"\n    with open(predictions_path, \"w\") as f:\n        json.dump(results, f, ensure_ascii=False, indent=2)\n    logger.info(\"Saved predictions to %s\", predictions_path)\n\n    # --- Step 5: Evaluate ---\n    logger.info(\"Evaluating (text_match mode)...\")\n    eval_results = evaluate_all(results, samples, eval_mode=\"text_match\")\n\n    eval_path = output_dir / \"eval_results.json\"\n    with open(eval_path, \"w\") as f:\n        json.dump(eval_results, f, indent=2)\n    logger.info(\"Saved eval results to %s\", eval_path)\n\n    # --- Step 6: Interaction analysis ---\n    logger.info(\"Computing interaction analysis...\")\n    analysis = compute_interaction_analysis(eval_results)\n\n    analysis_path = output_dir / \"interaction_analysis.json\"\n    with open(analysis_path, \"w\") as f:\n        json.dump(analysis, f, indent=2, default=str)\n    logger.info(\"Saved interaction analysis to %s\", analysis_path)\n\n    # --- Summary ---\n    logger.info(\"=\" * 70)\n    logger.info(\"EXP-006 RESULTS: Count × BCS 2×2 Interaction\")\n    logger.info(\"=\" * 70)\n    for cell_key in [\"low_count/low_bcs\", \"low_count/high_bcs\",\n                     \"high_count/low_bcs\", \"high_count/high_bcs\"]:\n        stats = analysis[\"cell_means\"].get(cell_key, {})\n        if stats:\n            logger.info(\"  %-25s F1=%.4f ± %.4f  P=%.4f  R=%.4f  BCS=%.4f  (n=%d)\",\n                         cell_key,\n                         stats[\"mean_f1\"], stats[\"std_f1\"],\n                         stats[\"mean_precision\"], stats[\"mean_recall\"],\n                         stats[\"mean_bcs\"], stats[\"n_batches\"])\n    logger.info(\"-\" * 70)\n    logger.info(\"  Count main effect:     %+.4f (high_count - low_count)\",\n                analysis[\"main_effects\"][\"count_effect\"])\n    logger.info(\"  BCS main effect:       %+.4f (high_bcs - low_bcs)\",\n                analysis[\"main_effects\"][\"bcs_effect\"])\n    logger.info(\"  Interaction term:      %+.4f  %s\",\n                analysis[\"interaction\"][\"interaction_term\"],\n                analysis[\"interaction\"][\"formula\"])\n    logger.info(\"  → %s\", analysis[\"interaction\"][\"interpretation\"])\n    if \"z_test\" in analysis.get(\"interaction\", {}):\n        z = analysis[\"interaction\"][\"z_test\"]\n        logger.info(\"  z-test: z=%.3f, SE=%.4f, p=%.4f %s\",\n                     z[\"z_statistic\"], z[\"se_interaction\"], z[\"p_value\"],\n                     \"**\" if z[\"significant_005\"] else \"n.s.\")\n    logger.info(\"=\" * 70)\n    logger.info(\"Extraction time: %.1fs\", extraction_time)\n    logger.info(\"All results in: %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_EOF\necho \"DONE: $(wc -l < /root/schema-dag-extraction/scripts/run_exp006_interaction.py) lines\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat > /root/schema-dag-extraction/scripts/run_exp006_interaction.py << 'PYTHON_EOF'\n#!/usr/bin/env python3\n\"\"\"Exp-006: 2×2 Factorial — Count × Confusability Interaction on NER.\n\nTests whether count × BCS effects are additive or multiplicative.\n4 conditions (low/high count × low/high BCS), 10 batches each.\nHypothesis: if multiplicative, high_count + high_BCS degradation exceeds\nthe sum of the two main effects.\n\nInput:\n  - Few-NERD test data (parquet in data/parquet/)\n  - Qwen3-32B-FP8 model\n  - Pre-computed cosine similarity matrix (sim_matrix.pt)\nOutput (all in artifacts/exp006/):\n  - batch_config.json — 4-cell batch definitions with BCS scores\n  - predictions.json — raw model extraction outputs\n  - eval_results.json — per-batch text_match F1/P/R metrics\n  - interaction_analysis.json — cell means, main effects, interaction term\nDependencies: src/ modules (run_extraction, evaluate, compute_bcs, few_nerd_utils), vllm, torch\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport random\nimport sys\nimport time\nfrom pathlib import Path\n\nlogger = logging.getLogger(__name__)\n\nPROJECT_ROOT = Path(__file__).resolve().parent.parent\n\n\ndef build_factorial_batches(sim_matrix, type_names, type_to_idx,\n                            low_count, high_count, batches_per_cell,\n                            pool_size, seed):\n    \"\"\"Build 2×2 factorial batch config by selecting BCS extremes from random pools.\n\n    For each count level, generates a large random pool of type batches,\n    sorts by BCS, and picks the lowest and highest N as the two BCS conditions.\n\n    Args:\n        sim_matrix: N×N cosine similarity tensor.\n        type_names: list of type name strings (active types only).\n        type_to_idx: dict mapping type name to sim_matrix row/col index.\n        low_count: number of types for the low-count condition.\n        high_count: number of types for the high-count condition.\n        batches_per_cell: how many batches per factorial cell.\n        pool_size: random batches to sample per count level before selecting extremes.\n        seed: random seed.\n\n    Returns:\n        batch_config dict with keys \"low_count\"/\"high_count\", each containing\n        \"low_bcs\" and \"high_bcs\" lists of {\"types\": [...], \"bcs\": float}.\n    \"\"\"\n    from compute_bcs import compute_bcs\n\n    batch_config = {}\n\n    for count, count_label in [(low_count, \"low_count\"), (high_count, \"high_count\")]:\n        rng = random.Random(seed + count)\n        pool = []\n        seen = set()\n        max_attempts = pool_size * 20\n\n        for _ in range(max_attempts):\n            if len(pool) >= pool_size:\n                break\n            chosen = tuple(sorted(rng.sample(type_names, count)))\n            if chosen in seen:\n                continue\n            seen.add(chosen)\n            bcs = compute_bcs(list(chosen), sim_matrix, type_to_idx)\n            pool.append({\"types\": list(chosen), \"bcs\": bcs})\n\n        pool.sort(key=lambda x: x[\"bcs\"])\n\n        low_bcs_batches = pool[:batches_per_cell]\n        high_bcs_batches = pool[-batches_per_cell:]\n\n        logger.info(\"  %s (count=%d): pool=%d, low_bcs=[%.4f, %.4f], high_bcs=[%.4f, %.4f]\",\n                     count_label, count, len(pool),\n                     low_bcs_batches[0][\"bcs\"], low_bcs_batches[-1][\"bcs\"],\n                     high_bcs_batches[0][\"bcs\"], high_bcs_batches[-1][\"bcs\"])\n\n        batch_config[count_label] = {\n            \"low_bcs\": low_bcs_batches,\n            \"high_bcs\": high_bcs_batches,\n        }\n\n    return batch_config\n\n\ndef compute_interaction_analysis(eval_results):\n    \"\"\"Compute 2×2 factorial analysis from evaluation results.\n\n    Groups batch results into 4 cells, computes cell means for text_match F1,\n    derives main effects and interaction term, and runs a contrast significance test.\n\n    Args:\n        eval_results: dict from evaluate_all(), mapping batch_id -> metrics.\n\n    Returns:\n        dict with cell_means, main_effects, interaction (with optional t-test).\n    \"\"\"\n    cells = {\n        \"low_count/low_bcs\": [],\n        \"low_count/high_bcs\": [],\n        \"high_count/low_bcs\": [],\n        \"high_count/high_bcs\": [],\n    }\n\n    for bid, metrics in eval_results.items():\n        parts = bid.split(\"/\")\n        if len(parts) >= 2:\n            cell_key = f\"{parts[0]}/{parts[1]}\"\n            if cell_key in cells:\n                cells[cell_key].append(metrics)\n\n    cell_means = {}\n    for key, batch_metrics in cells.items():\n        if not batch_metrics:\n            logger.warning(\"No results for cell %s\", key)\n            continue\n        f1s = [m[\"text_match\"][\"f1\"] for m in batch_metrics]\n        precs = [m[\"text_match\"][\"precision\"] for m in batch_metrics]\n        recs = [m[\"text_match\"][\"recall\"] for m in batch_metrics]\n        bcs_vals = [m[\"bcs\"] for m in batch_metrics]\n        mean_f1 = sum(f1s) / len(f1s)\n        std_f1 = (sum((x - mean_f1) ** 2 for x in f1s) / len(f1s)) ** 0.5\n        cell_means[key] = {\n            \"mean_f1\": mean_f1,\n            \"std_f1\": std_f1,\n            \"se_f1\": std_f1 / len(f1s) ** 0.5 if len(f1s) > 1 else 0.0,\n            \"mean_precision\": sum(precs) / len(precs),\n            \"mean_recall\": sum(recs) / len(recs),\n            \"mean_bcs\": sum(bcs_vals) / len(bcs_vals),\n            \"n_batches\": len(f1s),\n            \"f1_values\": f1s,\n        }\n\n    def get_f1(key):\n        return cell_means.get(key, {}).get(\"mean_f1\", 0.0)\n\n    def get_se(key):\n        return cell_means.get(key, {}).get(\"se_f1\", 0.0)\n\n    ll = get_f1(\"low_count/low_bcs\")\n    lh = get_f1(\"low_count/high_bcs\")\n    hl = get_f1(\"high_count/low_bcs\")\n    hh = get_f1(\"high_count/high_bcs\")\n\n    # Main effects (marginal means difference)\n    count_effect = (hl + hh) / 2 - (ll + lh) / 2\n    bcs_effect = (lh + hh) / 2 - (ll + hl) / 2\n\n    # Interaction: does BCS effect differ between count levels?\n    bcs_effect_at_low_count = lh - ll\n    bcs_effect_at_high_count = hh - hl\n    interaction = bcs_effect_at_high_count - bcs_effect_at_low_count\n\n    # Interaction < 0 means BCS hurts MORE at high count (super-additive / multiplicative)\n    if interaction < -0.005:\n        interpretation = \"Super-additive (multiplicative): BCS effect amplified at high count\"\n    elif interaction > 0.005:\n        interpretation = \"Sub-additive: BCS effect attenuated at high count\"\n    else:\n        interpretation = \"Approximately additive: BCS and count effects are independent\"\n\n    analysis = {\n        \"cell_means\": cell_means,\n        \"cell_f1_summary\": {\n            \"low_count_low_bcs\": ll,\n            \"low_count_high_bcs\": lh,\n            \"high_count_low_bcs\": hl,\n            \"high_count_high_bcs\": hh,\n        },\n        \"main_effects\": {\n            \"count_effect\": count_effect,\n            \"bcs_effect\": bcs_effect,\n            \"count_effect_interpretation\": \"high_count marginal mean - low_count marginal mean\",\n            \"bcs_effect_interpretation\": \"high_bcs marginal mean - low_bcs marginal mean\",\n        },\n        \"interaction\": {\n            \"bcs_effect_at_low_count\": bcs_effect_at_low_count,\n            \"bcs_effect_at_high_count\": bcs_effect_at_high_count,\n            \"interaction_term\": interaction,\n            \"formula\": \"(HH - HL) - (LH - LL)\",\n            \"interpretation\": interpretation,\n        },\n    }\n\n    # Contrast significance test via SE propagation\n    se_ll = get_se(\"low_count/low_bcs\")\n    se_lh = get_se(\"low_count/high_bcs\")\n    se_hl = get_se(\"high_count/low_bcs\")\n    se_hh = get_se(\"high_count/high_bcs\")\n    se_interaction = (se_ll**2 + se_lh**2 + se_hl**2 + se_hh**2) ** 0.5\n\n    if se_interaction > 0:\n        z_stat = interaction / se_interaction\n        # Two-tailed p-value approximation (normal)\n        p_value = 2 * (1 - _norm_cdf(abs(z_stat)))\n        analysis[\"interaction\"][\"z_test\"] = {\n            \"z_statistic\": z_stat,\n            \"se_interaction\": se_interaction,\n            \"p_value\": p_value,\n            \"significant_005\": p_value < 0.05,\n        }\n\n    return analysis\n\n\ndef _norm_cdf(x):\n    \"\"\"Standard normal CDF approximation (no scipy dependency).\"\"\"\n    return 0.5 * (1 + math.erf(x / math.sqrt(2)))\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Exp-006: Count × Confusability 2×2 factorial interaction design\"\n    )\n    parser.add_argument(\"--model_path\", default=\"/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\",\n                        help=\"Path to Qwen3-32B-FP8 model\")\n    parser.add_argument(\"--types_file\", default=\"configs/few_nerd_types.json\",\n                        help=\"Type definitions JSON\")\n    parser.add_argument(\"--sim_matrix_path\", default=\"artifacts/sim_matrix.pt\",\n                        help=\"Pre-computed similarity matrix\")\n    parser.add_argument(\"--output_dir\", default=\"artifacts/exp006\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--max_samples\", type=int, default=1000,\n                        help=\"Max test samples from Few-NERD\")\n    parser.add_argument(\"--max_model_len\", type=int, default=4096,\n                        help=\"vLLM max model length\")\n    parser.add_argument(\"--gpu_memory_utilization\", type=float, default=0.95,\n                        help=\"vLLM GPU memory utilization\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--low_count\", type=int, default=6,\n                        help=\"Number of types in low-count condition\")\n    parser.add_argument(\"--high_count\", type=int, default=22,\n                        help=\"Number of types in high-count condition\")\n    parser.add_argument(\"--batches_per_cell\", type=int, default=10,\n                        help=\"Number of random batches per factorial cell\")\n    parser.add_argument(\"--pool_size\", type=int, default=500,\n                        help=\"Random pool size for selecting BCS extremes\")\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Build and validate batches only, skip model extraction\")\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\n    random.seed(args.seed)\n\n    sys.path.insert(0, str(PROJECT_ROOT / \"src\"))\n\n    # Suppress CUDA init during imports (vLLM must init CUDA itself)\n    orig_cuda = os.environ.get(\"CUDA_VISIBLE_DEVICES\")\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = \"\"\n\n    import torch\n    from few_nerd_utils import load_few_nerd, load_type_definitions, get_all_types\n    from compute_bcs import compute_bcs\n    from evaluate import evaluate_all\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # --- Step 1: Load data ---\n    logger.info(\"Loading Few-NERD test data (max_samples=%s)...\", args.max_samples)\n    samples = load_few_nerd(split=\"test\", max_samples=args.max_samples)\n    type_definitions = load_type_definitions(args.types_file)\n    active_types = sorted(get_all_types(samples))\n    logger.info(\"Loaded %d samples, %d active entity types\", len(samples), len(active_types))\n\n    # --- Step 2: Load similarity matrix ---\n    logger.info(\"Loading similarity matrix from %s\", args.sim_matrix_path)\n    sim_data = torch.load(args.sim_matrix_path, map_location=\"cpu\", weights_only=True)\n    sim_matrix = sim_data[\"sim_matrix\"]\n    type_to_idx = sim_data[\"type_to_idx\"]\n\n    # Filter to types present in both test data and sim matrix\n    active_type_names = sorted(t for t in active_types if t in type_to_idx)\n    logger.info(\"Active types in sim matrix: %d / %d\", len(active_type_names), len(active_types))\n\n    if args.high_count > len(active_type_names):\n        logger.warning(\"high_count=%d exceeds active types=%d, clamping\",\n                        args.high_count, len(active_type_names))\n        args.high_count = len(active_type_names)\n\n    # --- Step 3: Build factorial batches ---\n    logger.info(\"Building 2×2 factorial batches (pool_size=%d)...\", args.pool_size)\n    batch_config = build_factorial_batches(\n        sim_matrix=sim_matrix,\n        type_names=active_type_names,\n        type_to_idx=type_to_idx,\n        low_count=args.low_count,\n        high_count=args.high_count,\n        batches_per_cell=args.batches_per_cell,\n        pool_size=args.pool_size,\n        seed=args.seed,\n    )\n\n    batch_config_path = output_dir / \"batch_config.json\"\n    with open(batch_config_path, \"w\") as f:\n        json.dump(batch_config, f, indent=2)\n    logger.info(\"Saved batch config to %s\", batch_config_path)\n\n    # Print batch summary\n    total_batches = 0\n    for count_key, strategies in batch_config.items():\n        for strat_key, batches in strategies.items():\n            n = len(batches)\n            total_batches += n\n            bcs_vals = [b[\"bcs\"] for b in batches]\n            logger.info(\"  %s/%s: %d batches, BCS=[%.4f, %.4f], mean=%.4f\",\n                         count_key, strat_key, n, min(bcs_vals), max(bcs_vals),\n                         sum(bcs_vals) / len(bcs_vals))\n    logger.info(\"Total: %d batches × %d samples = %d extractions\",\n                total_batches, len(samples), total_batches * len(samples))\n\n    if args.dry_run:\n        logger.info(\"DRY RUN complete — batch config saved, skipping extraction.\")\n        return\n\n    # --- Step 4: Run extraction ---\n    if orig_cuda is not None:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = orig_cuda\n    elif \"CUDA_VISIBLE_DEVICES\" in os.environ:\n        del os.environ[\"CUDA_VISIBLE_DEVICES\"]\n\n    from run_extraction import run_extraction\n\n    logger.info(\"Starting vLLM extraction with %s ...\", args.model_path)\n    t0 = time.time()\n    results = run_extraction(\n        model_path=args.model_path,\n        samples=samples,\n        batch_config=batch_config,\n        type_definitions=type_definitions,\n        max_model_len=args.max_model_len,\n        prompt_version=\"v2\",\n        task=\"ner\",\n        gpu_memory_utilization=args.gpu_memory_utilization,\n    )\n    extraction_time = time.time() - t0\n    logger.info(\"Extraction done in %.1fs, %d result entries\", extraction_time, len(results))\n\n    predictions_path = output_dir / \"predictions.json\"\n    with open(predictions_path, \"w\") as f:\n        json.dump(results, f, ensure_ascii=False, indent=2)\n    logger.info(\"Saved predictions to %s\", predictions_path)\n\n    # --- Step 5: Evaluate ---\n    logger.info(\"Evaluating (text_match mode)...\")\n    eval_results = evaluate_all(results, samples, eval_mode=\"text_match\")\n\n    eval_path = output_dir / \"eval_results.json\"\n    with open(eval_path, \"w\") as f:\n        json.dump(eval_results, f, indent=2)\n    logger.info(\"Saved eval results to %s\", eval_path)\n\n    # --- Step 6: Interaction analysis ---\n    logger.info(\"Computing interaction analysis...\")\n    analysis = compute_interaction_analysis(eval_results)\n\n    analysis_path = output_dir / \"interaction_analysis.json\"\n    with open(analysis_path, \"w\") as f:\n        json.dump(analysis, f, indent=2, default=str)\n    logger.info(\"Saved interaction analysis to %s\", analysis_path)\n\n    # --- Summary ---\n    logger.info(\"=\" * 70)\n    logger.info(\"EXP-006 RESULTS: Count × BCS 2×2 Interaction\")\n    logger.info(\"=\" * 70)\n    for cell_key in [\"low_count/low_bcs\", \"low_count/high_bcs\",\n                     \"high_count/low_bcs\", \"high_count/high_bcs\"]:\n        stats = analysis[\"cell_means\"].get(cell_key, {})\n        if stats:\n            logger.info(\"  %-25s F1=%.4f ± %.4f  P=%.4f  R=%.4f  BCS=%.4f  (n=%d)\",\n                         cell_key,\n                         stats[\"mean_f1\"], stats[\"std_f1\"],\n                         stats[\"mean_precision\"], stats[\"mean_recall\"],\n                         stats[\"mean_bcs\"], stats[\"n_batches\"])\n    logger.info(\"-\" * 70)\n    logger.info(\"  Count main effect:     %+.4f (high_count - low_count)\",\n                analysis[\"main_effects\"][\"count_effect\"])\n    logger.info(\"  BCS main effect:       %+.4f (high_bcs - low_bcs)\",\n                analysis[\"main_effects\"][\"bcs_effect\"])\n    logger.info(\"  Interaction term:      %+.4f  %s\",\n                analysis[\"interaction\"][\"interaction_term\"],\n                analysis[\"interaction\"][\"formula\"])\n    logger.info(\"  → %s\", analysis[\"interaction\"][\"interpretation\"])\n    if \"z_test\" in analysis.get(\"interaction\", {}):\n        z = analysis[\"interaction\"][\"z_test\"]\n        logger.info(\"  z-test: z=%.3f, SE=%.4f, p=%.4f %s\",\n                     z[\"z_statistic\"], z[\"se_interaction\"], z[\"p_value\"],\n                     \"**\" if z[\"significant_005\"] else \"n.s.\")\n    logger.info(\"=\" * 70)\n    logger.info(\"Extraction time: %.1fs\", extraction_time)\n    logger.info(\"All results in: %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_EOF\necho \"DONE: $(wc -l < /root/schema-dag-extraction/scripts/run_exp006_interaction.py) lines\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T17:37:32.961171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE: 405 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T17:37:32.961378+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python scripts/run_exp006_interaction.py --dry_run 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python scripts/run_exp006_interaction.py --dry_run 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T17:37:32.961608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 01:35:48,350 INFO Loading Few-NERD test data (max_samples=1000)...\\n2026-05-16 01:35:48,351 INFO Loading Few-NERD from local parquet: /root/schema-dag-extraction/data/parquet/test.parquet\\n2026-05-16 01:35:50,443 INFO Loaded 1000 samples from Few-NERD test split\\n2026-05-16 01:35:50,446 INFO Loaded 1000 samples, 64 active entity types\\n2026-05-16 01:35:50,447 INFO Loading similarity matrix from artifacts/sim_matrix.pt\\n2026-05-16 01:35:50,457 INFO Active types in sim matrix: 64 / 64\\n2026-05-16 01:35:50,457 INFO Building 2×2 factorial batches (pool_size=500)...\\n2026-05-16 01:35:50,587 INFO   low_count (count=6): pool=500, low_bcs=[0.8327, 0.8454], high_bcs=[0.9526, 0.9732]\\n2026-05-16 01:35:52,336 INFO   high_count (count=22): pool=500, low_bcs=[0.8993, 0.9103], high_bcs=[0.9732, 0.9732]\\n2026-05-16 01:35:52,341 INFO Saved batch config to artifacts/exp006/batch_config.json\\n2026-05-16 01:35:52,342 INFO   low_count/low_bcs: 10 batches, BCS=[0.8327, 0.8454], mean=0.8417\\n2026-05-16 01:35:52,342 INFO   low_count/high_bcs: 10 batches, BCS=[0.9526, 0.9732], mean=0.9615\\n2026-05-16 01:35:52,342 INFO   high_count/low_bcs: 10 batches, BCS=[0.8993, 0.9103], mean=0.9076\\n2026-05-16 01:35:52,342 INFO   high_count/high_bcs: 10 batches, BCS=[0.9732, 0.9732], mean=0.9732\\n2026-05-16 01:35:52,342 INFO Total: 40 batches × 1000 samples = 40000 extractions\\n2026-05-16 01:35:52,343 INFO DRY RUN complete — batch config saved, skipping extraction.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T17:37:32.961878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T17:37:32.962099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 01:36:05 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 590.44.01              Driver Version: 590.44.01      CUDA Version: 13.1     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |\\n| N/A   44C    P0            150W /  600W |   84661MiB /  97887MiB |     26%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          308566      C   VLLM::EngineCore                      84652MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T17:37:32.962336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls /tmp/.aml_gpu_locks/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls /tmp/.aml_gpu_locks/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T17:37:32.962519+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/tmp/.aml_gpu_locks/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T17:37:32.962689+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tmux list-sessions 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "tmux list-sessions 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T17:37:32.962883+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'tmux list-sessions 2>&1'\\n\\nExit code: 1\\n\\nStdout:\\n\\nno server running on /tmp/tmux-0/default\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T17:37:32.963076+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ps -p 308566 -o pid,ppid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ps -p 308566 -o pid,ppid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T17:37:32.963249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID   PPID     ELAPSED CMD\\n308566 308251       10:39 VLLM::EngineCore\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T17:37:32.963434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ps -p 308251 -o pid,ppid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ps -p 308251 -o pid,ppid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T17:37:32.963608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID   PPID     ELAPSED CMD\\n308251 308246       11:38 python3 src/run_experiment.py --mode exp1 --dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct --model_name llama-3.1-8b-instruct --max_samples 1000 --max_model_len 4096 --gpu_memory_utilization 0.85 --output_dir artifacts/exp012\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T17:37:32.963831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/artifacts/exp012/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -la /root/schema-dag-extraction/artifacts/exp012/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T17:37:32.964053+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 76828\\ndrwxr-xr-x  2 root root     4096 May 16 00:45 .\\ndrwxr-xr-x 17 root root     4096 May 16 01:35 ..\\n-rw-r--r--  1 root root    32311 May 16 01:25 batch_config_fewnerd_exp1_llama-3.1-8b-instruct.json\\n-rw-r--r--  1 root root    32311 May 15 23:51 batch_config_fewnerd_exp1_llama-3.3-70b-fp8.json\\n-rw-r--r--  1 root root    19664 May 16 00:37 batch_config_fewnerd_exp2_llama-3.1-8b-instruct.json\\n-rw-r--r--  1 root root    82015 May 16 00:37 eval_fewnerd_exp1_llama-3.1-8b-instruct.json\\n-rw-r--r--  1 root root    48535 May 16 00:45 eval_fewnerd_exp2_llama-3.1-8b-instruct.json\\n-rw-r--r--  1 root root 49057488 May 16 00:37 predictions_fewnerd_exp1_llama-3.1-8b-instruct.json\\n-rw-r--r--  1 root root 29381062 May 16 00:45 predictions_fewnerd_exp2_llama-3.1-8b-instruct.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T17:37:32.964250+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ps -p 308251 -o pid,ppid,etime,stat,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ps -p 308251 -o pid,ppid,etime,stat,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T17:37:32.964427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID   PPID     ELAPSED STAT CMD\\n308251 308246       11:54 Rl   python3 src/run_experiment.py --mode exp1 --dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path /root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct --model_name llama-3.1-8b-instruct --max_samples 1000 --max_model_len 4096 --gpu_memory_utilization 0.85 --output_dir artifacts/exp012\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T17:37:32.964649+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python scripts/run_exp006_interaction.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python scripts/run_exp006_interaction.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T17:37:32.964901+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_exp006_interaction.py [-h] [--model_path MODEL_PATH]\\n                                 [--types_file TYPES_FILE]\\n                                 [--sim_matrix_path SIM_MATRIX_PATH]\\n                                 [--output_dir OUTPUT_DIR]\\n                                 [--max_samples MAX_SAMPLES]\\n                                 [--max_model_len MAX_MODEL_LEN]\\n                                 [--gpu_memory_utilization GPU_MEMORY_UTILIZATION]\\n                                 [--seed SEED] [--low_count LOW_COUNT]\\n                                 [--high_count HIGH_COUNT]\\n                                 [--batches_per_cell BATCHES_PER_CELL]\\n                                 [--pool_size POOL_SIZE] [--dry_run]\\n\\nExp-006: Count × Confusability 2×2 factorial interaction design\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n                        Path to Qwen3-32B-FP8 model\\n  --types_file TYPES_FILE\\n                        Type definitions JSON\\n  --sim_matrix_path SIM_MATRIX_PATH\\n                        Pre-computed similarity matrix\\n  --output_dir OUTPUT_DIR\\n                        Output directory\\n  --max_samples MAX_SAMPLES\\n                        Max test samples from Few-NERD\\n  --max_model_len MAX_MODEL_LEN\\n                        vLLM max model length\\n  --gpu_memory_utilization GPU_MEMORY_UTILIZATION\\n                        vLLM GPU memory utilization\\n  --seed SEED\\n  --low_count LOW_COUNT\\n                        Number of types in low-count condition\\n  --high_count HIGH_COUNT\\n                        Number of types in high-count condition\\n  --batches_per_cell BATCHES_PER_CELL\\n                        Number of random batches per factorial cell\\n  --pool_size POOL_SIZE\\n                        Random pool size for selecting BCS extremes\\n  --dry_run             Build and validate ba
…[truncated 140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T17:37:32.965146+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp006_interaction_2x2_script",
  "type": "intermediate",
  "description": "Exp-006 script: 2×2 factorial (count × BCS) interaction experiment on Few-NERD with Qwen3-32B-FP8. Tests whether count and confusability effects are additive or multiplicative.",
  "project": "schema-dag-extraction",
  "exp_id": "exp006_interaction_2x2",
  "source_path": "/root/schema-dag-extraction/scripts/run_exp006_interaction.py",
  "tags": "['exp006', 'factorial', 'interaction', 'fewnerd', 'qwen3-32b']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp006_interaction_2x2_script",
    "type": "intermediate",
    "description": "Exp-006 script: 2×2 factorial (count × BCS) interaction experiment on Few-NERD with Qwen3-32B-FP8. Tests whether count and confusability effects are additive or multiplicative.",
    "project": "schema-dag-extraction",
    "exp_id": "exp006_interaction_2x2",
    "source_path": "/root/schema-dag-extraction/scripts/run_exp006_interaction.py",
    "tags": "['exp006', 'factorial', 'interaction', 'fewnerd', 'qwen3-32b']"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T17:37:32.965340+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/schema-dag-extraction/scripts/run_exp006_interaction.py\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T17:37:32.965537+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp006_interaction_2x2_script",
  "type": "intermediate",
  "description": "Exp-006 script: 2×2 factorial (count × BCS) interaction experiment on Few-NERD with Qwen3-32B-FP8. Tests whether count and confusability effects are additive or multiplicative. Located at /root/schema-dag-extraction/scripts/run_exp006_interaction.py on cqa1-38874.",
  "project": "schema-dag-extraction",
  "exp_id": "exp006_interaction_2x2",
  "content": "Remote file: /root/schema-dag-extraction/scripts/run_exp006_interaction.py on cqa1-38874\nDry-run validated: 4 cells × 10 batches = 40 batches × 1000 samples\nSubmit command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && FLASHINFER_DISABLE_VERSION_CHECK=1 python scripts/run_exp006_interaction.py --max_samples 1000\"",
  "content_filename": "exp006_script_info.txt",
  "tags": "['exp006', 'factorial', 'interaction', 'fewnerd', 'qwen3-32b']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp006_interaction_2x2_script",
    "type": "intermediate",
    "description": "Exp-006 script: 2×2 factorial (count × BCS) interaction experiment on Few-NERD with Qwen3-32B-FP8. Tests whether count and confusability effects are additive or multiplicative. Located at /root/schema-dag-extraction/scripts/run_exp006_interaction.py on cqa1-38874.",
    "project": "schema-dag-extraction",
    "exp_id": "exp006_interaction_2x2",
    "content": "Remote file: /root/schema-dag-extraction/scripts/run_exp006_interaction.py on cqa1-38874\nDry-run validated: 4 cells × 10 batches = 40 batches × 1000 samples\nSubmit command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && FLASHINFER_DISABLE_VERSION_CHECK=1 python scripts/run_exp006_interaction.py --max_samples 1000\"",
    "content_filename": "exp006_script_info.txt",
    "tags": "['exp006', 'factorial', 'interaction', 'fewnerd', 'qwen3-32b']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T17:37:32.965762+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b16537\", \"name\": \"exp006_interaction_2x2_script\", \"type\": \"intermediate\", \"description\": \"Exp-006 script: 2×2 factorial (count × BCS) interaction experiment on Few-NERD with Qwen3-32B-FP8. Tests whether count and confusability effects are additive or multiplicative. Located at /root/schema-dag-extraction/scripts/run_exp006_interaction.py on cqa1-38874.\", \"path\": \"projects/schema-dag-extraction/artifacts/exp006_interaction_2x2/intermediate/exp006_script_info.txt\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": \"exp006_interaction_2x2\", \"skill\": \"\", \"created_at\": \"2026-05-15T17:37:19.802489+00:00\", \"tags\": [\"exp006\", \"factorial\", \"interaction\", \"fewnerd\", \"qwen3-32b\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-15T17:37:32.966029+00:00_

## 完成状态

**脚本已就绪，未提交**（cuda:0 被 exp012 Llama-8B exp1 占用中）。

### 脚本位置
`/root/schema-dag-extraction/scripts/run_exp006_interaction.py` (cqa1-38874)

### Dry-run 验证结果
| Cell | Batches | BCS Range | Mean BCS |
|------|---------|-----------|----------|
| low_count (6) / low_bcs | 10 | [0.8327, 0.8454] | 0.8417 |
| low_count (6) / high_bcs | 10 | [0.9526, 0.9732] | 0.9615 |
| high_count (22) / low_bcs | 10 | [0.8993, 0.9103] | 0.9076 |
| high_count (22) / high_bcs | 10 | [0.9732, 0.9732] | 0.9732 |

共 40 batches × 1000 samples = 40,000 extractions。

### 提交命令（GPU 空闲后执行）
```
submit_training_job:
  server: cqa1-38874
  gpu_ids: ["cuda:0"]
  exp_id: exp006_interaction_2x2
  account: root
  timeout_hours: 3
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && FLASHINFER_DISABLE_VERSION_CHECK=1 python scripts/run_exp006_interaction.py --max_samples 1000"
```

### 设计要点
- 从 500 个随机 batch pool 中选 BCS 最低/最高各 10 个，确保 low/high BCS 有清晰分离
- 复用现有 `run_extraction` (vLLM + guided_json v2) 和 `evaluate_all` (text_match)
- 分析输出：4-cell mean F1、count/BCS main effects、interaction term (cross-difference) + z-test

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp006_interaction_2x2_20260515T173024"
}
```

</details>

---
