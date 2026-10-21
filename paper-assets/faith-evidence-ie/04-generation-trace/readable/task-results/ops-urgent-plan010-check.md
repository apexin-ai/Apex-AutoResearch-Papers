# ops urgent plan010 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_plan010_check_20260519T231419_result.json`
- **Structured JSON:** [`3589d86439c2c6298391.json`](../../sessions/35/3589d86439c2c6298391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 项目 | 状态 |
|------|------|
| **进程 717143 / 717138** | 已死 |
| **Step 1 CED scoring** | ✅ 完成，`/root/autodl-tmp/rsft_scored_v3_large/rsft_train.jsonl` = 2691 行 |
| **Step 2 RSFT training** | ✅ 完成，adapter 在 `/root/autodl-tmp/rsft_output_nli_large/`（528MB，checkpoint-507） |
| **Step 3 Eval** | ❌ 启动即失败：`inference.py: error: the following arguments are required: --data_path`，EXIT_CODE=2 |
| **cuda:1** | 空闲（0 MiB / 0%） |

**训练指标**：train_loss=0.6124, eval_loss=0.7621, mean_token_accuracy=0.8292, epoch=3

**根因**：进程不是卡住，而是 Step 3 eval 脚本调用缺少 `--data_path` 参数导致立即退出，整个 pipeline 随之结束。

**下一步**：cuda:1 空闲，可以立即用正确参数重新提交 Step 3 eval。需要确认 eval 的 `--data_path` 和 `--output_dir` 参数值。

---
