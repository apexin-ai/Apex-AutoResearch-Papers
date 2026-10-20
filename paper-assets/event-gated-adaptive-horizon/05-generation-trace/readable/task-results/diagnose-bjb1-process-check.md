# diagnose bjb1 process check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-process-check_20260526T021330_result.json`
- **Structured JSON:** [`7483fe7a7274dc9f67d3.json`](../../sessions/74/7483fe7a7274dc9f67d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总 — bjb1-45299

### GPU 使用
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|----------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 5215/97887 MiB (5%) | 20% | exp_098 (PID 322491) |
| 1 | RTX PRO 6000 Blackwell | 4165/97887 MiB (4%) | 23% | exp_099 (PID 322772) |

### 正在运行的实验
| 实验 | 任务 | 配置 | 当前 step | 目标 steps | 启动时间 | seed |
|------|------|------|-----------|-----------|----------|------|
| exp_098_cheetah_008a_s0 | dmc_cheetah_run | gate_fixed_dt=2, imag_horizon=15 | **8000** | 105000 | 今天 10:04 | 0 |
| exp_099_cheetah_008a_s1 | dmc_cheetah_run | gate_fixed_dt=2, imag_horizon=15 | **8000** | 105000 | 今天 10:04 | 1 |

进度：~7.6%，刚完成第一轮 eval（step 5000, eval_return 8.3 / 13.5）。

### Tmux Sessions
`tmux ls` 被 read-only 工具阻止，但从 `ps aux` 可见两个 tmux session：
- `exp_098_cheetah_008a_s0`
- `exp_099_cheetah_008a_s1`

### exp_088+ 实验目录
logdir 中不存在 exp_088/089。存在的 exp_088+ 目录：
- `exp_092_cheetah_no_dt_emb_s1` — 最后修改 May 26 07:10
- `exp_093_cheetah_no_dt_emb_s2` — 最后修改 May 26 07:10
- `exp_098_cheetah_008a_s0` — 活跃运行中
- `exp_099_cheetah_008a_s1` — 活跃运行中

exp_094–097 不存在于此服务器。

### 结论
Handoff 信息正确：exp_098/099 确实在 bjb1-45299 上运行（cuda:0/1），刚启动约1.5小时，step 8000/105000。Registry 中缺失这两条记录需要补上。

---
