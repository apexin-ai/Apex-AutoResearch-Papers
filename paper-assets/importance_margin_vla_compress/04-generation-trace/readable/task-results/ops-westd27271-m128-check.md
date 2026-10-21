# ops westd27271 m128 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-m128-check_20260521T052148_result.json`
- **Structured JSON:** [`5a5b6f32dd9e0f390831.json`](../../sessions/5a/5a5b6f32dd9e0f390831.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M128 Eval 状态

**进程**: 存活，PID 176320，GPU 0，77% util，36GB VRAM

**进度**: Task 0/10，Ep 16/50 已完成，正在跑 Ep 17

**SR**: 0/16 SUCCESS，全部 FAIL（每个 ep 都跑满 280 步超时）

**趋势**: 纯 0%，没有任何一个 episode 成功。

**值得注意**: 日志头部有严重的权重加载 WARNING —— 291 个 missing keys + 419 个 unexpected keys。Missing 的是普通权重（如 `layers.0.self_attn.q_proj.weight`），unexpected 的是 LoRA 格式权重（如 `q_proj.base_layer.weight`, `q_proj.lora_A.default.weight`）。说明 checkpoint 是 LoRA adapter 格式，但加载时没有正确走 LoRA merge 路径，导致模型权重实际上是随机/空的。这大概率是全 0% 的根因。

另外还有一个昨天的旧 run（`vtconly_20k`），那个 checkpoint 加载是 `strict match`，没有 missing/unexpected keys。

---
