# ops post restart gpu check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_gpu_check_20260516T051659_result.json`
- **Structured JSON:** [`402910a860a6f4339a9c.json`](../../sessions/40/402910a860a6f4339a9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器 westd-22162 状态总结

### GPU 状态

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 73.3/97.9 GB | 76% | c8 importance s025 profiling |
| 1 | 15.5/97.9 GB | 72% | c10 lang s020+s025 生成 |
| 2 | 73.3/97.9 GB | 100% | c8 main Round 1 (s015) |
| 3 | 73.3/97.9 GB | 100% | c8 main Round 1 (s020) |

### 进程状态

| PID | 任务 | 状态 | 运行时间 | 进度 | 预估剩余 |
|-----|------|------|---------|------|----------|
| **315052** | c8 GPU0 s025 importance | Running | 1h12m | 56/250 (22%) | ~4h |
| **310712** | c8 main (GPU 2+3) | Running | 1h56m | Round 1/4 (s015+s020), 输出目录为空 | ~16-20h（4轮串行） |
| **312143** | c10 s020/s025 gen | Running | 1h38m | 31/50 (62%) | ~1h |
| **318170** | 14B 模型下载 | Running | 27m | shard 8/8: 99%, shard 5/8: 62%, 仅1个shard落盘 | ~30-60min |
| **317541** | s030 chain monitor | Waiting | 38m | 等 s025 (PID 315052) 完成 | 跟随 s025 |
| **316993** | s025 guardian | Watching | 47m | 监控 GPU0 正常 | 跟随 s025 |
| **317716** | s030 guardian | Watching | 35m | 监控 chain 正常 | 跟随 chain |

### Sentinel 状态
- **s025**: placeholder（GPU 0 尚未写入真实结果）
- **s030**: placeholder（等待 chain 触发）

### 磁盘
`/root/autodl-tmp`: 106G/250G used, **145G 可用**

### 要点
1. **全部 7 个进程存活**，服务器重启未影响任何任务
2. c10 最快完成（~1h 后），可释放 GPU 1
3. 14B 下载接近完成，但速度慢（~2MB/s），多数 shard 尚未落盘
4. c8 main 是最耗时任务——4 轮串行×250 题×2 GPU，预计还需 16-20h
5. GPU 0 的 s025 完成后会自动触发 s030 chain

---
