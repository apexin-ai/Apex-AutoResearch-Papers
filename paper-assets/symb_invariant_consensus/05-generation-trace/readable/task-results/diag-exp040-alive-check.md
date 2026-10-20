# diag exp040 alive check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp040-alive-check_20260519T073434_result.json`
- **Structured JSON:** [`131b626071494109936d.json`](../../sessions/13/131b626071494109936d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## Part 1: exp-040 存活检查
- **存活**，tmux session `exp033` 运行中
- cuda:1 GPU-Util 100%, vLLM 进程活跃
- **进度：~482/600**（results.json 481 条，intermediates 482 个）
- 当前准确率：SICA=85.4%, SC=84.8%

## Part 2: EXP-E 部署完成
- **exp-063-llama8b-folio204-16639** 已部署在 cuda:0
- vLLM: tmux `exp063_vllm`, port 8004
- 全量运行: tmux `exp063_run`, 204 问题
- Dry-run 通过（3/3，SICA=66.7% SC=33.3%）
- Registry 已注册为 RUNNING
- 预计运行时间：~204 × 26s ≈ 88 min

---
