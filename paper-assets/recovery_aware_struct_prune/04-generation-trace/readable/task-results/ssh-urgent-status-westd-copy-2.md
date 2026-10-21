# ssh urgent status westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_westd_20260522T183309_result.json`
- **Structured JSON:** [`732836ee55afc3fad075.json`](../../sessions/73/732836ee55afc3fad075.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935 GPU 状态

| GPU | VRAM | Util | 进程 | PID | 状态 |
|-----|------|------|------|-----|------|
| 0 | 16747 / 97887 MiB | 99% | python (eval α=0.5) | 66827 | alive |
| 1 | 17007 / 97887 MiB | 97% | python (eval α=1.0) | 57202 | alive |
| 2 | 19227 / 97887 MiB | 96% | python (eval α=3.0) | 58276 | alive |
| 3 | 17527 / 97887 MiB | 98% | python (eval α=4.0) | 58435 | alive |

## MATH-500 结果

| α | GPU | PID | 状态 | 进度 | 启动时间 | 已运行 | 预估剩余 |
|---|-----|-----|------|------|----------|--------|----------|
| 0.5 | 0 | 66827 | running | 235/500 (47%) | 05-22 23:19 | ~3h14m | ~3.5h |
| 1.0 | 1 | 57202 | running | 304/500 (61%) | 05-23 00:49 | ~1h45m | ~1.7h |
| 3.0 | 2 | 58276 | running | 82/500 (16%) | 05-23 01:47 | ~46m | ~3.5h |
| 4.0 | 3 | 58435 | running | 282/500 (56%) | 05-22 23:20 | ~3h13m | ~2.5h |

**注意**: 实际跑的是 α=**1.0**（不是 α=2.0）。日志文件名为 `eval_math500_sft_rasp_alpha1p0_20.log`，没有 α=2.0 的 MATH-500 eval。

## 空闲 GPU
- 无（4 张 GPU 全部满载）

---
