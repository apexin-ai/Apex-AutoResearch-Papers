# ssh check processes

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-processes_20260521T231728_result.json`
- **Structured JSON:** [`d0216faa346ef218a013.json`](../../sessions/d0/d0216faa346ef218a013.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

| 实验 | PID | 状态 | 详情 |
|------|-----|------|------|
| **exp_014b** (r=0.25, seed43) | 577216 | **已完成** | 进程已退出，EXIT_CODE=0。10 代全部跑完，results JSON 已生成 (6079 bytes, May 22 06:24) |
| **exp_015** (r=0.25, seed44) | 516824 | **运行中** | 已运行 13h15m，当前在 **Generation 7/10** 的评估阶段（distinct-4 生成中）。results JSON 已存在 (3839 bytes, May 22 06:10)——可能是之前某次运行的残留 |
| **exp_016** (r=0.3, seed44) | 614614 | **运行中** | 已运行 1h36m，当前在 **Generation 0** 的评估阶段（刚启动，正在做 baseline 评估）。results JSON 尚未生成 |

**GPU 占用：**
- cuda:0 — PID 614619 (exp_016 子进程), 19036 MiB
- cuda:1 — PID 516836 (exp_015 子进程), 25008 MiB

**磁盘：** /root/autodl-tmp 250G，已用 163G，剩余 **88G (34%)**，空间充足。

---
