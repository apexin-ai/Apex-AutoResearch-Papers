# research sighup root cause

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sighup-root-cause_20260514T021418_result.json`
- **Structured JSON:** [`9039ce23368833b57512.json`](../../sessions/90/9039ce23368833b57512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已确认。现在写报告。

## SIGHUP 误杀根因分析报告

### 已确认的 SIGHUP 事件

| 实验 | 时间 (UTC) | Exit Code | Sentinel |
|------|-----------|-----------|----------|
| `mvp-p1-gpu0` | 2026-05-13 09:19:47 | 129 | `/tmp/agent-ml-exit/mvp-p1-gpu0.exit` |
| `plan-001b-gpu1-extra` | 2026-05-14 01:51:57 | 129 | `/tmp/agent-ml-exit/plan-001b-gpu1-extra.exit` |

---

### 事件 1: `mvp-p1-gpu0` — 根因已确认

**直接原因**: Worker `worker_exp_gpu0-boil-switch-vllm_20260513T091835` 调用 `kill_job(server="westb-13313", pid="mvp-p1-gpu0")` 杀了 tmux session。

**代码路径**:
1. Worker 调用 `kill_job` 时传入的 `pid="mvp-p1-gpu0"` 是 **exp_id（tmux session 名），不是数字 PID**
2. `ssh.py:1293` — `is_numeric = _RE_PID.match("mvp-p1-gpu0")` → `False`
3. `tmux_backend.py:256-261` — 因 `is_numeric=False`，跳过 `kill -TERM`，直接执行 `tmux kill-session -t mvp-p1-gpu0`
4. tmux 向 session 内所有进程发送 **SIGHUP**
5. `tmux_backend.py:68` — `trap 'exit 129' HUP` 捕获信号，bash exit 129
6. `tmux_backend.py:59-63` — EXIT trap 触发，写 sentinel `129|2026-05-13T09:19:47Z`

**日志证据** (`worker_exp_gpu0-boil-switch-vllm_20260513T091835.log` line 36):
```
kill_job返回: {"pid": "mvp-p1-gpu0", "reason": "Boil complete, switching to vLLM backend", "force_killed": false}
时间: 09:19:30Z → sentinel 09:19:47Z (17秒后写入)
```

**根因**: Worker 决定回收 GPU0 给新实验，主动杀了正在运行的 tmux session。这是 **设计层面的误操作** — Worker 没有等实验自然结束就回收了 GPU。

---

### 事件 2: `plan-001b-gpu1-extra` — 根因: 清理 Worker 误杀

**直接原因**: Worker `worker_ssh_gpu0-crash-cleanup_20260514T015135` 的 SSH 命令导致 tmux server 崩溃。

**时间线**:
| 时间 (UTC) | 事件 |
|-----------|------|
| 01:47:04 | plan-001b-gpu0-v2 exit 1 → tmux session 自毁 |
| 01:48:27 | plan-001b-gpu1-rebalance exit 1 → tmux session 自毁 |
| 01:51:35 | gpu0-crash-cleanup Worker 启动 |
| 01:51:56 | Worker 发送: `tmux kill-session -t plan-001b-gpu0-v2; tmux kill-session -t plan-001b-gpu0; pkill -f "episode_level_collection.*gpu_id 0"; pkill -f "vllm.*cuda:0"` (返回 -1) |
| **01:51:57** | **plan-001b-gpu1-extra 收到 SIGHUP, sentinel 写入 129** |
| 01:52:17 | Worker 再试 `tmux kill-session` → `"no server running on /tmp/tmux-0/default"` |
| 01:52:33 | GPU0=0MiB, GPU1=0MiB, 所有进程死亡 |

**分析**: 
- 01:51Z 时，`plan-001b-gpu1-extra` 可能是 tmux server 中 **唯一剩余的活跃 session**（其他 session 的进程已退出，session 已自毁）
- Worker 的 SSH 组合命令包含 `pkill -f "vllm.*cuda:0"` — 虽然 regex 指定了 `cuda:0`，但 vLLM 多进程架构可能创建了不含 `cuda:0` 的子进程名，或 `pkill` 的返回码 -1 表明命令部分执行
- 更可能的场景: 命令部分执行导致 tmux server 不稳定并崩溃，tmux server 向所有 pane 发送 SIGHUP

---

### 信号传播机制

```
tmux kill-session / tmux server crash
    └→ SIGHUP 发送到 session 内所有进程
        └→ tmux_backend.py:68 trap 'exit 129' HUP
            └→ bash exit 129
                └→ tmux_backend.py:59 EXIT trap → sentinel 写入 129
```

**关键代码位置**:
- `tmux_backend.py:68` — `trap 'exit 129' HUP` 将 SIGHUP 转换为 exit 129
- `tmux_backend.py:247-275` — `kill()` 函数对非数字 job_handle 直接执行 `tmux kill-session`
- `ssh.py:1293` — `is_numeric` 判断决定 kill 路径
- `cron.py:1054-1064` — `_EXIT_CODE_REASONS` 缺少 129 (SIGHUP) 映射

---

### 排除的嫌疑

| 组件 | 排除理由 |
|------|---------|
| SSH 连接池 `conn.close()` | tmux -d 创建的 detached session 不受 SSH 断开影响 |
| `cleanup_gpu_processes()` | 使用 SIGKILL (exit 137)，不是 SIGHUP (exit 129) |
| Cron `poll_cron()` | 只读状态检查，不发送任何 kill 信号 |
| Stale worker `_check_stale_workers()` | kill 的是本地 Worker 进程，不是远程 GPU 进程 |
| tmux `destroy-unattached` | 服务器无 `/etc/tmux.conf` 和 `~/.tmux.conf`，使用默认配置 (off) |
| NaN 检测自动 kill | 使用 SIGTERM → exit 143，不是 129 |

---

### 防护建议

**1. 修改信号处理策略** (`tmux_backend.py:68`)

当前:
```bash
trap 'exit 129' HUP
```
建议改为忽略 SIGHUP + 用 `setsid` 隔离进程组:
```python
inner_cmd = (
    f"rm -f {sentinel_path}; "
    f"mkdir -p {sentinel_dir}; "
    f"trap '{write_sentinel}' EXIT; "
    f"trap '' HUP; "  # 忽略 SIGHUP，不再因 tmux kill 退出
    f"trap 'exit 130' INT; "
    f"trap 'exit 143' TERM; "
    f"{{ {setup} && "
    f"setsid timeout {timeout_secs} env bash -c {shlex.quote(command)}"
    f"; }} > {log_file} 2>&1"
)
```

**2. `kill_job` 增加安全检查** (`tmux_backend.py:247-275`)

在 `tmux kill-session` 前验证目标 session 确实属于要杀的实验:
```python
if not is_numeric:
    # 验证 session 存在且匹配，避免误杀
    check = conn.run(f"tmux list-panes -t {shlex.quote(pid)} -F '#{{pane_pid}}' 2>/dev/null", ...)
    if not check.ok:
        return KillResult(success=True, force_killed=False)  # session 不存在，无需 kill
```

**3. 在 `_EXIT_CODE_REASONS` 中添加 129 映射** (`cron.py:1054`):
```python
129: "EXIT_CODE=129 (SIGHUP — tmux session 被外部终止)",
```

**4. Worker 指令层面**: 禁止 Worker 使用 `kill_job(pid=exp_id)` 杀正在运行的实验来腾 GPU。应该等实验结束或让 Reviewer 确认后再回收。

**5. 禁止在清理脚本中使用 `pkill -f` 宽泛模式**: 改为只 kill 特定 PID，避免 regex 匹配到其他 GPU 上的进程。

---
