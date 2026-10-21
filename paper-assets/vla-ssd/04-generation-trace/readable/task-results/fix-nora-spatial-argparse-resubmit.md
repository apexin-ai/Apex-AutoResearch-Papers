# fix nora spatial argparse resubmit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nora_spatial_argparse_resubmit_20260521T090133_result.json`
- **Structured JSON:** [`187701e9b63acadb4541.json`](../../sessions/18/187701e9b63acadb4541.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都在正常运行。

## 汇报

**修复内容**：`nora_spatial_full_pipeline.py` 的 `--conditions` argparse 从逗号分隔字符串改为 `nargs="+"` + `choices=["trained", "untrained"]`，与 nora_goal 一致。同时修复 line 587 的解析逻辑。

**重新提交**：`nora_spatial_pipeline_v2` 已提交到 cuda:1，PID=547498，模型加载中，pipeline conditions 正确解析为 `['trained', 'untrained']`。

**object_untrained_pipeline_v1 (cuda:0)**：运行正常，Phase 1 完成（5000 samples），正在 Phase 2 Ridge probing（L0 img_mean R²=0.7455）。

---
