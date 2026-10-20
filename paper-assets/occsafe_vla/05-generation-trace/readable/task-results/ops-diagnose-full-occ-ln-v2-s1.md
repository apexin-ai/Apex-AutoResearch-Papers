# ops diagnose full occ ln v2 s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-full_occ_ln_v2_s1_20260526T120622_result.json`
- **Structured JSON:** [`66da8c7fc8835e424773.json`](../../sessions/66/66da8c7fc8835e424773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志在持续增长（16KB → 20KB），进程 PID 341987 存活。训练刚启动约 7 分钟，当前大约在 step ~400。

**结论：full_occ_ln_v2_s1 并未退出，仍在正常训练中。**

- 进程：PID 341987，GPU 2，62GB 显存，99% 利用率
- 启动时间：20:01:53（约 7 分钟前）
- 当前状态：正在训练中，进度条通过 `\r` 覆写使得日志文件看起来很小
- 无任何错误或异常
- Checkpoint 目录已创建但尚无模型权重（save_freq=10000，还早）

同样 full_occ_ln_v2_s0（PID 341771，GPU 1）也在运行中。

不需要更新 registry 或删除 cron，训练仍在进行。

---
