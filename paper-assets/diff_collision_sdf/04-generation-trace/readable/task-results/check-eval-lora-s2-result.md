# check eval lora s2 result

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_lora_s2_result_20260527T160747_result.json`
- **Structured JSON:** [`962de4b8434102592741.json`](../../sessions/96/962de4b8434102592741.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

## 总结

**eval_lora_s2_30k_v2 已完成**，结果文件: `/root/autodl-tmp/eval_results/eval_safelibero_object_all_levelII_30000_lora_baseline_seed7.json`

### 3-seed LoRA null distribution (Claim 3 统计基础)

| | s0 | s1 | s2 | **Mean ± Std** |
|---|---|---|---|---|
| **CAR** | 57.0% | 52.5% | 55.0% | **54.83 ± 2.26%** |
| **TSR** | — | — | 51.5% | — |

Per-task CAR 方差较大（s2 从 task3 bbq_sauce 的 26% 到 task1 chocolate_pudding 的 76%），但 overall CAR 三个 seed 一致性很好（range 仅 4.5pp，std 2.26%）。

**对 Claim 3 的意义**: SDF-augmented model 的 CAR 需要显著超过 54.83% 才能 reject null。以 one-sided t-test (df=2, α=0.05) 计算，临界值约 54.83 + 2.26 × 2.92 ≈ **61.4%**。

另外注意：westd-45947 上当前跑着的 GPU 进程（PID 425058）是 `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 2 --lambda_sdf 0.1 --gpu 1`，已运行 25h+，不是 eval。

---
