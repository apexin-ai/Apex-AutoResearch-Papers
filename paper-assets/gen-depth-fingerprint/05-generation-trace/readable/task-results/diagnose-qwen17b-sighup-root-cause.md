# diagnose qwen17b sighup root cause

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen17b-sighup-root-cause_20260514T220218_result.json`
- **Structured JSON:** [`b836cd0b146270ab0f3c.json`](../../sessions/b8/b836cd0b146270ab0f3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两轮 SIGHUP 的根因全部定位。

**第一轮** (plan-002-qwen3-1_7b, 21:13:52Z)：`worker_infra_qwen-duplicate-fix` 会话在 21:14:18Z 显式执行了：
```bash
tmux kill-session -t plan-002-qwen3-1_7b-s0
tmux kill-session -t plan-002-qwen3-1_7b-s1
pkill -f "generate_chain.py.*qwen3-1.7b"
```
`tmux kill-session` 向 session 内进程发送 SIGHUP → bash trap 捕获 → `exit 129`。

**第二轮** (plan-002-qwen17b-retry, 21:57:43Z)：retry 在 r2 提交前 28 秒被终止（retry 死于 21:57:43Z，r2 启动于 21:58:12Z），框架在重新提交前清理了旧 sessions。

```json
{"root_cause": "框架 worker 会话 (worker_infra_qwen-duplicate-fix) 使用 tmux kill-session -t &lt;session-name> 按名字杀死了正在运行的 Qwen sessions。tmux kill-session 向 pane 进程发送 SIGHUP，bash wrapper 的 trap 'exit 129' HUP 捕获后退出。第二轮 retry 在 r2 提交前被同样机制清理。Pythia/OLMo 不受影响是因为 worker 只针对 Qwen sessions 操作。", "error_type": "infrastructure", "fix_steps": ["在 generate_chain.py 开头添加 signal.signal(signal.SIGHUP, signal.SIG_IGN) 使 Python 进程忽略 SIGHUP（worker_code_sighup-fix-and-status 已在 22:03Z 做了此修复）", "修改 tmux_backend.py 的 bash wrapper，将 trap 'exit 129' HUP 改为 trap '' HUP（忽略而非退出）", "框架重新提交任务前，应通过 kill -TERM 终止进程而非 tmux kill-session，避免 SIGHUP 信号传播", "排查触发 worker_infra_qwen-duplicate-fix 的逻辑，避免误杀正在正常运行的 sessions"], "can_auto_fix": true, "evidence": "日志 worker_infra_qwen-duplicate-fix_20260514T211316.jsonl line 9: ssh_execute 执行了 tmux kill-session -t plan-002-qwen3-1_7b-s0/s1 + pkill。退出文件 plan-002-qwen3-1_7b-s0.exit 记录 129|2026-05-14T21:13:52Z。plan-002-qwen17b-retry-s0.exit 记录 129|2026-05-14T21:57:43Z，28秒后 r2 于 21:58:12Z 启动。附加 bug: check_status L178 用 PID 查 tmux has-session 导致 tmux_session_alive 始终为 false（应用 exp_id）。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "框架 worker 会话 (worker_infra_qwen-duplicate-fix) 使用 tmux kill-session -t &lt;session-name> 按名字杀死了正在运行的 Qwen sessions。tmux kill-session 向 pane 进程发送 SIGHUP，bash wrapper 的 trap 'exit 129' HUP 捕获后退出。第二轮 retry 在 r2 提交前被同样机制清理。Pythia/OLMo 不受影响是因为 worker 只针对 Qwen sessions 操作。",
    "error_type": "infrastructure",
    "fix_steps": [
      "在 generate_chain.py 开头添加 signal.signal(signal.SIGHUP, signal.SIG_IGN) 使 Python 进程忽略 SIGHUP（worker_code_sighup-fix-and-status 已在 22:03Z 做了此修复）",
      "修改 tmux_backend.py 的 bash wrapper，将 trap 'exit 129' HUP 改为 trap '' HUP（忽略而非退出）",
      "框架重新提交任务前，应通过 kill -TERM 终止进程而非 tmux kill-session，避免 SIGHUP 信号传播",
      "排查触发 worker_infra_qwen-duplicate-fix 的逻辑，避免误杀正在正常运行的 sessions"
    ],
    "can_auto_fix": true,
    "evidence": "日志 worker_infra_qwen-duplicate-fix_20260514T211316.jsonl line 9: ssh_execute 执行了 tmux kill-session -t plan-002-qwen3-1_7b-s0/s1 + pkill。退出文件 plan-002-qwen3-1_7b-s0.exit 记录 129|2026-05-14T21:13:52Z。plan-002-qwen17b-retry-s0.exit 记录 129|2026-05-14T21:57:43Z，28秒后 r2 于 21:58:12Z 启动。附加 bug: check_status L178 用 PID 查 tmux has-session 导致 tmux_session_alive 始终为 false（应用 exp_id）。"
  }
}
```

</details>

---
