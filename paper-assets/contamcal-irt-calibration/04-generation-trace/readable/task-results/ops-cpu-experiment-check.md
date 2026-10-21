# ops cpu experiment check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cpu-experiment-check_20260515T010622_result.json`
- **Structured JSON:** [`e03525e0ae329779a3f2.json`](../../sessions/e0/e03525e0ae329779a3f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况清楚了。汇总如下：

---

## CPU 实验状态汇总

| 实验 | 状态 | PID | 进度 | 输出路径 |
|------|------|-----|------|----------|
| **exp_004_sim_sweep_v4** | **已完成/停止** | 无进程 | 9/120 conditions 完成（sweep_summary 仅含 4 条） | `/root/contamcal-irt-calibration/exp004_sim_sweep/results/` |
| **exp006-oracle-gsm8k-extended** | **已完成** | 无进程 | 100% — 有完整 `exp006_results.json`（37KB） | `/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended/` |
| **exp006-pooled-s1only-arc** | **已完成** | 无进程 | 100% — 有完整 `exp006_results.json`（246KB）+ `joint_fit/` + `arc_challenge/` | `/root/autodl-tmp/exp006/results_pooled_s1only_arc/` |
| **exp006-pooled-s1only-gsm8k** | **已完成** | 无进程（v3_rrf 版） | 100% — `exp006_results.json`（271KB）完成于 06:57 | `/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/` |

## 额外发现：3 个新进程在跑

| 进程 | PID | 启动时间 | 状态 |
|------|-----|----------|------|
| **pooled s1only gsm8k v2** (joint-fit) | 478825 | 09:08 | RUNNING — Stan warmup 中 |
| **oracle gsm8k extended v2** (4chain x 4000 samples) | 478967 | 09:08 | RUNNING — Stan warmup 中 |
| **2pl ablation** (gsm8k+arc+mmlu) | 467504 | 07:57 | RUNNING — mmlu 采样完成(3626s)，可能在做后处理 |

**sim_sweep_v4** 只完成了 9 个 condition（非 57/120），进程已不存在，可能提前终止或结果散落在其他位置。

---
