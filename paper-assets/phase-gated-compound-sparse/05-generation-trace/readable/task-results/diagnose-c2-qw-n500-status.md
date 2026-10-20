# diagnose c2 qw n500 status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c2_qw_n500_status_20260514T192251_result.json`
- **Structured JSON:** [`5b69b987d440e5f48204.json`](../../sessions/5b/5b69b987d440e5f48204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**Cron 误报，实验正常运行中。**

### s015 已完成
| Condition | 结果文件 | 完成时间 | 大小 |
|-----------|---------|---------|------|
| qw_imp_s015 | `profiling_results.json` | May 15 03:02 UTC | 18.7MB |
| qw_rand_s015 | `profiling_results.json` | May 15 03:11 UTC | 18.7MB |

### s020 正在运行
Screen 会话内的脚本在 s015 跑完后自动启动了 s020。原始 PID (131864/132002) 是 s015 的进程，已正常退出。新进程：

| GPU | PID | 任务 | 已运行 | CPU |
|-----|-----|------|--------|-----|
| 0 | 156554 | ds_imp_s020 (DeepSeek) | 53m | 100% |
| 1 | 154305 | ds_rand_s020 (DeepSeek) | 1h19m | 100% |
| 2 | 159269 | **qw_imp_s020** | 22m | 101% |
| 3 | 159794 | **qw_rand_s020** | 13m | 102% |

所有 4 个 GPU 都满载（77-99% GPU util），s020 输出目录已创建但结果尚未写入（profiling 在结束时才写 JSON）。

### Cron 误报原因
Cron 监控的是 s015 的 PID (131864/132002)，s015 正常完成后这些 PID 消失，cron 检测到"process dead"就报 failed。实际上 screen 会话中的脚本已经顺利推进到下一个 sparsity level。

---
