# ops check all gpu status 0519

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-gpu-status-0519_20260519T024730_result.json`
- **Structured JSON:** [`cc80f6d70450ce0709dd.json`](../../sessions/cc/cc80f6d70450ce0709dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the status report:

---

## GPU 状态报告 (2026-05-19 10:48 UTC)

### Seetacloud (4× RTX 5090)

| GPU | 状态 | PID | 任务 | VRAM | GPU Util | 进度 | 预估剩余 |
|-----|------|-----|------|------|----------|------|----------|
| **0** | **运行中** | 778334 | Qwen3-8B CWM repo eval, ckpt-400, seq4096 | 26,325/32,607 MiB | 85% | 1,304/9,784 (13.3%), acc=63.3% | ~17h |
| **1** | **空闲** | — | — | 0 MiB | 0% | — | — |
| **2** | **运行中** | 734440 | DeepSeek CWM repo eval, ckpt-13266 (e3), seq2048 | 15,765/32,607 MiB | 58% | 4,241/9,784 (43.3%) | ~17h |
| **3** | **运行中** | 668680 | DeepSeek CWM repo s123 eval, ckpt-8844, seq4096 | 17,699/32,607 MiB | 50% | 9,354/9,784 (**95.6%**) | ~1-2h |

### Home (1× RTX 5090)

| GPU | 状态 | PID | 任务 | VRAM | GPU Util | 进度 | 预估剩余 |
|-----|------|-----|------|------|----------|------|----------|
| **0** | **运行中** | 15876 | D133 CWM resume: DeepSeek CWM repo s42 e2 eval, seq2048 | 15,779/32,607 MiB | 86% | 5,694/9,784 (58.2%), acc=67.1% | ~3-4h |

### 关键发现

- **GPU 1 seetacloud 确实空闲**，0 MiB / 0% 利用率。有一个 `deepseek-cls-repo-resume-v3` 进程正在加载数据（已完成 tokenization），可能即将占用 GPU 1。
- **GPU 0 seetacloud (PID 778328/778334)**: Qwen3-8B CWM eval **在跑**，已运行 2h37m，进度 13.3%。
- **Home GPU 0 (PID 15872/15876)**: D133 resume **在跑**，已运行 ~3h，进度 58.2%（含 4357 条 resumed 结果）。
- **GPU 3 seetacloud 即将完成**：9,354/9,784 (95.6%)，预计 1-2 小时内跑完。

---
