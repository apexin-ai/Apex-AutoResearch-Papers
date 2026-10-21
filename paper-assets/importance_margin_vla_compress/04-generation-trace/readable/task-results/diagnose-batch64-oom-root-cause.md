# diagnose batch64 oom root cause

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch64_oom_root_cause_20260517T083148_result.json`
- **Structured JSON:** [`e4ddebd52dad090603df.json`](../../sessions/e4/e4ddebd52dad090603df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已存活超过 17 分钟（超过上次崩溃时间），同时 cgroup oom_kill 仍为 0。诊断结论如下。

---

## 诊断结果

### 根因：Host-level OOM Killer (非容器自身 OOM)

**核心证据**：

| 检查项 | 结果 |
|--------|------|
| tmux 输出 | `Killed`（SIGKILL，无 traceback） |
| cgroup `memory.max` | 320 GB |
| cgroup `memory.current` (崩溃后) | ~42 GB（远低于限制） |
| cgroup `oom_kill` 计数器 | **0**（崩溃前后都是 0） |
| 进程 RSS | 稳定 2.6 GB，VmHWM（峰值）仅 3.6 GB |
| 进程 `oom_score_adj` | **999**（最高优先级 victim） |
| /dev/shm | 160 GB 仅用 6 MB |
| Host memory | 1 TB 总量，952 GB 可用 |
| Swap | **完全没有**（容器和 Host 均为 0） |
| GPU 错误 | 无 ECC/Xid 错误 |
| 崩溃模式 | 非确定性（相同代码相同步数，Run 4 已存活超过 Run 3 崩溃时间点） |

### 机制

```
                        物理节点 (1 TB RAM, 无 swap)
                 ┌──────────────────────────────────────────┐
                 │  容器 A (oom_score_adj=999, limit=320GB) │ ← 你的容器
                 │  容器 B (其他租户)                        │
                 │  容器 C (其他租户)                        │
                 └──────────────────────────────────────────┘
                                    ↓
        当其他租户瞬间申请大量内存 → Host 内核触发全局 OOM killer
                                    ↓
        选择 oom_score 最高的进程 → 你的训练进程 (adj=999)
                                    ↓
        发送 SIGKILL → "Killed"，无任何 Python 错误信息
        cgroup oom_kill 计数器 NOT 增加（因为不是 cgroup 自身限制触发）
```

### 排除项

- **NOT** 容器内存泄漏（RSS 完全不增长）
- **NOT** cgroup OOM（计数器始终为 0）
- **NOT** 磁盘满（34 GB 剩余）
- **NOT** GPU 错误
- **NOT** 代码 bug（相同代码在不同时间可以正常运行）

### 建议（非必要时不执行）

这个问题**无法从容器内部解决**。可能的缓解方式：
1. 联系 AutoDL 客服反映节点超售/OOM 问题，要求迁移到负载较低的节点
2. 添加 checkpoint resume 逻辑（save_every=2000 已配置），这样被杀后可以从最近 checkpoint 恢复
3. 避开高峰时段训练（如果可能）

---

## k07/k03 状态

| 任务 | 状态 | Checkpoint |
|------|------|-----------|
| k07 | **已完成** (exitcode 0) | `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt` (878 MB, 15:56) |
| k03 | **已完成** (exitcode 0) | `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt` (878 MB, 15:57) |

两个 tmux session 均已清理。

---

## 当前 batch64_v2 状态

PID 23996 仍在运行（已 17+ 分钟），RSS=2.6 GB 稳定。监控脚本 `/tmp/monitor_kill.sh` 在后台持续记录，如果再次被杀可查看 `/tmp/kill_monitor.log` 确认崩溃时内存状态。

---
