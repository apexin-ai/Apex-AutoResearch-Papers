# analyze cls4b v5 ckpt600 test5120 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls4b-v5-ckpt600-test5120-eval_20260515T104457_result.json`
- **Structured JSON:** [`a8bebaa90b7e3e144b36.json`](../../sessions/a8/a8bebaa90b7e3e144b36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: success (EXIT_CODE=0, 日志无 error/exception)

METRICS:
  accuracy:       77.74%
  f1_macro:       74.74%
  f1_fail:        66.03%
  f1_pass:        83.44%
  precision_fail: 56.21%
  recall_fail:    80.01%
  unparseable:    0
  total:          9784

LOG_NOTES:
  - 模型: Qwen/Qwen3-4B, checkpoint-600, max_seq=5120, batch=16
  - 类别分布: pass=7138, fail=2646 (majority baseline 73.0%)
  - accuracy 超 majority baseline +4.78pp
  - fail 类 recall 高 (80%) 但 precision 低 (56.2%)，1649 个 pass 样本被误判为 fail
  - 推理耗时 1613.5s (~27min), 0 条截断
  - predictions 行数 9784，与 total 一致
```

---
