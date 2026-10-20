# monitor all exp progress v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all-exp-progress-v2_20260514T145126_result.json`
- **Structured JSON:** [`3073e643a2d9e0dd0736.json`](../../sessions/30/3073e643a2d9e0dd0736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报 (2026-05-14 22:52 CST)

### GPU 状态

| GPU | VRAM Used | Util | 占用 |
|-----|-----------|------|------|
| 0 | 23.7/97.9 GB (24%) | 95% | c2_n500 DS imp |
| 1 | 24.2/97.9 GB (25%) | 98% | c2_n500 DS rand |
| 2 | 48.1/97.9 GB (49%) | 90% | c2_qw imp + c3_llama imp |
| 3 | 50.9/97.9 GB (52%) | 97% | c2_qw rand + c3_llama rand |

---

### 1. c2_n500_deepseek (GPU 0+1, tmux: c2_n500_gpu0)

| 进程 | PID | 状态 | 当前进度 | 条件 | 速率 |
|------|-----|------|----------|------|------|
| GPU 0 imp | 130124 | **alive** | **118/500** on imp_s015 | 1/4 | ~1.65 prob/min |
| GPU 1 rand | 130263 | **alive** | **140/500** on rand_s015 | 1/4 | ~1.96 prob/min |

- 启动时间：21:41 CST
- 队列：s015 → s020 → s025 → s030（每 GPU 4 个条件，顺序执行）
- **预计完成**：
  - GPU 0 (imp 全部)：~May 15 17:50 CST
  - GPU 1 (rand 全部)：~May 15 14:40 CST

---

### 2. c2_qw_n500 (GPU 2+3, SCREEN: c2_qw_gpu2/gpu3)

| 进程 | PID | 状态 | 当前进度 | 条件 | 速率 |
|------|-----|------|----------|------|------|
| GPU 2 imp | 131864 | **alive** | **109/500** on imp_s015 | 1/4 | ~1.84 prob/min |
| GPU 3 rand | 132002 | **alive** | **115/500** on rand_s015 | 1/4 | ~1.95 prob/min |

- 启动时间：21:52 CST
- **重复进程 132389/132392：已清理，不存在**
- 队列：s015 → s020 → s025 → s030
- **预计完成**：
  - GPU 2 (imp 全部)：~May 15 16:00 CST
  - GPU 3 (rand 全部)：~May 15 15:00 CST

---

### 3. c3_llama (GPU 2+3 共享, PID 138393)

| 进程 | PID | 状态 | 当前进度 | 条件 | 速率 |
|------|-----|------|----------|------|------|
| GPU 2 imp | 138408 | **alive** | **12/50** on importance_s015 | 1/4 | ~1.83 prob/min |
| GPU 3 rand | 138410 | **alive** | **13/50** on random_s015 | 1/4 | ~1.62 prob/min |

- 启动时间：22:44 CST
- n=50（不是500），8 条件并行 2 路
- **预计完成**：
  - GPU 2 (imp 4 条件)：~May 15 00:35 CST
  - GPU 3 (rand 4 条件)：~May 15 00:48 CST

---

### 异常检查

- **重复进程**：132389/132392 已清理 ✓
- **OOM 风险**：GPU 2+3 共享两组实验，VRAM 48-51/98 GB，余量充足，无 OOM ✓
- **日志错误**：所有日志无 ERROR/Exception ✓
- **输出目录**：当前运行的 output 目录为空（profiling_results.json 在跑完 500/50 题后才写入）✓

### 总结

6 个进程全部存活，无异常。c3_llama 最先完成（今晚 ~01:00），c2 系列预计明天下午 14:40-17:50 全部跑完。

---
