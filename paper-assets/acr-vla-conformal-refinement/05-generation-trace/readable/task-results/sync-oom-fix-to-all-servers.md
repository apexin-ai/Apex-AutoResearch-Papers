# sync oom fix to all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_oom-fix-to-all-servers_20260525T111559_result.json`
- **Structured JSON:** [`77d58bff1e665f9b34fe.json`](../../sessions/77/77d58bff1e665f9b34fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 台服务器全部同步完成，MD5 一致，语法检查通过：

```
bjb1-32546: ✓ synced, syntax OK, MD5 match, grep confirms 5 fix lines
bjb2-28827: ✓ synced, syntax OK, MD5 match, grep confirms 5 fix lines
bjb1-18228: ✓ synced, syntax OK, MD5 match, grep confirms 5 fix lines
cqa1-32758: ✓ synced, syntax OK, MD5 match, grep confirms 5 fix lines
```

修复内容（lines 709-731）：每个 rollout 后 `gc.collect()` + `torch.cuda.empty_cache()`，OOM 异常捕获保留 partial results。

---
