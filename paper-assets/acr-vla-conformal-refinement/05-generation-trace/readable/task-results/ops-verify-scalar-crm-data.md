# ops verify scalar crm data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-scalar-crm-data_20260518T101620_result.json`
- **Structured JSON:** [`f3252c99c048f9614e7b.json`](../../sessions/f3/f3252c99c048f9614e7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Scalar CRM 实验完整列表（LIBERO Object, norm=0.1）

| Seed | SR | Successes/Total | n_rollouts/task | 来源文件 | 服务器 | 状态 |
|------|-----|----------------|-----------------|----------|--------|------|
| **42** | **9%** | 9/100 | 10 | `eval-acr-object-v4-scalar.log`（无 JSON 输出） | bjb1-32546 | **完整运行, EXIT_CODE=0** |
| 43 | 10% | 10/100 | 10 | `eval_object_scalar_seed43.json` | bjb1-32546 | 完整 |
| 44 | 6% | 6/100 | 10 | `eval_object_scalar_seed44_r2.json` | bjb1-32546 | 完整 |
| 45 | 9% | 18/200 | **20** | `eval_object_scalar_seed45.json` | bjb2-28827 | 完整 |

另有一次 seed42 重试 `eval-acr-object-v4-scalar-b2` 在 bjb2-28827 上因模型加载错误崩溃，无结果。

---

## 关键发现

**1. Seed42 存在且有效。** `eval-acr-object-v4-scalar` 在 bjb1-32546 上完整跑完 10/10 tasks × 10 rollouts = 100 rollouts，SR=9%，EXIT_CODE=0。但它被排除在 `magnitude_curve_data.json` 的 scalar 条目之外（只有 seed 43/44/45）。

**2. 论文数据与 JSON 一致：** `baselines.scalar` = {43: 0.10, 44: 0.06, 45: 0.09}，mean=8.33%, std=2.08%，论文写 8.3±2.1% ✓

**3. 如果加入 seed42：** {42: 0.09, 43: 0.10, 44: 0.06, 45: 0.09} → mean=8.5%, std=1.73%（4 seeds）

**4. seed45 的 n_rollouts 不一致：** seed45 用了 20 rollouts/task（18/200），其他 seed 用 10 rollouts/task。`magnitude_curve_data.json` metadata 写的是 `n_rollouts_per_task: 10`。

**5. seed42 没有 JSON 输出文件**，因为运行时未指定 `--output_file` 参数（对比 seed43/44/45 都指定了）。结果只记录在 log 和 registry 中。

---

## Reviewer 问题的回应选项

seed42 = 9%，是有效数据。论文要么：
- **纳入 seed42**：报告 4 seeds, mean=8.5±1.7%
- **解释排除原因**：需要合理理由（目前 registry conclusion 标记为 "negative" 但数据本身完整有效，没有技术问题）

---
