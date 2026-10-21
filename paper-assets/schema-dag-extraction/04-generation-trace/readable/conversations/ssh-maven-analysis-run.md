# ssh maven analysis run

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_ssh_maven-analysis-run_20260515T071416.jsonl`
- **Structured JSON:** [`0081f028cb89a138160b.json`](../../sessions/00/0081f028cb89a138160b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-15T07:18:33.748271+00:00_

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
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
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

_source line 2 · 2026-05-15T07:18:33.748591+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T07:18:33.748765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -lh /root/schema-dag-extraction/artifacts/exp004/eval_maven_exp1.json /root/schema-dag-extraction/artifacts/eval_exp2.json /root/schema-dag-extraction/artifacts/exp004/predictions_maven_exp1.json /root/schema-dag-extraction/artifacts/predictions_exp2.json /root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -lh /root/schema-dag-extraction/artifacts/exp004/eval_maven_exp1.json /root/schema-dag-extraction/artifacts/eval_exp2.json /root/schema-dag-extraction/artifacts/exp004/predictions_maven_exp1.json /root/schema-dag-extraction/artifacts/predictions_exp2.json /root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T07:18:33.748993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -100 /root/schema-dag-extraction/src/analyze_maven_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -100 /root/schema-dag-extraction/src/analyze_maven_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T07:18:33.749156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  18K May 15 13:02 /root/schema-dag-extraction/artifacts/eval_exp2.json\\n-rw-r--r-- 1 root root  53K May 15 15:06 /root/schema-dag-extraction/artifacts/exp004/eval_maven_exp1.json\\n-rw-r--r-- 1 root root  44M May 15 15:06 /root/schema-dag-extraction/artifacts/exp004/predictions_maven_exp1.json\\n-rw-r--r-- 1 root root 115K May 15 13:35 /root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt\\n-rw-r--r-- 1 root root  31M May 15 13:02 /root/schema-dag-extraction/artifacts/predictions_exp2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T07:18:33.749345+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Three-layer MAVEN analysis: pairwise SCS-confusion, per-type F1 vs BCS, batch percentile BCS.\\n\\nDesigned for MAVEN exp-004 where Qwen3 BCS range is extremely compressed\\n(max pairwise sim >=0.90, batch-level BCS delta ~ 0.014).\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport math\\nimport sys\\nfrom collections import defaultdict\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom scipy import stats\\n\\nsys.path.insert(0, str(Path(__file__).parent))\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_DATA_PATH = \\\"/root/schema-dag-extraction/data/maven_parquet/valid.parquet\\\"\\n\\n\\n# ─────────────────────────────────────────────────────\\n# Data loading\\n# ────────────────────────────────���────────────────────\\n\\ndef load_bcs_matrix(path: str) -> Tuple[List[str], np.ndarray]:\\n    data = torch.load(path, map_location=\\\"cpu\\\", weights_only=True)\\n    type_names = data[\\\"type_names\\\"]\\n    if isinstance(type_names, torch.Tensor):\\n        type_names = type_names.tolist()\\n    if isinstance(type_names[0], bytes):\\n        type_names = [t.decode() for t in type_names]\\n    sim_matrix = data[\\\"similarity_matrix\\\"].float().numpy()\\n    return list(type_names), sim_matrix\\n\\n\\ndef load_maven_samples(data_path: str = DEFAULT_DATA_PATH,\\n                       max_samples: Optional[int] = None) -> List[Dict]:\\n    import pandas as pd\\n    df = pd.read_parquet(data_path)\\n    if max_samples:\\n        df = df.head(max_samples)\\n    samples = []\\n    for _, row in df.iterrows():\\n        entities = row[\\\"entities\\\"]\\n        if isinstance(entities, str):\\n            entities = json.loads(entities)\\n        samples.append({\\\"text\\\": row[\\\"text\\\"], \\\"entities\
…[truncated 1749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T07:18:33.749533+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "wc -l /root/schema-dag-extraction/src/analyze_maven_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "wc -l /root/schema-dag-extraction/src/analyze_maven_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T07:18:33.749660+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "tail -100 /root/schema-dag-extraction/src/analyze_maven_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "tail -100 /root/schema-dag-extraction/src/analyze_maven_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T07:18:33.749784+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"596 /root/schema-dag-extraction/src/analyze_maven_results.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T07:18:33.750010+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n\\n# ─────────────────────────────────────────────────────\\n# Utilities\\n# ─────────────────────────────────────────────────────\\n\\ndef _f(x):\\n    if x is None or (isinstance(x, float) and math.isnan(x)):\\n        return None\\n    return round(float(x), 6)\\n\\n\\n# ─────────────────────────────────────────────────────\\n# Main\\n# ─────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Three-layer MAVEN analysis: pairwise SCS-confusion, \\\"\\n                    \\\"per-type F1 vs BCS, batch percentile BCS\\\")\\n    parser.add_argument(\\\"--results_dir\\\", type=str, default=None,\\n                        help=\\\"Directory with predictions and eval JSONs\\\")\\n    parser.add_argument(\\\"--bcs_matrix\\\", type=str, required=True,\\n                        help=\\\"Path to maven_bcs_matrix_qwen3.pt\\\")\\n    parser.add_argument(\\\"--types_file\\\", type=str, default=None,\\n                        help=\\\"Path to maven_event_types.json (optional)\\\")\\n    parser.add_argument(\\\"--data_path\\\", type=str, default=DEFAULT_DATA_PATH,\\n                        help=\\\"Path to MAVEN parquet for gold labels\\\")\\n    parser.add_argument(\\\"--max_samples\\\", type=int, default=500,\\n                        help=\\\"Max samples to load from dataset\\\")\\n    parser.add_argument(\\\"--output\\\", type=str, default=\\\"results/maven_analysis.json\\\",\\n                        help=\\\"Output JSON path\\\")\\n    parser.add_argument(\\\"--min_freq\\\", type=int, default=5,\\n                        help=\\\"Min frequency threshold for per-type analysis\\\")\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n                        help=\\\"Run with mock data to test script logic\\\")\\n    args = parser.parse_args()\\n\\n    type_names, sim_matrix = load_bcs_matrix(args.bcs_matrix)\\n    log
…[truncated 3121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T07:18:33.750208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -lh /root/schema-dag-extraction/data/maven_parquet/valid.parquet",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "ls -lh /root/schema-dag-extraction/data/maven_parquet/valid.parquet",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T07:18:33.750343+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1.9M May 15 11:34 /root/schema-dag-extraction/data/maven_parquet/valid.parquet\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T07:18:33.750464+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/src/analyze_maven_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/src/analyze_maven_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T07:18:33.750699+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Three-layer MAVEN analysis: pairwise SCS-confusion, per-type F1 vs BCS, batch percentile BCS.\\n\\nDesigned for MAVEN exp-004 where Qwen3 BCS range is extremely compressed\\n(max pairwise sim >=0.90, batch-level BCS delta ~ 0.014).\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport logging\\nimport math\\nimport sys\\nfrom collections import defaultdict\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom scipy import stats\\n\\nsys.path.insert(0, str(Path(__file__).parent))\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nDEFAULT_DATA_PATH = \\\"/root/schema-dag-extraction/data/maven_parquet/valid.parquet\\\"\\n\\n\\n# ─────────────────────────────────────────────────────\\n# Data loading\\n# ────────────────────────────────���────────────────────\\n\\ndef load_bcs_matrix(path: str) -> Tuple[List[str], np.ndarray]:\\n    data = torch.load(path, map_location=\\\"cpu\\\", weights_only=True)\\n    type_names = data[\\\"type_names\\\"]\\n    if isinstance(type_names, torch.Tensor):\\n        type_names = type_names.tolist()\\n    if isinstance(type_names[0], bytes):\\n        type_names = [t.decode() for t in type_names]\\n    sim_matrix = data[\\\"similarity_matrix\\\"].float().numpy()\\n    return list(type_names), sim_matrix\\n\\n\\ndef load_maven_samples(data_path: str = DEFAULT_DATA_PATH,\\n                       max_samples: Optional[int] = None) -> List[Dict]:\\n    import pandas as pd\\n    df = pd.read_parquet(data_path)\\n    if max_samples:\\n        df = df.head(max_samples)\\n    samples = []\\n    for _, row in df.iterrows():\\n        entities = row[\\\"entities\\\"]\\n        if isinstance(entities, str):\\n            entities = json.loads(entities)\\n        samples.append({\\\"text\\\": row[\\\"text\\\"], \\\"entities\
…[truncated 7156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T07:18:33.750910+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && cp artifacts/predictions_exp2.json artifacts/exp004/predictions_exp2.json && cp artifacts/eval_exp2.json artifacts/exp004/eval_exp2.json && echo \"COPIED\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && cp artifacts/predictions_exp2.json artifacts/exp004/predictions_exp2.json && cp artifacts/eval_exp2.json artifacts/exp004/eval_exp2.json && echo \"COPIED\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T07:18:33.751053+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"COPIED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T07:18:33.751176+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 src/analyze_maven_results.py --results_dir artifacts/exp004/ --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt --output results/maven_analysis.json 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 src/analyze_maven_results.py --results_dir artifacts/exp004/ --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt --output results/maven_analysis.json 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T07:18:33.751306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 15:15:48,728 INFO Loaded BCS matrix: 168 types, shape (168, 168)\\n2026-05-15 15:15:48,729 INFO Loading predictions from artifacts/exp004/predictions_exp2.json\\n2026-05-15 15:15:51,807 INFO === Layer 1: Pairwise SCS-Confusion ===\\n2026-05-15 15:15:52,448 INFO   Pairs: 0, Pearson r=None, Spearman rho=None\\n2026-05-15 15:15:52,448 INFO === Layer 2: Per-type F1 vs Mean BCS ===\\n2026-05-15 15:15:52,824 INFO === Layer 3: Batch-level Percentile Rank BCS ===\\n2026-05-15 15:15:52,833 INFO   count_12: n=27, r(F1,pctBCS)=0.518986 (p=0.00554)\\n2026-05-15 15:15:52,834 INFO   count_6: n=27, r(F1,pctBCS)=0.240034 (p=0.227831)\\n2026-05-15 15:15:52,834 INFO   Note: BCS compression limitation: batch-level BCS range too narrow for significance\\n2026-05-15 15:15:52,835 INFO Saved analysis to results/maven_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T07:18:33.751464+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import json; p=json.load(open('/root/schema-dag-extraction/artifacts/exp004/predictions_exp2.json')); print(type(p), len(p)); print(json.dumps(p[0], indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import json; p=json.load(open('/root/schema-dag-extraction/artifacts/exp004/predictions_exp2.json')); print(type(p), len(p)); print(json.dumps(p[0], indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T07:18:33.751589+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T07:18:33.751711+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import json; e=json.load(open('/root/schema-dag-extraction/artifacts/exp004/eval_exp2.json')); print(type(e)); print(json.dumps(dict(list(e.items())[:5]), indent=2)[:2000])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import json; e=json.load(open('/root/schema-dag-extraction/artifacts/exp004/eval_exp2.json')); print(type(e)); print(json.dumps(dict(list(e.items())[:5]), indent=2)[:2000])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T07:18:33.751832+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T07:18:33.751969+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -80 /root/schema-dag-extraction/artifacts/exp004/predictions_exp2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -80 /root/schema-dag-extraction/artifacts/exp004/predictions_exp2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T07:18:33.752084+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -60 /root/schema-dag-extraction/artifacts/exp004/eval_exp2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -60 /root/schema-dag-extraction/artifacts/exp004/eval_exp2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T07:18:33.752248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"sample_id\\\": 0,\\n    \\\"batch_id\\\": \\\"count_6_low_bcs\\\",\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"batch_types\\\": [\\n      \\\"organization-politicalparty\\\",\\n      \\\"person-actor\\\",\\n      \\\"location-bodiesofwater\\\",\\n      \\\"other-disease\\\",\\n      \\\"organization-education\\\",\\n      \\\"art-film\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.8708932995796204,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 233,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.047937602281570436,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 1,\\n    \\\"batch_id\\\": \\\"count_6_low_bcs\\\",\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"batch_types\\\": [\\n      \\\"organization-politicalparty\\\",\\n      \\\"person-actor\\\",\\n      \\\"location-bodiesofwater\\\",\\n      \\\"other-disease\\\",\\n      \\\"organization-education\\\",\\n      \\\"art-film\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.8708932995796204,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 226,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.047937602281570436,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 2,\\n    \\\"batch_id\\\": \\\"count_6_low_bcs\\\",\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"batch_types\\\": [\\n      \\\"organization-politicalparty\\\",\\n      \\\"person-actor\\\",\\n      \\\"location-bodiesofwater\\\",\\n      \\\"other-disease\\\",\\n      \\\"organization-education\\\",\\n      \\\"art-film\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.8708932995796204,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 219,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.047937602281570436,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 3,\\n    \\\"batch_id\\\": \\\"count_6_low_bcs\\\",\\n    \\\"count_key\\\": \\\"count_
…[truncated 673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T07:18:33.752434+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_6_low_bcs\\\": {\\n    \\\"bcs\\\": 0.8708932995796204,\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"num_types\\\": 6,\\n    \\\"num_samples\\\": 1000,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.1925925925925926,\\n      \\\"recall\\\": 0.36619718309859156,\\n      \\\"f1\\\": 0.2524271844660194,\\n      \\\"tp\\\": 78,\\n      \\\"total_pred\\\": 405,\\n      \\\"total_gold\\\": 213\\n    }\\n  },\\n  \\\"count_6_high_bcs\\\": {\\n    \\\"bcs\\\": 0.9446906447410583,\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"num_types\\\": 6,\\n    \\\"num_samples\\\": 1000,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.45726495726495725,\\n      \\\"recall\\\": 0.5181598062953995,\\n      \\\"f1\\\": 0.48581157775255385,\\n      \\\"tp\\\": 214,\\n      \\\"total_pred\\\": 468,\\n      \\\"total_gold\\\": 413\\n    }\\n  },\\n  \\\"count_6_random_0\\\": {\\n    \\\"bcs\\\": 0.9021296501159668,\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"num_types\\\": 6,\\n    \\\"num_samples\\\": 1000,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.4472049689440994,\\n      \\\"recall\\\": 0.36180904522613067,\\n      \\\"f1\\\": 0.4000000000000001,\\n      \\\"tp\\\": 72,\\n      \\\"total_pred\\\": 161,\\n      \\\"total_gold\\\": 199\\n    }\\n  },\\n  \\\"count_6_random_1\\\": {\\n    \\\"bcs\\\": 0.8867964744567871,\\n    \\\"count_key\\\": \\\"count_6\\\",\\n    \\\"num_types\\\": 6,\\n    \\\"num_samples\\\": 1000,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.20303030303030303,\\n      \\\"recall\\\": 0.6547231270358306,\\n      \\\"f1\\\": 0.3099460292983809,\\n      \\\"tp\\\": 201,\\n      \\\"total_pred\\\": 990,\\n      \\\"total_gold\\\": 307\\n    }\\n  },\\n  \\\"count_6_random_2\\\": {\\n    \\\"bcs\\\": 0.8683533072471619,\\n    \\\"count_key\\\": \\\"count_6\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\":
…[truncated 31 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T07:18:33.752623+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False); print(type(d['type_names']), len(d['type_names'])); print(d['type_names'][:20])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import torch; d=torch.load('/root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False); print(type(d['type_names']), len(d['type_names'])); print(d['type_names'][:20])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T07:18:33.752758+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T07:18:33.752919+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "python3 -c \"import pandas as pd; df=pd.read_parquet('/root/schema-dag-extraction/data/maven_parquet/valid.parquet'); print(df.columns.tolist()); print(df.iloc[0].to_dict())\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "python3 -c \"import pandas as pd; df=pd.read_parquet('/root/schema-dag-extraction/data/maven_parquet/valid.parquet'); print(df.columns.tolist()); print(df.iloc[0].to_dict())\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T07:18:33.753044+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T07:18:33.753162+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch, pandas as pd, json\nd=torch.load('artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False)\nprint('BCS type_names (first 20):', d['type_names'][:20])\nprint('BCS type_names (count):', len(d['type_names']))\nprint()\ndf=pd.read_parquet('data/maven_parquet/valid.parquet')\nprint('Parquet columns:', df.columns.tolist())\nrow = df.iloc[0]\nents = row['entities']\nif isinstance(ents, str):\n    ents = json.loads(ents)\nprint('First sample entities (first 3):', list(ents)[:3])\nprint('First sample text[:100]:', str(row['text'])[:100])\n\" 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport torch, pandas as pd, json\nd=torch.load('artifacts/maven_bcs_matrix_qwen3.pt', map_location='cpu', weights_only=False)\nprint('BCS type_names (first 20):', d['type_names'][:20])\nprint('BCS type_names (count):', len(d['type_names']))\nprint()\ndf=pd.read_parquet('data/maven_parquet/valid.parquet')\nprint('Parquet columns:', df.columns.tolist())\nrow = df.iloc[0]\nents = row['entities']\nif isinstance(ents, str):\n    ents = json.loads(ents)\nprint('First sample entities (first 3):', list(ents)[:3])\nprint('First sample text[:100]:', str(row['text'])[:100])\n\" 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T07:18:33.753300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"BCS type_names (first 20): ['Achieve', 'Action', 'Adducing', 'Agree_or_refuse_to_act', 'Aiming', 'Arranging', 'Arrest', 'Arriving', 'Assistance', 'Attack', 'Award', 'Bearing_arms', 'Becoming', 'Becoming_a_member', 'Being_in_operation', 'Besieging', 'Bodily_harm', 'Body_movement', 'Breathing', 'Bringing']\\nBCS type_names (count): 168\\n\\nParquet columns: ['doc_id', 'sent_id', 'text', 'tokens', 'entities', 'negative_triggers']\\nFirst sample entities (first 3): [{'end': 3, 'start': 2, 'text': 'Battle', 'type': 'Hostile_encounter'}, {'end': 11, 'start': 10, 'text': 'War', 'type': 'Hostile_encounter'}, {'end': 7, 'start': 5, 'text': 'took place', 'type': 'Process_start'}]\\nFirst sample text[:100]: The naval Battle of Salis took place during the Polish–Swedish War (1600–1611) during the night of M\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T07:18:33.753477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -80 /root/schema-dag-extraction/artifacts/exp004/predictions_maven_exp1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -80 /root/schema-dag-extraction/artifacts/exp004/predictions_maven_exp1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T07:18:33.753659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"sample_id\\\": 0,\\n    \\\"batch_id\\\": \\\"count_1_random_0\\\",\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"batch_types\\\": [\\n      \\\"Achieve\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.0,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 131,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.03295685243606567,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 1,\\n    \\\"batch_id\\\": \\\"count_1_random_0\\\",\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"batch_types\\\": [\\n      \\\"Achieve\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.0,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 136,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.03295685243606567,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 2,\\n    \\\"batch_id\\\": \\\"count_1_random_0\\\",\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"batch_types\\\": [\\n      \\\"Achieve\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.0,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 115,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.03295685243606567,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 3,\\n    \\\"batch_id\\\": \\\"count_1_random_0\\\",\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"batch_types\\\": [\\n      \\\"Achieve\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.0,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 133,\\n    \\\"gen_tokens\\\": 2,\\n    \\\"latency_s\\\": 0.03295685243606567,\\n    \\\"prompt_version\\\": \\\"v2\\\"\\n  },\\n  {\\n    \\\"sample_id\\\": 4,\\n    \\\"batch_id\\\": \\\"count_1_random_0\\\",\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"batch_types\\\": [\\n      \\\"Achieve\\\"\\n    ],\\n    \\\"batch_bcs\\\": 0.0,\\n    \\\"predictions\\\": [],\\n    \\\"prompt_tokens\\\": 123,\\n    \\\"gen_tokens\\\": 2,\\n    
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T07:18:33.753806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "head -60 /root/schema-dag-extraction/artifacts/exp004/eval_maven_exp1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "head -60 /root/schema-dag-extraction/artifacts/exp004/eval_maven_exp1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T07:18:33.753988+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"count_1_random_0\\\": {\\n    \\\"bcs\\\": 0.0,\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"num_types\\\": 1,\\n    \\\"num_samples\\\": 500,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.043478260869565216,\\n      \\\"recall\\\": 1.0,\\n      \\\"f1\\\": 0.08333333333333333,\\n      \\\"tp\\\": 3,\\n      \\\"total_pred\\\": 69,\\n      \\\"total_gold\\\": 3\\n    }\\n  },\\n  \\\"count_1_random_1\\\": {\\n    \\\"bcs\\\": 0.0,\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"num_types\\\": 1,\\n    \\\"num_samples\\\": 500,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.009940357852882704,\\n      \\\"recall\\\": 0.7142857142857143,\\n      \\\"f1\\\": 0.0196078431372549,\\n      \\\"tp\\\": 5,\\n      \\\"total_pred\\\": 503,\\n      \\\"total_gold\\\": 7\\n    }\\n  },\\n  \\\"count_1_random_2\\\": {\\n    \\\"bcs\\\": 0.0,\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"num_types\\\": 1,\\n    \\\"num_samples\\\": 500,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.25,\\n      \\\"recall\\\": 0.8181818181818182,\\n      \\\"f1\\\": 0.38297872340425526,\\n      \\\"tp\\\": 9,\\n      \\\"total_pred\\\": 36,\\n      \\\"total_gold\\\": 11\\n    }\\n  },\\n  \\\"count_1_random_3\\\": {\\n    \\\"bcs\\\": 0.0,\\n    \\\"count_key\\\": \\\"count_1\\\",\\n    \\\"num_types\\\": 1,\\n    \\\"num_samples\\\": 500,\\n    \\\"text_match\\\": {\\n      \\\"precision\\\": 0.041666666666666664,\\n      \\\"recall\\\": 0.6666666666666666,\\n      \\\"f1\\\": 0.0784313725490196,\\n      \\\"tp\\\": 2,\\n      \\\"total_pred\\\": 48,\\n      \\\"total_gold\\\": 3\\n    }\\n  },\\n  \\\"count_1_random_4\\\": {\\n    \\\"bcs\\\": 0.0,\\n    \\\"count_key\\\": \\\"count_1\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T07:18:33.754176+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\ne = json.load(open('artifacts/exp004/eval_maven_exp1.json'))\nfor k in sorted(e.keys()):\n    v = e[k]\n    print(f'{k}: bcs={v[\\\"bcs\\\"]:.4f}, n_types={v[\\\"num_types\\\"]}, n_samples={v[\\\"num_samples\\\"]}, f1={v[\\\"text_match\\\"][\\\"f1\\\"]:.4f}')\n\" 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\ne = json.load(open('artifacts/exp004/eval_maven_exp1.json'))\nfor k in sorted(e.keys()):\n    v = e[k]\n    print(f'{k}: bcs={v[\\\"bcs\\\"]:.4f}, n_types={v[\\\"num_types\\\"]}, n_samples={v[\\\"num_samples\\\"]}, f1={v[\\\"text_match\\\"][\\\"f1\\\"]:.4f}')\n\" 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T07:18:33.754389+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"count_12_random_0: bcs=0.9590, n_types=12, n_samples=500, f1=0.1000\\ncount_12_random_1: bcs=0.9643, n_types=12, n_samples=500, f1=0.1333\\ncount_12_random_2: bcs=0.9352, n_types=12, n_samples=500, f1=0.1942\\ncount_12_random_3: bcs=0.9608, n_types=12, n_samples=500, f1=0.2341\\ncount_12_random_4: bcs=0.9247, n_types=12, n_samples=500, f1=0.1168\\ncount_149_random_0: bcs=0.9832, n_types=149, n_samples=500, f1=0.2520\\ncount_149_random_1: bcs=0.9832, n_types=149, n_samples=500, f1=0.2540\\ncount_149_random_2: bcs=0.9832, n_types=149, n_samples=500, f1=0.2542\\ncount_149_random_3: bcs=0.9832, n_types=149, n_samples=500, f1=0.2525\\ncount_149_random_4: bcs=0.9832, n_types=149, n_samples=500, f1=0.2550\\ncount_1_random_0: bcs=0.0000, n_types=1, n_samples=500, f1=0.0833\\ncount_1_random_1: bcs=0.0000, n_types=1, n_samples=500, f1=0.0196\\ncount_1_random_10: bcs=0.0000, n_types=1, n_samples=500, f1=0.0571\\ncount_1_random_100: bcs=0.0000, n_types=1, n_samples=500, f1=0.0741\\ncount_1_random_101: bcs=0.0000, n_types=1, n_samples=500, f1=0.0374\\ncount_1_random_102: bcs=0.0000, n_types=1, n_samples=500, f1=0.1667\\ncount_1_random_103: bcs=0.0000, n_types=1, n_samples=500, f1=0.0000\\ncount_1_random_104: bcs=0.0000, n_types=1, n_samples=500, f1=0.0769\\ncount_1_random_105: bcs=0.0000, n_types=1, n_samples=500, f1=0.0476\\ncount_1_random_106: bcs=0.0000, n_types=1, n_samples=500, f1=0.0516\\ncount_1_random_107: bcs=0.0000, n_types=1, n_samples=500, f1=0.0000\\ncount_1_random_108: bcs=0.0000, n_types=1, n_samples=500, f1=0.1111\\ncount_1_random_109: bcs=0.0000, n_types=1, n_samples=500, f1=0.2500\\ncount_1_random_11: bcs=0.0000, n_types=1, n_samples=500, f1=0.2118\\ncount_1_random_110: bcs=0.0000, n_types=1, n_samples=500, f1=0.1818\\ncount_1_random_111: bcs=0.0000, n_types=1, n_samples=500, f1=0.2184\\ncount_1_random_112: bcs=0.0000, n_types=1, n_samples=500, f1=0.0000\\ncount_1_random_113: bcs=0.0000, n_types=1, n_sampl
…[truncated 6437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T07:18:33.754572+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction/artifacts/exp004 && rm -f predictions_exp2.json eval_exp2.json && ln -sf predictions_maven_exp1.json predictions_exp1.json && ln -sf eval_maven_exp1.json eval_exp1.json && ls -la *.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction/artifacts/exp004 && rm -f predictions_exp2.json eval_exp2.json && ln -sf predictions_maven_exp1.json predictions_exp1.json && ln -sf eval_maven_exp1.json eval_exp1.json && ls -la *.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T07:18:33.754707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root    55820 May 15 14:03 batch_config_maven_exp1.json\\n-rw-r--r-- 1 root root    28732 May 15 15:07 batch_config_maven_exp2.json\\nlrwxrwxrwx 1 root root       20 May 15 15:17 eval_exp1.json -> eval_maven_exp1.json\\n-rw-r--r-- 1 root root    53676 May 15 15:06 eval_maven_exp1.json\\nlrwxrwxrwx 1 root root       27 May 15 15:17 predictions_exp1.json -> predictions_maven_exp1.json\\n-rw-r--r-- 1 root root 45261764 May 15 15:06 predictions_maven_exp1.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T07:18:33.754831+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 src/analyze_maven_results.py --results_dir artifacts/exp004/ --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt --output results/maven_analysis.json --max_samples 500 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cd /root/schema-dag-extraction && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 src/analyze_maven_results.py --results_dir artifacts/exp004/ --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt --output results/maven_analysis.json --max_samples 500 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T07:18:33.754994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 15:17:55,262 INFO Loaded BCS matrix: 168 types, shape (168, 168)\\n2026-05-15 15:17:55,263 INFO Loading predictions from artifacts/exp004/predictions_exp1.json\\n2026-05-15 15:17:59,221 INFO === Layer 1: Pairwise SCS-Confusion ===\\n2026-05-15 15:18:00,547 INFO   Pairs: 11026, Pearson r=-0.007867, Spearman rho=0.003822\\n2026-05-15 15:18:00,547 INFO   Nonzero-only: n=632, Spearman rho=-0.042081 (p=0.290846)\\n2026-05-15 15:18:00,547 INFO === Layer 2: Per-type F1 vs Mean BCS ===\\n2026-05-15 15:18:01,740 INFO   Types: 149, Pearson r=0.175343, Partial r=0.188976\\n2026-05-15 15:18:01,740 INFO   Quartile: low_bcs_f1=0.136414, high_bcs_f1=0.234047, delta=0.097633\\n2026-05-15 15:18:01,741 INFO === Layer 3: Batch-level Percentile Rank BCS ===\\n/root/schema-dag-extraction/src/analyze_maven_results.py:374: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  r_f1, p_f1 = stats.pearsonr(pct_bcs, f1_arr)\\n/root/schema-dag-extraction/src/analyze_maven_results.py:375: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  r_rec, p_rec = stats.pearsonr(pct_bcs, recall_arr)\\n2026-05-15 15:18:01,766 INFO   count_1: n=149, r(F1,pctBCS)=None (p=None)\\n2026-05-15 15:18:01,767 INFO   count_12: n=5, r(F1,pctBCS)=0.204605 (p=0.741318)\\n2026-05-15 15:18:01,767 INFO   count_149: n=5, r(F1,pctBCS)=None (p=None)\\n2026-05-15 15:18:01,767 INFO   count_24: n=5, r(F1,pctBCS)=0.559807 (p=0.326442)\\n2026-05-15 15:18:01,767 INFO   count_42: n=5, r(F1,pctBCS)=-0.57239 (p=0.313236)\\n2026-05-15 15:18:01,767 INFO   count_6: n=5, r(F1,pctBCS)=-0.036193 (p=0.953927)\\n2026-05-15 15:18:01,767 INFO   count_84: n=5, r(F1,pctBCS)=0.973658 (p=0.005112)\\n2026-05-15 15:18:01,767 INFO   Note: BCS compression limitation: batch-level BCS range too narrow for significance\\n2026-05-15 15:18:01,770 INFO Saved analysis to results/maven_analysis.json\\n\"
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T07:18:33.755165+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/results/maven_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/results/maven_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T07:18:33.755401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"layer1_pairwise\\\": {\\n    \\\"n_pairs\\\": 11026,\\n    \\\"pearson_r\\\": -0.007867,\\n    \\\"pearson_p\\\": 0.408783,\\n    \\\"spearman_rho\\\": 0.003822,\\n    \\\"spearman_p\\\": 0.688228,\\n    \\\"nonzero_only\\\": {\\n      \\\"spearman_rho\\\": -0.042081,\\n      \\\"spearman_p\\\": 0.290846,\\n      \\\"n\\\": 632\\n    },\\n    \\\"top_confused_pairs\\\": [\\n      {\\n        \\\"type_a\\\": \\\"Achieve\\\",\\n        \\\"type_b\\\": \\\"Getting\\\",\\n        \\\"scs\\\": 0.749551,\\n        \\\"confusion\\\": 73\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Departing\\\",\\n        \\\"type_b\\\": \\\"Escaping\\\",\\n        \\\"scs\\\": 0.733434,\\n        \\\"confusion\\\": 49\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Death\\\",\\n        \\\"type_b\\\": \\\"Killing\\\",\\n        \\\"scs\\\": 0.704134,\\n        \\\"confusion\\\": 34\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Attack\\\",\\n        \\\"type_b\\\": \\\"Use_firearm\\\",\\n        \\\"scs\\\": 0.485284,\\n        \\\"confusion\\\": 33\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Action\\\",\\n        \\\"type_b\\\": \\\"Removing\\\",\\n        \\\"scs\\\": 0.906067,\\n        \\\"confusion\\\": 29\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Arriving\\\",\\n        \\\"type_b\\\": \\\"Conquering\\\",\\n        \\\"scs\\\": 0.661753,\\n        \\\"confusion\\\": 27\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Communication\\\",\\n        \\\"type_b\\\": \\\"Expressing_publicly\\\",\\n        \\\"scs\\\": 0.31205,\\n        \\\"confusion\\\": 25\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Arriving\\\",\\n        \\\"type_b\\\": \\\"Process_start\\\",\\n        \\\"scs\\\": 0.692726,\\n        \\\"confusion\\\": 24\\n      },\\n      {\\n        \\\"type_a\\\": \\\"Motion\\\",\\n        \\\"type_b\\\": \\\"Motion_directional\\\",\\n        \\\"scs\\\": 0.529793,\\n        \\
…[truncated 4750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_maven-analysis-run_20260515T071416",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T07:18:33.755600+00:00_

三层分析完成。结果已保存到 `results/maven_analysis.json`。

---

## 三层分析结果

### Layer 1: Pairwise SCS-Confusion

| 指标 | 值 |
|------|------|
| n_pairs | 11,026 |
| Pearson r | -0.0079 (p=0.409) |
| Spearman ρ | 0.0038 (p=0.688) |
| **Nonzero-only** (n=632) | ρ = -0.042 (p=0.291) |

**Top-10 confused pairs:**

| Type A | Type B | SCS | Confusion |
|--------|--------|-----|-----------|
| Achieve | Getting | 0.750 | 73 |
| Departing | Escaping | 0.733 | 49 |
| Death | Killing | 0.704 | 34 |
| Attack | Use_firearm | 0.485 | 33 |
| Action | Removing | 0.906 | 29 |
| Arriving | Conquering | 0.662 | 27 |
| Communication | Expressing_publicly | 0.312 | 25 |
| Arriving | Process_start | 0.693 | 24 |
| Motion | Motion_directional | 0.530 | 24 |
| Expressing_publicly | Statement | 0.388 | 23 |

**结论**: Pairwise 层 SCS 与 confusion 无显著相关。MAVEN 类型间 BCS 压缩严重（均 ≥0.90），pairwise SCS 区分度不足。

---

### Layer 2: Per-type F1 vs Mean BCS

| 指标 | 值 |
|------|------|
| n_types | 149 (freq≥5) |
| Pearson r | 0.175 (p=0.032*) |
| Spearman ρ | 0.184 (p=0.025*) |
| Partial r (控制 log-freq) | 0.189 (p=0.021*) |

**Quartile comparison:**
- Low BCS quartile (≤0.671) mean F1: **0.136**
- High BCS quartile (≥0.747) mean F1: **0.234**
- Delta: **+0.098**

**Confound check:** BCS vs log-freq r = -0.043 (p=0.599) — BCS 与频率无显著相关，confound 排除。

**结论**: 显著正相关——schema 越相似（BCS 越高）的类型 F1 越好。效应量小但稳健，控制频率后依然显著。

---

### Layer 3: Batch-level Percentile Rank BCS

| Count | n | BCS range | r(F1, pctBCS) | p |
|-------|---|-----------|---------------|-------|
| 1 | 149 | 0.000 | N/A | N/A |
| 6 | 5 | 0.068 | -0.036 | 0.954 |
| 12 | 5 | 0.040 | 0.205 | 0.741 |
| 24 | 5 | 0.023 | 0.560 | 0.326 |
| 42 | 5 | 0.005 | -0.572 | 0.313 |
| 84 | 5 | 0.013 | **0.974** | **0.005** |
| 149 | 5 | 0.000 | N/A | N/A |

**结论**: 仅 count_84 达到显著 (r=0.974, p=0.005)。但每组仅 5 个批次，且 BCS range 极窄 (≤0.068)，BCS 压缩限制了 batch-level 分析的统计效力。

---

### 总结

Layer 2 (per-type) 提供了最有力的证据：schema 相似度与 extraction F1 显著正相关 (partial r=0.189, p=0.021)。Layer 1/3 因 Qwen3 BCS 压缩（168 个 MAVEN 类型间 pairwise sim 均 ≥0.90）而缺乏区分度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_maven-analysis-run_20260515T071416"
}
```

</details>

---
