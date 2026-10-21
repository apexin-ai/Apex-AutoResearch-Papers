# ops verify experiments post restart

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-experiments-post-restart_20260527T133711_result.json`
- **Structured JSON:** [`97534e6d3449cced3fa1.json`](../../sessions/97/97534e6d3449cced3fa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. 进程存活 ✓

| 实验 | PID | 运行时长 | GPU 进程 PID | GPU 显存 |
|------|-----|---------|-------------|---------|
| exp_walker_no_dt_emb_s1 | 629189 | 2h 19m 46s | 629201 (GPU 0) | 3,257 MiB |
| exp_cheetah_008a_s1 | 629903 | 2h 08m 40s | 629908 (GPU 1) | 4,671 MiB |

GPU 总占用：GPU 0 = 52,448 / 97,887 MiB (13%), GPU 1 = 4,690 / 97,887 MiB (20%)

### 2. 训练进度

| 实验 | 当前步数 | 目标 | 进度 | 关键指标 |
|------|---------|------|------|---------|
| Walker no_dt_emb s1 | **85,000** | 105,000 | 81% | eval_return=303.2, fps=9.66 |
| Cheetah 008a s1 | **88,000** | 105,000 | 84% | train_return≈476~546 |

### 3. 预计完成时间

- **Walker**: 剩余 20,000 步, fps=9.66 → ~2,070s ≈ **35 分钟后** (~22:17 UTC)
- **Cheetah**: 剩余 17,000 步, 按运行时长估算 fps≈11.4 → ~1,490s ≈ **25 分钟后** (~22:07 UTC)

### 4. tmux session ✓
- `exp_walker_no_dt_emb_s1` — created 19:17:56
- `exp_cheetah_008a_s1` — created 19:29:03

### 5. cron 监控
**无 cron/poll 进程运行。** 服务器重启后 cron 监控未自动恢复。

### 结论

两个实验均存活且正常推进，预计 **30-35 分钟内全部完成**。唯一异常：cron 监控进程未恢复，但不影响训练本身。

---
