# code exp016 unified reeval prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp016-unified-reeval-prep_20260519T100949_result.json`
- **Structured JSON:** [`6d1c7447ddb3934586dc.json`](../../sessions/6d/6d1c7447ddb3934586dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 验证通过。脚本已创建在 `/root/contrastive_entrain_calib/eval/eval_exp016_actadd_unified.py`。

整合内容:
- **ActAdd hook**: 从 `run_exp016_reeval.py` 提取 `SteeringHookManager` + `load_directions`，`target_layers` 改为参数化
- **Eval 流程**: 从 `eval_unified_preset.py` 提取 D027 标准流程（NLIChecker discrete classification, ToF/NoF/SYCONScore）
- **Generation**: `enable_thinking=False` + regex `&lt;think>` 清除
- **输出**: 每个 alpha 打印指标 + 最终汇总表 + `summary.json` + `detailed.json`
- 所有路径默认值已配置（directions.pt, calibration data, Qwen3-8B, NLI 模型），离线环境变量已设置

---
