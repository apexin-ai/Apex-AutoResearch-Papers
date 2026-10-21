# audit permutation test statistic

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_audit_permutation_test_statistic_20260521T140801.jsonl`
- **Structured JSON:** [`611aca3cf69fed994dbc.json`](../../sessions/61/611aca3cf69fed994dbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-21T14:11:10.324093+00:00_

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
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
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

_source line 2 · 2026-05-21T14:11:10.324365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T14:11:10.324560+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T14:11:10.324699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/results/analysis -name \"*exp002*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/results/analysis -name \"*exp002*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T14:11:10.324966+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Gradient permutation test across 5 benchmarks.\\n\\nTests whether item_id% monotonically decreases (and model:item_id% monotonically\\nincreases) across benchmarks ordered by cognitive complexity, using an exact\\npermutation test over 5! = 120 orderings.\\n\\nInput:  Per-benchmark G-study results (exp-002) + optionally exp-001 MMLU results.\\nOutput: results/analysis/gradient_permutation_test.json\\n\\nUsage:\\n  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002\\n  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002 --exp001-gstudy results/analysis/exp001_gstudy.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations, permutations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[2]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\n\\nBENCHMARK_ORDER = [\\\"mmlu\\\", \\\"arc\\\", \\\"hellaswag\\\", \\\"gsm8k\\\", \\\"math\\\"]\\n\\n\\ndef load_exp002_data(data_dir: str) -> pd.DataFrame:\\n    data_path = Path(data_dir)\\n    jsonl_files = sorted(data_path.glob(\\\"*.jsonl\\\"))\\n    if not jsonl_files:\\n        raise FileNotFoundError(f\\\"No JSONL files in {data_dir}\\\")\\n    frames = [pd.read_json(f, lines=True) for f in jsonl_files]\\n    df = pd.concat(frames, ignore_index=True)\\n    if \\\"top_logprobs\\\" in df.columns:\\n        df.drop(columns=[\\\"top_logprobs\\\"], inplace=True)\\n    df[\\\"model\\\"] = df[\\\"model\\\"].map(normalize_model_name).fillna(df[\\\"model\\\"])\\n    for f in FACETS:\\n        df[f] = df[f].astype(str)\\n    return df\\n\\n\\ndef compute_henderson_i(df: pd.DataFrame, response: str, f
…[truncated 7207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T14:11:10.325129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/analysis/exp002_prep_report.md\\n/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T14:11:10.325306+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -n \"def permutation_test\\|def is_monotonic\\|spearman\\|kendall\\|linear_contrast\\|observed_stat\\|p_value\\|test_stat\\|rho\\|tau\\|contrast_coeff\" /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -n \"def permutation_test\\|def is_monotonic\\|spearman\\|kendall\\|linear_contrast\\|observed_stat\\|p_value\\|test_stat\\|rho\\|tau\\|contrast_coeff\" /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T14:11:10.325466+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T14:11:10.325592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T14:11:10.325922+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-002\\\",\\n  \\\"analysis\\\": \\\"per_benchmark_henderson_i_gstudy\\\",\\n  \\\"facets\\\": [\\n    \\\"model\\\",\\n    \\\"temperature\\\",\\n    \\\"prompt_template\\\",\\n    \\\"seed\\\",\\n    \\\"ordering\\\",\\n    \\\"item_id\\\"\\n  ],\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"benchmark\\\": \\\"mmlu\\\",\\n      \\\"n_observations\\\": 230400,\\n      \\\"n_levels\\\": {\\n        \\\"model\\\": 4,\\n        \\\"temperature\\\": 2,\\n        \\\"prompt_template\\\": 6,\\n        \\\"seed\\\": 6,\\n        \\\"ordering\\\": 4,\\n        \\\"item_id\\\": 200\\n      },\\n      \\\"grand_mean_accuracy\\\": 0.700247,\\n      \\\"variance_components\\\": {\\n        \\\"item_id\\\": {\\n          \\\"estimate\\\": 0.0876133124,\\n          \\\"pct\\\": 41.5471\\n        },\\n        \\\"model:item_id\\\": {\\n          \\\"estimate\\\": 0.0691895248,\\n          \\\"pct\\\": 32.8103\\n        },\\n        \\\"residual\\\": {\\n          \\\"estimate\\\": 0.043262815,\\n          \\\"pct\\\": 20.5156\\n        },\\n        \\\"prompt_template:item_id\\\": {\\n          \\\"estimate\\\": 0.0029608526,\\n          \\\"pct\\\": 1.4041\\n        },\\n        \\\"seed:item_id\\\": {\\n          \\\"estimate\\\": 0.0025039227,\\n          \\\"pct\\\": 1.1874\\n        },\\n        \\\"temperature:item_id\\\": {\\n          \\\"estimate\\\": 0.00249588,\\n          \\\"pct\\\": 1.1836\\n        },\\n        \\\"model\\\": {\\n          \\\"estimate\\\": 0.0015897059,\\n          \\\"pct\\\": 0.7539\\n        },\\n        \\\"ordering:item_id\\\": {\\n          \\\"estimate\\\": 0.0010917321,\\n          \\\"pct\\\": 0.5177\\n        },\\n        \\\"model:temperature\\\": {\\n          \\\"estimate\\\": 6.01697e-05,\\n          \\\"pct\\\": 0.0285\\n        },\\n        \\\"model:prompt_template\\\": {\\n          \\\"estimate\\\": 3.90555e-05,\\n          \\\"
…[truncated 8518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T14:11:10.326111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -160 /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -160 /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T14:11:10.326315+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Gradient permutation test across 5 benchmarks.\\n\\nTests whether item_id% monotonically decreases (and model:item_id% monotonically\\nincreases) across benchmarks ordered by cognitive complexity, using an exact\\npermutation test over 5! = 120 orderings.\\n\\nInput:  Per-benchmark G-study results (exp-002) + optionally exp-001 MMLU results.\\nOutput: results/analysis/gradient_permutation_test.json\\n\\nUsage:\\n  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002\\n  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002 --exp001-gstudy results/analysis/exp001_gstudy.json\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations, permutations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[2]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\n\\nBENCHMARK_ORDER = [\\\"mmlu\\\", \\\"arc\\\", \\\"hellaswag\\\", \\\"gsm8k\\\", \\\"math\\\"]\\n\\n\\ndef load_exp002_data(data_dir: str) -> pd.DataFrame:\\n    data_path = Path(data_dir)\\n    jsonl_files = sorted(data_path.glob(\\\"*.jsonl\\\"))\\n    if not jsonl_files:\\n        raise FileNotFoundError(f\\\"No JSONL files in {data_dir}\\\")\\n    frames = [pd.read_json(f, lines=True) for f in jsonl_files]\\n    df = pd.concat(frames, ignore_index=True)\\n    if \\\"top_logprobs\\\" in df.columns:\\n        df.drop(columns=[\\\"top_logprobs\\\"], inplace=True)\\n    df[\\\"model\\\"] = df[\\\"model\\\"].map(normalize_model_name).fillna(df[\\\"model\\\"])\\n    for f in FACETS:\\n        df[f] = df[f].astype(str)\\n    return df\\n\\n\\ndef compute_henderson_i(df: pd.DataFrame, response: str, f
…[truncated 4971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T14:11:10.326481+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T14:11:10.326613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"34:def load_exp002_data(data_dir: str) -> pd.DataFrame:\\n49:def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]) -> dict:\\n106:def is_monotonic_decreasing(values: list[float]) -> bool:\\n110:def is_monotonic_increasing(values: list[float]) -> bool:\\n114:def permutation_test(values_by_benchmark: dict[str, float], benchmark_order: list[str],\\n149:def load_exp001_gstudy(path: str) -> dict | None:\\n158:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T14:11:10.326768+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); arc=d['benchmarks']['arc']; print(json.dumps({k: arc[k] for k in ['benchmark','n_observations','grand_mean_accuracy','total_variance']}, indent=2)); vc=arc['variance_components']; [print(f'{k}: est={v[\\\"estimate\\\"]}, pct={v[\\\"pct\\\"]}') for k,v in vc.items() if v['estimate']>0]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); arc=d['benchmarks']['arc']; print(json.dumps({k: arc[k] for k in ['benchmark','n_observations','grand_mean_accuracy','total_variance']}, indent=2)); vc=arc['variance_components']; [print(f'{k}: est={v[\\\"estimate\\\"]}, pct={v[\\\"pct\\\"]}') for k,v in vc.items() if v['estimate']>0]\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T14:11:10.326891+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T14:11:10.327004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/gradient_permutation_test.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/gradient_permutation_test.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T14:11:10.327169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-002 (+ optional exp-001)\\\",\\n  \\\"benchmark_order_hypothesis\\\": [\\n    \\\"mmlu\\\",\\n    \\\"arc\\\",\\n    \\\"hellaswag\\\",\\n    \\\"gsm8k\\\",\\n    \\\"math\\\"\\n  ],\\n  \\\"benchmark_stats\\\": {\\n    \\\"arc\\\": {\\n      \\\"item_id_pct\\\": 48.89986395195155,\\n      \\\"model_item_pct\\\": 38.19723003554425,\\n      \\\"n_obs\\\": 230400,\\n      \\\"accuracy\\\": 0.8178298611111111\\n    },\\n    \\\"gsm8k\\\": {\\n      \\\"item_id_pct\\\": 11.990200787528359,\\n      \\\"model_item_pct\\\": 12.093403522004287,\\n      \\\"n_obs\\\": 230400,\\n      \\\"accuracy\\\": 0.5557638888888888\\n    },\\n    \\\"hellaswag\\\": {\\n      \\\"item_id_pct\\\": 44.46529444603867,\\n      \\\"model_item_pct\\\": 32.30561962034519,\\n      \\\"n_obs\\\": 230400,\\n      \\\"accuracy\\\": 0.7079513888888889\\n    },\\n    \\\"math\\\": {\\n      \\\"item_id_pct\\\": 4.781370358074999,\\n      \\\"model_item_pct\\\": 46.07432475263405,\\n      \\\"n_obs\\\": 35600,\\n      \\\"accuracy\\\": 0.22547752808988764\\n    },\\n    \\\"mmlu\\\": {\\n      \\\"item_id_pct\\\": 41.54706618382246,\\n      \\\"model_item_pct\\\": 32.810330873372344,\\n      \\\"n_obs\\\": 230400,\\n      \\\"accuracy\\\": 0.7002473958333333\\n    }\\n  },\\n  \\\"tests\\\": {\\n    \\\"item_id_decreasing\\\": {\\n      \\\"observed_order\\\": [\\n        \\\"mmlu\\\",\\n        \\\"arc\\\",\\n        \\\"hellaswag\\\",\\n        \\\"gsm8k\\\",\\n        \\\"math\\\"\\n      ],\\n      \\\"observed_values\\\": [\\n        41.54706618382246,\\n        48.89986395195155,\\n        44.46529444603867,\\n        11.990200787528359,\\n        4.781370358074999\\n      ],\\n      \\\"observed_is_monotonic\\\": false,\\n      \\\"direction\\\": \\\"decreasing\\\",\\n      \\\"n_permutations\\\": 120,\\n      \\\"n_monotonic\\\": 1,\\n      \\\"p_value\\\": 0.008333,\\n      \\\"significant_at_0.05\\\": t
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T14:11:10.327339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); arc=d['benchmarks']['arc']; print(json.dumps(arc, indent=2))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); arc=d['benchmarks']['arc']; print(json.dumps(arc, indent=2))\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T14:11:10.327481+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T14:11:10.327598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -A 2 \"estimate\" /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -A 2 \"estimate\" /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T14:11:10.327820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"          \\\"estimate\\\": 0.0876133124,\\n          \\\"pct\\\": 41.5471\\n        },\\n--\\n          \\\"estimate\\\": 0.0691895248,\\n          \\\"pct\\\": 32.8103\\n        },\\n--\\n          \\\"estimate\\\": 0.043262815,\\n          \\\"pct\\\": 20.5156\\n        },\\n--\\n          \\\"estimate\\\": 0.0029608526,\\n          \\\"pct\\\": 1.4041\\n        },\\n--\\n          \\\"estimate\\\": 0.0025039227,\\n          \\\"pct\\\": 1.1874\\n        },\\n--\\n          \\\"estimate\\\": 0.00249588,\\n          \\\"pct\\\": 1.1836\\n        },\\n--\\n          \\\"estimate\\\": 0.0015897059,\\n          \\\"pct\\\": 0.7539\\n        },\\n--\\n          \\\"estimate\\\": 0.0010917321,\\n          \\\"pct\\\": 0.5177\\n        },\\n--\\n          \\\"estimate\\\": 6.01697e-05,\\n          \\\"pct\\\": 0.0285\\n        },\\n--\\n          \\\"estimate\\\": 3.90555e-05,\\n          \\\"pct\\\": 0.0185\\n        },\\n--\\n          \\\"estimate\\\": 2.79487e-05,\\n          \\\"pct\\\": 0.0133\\n        },\\n--\\n          \\\"estimate\\\": 9.1618e-06,\\n          \\\"pct\\\": 0.0043\\n        },\\n--\\n          \\\"estimate\\\": 7.8161e-06,\\n          \\\"pct\\\": 0.0037\\n        },\\n--\\n          \\\"estimate\\\": 7.5672e-06,\\n          \\\"pct\\\": 0.0036\\n        },\\n--\\n          \\\"estimate\\\": 6.4663e-06,\\n          \\\"pct\\\": 0.0031\\n        },\\n--\\n          \\\"estimate\\\": 5.7918e-06,\\n          \\\"pct\\\": 0.0027\\n        },\\n--\\n          \\\"estimate\\\": 5.5314e-06,\\n          \\\"pct\\\": 0.0026\\n        },\\n--\\n          \\\"estimate\\\": 0.0,\\n          \\\"pct\\\": 0.0\\n        },\\n--\\n          \\\"estimate\\\": 0.0,\\n          \\\"pct\\\": 0.0\\n        },\\n--\\n          \\\"estimate\\\": 0.0,\\n          \\\"pct\\\": 0.0\\n        },\\n--\\n          \\\"estimate\\\": 0.0,\\n          \\\"pct\\\": 0.0\\n        },\\n--\\n          \\\"estimate\\\": 0.0,\
…[truncated 6034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T14:11:10.327994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep \"total_variance\" /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep \"total_variance\" /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T14:11:10.328125+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"total_variance\\\": 0.2108772542,\\n      \\\"total_variance\\\": 0.2638012123,\\n      \\\"total_variance\\\": 0.1505083246,\\n      \\\"total_variance\\\": 0.2082464035,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_permutation_test_statistic_20260521T140801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T14:11:10.328351+00:00_

数据收集完毕。以下是完整分析。

---

## Part A: Test Statistic 定义与 p-value 合理性

### Test Statistic

**二元严格单调检查**，不是 Spearman ρ 或 Kendall τ。

代码 (line 106-111):
```python
def is_monotonic_decreasing(values):
    return all(a >= b for a, b in zip(values, values[1:]))
```

p-value 计算 (line 130-136):
```python
n_monotonic = 0
for perm in all_perms:
    permuted = [ordered_values[i] for i in perm]
    if check_fn(permuted):
        n_monotonic += 1
p_value = n_monotonic / n_total
```

即：`p = (120 个排列中产生严格单调序列的个数) / 120`

### 问题所在

对于 5 个互不相等的值，恰好只有 1 个排列是严格单调递减的（排序后的那个），所以 **n_monotonic 永远 = 1，p 永远 = 1/120**，与观察到的排列是否单调无关。

observed 序列 [41.55, 48.90, 44.47, 11.99, 4.78] 不是那个唯一的单调排列（arc > mmlu 违反），所以 `observed_is_monotonic = false`。

**p = 1/120 不是观察数据的 p-value。** 正确的排列检验应计算"多少个排列的 test statistic ≥ observed"。这里 test statistic 是二元的，observed = 0（非单调），119 个排列也 = 0，所以真实 p ≈ 120/120 = 1.0——完全不显著。

### 修复方案

用连续型统计量。observed Spearman ρ（position vs item_id% 降序）:

| Position | Benchmark | item_id% | Value Rank (asc) |
|----------|-----------|----------|-----------------|
| 1 | mmlu | 41.55 | 3 |
| 2 | arc | 48.90 | 5 |
| 3 | hellaswag | 44.47 | 4 |
| 4 | gsm8k | 11.99 | 2 |
| 5 | math | 4.78 | 1 |

d² = 4 + 9 + 1 + 4 + 16 = 34, **ρ = 1 − 6×34/120 = −0.70**

ρ = −0.7 表明强下降趋势但非完美单调。排列 p-value = P(ρ ≤ −0.7 | H0)，需要枚举 120 个排列各自的 ρ 来计算——这才是有意义的 p-value。

---

## Part B: 绝对方差值分析

### 完整方差分量表（按 BENCHMARK_ORDER 排列）

| Component | mmlu | arc | hellaswag | gsm8k |
|-----------|------|-----|-----------|-------|
| **σ²(item_id)** | 0.0876 | 0.0736 | 0.0926 | 0.0316 |
| **σ²(model:item_id)** | 0.0692 | 0.0575 | 0.0673 | 0.0319 |
| **σ²(residual)** | 0.0433 | 0.0124 | 0.0355 | 0.0852 |
| σ²(model) | 0.0016 | 0.0019 | 0.0031 | 0.0400 |
| σ²(prompt_template) | 0.00001 | 0.0000 | 0.00006 | 0.0324 |
| σ²(model:prompt_template) | 0.00004 | 0.00003 | 0.0004 | 0.0249 |
| σ²(prompt_template:item_id) | 0.0030 | 0.0004 | 0.0073 | 0.0145 |
| **Total variance** | **0.2109** | **0.1505** | **0.2082** | **0.2638** |

对应百分比：

| Component | mmlu | arc | hellaswag | gsm8k |
|-----------|------|-----|-----------|-------|
| item_id% | 41.5 | 48.9 | 44.5 | 12.0 |
| model:item_id% | 32.8 | 38.2 | 32.3 | 12.1 |
| residual% | 20.5 | 8.2 | 17.1 | 32.3 |

### 绝对值的模式

**item_id σ² 绝对值序列**：0.0876 → 0.0736 → 0.0926 → 0.0316
- **不单调**（arc < hellaswag 违反）
- 前三个 benchmark 在同一量级（0.07–0.09），GSM8K 骤降到 0.03

**model:item_id σ² 绝对值序列**：0.0692 → 0.0575 → 0.0673 → 0.0319
- **也不单调**，且方向是递减而非假设的递增
- 同样是前三个 ~0.06–0.07，GSM8K 骤降

### 百分比 vs 绝对值的差异根源

GSM8K 的 item_id% 只有 12% 不是因为 item_id 绝对方差小（0.032 确实小），而是因为**分母膨胀**——GSM8K 有大量额外方差来源：

| 只在 GSM8K 显著的来源 | GSM8K | 其他三个最大值 |
|----------------------|-------|---------------|
| σ²(model) | **0.0400** | 0.0031 |
| σ²(prompt_template) | **0.0324** | 0.00006 |
| σ²(model:prompt_template) | **0.0249** | 0.0004 |

这三项在知识型 benchmark 中几乎为零，在 GSM8K 中合计贡献 0.097（占总方差 37%）。这是 GSM8K item_id% 被"压缩"的直接原因。

### 结论

1. **排列检验 p=1/120 有方法论错误**：二元 test statistic + 不检查观察值是否命中 → 对任何 5 个不等值恒得 p=1/120。应换用 Spearman ρ 作为 test statistic 重做。
2. **绝对值讲述的不是"gradient"故事，而是"两类 benchmark"故事**：知识型 (mmlu/arc/hellaswag) 三者 item_id σ² 在 0.07–0.09 之间互有起伏，无序；推理型 (gsm8k) 独立构成低谷。
3. **GSM8K item_id% 低的主因是分母膨胀**：model、prompt_template 及其交互在 GSM8K 中比知识型 benchmark 大 10–500 倍，撑大了 total variance，压缩了 item_id 的百分比份额。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_permutation_test_statistic_20260521T140801"
}
```

</details>

---
