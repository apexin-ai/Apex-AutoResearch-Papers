# code fix exp002 checkpoint path

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-exp002-checkpoint-path_20260514T102945_result.json`
- **Structured JSON:** [`19c0e478945eb7e05634.json`](../../sessions/19/19c0e478945eb7e05634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

- **已 kill** 旧进程 346325
- **已修复** `run_batch.py` 第50行：`checkpoint_path` 返回值追加 `/lora_adapter`
- **已验证** d000/d005/d100 三个 dosage 的 `lora_adapter/adapter_config.json` 均存在
- **已提交** v2 on cuda:0，PID 349740，9 tasks (3×3)，正在跑 task 1/9 (d000/mmlu)
- **Registry** 已更新 notes

注意：`--skip-completed` 检查的是 `signals_merged_*.json`，但 `compute_signals.py` 保存的合并文件名不含 `model_id` 后缀，两边命名不一致，所以 skip 逻辑实际不生效。这次全部重跑，不影响结果，但后续如果需要断点续跑需要修。

---
