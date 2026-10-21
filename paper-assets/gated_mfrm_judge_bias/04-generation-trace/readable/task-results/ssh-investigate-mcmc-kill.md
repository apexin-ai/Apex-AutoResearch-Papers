# ssh investigate mcmc kill

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_investigate-mcmc-kill_20260525T051244_result.json`
- **Structured JSON:** [`4efe32b6e62906f3c194.json`](../../sessions/4e/4efe32b6e62906f3c194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**原因：AutoDL 平台级别强制终止（非 OOM）**

### 证据

| 检查项 | 结果 | 排除 |
|--------|------|------|
| cgroup memory.events | `oom 0, oom_kill 0` | ✅ 排除 cgroup OOM |
| 系统内存 | 1TB 总量，当前使用 32GB，cgroup 限制 440GB | ✅ 排除内存不足 |
| 日志中错误 | grep 0 matches (无 Traceback/Signal/Error) | ✅ 排除 Python 异常 |
| bash_history | 无 kill 命令 | ✅ 排除人为误杀 |
| auto_mcmc_phase1.sh | 启动 PID 后已退出，无后续 kill 逻辑 | ✅ 排除脚本误杀 |
| last reboot | 无近期重启记录 | ✅ 排除系统重启 |
| dmesg | Operation not permitted (容器限制) | ❌ 无法查看宿主机内核日志 |

### 日志现场

- 进程 04:39 启动，12:10 日志停止写入（运行约 7.5 小时）
- 前面的 chain 正常完成 (10000/10000)
- 最后停在 joint_gmfrm chain 采样 9038/10000，无任何 graceful shutdown 痕迹（突然截断）

### 判定

**AutoDL 平台操作**——容器编排层面的 SIGKILL。在 AutoDL 容器内 dmesg 不可访问，且平台的资源管理/维护操作不留用户可见日志。内存、磁盘、用户操作均已排除，剩下唯一合理解释是平台层面干预。

---
