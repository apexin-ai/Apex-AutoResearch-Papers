# code fix inference quality

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_inference_quality_20260514T061441_result.json`
- **Structured JSON:** [`53afd73176fe9f1edd01.json`](../../sessions/53/53afd73176fe9f1edd01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件修改完成，语法验证通过。改动总结：

**sampling.py**:
- `format_chat_prompt` 加了 `enable_thinking=False`，避免 `&lt;think>` 块与 XGrammar 冲突
- 新增 `_TRAIN_ALIGNED_TEMPLATE`（与训练 prompt 格式一致）和 `SCIERC_SCHEMA_HINT` 常量
- `build_uie_prompt` 新增 `use_train_format` 参数（默认 `True`），启用时统一用训练模板
- `run_sampling_pipeline` 新增 `use_train_format` 参数并透传

**run_mvp_pilot.py**:
- 新增 `--schema_hint`、`--use_train_format` 参数；`--subtask` 扩展支持 `joint`
- SciERC 数据集在 `use_train_format=True` 时自动填充 schema hint
- `joint` 模式下用统一 prompt 采样一次，NER/RE 分别评估并报告
- `print_report` 重构为支持 joint 模式的分块打印

---
