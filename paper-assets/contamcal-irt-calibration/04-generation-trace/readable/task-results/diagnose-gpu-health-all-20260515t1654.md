# diagnose gpu health all 20260515T1654

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_health_all_20260515T1654_20260515T165450_result.json`
- **Structured JSON:** [`a10903bd85fd7968d182.json`](../../sessions/a1/a10903bd85fd7968d182.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_health_20260515T1654.md`。

**汇总**：

| GPU | 进程 | 状态 | 进度 | 预估剩余 |
|-----|------|------|------|----------|
| 0 | sft_d100_s123_v2 | ✅ | 311/4159 (7.5%) | ~4h17m |
| 1 | sft_d100_s42_v2 | ✅ | 361/4159 (8.7%) | ~4h13m |
| 2 | eval_d005_aligned | ✅ | GSM8K 766/1319 (58%) | ~1h13m + arc + humaneval |
| 3 | eval_d025_aligned | ✅ | GSM8K 941/1319 (71%) | ~46m + arc + humaneval |
| 4 | sft_d000_v3 | ⚠️ **冲突** | 40/3125 (1.3%) | ~4h01m |
| 5 | sft_d025_v3 | ✅ (无日志) | 42m elapsed | 未知 |

**需要处理**：
1. **GPU 4 冲突**：PID 590509（compute_signals.py, exp002）占 9658 MiB，与 sft_d000_v3 共享 GPU 4，总 VRAM 95.7%，温度 66°C。需要决定 kill 哪个——compute_signals 已跑 41m 可能接近完成，sft_d000_v3 才 1.3%。
2. **exp_001_sft_d025_3B_v3 无日志**：进程直接在 tmux 中启动，未通过 wrapper 重定向。进程本身正常运行（Rl+ 状态，VRAM 17640 MiB）。

---
