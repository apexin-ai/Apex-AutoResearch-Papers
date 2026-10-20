# analyze p8 latency overhead

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_p8_latency_overhead_20260518T150838.jsonl`
- **Structured JSON:** [`b8362480eaa2ff420d63.json`](../../sessions/b8/b8362480eaa2ff420d63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-18T15:09:05.455435+00:00_

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
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
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

_source line 2 · 2026-05-18T15:09:05.455868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T15:09:05.456070+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "tail -100 ~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "tail -100 ~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T15:09:05.456207+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "ls -la /root/autodl-tmp/schema_outputs/p8_timing_*.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "ls -la /root/autodl-tmp/schema_outputs/p8_timing_*.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T15:09:05.456404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[490/551] ICASSP_1997_706_abs_sent2: OK E=3 R=2 3.6s\\n[491/551] ICASSP_1997_706_abs_sent3: OK E=5 R=4 4.8s\\n[492/551] ICASSP_1997_706_abs_sent4: OK E=9 R=5 6.8s\\n[493/551] INTERSPEECH_2008_28_abs_sent0: OK E=3 R=2 3.1s\\n[494/551] INTERSPEECH_2008_28_abs_sent1: OK E=7 R=4 7.0s\\n[495/551] INTERSPEECH_2008_28_abs_sent2: OK E=6 R=5 5.4s\\n[496/551] INTERSPEECH_2008_28_abs_sent3: OK E=4 R=3 4.4s\\n[497/551] INTERSPEECH_2008_28_abs_sent4: OK E=7 R=5 6.3s\\n[498/551] INTERSPEECH_2008_28_abs_sent5: OK E=3 R=2 3.6s\\n[499/551] INTERSPEECH_2008_28_abs_sent6: OK E=3 R=2 3.0s\\n[500/551] ECCV_2016_110_abs_sent0: OK E=4 R=2 3.2s\\n[501/551] ECCV_2016_110_abs_sent1: OK E=2 R=1 2.4s\\n[502/551] ECCV_2016_110_abs_sent2: OK E=5 R=3 5.0s\\n[503/551] CVPR_2008_258_abs_sent0: OK E=6 R=3 5.4s\\n[504/551] CVPR_2008_258_abs_sent1: OK E=3 R=2 3.3s\\n[505/551] CVPR_2008_258_abs_sent2: OK E=2 R=1 2.2s\\n[506/551] CVPR_2008_258_abs_sent3: OK E=6 R=3 5.7s\\n[507/551] CVPR_2008_258_abs_sent4: OK E=4 R=3 3.8s\\n[508/551] CVPR_2008_258_abs_sent5: OK E=3 R=2 3.5s\\n[509/551] C08-2010_sent0: OK E=2 R=1 1.9s\\n[510/551] C08-2010_sent1: OK E=6 R=4 6.1s\\n[511/551] C08-2010_sent2: OK E=5 R=3 4.9s\\n[512/551] C08-2010_sent3: OK E=3 R=2 3.2s\\n[513/551] C08-2010_sent4: OK E=5 R=4 4.6s\\n[514/551] C08-2010_sent5: OK E=2 R=1 2.2s\\n[515/551] C08-2010_sent6: OK E=2 R=1 2.2s\\n[516/551] E93-1066_sent0: OK E=7 R=6 9.2s\\n[517/551] E93-1066_sent1: OK E=4 R=4 5.8s\\n[518/551] E93-1066_sent2: OK E=5 R=7 8.8s\\n[519/551] E93-1066_sent3: OK E=7 R=5 7.1s\\n[520/551] E93-1066_sent4: OK E=3 R=2 3.0s\\n[521/551] E93-1066_sent5: OK E=6 R=5 6.3s\\n[522/551] E93-1066_sent6: OK E=4 R=3 3.9s\\n[523/551] INTERSPEECH_2014_40_abs_sent0: OK E=7 R=6 6.7s\\n[524/551] INTERSPEECH_2014_40_abs_sent1: OK E=4 R=3 4.9s\\n[525/551] INTERSPEECH_2014_40_abs_sent2: OK E=6 R=5 5.6s\\n[526/551] INTERSPEECH_2014_40_abs_sent3: OK E=6 R=3 4.4s\\n[527/551] INTERSPEECH_2014_40_abs_sen
…[truncated 2379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T15:09:05.456568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1344482 May 18 23:05 /root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl\\n-rw-r--r-- 1 root root 1348986 May 18 22:22 /root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-18T15:09:05.456781+00:00_

## P8 Latency Overhead 结果

- 样本数: 551
- **Unconstrained**: mean=4.163s, median=4.106s, p5=1.756s, p95=7.562s, std=1.735s, total=2293.7s
- **Constrained (full_s1)**: mean=4.710s, median=4.644s, p5=2.173s, p95=8.136s, std=1.814s, total=2595.0s
- **Overhead ratio (aggregate)**: mean=1.131x, median=1.131x, p95=1.076x
- **Overhead ratio (per-doc)**: mean=1.151x, median=1.137x, p5=1.082x, p95=1.262x
- **结论**: Constrained decoding overhead 约 **13%**，远低于 2x 阈值。即使在 p95 最差情况下，per-doc overhead 也仅 1.26x。开销可忽略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_p8_latency_overhead_20260518T150838"
}
```

</details>

---
