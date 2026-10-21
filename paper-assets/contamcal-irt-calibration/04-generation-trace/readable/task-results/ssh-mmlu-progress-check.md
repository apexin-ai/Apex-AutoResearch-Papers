# ssh mmlu progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mmlu-progress-check_20260513T203927_result.json`
- **Structured JSON:** [`75a9c4aa4b533dff1076.json`](../../sessions/75/75a9c4aa4b533dff1076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
MMLU paraphrase: PID=204472/204758 [存活], 进度 826/878 batches (94%), 运行 1h25m, 预估剩余 ~10min

GPU 1 (0.5B s123): PID=214583 [已死] — OOM 失败，model.to(device) 时 GPU 0 被 vLLM 占满
GPU 2 (1.5B s123): PID=214660 [已死] — 同上 OOM 失败，也试图加载到 GPU 0
GPU 3 (3B s123): [已死] — 同上 OOM 失败

GPU 4 (1.5B s42): PID=210121 [训练中], step 1825/3125 (58%), elapsed 58min, ~46min remaining
GPU 5 (3B s42): PID=210671 [训练中], step 824/3125 (26%), elapsed 54min, ~2h38m remaining

全 GPU utilization:
GPU 0: 100%  23077/24564 MiB  — vLLM MMLU paraphrase (PID 204758)
GPU 1:   0%      0/24564 MiB  — 空闲
GPU 2:   0%      0/24564 MiB  — 空闲
GPU 3:   0%      0/24564 MiB  — 空闲
GPU 4:  66%  21561/24564 MiB  — 1.5B s42 训练 (PID 210121)
GPU 5:  41%  18663/24564 MiB  — 3B s42 训练 (PID 210671)
```

**问题**: 三个 s123 训练全部 OOM 崩溃——它们都试图加载到 GPU 0（被 vLLM 占满 22.5GB）。启动时 `--gpu` 参数可能指定了错误的 GPU，或者默认 fallback 到了 GPU 0。GPU 1/2/3 当前完全空闲，可以重新提交 s123 到这三块卡上。

---
