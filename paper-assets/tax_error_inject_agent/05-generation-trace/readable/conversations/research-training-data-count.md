# research training data count

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_research_training-data-count_20260516T134418.jsonl`
- **Structured JSON:** [`b5a23a8defc9a6233704.json`](../../sessions/b5/b5a23a8defc9a6233704.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-16T13:44:39.284015+00:00_

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
  "session": "worker_research_training-data-count_20260516T134418",
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

_source line 2 · 2026-05-16T13:44:39.284342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_training-data-count_20260516T134418",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T13:44:39.284505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_training-data-count_20260516T134418",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T13:44:39.284716+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    4358 /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl\\n    9029 /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\\n    9029 /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\\n   22416 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_training-data-count_20260516T134418",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T13:44:39.284892+00:00_

| 条件 | 文件 | 样本数 |
|------|------|--------|
| Vanilla | `sft_vanilla_v4.jsonl` | **4,358** |
| TaxEI | `sft_taxei_v4.jsonl` | **9,029** |
| Random | `sft_random_v4.jsonl` | **9,029** |

TaxEI 和 Random 数据量相同（9,029），均为 Vanilla（4,358）的约 2.07 倍。差值 4,671 应为注入的错误样本数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_training-data-count_20260516T134418"
}
```

</details>

---
