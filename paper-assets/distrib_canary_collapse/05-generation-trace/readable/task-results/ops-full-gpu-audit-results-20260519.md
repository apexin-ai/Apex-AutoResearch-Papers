# ops full gpu audit results 20260519

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_audit_results_20260519_20260519T121643_result.json`
- **Structured JSON:** [`243270be2ae10903e880.json`](../../sessions/24/243270be2ae10903e880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态（nvidia-smi 实际）

| GPU | 内存 | 利用率 | 进程 | 状态 |
|-----|------|--------|------|------|
| cuda:0 | 0 / 97887 MiB | 0% | PID 109870 DEAD | **空闲** |
| cuda:1 | 34801 / 97887 MiB | 59% | PID 74455 ALIVE (11h47m) | qwen35_v2 运行中 |
| cuda:2 | 14503 / 97887 MiB | 66% | PID 122877 ALIVE (2h12m) | padding_robustness 7/10 gens |
| cuda:3 | 14237 / 97887 MiB | 94% | PID 123809 ALIVE (2h10m) | a025_s43_fp32 6/10 gens |
| cuda:4 | 14487 / 97887 MiB | 89% | PID 124519 ALIVE (2h09m) | a025_s44_fp32 6/10 gens |
| cuda:5 | 14503 / 97887 MiB | 62% | PID 121667 ALIVE (2h18m) | a075_s42_fp32 7 gen dirs |

## 完成实验结果

**a025_s42_fp32** — 已完成 (11 gens, EXIT_CODE=0)

| 指标 | gen0 | gen10 | drift |
|------|------|-------|-------|
| token_entropy | 3.2342 | 3.0794 | **-4.8%** |
| distinct_1 | 0.0980 | 0.0596 | **-39.1%** |
| perplexity | 26.95 | 22.07 | -18.1% |
| ece | 0.0108 | 0.0194 | +79.2% |
| mauve | 0.0311 | 0.0181 | -41.9% |
| effective_rank | 46.61 | 44.85 | -3.8% |
| analysis_results | — | — | **NOT FOUND (lead-lag 未跑)** |

**a075_s42_fp32** — 仍在运行，interim 数据 (4/10+ gens in all_metrics)

| 指标 | gen0 | gen3 | drift |
|------|------|------|-------|
| token_entropy | 3.2342 | 2.0913 | **-35.3%** |
| distinct_1 | 0.0980 | 0.0779 | -20.5% |
| perplexity | 26.95 | 50.53 | **+87.5%** |
| ece | 0.0108 | 0.1883 | **+1642.5%** |
| mauve | 0.0311 | 0.0315 | +1.3% |
| effective_rank | 46.61 | 81.14 | +74.1% |
| analysis_results | EXISTS 但 n=4 | 所有 lead-lag "T=3 too short" | 无效，需完成后重跑 |

其余 3 个实验（a025_s43, a025_s44, padding_robustness）均在训练中，无 all_metrics.json。qwen35_v2 已跑 ~12h。

## 空闲 GPU

**cuda:0** — 可立即填充（a025_s42_fp32 已完成释放）

## 待办

1. a025_s42_fp32 需要跑 lead-lag analysis（analysis_results.json 缺失）
2. a075_s42_fp32 的 analysis_results 基于仅 4 gens 无统计效力，完成后需重跑
3. 其余实验预计 ~2-4h 内陆续完成（当前进度 6-7/10 gens）

---
