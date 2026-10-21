# analysis eval pi05 l2norm k095 long strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k095_long_strict_20260527T095613_result.json`
- **Structured JSON:** [`fc73d97951bb7c1bc662.json`](../../sessions/fc/fc73d97951bb7c1bc662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**结果：overall_sr = 86.2%**

- 原值（cqa1 宽松条件）：87.0%
- Strict 重跑：86.2%
- Δ = -0.8pp，与 Attn 系列 strict 偏差模式一致（Attn k=0.95 Δ=0pp，k=0.9 Δ=-0.2pp）
- 结论：**success** — L2norm k=0.95 Long 的 87.0% 基本可信，strict 条件下仅微降 0.8pp

---
