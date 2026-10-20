# diag plan014 failure

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan014-failure_20260514T035303_result.json`
- **Structured JSON:** [`ef47570fb63ab959f5d1.json`](../../sessions/ef/ef47570fb63ab959f5d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**：`--checkpoint_path` 路径多了 `/checkpoint-500`。由于训练时 `save_total_limit=1`，最终模型直接保存在 `plan001_exec_only_s42/` 根目录，不存在 `checkpoint-500` 子目录。transformers 找不到本地路径后尝试当 HF repo ID 解析，随即报错。

**修复**：重新运行时去掉路径末尾的 `/checkpoint-500`，改用 `/root/autodl-tmp/outputs/plan001_exec_only_s42`。代码本身无需修改。

是否现在重新提交运行？

---
