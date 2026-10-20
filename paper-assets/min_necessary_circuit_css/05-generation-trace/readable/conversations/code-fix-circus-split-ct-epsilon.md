# code fix circus split ct epsilon

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_code_fix-circus-split-ct-epsilon_20260513T002405.jsonl`
- **Structured JSON:** [`3885e158232f85692574.json`](../../sessions/38/3885e158232f85692574.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-13T00:24:56.901316+00:00_

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
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
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

_source line 2 · 2026-05-13T00:24:56.901632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T00:24:56.901820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/structfuse-context/circus.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/structfuse-context/circus.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T00:24:56.901962+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/structfuse-context/cross_tabulate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/structfuse-context/cross_tabulate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T00:24:56.902145+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"CIRCUS config-bagging for stability analysis.\\\"\\\"\\\"\\n     2\\t\\n     3\\tfrom typing import Dict, Set, Tuple\\n     4\\timport numpy as np\\n     5\\t\\n     6\\tfrom config import MVPConfig, MVP_CONFIG\\n     7\\t\\n     8\\t\\n     9\\tdef config_bag(edge_scores: Dict[str, float], B: int = 10) -> Dict[str, float]:\\n    10\\t    \\\"\\\"\\\"2D anti-chain config bagging.\\n    11\\t\\n    12\\t    Uses (node_threshold, edge_threshold) pairs along an anti-diagonal\\n    13\\t    to produce pairwise-incomparable circuits (no nesting).\\n    14\\t    \\\"\\\"\\\"\\n    15\\t    if not edge_scores:\\n    16\\t        return {}\\n    17\\t\\n    18\\t    edges = list(edge_scores.keys())\\n    19\\t    scores = np.array([edge_scores[e] for e in edges])\\n    20\\t    abs_scores = np.abs(scores)\\n    21\\t\\n    22\\t    node_max: Dict[str, float] = {}\\n    23\\t    for e, s in edge_scores.items():\\n    24\\t        src = e.split(\\\" -> \\\")[0]\\n    25\\t        node_max[src] = max(node_max.get(src, -np.inf), abs(s))\\n    26\\t\\n    27\\t    node_scores = np.array([node_max[e.split(\\\" -> \\\")[0]] for e in edges])\\n    28\\t\\n    29\\t    t = np.linspace(0, 1, B)\\n    30\\t    node_pcts = 10 + 80 * t\\n    31\\t    edge_pcts = 10 + 80 * (1 - t)\\n    32\\t\\n    33\\t    node_threshs = np.percentile(node_scores, node_pcts)\\n    34\\t    edge_threshs = np.percentile(abs_scores, edge_pcts)\\n    35\\t\\n    36\\t    stability = np.zeros(len(edges))\\n    37\\t    for nt, et in zip(node_threshs, edge_threshs):\\n    38\\t        included = (node_scores >= nt) & (abs_scores >= et)\\n    39\\t        stability += included.astype(float)\\n    40\\t    stability /= B\\n    41\\t\\n    42\\t    return {edge: float(stab) for edge, stab in zip(edges, stability)}\\n    43\\t\\n    44\\t\\n    45\\tdef get_circus_tiers(stability_scores: Dict[str, float], core_threshold: float = 1.0, con
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T00:24:56.902401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"CIRCUS-core x CSS cross-tabulation.\\\"\\\"\\\"\\n     2\\t\\n     3\\tfrom typing import Dict, Set\\n     4\\tfrom dataclasses import dataclass\\n     5\\t\\n     6\\t\\n     7\\t@dataclass\\n     8\\tclass CrossTable:\\n     9\\t    stable_core: Set[str]\\n    10\\t    method_specific: Set[str]\\n    11\\t    cross_unstable: Set[str]\\n    12\\t    noise: Set[str]\\n    13\\t\\n    14\\t    @property\\n    15\\t    def total(self) -> int:\\n    16\\t        return len(self.stable_core) + len(self.method_specific) + len(self.cross_unstable) + len(self.noise)\\n    17\\t\\n    18\\t    @property\\n    19\\t    def core_total(self) -> int:\\n    20\\t        return len(self.stable_core) + len(self.method_specific)\\n    21\\t\\n    22\\t    @property\\n    23\\t    def core_off_diagonal_pct(self) -> float:\\n    24\\t        if self.core_total == 0:\\n    25\\t            return 0.0\\n    26\\t        return len(self.method_specific) / self.core_total\\n    27\\t\\n    28\\t    def summary(self) -> Dict[str, object]:\\n    29\\t        return {\\n    30\\t            \\\"stable_core\\\": len(self.stable_core),\\n    31\\t            \\\"method_specific\\\": len(self.method_specific),\\n    32\\t            \\\"cross_unstable\\\": len(self.cross_unstable),\\n    33\\t            \\\"noise\\\": len(self.noise),\\n    34\\t            \\\"total\\\": self.total,\\n    35\\t            \\\"core_total\\\": self.core_total,\\n    36\\t            \\\"core_off_diagonal_pct\\\": round(self.core_off_diagonal_pct, 4),\\n    37\\t        }\\n    38\\t\\n    39\\t\\n    40\\tdef cross_tabulate(circus_tiers: Dict[str, str], css_scores: Dict[str, float], css_threshold: float = 0.67) -> CrossTable:\\n    41\\t    all_edges = set(circus_tiers.keys()) | set(css_scores.keys())\\n    42\\t    stable_core = set()\\n    43\\t    method_specific = set()\\n    44\\t    cross_unstable = set()\\n    45\\t    noise = 
…[truncated 3620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T00:24:56.902601+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/structfuse-context && sed -i 's/e\\.split(\" -> \")/e.split(\"->\")/g' circus.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/structfuse-context && sed -i 's/e\\.split(\" -> \")/e.split(\"->\")/g' circus.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T00:24:56.902755+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T00:24:56.902880+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/structfuse-context && sed -i 's/css_scores\\.get(edge, 0\\.0) >= css_threshold$/css_scores.get(edge, 0.0) >= css_threshold - 1e-2/' cross_tabulate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/structfuse-context && sed -i 's/css_scores\\.get(edge, 0\\.0) >= css_threshold$/css_scores.get(edge, 0.0) >= css_threshold - 1e-2/' cross_tabulate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T00:24:56.903000+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T00:24:56.903128+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n '\\\" -> \\\"' /root/structfuse-context/circus.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n '\\\" -> \\\"' /root/structfuse-context/circus.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T00:24:56.903252+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T00:24:56.903368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n 'split\\|css_threshold' /root/structfuse-context/circus.py /root/structfuse-context/cross_tabulate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n 'split\\|css_threshold' /root/structfuse-context/circus.py /root/structfuse-context/cross_tabulate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T00:24:56.903483+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T00:24:56.903591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T00:24:56.903719+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T00:24:56.903852+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"split\" /root/structfuse-context/circus.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"split\" /root/structfuse-context/circus.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T00:24:56.903968+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:        src = e.split(\\\"->\\\")[0]\\n27:    node_scores = np.array([node_max[e.split(\\\"->\\\")[0]] for e in edges])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T00:24:56.904079+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"css_threshold\" /root/structfuse-context/cross_tabulate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"css_threshold\" /root/structfuse-context/cross_tabulate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T00:24:56.904193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"40:def cross_tabulate(circus_tiers: Dict[str, str], css_scores: Dict[str, float], css_threshold: float = 0.67) -> CrossTable:\\n49:        css_high = css_scores.get(edge, 0.0) >= css_threshold - 1e-2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T00:24:56.904310+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T00:24:56.904432+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"import py_compile; py_compile.compile(\\\\'/root/structfuse-context/circus.py\\\\', doraise=True); py_compile.compile(\\\\'/root/structfuse-context/cross_tabulate.py\\\\', doraise=True); print(\\\\'SYNTAX_OK\\\\')\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T00:24:56.904544+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import py_compile; py_compile.compile('/root/structfuse-context/circus.py', doraise=True); py_compile.compile('/root/structfuse-context/cross_tabulate.py', doraise=True); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T00:24:56.904657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T00:24:56.904835+00:00_

两个文件修复完毕，语法验证通过。

### 修改报告

**circus.py** — 2 处修改：
| 行 | 原始 | 修改后 |
|---|---|---|
| 24 | `e.split(" -> ")[0]` | `e.split("->")[0]` |
| 27 | `e.split(" -> ")[0]` | `e.split("->")[0]` |

**cross_tabulate.py** — 1 处修改：
| 行 | 原始 | 修改后 |
|---|---|---|
| 49 | `css_scores.get(edge, 0.0) >= css_threshold` | `css_scores.get(edge, 0.0) >= css_threshold - 1e-2` |

无其他遗漏，文件中不再有 `" -> "` 分隔符。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_fix-circus-split-ct-epsilon_20260513T002405"
}
```

</details>

---
