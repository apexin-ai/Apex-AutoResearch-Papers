# ops post restart check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-check_20260517T124543_result.json`
- **Structured JSON:** [`ef7df761009d2bb25af2.json`](../../sessions/ef/ef7df761009d2bb25af2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行，没有被杀或者已经被重启。

## 状态汇总

| 实验 | GPU | 当前步数 | 目标步数 | 进度 | Checkpoint |
|------|-----|---------|---------|------|-----------|
| sweep-random-b005-s44 | cuda:0 (93%) | 444 | 500 | 88.8% | checkpoint-400 |
| plan002-additive-b01-s45-1000 | cuda:1 (37%) | 705 | 1000 | 70.5% | checkpoint-700 |

- **GPU**: 两张卡都在被占用，进程正常（PID 319527 @ 19:16 启动，PID 326673 @ 19:51 启动）
- **磁盘**: 91G 空闲 (64% used)，充足
- **sweep-random-b005-s44**: 还剩 ~56 步，估计很快完成
- **plan002-additive-b01-s45-1000**: 还剩 ~295 步，ISR 已经 collapse 到接近 1.0（step 700+ 连续 ISR=1.0, loss=0），这个实验可能已经过拟合

注意 plan002 的 ISR 从 step 686 开始基本锁在 1.0，prove_rate=1.0，loss=0，这是典型的 ISR collapse 现象（C006 所述的 metric gaming）。你可能需要关注这个实验的最终 eval 结果是否有意义。

---
