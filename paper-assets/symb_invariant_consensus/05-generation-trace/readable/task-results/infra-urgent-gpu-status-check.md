# infra urgent gpu status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-gpu-status-check_20260522T131538_result.json`
- **Structured JSON:** [`16a9a9e094439316cf24.json`](../../sessions/16/16a9a9e094439316cf24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告 — westd-16639 @ 2026-05-22 21:16 UTC

### GPU 总览

| GPU | 型号 | 利用率 | 显存 | 运行进程 |
|-----|------|--------|------|---------|
| 0 | RTX PRO 6000 Black | 97% | 90159/97887 MiB | vLLM Qwen2.5-14B (PID 551459) |
| 1 | RTX PRO 6000 Black | 96% | 88263/97887 MiB | vLLM LLaMA-3.1-8B (PID 595559) |
| 2 | RTX PRO 6000 Black | 96% | 90213/97887 MiB | vLLM Mistral-7B (PID 510289) |
| **3** | RTX PRO 6000 Black | **0%** | **0 MiB** | **空闲** |

### 实验进度

#### cuda:0 — Qwen2.5-14B PW (master PID 552333, alive 5h42m)

| Seed | 进度 | 状态 | 结果 |
|------|------|------|------|
| 123 | **303/600** | **运行中** | SICA=73.6%, SC=72.9%（中间结果） |
| 456 | 600/600 | 旧结果（异常） | SICA=0.0%, SC=0.0%, extraction_rate=0.0 |
| 789 | 600/600 | 旧结果（异常） | SICA=0.0%, SC=0.0%, extraction_rate=0.0 |

> seed456/789 的 results.json 是之前失败的 run_full_mvp.py 运行留下的（0% accuracy、0 extraction）。当前多种子脚本还在跑 seed123，这两个 seed 尚未被当前轮次覆盖。

#### cuda:1 — LLaMA-3.1-8B FOLIO (master PID 596151, alive 2h09m)

| Seed | 进度 | 状态 | 结果 |
|------|------|------|------|
| 123 | 204/204 | **完成** | **SICA=63.73%, SC=67.16%**, extraction_rate=95.9%, contradiction_rate=4.9% |
| 456 | **12/204** | **运行中** | ETA ~164 min (~2.7h) |
| 789 | — | 未开始 | 目录不存在 |

#### cuda:2 — Mistral-7B PW (master PID 510987, alive 9h45m)

| Seed | 进度 | 状态 | 结果 |
|------|------|------|------|
| 42 | 600/600 | **完成** | **SICA=36.67%, SC=40.0%**, abstention(t=0.5): coverage=25.8%, acc_retained=47.1% |
| 123 | **586/600** | **运行中** | SICA=37.88%, SC=41.13% (586个问题的中间结果), ETA ~7 min |
| 456 | — | 未开始 | 目录不存在 |
| 789 | — | 未开始 | 目录不存在 |

### 其他进程

- **PID 605169**: ModelScope 下载 Qwen2.5-7B-Instruct → `/root/autodl-tmp/models/Qwen2.5-7B-Instruct`（started 20:12）

### 空闲卡

**GPU 3** 完全空闲（0% utilization, 0 MiB）。

---
