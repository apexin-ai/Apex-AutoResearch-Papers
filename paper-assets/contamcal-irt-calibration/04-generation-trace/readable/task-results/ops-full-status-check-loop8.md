# ops full status check loop8

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check-loop8_20260515T044522_result.json`
- **Structured JSON:** [`6901a3d10ede064a14ae.json`](../../sessions/69/6901a3d10ede064a14ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. GPU 占用

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 21268/24564 MiB (87%) | 99% | PID 477489 (eval_3B_d100_v2_aligned, 8.8G) + PID 498153 (sft_05B_d025_s123_v2, 12.5G) |
| 1 | 8985/24564 MiB (37%) | 63% | PID 492660 (eval_3B_d000_v2_s123_aligned, 9.0G) |
| 2 | 9017/24564 MiB (37%) | 62% | PID 499610 (eval_3B_d025_v2_para_aligned, 9.0G) |
| **3** | **0/24564 MiB (0%)** | **0%** | **IDLE** |
| 4 | 7254/24564 MiB (30%) | 32% | PID 493617 (instruct_05B_eval, 3.6G) + PID 494109 (eval_05B_d000_s42_v7, 3.7G) |
| 5 | 17981/24564 MiB (73%) | 25% | PID 471296 (sft_3B_d100_s123, 18.0G) |

### 2. Eval 进程

| 实验 | PID | GPU | 状态 | 结果 |
|------|-----|-----|------|------|
| eval_3B_d100_v2_aligned_v2 | 477489 | 0 | ALIVE | 无结果（运行中） |
| exp_008_instruct_05B_eval | 493617 | 4 | ALIVE | 无结果（运行中） |
| eval_05B_d000_s42_v7 | 494109 | 4 | ALIVE | 无结果（运行中） |
| eval_3B_d000_v2_s123_aligned | 492660 | 1 | ALIVE | 无结果（运行中） |
| eval_3B_d025_v2_para_aligned | 499610 | 2 | ALIVE | 无结果（运行中） |

所有 eval 结果目录尚未生成，无 `.done` sentinel 文件。

### 3. SFT 进度

| 实验 | PID | GPU | 进度 | ETA | 备注 |
|------|-----|-----|------|-----|------|
| sft_05B_d025_s123_v2 | 498153 | **0** (非 3) | 1488/3384 (**44%**) | ~1h | ⚠️ 在 GPU 0 而非预期的 GPU 3，loss=1.51 |
| sft_3B_d100_s123 | 471296 | 5 | 3745/4159 (**90%**) | ~33min | loss=1.14，接近完成 |

### 4. IRT 实验 (CPU)

| 实验 | PID | 状态 | 结果 |
|------|-----|------|------|
| oracle-arc-2pl | 496697 | **DEAD** | **完成** — gamma=-0.618 (CI excludes 0 ✅), MAE=0.076, coverage_95=18.2% (极低), tau=0.739 |
| s1only-gsm8k-2pl | 496852 | ALIVE | 已有结果 — gamma=0.167 (CI **不** excludes 0 ❌ [-0.31, 0.64]), MAE=0.013, coverage_95=100%, tau=0.756 |
| oracle-arc-4pl-pooled | — | 进行中 | 目录 `arc_challenge/` 已创建但**空**，尚无输出 |

**IRT 对比 baselines (evaluation.json):**

| | IRT 2PL gamma | B0_raw | B6_dcr_fuzzy |
|--|---|---|---|
| **ARC oracle** MAE | 0.0759 | 0.0685 | 0.2631 |
| **ARC oracle** coverage_95 | 18.2% | 54.5% | 27.3% |
| **GSM8K s1only** MAE | 0.0131 | 0.0031 | 0.1793 |
| **GSM8K s1only** coverage_95 | 100% | 100% | 50% |

### 5. 本地进程

| 实验 | PID | 状态 |
|------|-----|------|
| exp_004_sim_sweep_v5 | 652931 | ALIVE |

### 6. 空闲 GPU

**GPU 3 完全空闲可用。** GPU 4 还有约 17G 余量。其余均在使用中。

### 注意

- sft_05B_d025_s123_v2 跑在 GPU 0 上，和 eval 进程共享，GPU 0 利用率 99%、显存 87%。
- ARC oracle-2pl 的 coverage_95 仅 18.2%，说明不确定性区间过窄。GSM8K s1only-2pl 的 gamma CI 包含 0，检测不到显著污染效应。

---
