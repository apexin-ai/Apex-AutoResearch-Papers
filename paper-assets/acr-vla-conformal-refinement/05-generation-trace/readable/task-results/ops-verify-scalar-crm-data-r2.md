# ops verify scalar crm data r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-scalar-crm-data-r2_20260518T102505_result.json`
- **Structured JSON:** [`2a665a0e749c2351037b.json`](../../sessions/2a/2a665a0e749c2351037b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是验证结果。

## Scalar CRM 数据验证结果

### 找到的 JSON 文件

| 文件路径 | 服务器 | seed | SR | norm | n_rollouts |
|----------|--------|------|----|------|------------|
| `logs/eval_object_scalar_seed43.json` | bjb1-32546 | 43 | **10%** | 0.1 | 10 |
| `logs/eval_object_scalar_seed44_r2.json` | bjb1-32546 | 44 | **6%** | 0.1 | 10 |
| `logs/eval_object_scalar_seed45.json` | bjb2-28827 | 45 | **9%** | 0.1 | **20** |
| *(无 JSON，仅 registry 记录)* | bjb1-32546 | 42 | **9%** (9/100) | 0.1 | 10 |

### 与 magnitude_curve_data.json 对比

| seed | 记录值 | JSON 实际值 | Registry 值 | 匹配? |
|------|--------|-------------|-------------|-------|
| 43 | 10% | 10% (10/100) | 10% | YES |
| 44 | 6% | 6% (6/100) | 6% | YES |
| 45 | 9% | 9% (18/200) | 9% | YES |
| 42 | **未记录** | 无文件 | 9% (9/100) | **缺失** |

### 结论

**三个已记录的数据点 (seed43=10%, seed44=6%, seed45=9%, mean=8.33%) 全部正确**，与服务器上的 JSON 文件和 registry 完全吻合。

**两个需要关注的问题：**

1. **seed42 (9%) 被遗漏**：`eval-acr-object-v4-scalar` 在 bjb1-32546 上完成了 seed42 的完整评估（10 tasks x 10 rollouts = 100 trials，9% SR），使用相同 checkpoint 和 `--max_correction_norm 0.1`。但 magnitude_curve_data.json 中 scalar baseline 未包含此数据。如果纳入，mean 从 8.33% (n=3) 变为 8.5% (n=4)。

2. **seed45 的 n_rollouts 不一致**：seed43/44 使用 10 rollouts/task，但 seed45 使用了 **20 rollouts/task** (total=200)。SR 值 (9%) 本身没错，但样本量不同可能影响 std 估计的可比性。

---
