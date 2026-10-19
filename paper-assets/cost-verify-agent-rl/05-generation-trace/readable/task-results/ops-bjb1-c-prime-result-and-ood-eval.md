# ops bjb1 c prime result and ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_c_prime_result_and_ood_eval_20260522T031819_result.json`
- **Structured JSON:** [`fb8b1b247ba9123ae33b.json`](../../sessions/fb/fb8b1b247ba9123ae33b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals are running. Both vLLM engines initialized successfully, models loaded on GPU 0 (~39.6GB) and GPU 1 (~39.6GB).

---

## 报告

### Part 1: exp029_c_prime_resume_mt50_v2 结果

训练已完成 (EXIT_CODE=0)，checkpoint 已保存。

| Metric | Step 5 (val) | Step 6 (train) | Step 7 (train) | Step 7 (val) |
|--------|-------------|----------------|----------------|-------------|
| **success** | 21.875% | 31.25% | 16.41% | **18.75%** |
| **pass@N** | pass@1: 21.875% | pass@8: 68.75% | pass@8: 62.5% | pass@1: 18.75% |
| **response_length** | val: 6892 | train: 4686 | train: 5391 | val: 7020 |
| **response_length (rollout)** | — | 11440 | 13304 | — |
| **val reward mean@32** | 2.1875 | — | — | 1.875 |
| **action_is_valid** | 0.630 | 0.712 | 0.704 | 0.705 |

- Step 6→7：train success 从 31.25% 下降到 16.41%，val 从 21.875%（step 5）下降到 18.75%（step 7）
- Checkpoint 保存在 `global_step_7`（save_freq=5 只在 step 5 触发，但训练结束时也保存了 step 7）
- 训练正常结束，无 crash（wandb teardown 有 BrokenPipeError 但无影响）

### Part 2: OOD Eval 已启动

- **Seed5** (GPU 0, PID 382718): `qwen_seed5_step10_hf` → `ood_eval_seed5.log`
- **Seed6** (GPU 1, PID 383485): `qwen_seed6_step15_hf` → `ood_eval_seed6.log`
- 两个 eval 并行运行，各 134 OOD tasks，max_turn=50, temperature=0.4
- 输出 JSON: `/root/autodl-tmp/tmp/seed5_step10_ood_eval.json` / `seed6_step15_ood_eval.json`

### Part 3: GPU 使用

| GPU | Memory | Utilization |
|-----|--------|-------------|
| cuda:0 | 39605 / 97887 MiB | 31% |
| cuda:1 | 39605 / 97887 MiB | 53% |

---
