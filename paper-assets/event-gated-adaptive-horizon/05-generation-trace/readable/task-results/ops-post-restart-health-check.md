# ops post restart health check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-health-check_20260518T162916_result.json`
- **Structured JSON:** [`a2fb9c456855f345a22d.json`](../../sessions/a2/a2fb9c456855f345a22d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验正常运行，汇总如下：

```
实验ID                              | 进程状态 | 当前步数 | 目标步数 | GPU卡号
------------------------------------|----------|----------|----------|--------
exp_008a_cheetah_unexposed_s0       | ✅ 运行中 | 76K      | 105K     | cuda:0
exp_008a_cheetah_unexposed_s1       | ✅ 运行中 | 80K      | 105K     | cuda:1
exp_023_cheetah_baseline_s2         | ✅ 运行中 | 12K      | 105K     | cuda:0
exp_008f_s2 (no_dt_emb)             | ✅ 运行中 | 8K       | 105K     | cuda:0
exp_001_baseline_s2                 | ✅ 运行中 | 12K      | 105K     | cuda:1
exp_009c_s2 (no_dt_emb)             | ✅ 运行中 | 8K       | 105K     | cuda:1
```

**GPU 状态：**
- GPU 0: 3 进程，13.2GB/97.9GB，利用率 99%，43°C
- GPU 1: 3 进程，12.1GB/97.9GB，利用率 100%，46°C

**进展对比：**
- Cheetah unexposed s0: 72K → 76K（+4K 步）
- Cheetah unexposed s1: 76K → 80K（+4K 步）
- 其余 4 个为新启动实验，均处于早期训练阶段（8K-12K 步）

无异常，全部正常推进。

---
