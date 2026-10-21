# ops check uncommitted changes

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-uncommitted-changes_20260516T013938_result.json`
- **Structured JSON:** [`a214a3e3748e3293bea1.json`](../../sessions/a2/a214a3e3748e3293bea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析报告

**HEAD 确认**: `06ab285 Fix Full-SGS: restore dt_emb.weight.requires_grad_(True) after imagination` ✓

### 未提交改动内容

这些改动 **不是** 06ab285 Full-SGS bugfix 的一部分，是独立的未提交修改，分两类：

#### 1. dreamer.py — 环境/渲染相关
- **osmesa → egl**：渲染后端从 `osmesa` 切到 `egl`（GPU 渲染，AutoDL 上更合理）
- **新增 maniskill 环境支持**：`make_env()` 加了 `maniskill` suite 分支，与当前实验无关

#### 2. tools.py — Video deadlock 修复 + 调试代码
- **`Logger.video()` 方法体替换为 `pass`**：直接禁用 video 记录
- **`add_video()` 包了 try/except**：即使 video 方法被调到也不会崩
- **`logger.video("eval_policy", ...)` 注释掉**：标注 "moviepy corruption causes add_video deadlock (D056)"
- **simulate() 加了调试计数器**：每 100 iter 打印进度，**超过 5000 iter 时 eval 强制 abort**

### 对 exp_018 的影响评估

| 改动 | 影响 | 风险 |
|------|------|------|
| osmesa→egl | 无影响，AutoDL GPU 支持 egl | 低 |
| maniskill env | 不触发（018 不用 maniskill） | 无 |
| video 禁用 | **正面**——避免 moviepy deadlock 卡死训练 | 无 |
| **eval abort at 5000 iters** | **潜在风险**——如果单次 eval episode 合法超过 5000 步，会被截断导致 eval 指标偏低 | **中** |

### 结论

**关键风险点**：`tools.py` 中 `_dbg_iter > 5000` 的 eval abort 是调试用的安全阀。如果 018 的 eval episode 步数在 5000 以内（通常 DM Control 任务 time_limit=1000），则无影响。但这段调试代码不应留在正式实验中。

**建议**：
1. Video deadlock fix（D056）是有价值的，应该提交
2. `_dbg_iter` 调试代码和 `import time` 应在 018 启动前清理掉，或至少确认 018 的 eval 不会触发 5000 上限
3. maniskill 和 egl 改动可以一并提交，不影响 018

---
