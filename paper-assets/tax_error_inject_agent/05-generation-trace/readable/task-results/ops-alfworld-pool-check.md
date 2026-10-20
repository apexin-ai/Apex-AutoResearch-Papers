# ops alfworld pool check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_alfworld-pool-check_20260516T053423_result.json`
- **Structured JSON:** [`6b86f05664c7c6ec2820.json`](../../sessions/6b/6b86f05664c7c6ec2820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## ALFWorld 任务池统计

| Split | 任务数 |
|-------|--------|
| train | 2435 |
| valid_seen | 242 |
| valid_unseen | 85 |
| **总计** | **2762** |

### 任务类型分布（train）

| 类型 | 数量 | 占比 |
|------|------|------|
| pick_two_obj_and_place | 407 | 16.7% |
| pick_and_place_simple | 385 | 15.8% |
| pick_and_place_with_movable_recep | 365 | 15.0% |
| pick_heat_then_place_in_recep | 340 | 14.0% |
| pick_cool_then_place_in_recep | 339 | 13.9% |
| pick_clean_then_place_in_recep | 334 | 13.7% |
| look_at_obj_in_light | 265 | 10.9% |

### 结论

**总任务数 2762，不满足 ≥ 3500 的 gate 要求，缺口 738。**

即使把 train + valid_seen + valid_unseen 全部用上也只有 2762。仅用 train split 则只有 2435，缺口更大（1065）。

可能的应对方案（供参考）：
- 对同一任务用不同 agent prompt / 不同错误注入策略生成多条 trajectory，从而在 2435 个 unique 任务上产出 2500 条 trajectory（每个任务平均跑 ~1.03 次即可）
- 将 valid_seen/valid_unseen 也纳入 trajectory 收集（但需确认不影响评估）

---
