# ssh ram monitor 3parallel

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ram-monitor-3parallel_20260520T012313_result.json`
- **Structured JSON:** [`4ed4db690a02e69fa14b.json`](../../sessions/4e/4ed4db690a02e69fa14b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**关键发现：用户提供的 3 个 PID 全部不存在。DeepSeek 训练未在运行。**

## 即时快照结果

### RAM
- cgroup memory.current = **76.2 GiB** (81,791,193,088 bytes)
- **SAFE**: 76.2 GiB << 300 GiB 阈值 (360 GiB 上限的 21%)

### GPU 状态
| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 99% | 21253/32607 MiB | PID 881323 — Qwen CWM s123 |
| 1 | 100% | 0 MiB | 无进程 (异常，可能是驱动残留) |
| 2 | 0% | 0 MiB | **无进程 — DeepSeek 未启动/已退出** |
| 3 | 98% | 31259/32607 MiB | PID 881465 — Qwen CWM s456 |

### PID 存活状态
| 你给的 PID | 状态 |
|-----------|------|
| 882967 (Qwen s123) | **已死** — 实际运行的是 PID 881323 |
| 883043 (Qwen s456) | **已死** — 实际运行的是 PID 881465 |
| 885231 (DeepSeek s123) | **已死** — GPU 2 空闲，无任何 DeepSeek 进程 |

### 结论
- **RAM: SAFE** — 仅 76.2 GiB，只有 2 个训练在跑
- **实际只有 2 并行**（Qwen s123 + Qwen s456），不是 3 并行
- **DeepSeek CWM s123 训练需要重新启动**，GPU 2 完全空闲
- GPU 1 显示 100% 利用率但 0 MiB 显存、无进程，建议关注

后台监控脚本还在跑但监控的 PID 已无意义，会自行结束。需要我帮重新启动 DeepSeek 训练吗？

---
