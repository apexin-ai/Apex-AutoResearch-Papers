# check ds s123 e3 eval done

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ds-s123-e3-eval-done_20260522T114754_result.json`
- **Structured JSON:** [`2bea95c872c7d67dcc85.json`](../../sessions/2b/2bea95c872c7d67dcc85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**deepseek-cwm-repo-s123-e3-eval → DONE (success)**

| Seed | Accuracy | F1 macro | F1 fail | Unparseable |
|------|----------|----------|---------|-------------|
| s42 | 61.49% | — | — | — |
| **s123** | **57.31%** | **51.79%** | **35.49%** | **51.39%** |
| s456 | ~56% | — | — | — |

- checkpoint: `checkpoint-12627`，日志和结果 JSON 均完整，进程正常退出
- 57.31% 在预期 56-62% 范围内，三 seed 均一致低于 majority baseline（72.96%），CWM repo-level 表现符合预期
- Registry 已更新（status=DONE, conclusion=success, metrics 已写入）
- 无活跃 cron 需要删除（已在之前 session 清理）

---
