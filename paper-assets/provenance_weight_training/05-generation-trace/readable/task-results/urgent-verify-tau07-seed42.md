# urgent verify tau07 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_verify_tau07_seed42_20260522T172332_result.json`
- **Structured JSON:** [`55f9a48402ac9721dcf8.json`](../../sessions/55/55f9a48402ac9721dcf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部证据已收集。结论如下：

---

## 1. tau07_seed42 的 n_min 实际值

**n_min = 2**

- 训练命令（registry）未显式传 `--n_min`，参数为 `null`
- 脚本默认逻辑：`n_min = max(2, batch_size // 2)`
- batch_size = 4 → `max(2, 4 // 2) = max(2, 2) = 2`
- config.json 确认记录值：`"n_min": 2`
- step_metrics 中 ess 最低约 2.0（如 `2.0147`, `2.001`），与 n_min=2 一致

## 2. tau07_seed42 是 from-scratch 还是 resume？

**From-scratch，非 resume。** 证据：

1. Registry 命令：`WANDB_MODE=disabled python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --seed 42` — **无 `--resume_from_checkpoint`**
2. 输出目录无 checkpoint 子目录（只有 `config.json, eval_results.json, final/, ood_results.json, step_metrics.jsonl`）
3. step_metrics 从 step 0 开始，loss 初始值 ~3.75（典型随机初始化水平）
4. Registry 中所有 12 个匹配实验**均无** `--resume_from_checkpoint`

## 3. seed123/456 的 adaptive 实验是否 from-scratch？

**是，全部 from-scratch。** 证据：

| 实验 | config n_min | batch_size | tau | step_metrics 从 step 0 开始 | 初始 loss | resume 参数 |
|------|-------------|-----------|-----|---------------------------|----------|------------|
| tau07_seed42 | 2 | 4 | 0.7 | Yes | 3.75 | 无 |
| tau07_seed123 | 2 | 4 | 0.7 | Yes | 1.03 | 无 |
| tau07_seed456 | 2 | 4 | 0.7 | Yes | 2.73 | 无 |

三个 seed 的 config 完全一致（除 seed 值），均从 step 0 开始，无 resume 痕迹。

---
