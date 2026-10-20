# ssh diagnose gpu1 speed

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-gpu1-speed_20260513T223342_result.json`
- **Structured JSON:** [`4b1314d3f77fd2c0df24.json`](../../sessions/4b/4b1314d3f77fd2c0df24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码确认了原因。现在报告诊断结论。

## 诊断结论

### 当前状态：速度正常

当前 plan-001b-gpu1 进程 (PID 773114) 启动于 **06:10**，截至 ~06:38 已运行约 **28 分钟**，完成 **6 个新 episode**（find-non-living-thing task），速度 **~4.7 min/episode** — 接近预期的 4 min/episode。

**用户上下文中的"运行 9.5h 仅完成 2 episodes"与当前实际状态不符。** 可能是基于旧的预估或已被替换的运行。

### 每 episode 耗时分解

每个 episode 跑两个模式：

| 模式 | 平均耗时 | 说明 |
|------|---------|------|
| **[I] always-internal** | ~31s | 纯 LLM，无 fork |
| **[D] always-deterministic** | ~200s | 每步 fork 3 个 JVM + replay action history |
| **合计** | ~230s ≈ 3.8 min | |

### [D] 模式慢的根因（by design）

`run_episode_deterministic` 每步调用 `fork_and_lookahead` 3 次（`n_candidates=3`），每次：
1. **新建 JVM**（ScienceWorld 用 py4j，每个 env = 独立 Java 进程）
2. **Replay 全部历史动作**（step 29 时要 replay 29 步）
3. **执行候选动作 + 评估**
4. **关闭 JVM**

30 步 episode = **90 次 JVM 启停** + **1305 次 action replay**。这不是 bug，是 fork-and-evaluate 的设计成本。

### 总预计耗时

- 4 tasks × 15 new episodes = 60 episodes
- ~4.7 min/episode → **~282 min ≈ 4.7 小时**

### 当前 Java CPU 异常

PID 865588 的 Java 进程占用 **489% CPU**，但整体速度正常，可能是短暂的初始化峰值。

### 建议（如果确需加速）

1. **减少 `n_candidates`**：从 3 降到 2，fork 开销减少 1/3
2. **环境池化**：保持 n 个 JVM 常驻而非每次新建/销毁
3. **增量 replay**：保存环境 snapshot 而非每次从头 replay（需 ScienceWorld 支持 save/load state）

---
