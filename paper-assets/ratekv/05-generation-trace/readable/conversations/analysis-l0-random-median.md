# analysis l0 random median

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analysis_l0_random_median_20260514T072537.jsonl`
- **Structured JSON:** [`3e90d4d0a083c930865f.json`](../../sessions/3e/3e90d4d0a083c930865f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-14T07:26:05.035671+00:00_

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
  "session": "worker_analysis_l0_random_median_20260514T072537",
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

_source line 2 · 2026-05-14T07:26:05.036019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_l0_random_median_20260514T072537",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T07:26:05.036197+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "cat /root/ratekv/l0_heuristic_corrected_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_l0_random_median_20260514T072537",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "cat /root/ratekv/l0_heuristic_corrected_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T07:26:05.036384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"plan_015_l0_heuristic_corrected\\\",\\n  \\\"description\\\": \\\"L0 heuristic baselines at exact budget=0.25 with actual MCKP eval\\\",\\n  \\\"eval_dtype\\\": \\\"bfloat16\\\",\\n  \\\"eval_dataset\\\": \\\"wikitext-2-raw-v1 test\\\",\\n  \\\"budget\\\": 0.25,\\n  \\\"models\\\": {\\n    \\\"Qwen2.5-7B\\\": {\\n      \\\"baseline_bf16_ppl\\\": 9.8106,\\n      \\\"uniform_4bit_ppl\\\": 15.4454,\\n      \\\"l0_random\\\": {\\n        \\\"seed_0\\\": 11.486,\\n        \\\"seed_1\\\": 11.6153,\\n        \\\"seed_2\\\": 11.3251,\\n        \\\"seed_3\\\": 11.5151,\\n        \\\"seed_4\\\": 12.5147,\\n        \\\"mean\\\": 11.69124,\\n        \\\"std\\\": 0.42215175280934186\\n      },\\n      \\\"naive_heuristic_ppl\\\": 12.2302,\\n      \\\"mckp_ppl\\\": 10.91312596440544\\n    },\\n    \\\"Llama-3.1-8B\\\": {\\n      \\\"baseline_bf16_ppl\\\": 8.0918,\\n      \\\"uniform_4bit_ppl\\\": 8.469,\\n      \\\"l0_random\\\": {\\n        \\\"seed_0\\\": 9.4845,\\n        \\\"seed_1\\\": 10.4884,\\n        \\\"seed_2\\\": 9.9406,\\n        \\\"seed_3\\\": 10.0381,\\n        \\\"seed_4\\\": 12.4441,\\n        \\\"mean\\\": 10.479140000000001,\\n        \\\"std\\\": 1.0329572974716816\\n      },\\n      \\\"naive_heuristic_ppl\\\": 9.941,\\n      \\\"mckp_ppl\\\": 8.449828728146104\\n    },\\n    \\\"Mistral-7B-v0.3\\\": {\\n      \\\"baseline_bf16_ppl\\\": 7.0351,\\n      \\\"uniform_4bit_ppl\\\": 7.1314,\\n      \\\"l0_random\\\": {\\n        \\\"seed_0\\\": 7.5233,\\n        \\\"seed_1\\\": 7.609940053596114,\\n        \\\"seed_2\\\": 7.413378213414536,\\n        \\\"seed_3\\\": 7.5860269808768255,\\n        \\\"seed_4\\\": 7.669195915436266,\\n        \\\"mean\\\": 7.560368232664748,\\n        \\\"std\\\": 0.08710834742979114\\n      },\\n      \\\"naive_heuristic_ppl\\\": 7.48072281890825,\\n      \\\"mckp_ppl\\\": 7.323111786933877\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_l0_random_median_20260514T072537",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T07:26:05.036598+00:00_

数据已获取。计算 median：

**Qwen2.5-7B — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 11.4860 |
| seed_1 | 11.6153 |
| seed_2 | 11.3251 |
| seed_3 | 11.5151 |
| seed_4 | **12.5147** (离群) |

- **Mean ± Std**: 11.691 ± 0.422
- **Median**: **11.5151** (seed_3)

---

**Llama-3.1-8B — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 9.4845 |
| seed_1 | 10.4884 |
| seed_2 | 9.9406 |
| seed_3 | 10.0381 |
| seed_4 | **12.4441** (离群) |

- **Mean ± Std**: 10.479 ± 1.033
- **Median**: **10.0381** (seed_3)

---

**Mistral-7B-v0.3 — L0-random per-seed PPL:**

| Seed | PPL |
|------|-----|
| seed_0 | 7.5233 |
| seed_1 | 7.6099 |
| seed_2 | 7.4134 |
| seed_3 | 7.5860 |
| seed_4 | 7.6692 |

- **Mean ± Std**: 7.560 ± 0.087
- **Median**: **7.5860** (seed_3)

---

**汇总对比表（所有方法）：**

| Method | Qwen2.5-7B | Llama-3.1-8B | Mistral-7B-v0.3 |
|--------|-----------|-------------|-----------------|
| BF16 baseline | 9.811 | 8.092 | 7.035 |
| Uniform 4-bit | 15.445 | 8.469 | 7.131 |
| Naive heuristic | 12.230 | 9.941 | 7.481 |
| **L0-random mean±std** | **11.691 ± 0.422** | **10.479 ± 1.033** | **7.560 ± 0.087** |
| **L0-random median** | **11.515** | **10.038** | **7.586** |
| MCKP | 10.913 | 8.450 | 7.323 |

seed_4 对 Qwen 和 Llama 影响明显：median 比 mean 分别低 0.176 和 0.441，Mistral 无离群值（median 与 mean 基本一致）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_l0_random_median_20260514T072537"
}
```

</details>

---
