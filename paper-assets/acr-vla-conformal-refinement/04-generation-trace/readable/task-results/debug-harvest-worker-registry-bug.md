# debug harvest worker registry bug

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_harvest-worker-registry-bug_20260524T234456_result.json`
- **Structured JSON:** [`61e9fb08aefedce4c3eb.json`](../../sessions/61/61e9fb08aefedce4c3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因分析完成。结论与用户假设相反——**不是 worker bug，是 Director 误判 + 任务约束**。

## 根因分析

### 1. Worker 有 update_registry 工具（排除假设 a）

三个 worker 的 system init 都包含 `mcp__agent-ml-research__update_registry`，Director 的 spawn_worker 调用都传了 `tool_groups: ['ssh', 'registry']`。**工具权限没问题。**

### 2. Worker 行为符合 prompt 指令（排除假设 b/c/e）

三个 task_prompt 都明确说了：
- "对每个**已完成的**实验：update_registry(...)"
- vla-only-results 还额外说："对于仍在运行的实验：**报告剩余进度**"（不写回 registry）

Worker 完整跑了 SSH 检查 → 读日志 → 统计 task 完成数，**显式得出"实验仍在运行"的结论**，然后按 prompt 跳过 update_registry。两个 worker 的原话：
- vla-baselines: "不需要更新 registry，等实验跑完再收割"
- vla-only-results 内部 think: "I'll share these results with the user once any experiments finish and I can update the registry"

### 3. 真正的根因：Director 的 spawn 前提是错的（假设 d 的变种）

Director 在 spawn 时基于"GPU 空闲 ⇒ 实验已完成"做判断：
- vla-baselines prompt: "5 个 VLA-only baseline 实验标记为 RUNNING，**但资源检查显示该服务器 GPU 全部空闲，说明实验已完成**"
- cqa1-baselines prompt: "6 个 VLA-only baseline 实验标记为 RUNNING，**但资源检查显示无实验在跑，说明已完成**"

但 worker SSH 进去看到：所有 python 进程 `Rl+` 状态、CPU 360-820%、tmux session 全在、日志在持续追加，**实验远未完成**（很多 3-5/10 task）。worker 自己识破了这个陷阱："GPU 仅在推理时短暂占用，大部分时间在 CPU 上做 LIBERO 仿真"——LIBERO simulator 是 CPU-heavy 的，GPU 利用率瞬时采样不可靠。

bjb1 的实验 04:18 才启动（worker 检查时只跑了 ~46-55 分钟），cqa1 的跑了 16 小时但 task 完成数只到 5/10——都是正常进行中。

## 修复建议

### Priority 1: 修 Director 的诊断逻辑
**不要再用 `nvidia-smi` 单点采样判断"实验是否完成"。** Director 在 spawn harvest worker 之前必须先用 `ssh_read_only` 执行 `ps -ef` 看进程，或 `find logs/ -mmin -5` 看日志是否还在更新。LIBERO/robosuite 类 CPU-heavy 仿真根本不应该看 GPU 利用率。

### Priority 2: 调整 harvest worker 的契约
当前契约是"完成才写 registry，运行中只口头报告"，导致 registry 里的 RUNNING 状态在多次错误 harvest 后仍保持 stale。建议在 spawn_worker 的 task_prompt 里加一条：
> 如果发现实验**仍在运行**，调用 `update_registry(exp_id, "progress", {"tasks_done": N, "tasks_total": 10, "checked_at": "..."})` 留痕，便于下次决策。**但不要把 status 改成 DONE。**

### Priority 3: 不需要改 skill / agent 行为
worker 端没问题、tool_groups 没问题。问题完全在 Director 的"何时该 harvest"决策。可以把这条规则沉淀进 Director 的 CLAUDE.md 或 memory：

> **判断实验是否完成的优先级**：`ps aux | grep evaluate`（最权威） > 日志 mtime > tmux session 存在 > GPU 利用率（**最不可靠**，CPU-heavy 仿真会让 GPU 闲置）

要不要我把这条经验直接写进 project memory？

---
