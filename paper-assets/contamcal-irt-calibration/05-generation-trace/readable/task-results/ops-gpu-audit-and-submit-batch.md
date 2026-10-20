# ops gpu audit and submit batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-and-submit-batch_20260515T032354_result.json`
- **Structured JSON:** [`2ac34ad820f29709f64b.json`](../../sessions/2a/2ac34ad820f29709f64b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 状态

| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| **0** | 8985/24564 MiB | 64% | 477489 | exp_001_eval_3B_d100_v2_aligned (eval, ~2.5h) |
| **1** | 6791→7662 MiB | 0% | 492660 | eval_3B_d000_v2_s123_aligned (刚启动 ~3min) |
| **2** | 6791→9008 MiB | 0% | 492733 | eval_3B_d000_v2_s123_para_aligned (刚启动 ~3min) |
| **3** | 17653 MiB | 9% | 466755 | exp_001_sft_d025_3B_v2 (train, ~3.5h) |
| **4** | ~5000 MiB | 活跃 | 494109 + 493617 | **新提交**: exp_001_eval_05B_d000_s42_v2 + 0.5B-Instruct eval (他方提交) |
| **5** | 17981 MiB | 63% | 471296 | exp_001_sft_3B_d100_s123 (train, ~3.2h) |

额外：PID 481167 (exp006-oracle-gsm8k-extended-v2) 在 CPU 上跑 IRT MCMC，不占 GPU。

### 2. Registry 更新

- **exp_001_eval_05B_d100_aligned_v4**: RUNNING → **DONE (success)**。Metrics: mmlu=0.2334, gsm8k=0.3654, arc=0.2944, humaneval=0.0
- **exp_001_eval_05B_d000_s42**: RUNNING → **DONE (negative)**。进程已 defunct，输出目录被并发进程删除

### 3. 已提交实验

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| exp_001_eval_05B_d000_s42_v2 | cuda:4 | 494109 | RUNNING (mmlu 14%, ~72 it/s) |

### 4. 未提交

- **exp_001_eval_05B_d100_v2** — 无空闲 GPU（GPU 4 被两个进程共享，但还有余量，可以考虑再挤一个 0.5B eval）
- **exp_001_eval_3B_raw_gen** — 需要 3B 模型，显存要求高，没有空闲 GPU

GPU 1/2 上的 eval（~3min 前刚启动）来源不明，不在已知活跃进程列表中。当这些 eval 完成后（预计 2-3h），可以在释放的 GPU 上提交剩余实验。

---
