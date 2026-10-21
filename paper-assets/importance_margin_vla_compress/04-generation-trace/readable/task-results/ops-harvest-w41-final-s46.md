# ops harvest w41 final s46

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-w41-final-s46_20260528T113728_result.json`
- **Structured JSON:** [`3ea0ac7f06826921ea2a.json`](../../sessions/3e/3ea0ac7f06826921ea2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 任务 1: Random k=0.95 seed46 ✅ 已收割

**SR = 60.8%** (304/500)

| Task | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| SR | 52% | 86% | 76% | 88% | 48% | 80% | 8% | 64% | 24% | 82% |

**5-seed 统计**: s42=60.6%, s43=60.8%, s44=61.2%, s45=62.4%, s46=60.8%
- **Mean = 61.16% ± 0.73pp** (sample std)
- s46 在范围内，无异常。Registry 已更新为 DONE/success。

### 任务 2: L2norm k=0.7 配置调查 — **无配置错误**

- pid 923767 的命令行确认 `--keep_ratio 0.7` ✓
- 日志首行确认 `Config: suite=libero_10, prune=l2norm, keep=0.7` ✓
- `pi05_l2norm_k0.75_libero_10_seed46.json` 是一个**独立的 k=0.75 s46 实验**（13:53-16:15完成，SR=73.2%），与 k=0.7 实验无关
- k=0.7 s46 当前进度：**T8 ep=30/50**（总进度 ~86%），约 30 min 后完成
- 运行中 partial: 258/400=64.5% (T0-T7)，T8 暂 2/30=7%

### 任务 3: Random k=0.5 seed46 — 即将完成

- 进度: **T9 ep=30/50**（最后一个 task，约 6 min 后完成）
- Running totals: 225/450=50.0% (T0-T8)
- Per-task: T0=82%, T1=38%, T2=58%, T3=82%, T4=44%, T5=40%, T6=36%, T7=52%, T8=18%
- T9 当前 18/30=60%

两个实验（L2norm k=0.7 和 Random k=0.5）都在 w41 上正常推进，预计 ~30-40 min 内全部完成。

---
