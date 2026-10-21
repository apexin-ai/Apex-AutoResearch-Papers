# diagnose detect remove q07 epoch matched seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detect_remove_q07_epoch_matched_seed42_20260519T011147_result.json`
- **Structured JSON:** [`b53759a04684792bffb4.json`](../../sessions/b5/b53759a04684792bffb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

**失败原因**：磁盘满（`/root/autodl-tmp/` 250G 100% 占满）。在 step 2000 保存 checkpoint 时 safetensors 序列化写入失败（errno 28）。

**训练进度**：崩溃于 step 2000/3047（64%），运行约 70 分钟。

**Checkpoint 状态**：
- checkpoint-500/1000/1500 均完整可用（各约 3.4GB）
- checkpoint-2000 **不完整**（model.safetensors 被截断至 795MB，正常应为 1.19GB，且缺少 optimizer/tokenizer/trainer_state），不可用

**可以 resume**：从 checkpoint-1500 恢复，需先清理磁盘空间（至少删除损坏的 checkpoint-2000 + 其他实验旧文件，释放 10-15GB）。

报告已保存至 `artifacts/detect_remove_q07_epoch_matched_seed42/report/diagnose_q07_epoch_matched.md`。

---
