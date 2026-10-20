# diagnose tmux death root cause

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_tmux-death-root-cause_20260514T220718_result.json`
- **Structured JSON:** [`b908329398b4694b9da5.json`](../../sessions/b9/b908329398b4694b9da5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认根因。**`tmux has-session -t 120612` 返回 NO（false negative），但 `tmux has-session -t plan-002-qwen17b-r2-s0` 返回 YES。Session 一直活着，是检查逻辑的 bug。

---

## 诊断结论

```json
{
  "root_cause": "框架 check_status 方法用 PID（如'120612'）调用 tmux has-session，但 session 名是 exp_id（如'plan-002-qwen17b-r2-s0'），导致永远报 tmux_session_alive=false。Worker 误判 session 已死，调用 kill_job(exp_id) 'cleanup orphan'，实际杀死了正在运行的 session。",
  "error_type": "framework_bug",
  "evidence": [
    "tmux has-session -t 120612 → NO; tmux has-session -t plan-002-qwen17b-r2-s0 → YES（session 一直活着）",
    "registry 22:01:52 记录 'tmux_session_alive=false（PID 120612 仍在运行 ~3min）' — 但 tmux ls 确认 session 存在",
    "所有 Qwen 失败均为 EXIT_CODE=129（SIGHUP from tmux kill-session），非 143（SIGTERM from kill PID）",
    "Pythia/OLMo 在 Worker 误判前已完成（exit 0），所以未受影响",
    "qwen06b 用 ssh_execute 直接启动（无 tmux），kill_job 的 tmux kill-session 对它无效，进程存活至今"
  ],
  "why_qwen_only": "Pythia/OLMo 运行时间短（40-70min），在 Worker 下一次 poll 触发 kill 前已自然完成。Qwen 运行时间长（预计 ~2h），Worker poll 周期内发现 tmux_session_alive=false 就触发了 kill。",
  "fix_steps": [
    "修复 tmux_backend.py:check_status() — tmux has-session 检查应使用 exp_id 而非 PID",
    "修复 tmux_backend.py:kill() — tmux kill-session 应使用 exp_id 而非 PID",
    "确认 Worker 不应在 tmux_session_alive=false 时自动调用 kill_job"
  ],
  "can_auto_fix": true,
  "r2_status": "PID 120612/120689 正在运行，tmux session 存活，GPU 0/1 利用率 39%/44%，进度 ~40%（200+/498 seeds）。r2 未被杀是因为 Worker 这次没立即 kill 而是先派诊断 Worker",
  "recommended_resubmit_strategy": "不需要重提交。r2 和 qwen06b 全部 4 个进程都在正常运行。修复框架 bug 后，后续实验不会再被误杀。"
}
```

### Bug 位置

`/home/ubuntu/agent-ml-research/core/tools/execution_backends/tmux_backend.py` 第 178 行：

```python
# BUG: pid 是数字 PID，session 名是 exp_id
tmux_result = conn.run(
    f"tmux has-session -t {shlex.quote(pid)} 2>/dev/null && echo yes || echo no", ...
)
```

应改为：
```python
session_name = exp_id if exp_id else pid
tmux_result = conn.run(
    f"tmux has-session -t {shlex.quote(session_name)} 2>/dev/null && echo yes || echo no", ...
)
```

### 当前状态

| 进程 | GPU | 进度 | 状态 |
|------|-----|------|------|
| qwen17b-r2-s0 (PID 120612) | cuda:0, 39% | ~200/498 seeds | tmux alive, 正常运行 |
| qwen17b-r2-s1 (PID 120694) | cuda:1, 44% | running | tmux alive, 正常运行 |
| qwen06b-s0 (PID 117855) | cuda:2, 33% | running (orphan) | 无 tmux，PPID=1，仍在正常写数据 |
| qwen06b-s1 (PID 118126) | cuda:3, 33% | running (orphan) | 无 tmux，PPID=1，仍在正常写数据 |

所有 4 个实验正在正常推进，无需干预。修复 `check_status` bug 可以防止未来实验被误杀。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "框架 check_status 方法用 PID（如'120612'）调用 tmux has-session，但 session 名是 exp_id（如'plan-002-qwen17b-r2-s0'），导致永远报 tmux_session_alive=false。Worker 误判 session 已死，调用 kill_job(exp_id) 'cleanup orphan'，实际杀死了正在运行的 session。",
    "error_type": "framework_bug",
    "evidence": [
      "tmux has-session -t 120612 → NO; tmux has-session -t plan-002-qwen17b-r2-s0 → YES（session 一直活着）",
      "registry 22:01:52 记录 'tmux_session_alive=false（PID 120612 仍在运行 ~3min）' — 但 tmux ls 确认 session 存在",
      "所有 Qwen 失败均为 EXIT_CODE=129（SIGHUP from tmux kill-session），非 143（SIGTERM from kill PID）",
      "Pythia/OLMo 在 Worker 误判前已完成（exit 0），所以未受影响",
      "qwen06b 用 ssh_execute 直接启动（无 tmux），kill_job 的 tmux kill-session 对它无效，进程存活至今"
    ],
    "why_qwen_only": "Pythia/OLMo 运行时间短（40-70min），在 Worker 下一次 poll 触发 kill 前已自然完成。Qwen 运行时间长（预计 ~2h），Worker poll 周期内发现 tmux_session_alive=false 就触发了 kill。",
    "fix_steps": [
      "修复 tmux_backend.py:check_status() — tmux has-session 检查应使用 exp_id 而非 PID",
      "修复 tmux_backend.py:kill() — tmux kill-session 应使用 exp_id 而非 PID",
      "确认 Worker 不应在 tmux_session_alive=false 时自动调用 kill_job"
    ],
    "can_auto_fix": true,
    "r2_status": "PID 120612/120689 正在运行，tmux session 存活，GPU 0/1 利用率 39%/44%，进度 ~40%（200+/498 seeds）。r2 未被杀是因为 Worker 这次没立即 kill 而是先派诊断 Worker",
    "recommended_resubmit_strategy": "不需要重提交。r2 和 qwen06b 全部 4 个进程都在正常运行。修复框架 bug 后，后续实验不会再被误杀。"
  }
}
```

</details>

---
