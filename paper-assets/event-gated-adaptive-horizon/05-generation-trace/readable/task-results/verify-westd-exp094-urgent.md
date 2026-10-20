# verify westd exp094 urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd_exp094_urgent_20260525T232729_result.json`
- **Structured JSON:** [`e8de2d64429ecfc40705.json`](../../sessions/e8/e8de2d64429ecfc40705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### PID 存活状态

| PID | 实验 | 状态 |
|-----|------|------|
| 53576 | exp_094_cheetah_008d_s3 (wrapper bash) | **存活** |
| 53581 | exp_094_cheetah_008d_s3 (python dreamer.py) | **存活** |
| 54457 | exp_095_cheetah_008a_s0 (wrapper bash) | **存活** |
| 54462 | exp_095_cheetah_008a_s0 (python dreamer.py) | **存活** |
| 54119 | exp_095_cheetah_no_dt_emb_s3 (wrapper bash) | **存活** |
| 54124 | exp_095_cheetah_no_dt_emb_s3 (python dreamer.py) | **存活** |

### Tmux Sessions

3 个 session 全部存在：
- `exp_094_cheetah_008d_s3` (created 06:57)
- `exp_095_cheetah_no_dt_emb_s3` (created 07:03)
- `exp_095_cheetah_008a_s0` (created 07:05)

### GPU 进程分布

| GPU | 进程 PID | 实验 | 显存占用 |
|-----|----------|------|----------|
| **cuda:0** (GPU-c252) | 54462 | exp_095_cheetah_008a_s0 | 4637 MiB |
| **cuda:1** (GPU-d446) | 53581 | **exp_094_cheetah_008d_s3** | 3223 MiB |
| **cuda:1** (GPU-d446) | 54124 | exp_095_cheetah_no_dt_emb_s3 | 3223 MiB |

### 结论

- **exp_094 (PID 53576/53581) 仍然在 cuda:1 上运行**，占用 3223 MiB。它与 exp_095_cheetah_no_dt_emb_s3 共享 cuda:1（两者各占 ~3.2GB，总计 6.4GB / 97.9GB，资源充裕）。
- cuda:0 只有 exp_095_cheetah_008a_s0 一个实验。
- 三个实验全部正常运行中，无异常。

---
