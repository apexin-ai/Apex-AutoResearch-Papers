# code val sweep analysis script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_val-sweep-analysis-script_20260514T071242_result.json`
- **Structured JSON:** [`a960250bba473478505e.json`](../../sessions/a9/a960250bba473478505e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。目前只有 1 个结果文件（seed123/ckpt-200），val accuracy 62.51%，符合预期——ckpt-200 是早期 checkpoint，在 val 上表现差，与它在 test 上也较差的已知情况一致。

Unparseable 数量 1883 说明 ckpt-200 在 batch_size=8 下有大量输出格式问题（对比 test 的 batch_size=16 只有 132 unparseable）。随着更多 checkpoint 结果写入，脚本会自动分组展示并推荐 best checkpoint。

---
