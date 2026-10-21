# ops verify all eval scripts skip logic

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-all-eval-scripts-skip-logic_20260519T103718_result.json`
- **Structured JSON:** [`8a7a8db276694dab3cb3.json`](../../sessions/8a/8a7a8db276694dab3cb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，语法验证通过。

### 报告

| 脚本 | 服务器 | skip 检查文件名 | 状态 |
|---|---|---|---|
| `run_exp004_unified_eval.sh` | westd-28034 | `${EXP_ID}_preset_eval.json` | 已正确 |
| `run_exp008v3_unified_eval.sh` | westd-28034 | ~~`_results.json`~~ → `_preset_eval.json` (2处) | **已修复** |
| `run_exp003_unified_eval.sh` | westd-29046 | ~~`_metrics.json`~~ → `_preset_eval.json` (1处) | **已修复** |
| `run_exp002v2recalib_unified_eval.sh` | westd-29046 | `${EXP_ID}_preset_eval.json` | 已正确 |

修复内容：
- **exp008v3**: 行37 `${EXP_ID}_results.json` → `${EXP_ID}_preset_eval.json`，行63 `${FINAL_EXP_ID}_results.json` → `${FINAL_EXP_ID}_preset_eval.json`
- **exp003**: 行30 `${exp_id}_metrics.json` → `${exp_id}_preset_eval.json`

---
