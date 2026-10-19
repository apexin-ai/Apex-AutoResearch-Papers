# code connector only ablation

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_connector-only-ablation_20260517T150609_result.json`
- **Structured JSON:** [`19564b3f55b209feb95c.json`](../../sessions/19/19564b3f55b209feb95c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：

- **Total**: 450,169,185 params
- **Trainable**: 11,796,480 (2.62%) — 只有 connector 的 `modality_projection.proj.weight`
- scorer params 已被冻结（不再出现在 trainable 列表中）

修改总结：

| 文件 | 修改 |
|------|------|
| `config.py` | `freeze_mode` Literal 增加 `"connector_only"` |
| `acib_policy.py` `_connector_hook` | `connector_only` 模式跳过 scorer，直接 return output |
| `acib_policy.py` `_setup_freeze_by_mode` | 新增 `connector_only` 分支：冻结 base_policy + scorer，只解冻 connector |
| `acib_policy.py` `forward` | 无需显式修改 — hook 不缓存 logits，现有 `if not self._cached_logits` 检查自动跳过所有 ACIB loss |
| `train_acib.py` | `--freeze_mode` choices 增加 `"connector_only"` |
| `scripts/run_connector_only.sh` | 新建训练脚本，`--freeze_mode connector_only`，所有 ACIB loss lambda=0.0 |

Trainable params = 11.8M（仅 connector），符合预期。

---
