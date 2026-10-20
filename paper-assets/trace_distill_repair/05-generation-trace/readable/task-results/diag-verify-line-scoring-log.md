# diag verify line scoring log

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_verify_line_scoring_log_20260515T014705_result.json`
- **Structured JSON:** [`70ac5f128bf6310db957.json`](../../sessions/70/70ac5f128bf6310db957.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 日志最后几行

```
=== Phase 2 Scoring Complete (line) ===
Instances: 38
Segments:  3922
Scored:    2256
Failed:    1666
Time:      14016.1s
```

实验正常完成，有明确的 "Phase 2 Scoring Complete" 结束标记，无 error/traceback/crash。日志中的 WARNING 均为 API 返回 None content 的正常重试（最多 3 次），以及 1 次 502 Bad Gateway 自动重试，属正常行为。

### 日志 vs Registry 一致性

| 指标 | 日志 | Registry | 匹配 |
|------|------|----------|------|
| instances | 38 | 38 | ✓ |
| total_segments | 3922 | 3922 | ✓ |
| scored_segments | 2256 | 2256 | ✓ |
| failed_segments | 1666 | 1666 | ✓ |
| elapsed_seconds | 14016.1 | 14016 | ✓ |

Registry 额外记录的 keep=38, drop=2218, error=1666 在日志尾部未直接显示，但属于后续聚合统计，不矛盾。

### 输出文件

`phase2_line_scores.json` 存在，1,832,507 字节，与 registry 中 `output_size_bytes: 1832507` 完全一致。

### 结论

日志与 registry 完全一致，实验正常完成。Registry 已是 `status=DONE, conclusion=success`，无需更新。

---
