# fix bjb1 vla only k1 restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb1-vla-only-k1-restart_20260514T000235_result.json`
- **Structured JSON:** [`e155c578010bb54ee0f5.json`](../../sessions/e1/e155c578010bb54ee0f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已由前一个 Worker 完成，当前状态确认如下：

**代码修复**: `evaluate.py` 第 364-365 行已添加 `if args.mode == "vla_only": args.K = 1`，在 `main()` 中解析参数后立即强制覆盖 K 值。

**进程状态**:
| 进程 | PID | GPU | 状态 |
|------|-----|-----|------|
| eval-spatial-v7 (vla_only, **K=1**) | 123761 | cuda:0, 6185 MiB | 已启动，正在加载环境 |
| eval-acr-spatial-v2 (acr_vla, K=10) | 117814 | cuda:1, 1450 MiB | 正常运行，未受影响 |
| eval-reconvla-spatial-v3 (reconvla, K=10) | 118108 | cuda:2, 1414 MiB | 正常运行，未受影响 |
| crm-train-a4-scalar-unc | 121984 | cuda:3, 532 MiB | 正常运行，未受影响 |

原 PID 117486 已不存在。新进程 123761 的日志确认 `'K': 1`，输出到 `eval-spatial-v7.log`。预估运行时间从 20-30h 降至 2-3h。

---
