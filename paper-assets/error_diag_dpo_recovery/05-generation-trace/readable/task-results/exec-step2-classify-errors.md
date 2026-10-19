# exec step2 classify errors

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_step2-classify-errors_20260512T145347_result.json`
- **Structured JSON:** [`35849da875815122def2.json`](../../sessions/35/35849da875815122def2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

88 条分类全部完成，无报错。结果汇总：

## 分类结果

| 错误类型 | 数量 | 占比 | 平均 correction_horizon |
|----------|------|------|------------------------|
| **Planning** | 79 | 89.8% | 1.4 |
| **Action** | 5 | 5.7% | 1.0 |
| **Verification** | 4 | 4.5% | 1.5 |

## 按 task_type 交叉统计

| Task Type | 总数 | Action | Verification | Planning |
|-----------|------|--------|-------------|----------|
| pick_two_obj | 18 | 0 | 0 | 18 |
| pick_clean_then_place | 20 | 2 | 0 | 18 |
| pick_heat_then_place | 19 | 0 | 1 | 18 |
| pick_and_place | 17 | 3 | 3 | 11 |
| look_at_obj | 7 | 0 | 0 | 7 |
| pick_cool_then_place | 7 | 0 | 0 | 7 |

## 注意事项

- 总共 88 条（非 89），有 1 条 reward 不是 False 被过滤
- **P1 Gate FAIL**：horizon(action)=1.0 < horizon(verification)=1.5 但 horizon(planning)=1.4 < horizon(verification)，planning 和 verification 的 horizon 未满足预期大小关系
- planning 占比极高（89.8%），模型倾向于将大多数错误归为 planning error。可能需要 cross-validation（`--cross_validate`）或调整 prompt 来获得更均衡的分类
- 输出文件：`/root/autodl-tmp/error_diag_dpo_recovery/data/classified/classified_errors.jsonl`

---
