# analysis exp004 sim sweep status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004-sim-sweep-status_20260515T135451_result.json`
- **Structured JSON:** [`2cc639006b06dd63360e.json`](../../sessions/2c/2cc639006b06dd63360e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| 项目 | 状态 |
|------|------|
| **进程** | 存活，PID 528993，已运行 5h20m，RSS 214MB，CPU 0.3% |
| **总任务** | 8 conditions × 10 seeds = 80 runs（gamma{2.0,4.0} × AUC{0.7,0.9} × N{20,50}） |
| **已完成** | 4/8 conditions（全部 gamma=2.0），结果已写入 `results_extreme_gamma/` |
| **当前** | 第 5 condition（gamma=4.0），seed 8/10（chain 4/4 采样中） |
| **进度** | ~47/80 seeds ≈ **59%** |
| **每 seed 耗时** | N=20 ~300s, N=50 ~700s |
| **预计剩余** | ~32 seeds，混合 N=20/N=50，约 **4-5 小时** |
| **Registry** | **不一致** — 实验不在 registry 中（RUNNING 列表无此条目，按 name 查也无结果） |

**需要修正**：Registry 缺少 exp_004_sim_sweep_extreme_gamma 记录。要现在注册补录吗？

---
