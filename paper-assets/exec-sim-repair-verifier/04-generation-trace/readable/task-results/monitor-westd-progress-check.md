# monitor westd progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-progress-check_20260514T234731_result.json`
- **Structured JSON:** [`78baa04d48b43c607703.json`](../../sessions/78/78baa04d48b43c607703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总（2026-05-15 07:48 UTC）

| 进程 | GPU | 当前 step | 总步数 | 进度 | train loss | eval loss | ETA | 状态 |
|------|-----|-----------|--------|------|-----------|-----------|-----|------|
| CLS 8B s42 resume | cuda:1 | 1000 | 6633 | 15.1% | ~1.04 | 0.182 | ~19h | 运行中，~293 step/h |
| CWM 8B v4 | cuda:2 | 2500 | 6633 | 37.7% | 0.085 | 0.435 | ~27h | 运行中，~154 step/h |
| CLS 8B seed123 v3 | cuda:3 | 4600 | 6633 | 69.4% | ~0.28 | 0.387 | ~7h | 运行中，~286 step/h |
| CLS 8B s42 ckpt-800 val eval | cuda:0 | 2290/9335 样本 | — | 24.5% | — | — | ~23min | running_acc=85.1% |

**备注：**
- 4 个进程全部存活，无报错
- CWM 速度明显慢于 CLS（~154 vs ~286 step/h），因为 CWM 每 100 步存 checkpoint 且有 eval
- CLS s42 resume 刚跑不到 2h，从 ckpt-600 resume 到了 step 1000
- CLS seed123 进展最快，预计今天下午完成
- Eval 进程刚启动 7 分钟，约 23 分钟后出结果

---
