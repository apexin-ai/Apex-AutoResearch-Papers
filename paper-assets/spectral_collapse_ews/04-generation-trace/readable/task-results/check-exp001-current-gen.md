# check exp001 current gen

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp001_current_gen_20260517T041110_result.json`
- **Structured JSON:** [`37d36f7b99da7f2afda4.json`](../../sessions/37/37d36f7b99da7f2afda4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001 状态报告

**状态：仍在运行**，进程 59365 活跃，GPU 0 满载 (100%, 78°C, 65.9GB/97.9GB)。

**当前进度：正在训练 Gen 5**（fine-tuning 阶段，已到 step 2500）。

### 已完成代数 (Gen 0–4) 指标

| Gen | eff_rank | log_det | perplexity | distinct_4 | sigma_1 |
|-----|----------|---------|------------|------------|---------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | 1942.82 |
| 1 | 491.77 | 2464.76 | 11.38 | 0.626 | 803.96 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.515 | 712.03 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.490 | 700.68 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.468 | 729.59 |

**趋势观察：**
- perplexity 稳定上升 (9.5 → 19.8)，distinct_4 持续下降 (0.74 → 0.47) — 符合 model collapse 预期
- eff_rank 在 Gen 1-2 升高后开始回落 (496 → 485)
- sigma_1 在 Gen 0 极高 (1942)，Gen 1 后稳定在 700-800 范围

**预估剩余时间：** 进程已运行约 292 分钟完成了 Gen 4 并正在做 Gen 5 (即约 4h52m 跑了 ~5.5 代)。每代约 53 分钟，还剩 Gen 5(部分)–9，约 **4 小时**完成全部 10 代。

---
