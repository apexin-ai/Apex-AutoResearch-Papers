# ops eval progress monitor 1h

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-progress-monitor-1h_20260519T133735_result.json`
- **Structured JSON:** [`840272bb481f1024c555.json`](../../sessions/84/840272bb481f1024c555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### exp-004 eval (GPU 0, PID 136205)
- **进程存活**，已运行 ~3 分钟
- 当前在 **checkpoint-500**，进度 **20/362**
- 每 20 样本约 2.5 min → 单 ckpt 约 45 min
- 3 个 ckpt (500, 2000, 8000) → **预计总耗时 ~2.5h**，约 UTC 00:00 完成
- **尚无已完成结果**（刚开始第一个 ckpt）

### exp-016 ActAdd re-eval (GPU 3, PID 126897)
- **进程存活**，已运行 3h 05min
- 5 个 alpha 值，每个跑 362 对，单 alpha 约 60 min：

| Alpha | 状态 |
|-------|------|
| 0.0 | ✅ 完成 (18:33→19:33) |
| 0.5 | ✅ 完成 (19:33→20:33) |
| 1.0 | ✅ 完成 (20:33→21:33) |
| 2.0 | 🔄 进行中 20/362 (21:33 开始) |
| 5.0 | ⏳ 未开始 |

- **预计完成**: ~2h 后，约 UTC 23:30
- **结果目录为空** — 脚本应在全部 alpha 跑完后统一写 json

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 41% | 17.2/31.8 GB (exp-004) |
| 1 | 71% | 30.7/31.8 GB |
| 2 | 68% | 30.0/31.8 GB |
| 3 | 56% | 16.1/31.8 GB (exp-016) |

两个任务都在正常推进。exp-016 3/5 alpha 已完成但中间结果未落盘，需等全部跑完才能收集 json。

---
