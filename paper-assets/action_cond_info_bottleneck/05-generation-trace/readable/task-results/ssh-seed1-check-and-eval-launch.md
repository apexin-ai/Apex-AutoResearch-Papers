# ssh seed1 check and eval launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed1-check-and-eval-launch_20260516T054211_result.json`
- **Structured JSON:** [`5f7ec09d4af03aab8b62.json`](../../sessions/5f/5f7ec09d4af03aab8b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**seed1 状态：仍在训练中，未完成。**

- **当前进度**: step 12800 / 20000 (64%)
- **进程**: PID 682228，已运行 4h13m，仍然存活
- **速度**: 0.8-0.9 steps/s
- **剩余**: 7200 steps ÷ ~0.85 steps/s ≈ **8470 秒 ≈ 2h21m**，预计 ~07:56 UTC 完成
- **最新 checkpoint**: checkpoint-10000（下一个应该是 checkpoint-15000）
- **scorer_mean**: 0.547-0.551，scorer_std: 0.447-0.449
- **loss 指标**: ib 持续下降 (0.166→0.158→0.164)，div 稳定在 -0.449~-0.451

不启动 eval，等训练完成。

---
