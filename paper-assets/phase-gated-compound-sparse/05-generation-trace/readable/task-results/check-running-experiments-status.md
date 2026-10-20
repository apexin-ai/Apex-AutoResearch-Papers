# check running experiments status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running-experiments-status_20260514T072124_result.json`
- **Structured JSON:** [`e1799a17ac046e54ab8e.json`](../../sessions/e1/e1799a17ac046e54ab8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 分配

| GPU | 显存使用 | 利用率 | 运行进程 |
|-----|---------|--------|---------|
| 0 | 25.1/96 GB | 98% | bf16_qw_imp_**s015** (PID 92198) |
| 1 | 39.3/96 GB | 62% | bf16_qw_imp_**s020** (PID 92337) + **c4_entropy** (PID 93190) |
| 2 | 22.5/96 GB | 70% | bf16_qw_imp_**s025** (PID 92479) |
| 3 | 22.5/96 GB | 60% | bf16_qw_imp_**s030** (PID 92619) |

### bf16 Qwen Importance 实验（4个，全部 ALIVE）

| 实验 | 进度 | 最后日志时间 | 预计剩余 |
|------|------|------------|---------|
| s015 | **15/50** | 15:21 | ~15-20 min |
| s020 | **14/50** | 15:22 | ~15-20 min |
| s025 | **15/50** | 15:21 | ~15-20 min |
| s030 | **15/50** | 15:22 | ~15-20 min |

输出目录目前只有 train.log，尚未生成 profiling_results.json（正常，需跑完 50 题才输出）。

### bf16_ds_rand_s030 — COMPLETED

完成时间：15:12 UTC+8（07:12 UTC）。结果文件 1.9MB。

**Interaction Index (sparsity=0.30, random masking, DeepSeek-R1-Distill-Qwen-7B)**:

| Phase | Mean | Median | CI_low | CI_high | Winsorized Mean | Skewness |
|-------|------|--------|--------|---------|----------------|----------|
| high_sparsity | **9.24** | 4.02 | 2.51 | 15.07 | 11.71 | -5.76 |
| mid_sparsity | **-230.76** | 2.43 | -659.62 | -3.94 | 6.51 | -13.08 |
| low_sparsity | **-7.41** | 4.74 | -41.63 | 15.06 | 9.96 | -14.60 |

**Pass/Fail: PASS**
- CI overlap test: pass（high vs mid CI 不重叠）
- Sign reversal test: pass（high II>0, mid II<0）

### c4_entropy — ALIVE

进度：**5/30** problems（15:22 仍在运行）。在 GPU 1 上与 s020 共享。每个 problem 耗时差异很大（68s ~ 200s），预计还需 ~30-40 min。

### 异常/需关注

1. **3 个残留模型下载进程**仍在运行：
   - PID 58322: `huggingface-cli download Qwen2.5-7B-Instruct`（11:26 启动，已运行 ~4h）
   - PID 89564/89650: 两个 ModelScope 下载（15:07 启动）
   
   这些看起来是之前环境搭建时的残留。模型检查点已经在 `/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct` 且实验正常使用，建议清理这 3 个下载进程释放 CPU/网络。

2. **GPU 1 跑了两个实验**（s020 + c4_entropy），显存占用 39.3GB，利用率相对较低(62%)。两个实验互相争抢可能导致速度下降，但 96GB 显存足够，暂无 OOM 风险。

---
