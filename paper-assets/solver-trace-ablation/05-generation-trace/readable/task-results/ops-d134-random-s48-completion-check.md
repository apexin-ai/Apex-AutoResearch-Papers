# ops d134 random s48 completion check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-random-s48-completion-check_20260518T175729_result.json`
- **Structured JSON:** [`63bc679c68350f1b7bec.json`](../../sessions/63/63bc679c68350f1b7bec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结构化摘要

### s48 结论：FAILED
- **崩溃点**: step 100/500，checkpoint-100 保存时 `safetensors_rust.SafetensorError: No space left on device (os error 28)`
- **训练指标 (step 100)**: prove_rate=0.250, ISR=0.057
- **Registry**: 已更新为 `DONE / failed`
- **Cron**: 已删除

### s49 状态：正在跑但即将崩溃
- PID 124789，GPU 0 占用 80294 MiB，当前 step 6/500
- **磁盘 250G/250G，仅剩 816K** — 到 checkpoint save 时必定 OOM on disk
- 未注册到 registry

### 磁盘/GPU
- **磁盘**: 250G/250G (100%)，816K 可用
- **GPU 0**: 93% util, PID 124789 (s49)

### 紧急问题
s49 在 ~step 50 时会尝试保存 checkpoint（约 7 分钟后），届时因磁盘满必定崩溃。

**可立即释放的空间：**
- s48 的 checkpoint-50 (15G) + checkpoint-100 (13G, 不完整) = 28G
- s47 目录 16G（需确认是否已完成 eval）

是否要删除 s48 的 checkpoint 目录来救 s49？s48 已判定 failed，这些 checkpoint 没有保留价值。

---
