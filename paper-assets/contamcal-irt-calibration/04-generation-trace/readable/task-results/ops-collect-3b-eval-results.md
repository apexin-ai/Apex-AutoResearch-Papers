# ops collect 3b eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-3b-eval-results_20260515T090357_result.json`
- **Structured JSON:** [`43098cea347020578c79.json`](../../sessions/43/43098cea347020578c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: 3 个 3B Eval 实验指标

| Benchmark | d025_v2 (s42) | d100_v2_s123 | d000_v2_s123 |
|-----------|--------------|--------------|--------------|
| **MMLU** | 0.5998 (8422/14042) | **0.6319** (8873/14042) | 0.6314 (8866/14042) |
| **GSM8K** | 0.6793 (896/1319) | **0.7324** (966/1319) | 0.2676 (353/1319) |
| **ARC-C** | 0.8276 (970/1172) | **0.8311** (974/1172) | 0.8259 (968/1172) |
| **HumanEval** | 9.8% (16/164) | **18.3%** (30/164) | 6.1% (10/164) |

**.done sentinel 状态:**
- d025_v2_aligned: **.done 存在** (May 15 16:38)
- d100_v2_s123_aligned: **.done 存在** (May 15 16:58)
- d000_v2_s123_aligned: **无 .done 文件**

### Part 2: .done sentinel 逻辑

`evaluate.py:636` — `(output_dir / ".done").touch()`，在所有 benchmark 评估完成后写入。d000_v2_s123 缺 .done，但 eval_results.json 内容完整（4 个 benchmark 全有），可能是写 sentinel 前崩溃或被中断。

### Part 3: Zombie Stan 进程

**PID 452348 仍然存活** — `run_exp006.py --benchmark gsm8k ... --output-dir .../results_pooled_05B_15B_gsm8k_v3_rrf`，状态 S（sleeping）。

**4 个 zombie 子进程**（均为 `contam_irt_4pl_` &lt;defunct>）：
- PID 452486, 452489, 452490, 452491
- 自 06:42 起运行，累计 CPU 时间 ~5h，现在是 defunct 状态
- 父进程就是 PID 452348，父进程未回收子进程导致 zombie

**活跃 Stan 进程**（非 zombie，正常运行中）：
- exp004_sim_sweep: 3 个 `contam_irt_4pl_sweep` 采样进程 (PIDs 532941, 534482, 534493, 535049)
- 2pl_joint: 1 个 `contam_irt_2pl_gamma` 采样进程 (PID 534278)

---
