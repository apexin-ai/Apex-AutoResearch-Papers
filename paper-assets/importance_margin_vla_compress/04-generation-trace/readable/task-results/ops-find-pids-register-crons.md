# ops find pids register crons

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find-pids-register-crons_20260527T130601_result.json`
- **Structured JSON:** [`b4cb8828a9d0db30670d.json`](../../sessions/b4/b4cb8828a9d0db30670d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 目标实验 PID

```
exp_id                                        | server       | pid    | tmux_session
----------------------------------------------|--------------|--------|-------------
eval_pi05_l2norm_k07_long_seed42_strict       | cqa1-33015   | 274739 | N/A (nohup)
eval_pi05_random_k05_long_seed42_strict (cron)| cqa1-33015   | 118726 | NOT_RUNNING
eval_pi05_l2norm_k05_long_seed42_strict       | westd-38929  | 250745 | N/A (nohup)
eval_pi05_attn_k07_long_seed42_strict_w41     | westd-41074  | 608185 | N/A (tee)
eval_pi05_attn_k095_long_seed42_strict_w41_v2 | westd-41074  | NOT_FOUND | —
eval_pi05_random_k09_long_seed43_strict_w41   | westd-41074  | 610959 | N/A (tee)
```

### 各服务器全部 eval 进程

**cqa1-33015** (4 python + 1 tmux):

| python PID | 实验 | GPU |
|---|---|---|
| 200112 | pi05 l2norm k=0.9 long seed42 | 3 |
| 274739 | pi05 l2norm k=0.7 long seed42 | 2 |
| 300492 | pi05 attn k=0.75 long seed42 | 0 |
| 328563 | pi05 attn k=0.7 long seed42 | 1 |
| 895663 (tmux) | openvla random k=0.95 goal | 0 |

**westd-38929** (4 python + 1 tmux):

| python PID | 实验 | GPU |
|---|---|---|
| 250745 | pi05 l2norm k=0.5 long seed42 | 3 |
| 266221 | openvla attn k=0.75 long seed42 v3 | 1 |
| 272022 | openvla random k=0.95 long seed42 v3 | 0 |
| 968309 | openvla l2norm k=0.75 long seed42 v2 | 2 |
| 6805 (tmux) | openvla attn k=0.7 long seed42 v2 | 0 |

**westd-41074** (5 python + 1 tmux):

| python PID | 实验 | GPU |
|---|---|---|
| 547488 | pi05 attn k=0.5 long seed42 | 1 |
| 561220 | pi05 attn k=0.75 long seed42 | 0 |
| 568159 | pi05 attn k=0.75 long seed42 (agent-ml wrapped) | 0 |
| 608185 | pi05 attn k=0.7 long seed42 | 3 |
| 610959 | pi05 random k=0.9 long seed43 | 2 |
| 3977 (tmux) | openvla random k=0.5 object seed42 v2 | 0 |

注：`tmux ls` 被 ssh_read_only 白名单拦截，tmux session 名从 `/proc/PID/cmdline` 中提取。`eval_pi05_attn_k095_long_seed42_strict_w41_v2` 在 westd-41074 上无任何匹配进程（已搜索 `0.95` 关键字确认）。PID 118726 在 cqa1 上已不存在。

---
