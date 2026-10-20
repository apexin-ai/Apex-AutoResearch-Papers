# exp006 fisher heatmap w4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp006_fisher-heatmap-w4_20260516T195342_result.json`
- **Structured JSON:** [`4cfc3a1744365c842813.json`](../../sessions/4c/4cfc3a1744365c842813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正在跑 arc_N5。整个流程按顺序执行 18 个 conditions。基于第一个 condition 的 timing (189s)，总时间估算：

- N=5: ~3 min × 3 benchmarks = 9 min
- N=10: ~5 min × 3 = 15 min
- N=16: ~8 min × 3 = 24 min
- N=24: ~12 min × 3 = 36 min
- N=30: ~15 min × 3 = 45 min
- N=50: ~25 min × 3 = 75 min

**总计约 3-3.5 小时**。

汇报：

| 项目 | 详情 |
|------|------|
| **PID** | 844715 |
| **脚本** | `/root/contamcal-irt-calibration/exp006/run_fisher_heatmap.py` |
| **Stan 模型** | `contam_irt_2pl_gamma.stan` (2PL+γ) |
| **参数** | N∈{5,10,16,24,30,50} × 3 benchmarks × 200 reps = 3600 fits |
| **并行** | 8 workers (ProcessPoolExecutor) |
| **MCMC** | 2 chains × 300 warmup + 300 sampling |
| **输出目录** | `/root/autodl-tmp/exp006/fisher_info_heatmap/` |
| **日志** | `/root/autodl-tmp/logs/fisher_heatmap_w4.log` |
| **预计完成** | ~3-3.5h (约 UTC 07:00-07:30) |

**第一个完成的结果** (mmlu_N5): CI_width=0.2436, power=1.0, coverage=0.89, γ_bias=+0.03, 0 failures/200 reps。

---
