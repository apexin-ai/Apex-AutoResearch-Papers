# ssh gpu1 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu1-status-check_20260515T130234_result.json`
- **Structured JSON:** [`37859269124d5efcfc01.json`](../../sessions/37/37859269124d5efcfc01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

**GPU 1 状态**
- 显存：40701 MiB / 97887 MiB（已用 41.6%，空闲 57194 MiB）
- 进程：仅 PID 353661（python3，40692 MiB）
- **PID 352975 已不存在**，显存已释放

**r3 训练进度**
- 当前 step：250/1000（25%）
- 运行时间：约 6 分 34 秒
- 最近速度：~0.76–0.85 s/step（1.17–1.35 it/s）
- step 200 处有一次 eval 导致瞬时降速（12.29 s/it），之后恢复正常
- **对比基准 1.7 s/step：当前速度约快一倍**，符合预期——GPU 1 独占后无显存争抢

---
