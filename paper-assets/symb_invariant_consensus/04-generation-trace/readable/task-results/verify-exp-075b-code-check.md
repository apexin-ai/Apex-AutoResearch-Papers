# verify exp 075b code check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp-075b-code-check_20260519T180735_result.json`
- **Structured JSON:** [`691cc7b9b7d4bc0456ce.json`](../../sessions/69/691cc7b9b7d4bc0456ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：**一切正常，无需干预。**

| 检查项 | 状态 |
|--------|------|
| 磁盘代码 `pro_n_unique` | 不存在 ✓ |
| 归一化逻辑 `max(n_pro, 1)` | 第 214 行存在 ✓ |
| 进程 PID 265705 | 运行中，已 17 分钟 ✓ |
| 日志报错 | 无 `KeyError`，无异常 ✓ |
| 处理进度 | 20/204（正在处理 folio_19），ETA ~162 min |
| 中间文件 | folio_0 ~ folio_18 已保存（19 个） |
| API 调用 | 正常返回 HTTP 200，有偶发 retry 但成功恢复 |

进程使用的是修复后的代码，正常推进中。

---
