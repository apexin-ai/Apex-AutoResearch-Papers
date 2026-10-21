# diagnose w5 lora scierc training

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w5_lora_scierc_training_20260515T150019_result.json`
- **Structured JSON:** [`3be437b4978fd0b0650c.json`](../../sessions/3b/3be437b4978fd0b0650c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**错误类型**: 配置错误（wandb 未登录）  
**根本原因**: `train_lora_scierc.py` 默认 `report_to="wandb"`，但服务器无 `WANDB_API_KEY`、无 `~/.netrc`、无 `~/.config/wandb`；wandb 在 noninteractive 下无法 prompt，抛 `UsageError` 终止训练。  
**失败位置**: `trainer.train()` 的 `on_train_begin` 回调，模型/数据/LoRA/Trainer 全部构造成功，未消耗显存。

**排除**: 非 OOM、非依赖缺失、非路径错误、非代码 bug。

**修复（无需改代码）**：
- 重跑命令前加 `WANDB_MODE=disabled` 直接禁用 wandb（最快）；或
- `export WANDB_API_KEY=[REDACTED] 后重跑保留 W&B 追踪。

诊断报告写入 `artifacts/w5_lora_scierc_training/diagnosis.md`（`save_project_file` 白名单不含 artifacts，已直接在本地路径写入）。

---
