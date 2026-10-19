# ops read buggy eval results

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-buggy-eval-results_20260516T173346_result.json`
- **Structured JSON:** [`fe0fe8cf3035103e4416.json`](../../sessions/fe/fe0fe8cf3035103e4416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Let me provide the summary.

---

## 结果汇总

### 1. Buggy Eval（unconditioned scoring ablation）— **未完成，无 eval_info.json**

| 目录 | 来源 | 状态 |
|------|------|------|
| `/root/autodl-tmp/v7_eval_seed1/` | acib_v7_contrastive ckpt-20000, buggy (无 language conditioning) | **中断** — 只完成 libero_spatial 的 6/10 个 task（每个 10 episodes），未生成 eval_info.json |
| `/root/autodl-tmp/v7_eval_seed2/` | acib_v7_seed2 ckpt-20000, buggy | **中断** — libero_spatial 完成(1 task partial)，libero_object 部分开始 |

monitor_seed1.log 中能看到 buggy eval 的部分 running_success_rate（libero_spatial task 0 约 ~20%，后续 tasks 接近 0%），但**没有任何已完成的 per-suite 聚合数据可用**。

### 2. Fixed Eval（正确 language conditioning）— **正在运行**

| 目录 | PID | 状态 |
|------|-----|------|
| `/root/autodl-tmp/v7_eval_fixed_seed1/` | 104743 | 运行中（4 suites, seed=42），已在 libero_spatial |
| `/root/autodl-tmp/v7_eval_fixed_seed2/` | 111920 | 运行中（4 suites, seed=42），已在 libero_spatial |

日志中每个 episode 都打印 `[EVAL] Using language conditioning, shape=torch.Size([1, 960])`，确认是修复后的版本。

### 3. Baseline 已完成结果

| Suite | baseline_std_v3 (SR) | baseline_plus_v2 (SR) |
|-------|---------------------|----------------------|
| libero_spatial | 66.0% | 81.6% |
| libero_object | 67.8% | 88.8% |
| libero_goal | 76.4% | 87.8% |
| libero_10 | 54.2% | 67.2% |

### 结论

**Buggy eval（unconditioned scoring ablation）数据不可用** — eval 在完成之前被中断，没有生成 eval_info.json。仅有 libero_spatial 的部分 video 输出（6个 task × 10 episodes），但无聚合 SR 数据。如需此 ablation 数据，需重新跑一次 buggy eval。

---
