# ops check all experiment progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-experiment-progress_20260516T041826_result.json`
- **Structured JSON:** [`80274b61d50d3bfabc9f.json`](../../sessions/80/80274b61d50d3bfabc9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPU 总览

| GPU | 内存占用 | 利用率 | 进程 |
|-----|----------|--------|------|
| cuda:0 | 12696/24564 MiB | 96% | d025 eval + 1.5B signals（双进程） |
| cuda:1 | 8985/24564 MiB | 69% | d000 eval |
| cuda:2 | 8985/24564 MiB | 64% | d005 eval |
| cuda:3 | 8985/24564 MiB | 69% | d100 eval |
| cuda:4 | 7217/24564 MiB | 65% | 3B d100 signals |
| cuda:5 | 2067/24564 MiB | 28% | 0.5B signals |

---

### Eval 实验

**1. exp_001_eval_3B_d000_s42_a32_batch** (cuda:1, PID 676487) — 已运行 2h16m
- Phase 1 (aligned): GSM8K **1000/1319 (76%)**, mmlu 已完成
- Phase 2 (para_aligned): 未开始
- 剩余估计：GSM8K ~40min + arc/humaneval ~15min + Phase 2 ~50min = **~1h45m**

**2. exp_001_eval_3B_d005_s42_a32_batch** (cuda:2, PID 679180) — 已运行 2h02m
- Phase 1 (aligned): GSM8K **884/1319 (67%)**, mmlu 已完成
- Phase 2 (para_aligned): 未开始
- 剩余估计：GSM8K ~58min + arc/humaneval ~15min + Phase 2 ~50min = **~2h**

**3. exp_001_eval_3B_d025_s42_a32_para** (cuda:0, PID 691033) — 已运行 39min
- Para_aligned eval: GSM8K (paraphrased) **223/228 (98%)**
- aligned eval 已在之前完成 ✓
- 剩余：GSM8K ~1min + arc_para + humaneval_para ≈ **~15min** ⚡ 最快完成

**4. exp_001_eval_3B_d100_s42_a32_batch** (cuda:3, PID 687347) — 已运行 1h13m
- Aligned eval only（无 para 阶段）
- 无日志可查，按时间估算：~39% through GSM8K
- 剩余估计：GSM8K ~100min + arc/humaneval ~15min = **~2h**

---

### Signal 实验

**5. exp_002_signals_3B_d100_s123_v9** (cuda:4, PID 689315) — 已运行 54min, signal=s4
- s1_embedding ✓, s2_minkpp ✓
- s4_selfcritique: chunk [4000:5000] **458/500 (92%)**, 已完成 4/15 chunks
- 总进度 s4: **~33%**
- 剩余：~10 chunks × ~10.5min = **~1h45m**

**6. exp_002_signals_05B_s123_v2** (cuda:5, PID 687036) — 已运行 1h14m, signal=all
- s1_embedding ✓, s2_minkpp ✓
- s4_selfcritique: 已完成 **7/15 chunks (47%)**
- 剩余：~8 chunks × ~9min = **~1h10m**

**7. exp_002_signals_15B_s123_batch** (cuda:0, PID 691887) — 已运行 34min, signal=all
- s1_embedding ✓, s2_minkpp ✓, ref_logprobs ✓
- s4_selfcritique: chunk [2000:3000] 进行中, 已完成 **2/15 chunks (13%)**
- 与 d025 eval 共享 cuda:0，d025 完成后速度会提升
- 剩余：~13 chunks × ~12min = **~2.5h** （最慢）

---

### GPU 释放顺序预测

| 预计完成时间 | GPU | 实验 |
|-------------|-----|------|
| **~15min** | cuda:0 (部分释放 9GB) | d025 para eval |
| **~1h10m** | cuda:5 | 0.5B s123 signals |
| **~1h45m** | cuda:1 | d000 eval batch |
| **~1h45m** | cuda:4 | 3B d100 s123 signals |
| **~2h** | cuda:2 | d005 eval batch |
| **~2h** | cuda:3 | d100 eval |
| **~2.5h** | cuda:0 (完全释放) | 1.5B s123 signals |

**注意：** 0.5B signals 的 batch log 显示 EXIT_CODE=127（脚本路径错误），但 PID 687036 仍在正常运行——说明当前进程是手动启动的，不受旧日志影响。

---
