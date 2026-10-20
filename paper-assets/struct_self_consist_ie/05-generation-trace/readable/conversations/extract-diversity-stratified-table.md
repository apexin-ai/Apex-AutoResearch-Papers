# extract diversity stratified table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_extract_diversity_stratified_table_20260515T045028.jsonl`
- **Structured JSON:** [`d24ed38a5e84b821fbb8.json`](../../sessions/d2/d24ed38a5e84b821fbb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-15T04:51:19.793431+00:00_

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
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
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

_source line 2 · 2026-05-15T04:51:19.793775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:51:19.793954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_stratified_selection.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_stratified_selection.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T04:51:19.794086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T04:51:19.794402+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen_scierc_ner\\\": {\\n    \\\"n_total_valid\\\": 529,\\n    \\\"strata\\\": {\\n      \\\"high_diversity\\\": {\\n        \\\"criterion\\\": \\\"n_unique >= 4\\\",\\n        \\\"n\\\": 232,\\n        \\\"greedy_f1\\\": 0.5753,\\n        \\\"oracle_f1\\\": 0.7384,\\n        \\\"oracle_headroom\\\": 0.1631,\\n        \\\"signals\\\": {\\n          \\\"sj\\\": {\\n            \\\"selection_f1\\\": 0.5747,\\n            \\\"selection_gap\\\": -0.0006\\n          },\\n          \\\"fk\\\": {\\n            \\\"selection_f1\\\": 0.5733,\\n            \\\"selection_gap\\\": -0.002\\n          },\\n          \\\"em\\\": {\\n            \\\"selection_f1\\\": 0.5561,\\n            \\\"selection_gap\\\": -0.0192\\n          },\\n          \\\"voting_conf\\\": {\\n            \\\"selection_f1\\\": 0.5498,\\n            \\\"selection_gap\\\": -0.0255\\n          },\\n          \\\"logprob\\\": {\\n            \\\"selection_f1\\\": 0.5829,\\n            \\\"selection_gap\\\": 0.0076\\n          }\\n        }\\n      },\\n      \\\"medium\\\": {\\n        \\\"criterion\\\": \\\"n_unique == 3\\\",\\n        \\\"n\\\": 112,\\n        \\\"greedy_f1\\\": 0.674,\\n        \\\"oracle_f1\\\": 0.8063,\\n        \\\"oracle_headroom\\\": 0.1323,\\n        \\\"signals\\\": {\\n          \\\"sj\\\": {\\n            \\\"selection_f1\\\": 0.6968,\\n            \\\"selection_gap\\\": 0.0228\\n          },\\n          \\\"fk\\\": {\\n            \\\"selection_f1\\\": 0.6989,\\n            \\\"selection_gap\\\": 0.0249\\n          },\\n          \\\"em\\\": {\\n            \\\"selection_f1\\\": 0.6938,\\n            \\\"selection_gap\\\": 0.0198\\n          },\\n          \\\"voting_conf\\\": {\\n            \\\"selection_f1\\\": 0.6461,\\n            \\\"selection_gap\\\": -0.0279\\n          },\\n          \\\"logprob\\\": {\\n            \\\"selection_f1\\\": 0.6888,\\n            \\\"selection_gap\\\": 0.0148\\n          }\\n 
…[truncated 4336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:51:19.794700+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen_scierc_ner\\\": {\\n    \\\"n_valid\\\": 529,\\n    \\\"n_total\\\": 551,\\n    \\\"unique_fraction\\\": {\\n      \\\"mean\\\": 0.4327,\\n      \\\"median\\\": 0.375,\\n      \\\"histogram\\\": {\\n        \\\"1\\\": 59,\\n        \\\"2\\\": 126,\\n        \\\"3\\\": 112,\\n        \\\"4\\\": 94,\\n        \\\"5\\\": 72,\\n        \\\"6\\\": 32,\\n        \\\"7\\\": 16,\\n        \\\"8\\\": 18\\n      }\\n    },\\n    \\\"logprob_std\\\": {\\n      \\\"mean\\\": 0.020484,\\n      \\\"median\\\": 0.013479,\\n      \\\"p25\\\": 0.008671,\\n      \\\"p75\\\": 0.022697\\n    },\\n    \\\"f1_std\\\": {\\n      \\\"mean\\\": 0.1442,\\n      \\\"median\\\": 0.1308\\n    },\\n    \\\"pairwise_sj\\\": {\\n      \\\"mean\\\": 0.7026,\\n      \\\"median\\\": 0.7143,\\n      \\\"p25\\\": 0.5674,\\n      \\\"p75\\\": 0.8661,\\n      \\\"histogram\\\": {\\n        \\\"0.0-0.1\\\": 0,\\n        \\\"0.1-0.2\\\": 1,\\n        \\\"0.2-0.3\\\": 11,\\n        \\\"0.3-0.4\\\": 26,\\n        \\\"0.4-0.5\\\": 52,\\n        \\\"0.5-0.6\\\": 67,\\n        \\\"0.6-0.7\\\": 91,\\n        \\\"0.7-0.8\\\": 109,\\n        \\\"0.8-0.9\\\": 65,\\n        \\\"0.9-1.0\\\": 107\\n      }\\n    }\\n  },\\n  \\\"llama_scierc_ner\\\": {\\n    \\\"n_valid\\\": 529,\\n    \\\"n_total\\\": 551,\\n    \\\"unique_fraction\\\": {\\n      \\\"mean\\\": 0.3885,\\n      \\\"median\\\": 0.375,\\n      \\\"histogram\\\": {\\n        \\\"1\\\": 94,\\n        \\\"2\\\": 142,\\n        \\\"3\\\": 107,\\n        \\\"4\\\": 71,\\n        \\\"5\\\": 57,\\n        \\\"6\\\": 36,\\n        \\\"7\\\": 16,\\n        \\\"8\\\": 6\\n      }\\n    },\\n    \\\"logprob_std\\\": {\\n      \\\"mean\\\": 0.01876,\\n      \\\"median\\\": 0.013596,\\n      \\\"p25\\\": 0.008513,\\n      \\\"p75\\\": 0.023427\\n    },\\n    \\\"f1_std\\\": {\\n      \\\"mean\\\": 0.1267,\\n      \\\"median\\\": 0.1102\\n    },\\n    \\\"pairwise_sj\\\": {\\n      \\\"mean\\\": 0.
…[truncated 4125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_extract_diversity_stratified_table_20260515T045028",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T04:51:19.794933+00:00_

JSON 数据完整，直接提取。

## Qwen SciERC NER

| Group | n | Greedy F1 | Oracle F1 | Headroom | SJ sel | FK sel | EM sel | LP sel | VC sel | Best signal | Best gap vs greedy |
|-------|--:|----------:|----------:|---------:|-------:|-------:|-------:|-------:|-------:|:-----------:|-------------------:|
| **high-diversity** (≥4 unique) | 232 | .5753 | .7384 | .1631 | .5747 | .5733 | .5561 | **.5829** | .5498 | **LP** | **+.0076** |
| medium (=3 unique) | 112 | .6740 | .8063 | .1323 | .6968 | **.6989** | .6938 | .6888 | .6461 | **FK** | **+.0249** |
| **low-diversity** (≤2 unique) | 185 | .7118 | .8043 | .0925 | .7018 | .7018 | .7018 | .7109 | **.7117** | **VC** | **−.0001** |

## LLaMA SciERC NER

| Group | n | Greedy F1 | Oracle F1 | Headroom | SJ sel | FK sel | EM sel | LP sel | VC sel | Best signal | Best gap vs greedy |
|-------|--:|----------:|----------:|---------:|-------:|-------:|-------:|-------:|-------:|:-----------:|-------------------:|
| **high-diversity** (≥4 unique) | 186 | .5630 | .7644 | .2014 | .5618 | .5622 | .5381 | **.5826** | .5455 | **LP** | **+.0196** |
| medium (=3 unique) | 107 | .6307 | .7623 | .1316 | .6209 | .6246 | **.6277** | .6250 | .6140 | **EM** | **−.0029** |
| **low-diversity** (≤2 unique) | 236 | .7184 | .7959 | .0775 | .7177 | .7176 | .7164 | .7185 | **.7252** | **VC** | **+.0068** |

## 关键发现

**High-diversity 组 (≥4 unique)**：
- Headroom 大（Qwen 16.3pp, LLaMA 20.1pp），但所有 consistency-based 信号（SJ/FK/EM/VC）都**低于 greedy**
- 唯一正向信号是 **logprob (LP)**：Qwen +0.76pp, LLaMA +1.96pp
- 说明当输出高度分歧时，consistency 信号失效，只有模型自身置信度（logprob）能提供微弱的选择信号

**Low-diversity 组 (≤2 unique)**：
- Headroom 小（Qwen 9.25pp, LLaMA 7.75pp），所有信号的 gap 都接近零（|gap| < 1pp）
- 最佳信号是 **voting confidence (VC)**，但增益可忽略
- 天花板效应：输出几乎一致时，selection 无改进空间

**Diversity histogram（参考）**：
- Qwen: 1→59, 2→126, 3→112, 4→94, 5→72, 6→32, 7→16, 8→18
- LLaMA: 1→94, 2→142, 3→107, 4→71, 5→57, 6→36, 7→16, 8→6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_extract_diversity_stratified_table_20260515T045028"
}
```

</details>

---
