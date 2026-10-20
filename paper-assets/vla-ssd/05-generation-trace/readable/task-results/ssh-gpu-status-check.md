# ssh gpu status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-check_20260515T171110_result.json`
- **Structured JSON:** [`851fbfee4e80ee9b5da2.json`](../../sessions/85/851fbfee4e80ee9b5da2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black (96GB) | 16,375 / 97,887 MiB | 95% | 69°C |
| 1 | RTX PRO 6000 Black (96GB) | 16,373 / 97,887 MiB | 0% | 65°C |

## tmux

`tmux ls` 被 read-only 模式拦截，无法执行。

## 进程状态

PID 627256 和 627335 均存活，运行时间 ~26 分钟。

```
PID     PPID  CMD                              ELAPSED
627256  627255  python /root/vla-ssd/script       26:15
627335  627334  python /root/vla-ssd/script       26:13
```

## 特征提取进度

**trained_libero_goal** — 5/10 完成，第 5 个正在提取：

| # | 任务 | 大小 | 状态 |
|---|------|------|------|
| 1 | open_the_middle_drawer_of_the_cabinet | 2.90 GB | 完成 |
| 2 | open_the_top_drawer_and_put_the_bowl_inside | 4.21 GB | 完成 |
| 3 | push_the_plate_to_the_front_of_the_stove | 3.15 GB | 完成 |
| 4 | put_the_bowl_on_the_plate | 1.93 GB | 完成 |
| 5 | put_the_bowl_on_the_stove | 0.93 GB (写入中) | **进行中** ~46% (2357/5081) |

**untrained_libero_goal** — 4/10 完成，第 4 个正在提取：

| # | 任务 | 大小 | 状态 |
|---|------|------|------|
| 1 | open_the_middle_drawer_of_the_cabinet | 2.91 GB | 完成 |
| 2 | open_the_top_drawer_and_put_the_bowl_inside | 4.22 GB | 完成 |
| 3 | push_the_plate_to_the_front_of_the_stove | 3.16 GB | 完成 |
| 4 | put_the_bowl_on_the_plate | 1.50 GB (写入中) | **进行中** ~79% (3711/4669) |

## 日志尾部

**trained** (GPU 0): 正在提取 `put_the_bowl_on_the_stove`，进度 ~46%，速度 ~40 step/s

**untrained** (GPU 1): 正在提取 `put_the_bowl_on_the_plate`，进度 ~79%，速度 ~38 step/s

---
