# investigate alpha verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_investigate_alpha-verify_20260515T151011.jsonl`
- **Structured JSON:** [`a39516debafadfe47b68.json`](../../sessions/a3/a39516debafadfe47b68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T15:11:20.611874+00:00_

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
  "session": "worker_investigate_alpha-verify_20260515T151011",
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

_source line 2 · 2026-05-15T15:11:20.612341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:11:20.612629+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_* -name adapter_config.json -path \"*/lora_adapter/*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_* -name adapter_config.json -path \"*/lora_adapter/*\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T15:11:20.612909+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/checkpoint-3125/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/checkpoint-3125/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/checkpoint-3125/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/checkpoint-3125/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/checkpoint-3177/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/checkpoint-3177/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/checkpoint-3384/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/checkpoint-3384/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter/checkpoint-4159/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/checkpoint-4159/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoin
…[truncated 162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T15:11:20.613218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:11:20.613490+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 16,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 16,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T15:11:20.613733+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:11:20.613969+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 16,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 16,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 16,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:11:20.614251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_* -maxdepth 2 -name adapter_config.json -path \"*/lora_adapter/adapter_config.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_* -maxdepth 2 -name adapter_config.json -path \"*/lora_adapter/adapter_config.json\""
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T15:11:20.614519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_* -maxdepth 2 -name adapter_config.json -path \"*/lora_adapter/adapter_config.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_* -maxdepth 2 -name adapter_config.json -path \"*/lora_adapter/adapter_config.json\""
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T15:11:20.614752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter/adapter_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T15:11:20.615116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter/adapter_config.json\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter/adapter_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T15:11:20.615422+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -H lora_alpha /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter/adapter_config.json /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T15:11:20.615663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter/adapter_config.json:  \\\"lora_alpha\\\": 32,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_alpha-verify_20260515T151011",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T15:11:20.615996+00:00_

## 结果

### 3B SFT Checkpoints（全部 10 个）

| Checkpoint | lora_alpha | 备注 |
|---|---|---|
| `Qwen2.5-3B_d000_s123` | **32** | |
| `Qwen2.5-3B_d000_s42` | **32** | |
| `Qwen2.5-3B_d000_v2_s123` | **16** | v2 重跑版本 |
| `Qwen2.5-3B_d000_v2_s42` | **16** | v2 重跑版本 |
| `Qwen2.5-3B_d005_s123` | **32** | ⚠️ registry 命令写 `--lora-alpha 16`，实际是 32 |
| `Qwen2.5-3B_d005_s42` | **32** | |
| `Qwen2.5-3B_d025_s123` | **32** | |
| `Qwen2.5-3B_d025_s42` | **16** | |
| `Qwen2.5-3B_d100_s123` | **16** | |
| `Qwen2.5-3B_d100_s42` | **16** | |

**分布：5 个 alpha=32，5 个 alpha=16**

### 0.5B / 1.5B 代表性 Checkpoints（各 2 个）

| Checkpoint | lora_alpha |
|---|---|
| `Qwen2.5-0.5B_d005_s123` | **32** |
| `Qwen2.5-0.5B_d025_s42` | **32** |
| `Qwen2.5-1.5B_d005_s123` | **32** |
| `Qwen2.5-1.5B_d025_s42` | **32** |

0.5B 和 1.5B 采样点全部一致为 alpha=32。

### 关键发现

1. **`exp_001_sft_3B_d005_s123` 存在 registry 与实际不一致**：registry 提交命令记录 `--lora-alpha 16`，但 checkpoint 实际保存的是 `lora_alpha=32`。可能原因：脚本有默认值覆盖了命令行参数，或 registry 记录有误。
2. **3B 的 alpha=16 集中在**：v2 重跑版本（d000_v2）和部分后期实验（d025_s42、d100_s123、d100_s42），暗示这些是在某次配置变更后训练的。
3. **0.5B / 1.5B 未受影响**，采样点均为 alpha=32。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_investigate_alpha-verify_20260515T151011"
}
```

</details>

---
