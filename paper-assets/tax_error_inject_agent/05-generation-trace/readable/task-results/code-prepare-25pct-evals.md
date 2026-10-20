# code prepare 25pct evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-25pct-evals_20260515T223443_result.json`
- **Structured JSON:** [`f2131bfc2bf850abb966.json`](../../sessions/f2/f2131bfc2bf850abb966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。摘要：

**Registry 创建** — 4 个 eval 实验均已成功创建（status=PREPARING）：

| exp_id | parent | status |
|--------|--------|--------|
| `v4-taxei-fixed-inject25-s1-eval` | `v4-taxei-fixed-inject25-s1` | PREPARING |
| `v4-taxei-fixed-inject25-s7-eval` | `v4-taxei-fixed-inject25-s7` | PREPARING |
| `v4-random-fixed-inject25-s1-eval` | `v4-random-fixed-inject25-s1` | PREPARING |
| `v4-random-fixed-inject25-s7-eval` | `v4-random-fixed-inject25-s7` | PREPARING |

**服务器检查**：
- `eval/recovery.py` — 存在，25991 bytes，最后修改 May 15 02:30
- `v4_taxei_fixed_inject25_s1` checkpoint — 已确认存在，含 `adapter_model.safetensors`（174MB）+ 完整训练状态文件

待另一个 Worker 确认 `v4-random-fixed-inject25-s1` 和 `v4-taxei-fixed-inject25-s7` 的 checkpoint 路径后即可启动 eval。

---
