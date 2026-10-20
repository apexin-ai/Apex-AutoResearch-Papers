# infra server health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server-health-check_20260515T034446_result.json`
- **Structured JSON:** [`e7c750c8b9625513ab7b.json`](../../sessions/e7/e7c750c8b9625513ab7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### GPU 概览

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 70% | 8,985 / 24,564 MiB | eval (3B d100 aligned) |
| 1 | 68% | 8,985 / 24,564 MiB | eval (3B d000 s123 aligned) |
| 2 | 65% | 9,017 / 24,564 MiB | eval (3B d000 s123 para_aligned) |
| 3 | 28% | 17,653 / 24,564 MiB | SFT (3B d025 v2) |
| 4 | 96% | 7,252 / 24,564 MiB | eval x2 (Instruct 0.5B + 0.5B d000 s42) |
| 5 | 28% | 17,981 / 24,564 MiB | SFT (3B d100 s123) |

### 逐实验状态

#### 1. PID 466755 — SFT 3B d025 v2 (cuda:3) ✅ ALIVE
- **进度**: 3237 / 3384 (**95.7%**), epoch 0.93
- **Loss**: ~1.12–1.18, token accuracy ~0.74
- **运行时间**: 3h50m
- **ETA**: ~13 min

#### 2. PID 471296 — SFT 3B d100 s123 (cuda:5) ✅ ALIVE
- **进度**: 2961 / 4159 (**71.2%**), epoch 0.67
- **Loss**: ~1.12–1.18, token accuracy ~0.73
- **运行时间**: 3h32m
- **ETA**: ~1h 45min
- ⚠️ 命令行 `--gpu 0`，但实际跑在 GPU 5（CUDA_VISIBLE_DEVICES 生效）

#### 3. PID 477489 — eval 3B d100 aligned (cuda:0) ✅ ALIVE
- **运行时间**: 2h43m, CPU 93.6%
- **已完成 benchmark**: 0 / 4（输出目录空）
- 目录创建于 09:01，仍在跑第一个 benchmark

#### 4. PID 492660 — eval 3B d000 s123 aligned (cuda:1) ✅ ALIVE
- **运行时间**: 23min, CPU 53%
- **已完成 benchmark**: 0 / 4（输出目录空）

#### 5. PID 492733 — eval 3B d000 s123 para_aligned (cuda:2) ✅ ALIVE
- **运行时间**: 23min, CPU 79.9%
- **已完成 benchmark**: 0 / 4（输出目录空）

#### 6. PID 493617 — Instruct 0.5B eval (cuda:4) ✅ ALIVE
- **运行时间**: 19min, CPU 44.8%
- **已完成 benchmark**: 0 / 4（输出目录空）

#### 7. PID 494109 — 0.5B d000 s42 eval v7 (cuda:4) ✅ ALIVE
- **运行时间**: 17min, CPU 103%
- **已完成 benchmark**: 0 / 4（输出目录空）
- ⚠️ 与 PID 493617 共享 GPU 4（当前 96% 利用率，显存 7.2GB 尚可）

### 总结

- **7/7 进程全部存活**，无异常
- SFT d025 v2 即将完成（~13min），d100 s123 还需 ~1h45m
- 5 个 eval 任务均在运行中，尚无 benchmark 完成输出（d100 aligned 已跑 2h43m 仍无输出，3B 模型 eval 较慢属正常）
- GPU 4 上两个 0.5B eval 共存，利用率 96%，暂未 OOM 但需关注

---
