# fix verify gpu state and recover

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_verify-gpu-state-and-recover_20260516T055651_result.json`
- **Structured JSON:** [`cd90a2529a2f9d831c38.json`](../../sessions/cd/cd90a2529a2f9d831c38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 GPU 满载确认。

## 报告

| GPU | 实验 | PID | 当前 step | 速度 | 预计完成 |
|-----|------|-----|-----------|------|----------|
| cuda:0 | plan018-additive-random-b01-s45-r3 (random β=0.1, seed 45) | 688887 | 8/500 | ~10s/step | ~1.3h (~15:20 UTC) |
| cuda:1 | sweep-isr-b02-s44 (ISR bonus β=0.2, seed 44) | 688219 | 11/500 | ~13s/step | ~1.7h (~15:40 UTC) |

**磁盘**: 197G/250G (79%), 54G 空闲 — 足够完成两个实验。

**处理的问题**:
- GPU 0 上已有另一个 worker 提交的 r3 job，我提交的 r2 因 OOM 死亡 → 已清理 r2 残留目录
- plan018-random-b01-s45-r2 registry 已标记 DONE/failed
- sweep-isr-b02-s44 registry 从 PREPARING 更新为 RUNNING（PID 更新为实际进程 688219）
- plan018-additive-random-b01-s45-r3 已注册到 registry

---
