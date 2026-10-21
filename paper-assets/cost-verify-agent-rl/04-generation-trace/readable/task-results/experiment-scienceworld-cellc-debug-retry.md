# experiment scienceworld cellc debug retry

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_scienceworld-cellc-debug-retry_20260520T153530_result.json`
- **Structured JSON:** [`44a9588b6226c8bdcd0b.json`](../../sessions/44/44a9588b6226c8bdcd0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在初始化中。

---

**产出总结**：

### 1. 崩溃 Root Cause
- **py4j JVM 死亡**：ScienceWorld 通过 py4j 桥接 Python↔Java（Scala）。Cell C step 1 完成后，step 2 rollout 运行约 2 小时后 JVM 进程死亡（推测原因：默认 JVM 堆不足 + 128 episodes 反复 `load()`/`reset()` 累积 GC 压力），导致 `Py4JNetworkError: Exception while sending command`
- **无重连机制**：原 wrapper 的 `_get_cached_env()` 按 thread ID 缓存 JVM 实例，JVM 死后返回 stale 连接，py4j 重试一次也失败，训练直接崩溃
- 不是系统 OOM（1TB RAM，仅用 52GB），无 JVM crash dump（`hs_err_pid*`），无 OOM killer 记录

### 2. 加固措施（`env.py` 重写）
- **JVM 堆增大**：`JAVA_TOOL_OPTIONS=-Xmx4g`（原来无显式设置，默认 ~256MB）
- **`reset()` 自动重建 JVM**：捕获 `Py4JNetworkError`/`ConnectionError`/`OSError`，shutdown 旧 gateway，创建新 JVM 实例，最多重试 3 次
- **`step()` 优雅降级**：JVM 死亡时标记 `_env_dead=True`，返回 `done=True, reward=0`，不影响后续 episode

### 3. 重试提交
- **exp_id**: `scienceworld_grpo_cell_c_v2`
- **server**: westd-47453, GPU cuda:2,3
- **PID**: 920065
- **timeout**: 12h

---
