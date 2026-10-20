# diagnose openvla spatial standardized v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_openvla_spatial_standardized_v1_20260522T072334_result.json`
- **Structured JSON:** [`29d35b70404a8d575813.json`](../../sessions/29/29d35b70404a8d575813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：transformers 今天被升级到 5.9.0，该版本移除了 `AutoModelForVision2Seq`（替代类为 `AutoModelForImageTextToText`）。脚本在 import 阶段立即崩溃，0 个 phase 完成。5.74 小时全部消耗在等待 checkpoint 下载上。

**现状**：`libero_spatial_full_pipeline.py` 已有人修复了 import，但未重跑。另外 6 个脚本（`libero_object/long/goal_full_pipeline.py` 等）仍使用旧 import，需要一并修复。

**修复**：推荐批量 sed 替换所有脚本中的 `AutoModelForVision2Seq` → `AutoModelForImageTextToText`，然后重跑实验。checkpoint 已下载完成，重跑不会再等。

报告已写入 `artifacts/openvla_spatial_standardized_v1/diagnosis.md`。

---
