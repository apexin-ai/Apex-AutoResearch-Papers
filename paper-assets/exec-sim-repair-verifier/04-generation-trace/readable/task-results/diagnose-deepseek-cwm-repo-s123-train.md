# diagnose deepseek cwm repo s123 train

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_deepseek-cwm-repo-s123-train_20260520T025627_result.json`
- **Structured JSON:** [`bf841a72e61ad32d09b1.json`](../../sessions/bf/bf841a72e61ad32d09b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练实际成功完成，EXIT_CODE=2 是 wrapper 脚本误报。**

关键发现：
- 3 epochs 全部跑完（2865/2865 steps），train_loss=0.077，eval_loss=0.043
- 日志中 error/traceback/oom 匹配数为 0
- `best/` checkpoint 完整保存（67MB adapter），另有 checkpoint-1910 和 checkpoint-2865
- GPU 2 已释放，磁盘空间充足（53G 可用）

**无需重新训练。** 建议将 registry 状态从 `failed` 更新为 `done`，直接用 `best/` checkpoint 进行 eval。

---
