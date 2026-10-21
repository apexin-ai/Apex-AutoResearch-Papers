# code v2 gradient comparison script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-comparison-script_20260526T202845_result.json`
- **Structured JSON:** [`c657ac4aebd12f384a08.json`](../../sessions/c6/c657ac4aebd12f384a08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

1. **`/root/occsafe_vla/scripts/compare_gradient_conditions.py`** 已创建并通过语法检查。支持两种模式：
   - JSON 模式：读取 3 个预计算的 `_gradient_stats.json`
   - Checkpoint 模式：给 3 个 checkpoint 路径，自动依次调用 `run_gradient_analysis_v2.py`

2. **输出内容**：
   - 每层 action gradient norm（3 条件并排）
   - 每层 occ gradient norm
   - 每层 cosine similarity（如有）
   - Full OCC LN / Vanilla ratio 和 Detach LN / Vanilla ratio
   - 摘要统计（mean/std/max/min ratio 及对应层）
   - 终端表格 + JSON 文件

3. **`artifacts/gradient_analysis_v2_commands.md`** 已创建，含完整运行命令、checkpoint 路径变量、SCP 说明。

---
