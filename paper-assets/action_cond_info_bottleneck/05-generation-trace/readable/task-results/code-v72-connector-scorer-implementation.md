# code v72 connector scorer implementation

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v72-connector-scorer-implementation_20260517T075346_result.json`
- **Structured JSON:** [`babf5779f502bea7b6a8.json`](../../sessions/ba/babf5779f502bea7b6a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 修改结果

**config.py**: 新增 `freeze_mode` 字段，类型 `Literal["legacy", "scorer_only", "connector_scorer", "all_trainable"]`，默认 `"legacy"` 保持向后兼容。

**acib_policy.py**: `_setup_freeze` 新增 `freeze_mode != "legacy"` 分支，委托给 `_setup_freeze_by_mode`：
- `scorer_only`: 冻结全部 base_policy，仅训 scorer
- `connector_scorer`: 冻结全部 base_policy，解冻 connector + scorer
- `all_trainable`: 不冻结任何东西，仅确保 scorer 可训

**train_acib.py**: 新增 `--freeze_mode` CLI 参数，传入 ACIBConfig，日志输出。

**run_v7.2_connector_scorer.sh**: 训练脚本，lr=5e-5。

### 参数统计验证

| 模式 | Trainable | 比例 |
|------|-----------|------|
| legacy (scorer_only) | 123,009 | 0.03% |
| connector_scorer | 11,919,489 | 2.65% |

其中 connector_scorer = connector 11,796,480 + scorer 123,009，符合预期（~11.8M + ~0.1M）。

---
