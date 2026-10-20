# code fix server code and submit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_server_code_and_submit_20260514T133943_result.json`
- **Structured JSON:** [`0a1e2f1b4f9d6b75c435.json`](../../sessions/0a/0a1e2f1b4f9d6b75c435.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 检查项 | 结果 |
|--------|------|
| n_min 默认值 `max(2, batch_size // 2)` | line 280, 正确 |
| 无 EMA 相关代码 | grep 返回空，确认无 ema |
| unweighted_loss 日志 | line 130/158/191，存在 |
| help 文本说 `batch_size // 2` | line 237-239，一致 |
| alpha_eff.py 存在 | 6863 bytes，存在 |
| Python 验证 n_min=2 | PASS |

代码已修正，可以开始跑 adaptive_fix 实验。

---
