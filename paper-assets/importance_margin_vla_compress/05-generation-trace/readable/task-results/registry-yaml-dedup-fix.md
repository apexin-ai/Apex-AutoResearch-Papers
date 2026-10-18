# registry yaml dedup fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_yaml_dedup_fix_20260522T205526_result.json`
- **Structured JSON:** [`72f0438a4a017872231c.json`](../../sessions/72/72f0438a4a017872231c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 exp_ids are present and correct via `read_registry`:

| exp_id | status | success_rate | conclusion |
|--------|--------|-------------|------------|
| eval_pi05_l2norm_k095_spatial_seed42 | DONE | 0.978 | success |
| eval_pi05_random_k085_spatial_seed42 | DONE | 0.584 | success |
| eval_pi05_random_k0925_object_seed43 | DONE | 0.3 | success |

**没有重复条目。** 原始 YAML 中这 3 个 exp_id 各只出现一次，状态均为 DONE，metrics 和 conclusion 与任务要求完全一致。`read_registry` 也正确返回了它们。

可能之前的重复已经被某次写入覆盖掉了（YAML dict 的 key 重复时，解析器取最后一个，而后续 `update_registry` 写回时只保留了一份）。当前 registry 无需修复。

---
