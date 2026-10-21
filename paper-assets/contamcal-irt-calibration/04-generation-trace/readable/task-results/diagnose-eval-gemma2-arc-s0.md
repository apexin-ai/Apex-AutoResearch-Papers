# diagnose eval gemma2 arc s0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gemma2_arc_s0_20260520T222315_result.json`
- **Structured JSON:** [`7df236e2d5bdfa946480.json`](../../sessions/7d/7df236e2d5bdfa946480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个文件完整，sentinel 均存在。结果：

```
d000_s0: accuracy=0.8584 (1006/1172)
d005_s0: accuracy=0.8677 (1017/1172)
d025_s0: accuracy=0.6485 (760/1172)
d050_s0: accuracy=0.8549 (1002/1172)
```

所有 `.done` sentinel 已创建（May 21 06:07-06:17），eval 确认完成。

注意 d025 accuracy 异常低（64.85%），远低于 baseline d000（85.84%），而 d005 和 d050 都在 ~86% 附近。d025 可能存在训练或 checkpoint 问题，值得复查。

---
