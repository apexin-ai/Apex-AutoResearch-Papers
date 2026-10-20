# code verify num generations

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_code_verify-num-generations_20260516T030412.jsonl`
- **Structured JSON:** [`e643e96859817958df3e.json`](../../sessions/e6/e643e96859817958df3e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-16T03:05:37.885995+00:00_

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
  "session": "worker_code_verify-num-generations_20260516T030412",
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

_source line 2 · 2026-05-16T03:05:37.886428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:05:37.886615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -20 /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -20 /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:05:37.887002+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 1, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 1e-06, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:41:57.699839+00:00\\\"}\\n{\\\"step\\\": 2, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.9e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:42:02.659698+00:00\\\"}\\n{\\\"step\\\": 3, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.8e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:42:22.905412+00:00\\\"}\\n{\\\"step\\\": 4, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.7e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:42:40.458740+00:00\\\"}\\n{\\\"step\\\": 5, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.6e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:42:50.061333+00:00\\\"}\\n{\\\"step\\\": 6, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.499999999999999e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:42:56.116988+00:00\\\"}\\n{\\\"step\\\": 7, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"l
…[truncated 4199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:05:37.887209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -20 /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -20 /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T03:05:37.887361+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "wc -l /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "wc -l /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T03:05:37.887645+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 1, \\\"reward_mean\\\": 0.12999999523162842, \\\"reward_std\\\": 0.36769551038742065, \\\"prove_rate\\\": 0.125, \\\"isr_mean\\\": 0.1, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0261, \\\"lr\\\": 1e-06, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:42:08.161700+00:00\\\"}\\n{\\\"step\\\": 2, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.9e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:42:19.743933+00:00\\\"}\\n{\\\"step\\\": 3, \\\"reward_mean\\\": 0.3843749761581421, \\\"reward_std\\\": 0.5304878950119019, \\\"prove_rate\\\": 0.375, \\\"isr_mean\\\": 0.1875, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0676, \\\"lr\\\": 9.8e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:42:32.777205+00:00\\\"}\\n{\\\"step\\\": 4, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.7e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:42:36.004376+00:00\\\"}\\n{\\\"step\\\": 5, \\\"reward_mean\\\": 0.5169791579246521, \\\"reward_std\\\": 0.5526907444000244, \\\"prove_rate\\\": 0.5, \\\"isr_mean\\\": 0.33958333333333335, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0101, \\\"lr\\\": 9.6e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:42:44.537623+00:00\\\"}\\n{\\\"step\\\": 6, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 9.499999999999999e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:43:00.837422+00:00\\\"}\\n{\\\"step\\\": 7, \\\"reward_mean\\\": 0.0, 
…[truncated 4534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T03:05:37.887898+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "wc -l /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "wc -l /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T03:05:37.888056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"100 /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:05:37.888200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"100 /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:05:37.888402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -30 /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -30 /root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:05:37.888787+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 71, \\\"reward_mean\\\": 0.5195833444595337, \\\"reward_std\\\": 0.5554818511009216, \\\"prove_rate\\\": 0.5, \\\"isr_mean\\\": 0.1958333333333333, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0316, \\\"lr\\\": 3e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:52:41.683004+00:00\\\"}\\n{\\\"step\\\": 72, \\\"reward_mean\\\": 0.5166666507720947, \\\"reward_std\\\": 0.5523399114608765, \\\"prove_rate\\\": 0.5, \\\"isr_mean\\\": 0.16666666666666666, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 2.9e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:52:50.436882+00:00\\\"}\\n{\\\"step\\\": 73, \\\"reward_mean\\\": 0.13333334028720856, \\\"reward_std\\\": 0.3771236538887024, \\\"prove_rate\\\": 0.125, \\\"isr_mean\\\": 0.08333333333333333, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": -0.0082, \\\"lr\\\": 2.8e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:53:01.243476+00:00\\\"}\\n{\\\"step\\\": 74, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 2.7e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:53:07.244442+00:00\\\"}\\n{\\\"step\\\": 75, \\\"reward_mean\\\": 0.2611111104488373, \\\"reward_std\\\": 0.48348382115364075, \\\"prove_rate\\\": 0.25, \\\"isr_mean\\\": 0.1111111111111111, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.1191, \\\"lr\\\": 2.6e-07, \\\"beta_t\\\": 0.1, \\\"timestamp\\\": \\\"2026-05-16T02:53:24.097575+00:00\\\"}\\n{\\\"step\\\": 76, \\\"reward_mean\\\": 0.3910714387893677, \\\"reward_std\\\": 0.53972989320755, \\\"prove_rate\\\": 0.375, \\\"isr_mean\\\": 0.1607142857142857, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0252, \\\"lr\\\": 2.5e-07, \\\"beta_t\\\": 0.1, 
…[truncated 7713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:05:37.888985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -30 /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -30 /root/autodl-tmp/outputs/sweep_isr_b005_s42/reward_log.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T03:05:37.889319+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"step\\\": 71, \\\"reward_mean\\\": 0.2541666626930237, \\\"reward_std\\\": 0.47062522172927856, \\\"prove_rate\\\": 0.25, \\\"isr_mean\\\": 0.08333333333333333, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": -0.0048, \\\"lr\\\": 3e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:51:32.556575+00:00\\\"}\\n{\\\"step\\\": 72, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 2.9e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:51:38.816736+00:00\\\"}\\n{\\\"step\\\": 73, \\\"reward_mean\\\": 0.6447321176528931, \\\"reward_std\\\": 0.5339348316192627, \\\"prove_rate\\\": 0.625, \\\"isr_mean\\\": 0.3946428571428572, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0039, \\\"lr\\\": 2.8e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:51:50.066430+00:00\\\"}\\n{\\\"step\\\": 74, \\\"reward_mean\\\": 0.0, \\\"reward_std\\\": 0.0, \\\"prove_rate\\\": 0.0, \\\"isr_mean\\\": 0.0, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0, \\\"lr\\\": 2.7e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:51:55.492802+00:00\\\"}\\n{\\\"step\\\": 75, \\\"reward_mean\\\": 0.12812499701976776, \\\"reward_std\\\": 0.36239221692085266, \\\"prove_rate\\\": 0.125, \\\"isr_mean\\\": 0.0625, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0104, \\\"lr\\\": 2.6e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:52:02.187669+00:00\\\"}\\n{\\\"step\\\": 76, \\\"reward_mean\\\": 0.6489062309265137, \\\"reward_std\\\": 0.537353515625, \\\"prove_rate\\\": 0.625, \\\"isr_mean\\\": 0.478125, \\\"parse_rate\\\": 1.0, \\\"random_mean\\\": null, \\\"loss\\\": 0.0113, \\\"lr\\\": 2.5e-07, \\\"beta_t\\\": 0.05, \\\"timestamp\\\": \\\"2026-05-16T02:52:09.054591+00:00\\\"}\
…[truncated 7985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_verify-num-generations_20260516T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T03:05:37.889582+00:00_

## 汇报

### 实际步数
- **sweep-isr-b01-s45**: 100 步（完成）
- **sweep-isr-b005-s42**: 100 步（完成）

### 实际 K 值：**K=4**（两个实验均是）

判据：所有 prove_rate 值都是 1/8 的整数倍，从未出现 1/16 的值（如 0.0625、0.1875、0.3125）。

batch_size=2 时，prove_rate 粒度 = 1/(2K)：
- K=4 → 粒度 1/8 = 0.125 ✓（与观测吻合）
- K=8 → 粒度 1/16 = 0.0625 ✗（从未观测到）

### prove_rate 分布

**sweep-isr-b01-s45** (β=0.1) — 出现的非零值：

| prove_rate | 对应 | 示例步 |
|---|---|---|
| 0.125 = 1/8 | 1/8 proved | 73, 80, 86, 87, 89 |
| 0.25 = 2/8 | 2/8 proved | 75 |
| 0.375 = 3/8 | 3/8 proved | 76 |
| 0.5 = 4/8 | 4/8 proved | 20, 71, 72, 79, 82, 85, 94, 95 |
| 0.875 = 7/8 | 7/8 proved | 96 |

大量步数 prove_rate=0（前 19 步全是 0），整体训练信号很弱。

**sweep-isr-b005-s42** (β=0.05) — 出现的非零值：

| prove_rate | 对应 | 示例步 |
|---|---|---|
| 0.125 = 1/8 | | 1, 9, 12, 75, 80, 83, 87, 89, 92 |
| 0.25 = 2/8 | | 71, 85, 96 |
| 0.375 = 3/8 | | 3, 79, 81, 95 |
| 0.5 = 4/8 | | 5, 19, 86, 90, 93, 98, 100 |
| 0.625 = 5/8 | | 11, 73, 76, 82, 94 |
| 0.75 = 6/8 | | 20 |

b005-s42 的 prove_rate 分布更丰富，训练信号明显好于 b01-s45。

**结论：K=8 配置未生效，被 argparse 默认值 K=4 覆盖。** 两个实验实际都以 K=4 运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_verify-num-generations_20260516T030412"
}
```

</details>

---
