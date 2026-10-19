# code eval repobench

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_code_eval_repobench_20260514T082145.jsonl`
- **Structured JSON:** [`bde6eb19f67ff46f08d1.json`](../../sessions/bd/bde6eb19f67ff46f08d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-14T08:31:23.151324+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T08:31:23.151768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T08:31:23.151952+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RepoBench-R cross-file retrieval dataset format huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RepoBench-R cross-file retrieval dataset format huggingface"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T08:31:23.152098+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RepoBench evaluation protocol retrieval recall MRR metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RepoBench evaluation protocol retrieval recall MRR metrics"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T08:31:23.152221+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T08:31:23.152388+00:00_

Web search results for query: "RepoBench evaluation protocol retrieval recall MRR metrics"

Links: [{"title":"Evaluation Metrics for Search and Recommendation Systems | Weaviate","url":"https://weaviate.io/blog/retrieval-evaluation-metrics"},{"title":"The aRt of RAG Part 4: Retrieval evaluation | by Ross Ashman (PhD) | Medium","url":"https://medium.com/@rossashman/the-art-of-rag-part-4-retrieval-evaluation-427bb5db0475"},{"title":"Retrieval Metrics Tutorial: Recall@k and MRR Explained | by rajnish khatri | Medium","url":"https://medium.com/@rajnish_khatri/retrieval-metrics-tutorial-recall-k-and-mrr-explained-d2f12afb9c89"},{"title":"Evaluation Measures in Information Retrieval | Pinecone","url":"https://www.pinecone.io/learn/offline-evaluation/"},{"title":"Redefining Retrieval Evaluation in the Era of LLMs","url":"https://arxiv.org/html/2510.21440v1"},{"title":"Metrics for Evaluation of Retrieval in Retrieval-Augmented Generation (RAG) Systems | Deconvolute Labs","url":"https://deconvoluteai.com/blog/rag/metrics-retrieval"},{"title":"RAG Evaluation: 2026 Metrics and Benchmarks for Enterprise AI Systems | Label Your Data","url":"https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation"},{"title":"Evaluating Information Retrieval Models: A Comprehensive Guide to Performance Metrics | by Prateek Gaurav | Medium","url":"https://medium.com/@prateekgaurav/evaluating-information-retrieval-models-a-comprehensive-guide-to-performance-metrics-78aadacb73b4"},{"title":"Evaluation Metrics for Retrieval-Augmented Generation (RAG) Systems - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/evaluation-metrics-for-retrieval-augmented-generation-rag-systems/"},{"title":"Aman's AI Journal • Recommendation Systems • Evaluation Metrics and Loss Functions","url":"https://aman.ai/recsys/metrics/"}]

I've performed a web search for "RepoBench evaluation protocol retrieval recall MRR metrics". The results returned comprehensive information about retrieval evaluation metrics i
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T08:31:23.152571+00:00_

Web search results for query: "RepoBench-R cross-file retrieval dataset format huggingface"

Links: [{"title":"tianyang/repobench-r · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-r"},{"title":"tianyang/repobench-p · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-p"},{"title":"repobench-r.py · tianyang/repobench-r at e6d80b14226f09bfd7817d2ee7591cfe372f1f5f","url":"https://huggingface.co/datasets/tianyang/repobench-r/blame/e6d80b14226f09bfd7817d2ee7591cfe372f1f5f/repobench-r.py"},{"title":"README.md · yanbingzheng/LongBench at main","url":"https://huggingface.co/datasets/yanbingzheng/LongBench/blob/main/README.md"},{"title":"tianyang/repobench_java_v1.1 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_java_v1.1"},{"title":"tianyang/repobench_python_v1.1 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_python_v1.1"},{"title":"README.md · tianyang/repobench-r at 93c340aca9c02afd23f3c70087433af1c154ccfc","url":"https://huggingface.co/datasets/tianyang/repobench-r/blob/93c340aca9c02afd23f3c70087433af1c154ccfc/README.md"},{"title":"zai-org/LongBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/zai-org/LongBench"},{"title":"yanbingzheng/LongBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yanbingzheng/LongBench"},{"title":"tianyang/repobench-c · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-c"}]

Based on the search results, here's information about the RepoBench-R cross-file retrieval dataset format on Hugging Face:

## Dataset Overview

RepoBench-R (Retrieval) is a subtask of RepoBench, targeting the retrieval component of a repository-level auto-completion system, focusing on retrieving the most relevant code snippet from a project repository for next-line code prediction.

## Dataset Subsets and Splits

The dataset has 4 subsets (java_cff,
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T08:31:23.152758+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T08:31:23.152927+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -type f -name \"*.py\" -path \"*/evaluation/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -type f -name \"*.py\" -path \"*/evaluation/*\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T08:31:23.153055+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T08:31:23.153171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -type f -name \"model*.py\" -path \"*/training/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -type f -name \"model*.py\" -path \"*/training/*\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T08:31:23.153290+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T08:31:23.153404+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls -la /root/structfuse/evaluation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls -la /root/structfuse/evaluation/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T08:31:23.153526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 84\\ndrwxr-xr-x  3 root root   186 May 14 08:47 .\\ndrwxr-xr-x 11 root root  4096 May 14 10:57 ..\\ndrwxr-xr-x  2 root root    51 May 14 08:47 __pycache__\\n-rw-r--r--  1 root root 17145 May 12 19:55 eval_retrieval.py\\n-rw-r--r--  1 root root 20395 May 14 07:59 eval_swebench.py\\n-rw-r--r--  1 root root 18098 May 14 02:54 eval_swebench.py.bak\\n-rw-r--r--  1 root root 14097 May 14 07:58 linear_proxy.py\\n-rw-r--r--  1 root root  3073 May 12 19:39 linear_proxy_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T08:31:23.153704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/evaluation/eval_retrieval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/evaluation/eval_retrieval.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T08:31:23.153990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"4\\\"\\n\\n\\\"\\\"\\\"\\nStructFuse Retrieval Evaluation Script\\n\\nEvaluates the StructFuse contrastive retriever on file-level and function-level\\nretrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.\\n\\nInput:\\n  - Trained StructFuse checkpoint(s)\\n  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}\\n  - (Optional) CodeQL data-flow output directory\\n\\nOutput:\\n  - JSON file with per-instance predictions and aggregate metrics:\\n    Recall@1/5/10, MRR, Structural Precision\\n\\nDependencies: transformers, torch, rank_bm25, faiss-cpu, numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom dataclasses import dataclass, field\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport jsonlines\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom tqdm import tqdm\\nfrom transformers import AutoTokenizer\\nfrom rank_bm25 import BM25Okapi\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\n@dataclass\\nclass RetrievalInstance:\\n    query: str\\n    gold_files: list[str]\\n    gold_functions: list[str] = field(default_factory=list)\\n    repo_path: str = \\\"\\\"\\n    instance_id: str = \\\"\\\"\\n    metadata: dict = field(default_factory=dict)\\n\\n\\n@dataclass\\nclass RetrievalResult:\\n    instance_id: str\\n    query: str\\n    gold_files: list[str]\\n    predicted_files: list[str]\\n    scores: list[float]\\n    hits: dict[str, bool] = field(default_factory=dict)\\n\\n\\ndef load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:\\n    \\\"\\\"\\\"Load test instances from JSON Lines file, adapting format per dataset
…[truncated 7347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T08:31:23.154147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T08:31:23.154406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"StructFuse SWE-bench Retrieval Evaluation.\\n\\nMeasures file-level retrieval quality of a trained StructFuse checkpoint on\\nSWE-bench Lite (300 instances) or Verified split.\\n\\nPer-instance pipeline:\\n  1. Clone/checkout target repo at base_commit\\n  2. Collect all Python files as candidate pool\\n  3. Encode issue text (query) and file contents (candidates) with StructFuse\\n  4. Rank candidates by cosine similarity\\n  5. Compare predicted top-k with gold patch files -> Recall@k, MRR\\n\\nOutputs (in --output-dir):\\n  per_instance_results.jsonl  per-instance ranked predictions and metrics\\n  summary.json                aggregate Recall@k, MRR, config\\n\\nUsage:\\n  # Full eval (requires GPU + trained checkpoint)\\n  python eval_swebench.py \\\\\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s42/best_by_recall_at_1 \\\\\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/qwen_best_recall\\n\\n  # Dry-run (no GPU, tests pipeline logic with mock embeddings)\\n  python eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5\\n\\nDependencies: transformers, torch, datasets, numpy, tqdm\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom dataclasses import asdict, dataclass, field\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom tqdm import tqdm\\n\\n\\n# ── Data structures ─────────────────────────────────────────────────\\n\\n@dataclass\\nclass SWEInstance:\\n    instance_id: str\\n    repo: str\\n    base_commit: str\\n    problem_statement: str\\n    patch: str\\n    gold_files: list[str] = field(default_factory=list)\\n\\n\\n@dataclass\\nclass InstanceResult:\\n    instance_id: str\\n    repo: str\\n    gold_files: list[str]\\n    predicted_files: list[str]\\n    predicted_
…[truncated 7287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T08:31:23.154572+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -type f -name \"*.py\" -path \"*/training/*\" -not -path \"*/__pycache__/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -type f -name \"*.py\" -path \"*/training/*\" -not -path \"*/__pycache__/*\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T08:31:23.154732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T08:31:23.154889+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse/training -type f -name \"*.py\" -not -path \"*/__pycache__/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse/training -type f -name \"*.py\" -not -path \"*/__pycache__/*\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T08:31:23.155017+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/training/train.py\\n/root/structfuse/training/contrastive_model.py\\n/root/structfuse/training/hard_negative_mining.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T08:31:23.155153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/training/contrastive_model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/training/contrastive_model.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T08:31:23.155384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"StructFuse contrastive bi-encoder with fusion head.\\n\\nBi-encoder over Qwen2.5-Coder-3B with InfoNCE loss, weighted positives\\n(data-flow path distance), and an optional lightweight fusion head that\\ncombines embedding similarity with explicit structural features.\\n\\\"\\\"\\\"\\n\\nimport math\\nimport torch\\nimport torch.nn as nn\\nimport torch.nn.functional as F\\nfrom transformers import AutoModel, AutoConfig\\n\\n\\nclass FusionHead(nn.Module):\\n    \\\"\\\"\\\"MLP that fuses embedding similarity with explicit features into a relevance score.\\\"\\\"\\\"\\n\\n    FEATURE_NAMES = [\\n        \\\"dataflow_distance\\\",\\n        \\\"bm25_score\\\",\\n        \\\"co_change_freq\\\",\\n        \\\"inter_procedural_flag\\\",\\n        \\\"path_count\\\",\\n    ]\\n    NUM_EXPLICIT = len(FEATURE_NAMES)\\n\\n    def __init__(self, hidden_dim: int = 128):\\n        super().__init__()\\n        input_dim = 1 + self.NUM_EXPLICIT  # embed_similarity + explicit features\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, hidden_dim),\\n            nn.GELU(),\\n            nn.Linear(hidden_dim, hidden_dim),\\n            nn.GELU(),\\n            nn.Linear(hidden_dim, 1),\\n        )\\n\\n    def forward(self, embed_similarity: torch.Tensor, features: torch.Tensor) -> torch.Tensor:\\n        \\\"\\\"\\\"\\n        Args:\\n            embed_similarity: (B,) or (B, K) cosine similarities.\\n            features: same leading dims + NUM_EXPLICIT trailing dim.\\n        Returns:\\n            scores with same shape as embed_similarity.\\n        \\\"\\\"\\\"\\n        orig_shape = embed_similarity.shape\\n        sim = embed_similarity.unsqueeze(-1)  # (..., 1)\\n        x = torch.cat([sim, features], dim=-1)  # (..., 1+NUM_EXPLICIT)\\n        x = x.view(-1, x.size(-1))\\n        out = self.net(x).squeeze(-1)\\n        return out.view(orig_shape)\\n\\n\\nclass StructFuseEncoder(nn.Modul
…[truncated 5901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T08:31:23.155577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def load_model\\|def _load\\|def create_encoder\\|StructFuseEncoder\\|training_config\\|checkpoint\\|model\\.pt\\|state_dict\\|tokenizer\" /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def load_model\\|def _load\\|def create_encoder\\|StructFuseEncoder\\|training_config\\|checkpoint\\|model\\.pt\\|state_dict\\|tokenizer\" /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T08:31:23.155734+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T08:31:23.155859+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def load_model\\|def _load\\|StructFuseEncoder\\|training_config\\|state_dict\\|tokenizer\" /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def load_model\\|def _load\\|StructFuseEncoder\\|training_config\\|state_dict\\|tokenizer\" /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T08:31:23.155989+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T08:31:23.156121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \\|StructFuse\\|tokenizer\\|state_dict\\|training_config\\|model_name\" /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def \\|StructFuse\\|tokenizer\\|state_dict\\|training_config\\|model_name\" /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T08:31:23.156239+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T08:31:23.156352+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \" /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def \" /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T08:31:23.156477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"73:def extract_gold_files(patch: str) -> list[str]:\\n84:def load_swebench(split: str, num_instances: int = 0) -> list[SWEInstance]:\\n111:def _mock_swebench(num_instances: int) -> list[SWEInstance]:\\n130:def setup_repo(repo: str, base_commit: str, workspace: str,\\n172:def collect_python_files(repo_dir: str, pool_size: int = 0) -> list[dict]:\\n199:    def rank(\\n218:    def __init__(\\n263:    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:\\n280:    def rank(\\n295:def recall_at_k(predicted: list[str], gold: list[str], k: int) -> float:\\n302:def reciprocal_rank(predicted: list[str], gold: list[str]) -> float:\\n312:def load_completed(output_dir: str) -> set[str]:\\n326:def append_result(output_dir: str, result: InstanceResult):\\n334:def evaluate(args):\\n391:                cands.append({\\\"path\\\": gf, \\\"content\\\": f\\\"def fix(): pass  # {gf}\\\"})\\n448:def _write_summary(args, k_values: list[int]):\\n505:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T08:31:23.156612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -300 /root/structfuse/evaluation/eval_swebench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "head -300 /root/structfuse/evaluation/eval_swebench.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T08:31:23.156854+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"StructFuse SWE-bench Retrieval Evaluation.\\n\\nMeasures file-level retrieval quality of a trained StructFuse checkpoint on\\nSWE-bench Lite (300 instances) or Verified split.\\n\\nPer-instance pipeline:\\n  1. Clone/checkout target repo at base_commit\\n  2. Collect all Python files as candidate pool\\n  3. Encode issue text (query) and file contents (candidates) with StructFuse\\n  4. Rank candidates by cosine similarity\\n  5. Compare predicted top-k with gold patch files -> Recall@k, MRR\\n\\nOutputs (in --output-dir):\\n  per_instance_results.jsonl  per-instance ranked predictions and metrics\\n  summary.json                aggregate Recall@k, MRR, config\\n\\nUsage:\\n  # Full eval (requires GPU + trained checkpoint)\\n  python eval_swebench.py \\\\\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s42/best_by_recall_at_1 \\\\\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/qwen_best_recall\\n\\n  # Dry-run (no GPU, tests pipeline logic with mock embeddings)\\n  python eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5\\n\\nDependencies: transformers, torch, datasets, numpy, tqdm\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport subprocess\\nimport sys\\nimport time\\nfrom dataclasses import asdict, dataclass, field\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom tqdm import tqdm\\n\\n\\n# ── Data structures ─────────────────────────────────────────────────\\n\\n@dataclass\\nclass SWEInstance:\\n    instance_id: str\\n    repo: str\\n    base_commit: str\\n    problem_statement: str\\n    patch: str\\n    gold_files: list[str] = field(default_factory=list)\\n\\n\\n@dataclass\\nclass InstanceResult:\\n    instance_id: str\\n    repo: str\\n    gold_files: list[str]\\n    predicted_files: list[str]\\n    predicted_
…[truncated 7071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T08:31:23.157045+00:00_

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
  "session": "worker_code_eval_repobench_20260514T082145",
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

_source line 36 · 2026-05-14T08:31:23.157170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T08:31:23.157289+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tianyang/repobench-r', 'python_cff', split='test_easy', trust_remote_code=True)\nprint('Len:', len(ds))\nprint('Columns:', ds.column_names)\nex = ds[0]\nfor k, v in ex.items():\n    if isinstance(v, str):\n        print(f'  {k}: ({len(v)} chars) {v[:150]}')\n    elif isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if v and isinstance(v[0], str):\n            print(f'    first item ({len(v[0])} chars): {v[0][:100]}')\n    else:\n        print(f'  {k}: {v}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('tianyang/repobench-r', 'python_cff', split='test_easy', trust_remote_code=True)\nprint('Len:', len(ds))\nprint('Columns:', ds.column_names)\nex = ds[0]\nfor k, v in ex.items():\n    if isinstance(v, str):\n        print(f'  {k}: ({len(v)} chars) {v[:150]}')\n    elif isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if v and isinstance(v[0], str):\n            print(f'    first item ({len(v[0])} chars): {v[0][:100]}')\n    else:\n        print(f'  {k}: {v}')\n\"\n"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T08:31:23.157415+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp -type d -name \"best_by*\" -o -type d -name \"checkpoint*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp -type d -name \"best_by*\" -o -type d -name \"checkpoint*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T08:31:23.157569+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\\\\nfrom datasets import load_dataset\\\\nds = load_dataset(\\\\'tianyang/repobench-r\\\\', \\\\'python_cff\\\\', split=\\\\'test_easy\\\\', trust_remote_code=True)\\\\nprint(\\\\'Len:\\\\', len(ds))\\\\nprint(\\\\'Columns:\\\\', ds.column_names)\\\\nex = ds[0]\\\\nfor k, v in ex.items():\\\\n    if isinstance(v, str):\\\\n        print(f\\\\'  {k}: ({len(v)} chars) {v[:150]}\\\\')\\\\n    elif isinstance(v, list):\\\\n        print(f\\\\'  {k}: list of {len(v)} items\\\\')\\\\n        if v and isinstance(v[0], str):\\\\n            print(f\\\\'    first item ({len(v[0])} chars): {v[0][:100]}\\\\')\\\\n    else:\\\\n        print(f\\\\'  {k}: {v}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n\\nStderr:\\n\\n    builder_instance = load_dataset_builder(\\n                       ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1315, in load_dataset_builder\\n    dataset_module = dataset_module_factory(\\n                     ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1207, in dataset_module_factory\\n    raise e1 from None\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1167, in dataset_module_factory\\n    raise RuntimeError(f\\\"Dataset scripts are no longer supported, but found {filename}\\\")\\nRuntimeError: Dataset scripts are no longer supported, but found repobench-r.py\\n\\n\", \"metadata\": {\"elapsed_seconds\": 6.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T08:31:23.157743+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T08:31:23.157899+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport datasets\nprint('datasets version:', datasets.__version__)\n# Try with TRUST_REMOTE_CODE env var\nimport os\nos.environ['HF_DATASETS_TRUST_REMOTE_CODE'] = '1'\nds = datasets.load_dataset('tianyang/repobench-r', 'python_cff', split='test_easy', trust_remote_code=True)\nprint('Len:', len(ds))\nprint('Columns:', ds.column_names)\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport datasets\nprint('datasets version:', datasets.__version__)\n# Try with TRUST_REMOTE_CODE env var\nimport os\nos.environ['HF_DATASETS_TRUST_REMOTE_CODE'] = '1'\nds = datasets.load_dataset('tianyang/repobench-r', 'python_cff', split='test_easy', trust_remote_code=True)\nprint('Len:', len(ds))\nprint('Columns:', ds.column_names)\n\"\n"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T08:31:23.158026+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp -type d -name \"best_by*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp -type d -name \"best_by*\""
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T08:31:23.158176+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\\\\nimport datasets\\\\nprint(\\\\'datasets version:\\\\', datasets.__version__)\\\\n# Try with TRUST_REMOTE_CODE env var\\\\nimport os\\\\nos.environ[\\\\'HF_DATASETS_TRUST_REMOTE_CODE\\\\'] = \\\\'1\\\\'\\\\nds = datasets.load_dataset(\\\\'tianyang/repobench-r\\\\', \\\\'python_cff\\\\', split=\\\\'test_easy\\\\', trust_remote_code=True)\\\\nprint(\\\\'Len:\\\\', len(ds))\\\\nprint(\\\\'Columns:\\\\', ds.column_names)\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\ndatasets version: 4.8.4\\n\\nStderr:\\n\\n    builder_instance = load_dataset_builder(\\n                       ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1315, in load_dataset_builder\\n    dataset_module = dataset_module_factory(\\n                     ^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1207, in dataset_module_factory\\n    raise e1 from None\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/datasets/load.py\\\", line 1167, in dataset_module_factory\\n    raise RuntimeError(f\\\"Dataset scripts are no longer supported, but found {filename}\\\")\\nRuntimeError: Dataset scripts are no longer supported, but found repobench-r.py\\n\\n\", \"metadata\": {\"elapsed_seconds\": 10.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T08:31:23.158325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T08:31:23.158483+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom datasets import load_dataset\n# Try v1.1 which may have native parquet\nds = load_dataset('tianyang/repobench_python_v1.1', trust_remote_code=True)\nprint('Keys:', list(ds.keys()))\nfor k in ds:\n    print(f'{k}: {len(ds[k])} rows, cols={ds[k].column_names}')\n    ex = ds[k][0]\n    for field, val in ex.items():\n        if isinstance(val, str):\n            print(f'  {field}: str({len(val)})')\n        elif isinstance(val, list):\n            print(f'  {field}: list({len(val)})')\n        else:\n            print(f'  {field}: {type(val).__name__} = {val}')\n    break\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom datasets import load_dataset\n# Try v1.1 which may have native parquet\nds = load_dataset('tianyang/repobench_python_v1.1', trust_remote_code=True)\nprint('Keys:', list(ds.keys()))\nfor k in ds:\n    print(f'{k}: {len(ds[k])} rows, cols={ds[k].column_names}')\n    ex = ds[k][0]\n    for field, val in ex.items():\n        if isinstance(val, str):\n            print(f'  {field}: str({len(val)})')\n        elif isinstance(val, list):\n            print(f'  {field}: list({len(val)})')\n        else:\n            print(f'  {field}: {type(val).__name__} = {val}')\n    break\n\"\n"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T08:31:23.158634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "tianyang repobench-r huggingface parquet data files format 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "tool_args": {
    "query": "tianyang repobench-r huggingface parquet data files format 2025"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T08:31:23.158795+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\\\\nfrom datasets import load_dataset\\\\n# Try v1.1 which may have native parquet\\\\nds = load_dataset(\\\\'tianyang/repobench_python_v1.1\\\\', trust_remote_code=True)\\\\nprint(\\\\'Keys:\\\\', list(ds.keys()))\\\\nfor k in ds:\\\\n    print(f\\\\'{k}: {len(ds[k])} rows, cols={ds[k].column_names}\\\\')\\\\n    ex = ds[k][0]\\\\n    for field, val in ex.items():\\\\n        if isinstance(val, str):\\\\n            print(f\\\\'  {field}: str({len(val)})\\\\')\\\\n        elif isinstance(val, list):\\\\n            print(f\\\\'  {field}: list({len(val)})\\\\')\\\\n        else:\\\\n            print(f\\\\'  {field}: {type(val).__name__} = {val}\\\\')\\\\n    break\\\\n\\\"\\\\n'\\n\\nStdout:\\n\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n\\nStderr:\\n\\n`trust_remote_code` is not supported anymore.\\nPlease check that the Hugging Face dataset 'tianyang/repobench_python_v1.1' isn't based on a loading script and remove `trust_remote_code`.\\nIf the dataset is based on a loading script, please ask the dataset author to remove it and convert it to a standard format like Parquet.\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T08:31:23.158964+00:00_

Web search results for query: "tianyang repobench-r huggingface parquet data files format 2025"

Links: [{"title":"tianyang/repobench-r · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-r"},{"title":"tianyang/repobench-c · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-c"},{"title":"tianyang/repobench_python_v1.1 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_python_v1.1"},{"title":"tianyang/repobench_java_v1.1 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_java_v1.1"},{"title":"repobench-r.py · tianyang/repobench-r at e6d80b14226f09bfd7817d2ee7591cfe372f1f5f","url":"https://huggingface.co/datasets/tianyang/repobench-r/blame/e6d80b14226f09bfd7817d2ee7591cfe372f1f5f/repobench-r.py"},{"title":"tianyang/repobench-p · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench-p"},{"title":"README.md · tianyang/repobench-r at 93c340aca9c02afd23f3c70087433af1c154ccfc","url":"https://huggingface.co/datasets/tianyang/repobench-r/blob/93c340aca9c02afd23f3c70087433af1c154ccfc/README.md"},{"title":"README.md · tianyang/repobench_python_v1.1 at 8a7cf0c8942cc1aa066bf261839650ac55a2ff79","url":"https://huggingface.co/datasets/tianyang/repobench_python_v1.1/blob/8a7cf0c8942cc1aa066bf261839650ac55a2ff79/README.md"},{"title":"tianyang/repobench_ablation_8k · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_ablation_8k"},{"title":"tianyang/repobench_raw_v1.1 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tianyang/repobench_raw_v1.1"}]

Based on the search results, here's information about the tianyang repobench-r dataset on Hugging Face:

## Dataset Overview

RepoBench-R (Retrieval) is a subtask of RepoBench targeting the retrieval component of a repository-level auto-completion system, focusing on retrieving the most relevant code snippet from a project re
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T08:31:23.159145+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom huggingface_hub import HfApi\napi = HfApi()\nfiles = api.list_repo_files('tianyang/repobench-r', repo_type='dataset')\nfor f in files:\n    print(f)\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom huggingface_hub import HfApi\napi = HfApi()\nfiles = api.list_repo_files('tianyang/repobench-r', repo_type='dataset')\nfor f in files:\n    print(f)\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T08:31:23.159284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n.gitattributes\\nREADME.md\\ndata/java_cff.gz\\ndata/java_cfr.gz\\ndata/python_cff.gz\\ndata/python_cfr.gz\\nrepobench-r.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T08:31:23.159438+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom huggingface_hub import hf_hub_download\n# Download the loading script to see the format\npath = hf_hub_download('tianyang/repobench-r', 'repobench-r.py', repo_type='dataset')\nwith open(path) as f:\n    print(f.read())\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nfrom huggingface_hub import hf_hub_download\n# Download the loading script to see the format\npath = hf_hub_download('tianyang/repobench-r', 'repobench-r.py', repo_type='dataset')\nwith open(path) as f:\n    print(f.read())\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T08:31:23.159708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.\\n#\\n# Licensed under the Apache License, Version 2.0 (the \\\"License\\\");\\n# you may not use this file except in compliance with the License.\\n# You may obtain a copy of the License at\\n#\\n#     http://www.apache.org/licenses/LICENSE-2.0\\n#\\n# Unless required by applicable law or agreed to in writing, software\\n# distributed under the License is distributed on an \\\"AS IS\\\" BASIS,\\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\\n# See the License for the specific language governing permissions and\\n# limitations under the License.\\n\\n\\\"\\\"\\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\\"\\\"\\n\\nimport gzip\\nimport pickle\\nimport textwrap\\nimport datasets\\n\\n_CITATION = \\\"\\\"\\\"\\\\\\n@misc{liu2023repobench,\\n      title={RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems}, \\n      author={Tianyang Liu and Canwen Xu and Julian McAuley},\\n      year={2023},\\n      eprint={2306.03091},\\n      archivePrefix={arXiv},\\n      primaryClass={cs.CL}\\n}\\n\\\"\\\"\\\"\\n\\n_DESCRIPTION = \\\"\\\"\\\"\\\\\\nRepoBench is a dataset that benchmarks repository-level code auto-completion systems.\\n\\nRepoBench-R denotes RepoBench for Retrieval, which is a sub-task of RepoBench, \\naiming to evaluate the ability of code auto-completion systems to retrieve \\nrelevant code snippets for next-line code completion.\\n\\\"\\\"\\\"\\n\\n_HOMEPAGE = \\\"https://github.com/Leolty/repobench\\\"\\n\\n_LICENSE = \\\"Apache License 2.0\\\"\\n\\n_URLs = {\\n    \\\"java_cff\\\": \\\"https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/java_cff.gz\\\",\\n    \\\"java_cfr\\\": \\\"https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/java_cfr.gz\\\
…[truncated 4539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T08:31:23.159944+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport gzip, pickle\nfrom huggingface_hub import hf_hub_download\n\npath = hf_hub_download('tianyang/repobench-r', 'data/python_cff.gz', repo_type='dataset')\nwith gzip.open(path, 'rb') as f:\n    data = pickle.load(f)\n\nprint('Top keys:', list(data.keys()))\nfor subset in data:\n    print(f'{subset}:')\n    for level in data[subset]:\n        examples = data[subset][level]\n        print(f'  {level}: {len(examples)} examples')\n        if examples:\n            ex = examples[0]\n            print(f'    fields: {list(ex.keys())}')\n            print(f'    context length: {len(ex[\\\"context\\\"])}')\n            print(f'    golden_snippet_index: {ex[\\\"golden_snippet_index\\\"]}')\n            print(f'    code snippet: {ex[\\\"code\\\"][:100]}')\n            print(f'    import_statement: {ex[\\\"import_statement\\\"][:100]}')\n            # Check pool sizes across examples\n            pool_sizes = [len(e['context']) for e in examples[:100]]\n            print(f'    pool sizes (first 100): min={min(pool_sizes)}, max={max(pool_sizes)}, mean={sum(pool_sizes)/len(pool_sizes):.1f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport gzip, pickle\nfrom huggingface_hub import hf_hub_download\n\npath = hf_hub_download('tianyang/repobench-r', 'data/python_cff.gz', repo_type='dataset')\nwith gzip.open(path, 'rb') as f:\n    data = pickle.load(f)\n\nprint('Top keys:', list(data.keys()))\nfor subset in data:\n    print(f'{subset}:')\n    for level in data[subset]:\n        examples = data[subset][level]\n        print(f'  {level}: {len(examples)} examples')\n        if examples:\n            ex = examples[0]\n            print(f'    fields: {list(ex.keys())}')\n            print(f'    context length: {len(ex[\\\"context\\\"])}')\n            print(f'    golden_snippet_index: {ex[\\\"golden_snippet_index\\\"]}')\n            print(f'    code snippet: {ex[\\\"code\\\"][:100]}')\n            print(f'    import_statement: {ex[\\\"import_statement\\\"][:100]}')\n            # Check pool sizes across examples\n            pool_sizes = [len(e['context']) for e in examples[:100]]\n            print(f'    pool sizes (first 100): min={min(pool_sizes)}, max={max(pool_sizes)}, mean={sum(pool_sizes)/len(pool_sizes):.1f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T08:31:23.160171+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \\\"\\\\nimport gzip, pickle\\\\nfrom huggingface_hub import hf_hub_download\\\\n\\\\npath = hf_hub_download(\\\\'tianyang/repobench-r\\\\', \\\\'data/python_cff.gz\\\\', repo_type=\\\\'dataset\\\\')\\\\nwith gzip.open(path, \\\\'rb\\\\') as f:\\\\n    data = pickle.load(f)\\\\n\\\\nprint(\\\\'Top keys:\\\\', list(data.keys()))\\\\nfor subset in data:\\\\n    print(f\\\\'{subset}:\\\\')\\\\n    for level in data[subset]:\\\\n        examples = data[subset][level]\\\\n        print(f\\\\'  {level}: {len(examples)} examples\\\\')\\\\n        if examples:\\\\n            ex = examples[0]\\\\n            print(f\\\\'    fields: {list(ex.keys())}\\\\')\\\\n            print(f\\\\'    context length: {len(ex[\\\\\\\\\\\"context\\\\\\\\\\\"])}\\\\')\\\\n            print(f\\\\'    golden_snippet_index: {ex[\\\\\\\\\\\"golden_snippet_index\\\\\\\\\\\"]}\\\\')\\\\n            print(f\\\\'    code snippet: {ex[\\\\\\\\\\\"code\\\\\\\\\\\"][:100]}\\\\')\\\\n            print(f\\\\'    import_statement: {ex[\\\\\\\\\\\"import_statement\\\\\\\\\\\"][:100]}\\\\')\\\\n            # Check pool sizes across examples\\\\n            pool_sizes = [len(e[\\\\'context\\\\']) for e in examples[:100]]\\\\n            print(f\\\\'    pool sizes (first 100): min={min(pool_sizes)}, max={max(pool_sizes)}, mean={sum(pool_sizes)/len(pool_sizes):.1f}\\\\')\\\\n\\\"\\\\n'\\n\\nStdout:\\n\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T08:31:23.160366+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && nohup python3 -c \"\nfrom huggingface_hub import hf_hub_download\npath = hf_hub_download('tianyang/repobench-r', 'data/python_cff.gz', repo_type='dataset')\nprint('Downloaded to:', path)\npath2 = hf_hub_download('tianyang/repobench-r', 'data/python_cfr.gz', repo_type='dataset')\nprint('Downloaded to:', path2)\n\" > /tmp/repobench_download.log 2>&1 &\necho \"PID: $!\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && nohup python3 -c \"\nfrom huggingface_hub import hf_hub_download\npath = hf_hub_download('tianyang/repobench-r', 'data/python_cff.gz', repo_type='dataset')\nprint('Downloaded to:', path)\npath2 = hf_hub_download('tianyang/repobench-r', 'data/python_cfr.gz', repo_type='dataset')\nprint('Downloaded to:', path2)\n\" > /tmp/repobench_download.log 2>&1 &\necho \"PID: $!\"\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T08:31:23.160523+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && nohup python3 -c \\\"\\\\nfrom huggingface_hub import hf_hub_download\\\\npath = hf_hub_download(\\\\'tianyang/repobench-r\\\\', \\\\'data/python_cff.gz\\\\', repo_type=\\\\'dataset\\\\')\\\\nprint(\\\\'Downloaded to:\\\\', path)\\\\npath2 = hf_hub_download(\\\\'tianyang/repobench-r\\\\', \\\\'data/python_cfr.gz\\\\', repo_type=\\\\'dataset\\\\')\\\\nprint(\\\\'Downloaded to:\\\\', path2)\\\\n\\\" > /tmp/repobench_download.log 2>&1 &\\\\necho \\\"PID: $!\\\"\\\\n'\\n\\nStdout:\\n\\nPID: 960224\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T08:31:23.160734+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /tmp/repobench_download.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /tmp/repobench_download.log"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T08:31:23.160879+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"'(ReadTimeoutError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Read timed out. (read timeout=10)\\\"), '(Request ID: 63ed1da9-d2e9-4556-b6f7-b589f2346ca4)')' thrown while requesting HEAD https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz\\nRetrying in 1s [Retry 1/5].\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T08:31:23.161045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T08:31:23.161175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"added_tokens.json\\nchat_template.jinja\\nmerges.txt\\nmodel.pt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T08:31:23.161294+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T08:31:23.161437+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n  \\\"train_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/train_random_s42.jsonl\\\",\\n  \\\"val_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\\",\\n  \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\\",\\n  \\\"batch_size\\\": 8,\\n  \\\"learning_rate\\\": 2e-05,\\n  \\\"num_epochs\\\": 3,\\n  \\\"warmup_ratio\\\": 0.1,\\n  \\\"num_negatives\\\": 7,\\n  \\\"hard_negative_strategy\\\": \\\"random\\\",\\n  \\\"hard_negative_ratio\\\": 0.5,\\n  \\\"temperature\\\": 0.07,\\n  \\\"pos_weight_alpha\\\": 1.0,\\n  \\\"use_fusion_head\\\": false,\\n  \\\"use_lora\\\": true,\\n  \\\"lora_r\\\": 16,\\n  \\\"proj_dim\\\": 256,\\n  \\\"gradient_checkpointing\\\": true,\\n  \\\"eval_steps\\\": 500,\\n  \\\"save_steps\\\": 1000,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 42,\\n  \\\"wandb_project\\\": \\\"structfuse\\\",\\n  \\\"wandb_run_name\\\": \\\"m2_full_random_s42\\\",\\n  \\\"dataflow_graph_file\\\": null,\\n  \\\"embeddings_file\\\": null,\\n  \\\"dynamic_mining\\\": false,\\n  \\\"candidate_pool_file\\\": null,\\n  \\\"early_stopping_patience\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T08:31:23.161678+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py",
  "content": "#!/usr/bin/env python3\n\"\"\"StructFuse RepoBench-R Retrieval Evaluation.\n\nEvaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool\ncross-file code retrieval benchmark.  Each instance contains a query\n(import_statement + code context) and a candidate pool (context list);\nthe task is to rank candidates so the gold snippet appears near the top.\n\nDataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)\nSubsets: python_cff, python_cfr, java_cff, java_cfr\nSplits:  train_easy, train_hard, test_easy, test_hard\n\nOutputs (in --output-dir):\n  per_instance_results.jsonl   one JSON object per instance\n  summary.json                 aggregate Recall@1/5/10, MRR, config\n\nUsage:\n  # Dry-run (no GPU, validates pipeline end-to-end)\n  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20\n\n  # Full eval with trained checkpoint\n  python eval_repobench.py \\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \\\n      --subset python_cff --split test_easy\n\nDependencies: torch, transformers, numpy, tqdm, huggingface_hub\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport gzip\nimport json\nimport os\nimport pickle\nimport sys\nimport time\nfrom dataclasses import asdict, dataclass, field\nfrom pathlib import Path\n\nimport numpy as np\nfrom tqdm import tqdm\n\n\n# ── Data structures ─────────────────────────────────────────────────\n\n@dataclass\nclass RepoBenchInstance:\n    instance_id: str\n    repo_name: str\n    file_path: str\n    import_statement: str\n    code: str\n    next_line: str\n    context: list[str]\n    gold_snippet_index: int\n\n\n@dataclass\nclass InstanceResult:\n    instance_id: str\n    repo_name: str\n    gold_index: int\n    pool_size: int\n    predicted_ranking: list[int]       # indices into context, ranked by score\n    predicted_scores: list[float]      # corresponding scores\n    recall: dict[str, float]           # {\"@1\": 0/1, \"@5\": ..., \"@10\": ...}\n    reciprocal_rank: float\n    error: str = \"\"\n\n\n# ── Data loading ────────────────────────────────────────────────────\n\n_URLS = {\n    \"java_cff\":   \"data/java_cff.gz\",\n    \"java_cfr\":   \"data/java_cfr.gz\",\n    \"python_cff\": \"data/python_cff.gz\",\n    \"python_cfr\": \"data/python_cfr.gz\",\n}\n\n\ndef load_repobench(\n    subset: str,\n    split: str,\n    cache_dir: str = \"\",\n) -> list[RepoBenchInstance]:\n    \"\"\"Download and parse RepoBench-R data via huggingface_hub.\"\"\"\n    from huggingface_hub import hf_hub_download\n\n    if subset not in _URLS:\n        raise ValueError(f\"Unknown subset '{subset}', choose from {list(_URLS.keys())}\")\n\n    parts = split.split(\"_\")\n    if len(parts) != 2 or parts[0] not in (\"train\", \"test\") or parts[1] not in (\"easy\", \"hard\"):\n        raise ValueError(f\"Invalid split '{split}', use train_easy/train_hard/test_easy/test_hard\")\n\n    kwargs = {}\n    if cache_dir:\n        kwargs[\"cache_dir\"] = cache_dir\n\n    print(f\"Downloading tianyang/repobench-r/{_URLS[subset]} ...\")\n    gz_path = hf_hub_download(\n        \"tianyang/repobench-r\", _URLS[subset], repo_type=\"dataset\", **kwargs\n    )\n\n    print(f\"Loading pickle from {gz_path} ...\")\n    with gzip.open(gz_path, \"rb\") as f:\n        data = pickle.load(f)\n\n    subset_key, level = parts[0], parts[1]\n    raw = data[subset_key][level]\n    print(f\"  {subset}/{split}: {len(raw)} examples\")\n\n    instances = []\n    for i, ex in enumerate(raw):\n        instances.append(RepoBenchInstance(\n            instance_id=f\"{subset}_{split}_{i:05d}\",\n            repo_name=ex[\"repo_name\"],\n            file_path=ex[\"file_path\"],\n            import_statement=ex[\"import_statement\"],\n            code=ex[\"code\"],\n            next_line=ex[\"next_line\"],\n            context=ex[\"context\"],\n            gold_snippet_index=ex[\"golden_snippet_index\"],\n        ))\n    return instances\n\n\ndef _mock_repobench(num_instances: int, pool_size: int = 10) -> list[RepoBenchInstance]:\n    \"\"\"Generate synthetic instances for dry-run testing.\"\"\"\n    rng = np.random.default_rng(42)\n    instances = []\n    for i in range(num_instances):\n        gold_idx = int(rng.integers(0, pool_size))\n        context = [\n            f\"def helper_{i}_{j}():\\n    return {j}\\n\" for j in range(pool_size)\n        ]\n        instances.append(RepoBenchInstance(\n            instance_id=f\"mock_{i:05d}\",\n            repo_name=f\"mock/repo_{i % 3}\",\n            file_path=f\"src/module_{i}.py\",\n            import_statement=f\"from helpers import helper_{i}_{gold_idx}\",\n            code=f\"def main():\\n    result = helper_{i}_{gold_idx}()\\n\",\n            next_line=f\"    print(result)\",\n            context=context,\n            gold_snippet_index=gold_idx,\n        ))\n    return instances\n\n\n# ── Retrievers ──────────────────────────────────────────────────────\n\nclass MockRetriever:\n    \"\"\"Random-score retriever for dry-run validation.\"\"\"\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        \"\"\"Return (ranked_indices, scores) with deterministic random scores.\"\"\"\n        if not candidates:\n            return [], []\n        rng = np.random.default_rng(hash(query) % (2**31))\n        scores = rng.random(len(candidates)).astype(float)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\nclass StructFuseRetriever:\n    \"\"\"Bi-encoder retriever using a trained StructFuse checkpoint.\"\"\"\n\n    def __init__(\n        self,\n        checkpoint_path: str,\n        model_name: str | None = None,\n        max_seq_length: int = 2048,\n        device: str = \"cuda\",\n    ):\n        import torch\n        from transformers import AutoTokenizer\n\n        train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"..\", \"training\"\n        )\n        # Also try sibling directory layout\n        alt_train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"training\"\n        )\n        for d in [train_dir, alt_train_dir]:\n            if d not in sys.path and os.path.isdir(d):\n                sys.path.insert(0, d)\n        from contrastive_model import StructFuseEncoder\n\n        self._torch = torch\n        self.device = torch.device(device if torch.cuda.is_available() else \"cpu\")\n        self.max_seq_length = max_seq_length\n\n        with open(os.path.join(checkpoint_path, \"training_config.json\")) as f:\n            cfg = json.load(f)\n\n        base_model = model_name or cfg.get(\"model_name\", \"Qwen/Qwen2.5-Coder-3B\")\n        self.tokenizer = AutoTokenizer.from_pretrained(\n            checkpoint_path, trust_remote_code=True\n        )\n        self.model = StructFuseEncoder(\n            model_name=base_model,\n            proj_dim=cfg.get(\"proj_dim\", 256),\n            use_projection=True,\n            use_lora=cfg.get(\"use_lora\", False),\n            lora_r=cfg.get(\"lora_r\", 16),\n            lora_alpha=cfg.get(\"lora_alpha\", 32),\n            use_fusion_head=cfg.get(\"use_fusion_head\", False),\n        )\n        sd = torch.load(\n            os.path.join(checkpoint_path, \"model.pt\"),\n            map_location=\"cpu\",\n            weights_only=True,\n        )\n        self.model.load_state_dict(sd)\n        self.model.to(self.device).eval()\n        print(f\"Loaded StructFuse from {checkpoint_path} on {self.device}\")\n\n    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:\n        torch = self._torch\n        parts: list[np.ndarray] = []\n        for i in range(0, len(texts), batch_size):\n            batch = texts[i : i + batch_size]\n            enc = self.tokenizer(\n                batch,\n                padding=True,\n                truncation=True,\n                max_length=self.max_seq_length,\n                return_tensors=\"pt\",\n            ).to(self.device)\n            with torch.no_grad():\n                emb = self.model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            parts.append(emb.cpu().numpy())\n        return np.concatenate(parts, axis=0)\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        \"\"\"Rank candidates by cosine similarity to query. Returns (indices, scores).\"\"\"\n        if not candidates:\n            return [], []\n        q = self._encode([query], batch_size=1)\n        # Truncate very long snippets for encoding\n        docs = [c[:12000] for c in candidates]\n        d = self._encode(docs, batch_size=batch_size)\n        scores = (q @ d.T).squeeze(0)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\n# ── Metrics ─────────────────────────────────────────────────────────\n\ndef recall_at_k(predicted_indices: list[int], gold_index: int, k: int) -> float:\n    return 1.0 if gold_index in predicted_indices[:k] else 0.0\n\n\ndef reciprocal_rank(predicted_indices: list[int], gold_index: int) -> float:\n    for rank, idx in enumerate(predicted_indices, start=1):\n        if idx == gold_index:\n            return 1.0 / rank\n    return 0.0\n\n\n# ── Resume helpers ──────────────────────────────────────────────────\n\ndef load_completed(output_dir: str) -> set[str]:\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    done = set()\n    if os.path.exists(path):\n        with open(path) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        obj = json.loads(line)\n                        done.add(obj[\"instance_id\"])\n                    except (json.JSONDecodeError, KeyError):\n                        pass\n    return done\n\n\ndef append_result(output_dir: str, result: InstanceResult):\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    with open(path, \"a\") as f:\n        f.write(json.dumps(asdict(result), ensure_ascii=False) + \"\\n\")\n\n\n# ── Query construction ──────────────────────────────────────────────\n\ndef build_query(inst: RepoBenchInstance) -> str:\n    \"\"\"Build the query text from import_statement + code context.\"\"\"\n    parts = []\n    if inst.import_statement.strip():\n        parts.append(inst.import_statement.strip())\n    if inst.code.strip():\n        parts.append(inst.code.strip())\n    return \"\\n\".join(parts)\n\n\n# ── Main evaluation ─────────────────────────────────────────────────\n\ndef evaluate(args):\n    k_values = [int(k) for k in args.top_k.split(\",\")]\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Load data\n    if args.dry_run:\n        limit = args.limit if args.limit > 0 else 50\n        try:\n            instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n            if limit > 0:\n                instances = instances[:limit]\n            print(f\"Dry-run: loaded {len(instances)} real instances\")\n        except Exception as e:\n            print(f\"Could not load HF dataset ({e}), using mock data\")\n            instances = _mock_repobench(limit)\n    else:\n        instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n        if args.limit > 0:\n            instances = instances[:args.limit]\n\n    print(f\"Evaluating {len(instances)} instances, subset={args.subset}, split={args.split}\")\n    pool_sizes = [len(inst.context) for inst in instances]\n    print(f\"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, \"\n          f\"mean={np.mean(pool_sizes):.1f}\")\n\n    # 2. Initialize retriever\n    if args.dry_run:\n        retriever = MockRetriever()\n    else:\n        retriever = StructFuseRetriever(\n            checkpoint_path=args.checkpoint_path,\n            model_name=args.model_name,\n            max_seq_length=args.max_seq_length,\n            device=args.device,\n        )\n\n    # 3. Resume support\n    completed = load_completed(args.output_dir)\n    if completed:\n        print(f\"Resuming: {len(completed)} already done, \"\n              f\"{len(instances) - len(completed)} remaining\")\n\n    # 4. Evaluate each instance\n    for inst in tqdm(instances, desc=\"RepoBench-R eval\"):\n        if inst.instance_id in completed:\n            continue\n\n        try:\n            query = build_query(inst)\n            ranked_indices, scores = retriever.rank(\n                query, inst.context, batch_size=args.batch_size\n            )\n\n            rec = {}\n            for k in k_values:\n                rec[f\"@{k}\"] = recall_at_k(ranked_indices, inst.gold_snippet_index, k)\n            rr = reciprocal_rank(ranked_indices, inst.gold_snippet_index)\n\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=ranked_indices[:20],\n                predicted_scores=scores[:20],\n                recall=rec,\n                reciprocal_rank=round(rr, 6),\n            )\n        except Exception as e:\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=[],\n                predicted_scores=[],\n                recall={f\"@{k}\": 0.0 for k in k_values},\n                reciprocal_rank=0.0,\n                error=str(e),\n            )\n\n        append_result(args.output_dir, result)\n\n    # 5. Write summary\n    _write_summary(args, k_values)\n\n\ndef _write_summary(args, k_values: list[int]):\n    \"\"\"Recompute aggregate metrics from all per-instance results.\"\"\"\n    all_results = []\n    rpath = os.path.join(args.output_dir, \"per_instance_results.jsonl\")\n    if os.path.exists(rpath):\n        with open(rpath) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        all_results.append(json.loads(line))\n                    except json.JSONDecodeError:\n                        pass\n\n    valid = [r for r in all_results if not r.get(\"error\")]\n    summary: dict = {\n        \"config\": {\n            \"checkpoint_path\": args.checkpoint_path,\n            \"subset\": args.subset,\n            \"split\": args.split,\n            \"top_k\": k_values,\n            \"dry_run\": args.dry_run,\n            \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        },\n        \"total_instances\": len(all_results),\n        \"valid_instances\": len(valid),\n        \"errors\": len(all_results) - len(valid),\n    }\n\n    # Pool size stats\n    pool_sizes = [r.get(\"pool_size\", 0) for r in valid]\n    if pool_sizes:\n        summary[\"pool_size_mean\"] = round(float(np.mean(pool_sizes)), 1)\n        summary[\"pool_size_min\"] = min(pool_sizes)\n        summary[\"pool_size_max\"] = max(pool_sizes)\n        # Theoretical chance level\n        summary[\"chance_recall_at_1\"] = round(1.0 / np.mean(pool_sizes), 4)\n\n    for k in k_values:\n        vals = [r[\"recall\"].get(f\"@{k}\", 0.0) for r in valid]\n        summary[f\"recall@{k}\"] = round(float(np.mean(vals)), 4) if vals else 0.0\n\n    mrr_vals = [r.get(\"reciprocal_rank\", 0.0) for r in valid]\n    summary[\"mrr\"] = round(float(np.mean(mrr_vals)), 4) if mrr_vals else 0.0\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Instances: {len(all_results)} total, {len(valid)} valid, \"\n          f\"{len(all_results) - len(valid)} errors\")\n    if pool_sizes:\n        print(f\"  Pool size: mean={summary['pool_size_mean']}, \"\n              f\"min={summary['pool_size_min']}, max={summary['pool_size_max']}\")\n        print(f\"  Chance Recall@1: {summary['chance_recall_at_1']:.4f}\")\n    for k in k_values:\n        print(f\"  Recall@{k:>2d}: {summary[f'recall@{k}']:.4f}\")\n    print(f\"  MRR:       {summary['mrr']:.4f}\")\n    print(f\"\\nResults: {args.output_dir}/\")\n\n\n# ── CLI ─────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"StructFuse RepoBench-R retrieval evaluation\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    p.add_argument(\n        \"--checkpoint-path\", default=\"mock\",\n        help='Checkpoint dir (model.pt + training_config.json), or \"mock\" for dry-run',\n    )\n    p.add_argument(\"--model-name\", default=None,\n                    help=\"Override base model name (default: from training_config.json)\")\n    p.add_argument(\"--subset\", default=\"python_cff\",\n                    choices=list(_URLS.keys()),\n                    help=\"RepoBench-R subset (default: python_cff)\")\n    p.add_argument(\"--split\", default=\"test_easy\",\n                    help=\"Split to evaluate: train_easy/train_hard/test_easy/test_hard\")\n    p.add_argument(\"--output-dir\", default=\"repobench_eval_results\")\n    p.add_argument(\"--top-k\", default=\"1,5,10\",\n                    help=\"Comma-separated k values for Recall@k (default: 1,5,10)\")\n    p.add_argument(\"--batch-size\", type=int, default=32)\n    p.add_argument(\"--max-seq-length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda\")\n    p.add_argument(\"--limit\", type=int, default=0,\n                    help=\"Max instances to evaluate, 0 = all\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                    help=\"Mock retriever (random scores), no GPU needed\")\n    p.add_argument(\"--cache-dir\", default=\"\",\n                    help=\"HuggingFace cache dir for dataset downloads\")\n    args = p.parse_args()\n    evaluate(args)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py",
    "content": "#!/usr/bin/env python3\n\"\"\"StructFuse RepoBench-R Retrieval Evaluation.\n\nEvaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool\ncross-file code retrieval benchmark.  Each instance contains a query\n(import_statement + code context) and a candidate pool (context list);\nthe task is to rank candidates so the gold snippet appears near the top.\n\nDataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)\nSubsets: python_cff, python_cfr, java_cff, java_cfr\nSplits:  train_easy, train_hard, test_easy, test_hard\n\nOutputs (in --output-dir):\n  per_instance_results.jsonl   one JSON object per instance\n  summary.json                 aggregate Recall@1/5/10, MRR, config\n\nUsage:\n  # Dry-run (no GPU, validates pipeline end-to-end)\n  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20\n\n  # Full eval with trained checkpoint\n  python eval_repobench.py \\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \\\n      --subset python_cff --split test_easy\n\nDependencies: torch, transformers, numpy, tqdm, huggingface_hub\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport gzip\nimport json\nimport os\nimport pickle\nimport sys\nimport time\nfrom dataclasses import asdict, dataclass, field\nfrom pathlib import Path\n\nimport numpy as np\nfrom tqdm import tqdm\n\n\n# ── Data structures ─────────────────────────────────────────────────\n\n@dataclass\nclass RepoBenchInstance:\n    instance_id: str\n    repo_name: str\n    file_path: str\n    import_statement: str\n    code: str\n    next_line: str\n    context: list[str]\n    gold_snippet_index: int\n\n\n@dataclass\nclass InstanceResult:\n    instance_id: str\n    repo_name: str\n    gold_index: int\n    pool_size: int\n    predicted_ranking: list[int]       # indices into context, ranked by score\n    predicted_scores: list[float]      # corresponding scores\n    recall: dict[str, float]           # {\"@1\": 0/1, \"@5\": ..., \"@10\": ...}\n    reciprocal_rank: float\n    error: str = \"\"\n\n\n# ── Data loading ────────────────────────────────────────────────────\n\n_URLS = {\n    \"java_cff\":   \"data/java_cff.gz\",\n    \"java_cfr\":   \"data/java_cfr.gz\",\n    \"python_cff\": \"data/python_cff.gz\",\n    \"python_cfr\": \"data/python_cfr.gz\",\n}\n\n\ndef load_repobench(\n    subset: str,\n    split: str,\n    cache_dir: str = \"\",\n) -> list[RepoBenchInstance]:\n    \"\"\"Download and parse RepoBench-R data via huggingface_hub.\"\"\"\n    from huggingface_hub import hf_hub_download\n\n    if subset not in _URLS:\n        raise ValueError(f\"Unknown subset '{subset}', choose from {list(_URLS.keys())}\")\n\n    parts = split.split(\"_\")\n    if len(parts) != 2 or parts[0] not in (\"train\", \"test\") or parts[1] not in (\"easy\", \"hard\"):\n        raise ValueError(f\"Invalid split '{split}', use train_easy/train_hard/test_easy/test_hard\")\n\n    kwargs = {}\n    if cache_dir:\n        kwargs[\"cache_dir\"] = cache_dir\n\n    print(f\"Downloading tianyang/repobench-r/{_URLS[subset]} ...\")\n    gz_path = hf_hub_download(\n        \"tianyang/repobench-r\", _URLS[subset], repo_type=\"dataset\", **kwargs\n    )\n\n    print(f\"Loading pickle from {gz_path} ...\")\n    with gzip.open(gz_path, \"rb\") as f:\n        data = pickle.load(f)\n\n    subset_key, level = parts[0], parts[1]\n    raw = data[subset_key][level]\n    print(f\"  {subset}/{split}: {len(raw)} examples\")\n\n    instances = []\n    for i, ex in enumerate(raw):\n        instances.append(RepoBenchInstance(\n            instance_id=f\"{subset}_{split}_{i:05d}\",\n            repo_name=ex[\"repo_name\"],\n            file_path=ex[\"file_path\"],\n            import_statement=ex[\"import_statement\"],\n            code=ex[\"code\"],\n            next_line=ex[\"next_line\"],\n            context=ex[\"context\"],\n            gold_snippet_index=ex[\"golden_snippet_index\"],\n        ))\n    return instances\n\n\ndef _mock_repobench(num_instances: int, pool_size: int = 10) -> list[RepoBenchInstance]:\n    \"\"\"Generate synthetic instances for dry-run testing.\"\"\"\n    rng = np.random.default_rng(42)\n    instances = []\n    for i in range(num_instances):\n        gold_idx = int(rng.integers(0, pool_size))\n        context = [\n            f\"def helper_{i}_{j}():\\n    return {j}\\n\" for j in range(pool_size)\n        ]\n        instances.append(RepoBenchInstance(\n            instance_id=f\"mock_{i:05d}\",\n            repo_name=f\"mock/repo_{i % 3}\",\n            file_path=f\"src/module_{i}.py\",\n            import_statement=f\"from helpers import helper_{i}_{gold_idx}\",\n            code=f\"def main():\\n    result = helper_{i}_{gold_idx}()\\n\",\n            next_line=f\"    print(result)\",\n            context=context,\n            gold_snippet_index=gold_idx,\n        ))\n    return instances\n\n\n# ── Retrievers ──────────────────────────────────────────────────────\n\nclass MockRetriever:\n    \"\"\"Random-score retriever for dry-run validation.\"\"\"\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        \"\"\"Return (ranked_indices, scores) with deterministic random scores.\"\"\"\n        if not candidates:\n            return [], []\n        rng = np.random.default_rng(hash(query) % (2**31))\n        scores = rng.random(len(candidates)).astype(float)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\nclass StructFuseRetriever:\n    \"\"\"Bi-encoder retriever using a trained StructFuse checkpoint.\"\"\"\n\n    def __init__(\n        self,\n        checkpoint_path: str,\n        model_name: str | None = None,\n        max_seq_length: int = 2048,\n        device: str = \"cuda\",\n    ):\n        import torch\n        from transformers import AutoTokenizer\n\n        train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"..\", \"training\"\n        )\n        # Also try sibling directory layout\n        alt_train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"training\"\n        )\n        for d in [train_dir, alt_train_dir]:\n            if d not in sys.path and os.path.isdir(d):\n                sys.path.insert(0, d)\n        from contrastive_model import StructFuseEncoder\n\n        self._torch = torch\n        self.device = torch.device(device if torch.cuda.is_available() else \"cpu\")\n        self.max_seq_length = max_seq_length\n\n        with open(os.path.join(checkpoint_path, \"training_config.json\")) as f:\n            cfg = json.load(f)\n\n        base_model = model_name or cfg.get(\"model_name\", \"Qwen/Qwen2.5-Coder-3B\")\n        self.tokenizer = AutoTokenizer.from_pretrained(\n            checkpoint_path, trust_remote_code=True\n        )\n        self.model = StructFuseEncoder(\n            model_name=base_model,\n            proj_dim=cfg.get(\"proj_dim\", 256),\n            use_projection=True,\n            use_lora=cfg.get(\"use_lora\", False),\n            lora_r=cfg.get(\"lora_r\", 16),\n            lora_alpha=cfg.get(\"lora_alpha\", 32),\n            use_fusion_head=cfg.get(\"use_fusion_head\", False),\n        )\n        sd = torch.load(\n            os.path.join(checkpoint_path, \"model.pt\"),\n            map_location=\"cpu\",\n            weights_only=True,\n        )\n        self.model.load_state_dict(sd)\n        self.model.to(self.device).eval()\n        print(f\"Loaded StructFuse from {checkpoint_path} on {self.device}\")\n\n    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:\n        torch = self._torch\n        parts: list[np.ndarray] = []\n        for i in range(0, len(texts), batch_size):\n            batch = texts[i : i + batch_size]\n            enc = self.tokenizer(\n                batch,\n                padding=True,\n                truncation=True,\n                max_length=self.max_seq_length,\n                return_tensors=\"pt\",\n            ).to(self.device)\n            with torch.no_grad():\n                emb = self.model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            parts.append(emb.cpu().numpy())\n        return np.concatenate(parts, axis=0)\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        \"\"\"Rank candidates by cosine similarity to query. Returns (indices, scores).\"\"\"\n        if not candidates:\n            return [], []\n        q = self._encode([query], batch_size=1)\n        # Truncate very long snippets for encoding\n        docs = [c[:12000] for c in candidates]\n        d = self._encode(docs, batch_size=batch_size)\n        scores = (q @ d.T).squeeze(0)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\n# ── Metrics ─────────────────────────────────────────────────────────\n\ndef recall_at_k(predicted_indices: list[int], gold_index: int, k: int) -> float:\n    return 1.0 if gold_index in predicted_indices[:k] else 0.0\n\n\ndef reciprocal_rank(predicted_indices: list[int], gold_index: int) -> float:\n    for rank, idx in enumerate(predicted_indices, start=1):\n        if idx == gold_index:\n            return 1.0 / rank\n    return 0.0\n\n\n# ── Resume helpers ──────────────────────────────────────────────────\n\ndef load_completed(output_dir: str) -> set[str]:\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    done = set()\n    if os.path.exists(path):\n        with open(path) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        obj = json.loads(line)\n                        done.add(obj[\"instance_id\"])\n                    except (json.JSONDecodeError, KeyError):\n                        pass\n    return done\n\n\ndef append_result(output_dir: str, result: InstanceResult):\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    with open(path, \"a\") as f:\n        f.write(json.dumps(asdict(result), ensure_ascii=False) + \"\\n\")\n\n\n# ── Query construction ──────────────────────────────────────────────\n\ndef build_query(inst: RepoBenchInstance) -> str:\n    \"\"\"Build the query text from import_statement + code context.\"\"\"\n    parts = []\n    if inst.import_statement.strip():\n        parts.append(inst.import_statement.strip())\n    if inst.code.strip():\n        parts.append(inst.code.strip())\n    return \"\\n\".join(parts)\n\n\n# ── Main evaluation ─────────────────────────────────────────────────\n\ndef evaluate(args):\n    k_values = [int(k) for k in args.top_k.split(\",\")]\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Load data\n    if args.dry_run:\n        limit = args.limit if args.limit > 0 else 50\n        try:\n            instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n            if limit > 0:\n                instances = instances[:limit]\n            print(f\"Dry-run: loaded {len(instances)} real instances\")\n        except Exception as e:\n            print(f\"Could not load HF dataset ({e}), using mock data\")\n            instances = _mock_repobench(limit)\n    else:\n        instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n        if args.limit > 0:\n            instances = instances[:args.limit]\n\n    print(f\"Evaluating {len(instances)} instances, subset={args.subset}, split={args.split}\")\n    pool_sizes = [len(inst.context) for inst in instances]\n    print(f\"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, \"\n          f\"mean={np.mean(pool_sizes):.1f}\")\n\n    # 2. Initialize retriever\n    if args.dry_run:\n        retriever = MockRetriever()\n    else:\n        retriever = StructFuseRetriever(\n            checkpoint_path=args.checkpoint_path,\n            model_name=args.model_name,\n            max_seq_length=args.max_seq_length,\n            device=args.device,\n        )\n\n    # 3. Resume support\n    completed = load_completed(args.output_dir)\n    if completed:\n        print(f\"Resuming: {len(completed)} already done, \"\n              f\"{len(instances) - len(completed)} remaining\")\n\n    # 4. Evaluate each instance\n    for inst in tqdm(instances, desc=\"RepoBench-R eval\"):\n        if inst.instance_id in completed:\n            continue\n\n        try:\n            query = build_query(inst)\n            ranked_indices, scores = retriever.rank(\n                query, inst.context, batch_size=args.batch_size\n            )\n\n            rec = {}\n            for k in k_values:\n                rec[f\"@{k}\"] = recall_at_k(ranked_indices, inst.gold_snippet_index, k)\n            rr = reciprocal_rank(ranked_indices, inst.gold_snippet_index)\n\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=ranked_indices[:20],\n                predicted_scores=scores[:20],\n                recall=rec,\n                reciprocal_rank=round(rr, 6),\n            )\n        except Exception as e:\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=[],\n                predicted_scores=[],\n                recall={f\"@{k}\": 0.0 for k in k_values},\n                reciprocal_rank=0.0,\n                error=str(e),\n            )\n\n        append_result(args.output_dir, result)\n\n    # 5. Write summary\n    _write_summary(args, k_values)\n\n\ndef _write_summary(args, k_values: list[int]):\n    \"\"\"Recompute aggregate metrics from all per-instance results.\"\"\"\n    all_results = []\n    rpath = os.path.join(args.output_dir, \"per_instance_results.jsonl\")\n    if os.path.exists(rpath):\n        with open(rpath) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        all_results.append(json.loads(line))\n                    except json.JSONDecodeError:\n                        pass\n\n    valid = [r for r in all_results if not r.get(\"error\")]\n    summary: dict = {\n        \"config\": {\n            \"checkpoint_path\": args.checkpoint_path,\n            \"subset\": args.subset,\n            \"split\": args.split,\n            \"top_k\": k_values,\n            \"dry_run\": args.dry_run,\n            \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        },\n        \"total_instances\": len(all_results),\n        \"valid_instances\": len(valid),\n        \"errors\": len(all_results) - len(valid),\n    }\n\n    # Pool size stats\n    pool_sizes = [r.get(\"pool_size\", 0) for r in valid]\n    if pool_sizes:\n        summary[\"pool_size_mean\"] = round(float(np.mean(pool_sizes)), 1)\n        summary[\"pool_size_min\"] = min(pool_sizes)\n        summary[\"pool_size_max\"] = max(pool_sizes)\n        # Theoretical chance level\n        summary[\"chance_recall_at_1\"] = round(1.0 / np.mean(pool_sizes), 4)\n\n    for k in k_values:\n        vals = [r[\"recall\"].get(f\"@{k}\", 0.0) for r in valid]\n        summary[f\"recall@{k}\"] = round(float(np.mean(vals)), 4) if vals else 0.0\n\n    mrr_vals = [r.get(\"reciprocal_rank\", 0.0) for r in valid]\n    summary[\"mrr\"] = round(float(np.mean(mrr_vals)), 4) if mrr_vals else 0.0\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Instances: {len(all_results)} total, {len(valid)} valid, \"\n          f\"{len(all_results) - len(valid)} errors\")\n    if pool_sizes:\n        print(f\"  Pool size: mean={summary['pool_size_mean']}, \"\n              f\"min={summary['pool_size_min']}, max={summary['pool_size_max']}\")\n        print(f\"  Chance Recall@1: {summary['chance_recall_at_1']:.4f}\")\n    for k in k_values:\n        print(f\"  Recall@{k:>2d}: {summary[f'recall@{k}']:.4f}\")\n    print(f\"  MRR:       {summary['mrr']:.4f}\")\n    print(f\"\\nResults: {args.output_dir}/\")\n\n\n# ── CLI ─────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"StructFuse RepoBench-R retrieval evaluation\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    p.add_argument(\n        \"--checkpoint-path\", default=\"mock\",\n        help='Checkpoint dir (model.pt + training_config.json), or \"mock\" for dry-run',\n    )\n    p.add_argument(\"--model-name\", default=None,\n                    help=\"Override base model name (default: from training_config.json)\")\n    p.add_argument(\"--subset\", default=\"python_cff\",\n                    choices=list(_URLS.keys()),\n                    help=\"RepoBench-R subset (default: python_cff)\")\n    p.add_argument(\"--split\", default=\"test_easy\",\n                    help=\"Split to evaluate: train_easy/train_hard/test_easy/test_hard\")\n    p.add_argument(\"--output-dir\", default=\"repobench_eval_results\")\n    p.add_argument(\"--top-k\", default=\"1,5,10\",\n                    help=\"Comma-separated k values for Recall@k (default: 1,5,10)\")\n    p.add_argument(\"--batch-size\", type=int, default=32)\n    p.add_argument(\"--max-seq-length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda\")\n    p.add_argument(\"--limit\", type=int, default=0,\n                    help=\"Max instances to evaluate, 0 = all\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                    help=\"Mock retriever (random scores), no GPU needed\")\n    p.add_argument(\"--cache-dir\", default=\"\",\n                    help=\"HuggingFace cache dir for dataset downloads\")\n    args = p.parse_args()\n    evaluate(args)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T08:31:23.162083+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/eval_repobench.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T08:31:23.162301+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat > /root/structfuse/evaluation/eval_repobench.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"StructFuse RepoBench-R Retrieval Evaluation.\n\nEvaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool\ncross-file code retrieval benchmark.  Each instance contains a query\n(import_statement + code context) and a candidate pool (context list);\nthe task is to rank candidates so the gold snippet appears near the top.\n\nDataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)\nSubsets: python_cff, python_cfr, java_cff, java_cfr\nSplits:  train_easy, train_hard, test_easy, test_hard\n\nOutputs (in --output-dir):\n  per_instance_results.jsonl   one JSON object per instance\n  summary.json                 aggregate Recall@1/5/10, MRR, config\n\nUsage:\n  # Dry-run (no GPU, validates pipeline end-to-end)\n  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20\n\n  # Full eval with trained checkpoint\n  python eval_repobench.py \\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \\\n      --subset python_cff --split test_easy\n\nDependencies: torch, transformers, numpy, tqdm, huggingface_hub\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport gzip\nimport json\nimport os\nimport pickle\nimport sys\nimport time\nfrom dataclasses import asdict, dataclass, field\nfrom pathlib import Path\n\nimport numpy as np\nfrom tqdm import tqdm\n\n\n# ── Data structures ─────────────────────────────────────────────────\n\n@dataclass\nclass RepoBenchInstance:\n    instance_id: str\n    repo_name: str\n    file_path: str\n    import_statement: str\n    code: str\n    next_line: str\n    context: list[str]\n    gold_snippet_index: int\n\n\n@dataclass\nclass InstanceResult:\n    instance_id: str\n    repo_name: str\n    gold_index: int\n    pool_size: int\n    predicted_ranking: list[int]\n    predicted_scores: list[float]\n    recall: dict[str, float]\n    reciprocal_rank: float\n    error: str = \"\"\n\n\n# ── Data loading ────────────────────────────────────────────────────\n\n_URLS = {\n    \"java_cff\":   \"data/java_cff.gz\",\n    \"java_cfr\":   \"data/java_cfr.gz\",\n    \"python_cff\": \"data/python_cff.gz\",\n    \"python_cfr\": \"data/python_cfr.gz\",\n}\n\n\ndef load_repobench(\n    subset: str,\n    split: str,\n    cache_dir: str = \"\",\n) -> list[RepoBenchInstance]:\n    \"\"\"Download and parse RepoBench-R data via huggingface_hub.\"\"\"\n    from huggingface_hub import hf_hub_download\n\n    if subset not in _URLS:\n        raise ValueError(f\"Unknown subset '{subset}', choose from {list(_URLS.keys())}\")\n\n    parts = split.split(\"_\")\n    if len(parts) != 2 or parts[0] not in (\"train\", \"test\") or parts[1] not in (\"easy\", \"hard\"):\n        raise ValueError(f\"Invalid split '{split}', use train_easy/train_hard/test_easy/test_hard\")\n\n    kwargs = {}\n    if cache_dir:\n        kwargs[\"cache_dir\"] = cache_dir\n\n    print(f\"Downloading tianyang/repobench-r/{_URLS[subset]} ...\")\n    gz_path = hf_hub_download(\n        \"tianyang/repobench-r\", _URLS[subset], repo_type=\"dataset\", **kwargs\n    )\n\n    print(f\"Loading pickle from {gz_path} ...\")\n    with gzip.open(gz_path, \"rb\") as f:\n        data = pickle.load(f)\n\n    subset_key, level = parts[0], parts[1]\n    raw = data[subset_key][level]\n    print(f\"  {subset}/{split}: {len(raw)} examples\")\n\n    instances = []\n    for i, ex in enumerate(raw):\n        instances.append(RepoBenchInstance(\n            instance_id=f\"{subset}_{split}_{i:05d}\",\n            repo_name=ex[\"repo_name\"],\n            file_path=ex[\"file_path\"],\n            import_statement=ex[\"import_statement\"],\n            code=ex[\"code\"],\n            next_line=ex[\"next_line\"],\n            context=ex[\"context\"],\n            gold_snippet_index=ex[\"golden_snippet_index\"],\n        ))\n    return instances\n\n\ndef _mock_repobench(num_instances: int, pool_size: int = 10) -> list[RepoBenchInstance]:\n    \"\"\"Generate synthetic instances for dry-run testing.\"\"\"\n    rng = np.random.default_rng(42)\n    instances = []\n    for i in range(num_instances):\n        gold_idx = int(rng.integers(0, pool_size))\n        context = [\n            f\"def helper_{i}_{j}():\\n    return {j}\\n\" for j in range(pool_size)\n        ]\n        instances.append(RepoBenchInstance(\n            instance_id=f\"mock_{i:05d}\",\n            repo_name=f\"mock/repo_{i % 3}\",\n            file_path=f\"src/module_{i}.py\",\n            import_statement=f\"from helpers import helper_{i}_{gold_idx}\",\n            code=f\"def main():\\n    result = helper_{i}_{gold_idx}()\\n\",\n            next_line=f\"    print(result)\",\n            context=context,\n            gold_snippet_index=gold_idx,\n        ))\n    return instances\n\n\n# ── Retrievers ──────────────────────────────────────────────────────\n\nclass MockRetriever:\n    \"\"\"Random-score retriever for dry-run validation.\"\"\"\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        if not candidates:\n            return [], []\n        rng = np.random.default_rng(hash(query) % (2**31))\n        scores = rng.random(len(candidates)).astype(float)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\nclass StructFuseRetriever:\n    \"\"\"Bi-encoder retriever using a trained StructFuse checkpoint.\"\"\"\n\n    def __init__(\n        self,\n        checkpoint_path: str,\n        model_name: str | None = None,\n        max_seq_length: int = 2048,\n        device: str = \"cuda\",\n    ):\n        import torch\n        from transformers import AutoTokenizer\n\n        train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"..\", \"training\"\n        )\n        alt_train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"training\"\n        )\n        for d in [train_dir, alt_train_dir]:\n            if d not in sys.path and os.path.isdir(d):\n                sys.path.insert(0, d)\n        from contrastive_model import StructFuseEncoder\n\n        self._torch = torch\n        self.device = torch.device(device if torch.cuda.is_available() else \"cpu\")\n        self.max_seq_length = max_seq_length\n\n        with open(os.path.join(checkpoint_path, \"training_config.json\")) as f:\n            cfg = json.load(f)\n\n        base_model = model_name or cfg.get(\"model_name\", \"Qwen/Qwen2.5-Coder-3B\")\n        self.tokenizer = AutoTokenizer.from_pretrained(\n            checkpoint_path, trust_remote_code=True\n        )\n        self.model = StructFuseEncoder(\n            model_name=base_model,\n            proj_dim=cfg.get(\"proj_dim\", 256),\n            use_projection=True,\n            use_lora=cfg.get(\"use_lora\", False),\n            lora_r=cfg.get(\"lora_r\", 16),\n            lora_alpha=cfg.get(\"lora_alpha\", 32),\n            use_fusion_head=cfg.get(\"use_fusion_head\", False),\n        )\n        sd = torch.load(\n            os.path.join(checkpoint_path, \"model.pt\"),\n            map_location=\"cpu\",\n            weights_only=True,\n        )\n        self.model.load_state_dict(sd)\n        self.model.to(self.device).eval()\n        print(f\"Loaded StructFuse from {checkpoint_path} on {self.device}\")\n\n    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:\n        torch = self._torch\n        parts: list[np.ndarray] = []\n        for i in range(0, len(texts), batch_size):\n            batch = texts[i : i + batch_size]\n            enc = self.tokenizer(\n                batch,\n                padding=True,\n                truncation=True,\n                max_length=self.max_seq_length,\n                return_tensors=\"pt\",\n            ).to(self.device)\n            with torch.no_grad():\n                emb = self.model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            parts.append(emb.cpu().numpy())\n        return np.concatenate(parts, axis=0)\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        if not candidates:\n            return [], []\n        q = self._encode([query], batch_size=1)\n        docs = [c[:12000] for c in candidates]\n        d = self._encode(docs, batch_size=batch_size)\n        scores = (q @ d.T).squeeze(0)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\n# ── Metrics ─────────────────────────────────────────────────────────\n\ndef recall_at_k(predicted_indices: list[int], gold_index: int, k: int) -> float:\n    return 1.0 if gold_index in predicted_indices[:k] else 0.0\n\n\ndef reciprocal_rank(predicted_indices: list[int], gold_index: int) -> float:\n    for rank, idx in enumerate(predicted_indices, start=1):\n        if idx == gold_index:\n            return 1.0 / rank\n    return 0.0\n\n\n# ── Resume helpers ──────────────────────────────────────────────────\n\ndef load_completed(output_dir: str) -> set[str]:\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    done = set()\n    if os.path.exists(path):\n        with open(path) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        obj = json.loads(line)\n                        done.add(obj[\"instance_id\"])\n                    except (json.JSONDecodeError, KeyError):\n                        pass\n    return done\n\n\ndef append_result(output_dir: str, result: InstanceResult):\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    with open(path, \"a\") as f:\n        f.write(json.dumps(asdict(result), ensure_ascii=False) + \"\\n\")\n\n\ndef build_query(inst: RepoBenchInstance) -> str:\n    parts = []\n    if inst.import_statement.strip():\n        parts.append(inst.import_statement.strip())\n    if inst.code.strip():\n        parts.append(inst.code.strip())\n    return \"\\n\".join(parts)\n\n\n# ── Main evaluation ─────────────────────────────────────────────────\n\ndef evaluate(args):\n    k_values = [int(k) for k in args.top_k.split(\",\")]\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Load data\n    if args.dry_run:\n        limit = args.limit if args.limit > 0 else 50\n        try:\n            instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n            if limit > 0:\n                instances = instances[:limit]\n            print(f\"Dry-run: loaded {len(instances)} real instances\")\n        except Exception as e:\n            print(f\"Could not load HF dataset ({e}), using mock data\")\n            instances = _mock_repobench(limit)\n    else:\n        instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n        if args.limit > 0:\n            instances = instances[:args.limit]\n\n    print(f\"Evaluating {len(instances)} instances, subset={args.subset}, split={args.split}\")\n    pool_sizes = [len(inst.context) for inst in instances]\n    print(f\"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, \"\n          f\"mean={np.mean(pool_sizes):.1f}\")\n\n    # 2. Initialize retriever\n    if args.dry_run:\n        retriever = MockRetriever()\n    else:\n        retriever = StructFuseRetriever(\n            checkpoint_path=args.checkpoint_path,\n            model_name=args.model_name,\n            max_seq_length=args.max_seq_length,\n            device=args.device,\n        )\n\n    # 3. Resume support\n    completed = load_completed(args.output_dir)\n    if completed:\n        print(f\"Resuming: {len(completed)} already done, \"\n              f\"{len(instances) - len(completed)} remaining\")\n\n    # 4. Evaluate each instance\n    for inst in tqdm(instances, desc=\"RepoBench-R eval\"):\n        if inst.instance_id in completed:\n            continue\n\n        try:\n            query = build_query(inst)\n            ranked_indices, scores = retriever.rank(\n                query, inst.context, batch_size=args.batch_size\n            )\n\n            rec = {}\n            for k in k_values:\n                rec[f\"@{k}\"] = recall_at_k(ranked_indices, inst.gold_snippet_index, k)\n            rr = reciprocal_rank(ranked_indices, inst.gold_snippet_index)\n\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=ranked_indices[:20],\n                predicted_scores=scores[:20],\n                recall=rec,\n                reciprocal_rank=round(rr, 6),\n            )\n        except Exception as e:\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=[],\n                predicted_scores=[],\n                recall={f\"@{k}\": 0.0 for k in k_values},\n                reciprocal_rank=0.0,\n                error=str(e),\n            )\n\n        append_result(args.output_dir, result)\n\n    # 5. Write summary\n    _write_summary(args, k_values)\n\n\ndef _write_summary(args, k_values: list[int]):\n    all_results = []\n    rpath = os.path.join(args.output_dir, \"per_instance_results.jsonl\")\n    if os.path.exists(rpath):\n        with open(rpath) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        all_results.append(json.loads(line))\n                    except json.JSONDecodeError:\n                        pass\n\n    valid = [r for r in all_results if not r.get(\"error\")]\n    summary: dict = {\n        \"config\": {\n            \"checkpoint_path\": args.checkpoint_path,\n            \"subset\": args.subset,\n            \"split\": args.split,\n            \"top_k\": k_values,\n            \"dry_run\": args.dry_run,\n            \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        },\n        \"total_instances\": len(all_results),\n        \"valid_instances\": len(valid),\n        \"errors\": len(all_results) - len(valid),\n    }\n\n    pool_sizes = [r.get(\"pool_size\", 0) for r in valid]\n    if pool_sizes:\n        summary[\"pool_size_mean\"] = round(float(np.mean(pool_sizes)), 1)\n        summary[\"pool_size_min\"] = min(pool_sizes)\n        summary[\"pool_size_max\"] = max(pool_sizes)\n        summary[\"chance_recall_at_1\"] = round(1.0 / np.mean(pool_sizes), 4)\n\n    for k in k_values:\n        vals = [r[\"recall\"].get(f\"@{k}\", 0.0) for r in valid]\n        summary[f\"recall@{k}\"] = round(float(np.mean(vals)), 4) if vals else 0.0\n\n    mrr_vals = [r.get(\"reciprocal_rank\", 0.0) for r in valid]\n    summary[\"mrr\"] = round(float(np.mean(mrr_vals)), 4) if mrr_vals else 0.0\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Instances: {len(all_results)} total, {len(valid)} valid, \"\n          f\"{len(all_results) - len(valid)} errors\")\n    if pool_sizes:\n        print(f\"  Pool size: mean={summary['pool_size_mean']}, \"\n              f\"min={summary['pool_size_min']}, max={summary['pool_size_max']}\")\n        print(f\"  Chance Recall@1: {summary['chance_recall_at_1']:.4f}\")\n    for k in k_values:\n        print(f\"  Recall@{k:>2d}: {summary[f'recall@{k}']:.4f}\")\n    print(f\"  MRR:       {summary['mrr']:.4f}\")\n    print(f\"\\nResults: {args.output_dir}/\")\n\n\n# ── CLI ─────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"StructFuse RepoBench-R retrieval evaluation\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    p.add_argument(\n        \"--checkpoint-path\", default=\"mock\",\n        help='Checkpoint dir (model.pt + training_config.json), or \"mock\" for dry-run',\n    )\n    p.add_argument(\"--model-name\", default=None,\n                    help=\"Override base model name (default: from training_config.json)\")\n    p.add_argument(\"--subset\", default=\"python_cff\",\n                    choices=[\"python_cff\", \"python_cfr\", \"java_cff\", \"java_cfr\"],\n                    help=\"RepoBench-R subset (default: python_cff)\")\n    p.add_argument(\"--split\", default=\"test_easy\",\n                    help=\"Split: train_easy/train_hard/test_easy/test_hard\")\n    p.add_argument(\"--output-dir\", default=\"repobench_eval_results\")\n    p.add_argument(\"--top-k\", default=\"1,5,10\",\n                    help=\"Comma-separated k values for Recall@k (default: 1,5,10)\")\n    p.add_argument(\"--batch-size\", type=int, default=32)\n    p.add_argument(\"--max-seq-length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda\")\n    p.add_argument(\"--limit\", type=int, default=0,\n                    help=\"Max instances to evaluate, 0 = all\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                    help=\"Mock retriever (random scores), no GPU needed\")\n    p.add_argument(\"--cache-dir\", default=\"\",\n                    help=\"HuggingFace cache dir for dataset downloads\")\n    args = p.parse_args()\n    evaluate(args)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"DONE: $(wc -l /root/structfuse/evaluation/eval_repobench.py)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat > /root/structfuse/evaluation/eval_repobench.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"StructFuse RepoBench-R Retrieval Evaluation.\n\nEvaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool\ncross-file code retrieval benchmark.  Each instance contains a query\n(import_statement + code context) and a candidate pool (context list);\nthe task is to rank candidates so the gold snippet appears near the top.\n\nDataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)\nSubsets: python_cff, python_cfr, java_cff, java_cfr\nSplits:  train_easy, train_hard, test_easy, test_hard\n\nOutputs (in --output-dir):\n  per_instance_results.jsonl   one JSON object per instance\n  summary.json                 aggregate Recall@1/5/10, MRR, config\n\nUsage:\n  # Dry-run (no GPU, validates pipeline end-to-end)\n  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20\n\n  # Full eval with trained checkpoint\n  python eval_repobench.py \\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \\\n      --subset python_cff --split test_easy\n\nDependencies: torch, transformers, numpy, tqdm, huggingface_hub\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport gzip\nimport json\nimport os\nimport pickle\nimport sys\nimport time\nfrom dataclasses import asdict, dataclass, field\nfrom pathlib import Path\n\nimport numpy as np\nfrom tqdm import tqdm\n\n\n# ── Data structures ─────────────────────────────────────────────────\n\n@dataclass\nclass RepoBenchInstance:\n    instance_id: str\n    repo_name: str\n    file_path: str\n    import_statement: str\n    code: str\n    next_line: str\n    context: list[str]\n    gold_snippet_index: int\n\n\n@dataclass\nclass InstanceResult:\n    instance_id: str\n    repo_name: str\n    gold_index: int\n    pool_size: int\n    predicted_ranking: list[int]\n    predicted_scores: list[float]\n    recall: dict[str, float]\n    reciprocal_rank: float\n    error: str = \"\"\n\n\n# ── Data loading ────────────────────────────────────────────────────\n\n_URLS = {\n    \"java_cff\":   \"data/java_cff.gz\",\n    \"java_cfr\":   \"data/java_cfr.gz\",\n    \"python_cff\": \"data/python_cff.gz\",\n    \"python_cfr\": \"data/python_cfr.gz\",\n}\n\n\ndef load_repobench(\n    subset: str,\n    split: str,\n    cache_dir: str = \"\",\n) -> list[RepoBenchInstance]:\n    \"\"\"Download and parse RepoBench-R data via huggingface_hub.\"\"\"\n    from huggingface_hub import hf_hub_download\n\n    if subset not in _URLS:\n        raise ValueError(f\"Unknown subset '{subset}', choose from {list(_URLS.keys())}\")\n\n    parts = split.split(\"_\")\n    if len(parts) != 2 or parts[0] not in (\"train\", \"test\") or parts[1] not in (\"easy\", \"hard\"):\n        raise ValueError(f\"Invalid split '{split}', use train_easy/train_hard/test_easy/test_hard\")\n\n    kwargs = {}\n    if cache_dir:\n        kwargs[\"cache_dir\"] = cache_dir\n\n    print(f\"Downloading tianyang/repobench-r/{_URLS[subset]} ...\")\n    gz_path = hf_hub_download(\n        \"tianyang/repobench-r\", _URLS[subset], repo_type=\"dataset\", **kwargs\n    )\n\n    print(f\"Loading pickle from {gz_path} ...\")\n    with gzip.open(gz_path, \"rb\") as f:\n        data = pickle.load(f)\n\n    subset_key, level = parts[0], parts[1]\n    raw = data[subset_key][level]\n    print(f\"  {subset}/{split}: {len(raw)} examples\")\n\n    instances = []\n    for i, ex in enumerate(raw):\n        instances.append(RepoBenchInstance(\n            instance_id=f\"{subset}_{split}_{i:05d}\",\n            repo_name=ex[\"repo_name\"],\n            file_path=ex[\"file_path\"],\n            import_statement=ex[\"import_statement\"],\n            code=ex[\"code\"],\n            next_line=ex[\"next_line\"],\n            context=ex[\"context\"],\n            gold_snippet_index=ex[\"golden_snippet_index\"],\n        ))\n    return instances\n\n\ndef _mock_repobench(num_instances: int, pool_size: int = 10) -> list[RepoBenchInstance]:\n    \"\"\"Generate synthetic instances for dry-run testing.\"\"\"\n    rng = np.random.default_rng(42)\n    instances = []\n    for i in range(num_instances):\n        gold_idx = int(rng.integers(0, pool_size))\n        context = [\n            f\"def helper_{i}_{j}():\\n    return {j}\\n\" for j in range(pool_size)\n        ]\n        instances.append(RepoBenchInstance(\n            instance_id=f\"mock_{i:05d}\",\n            repo_name=f\"mock/repo_{i % 3}\",\n            file_path=f\"src/module_{i}.py\",\n            import_statement=f\"from helpers import helper_{i}_{gold_idx}\",\n            code=f\"def main():\\n    result = helper_{i}_{gold_idx}()\\n\",\n            next_line=f\"    print(result)\",\n            context=context,\n            gold_snippet_index=gold_idx,\n        ))\n    return instances\n\n\n# ── Retrievers ──────────────────────────────────────────────────────\n\nclass MockRetriever:\n    \"\"\"Random-score retriever for dry-run validation.\"\"\"\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        if not candidates:\n            return [], []\n        rng = np.random.default_rng(hash(query) % (2**31))\n        scores = rng.random(len(candidates)).astype(float)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\nclass StructFuseRetriever:\n    \"\"\"Bi-encoder retriever using a trained StructFuse checkpoint.\"\"\"\n\n    def __init__(\n        self,\n        checkpoint_path: str,\n        model_name: str | None = None,\n        max_seq_length: int = 2048,\n        device: str = \"cuda\",\n    ):\n        import torch\n        from transformers import AutoTokenizer\n\n        train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"..\", \"training\"\n        )\n        alt_train_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), \"training\"\n        )\n        for d in [train_dir, alt_train_dir]:\n            if d not in sys.path and os.path.isdir(d):\n                sys.path.insert(0, d)\n        from contrastive_model import StructFuseEncoder\n\n        self._torch = torch\n        self.device = torch.device(device if torch.cuda.is_available() else \"cpu\")\n        self.max_seq_length = max_seq_length\n\n        with open(os.path.join(checkpoint_path, \"training_config.json\")) as f:\n            cfg = json.load(f)\n\n        base_model = model_name or cfg.get(\"model_name\", \"Qwen/Qwen2.5-Coder-3B\")\n        self.tokenizer = AutoTokenizer.from_pretrained(\n            checkpoint_path, trust_remote_code=True\n        )\n        self.model = StructFuseEncoder(\n            model_name=base_model,\n            proj_dim=cfg.get(\"proj_dim\", 256),\n            use_projection=True,\n            use_lora=cfg.get(\"use_lora\", False),\n            lora_r=cfg.get(\"lora_r\", 16),\n            lora_alpha=cfg.get(\"lora_alpha\", 32),\n            use_fusion_head=cfg.get(\"use_fusion_head\", False),\n        )\n        sd = torch.load(\n            os.path.join(checkpoint_path, \"model.pt\"),\n            map_location=\"cpu\",\n            weights_only=True,\n        )\n        self.model.load_state_dict(sd)\n        self.model.to(self.device).eval()\n        print(f\"Loaded StructFuse from {checkpoint_path} on {self.device}\")\n\n    def _encode(self, texts: list[str], batch_size: int) -> np.ndarray:\n        torch = self._torch\n        parts: list[np.ndarray] = []\n        for i in range(0, len(texts), batch_size):\n            batch = texts[i : i + batch_size]\n            enc = self.tokenizer(\n                batch,\n                padding=True,\n                truncation=True,\n                max_length=self.max_seq_length,\n                return_tensors=\"pt\",\n            ).to(self.device)\n            with torch.no_grad():\n                emb = self.model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            parts.append(emb.cpu().numpy())\n        return np.concatenate(parts, axis=0)\n\n    def rank(\n        self, query: str, candidates: list[str], batch_size: int = 32\n    ) -> tuple[list[int], list[float]]:\n        if not candidates:\n            return [], []\n        q = self._encode([query], batch_size=1)\n        docs = [c[:12000] for c in candidates]\n        d = self._encode(docs, batch_size=batch_size)\n        scores = (q @ d.T).squeeze(0)\n        idx = np.argsort(scores)[::-1]\n        return idx.tolist(), [float(scores[i]) for i in idx]\n\n\n# ── Metrics ─────────────────────────────────────────────────────────\n\ndef recall_at_k(predicted_indices: list[int], gold_index: int, k: int) -> float:\n    return 1.0 if gold_index in predicted_indices[:k] else 0.0\n\n\ndef reciprocal_rank(predicted_indices: list[int], gold_index: int) -> float:\n    for rank, idx in enumerate(predicted_indices, start=1):\n        if idx == gold_index:\n            return 1.0 / rank\n    return 0.0\n\n\n# ── Resume helpers ──────────────────────────────────────────────────\n\ndef load_completed(output_dir: str) -> set[str]:\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    done = set()\n    if os.path.exists(path):\n        with open(path) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        obj = json.loads(line)\n                        done.add(obj[\"instance_id\"])\n                    except (json.JSONDecodeError, KeyError):\n                        pass\n    return done\n\n\ndef append_result(output_dir: str, result: InstanceResult):\n    path = os.path.join(output_dir, \"per_instance_results.jsonl\")\n    with open(path, \"a\") as f:\n        f.write(json.dumps(asdict(result), ensure_ascii=False) + \"\\n\")\n\n\ndef build_query(inst: RepoBenchInstance) -> str:\n    parts = []\n    if inst.import_statement.strip():\n        parts.append(inst.import_statement.strip())\n    if inst.code.strip():\n        parts.append(inst.code.strip())\n    return \"\\n\".join(parts)\n\n\n# ── Main evaluation ─────────────────────────────────────────────────\n\ndef evaluate(args):\n    k_values = [int(k) for k in args.top_k.split(\",\")]\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Load data\n    if args.dry_run:\n        limit = args.limit if args.limit > 0 else 50\n        try:\n            instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n            if limit > 0:\n                instances = instances[:limit]\n            print(f\"Dry-run: loaded {len(instances)} real instances\")\n        except Exception as e:\n            print(f\"Could not load HF dataset ({e}), using mock data\")\n            instances = _mock_repobench(limit)\n    else:\n        instances = load_repobench(args.subset, args.split, cache_dir=args.cache_dir)\n        if args.limit > 0:\n            instances = instances[:args.limit]\n\n    print(f\"Evaluating {len(instances)} instances, subset={args.subset}, split={args.split}\")\n    pool_sizes = [len(inst.context) for inst in instances]\n    print(f\"Pool sizes: min={min(pool_sizes)}, max={max(pool_sizes)}, \"\n          f\"mean={np.mean(pool_sizes):.1f}\")\n\n    # 2. Initialize retriever\n    if args.dry_run:\n        retriever = MockRetriever()\n    else:\n        retriever = StructFuseRetriever(\n            checkpoint_path=args.checkpoint_path,\n            model_name=args.model_name,\n            max_seq_length=args.max_seq_length,\n            device=args.device,\n        )\n\n    # 3. Resume support\n    completed = load_completed(args.output_dir)\n    if completed:\n        print(f\"Resuming: {len(completed)} already done, \"\n              f\"{len(instances) - len(completed)} remaining\")\n\n    # 4. Evaluate each instance\n    for inst in tqdm(instances, desc=\"RepoBench-R eval\"):\n        if inst.instance_id in completed:\n            continue\n\n        try:\n            query = build_query(inst)\n            ranked_indices, scores = retriever.rank(\n                query, inst.context, batch_size=args.batch_size\n            )\n\n            rec = {}\n            for k in k_values:\n                rec[f\"@{k}\"] = recall_at_k(ranked_indices, inst.gold_snippet_index, k)\n            rr = reciprocal_rank(ranked_indices, inst.gold_snippet_index)\n\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=ranked_indices[:20],\n                predicted_scores=scores[:20],\n                recall=rec,\n                reciprocal_rank=round(rr, 6),\n            )\n        except Exception as e:\n            result = InstanceResult(\n                instance_id=inst.instance_id,\n                repo_name=inst.repo_name,\n                gold_index=inst.gold_snippet_index,\n                pool_size=len(inst.context),\n                predicted_ranking=[],\n                predicted_scores=[],\n                recall={f\"@{k}\": 0.0 for k in k_values},\n                reciprocal_rank=0.0,\n                error=str(e),\n            )\n\n        append_result(args.output_dir, result)\n\n    # 5. Write summary\n    _write_summary(args, k_values)\n\n\ndef _write_summary(args, k_values: list[int]):\n    all_results = []\n    rpath = os.path.join(args.output_dir, \"per_instance_results.jsonl\")\n    if os.path.exists(rpath):\n        with open(rpath) as f:\n            for line in f:\n                if line.strip():\n                    try:\n                        all_results.append(json.loads(line))\n                    except json.JSONDecodeError:\n                        pass\n\n    valid = [r for r in all_results if not r.get(\"error\")]\n    summary: dict = {\n        \"config\": {\n            \"checkpoint_path\": args.checkpoint_path,\n            \"subset\": args.subset,\n            \"split\": args.split,\n            \"top_k\": k_values,\n            \"dry_run\": args.dry_run,\n            \"timestamp\": time.strftime(\"%Y-%m-%d %H:%M:%S\"),\n        },\n        \"total_instances\": len(all_results),\n        \"valid_instances\": len(valid),\n        \"errors\": len(all_results) - len(valid),\n    }\n\n    pool_sizes = [r.get(\"pool_size\", 0) for r in valid]\n    if pool_sizes:\n        summary[\"pool_size_mean\"] = round(float(np.mean(pool_sizes)), 1)\n        summary[\"pool_size_min\"] = min(pool_sizes)\n        summary[\"pool_size_max\"] = max(pool_sizes)\n        summary[\"chance_recall_at_1\"] = round(1.0 / np.mean(pool_sizes), 4)\n\n    for k in k_values:\n        vals = [r[\"recall\"].get(f\"@{k}\", 0.0) for r in valid]\n        summary[f\"recall@{k}\"] = round(float(np.mean(vals)), 4) if vals else 0.0\n\n    mrr_vals = [r.get(\"reciprocal_rank\", 0.0) for r in valid]\n    summary[\"mrr\"] = round(float(np.mean(mrr_vals)), 4) if mrr_vals else 0.0\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Instances: {len(all_results)} total, {len(valid)} valid, \"\n          f\"{len(all_results) - len(valid)} errors\")\n    if pool_sizes:\n        print(f\"  Pool size: mean={summary['pool_size_mean']}, \"\n              f\"min={summary['pool_size_min']}, max={summary['pool_size_max']}\")\n        print(f\"  Chance Recall@1: {summary['chance_recall_at_1']:.4f}\")\n    for k in k_values:\n        print(f\"  Recall@{k:>2d}: {summary[f'recall@{k}']:.4f}\")\n    print(f\"  MRR:       {summary['mrr']:.4f}\")\n    print(f\"\\nResults: {args.output_dir}/\")\n\n\n# ── CLI ─────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"StructFuse RepoBench-R retrieval evaluation\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    p.add_argument(\n        \"--checkpoint-path\", default=\"mock\",\n        help='Checkpoint dir (model.pt + training_config.json), or \"mock\" for dry-run',\n    )\n    p.add_argument(\"--model-name\", default=None,\n                    help=\"Override base model name (default: from training_config.json)\")\n    p.add_argument(\"--subset\", default=\"python_cff\",\n                    choices=[\"python_cff\", \"python_cfr\", \"java_cff\", \"java_cfr\"],\n                    help=\"RepoBench-R subset (default: python_cff)\")\n    p.add_argument(\"--split\", default=\"test_easy\",\n                    help=\"Split: train_easy/train_hard/test_easy/test_hard\")\n    p.add_argument(\"--output-dir\", default=\"repobench_eval_results\")\n    p.add_argument(\"--top-k\", default=\"1,5,10\",\n                    help=\"Comma-separated k values for Recall@k (default: 1,5,10)\")\n    p.add_argument(\"--batch-size\", type=int, default=32)\n    p.add_argument(\"--max-seq-length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda\")\n    p.add_argument(\"--limit\", type=int, default=0,\n                    help=\"Max instances to evaluate, 0 = all\")\n    p.add_argument(\"--dry-run\", action=\"store_true\",\n                    help=\"Mock retriever (random scores), no GPU needed\")\n    p.add_argument(\"--cache-dir\", default=\"\",\n                    help=\"HuggingFace cache dir for dataset downloads\")\n    args = p.parse_args()\n    evaluate(args)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"DONE: $(wc -l /root/structfuse/evaluation/eval_repobench.py)\""
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T08:31:23.162630+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE: 476 /root/structfuse/evaluation/eval_repobench.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T08:31:23.162799+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && rm -rf /tmp/repobench_dryrun && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && rm -rf /tmp/repobench_dryrun && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 10"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T08:31:23.162944+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && rm -rf /tmp/repobench_dryrun && CUDA_VISIBLE_DEVICES=\\\"\\\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 10'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz (Caused by NewConnectionError('&lt;urllib3.connection.HTTPSConnection object at 0x7fdd79123ef0>: Failed to establish a new connection: [Errno 101] Network is unreachable'))\\\"), '(Request ID: f6374121-9ccb-4120-a179-b9f682eea04b)')' thrown while requesting HEAD https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz\\nRetrying in 1s [Retry 1/5].\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz (Caused by NewConnectionError('&lt;urllib3.connection.HTTPSConnection object at 0x7fdd7904cc20>: Failed to establish a new connection: [Errno 101] Network is unreachable'))\\\"), '(Request ID: b7fee003-dd64-4419-ac41-7c91c4057866)')' thrown while requesting HEAD https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz\\nRetrying in 2s [Retry 2/5].\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T08:31:23.163111+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && rm -rf /tmp/repobench_dryrun && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 10",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && rm -rf /tmp/repobench_dryrun && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 10",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T08:31:23.163263+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nDownloading tianyang/repobench-r/data/python_cff.gz ...\\nLoading pickle from /root/.cache/huggingface/hub/datasets--tianyang--repobench-r/snapshots/b10acdbfa9a62bad85cbaa58737a978851ab9039/data/python_cff.gz ...\\n  python_cff/test_easy: 8000 examples\\nDry-run: loaded 10 real instances\\nEvaluating 10 instances, subset=python_cff, split=test_easy\\nPool sizes: min=5, max=7, mean=5.9\\n\\n============================================================\\nInstances: 10 total, 10 valid, 0 errors\\n  Pool size: mean=5.9, min=5, max=7\\n  Chance Recall@1: 0.1695\\n  Recall@ 1: 0.1000\\n  Recall@ 5: 1.0000\\n  Recall@10: 1.0000\\n  MRR:       0.3567\\n\\nResults: /tmp/repobench_dryrun/\\n\", \"stderr\": \"\\rRepoBench-R eval:   0%|          | 0/10 [00:00<?, ?it/s]\\rRepoBench-R eval: 100%|██████████| 10/10 [00:00<00:00, 1587.67it/s]\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T08:31:23.163432+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /tmp/repobench_dryrun/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /tmp/repobench_dryrun/summary.json"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T08:31:23.163555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -3 /tmp/repobench_dryrun/per_instance_results.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "head -3 /tmp/repobench_dryrun/per_instance_results.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T08:31:23.163718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint_path\\\": \\\"mock\\\",\\n    \\\"subset\\\": \\\"python_cff\\\",\\n    \\\"split\\\": \\\"test_easy\\\",\\n    \\\"top_k\\\": [\\n      1,\\n      5,\\n      10\\n    ],\\n    \\\"dry_run\\\": true,\\n    \\\"timestamp\\\": \\\"2026-05-14 16:29:59\\\"\\n  },\\n  \\\"total_instances\\\": 10,\\n  \\\"valid_instances\\\": 10,\\n  \\\"errors\\\": 0,\\n  \\\"pool_size_mean\\\": 5.9,\\n  \\\"pool_size_min\\\": 5,\\n  \\\"pool_size_max\\\": 7,\\n  \\\"chance_recall_at_1\\\": 0.1695,\\n  \\\"recall@1\\\": 0.1,\\n  \\\"recall@5\\\": 1.0,\\n  \\\"recall@10\\\": 1.0,\\n  \\\"mrr\\\": 0.3567\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T08:31:23.163869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instance_id\\\": \\\"python_cff_test_easy_00000\\\", \\\"repo_name\\\": \\\"merll/docker-map\\\", \\\"gold_index\\\": 0, \\\"pool_size\\\": 5, \\\"predicted_ranking\\\": [0, 3, 2, 4, 1], \\\"predicted_scores\\\": [0.905517899990039, 0.8890811001123341, 0.6630285744423223, 0.5326069158659521, 0.38998773968459843], \\\"recall\\\": {\\\"@1\\\": 1.0, \\\"@5\\\": 1.0, \\\"@10\\\": 1.0}, \\\"reciprocal_rank\\\": 1.0, \\\"error\\\": \\\"\\\"}\\n{\\\"instance_id\\\": \\\"python_cff_test_easy_00001\\\", \\\"repo_name\\\": \\\"iancze/PSOAP\\\", \\\"gold_index\\\": 2, \\\"pool_size\\\": 7, \\\"predicted_ranking\\\": [5, 2, 3, 1, 0, 6, 4], \\\"predicted_scores\\\": [0.9959243165575857, 0.9738405888984782, 0.8461042155567049, 0.6805855494888912, 0.5651972569553655, 0.2725235237648207, 0.11363957580714013], \\\"recall\\\": {\\\"@1\\\": 0.0, \\\"@5\\\": 1.0, \\\"@10\\\": 1.0}, \\\"reciprocal_rank\\\": 0.5, \\\"error\\\": \\\"\\\"}\\n{\\\"instance_id\\\": \\\"python_cff_test_easy_00002\\\", \\\"repo_name\\\": \\\"andymeneely/attack-surface-metrics\\\", \\\"gold_index\\\": 1, \\\"pool_size\\\": 5, \\\"predicted_ranking\\\": [4, 0, 3, 1, 2], \\\"predicted_scores\\\": [0.6822076596859564, 0.5356046869936448, 0.442343849010712, 0.43171465873104287, 0.08731903737816993], \\\"recall\\\": {\\\"@1\\\": 0.0, \\\"@5\\\": 1.0, \\\"@10\\\": 1.0}, \\\"reciprocal_rank\\\": 0.25, \\\"error\\\": \\\"\\\"}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T08:31:23.164032+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && rm -rf /tmp/repobench_dryrun2 && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun2 --limit 200 --split test_hard",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && rm -rf /tmp/repobench_dryrun2 && CUDA_VISIBLE_DEVICES=\"\" python3 /root/structfuse/evaluation/eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun2 --limit 200 --split test_hard",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T08:31:23.164180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nDownloading tianyang/repobench-r/data/python_cff.gz ...\\nLoading pickle from /root/.cache/huggingface/hub/datasets--tianyang--repobench-r/snapshots/b10acdbfa9a62bad85cbaa58737a978851ab9039/data/python_cff.gz ...\\n  python_cff/test_hard: 8000 examples\\nDry-run: loaded 200 real instances\\nEvaluating 200 instances, subset=python_cff, split=test_hard\\nPool sizes: min=10, max=60, mean=15.7\\n\\n============================================================\\nInstances: 200 total, 200 valid, 0 errors\\n  Pool size: mean=15.7, min=10, max=60\\n  Chance Recall@1: 0.0637\\n  Recall@ 1: 0.1150\\n  Recall@ 5: 0.4200\\n  Recall@10: 0.7300\\n  MRR:       0.2638\\n\\nResults: /tmp/repobench_dryrun2/\\n\", \"stderr\": \"\\rRepoBench-R eval:   0%|          | 0/200 [00:00<?, ?it/s]\\rRepoBench-R eval: 100%|██████████| 200/200 [00:00<00:00, 11158.48it/s]\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T08:31:23.164355+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport gzip, pickle\nfrom huggingface_hub import hf_hub_download\nimport numpy as np\n\nfor subset in ['python_cff', 'python_cfr']:\n    path = hf_hub_download('tianyang/repobench-r', f'data/{subset}.gz', repo_type='dataset')\n    with gzip.open(path, 'rb') as f:\n        data = pickle.load(f)\n    print(f'=== {subset} ===')\n    for s in data:\n        for l in data[s]:\n            exs = data[s][l]\n            pools = [len(e['context']) for e in exs]\n            print(f'  {s}_{l}: {len(exs)} examples, pool min={min(pools)} max={max(pools)} mean={np.mean(pools):.1f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python3 -c \"\nimport gzip, pickle\nfrom huggingface_hub import hf_hub_download\nimport numpy as np\n\nfor subset in ['python_cff', 'python_cfr']:\n    path = hf_hub_download('tianyang/repobench-r', f'data/{subset}.gz', repo_type='dataset')\n    with gzip.open(path, 'rb') as f:\n        data = pickle.load(f)\n    print(f'=== {subset} ===')\n    for s in data:\n        for l in data[s]:\n            exs = data[s][l]\n            pools = [len(e['context']) for e in exs]\n            print(f'  {s}_{l}: {len(exs)} examples, pool min={min(pools)} max={max(pools)} mean={np.mean(pools):.1f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T08:31:23.164502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n=== python_cff ===\\n  test_easy: 8000 examples, pool min=5 max=9 mean=6.6\\n  test_hard: 8000 examples, pool min=10 max=60 mean=17.9\\n  train_easy: 24000 examples, pool min=5 max=9 mean=6.6\\n  train_hard: 24000 examples, pool min=10 max=131 mean=18.6\\n=== python_cfr ===\\n  test_easy: 4000 examples, pool min=5 max=9 mean=6.7\\n  test_hard: 4000 examples, pool min=10 max=60 mean=17.7\\n  train_easy: 12000 examples, pool min=5 max=9 mean=6.6\\n  train_hard: 12000 examples, pool min=10 max=131 mean=18.0\\n\", \"stderr\": \"'(ReadTimeoutError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Read timed out. (read timeout=10)\\\"), '(Request ID: 0b9b6547-6c68-42c4-9936-845c1ecbbf02)')' thrown while requesting HEAD https://huggingface.co/datasets/tianyang/repobench-r/resolve/main/data/python_cff.gz\\nRetrying in 1s [Retry 1/5].\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T08:31:23.164666+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/evaluation/eval_repobench.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/evaluation/eval_repobench.py"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T08:31:23.164926+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"StructFuse RepoBench-R Retrieval Evaluation.\\n\\nEvaluates a trained StructFuse bi-encoder on RepoBench-R, a closed-pool\\ncross-file code retrieval benchmark.  Each instance contains a query\\n(import_statement + code context) and a candidate pool (context list);\\nthe task is to rank candidates so the gold snippet appears near the top.\\n\\nDataset: tianyang/repobench-r (gzip-pickled, loaded via huggingface_hub)\\nSubsets: python_cff, python_cfr, java_cff, java_cfr\\nSplits:  train_easy, train_hard, test_easy, test_hard\\n\\nOutputs (in --output-dir):\\n  per_instance_results.jsonl   one JSON object per instance\\n  summary.json                 aggregate Recall@1/5/10, MRR, config\\n\\nUsage:\\n  # Dry-run (no GPU, validates pipeline end-to-end)\\n  python eval_repobench.py --dry-run --output-dir /tmp/repobench_dryrun --limit 20\\n\\n  # Full eval with trained checkpoint\\n  python eval_repobench.py \\\\\\n      --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \\\\\\n      --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen \\\\\\n      --subset python_cff --split test_easy\\n\\nDependencies: torch, transformers, numpy, tqdm, huggingface_hub\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport gzip\\nimport json\\nimport os\\nimport pickle\\nimport sys\\nimport time\\nfrom dataclasses import asdict, dataclass, field\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom tqdm import tqdm\\n\\n\\n# ── Data structures ─────────────────────────────────────────────────\\n\\n@dataclass\\nclass RepoBenchInstance:\\n    instance_id: str\\n    repo_name: str\\n    file_path: str\\n    import_statement: str\\n    code: str\\n    next_line: str\\n    context: list[str]\\n    gold_snippet_index: int\\n\\n\\n@dataclass\\nclass InstanceResult:\\n    instance_id: str\\n    repo_name: st
…[truncated 7328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval_repobench_20260514T082145",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-14T08:31:23.165142+00:00_

脚本确认正确。下面是完整的交付总结。

---

## 交付结果

### 1. RepoBench-R 数据集格式

| 字段 | 类型 | 说明 |
|------|------|------|
| `repo_name` | str | 仓库名 |
| `file_path` | str | 文件路径 |
| `context` | list[str] | 候选代码片段池（闭合检索池） |
| `import_statement` | str | 文件的 import 语句 |
| `code` | str | 待补全的代码上下文 |
| `next_line` | str | 下一行（ground truth） |
| `golden_snippet_index` | int | gold 答案在 context 中的索引 |

**Python 子集统计：**

| Subset | Split | Examples | Pool size |
|--------|-------|----------|-----------|
| python_cff | test_easy | 8,000 | 5-9 (mean 6.6) |
| python_cff | test_hard | 8,000 | 10-60 (mean 17.9) |
| python_cfr | test_easy | 4,000 | 5-9 (mean 6.7) |
| python_cfr | test_hard | 4,000 | 10-60 (mean 17.7) |

数据通过 `huggingface_hub.hf_hub_download` 下载 gzip pickle 文件，绕过 datasets 4.8.4 不兼容 legacy scripts 的问题。

### 2. eval_repobench.py

路径：`/root/structfuse/evaluation/eval_repobench.py`（476 行）

核心逻辑：
- **Query** = `import_statement + "\n" + code`
- **Candidates** = `context` 列表中的每个 snippet
- **Scoring** = bi-encoder 余弦相似度（与 eval_swebench.py 共用 `StructFuseRetriever`）
- **Metrics** = Recall@1/5/10, MRR
- 支持 resume、dry-run（mock 随机分数）、`--limit`

### 3. Dry-run 结果

**test_easy** (10 instances, pool ~6):
```
Recall@1: 0.10, Recall@5: 1.00, Recall@10: 1.00, MRR: 0.36
Chance R@1: 0.17
```

**test_hard** (200 instances, pool ~16):
```
Recall@1: 0.12, Recall@5: 0.42, Recall@10: 0.73, MRR: 0.26
Chance R@1: 0.06
```

随机分数的指标接近 chance level，验证通过。

### 4. 正式 eval 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# python_cff test_easy
python /root/structfuse/evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen_cff_easy \
    --subset python_cff --split test_easy

# python_cff test_hard
python /root/structfuse/evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen_cff_hard \
    --subset python_cff --split test_hard
```

### 5. 预估耗时（单 GPU）

每个 instance 需编码 1 query + ~6-18 candidates。Qwen2.5-Coder-3B 在单 A6000 上约 30-50ms/encode：
- **test_easy** (8000 instances × ~7 candidates): ~30 分钟
- **test_hard** (8000 instances × ~18 candidates): ~60-90 分钟

### 6. 注意事项

- **网络依赖**：首次运行需下载 ~180MB python_cff.gz，必须开启 `network_turbo` 代理。数据下载后会缓存在 `~/.cache/huggingface/hub/`
- **datasets 库不兼容**：`tianyang/repobench-r` 使用 legacy dataset script，datasets>=4.0 无法直接 `load_dataset`，脚本改用 `hf_hub_download` + gzip/pickle 手动解析
- **pool size 差异**：test_easy 的池只有 5-9 个候选，Recall@5 几乎必然为 1.0，主要看 Recall@1 和 MRR；test_hard 池 10-60 个，指标区分度更好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_eval_repobench_20260514T082145"
}
```

</details>

---
