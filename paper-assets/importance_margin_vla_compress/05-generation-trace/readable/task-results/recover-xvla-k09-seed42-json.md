# recover xvla k09 seed42 json

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recover_xvla_k09_seed42_json_20260523T014957_result.json`
- **Structured JSON:** [`2d411afbdfa4b6cbc488.json`](../../sessions/2d/2d411afbdfa4b6cbc488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。

**原始文件不可恢复。** 具体情况：

- `xvla_prune_k0.9_libero_object.json`（seed42 的默认文件）已被覆盖，当前内容是 mode="random"、SR=97.8%，不是原始的 L2 norm 评估（SR=99.2%）
- seed43/seed44 文件确认命名模式一致（mode="l2_norm_prune"），说明原始 seed42 文件确实存在过，但被后续的 random pruning 评估覆盖了
- 无备份文件，无对应 log 文件
- spatial 和 goal suite 的 L2norm k=0.9 seed42 JSON 完好（`xvla_spatial_k09_seed42.json`、`xvla_goal_k09_seed42.json`），仅 libero_object 的 seed42 丢失

Registry 中 `eval_xvla_prune_k09_seed42` 的 reconstructed 标注保持不变。SR=99.2% 来自交叉引用，per_task_sr 和 wilson_ci_95 无法补充。

---
