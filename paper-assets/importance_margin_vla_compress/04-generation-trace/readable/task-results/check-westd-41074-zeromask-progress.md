# check westd 41074 zeromask progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-41074-zeromask-progress_20260525T220449_result.json`
- **Structured JSON:** [`c8964f8a751335eb2e0f.json`](../../sessions/c8/c8964f8a751335eb2e0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU0: random_k05_object_v2     — Task 4/10, Ep 30/50, elapsed ~3.7h, ETA ~3.1h
GPU1: l2norm_k05_object_v2     — Task 4/10, Ep  0/50, elapsed ~3.7h, ETA ~3.9h
GPU2: zeromask_random_k09      — Task 9/10, Ep 40/50, elapsed ~3.7h, ETA ~0.5h
GPU3: zeromask_l2norm_k09      — Task 9/10, Ep 20/50, elapsed ~3.7h, ETA ~0.7h
```

备注：
- Zeromask 两个实验即将完成（30-40 分钟内）。日志输出在 `/tmp/` 而非 `~/runs/`（`~/runs/` 下的 log 是 0 字节空文件）。
- k=0.5 实验进度约 36%/30%，预计还需 3-4 小时。
- Zeromask 中间结果：random 当前累计 SR 偏低（task7=50%, task8=74%）；l2norm 表现更好（task7=62%, task8=82%）。

---
