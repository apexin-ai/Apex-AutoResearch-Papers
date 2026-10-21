# ops gpu diagnostic cuda3 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-diagnostic-cuda3-fix_20260514T221120_result.json`
- **Structured JSON:** [`cc8b0cfe06a4175e5545.json`](../../sessions/cc/cc8b0cfe06a4175e5545.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## GPU 状态总览

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 13645/32607 MiB | 50% | PID 90080 — GRPO training (grpo_ced_lr5e6_r1)，已运行 2h31m |
| cuda:1 | 0/32607 MiB | 0% | **空闲** — PID 96500 已死亡 |
| cuda:2 | 9719/32607 MiB | 66% | PID 101842 — eval lr5e6_r1_ckpt40，已运行 46m |
| cuda:3 | 9713/32607 MiB | 72% | PID 104979 — **SFT baseline eval 正在运行**，已运行 18m |

## PID 存活状态

| PID | 状态 | 任务 |
|-----|------|------|
| 90080 | ALIVE | GRPO training |
| 96500 | **DEAD** | (原 eval lr5e6_r1_ckpt20，已结束) |
| 101842 | ALIVE | eval lr5e6_r1_ckpt40_r2 |
| 104979 | **ALIVE** | SFT baseline eval |
| 103825 | **DEAD** | (已 kill) |
| 103831 | **DEAD** | (已 kill) |

## 输出文件状态

- **sft_baseline_eval_results**: 目录已创建但为空 — eval 仍在进行中（PID 104979，运行 18 分钟，cuda:3 占用 9.7GB，72% 利用率）
- **rp_r2_ckpt20**: 位于 `/root/autodl-tmp/eval_results/grpo_ced_lr5e6_rp/checkpoint-20/` — **目录为空**，`summary.json` 内容为 `{}`。该 eval 被 kill（PID 103825/103831）后未完成，结果不可用

## 结论

- **cuda:3 不空闲**，SFT baseline eval 已在运行中，无需重新启动
- **cuda:1 空闲**，可用于重跑被 kill 的 rp_r2_ckpt20 eval（如果需要的话）
- rp_r2_ckpt20 的结果因进程被 kill 而丢失，需要重跑才能拿到数据

---
