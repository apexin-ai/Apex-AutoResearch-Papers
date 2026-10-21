# analysis copula gof

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_copula-gof_20260521T224845.jsonl`
- **Structured JSON:** [`24ae2e9c1ec0611005d3.json`](../../sessions/24/24ae2e9c1ec0611005d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-21T22:49:20.209603+00:00_

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
  "session": "worker_analysis_copula-gof_20260521T224845",
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

_source line 2 · 2026-05-21T22:49:20.209946+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_copula-gof_20260521T224845",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T22:49:20.210122+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/scripts/copula_gof_check.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_copula-gof_20260521T224845",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ls /root/cert_manip_resist_eval/scripts/copula_gof_check.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T22:49:20.210261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/cert_manip_resist_eval/scripts/copula_gof_check.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_copula-gof_20260521T224845",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T22:49:20.210402+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cd /root/cert_manip_resist_eval && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 scripts/copula_gof_check.py 2>&1 | tee /tmp/copula_gof.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_copula-gof_20260521T224845",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cd /root/cert_manip_resist_eval && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 scripts/copula_gof_check.py 2>&1 | tee /tmp/copula_gof.log"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T22:49:20.210568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[06:49:08 INFO] copula_gof: \\n============================================================\\n[06:49:08 INFO] copula_gof: Copula GoF Check: mmlu\\n[06:49:08 INFO] copula_gof: ============================================================\\n[06:49:08 INFO] copula_gof: Pair                                       MI_obs      rho   MI_gauss    Ratio   Flag\\n[06:49:08 INFO] copula_gof: --------------------------------------------------------------------------------\\n[06:49:08 INFO] copula_gof: llama3.1-70b <-> llama3.1-8b               0.0447   0.1735     0.0153     2.93     !!\\n[06:49:08 INFO] copula_gof: llama3.1-70b <-> mistral-large             0.2358   0.4028     0.0885     2.66     !!\\n[06:49:08 INFO] copula_gof: llama3.1-70b <-> qwen2.5-14b               0.1222   0.0880     0.0039    31.47     !!\\n[06:49:08 INFO] copula_gof: llama3.1-70b <-> qwen2.5-32b               0.2605   0.3861     0.0807     3.23     !!\\n[06:49:08 INFO] copula_gof: llama3.1-70b <-> qwen2.5-72b               0.2780   0.3125     0.0514     5.41     !!\\n[06:49:08 INFO] copula_gof: llama3.1-8b <-> mistral-large              0.0428   0.2120     0.0230     1.86       \\n[06:49:08 INFO] copula_gof: llama3.1-8b <-> qwen2.5-14b                0.0374   0.1768     0.0159     2.36     !!\\n[06:49:08 INFO] copula_gof: llama3.1-8b <-> qwen2.5-32b                0.0235   0.1437     0.0104     2.25     !!\\n[06:49:08 INFO] copula_gof: llama3.1-8b <-> qwen2.5-72b                0.0296   0.1316     0.0087     3.39     !!\\n[06:49:08 INFO] copula_gof: mistral-large <-> qwen2.5-14b              0.1052   0.0299     0.0004   235.86     !!\\n[06:49:08 INFO] copula_gof: mistral-large <-> qwen2.5-32b              0.1957   0.3198     0.0539     3.63     !!\\n[06:49:08 INFO] copula_gof: mistral-large <-> qwen2.5-72b              0.2617   0.2828     0.0417     6.28     !!\\n[06:49:08 INFO] copula_gof: qwen2.5-14b <-> qwen2.5-32b                0.1911   0.2629 
…[truncated 3011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_copula-gof_20260521T224845",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-21T22:49:20.210786+00:00_

## 结果

### MMLU
| 指标 | 值 |
|------|-----|
| Mean ratio (MI_obs / MI_gauss) | **21.13** |
| Pairs with ratio > 2 | **14/15** |
| 结论 | Gaussian copula 假设系统性违反 |

极端案例：`mistral-large <-> qwen2.5-14b` ratio = 235.86（ρ 极低但 MI 不低，说明依赖结构高度非线性）。

### ARC Challenge
| 指标 | 值 |
|------|-----|
| Mean ratio (MI_obs / MI_gauss) | **10.36** |
| Pairs with ratio > 2 | **15/15** |
| 结论 | Gaussian copula 假设系统性违反 |

极端案例：`mistral-large <-> qwen2.5-14b` ratio = 69.43。

**总结**：两个数据集上 Gaussian copula 假设均被系统性违反——观测 MI 远大于 Gaussian copula 对应的 MI，表明 judge 间的依赖结构包含大量非线性/尾部依赖，不能用简单的相关系数 ρ 刻画。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_copula-gof_20260521T224845"
}
```

</details>

---
