# ops c10 c8 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c10_c8_progress_check_20260516T042155_result.json`
- **Structured JSON:** [`c6cc8c5bfb2f254e337f.json`](../../sessions/c6/c6cc8c5bfb2f254e337f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
c10 状态: RUNNING
c10 进度: 20/50 (Problem 20，正在处理 s020 生成)
c10 输出文件: 不存在（未完成）
c10 GPU: GPU 0, 56321MiB/97887MiB, 79% util (PID 315057)

c8 状态: RUNNING
c8 Round: 1/4
c8 当前条件: importance_s015 (GPU 2) + importance_s020 (GPU 3)
c8 已完成条件:
  - dryrun: ✅ (profiling_results.json 存在)
  - importance_s015: ⏳ 目录存在但为空，正在运行
  - importance_s020: ⏳ 目录存在但为空，正在运行
  - importance_s025: ⏳ 目录存在但为空（等待后续 round）
c8 启动时间: 11:20:55, 已运行 ~1h

GPU 利用:
  GPU 0: 56321MiB / 97887MiB, 79%  (c10 lang)
  GPU 1: 15557MiB / 97887MiB, 73%  (其他进程 PID 312143)
  GPU 2: 73273MiB / 97887MiB, 100% (c8 s015)
  GPU 3: 73273MiB / 97887MiB, 77%  (c8 s020)
```

c10 每个 problem 约 175s×2 条件 ≈ 6min，剩 30 个 problem 预计还需 ~3h。c8 Round 1 的两个条件还没产出文件，4 个 round 总计预计较长。

---
