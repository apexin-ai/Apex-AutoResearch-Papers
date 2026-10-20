# verify debugbench fix landing

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_debugbench_fix_landing_20260515T232113_result.json`
- **Structured JSON:** [`f88f191c926c7afff3ac.json`](../../sessions/f8/f88f191c926c7afff3ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。总结：

### 修复落地确认
- **代码修复已 apply**：`format_sample()` L148-159 有 `test_results.error` fallback，不在 `compress_exception_only()` 函数本身而在调用前注入合成 exception 事件
- 数据文件 5 月 16 日 07:12-07:13 重新生成

### 5 条件数据验证

| Condition | Train | Test | Mean tok | Median | Max | >2048 |
|-----------|-------|------|----------|--------|-----|-------|
| no_trace | 1622 | 426 | 274 | 226 | 1849 | 0% |
| exception_only | 1622 | 426 | 377 | 299 | 1879 | 0% |
| full_trace | 1622 | 426 | 1508 | 2048 | 2048 | 0% |
| vota | 1622 | 426 | 1508 | 2047 | 2048 | 0% |
| ae_only | 1622 | 426 | 754 | 731 | 2048 | 0% |

### exception_only 修复效果
- **Fail signal coverage: 207/207 = 100.0%**
- Pass false signal: 0/219 = 0.0%
- 信号完美分离，理论上限 100%

### Registry
- `debugbench_exception_bug_fix`: PENDING → **DONE** (success)

---
