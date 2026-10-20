# analysis bf16 batch2 random and imp

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_analysis_bf16_batch2_random_and_imp_20260514T064655.jsonl`
- **Structured JSON:** [`93d2b5be4837a2c22847.json`](../../sessions/93/93d2b5be4837a2c22847.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-14T06:50:38.538610+00:00_

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
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
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

_source line 2 · 2026-05-14T06:50:38.538974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T06:50:38.539147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s015.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s015.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T06:50:38.539288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s020.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s020.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T06:50:38.539522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Setting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:36:17,900 [INFO] run_profiling:   -> 35 phases, boundaries at [8, 48, 98, 135, 193, 234, 246, 271, 314, 340, 384, 405, 442, 489, 520, 542, 581, 929, 1009, 1039, 1274, 1287, 1428, 1715, 1795, 1815, 1844, 1885, 1909, 1933, 1946, 1963, 1978, 2021]\\n2026-05-14 14:36:17,900 [INFO] run_profiling: [41/50] Processing problem test/algebra/2277.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:37:10,578 [INFO] run_profiling:   -> 41 phases, boundaries at [17, 37, 171, 241, 352, 397, 456, 502, 526, 550, 567, 628, 670, 746, 845, 857, 901, 913, 924, 1040, 1077, 1102, 1136, 1164, 1231, 1248, 1298, 1440, 1497, 1518, 1716, 1727, 1765, 1801, 1818, 1875, 1897, 1928, 1946, 1993]\\n2026-05-14 14:37:10,579 [INFO] run_profiling: [42/50] Processing problem test/intermediate_algebra/582.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:37:59,095 [INFO] run_profiling:   -> 28 phases, boundaries at [15, 153, 189, 221, 234, 257, 294, 342, 381, 401, 443, 471, 556, 869, 902, 1573, 1592, 1632, 1680, 1692, 1745, 1833, 1856, 1871, 1915, 1937, 1966]\\n2026-05-14 14:37:59,095 [INFO] run_profiling: [43/50] Processing problem test/number_theory/427.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:38:13,127 [INFO] run_profiling:   -> 5 phases, boundaries at [140, 355, 557, 707]\\n2026-05-14 14:38:13,128 [INFO] run_profiling: [44/50] Processing problem test/number_theory/820.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:39:04,794 [INFO] run_profiling:   -> 39 phases, boundaries at [104, 132, 167, 181, 211, 223, 244, 263, 285, 323, 342, 364, 401, 422, 454, 567, 588, 631, 642, 676, 828, 905, 965, 1110, 1147, 1420, 1475, 1542, 1656, 1702, 1741, 1833, 1852, 1889, 1922, 1961, 197
…[truncated 3616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T06:50:38.539700+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s025.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_ds_rand_s025.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T06:50:38.540022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 14:36:18,607 [INFO] run_profiling:   -> 35 phases, boundaries at [8, 48, 98, 135, 193, 234, 246, 271, 314, 340, 384, 405, 442, 489, 520, 542, 581, 929, 1009, 1039, 1274, 1287, 1428, 1715, 1795, 1815, 1844, 1885, 1909, 1933, 1946, 1963, 1978, 2021]\\n2026-05-14 14:36:18,608 [INFO] run_profiling: [41/50] Processing problem test/algebra/2277.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:37:11,015 [INFO] run_profiling:   -> 41 phases, boundaries at [17, 37, 171, 241, 352, 397, 456, 502, 526, 550, 567, 628, 670, 746, 845, 857, 901, 913, 924, 1040, 1077, 1102, 1136, 1164, 1231, 1248, 1298, 1440, 1497, 1518, 1716, 1727, 1765, 1801, 1818, 1875, 1897, 1928, 1946, 1993]\\n2026-05-14 14:37:11,016 [INFO] run_profiling: [42/50] Processing problem test/intermediate_algebra/582.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:37:59,283 [INFO] run_profiling:   -> 28 phases, boundaries at [15, 153, 189, 221, 234, 257, 294, 342, 381, 401, 443, 471, 556, 869, 902, 1573, 1592, 1632, 1680, 1692, 1745, 1833, 1856, 1871, 1915, 1937, 1966]\\n2026-05-14 14:37:59,284 [INFO] run_profiling: [43/50] Processing problem test/number_theory/427.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:38:13,223 [INFO] run_profiling:   -> 5 phases, boundaries at [140, 355, 557, 707]\\n2026-05-14 14:38:13,224 [INFO] run_profiling: [44/50] Processing problem test/number_theory/820.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:39:04,671 [INFO] run_profiling:   -> 39 phases, boundaries at [104, 132, 167, 181, 211, 223, 244, 263, 285, 323, 342, 364, 401, 422, 454, 567, 588, 631, 642, 676, 828, 905, 965, 1110, 1147, 1420, 1475, 1542, 1656, 1702, 1741, 1833, 1852, 1889, 1922, 1961, 1974, 2027]\\n2026-05-14 14:39:04,672 [INFO] run_profiling: [45/50] Processing
…[truncated 3601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:50:38.540362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 14:36:25,990 [INFO] run_profiling:   -> 35 phases, boundaries at [8, 48, 98, 135, 193, 234, 246, 271, 314, 340, 384, 405, 442, 489, 520, 542, 581, 929, 1009, 1039, 1274, 1287, 1428, 1715, 1795, 1815, 1844, 1885, 1909, 1933, 1946, 1963, 1978, 2021]\\n2026-05-14 14:36:25,990 [INFO] run_profiling: [41/50] Processing problem test/algebra/2277.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:37:18,598 [INFO] run_profiling:   -> 41 phases, boundaries at [17, 37, 171, 241, 352, 397, 456, 502, 526, 550, 567, 628, 670, 746, 845, 857, 901, 913, 924, 1040, 1077, 1102, 1136, 1164, 1231, 1248, 1298, 1440, 1497, 1518, 1716, 1727, 1765, 1801, 1818, 1875, 1897, 1928, 1946, 1993]\\n2026-05-14 14:37:18,599 [INFO] run_profiling: [42/50] Processing problem test/intermediate_algebra/582.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:38:06,951 [INFO] run_profiling:   -> 28 phases, boundaries at [15, 153, 189, 221, 234, 257, 294, 342, 381, 401, 443, 471, 556, 869, 902, 1573, 1592, 1632, 1680, 1692, 1745, 1833, 1856, 1871, 1915, 1937, 1966]\\n2026-05-14 14:38:06,952 [INFO] run_profiling: [43/50] Processing problem test/number_theory/427.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:38:20,936 [INFO] run_profiling:   -> 5 phases, boundaries at [140, 355, 557, 707]\\n2026-05-14 14:38:20,936 [INFO] run_profiling: [44/50] Processing problem test/number_theory/820.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:39:12,562 [INFO] run_profiling:   -> 39 phases, boundaries at [104, 132, 167, 181, 211, 223, 244, 263, 285, 323, 342, 364, 401, 422, 454, 567, 588, 631, 642, 676, 828, 905, 965, 1110, 1147, 1420, 1475, 1542, 1656, 1702, 1741, 1833, 1852, 1889, 1922, 1961, 1974, 2027]\\n2026-05-14 14:39:12,563 [INFO] run_profiling: [45/50] Processing
…[truncated 3611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T06:50:38.540602+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_importance_s020.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_importance_s020.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T06:50:38.540745+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_importance_s030.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -50 ~/runs/phase-gated-compound-sparse/bf16_importance_s030.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T06:50:38.540937+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Setting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:19:16,852 [INFO] run_profiling:   -> 35 phases, boundaries at [8, 48, 98, 135, 193, 234, 246, 271, 314, 340, 384, 405, 442, 489, 520, 542, 581, 929, 1009, 1039, 1274, 1287, 1428, 1715, 1795, 1815, 1844, 1885, 1909, 1933, 1946, 1963, 1978, 2021]\\n2026-05-14 14:19:16,852 [INFO] run_profiling: [41/50] Processing problem test/algebra/2277.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:20:57,582 [INFO] run_profiling:   -> 41 phases, boundaries at [17, 37, 171, 241, 352, 397, 456, 502, 526, 550, 567, 628, 670, 746, 845, 857, 901, 913, 924, 1040, 1077, 1102, 1136, 1164, 1231, 1248, 1298, 1440, 1497, 1518, 1716, 1727, 1765, 1801, 1818, 1875, 1897, 1928, 1946, 1993]\\n2026-05-14 14:20:57,582 [INFO] run_profiling: [42/50] Processing problem test/intermediate_algebra/582.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:22:29,342 [INFO] run_profiling:   -> 28 phases, boundaries at [15, 153, 189, 221, 234, 257, 294, 342, 381, 401, 443, 471, 556, 869, 902, 1573, 1592, 1632, 1680, 1692, 1745, 1833, 1856, 1871, 1915, 1937, 1966]\\n2026-05-14 14:22:29,342 [INFO] run_profiling: [43/50] Processing problem test/number_theory/427.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:22:56,336 [INFO] run_profiling:   -> 5 phases, boundaries at [140, 355, 557, 707]\\n2026-05-14 14:22:56,336 [INFO] run_profiling: [44/50] Processing problem test/number_theory/820.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:24:36,741 [INFO] run_profiling:   -> 39 phases, boundaries at [104, 132, 167, 181, 211, 223, 244, 263, 285, 323, 342, 364, 401, 422, 454, 567, 588, 631, 642, 676, 828, 905, 965, 1110, 1147, 1420, 1475, 1542, 1656, 1702, 1741, 1833, 1852, 1889, 1922, 1961, 197
…[truncated 3606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:50:38.541147+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Setting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:25:58,742 [INFO] run_profiling:   -> 35 phases, boundaries at [8, 48, 98, 135, 193, 234, 246, 271, 314, 340, 384, 405, 442, 489, 520, 542, 581, 929, 1009, 1039, 1274, 1287, 1428, 1715, 1795, 1815, 1844, 1885, 1909, 1933, 1946, 1963, 1978, 2021]\\n2026-05-14 14:25:58,742 [INFO] run_profiling: [41/50] Processing problem test/algebra/2277.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:27:42,201 [INFO] run_profiling:   -> 41 phases, boundaries at [17, 37, 171, 241, 352, 397, 456, 502, 526, 550, 567, 628, 670, 746, 845, 857, 901, 913, 924, 1040, 1077, 1102, 1136, 1164, 1231, 1248, 1298, 1440, 1497, 1518, 1716, 1727, 1765, 1801, 1818, 1875, 1897, 1928, 1946, 1993]\\n2026-05-14 14:27:42,202 [INFO] run_profiling: [42/50] Processing problem test/intermediate_algebra/582.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:29:17,575 [INFO] run_profiling:   -> 28 phases, boundaries at [15, 153, 189, 221, 234, 257, 294, 342, 381, 401, 443, 471, 556, 869, 902, 1573, 1592, 1632, 1680, 1692, 1745, 1833, 1856, 1871, 1915, 1937, 1966]\\n2026-05-14 14:29:17,575 [INFO] run_profiling: [43/50] Processing problem test/number_theory/427.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:29:44,209 [INFO] run_profiling:   -> 5 phases, boundaries at [140, 355, 557, 707]\\n2026-05-14 14:29:44,209 [INFO] run_profiling: [44/50] Processing problem test/number_theory/820.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 14:31:23,313 [INFO] run_profiling:   -> 39 phases, boundaries at [104, 132, 167, 181, 211, 223, 244, 263, 285, 323, 342, 364, 401, 422, 454, 567, 588, 631, 642, 676, 828, 905, 965, 1110, 1147, 1420, 1475, 1542, 1656, 1702, 1741, 1833, 1852, 1889, 1922, 1961, 197
…[truncated 3611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T06:50:38.541340+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T06:50:38.541493+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T06:50:38.541818+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1687,\\n        \\\"attn\\\": 3.5947,\\n        \\\"kv\\\": 2.9239,\\n        \\\"both\\\": 5.7569\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2284,\\n        \\\"attn\\\": 11.3419,\\n        \\\"kv\\\": 3.6161,\\n        \\\"both\\\": 6.2886\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 297.7957,\\n        \\\"kv\\\": 2.915,\\n        \\\"both\\\": 11.3156\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 0.384934,\\n        \\\"ci_low\\\": -0.540924,\\n        \\\"ci_high\\\": 1.314665,\\n        \\\"median\\\": 0.114695,\\n        \\\"winsorized_mean\\\": 0.316098,\\n        \\\"skewness\\\": -5.4014,\\n        \\\"outlier_count\\\": 4\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": -5.732553,\\n        \\\"ci_low\\\": -10.92833,\\n    
…[truncated 8043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:50:38.542177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.2\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.1687,\\n        \\\"attn\\\": 3.1905,\\n        \\\"kv\\\": 3.8002,\\n        \\\"both\\\": 8.8129\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.2284,\\n        \\\"attn\\\": 8.592,\\n        \\\"kv\\\": 5.0078,\\n        \\\"both\\\": 9.2001\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 67.8504,\\n        \\\"kv\\\": 3.788,\\n        \\\"both\\\": 11.4974\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"mean\\\": 2.525895,\\n        \\\"ci_low\\\": 1.254586,\\n        \\\"ci_high\\\": 4.235625,\\n        \\\"median\\\": 0.327821,\\n        \\\"winsorized_mean\\\": 1.766381,\\n        \\\"skewness\\\": 9.5932,\\n        \\\"outlier_count\\\": 4\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"mean\\\": -2.480513,\\n        \\\"ci_low\\\": -5.629591,\\n        \\\"ci_
…[truncated 8048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T06:50:38.542341+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T06:50:38.542497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T06:50:38.542621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T06:50:38.542955+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.25\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1687,\\n        \\\"attn\\\": 7.237,\\n        \\\"kv\\\": 4.9751,\\n        \\\"both\\\": 17.7423\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.2284,\\n        \\\"attn\\\": 24.3571,\\n        \\\"kv\\\": 6.7993,\\n        \\\"both\\\": 17.9694\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 868.3199,\\n        \\\"kv\\\": 5.1165,\\n        \\\"both\\\": 29.4661\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"mean\\\": 5.590551,\\n        \\\"ci_low\\\": 1.171567,\\n        \\\"ci_high\\\": 9.465606,\\n        \\\"median\\\": 1.554497,\\n        \\\"winsorized_mean\\\": 6.396533,\\n        \\\"skewness\\\": -7.566,\\n        \\\"outlier_count\\\": 4\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"mean\\\": -9.106223,\\n        \\\"ci_low\\\": -25.804467,\\n   
…[truncated 8054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T06:50:38.543397+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.2\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.1689,\\n        \\\"attn\\\": 1.5233,\\n        \\\"kv\\\": 1.6191,\\n        \\\"both\\\": 2.1047\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.2286,\\n        \\\"attn\\\": 1.6486,\\n        \\\"kv\\\": 15.7987,\\n        \\\"both\\\": 23.74\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 1.5375,\\n        \\\"kv\\\": 3.5164,\\n        \\\"both\\\": 5.4246\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"mean\\\": 0.128925,\\n        \\\"ci_low\\\": -0.197532,\\n        \\\"ci_high\\\": 0.664714,\\n        \\\"median\\\": 0.014513,\\n        \\\"winsorized_mean\\\": -0.029682,\\n        \\\"skewness\\\": 16.6701,\\n        \\\"outlier_count\\\": 2\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"mean\\\": 6.028786,\\n 
…[truncated 8044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T06:50:38.543939+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.3\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.1689,\\n        \\\"attn\\\": 1.7123,\\n        \\\"kv\\\": 2.0544,\\n        \\\"both\\\": 3.2372\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2286,\\n        \\\"attn\\\": 1.9347,\\n        \\\"kv\\\": 51.6485,\\n        \\\"both\\\": 122.609\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 1.7894,\\n        \\\"kv\\\": 9.4821,\\n        \\\"both\\\": 24.2847\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 0.554708,\\n        \\\"ci_low\\\": 0.277272,\\n        \\\"ci_high\\\": 0.919782,\\n        \\\"median\\\": 0.053399,\\n        \\\"winsorized_mean\\\": 0.336673,\\n        \\\"skewness\\\": 10.622,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 57.794625,\\n
…[truncated 8054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T06:50:38.544186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"\nimport json\nfiles = {\n  'bf16_ds_rand_s015': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json',\n  'bf16_ds_rand_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json',\n  'bf16_ds_rand_s025': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json',\n  'bf16_imp_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json',\n  'bf16_imp_s030': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json',\n}\nimport statistics\nfor name, path in files.items():\n    d = json.load(open(path))\n    diag = d['diagnostics']\n    # Check if per_problem_ii_stats exists as a key\n    print(f'=== {name} ===')\n    print('Keys in diagnostics:', list(diag.keys()))\n    # Compute per-problem stats from raw data\n    pp = diag.get('per_problem_ii', diag.get('per_problem_ii_stats', []))\n    if not pp:\n        pp = [p for p in diag.get('per_problem_sparsity', []) if 'ii_high' in (p if isinstance(p, dict) else {})]\n        if not pp:\n            # Try the other structure\n            for k in diag:\n                if 'ii' in k.lower():\n                    print(f'  Found key: {k}')\n    # Get ii values per phase\n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    print(f'  high: n={len(highs)}, min={min(highs):.4f}, max={max(highs):.4f}, mean={statistics.mean(highs):.4f}, median={statistics.median(highs):.4f}, std={statistics.stdev(highs):.4f}')\n    print(f'  mid:  n={len(mids)}, min={min(mids):.4f}, max={max(mids):.4f}, mean={statistics.mean(mids):.4f}, median={statistics.median(mids):.4f}, std={statistics.stdev(mids):.4f}')\n    print(f'  low:  n={len(lows)}, min={min(lows):.4f}, max={max(lows):.4f}, mean={statistics.mean(lows):.4f}, median={statistics.median(lows):.4f}, std={statistics.stdev(lows):.4f}')\n    # Gradient\n    med_low = statistics.median(lows)\n    med_high = statistics.median(highs)\n    grad = med_low / med_high if med_high != 0 else float('inf')\n    print(f'  gradient(low_median/high_median) = {grad:.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"\nimport json\nfiles = {\n  'bf16_ds_rand_s015': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json',\n  'bf16_ds_rand_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json',\n  'bf16_ds_rand_s025': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json',\n  'bf16_imp_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json',\n  'bf16_imp_s030': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json',\n}\nimport statistics\nfor name, path in files.items():\n    d = json.load(open(path))\n    diag = d['diagnostics']\n    # Check if per_problem_ii_stats exists as a key\n    print(f'=== {name} ===')\n    print('Keys in diagnostics:', list(diag.keys()))\n    # Compute per-problem stats from raw data\n    pp = diag.get('per_problem_ii', diag.get('per_problem_ii_stats', []))\n    if not pp:\n        pp = [p for p in diag.get('per_problem_sparsity', []) if 'ii_high' in (p if isinstance(p, dict) else {})]\n        if not pp:\n            # Try the other structure\n            for k in diag:\n                if 'ii' in k.lower():\n                    print(f'  Found key: {k}')\n    # Get ii values per phase\n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    print(f'  high: n={len(highs)}, min={min(highs):.4f}, max={max(highs):.4f}, mean={statistics.mean(highs):.4f}, median={statistics.median(highs):.4f}, std={statistics.stdev(highs):.4f}')\n    print(f'  mid:  n={len(mids)}, min={min(mids):.4f}, max={max(mids):.4f}, mean={statistics.mean(mids):.4f}, median={statistics.median(mids):.4f}, std={statistics.stdev(mids):.4f}')\n    print(f'  low:  n={len(lows)}, min={min(lows):.4f}, max={max(lows):.4f}, mean={statistics.mean(lows):.4f}, median={statistics.median(lows):.4f}, std={statistics.stdev(lows):.4f}')\n    # Gradient\n    med_low = statistics.median(lows)\n    med_high = statistics.median(highs)\n    grad = med_low / med_high if med_high != 0 else float('inf')\n    print(f'  gradient(low_median/high_median) = {grad:.4f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T06:50:38.544345+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T06:50:38.544553+00:00_

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
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
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

_source line 26 · 2026-05-14T06:50:38.544706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T06:50:38.544832+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, statistics\n\nfiles = {\n  'bf16_ds_rand_s015': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json',\n  'bf16_ds_rand_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json',\n  'bf16_ds_rand_s025': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json',\n  'bf16_imp_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json',\n  'bf16_imp_s030': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json',\n}\n\nfor name, path in files.items():\n    d = json.load(open(path))\n    diag = d['diagnostics']\n    pp = diag.get('per_problem_ii', [])\n    if not pp:\n        # fallback: look in per_problem_sparsity which has ii_high/ii_mid/ii_low\n        pp = [p for p in diag.get('per_problem_sparsity', []) if 'ii_high' in p]\n    \n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    \n    print(f'=== {name} ===')\n    for label, vals in [('high', highs), ('mid', mids), ('low', lows)]:\n        if vals:\n            print(f'  {label}: n={len(vals)}, min={min(vals):.4f}, max={max(vals):.4f}, mean={statistics.mean(vals):.4f}, median={statistics.median(vals):.4f}, std={statistics.stdev(vals):.4f}')\n    \n    med_low = statistics.median(lows) if lows else 0\n    med_high = statistics.median(highs) if highs else 0\n    if med_high != 0:\n        grad = med_low / med_high\n    else:\n        grad = float('inf')\n    print(f'  gradient(low_med/high_med) = {grad:.4f}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, statistics\n\nfiles = {\n  'bf16_ds_rand_s015': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json',\n  'bf16_ds_rand_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json',\n  'bf16_ds_rand_s025': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json',\n  'bf16_imp_s020': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json',\n  'bf16_imp_s030': '/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json',\n}\n\nfor name, path in files.items():\n    d = json.load(open(path))\n    diag = d['diagnostics']\n    pp = diag.get('per_problem_ii', [])\n    if not pp:\n        # fallback: look in per_problem_sparsity which has ii_high/ii_mid/ii_low\n        pp = [p for p in diag.get('per_problem_sparsity', []) if 'ii_high' in p]\n    \n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    \n    print(f'=== {name} ===')\n    for label, vals in [('high', highs), ('mid', mids), ('low', lows)]:\n        if vals:\n            print(f'  {label}: n={len(vals)}, min={min(vals):.4f}, max={max(vals):.4f}, mean={statistics.mean(vals):.4f}, median={statistics.median(vals):.4f}, std={statistics.stdev(vals):.4f}')\n    \n    med_low = statistics.median(lows) if lows else 0\n    med_high = statistics.median(highs) if highs else 0\n    if med_high != 0:\n        grad = med_low / med_high\n    else:\n        grad = float('inf')\n    print(f'  gradient(low_med/high_med) = {grad:.4f}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T06:50:38.544976+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== bf16_ds_rand_s015 ===\\n  gradient(low_med/high_med) = inf\\n\\n=== bf16_ds_rand_s020 ===\\n  gradient(low_med/high_med) = inf\\n\\n=== bf16_ds_rand_s025 ===\\n  gradient(low_med/high_med) = inf\\n\\n=== bf16_imp_s020 ===\\n  gradient(low_med/high_med) = inf\\n\\n=== bf16_imp_s030 ===\\n  gradient(low_med/high_med) = inf\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T06:50:38.545112+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json'))\ndiag = d['diagnostics']\nprint('diagnostics keys:', list(diag.keys()))\nfor k in diag:\n    v = diag[k]\n    if isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if v:\n            print(f'    first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n    elif isinstance(v, dict):\n        print(f'  {k}: dict with keys {list(v.keys())}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json'))\ndiag = d['diagnostics']\nprint('diagnostics keys:', list(diag.keys()))\nfor k in diag:\n    v = diag[k]\n    if isinstance(v, list):\n        print(f'  {k}: list of {len(v)} items')\n        if v:\n            print(f'    first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n    elif isinstance(v, dict):\n        print(f'  {k}: dict with keys {list(v.keys())}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T06:50:38.545246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"diagnostics keys: ['per_problem_sparsity', 'global_sparsity_histogram']\\n  per_problem_sparsity: list of 50 items\\n    first item keys: ['problem_id', 'sparsity_values', 'n_tokens', 'sparsity_mean', 'sparsity_std', 'sparsity_min', 'sparsity_max', 'n_phases_detected', 'phase_sizes', 'phase_names', 'segmentation_method', 'quantile_boundaries', 'quantile_group_stats']\\n  global_sparsity_histogram: dict with keys ['bins', 'counts']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T06:50:38.545399+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json'))\nprint('Top-level keys:', list(d.keys()))\n# Check for per_problem_ii anywhere\nfor k in d:\n    if 'ii' in k.lower() or 'problem' in k.lower():\n        v = d[k]\n        if isinstance(v, list) and v:\n            print(f'{k}: list[{len(v)}], first keys={list(v[0].keys()) if isinstance(v[0],dict) else type(v[0])}')\n        elif isinstance(v, dict):\n            print(f'{k}: dict keys={list(v.keys())[:5]}...')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json'))\nprint('Top-level keys:', list(d.keys()))\n# Check for per_problem_ii anywhere\nfor k in d:\n    if 'ii' in k.lower() or 'problem' in k.lower():\n        v = d[k]\n        if isinstance(v, list) and v:\n            print(f'{k}: list[{len(v)}], first keys={list(v[0].keys()) if isinstance(v[0],dict) else type(v[0])}')\n        elif isinstance(v, dict):\n            print(f'{k}: dict keys={list(v.keys())[:5]}...')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T06:50:38.545610+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Top-level keys: ['config', 'phase_stats', 'perplexity', 'interaction_index', 'pass_fail', 'warnings', 'diagnostics', 'per_problem_ii']\\nper_problem_ii: dict keys=['0.15']...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T06:50:38.545742+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, statistics\n\nfiles = {\n  'bf16_ds_rand_s015': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json', '0.15'),\n  'bf16_ds_rand_s020': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json', '0.2'),\n  'bf16_ds_rand_s025': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json', '0.25'),\n  'bf16_imp_s020': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json', '0.2'),\n  'bf16_imp_s030': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json', '0.3'),\n}\n\nfor name, (path, sp) in files.items():\n    d = json.load(open(path))\n    pp = d['per_problem_ii'][sp]\n    \n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    \n    print(f'=== {name} (s={sp}) ===')\n    for label, vals in [('high', highs), ('mid', mids), ('low', lows)]:\n        if vals:\n            print(f'  {label}: n={len(vals)}, min={min(vals):.4f}, max={max(vals):.4f}, mean={statistics.mean(vals):.4f}, median={statistics.median(vals):.4f}, std={statistics.stdev(vals):.4f}')\n    \n    med_low = statistics.median(lows)\n    med_high = statistics.median(highs)\n    if med_high != 0:\n        grad = med_low / med_high\n    else:\n        grad = float('inf')\n    print(f'  gradient(low_med/high_med) = {grad:.4f}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, statistics\n\nfiles = {\n  'bf16_ds_rand_s015': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json', '0.15'),\n  'bf16_ds_rand_s020': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020/profiling_results.json', '0.2'),\n  'bf16_ds_rand_s025': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025/profiling_results.json', '0.25'),\n  'bf16_imp_s020': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020/profiling_results.json', '0.2'),\n  'bf16_imp_s030': ('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json', '0.3'),\n}\n\nfor name, (path, sp) in files.items():\n    d = json.load(open(path))\n    pp = d['per_problem_ii'][sp]\n    \n    highs = [p['ii_high'] for p in pp if p.get('ii_high') is not None]\n    mids = [p['ii_mid'] for p in pp if p.get('ii_mid') is not None]\n    lows = [p['ii_low'] for p in pp if p.get('ii_low') is not None]\n    \n    print(f'=== {name} (s={sp}) ===')\n    for label, vals in [('high', highs), ('mid', mids), ('low', lows)]:\n        if vals:\n            print(f'  {label}: n={len(vals)}, min={min(vals):.4f}, max={max(vals):.4f}, mean={statistics.mean(vals):.4f}, median={statistics.median(vals):.4f}, std={statistics.stdev(vals):.4f}')\n    \n    med_low = statistics.median(lows)\n    med_high = statistics.median(highs)\n    if med_high != 0:\n        grad = med_low / med_high\n    else:\n        grad = float('inf')\n    print(f'  gradient(low_med/high_med) = {grad:.4f}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T06:50:38.545896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== bf16_ds_rand_s015 (s=0.15) ===\\n  high: n=49, min=-17.4797, max=22.5146, mean=0.2208, median=0.0931, std=4.1856\\n  mid: n=40, min=-75.8992, max=6.2495, mean=-3.3604, median=0.0967, std=15.4282\\n  low: n=50, min=-59.7311, max=5.0415, mean=-1.8952, median=0.1026, std=10.2205\\n  gradient(low_med/high_med) = 1.1028\\n\\n=== bf16_ds_rand_s020 (s=0.2) ===\\n  high: n=49, min=-4.5854, max=29.4003, mean=1.1216, median=0.2918, std=4.6109\\n  mid: n=40, min=-80.8773, max=11.0717, mean=-1.5827, median=0.3504, std=13.8427\\n  low: n=50, min=-38.3425, max=8.3532, mean=-0.4116, median=0.2763, std=7.3481\\n  gradient(low_med/high_med) = 0.9467\\n\\n=== bf16_ds_rand_s025 (s=0.25) ===\\n  high: n=49, min=-13.5968, max=44.5263, mean=3.5900, median=0.8182, std=8.6725\\n  mid: n=40, min=-126.2488, max=18.7198, mean=-1.8455, median=0.9324, std=26.7996\\n  low: n=50, min=-91.2344, max=25.7084, mean=0.7212, median=1.3627, std=16.9395\\n  gradient(low_med/high_med) = 1.6655\\n\\n=== bf16_imp_s020 (s=0.2) ===\\n  high: n=49, min=-0.1884, max=0.4196, mean=0.0025, median=0.0036, std=0.0976\\n  mid: n=40, min=-0.0519, max=8.6969, mean=0.6795, median=0.1977, std=1.5189\\n  low: n=50, min=-1.6151, max=22.6875, mean=2.2301, median=1.1280, std=4.4202\\n  gradient(low_med/high_med) = 314.0331\\n\\n=== bf16_imp_s030 (s=0.3) ===\\n  high: n=49, min=-0.5095, max=4.4457, mean=0.1976, median=0.0343, std=0.6864\\n  mid: n=40, min=-0.1989, max=34.0258, mean=5.2585, median=1.5173, std=8.0394\\n  low: n=50, min=-7.3027, max=126.7985, mean=22.6601, median=9.9731, std=28.6981\\n  gradient(low_med/high_med) = 291.1489\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T06:50:38.546215+00:00_

数据齐全。以下是 5 个实验的完整分析结果。

---

## 1. bf16_ds_rand_s015

```json
{
  "exp_id": "bf16_ds_rand_s015",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.3849, "ci": [-0.5409, 1.3147], "median": 0.1147, "winsorized_mean": 0.3161, "skewness": -5.4014},
      "mid":  {"mean": -172.6626, "ci": [-427.0058, -9.0687], "median": 0.0969, "winsorized_mean": -0.6366, "skewness": -10.5634},
      "low":  {"mean": -5.7326, "ci": [-10.9283, -1.4391], "median": 0.1121, "winsorized_mean": 0.0521, "skewness": -11.5715}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -17.4797, "max": 22.5146, "mean": 0.2208, "median": 0.0931, "std": 4.1856},
      "mid":  {"n": 40, "min": -75.8992, "max": 6.2495, "mean": -3.3604, "median": 0.0967, "std": 15.4282},
      "low":  {"n": 50, "min": -59.7311, "max": 5.0415, "mean": -1.8952, "median": 0.1026, "std": 10.2205}
    },
    "gradient_paired_aggregate": 0.98,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 3.5947, "kv": 2.9239, "both": 5.7569},
      "low":  {"dense": 1.2284, "attn": 11.3419, "kv": 3.6161, "both": 6.2886},
      "mid":  {"dense": 1.2269, "attn": 297.7957, "kv": 2.915, "both": 11.3156}
    }
  }
}
```

---

## 2. bf16_ds_rand_s020

```json
{
  "exp_id": "bf16_ds_rand_s020",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 2.5259, "ci": [1.2546, 4.2356], "median": 0.3278, "winsorized_mean": 1.7664, "skewness": 9.5932},
      "mid":  {"mean": -36.0516, "ci": [-93.2484, -2.2016], "median": 0.2977, "winsorized_mean": 0.5839, "skewness": -12.3126},
      "low":  {"mean": -2.4805, "ci": [-5.6296, 0.1128], "median": 0.3909, "winsorized_mean": 0.9942, "skewness": -10.0661}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -4.5854, "max": 29.4003, "mean": 1.1216, "median": 0.2918, "std": 4.6109},
      "mid":  {"n": 40, "min": -80.8773, "max": 11.0717, "mean": -1.5827, "median": 0.3504, "std": 13.8427},
      "low":  {"n": 50, "min": -38.3425, "max": 8.3532, "mean": -0.4116, "median": 0.2763, "std": 7.3481}
    },
    "gradient_paired_aggregate": 1.19,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": true, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 3.1905, "kv": 3.8002, "both": 8.8129},
      "low":  {"dense": 1.2284, "attn": 8.592, "kv": 5.0078, "both": 9.2001},
      "mid":  {"dense": 1.2269, "attn": 67.8504, "kv": 3.788, "both": 11.4974}
    }
  }
}
```

---

## 3. bf16_ds_rand_s025

```json
{
  "exp_id": "bf16_ds_rand_s025",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 5.5906, "ci": [1.1716, 9.4656], "median": 1.5545, "winsorized_mean": 6.3965, "skewness": -7.566},
      "mid":  {"mean": -514.2418, "ci": [-1361.4741, -24.9357], "median": 1.0202, "winsorized_mean": 3.1014, "skewness": -12.7601},
      "low":  {"mean": -9.1062, "ci": [-25.8045, 2.5166], "median": 1.8937, "winsorized_mean": 4.1866, "skewness": -15.8457}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -13.5968, "max": 44.5263, "mean": 3.5900, "median": 0.8182, "std": 8.6725},
      "mid":  {"n": 40, "min": -126.2488, "max": 18.7198, "mean": -1.8455, "median": 0.9324, "std": 26.7996},
      "low":  {"n": 50, "min": -91.2344, "max": 25.7084, "mean": 0.7212, "median": 1.3627, "std": 16.9395}
    },
    "gradient_paired_aggregate": 1.22,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": true, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1687, "attn": 7.237, "kv": 4.9751, "both": 17.7423},
      "low":  {"dense": 1.2284, "attn": 24.3571, "kv": 6.7993, "both": 17.9694},
      "mid":  {"dense": 1.2269, "attn": 868.3199, "kv": 5.1165, "both": 29.4661}
    }
  }
}
```

---

## 4. bf16_importance_s020

```json
{
  "exp_id": "bf16_importance_s020",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.1289, "ci": [-0.1975, 0.6647], "median": 0.0145, "winsorized_mean": -0.0297, "skewness": 16.6701},
      "mid":  {"mean": 1.2604, "ci": [0.7466, 1.8962], "median": 0.2027, "winsorized_mean": 0.7660, "skewness": 7.0541},
      "low":  {"mean": 6.0288, "ci": [4.4671, 7.9237], "median": 1.4963, "winsorized_mean": 4.3426, "skewness": 6.012}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -0.1884, "max": 0.4196, "mean": 0.0025, "median": 0.0036, "std": 0.0976},
      "mid":  {"n": 40, "min": -0.0519, "max": 8.6969, "mean": 0.6795, "median": 0.1977, "std": 1.5189},
      "low":  {"n": 50, "min": -1.6151, "max": 22.6875, "mean": 2.2301, "median": 1.1280, "std": 4.4202}
    },
    "gradient_paired_aggregate": 103.10,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1689, "attn": 1.5233, "kv": 1.6191, "both": 2.1047},
      "low":  {"dense": 1.2286, "attn": 1.6486, "kv": 15.7987, "both": 23.74},
      "mid":  {"dense": 1.2269, "attn": 1.5375, "kv": 3.5164, "both": 5.4246}
    }
  }
}
```

---

## 5. bf16_importance_s030

```json
{
  "exp_id": "bf16_importance_s030",
  "conclusion": "success",
  "metrics": {
    "interaction_index": {
      "high": {"mean": 0.5547, "ci": [0.2773, 0.9198], "median": 0.0534, "winsorized_mean": 0.3367, "skewness": 10.622},
      "mid":  {"mean": 11.3000, "ci": [6.8650, 17.2633], "median": 2.2833, "winsorized_mean": 8.1752, "skewness": 9.1908},
      "low":  {"mean": 57.7946, "ci": [41.4416, 77.0467], "median": 14.6395, "winsorized_mean": 39.3143, "skewness": 8.3142}
    },
    "per_problem_ii_stats": {
      "high": {"n": 49, "min": -0.5095, "max": 4.4457, "mean": 0.1976, "median": 0.0343, "std": 0.6864},
      "mid":  {"n": 40, "min": -0.1989, "max": 34.0258, "mean": 5.2585, "median": 1.5173, "std": 8.0394},
      "low":  {"n": 50, "min": -7.3027, "max": 126.7985, "mean": 22.6601, "median": 9.9731, "std": 28.6981}
    },
    "gradient_paired_aggregate": 274.24,
    "n_problems": 50,
    "pass_fail": {"ci_overlap": true, "sign_reversal": false, "overall": "PASS"},
    "phase_stats": {"high": {"n_tokens": 21086, "n_segments": 387}, "low": {"n_tokens": 27748, "n_segments": 397}, "mid": {"n_tokens": 13306, "n_segments": 191}},
    "perplexity": {
      "high": {"dense": 1.1689, "attn": 1.7123, "kv": 2.0544, "both": 3.2372},
      "low":  {"dense": 1.2286, "attn": 1.9347, "kv": 51.6485, "both": 122.609},
      "mid":  {"dense": 1.2269, "attn": 1.7894, "kv": 9.4821, "both": 24.2847}
    }
  }
}
```

---

## 汇总表

| exp_id | masking | sparsity | gradient | II_low_median | conclusion |
|--------|---------|----------|----------|---------------|------------|
| bf16_ds_rand_s015 | random | 0.15 | **0.98×** | 0.112 | success |
| bf16_ds_rand_s020 | random | 0.20 | **1.19×** | 0.391 | success |
| bf16_ds_rand_s025 | random | 0.25 | **1.22×** | 1.894 | success |
| bf16_importance_s020 | importance | 0.20 | **103.10×** | 1.496 | success |
| bf16_importance_s030 | importance | 0.30 | **274.24×** | 14.639 | success |

**Random 对照组**：3 个 sparsity 级别的 gradient 均在 0.98×–1.22× 范围内（< 3× 阈值），确认 random masking 无 compound effect。

**Importance 完整趋势**（含已完成参考值）：

| sparsity | gradient | II_low_median |
|----------|----------|---------------|
| 0.15 | 69.24× | 0.398 |
| 0.20 | 103.10× | 1.496 |
| 0.25 | 222.35× | 7.196 |
| 0.30 | 274.24× | 14.639 |

Gradient 和 II_low_median 均随 sparsity 单调递增，compound sparsity effect 在 importance masking 下持续增强。全部 5 个实验 conclusion = **success**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bf16_batch2_random_and_imp_20260514T064655"
}
```

</details>

---
