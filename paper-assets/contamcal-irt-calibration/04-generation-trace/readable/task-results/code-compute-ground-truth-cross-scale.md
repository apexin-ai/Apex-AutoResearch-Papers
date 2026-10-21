# code compute ground truth cross scale

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compute_ground_truth_cross_scale_20260514T205354_result.json`
- **Structured JSON:** [`19668ffa54f2acbecce3.json`](../../sessions/19/19668ffa54f2acbecce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，所有测试通过。

**改动摘要：**
- `compute_ground_truth(responses, dosages, models=None)` — 新增可选 `models` 参数
- 当存在多 scale（`models` 中有 ≥2 个不同 scale）时，每个 d>0 模型的 counterfactual 取同 scale d0 均值；某 scale 无 d0 时 fallback 全局均值 + WARNING
- 单 scale 或无 `models` 参数时行为与原来完全一致（测试已验证）
- 调用处 L425 传入 `models=models_bench`

测试数据证实了 bug 影响：0.5B 旧值高估 ~15pp，3B 低估 ~15pp，修复后各 scale 使用自己的 d0 基线。

---
