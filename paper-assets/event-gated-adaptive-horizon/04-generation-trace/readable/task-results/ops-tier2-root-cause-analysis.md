# ops tier2 root cause analysis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tier2-root-cause-analysis_20260528T000308_result.json`
- **Structured JSON:** [`9489ef922b87d999a705.json`](../../sessions/94/9489ef922b87d999a705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 根因排查报告

### 时间线

| 实验 | 启动 | 死亡 | 持续 | 最终状态 |
|------|------|------|------|---------|
| s6 (首次) | 07:09:16 | 07:20:15 | 11min | `Terminated` EXIT_CODE=143 (SIGTERM，手动杀) |
| s7 (首次) | 07:09:27 | 07:20:16 | 11min | `Terminated` EXIT_CODE=143 (SIGTERM，手动杀) |
| **s6_r2** | 07:25:09 | **07:42:39** | 17min | **无错误输出，无退出码，静默消失** |
| **s7_r2** | 07:25:17 | **07:42:46** | 17min | **无错误输出，无退出码，静默消失** |

两个 r2 进程死亡时差 = 7 秒，与启动时差 (8 秒) 几乎一致。

### 排除项

| 检查项 | 结果 | 排除？ |
|--------|------|--------|
| GPU OOM | 2× RTX PRO 6000 94GB，DreamerV3 MLP-only ~2-3GB | ✅ 排除 |
| 系统 RAM OOM | 1TB 总量，仅用 83GB | ✅ 排除 |
| 磁盘满 | 250GB 仅用 7.9GB (4%) | ✅ 排除 |
| 外部杀进程 | 死亡时差 7s（非同时），与启动偏移一致 | ✅ 基本排除 |

### 根因判定：eval 阶段确定性崩溃 + stderr 未捕获

**关键证据：**

1. **两个进程都停在完全相同的位置**：`[15000] Start evaluation.` 后进入 `tools.simulate()` eval 调用时死亡
2. **死亡时差 = 启动时差** → 不是外部 kill，是代码路径上的确定性 bug
3. **无任何错误输出** → nohup 启动时没有 `2>&1`，stderr（Python traceback）被丢弃
4. **logdir 完全不存在** → 整个文件系统搜索无 `exp_walker_008d_s6_r2` 目录。checkpoint 从未保存或已被清理
5. step 5000 的 eval 成功通过，step 15000 的 eval 崩溃 → 问题可能与 agent 训练后的行为变化或 eval episode 交互相关

**最可能的崩溃点**：`tools.simulate()` 中的 eval 环境交互，可能是 MuJoCo/Gym `Parallel(env, "process")` 子进程崩溃（EGL 渲染错误、MuJoCo 段错误）导致主进程异常退出。

### 建议

1. **重跑时加 `2>&1` 和 `PYTHONUNBUFFERED=1`** — 捕获 stderr 才能看到真正的 traceback
2. **先跑单卡单进程** — 排除并发因素
3. **启动命令改为**：
   ```bash
   PYTHONUNBUFFERED=1 nohup python dreamer.py ... > /root/runs/.../exp_walker_008d_s6_r3.log 2>&1 &
   ```

15K 步训练数据已全部丢失（无 checkpoint），需要从头重跑。

---
