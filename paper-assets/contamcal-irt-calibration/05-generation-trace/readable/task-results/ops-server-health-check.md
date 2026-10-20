# ops server health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-health-check_20260514T030526_result.json`
- **Structured JSON:** [`2a08f6e98bd2d0a2c527.json`](../../sessions/2a/2a08f6e98bd2d0a2c527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 显存 | 利用率 | PID | 实验 | 当前进度 |
|-----|------|--------|-----|------|----------|
| 0 | 10055/24564 MiB | 23% | 251924 | 1.5B d100 SFT | step 2028/4159 (49%) |
| 1 | 12620/24564 MiB | 100% | 249294 | 3B d000 s42 eval | GSM8K 909/1319 (69%) |
| 1 | ↑共享 | ↑ | 255322 | 0.5B d005 eval | GSM8K 240/1319 (18%) |
| 2 | 7330/24564 MiB | 99% | 266511 | 0.5B d000 s42 eval | GSM8K 240/1319 (18%) |
| 2 | ↑共享 | ↑ | 266780 | 0.5B d100 eval | GSM8K 240/1319 (18%) |
| 3 | 8957/24564 MiB | 62% | 242581 | 3B d000 s123 eval | HumanEval 146/164 (89%) |
| 4 | 10365/24564 MiB | 48% | 243290 | 1.5B d000 s42 eval | GSM8K 1185/1319 (90%) |
| 5 | 5829/24564 MiB | 45% | 250600 | 1.5B d000 s123 eval | GSM8K 726/1319 (55%) |

**全部 8 个 GPU 进程存活。**

## SFT 进度

| 实验 | 当前step/总step | loss | speed | ETA |
|------|----------------|------|-------|-----|
| 1.5B d100 s42 (GPU 0) | 2028/4159 (49%) | ~1.29 | 3.8s/it | ~2h15m |

## Eval 完成情况

| 实验 | MMLU | GSM8K | ARC | HumanEval | 预估剩余 |
|------|------|-------|-----|-----------|----------|
| 3B d000 s42 (GPU 1) | ✅ | 69% | - | - | ~1.5h |
| 3B d000 s123 (GPU 3) | ✅ | ✅ | ✅ | 89% | **~2min** |
| 1.5B d000 s42 (GPU 4) | ✅ | 90% | - | - | ~40min |
| 1.5B d000 s123 (GPU 5) | ✅ | 55% | - | - | ~1.5h |
| 0.5B d005 (GPU 1) | ✅ | 18% | - | - | ~2.5h |
| 0.5B d000 s42 (GPU 2) | ✅ | 18% | - | - | ~2.5h |
| 0.5B d100 (GPU 2) | ✅ | 18% | - | - | ~2.5h |

Benchmark 执行顺序: MMLU → GSM8K → ARC → HumanEval。GPU 1、2 各跑 2 个 eval，存在资源争抢，速度偏慢。

## CPU 进程

| 实验 | 状态 | 说明 |
|------|------|------|
| exp_004_sim_sweep (PID 219346) | **DEAD** | 进程不存在，`/root/contamcal-irt-calibration/exp004/` 目录也不存在 |

## 磁盘

| 分区 | 已用/总量 | 使用率 |
|------|----------|--------|
| 根分区 (/) | 17G/30G | 55% |
| 数据盘 (/root/autodl-tmp) | 104G/169G | 62% |
| - checkpoints | 2.3G | |
| - eval_results | 3.0M | |
| - hf_cache | 56G | |

**3B s123 eval 即将完成（~2min）；1.5B s42 eval 约 40min 后完成。其余 eval 和 SFT 还需 1.5-2.5h。exp004 进程已死，目录不存在。**

---
