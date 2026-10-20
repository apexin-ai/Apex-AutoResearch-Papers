# diagnose westd full status 20260526

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_full_status_20260526_20260526T001105_result.json`
- **Structured JSON:** [`bd06c202aa0029a33631.json`](../../sessions/bd/bd06c202aa0029a33631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-19154 GPU 状态

| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 Blackwell | 4,656 MiB / 97,887 MiB (5%) | 43% | PID 54462 (exp_096_008a_s0) |
| 1 | RTX PRO 6000 Blackwell | 6,480 MiB / 97,887 MiB (7%) | 68% | PID 53581 (exp_094_008d_s3), PID 54124 (exp_095_no_dt_emb_s3) |

## 实验进度

| exp_id | PID | Step/Total | eval_return (latest) | FPS |
|--------|-----|-----------|---------------------|-----|
| exp_094_cheetah_008d_s3 | 53581 | ~48K / 105K (46%) | 23.39 @ 45K | 9.84 |
| exp_095_cheetah_no_dt_emb_s3 | 54124 | ~45K / 105K (43%) | 149.57 @ 35K | 9.79 |
| exp_096_cheetah_008a_s0 | 54462 | ~56K / 105K (53%) | 85.00 @ 55K | 13.17 |

备注：
- exp_094 eval_return 在下降（216→139→105→23），表现异常
- exp_095_no_dt_emb eval_return 在上升（8→33→50→150），趋势良好
- exp_096_008a eval_return 在 25K 后震荡（120→136→84→85）

## tmux sessions

| Session | 创建时间 |
|---------|---------|
| exp_094_cheetah_008d_s3 | May 26 06:57 |
| exp_095_cheetah_008a_s0 | May 26 07:05 |
| exp_095_cheetah_no_dt_emb_s3 | May 26 07:03 |

3 个 session，均活跃，与 3 个实验一一对应。

## 磁盘

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (根分区) | 30G | 979M | 30G | 4% |
| /root/autodl-tmp | 350G | 9.1G | 341G | 3% |

磁盘充裕，无压力。

---
