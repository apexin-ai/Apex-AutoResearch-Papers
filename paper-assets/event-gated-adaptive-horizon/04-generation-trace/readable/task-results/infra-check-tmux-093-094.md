# infra check tmux 093 094

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_tmux_093_094_20260525T230435_result.json`
- **Structured JSON:** [`1205a2107334fce0b962.json`](../../sessions/12/1205a2107334fce0b962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 实验 | 服务器 | PID | 当前步数 | eval_return@5k | 状态 |
|------|--------|-----|---------|----------------|------|
| exp_093 (no_dt_emb, s2) | bjb1-45299, cuda:1 | 313815 | ~8000 | 9.1 | RUNNING ✓ |
| exp_094 (008d, s3) | westd-19154, cuda:0 | 53581 | ~8000 | 8.7 | RUNNING ✓ |

附带确认：
- **exp_092** (bjb1-45299, cuda:0, PID 313538) 也在跑，同步到 step 8000
- **exp_095** (westd-19154, cuda:1, PID 54124) 也已启动并在跑

两个 registry 已从 PREPARING → QUEUED → RUNNING 更新完毕。"duplicate session" 错误确认是因为之前的提交已成功创建了 tmux session，训练正常进行中。

---
