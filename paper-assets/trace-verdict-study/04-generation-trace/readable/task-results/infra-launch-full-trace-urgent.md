# infra launch full trace urgent

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_launch-full-trace-urgent_20260514T183740_result.json`
- **Structured JSON:** [`a2d58a75955e375ee1dd.json`](../../sessions/a2/a2d58a75955e375ee1dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**full_trace** — 启动成功，运行正常
- PID: 712474，GPU 0 占用 15.3GB / 97.8GB
- 进度: 128/444 steps (29%)，~17s/step，预计剩余 ~1.5h
- 无 OOM，无报错

**vota (GPU 1)** — 运行中
- GPU 1 占用 41.2GB，利用率 100%
- 进度在正常推进（日志被截断，但 GPU 状态健康）

**no_trace** — 失败
- `SFTConfig.__init__() got an unexpected keyword argument 'max_seq_length'`，EXIT_CODE=1
- 这是 TRL 版本兼容性问题（新版 SFTConfig 改名了该参数）。需要修复后重跑。

---
