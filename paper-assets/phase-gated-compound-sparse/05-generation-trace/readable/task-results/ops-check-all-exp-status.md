# ops check all exp status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-exp-status_20260514T024814_result.json`
- **Structured JSON:** [`90b7953b1a1ac449d92d.json`](../../sessions/90/90b7953b1a1ac449d92d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

**4 个实验全部在运行中，无一完成。**

| 实验 | GPU | PID | 运行时间 | 进度 | GPU 显存 | GPU 利用率 |
|------|-----|-----|----------|------|----------|-----------|
| mvp_v5_fixed_s020_r2 | cuda:0 | 51024 | 36min | **48/50** | 38905 MiB | 99% |
| mvp_v5_fixed_s030_r2 | cuda:1 | 51161 | 36min | **48/50** | 38905 MiB | 97% |
| mvp_v5_random_s015 | cuda:2 | 51961 | 29min | **40/50** | 31961 MiB | 99% |
| mvp_v5_random_s025 | cuda:3 | 52103 | 29min | **41/50** | 31961 MiB | 99% |

**关键信息：**
- 所有进程状态均为 `Rl`（Running），正常执行中
- 4 个输出目录均为空，尚无 `profiling_results.json`
- fixed 组 (s020/s030) 进度接近完成（48/50），预计几分钟内跑完
- random 组 (s015/s025) 稍慢（40-41/50），GPU 显存占用较少（31.9G vs 38.9G）
- 所有实验均有 layer 27 的 NaN attention warning，非致命

---
