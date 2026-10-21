# fix plan 009 csv sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_009_csv_sync_20260515T190642_result.json`
- **Structured JSON:** [`f5be438b1d67dd552c03.json`](../../sessions/f5/f5be438b1d67dd552c03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三件事全部完成：

1. **修 CSV `group_size`**：两份本地 CSV（`plan_009_forgetting_data.csv` 和 `_v5.csv`）中 `qlora_ced_lr5e6` 的 `group_size` 已从 `4` 改为 `8`。服务器端 `training_logs_grpo.json` 新增 `_metadata` 段记录各实验的 `group_size`，plot 脚本标签统一添加了 `G=8`，并重新生成了 PDF/PNG。

2. **同步图表 + 注册 artifact**：`grpo_forgetting_dynamics.pdf` 和 `.png` 已 SCP 到本地 artifacts 目录，注册为 `art_20260515_8df0cd`（PDF）和 `art_20260515_6847e6`（PNG）。

3. **memory.md 已更新**：添加了 "Figure Notes" 段，记录 caption 需注明"仅展示 CED reward 变体"以及 `group_size` 修正记录。

---
