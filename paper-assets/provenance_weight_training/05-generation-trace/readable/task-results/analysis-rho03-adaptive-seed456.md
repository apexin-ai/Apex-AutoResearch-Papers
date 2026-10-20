# analysis rho03 adaptive seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho03_adaptive_seed456_20260523T031218_result.json`
- **Structured JSON:** [`5d6e32f31836ff083d7a.json`](../../sessions/5d/5d6e32f31836ff083d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**rho03_adaptive_seed456 没有完成训练。** 关键发现：

- 训练只跑到 step 1000 / 6103（~16%），exit code 1（失败）
- 退出时间：2026-05-23T01:48:34Z
- 只有 `checkpoint-500` 和 `checkpoint-1000`，没有 `final` 目录
- 同批的 rho03_uniform_seed456 也失败了（exit code 1，停在 checkpoint-1500）
- 而 rho03_adaptive_seed42 和 seed123 都正常跑完了 6103 步

无法对未完成的模型运行 eval。需要从 checkpoint-1000 恢复训练。要我查看训练脚本的 resume 机制并重启训练吗？

---
