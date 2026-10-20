# ssh check eval status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-status_20260516T151429_result.json`
- **Structured JSON:** [`d7db91e16cc197e6ade5.json`](../../sessions/d7/d7db91e16cc197e6ade5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 使用

| GPU | 显存占用 | 利用率 | 当前任务 |
|-----|---------|--------|---------|
| 0 | 16.8/32.6 GB | 75% | llama31-taxei-s123 injected eval |
| 1 | 16.8/32.6 GB | 53% | llama31-random-s123 injected eval (刚启动) |
| 2 | 16.8/32.6 GB | 0% | llama31-taxei-s123 clean eval (CPU 阶段) |
| 3 | 16.8/32.6 GB | 90% | llama31-random-s123 clean eval |

### Eval 进程状态

| 任务 | 状态 | GPU | 备注 |
|------|------|-----|------|
| llama31-vanilla-s123-eval | **已完成** | — | 产出: `llama31_vanilla_s123_injected.json` (23:13) + `llama31_vanilla_s123_clean.json` (22:35) |
| llama31-taxei-s123 injected | **运行中** | cuda:0 | PID 293496, 已跑 ~8 min |
| llama31-taxei-s123 clean | **运行中** | cuda:2 | PID 291995, 已跑 ~12 min |
| llama31-random-s123 injected | **运行中** | cuda:1 | PID 294869, 刚启动 ~1 min (队列等 vanilla 完后触发) |
| llama31-random-s123 clean | **运行中** | cuda:3 | PID 292353, 已跑 ~12 min |

### Scale-up 数据收集
- PID 266813: **已完成**
- `/data/scale_up/` 目录不存在——数据可能输出到了其他路径

### Tmux
- 无活跃 tmux sessions（所有 eval 通过 nohup 后台运行）

### 总结
4 个 s123 eval 中，vanilla 已完成，另外 4 个进程（taxei injected/clean + random injected/clean）正在 4 张 GPU 上全速运行，预计 10-20 分钟内全部完成。

---
