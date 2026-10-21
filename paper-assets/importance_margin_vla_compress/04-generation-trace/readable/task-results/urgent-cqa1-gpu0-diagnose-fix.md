# urgent cqa1 gpu0 diagnose fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cqa1-gpu0-diagnose-fix_20260526T221627_result.json`
- **Structured JSON:** [`c3df57b1b10b0905a48a.json`](../../sessions/c3/c3df57b1b10b0905a48a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程确认存活：PID 790017，CPU 642%，正在加载模型到内存（4.5GB RSS），尚未传到 GPU。一切正常。

汇总：

```
GPU 0: 已完成（非卡死）PID 617566 已退出，L2norm k=0.7 SR=63.2%，GPU 空闲
GPU 1: 在跑 PID=617728 显存=10378MiB GPU-util=23%
GPU 2: 新部署 L2norm k=0.85 PID=790017 模型加载中（CPU阶段），tmux session=pi05_l2norm_k085_long
GPU 3: 在跑 PID=732826 Random k=0.7 elapsed=01:27:21 显存=10162MiB GPU-util=22%
```

GPU 0 现在空闲，可以安排下一个任务。

---
