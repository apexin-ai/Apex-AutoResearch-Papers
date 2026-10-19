# ops fix extract activations

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-extract-activations_20260521T071327_result.json`
- **Structured JSON:** [`05d4d3717db09d82481b.json`](../../sessions/05/05d4d3717db09d82481b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个修复全部完成并验证通过：

1. **LANGS_20**: `"th"` → `"te"` (line 53 确认)
2. **compute_layer_indices**: interval 模式现在自动 append 最后一层（`n_layers-1`），docstring 中 Qwen3-235B 层数更新为 25
3. **run_p0.sh**: 注释中添加了单卡（Llama4 Scout, `GPU_IDS=0`）和多卡（Qwen3-235B, `GPU_IDS=0,1,2,3`）的用法示例，默认值保持 `0,1,2,3` 不变

---
