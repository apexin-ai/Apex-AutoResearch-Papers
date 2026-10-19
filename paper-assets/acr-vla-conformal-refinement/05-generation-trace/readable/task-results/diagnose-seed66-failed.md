# diagnose seed66 failed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed66-failed_20260521T014338_result.json`
- **Structured JSON:** [`19bd747394c909af2c4d.json`](../../sessions/19/19bd747394c909af2c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有证据汇总如下：

## 诊断结果

**原始实验（PID 638171/638251/638518）已死亡。**

**根因：SSH 会话断开导致 SIGHUP 杀死进程。**

证据链：
- dmesg 无 OOM/kill 记录 — 排除内核 OOM killer
- 系统资源充足：927GB RAM 可用、磁盘 53%/61%、GPU 正常
- **无 tmux/screen 会话** — 进程没有 session 保护
- 三个进程在 2 分钟窗口内同时死亡 — 与 SSH 断连行为一致
- 日志无 traceback/error — SIGHUP 直接终止，不产生 Python 异常
- 原始日志已被重启实验覆盖

**重启实验已在运行且健康：**

| PID | GPU | norm | 启动时间(CST) | CPU% | GPU内存 |
|-----|-----|------|-------------|------|---------|
| 642428 | 0 | 0.03 | 09:30 | 387% | 5711 MiB |
| 642506 | 2 | 0.05 | 09:30 | 404% | 5711 MiB |
| 642775 | 3 | 0.1 | 09:31 | 412% | 5711 MiB |

重启版本 PPID=1（已正确脱离终端），但 **log 文件停滞**：启动时没用 `python -u`，stdout 块缓冲未 flush。进程实际在跑，日志会在完成时一次性写出。

```json
{"root_cause":"SSH session disconnected ~01:37 UTC sending SIGHUP to all 3 child processes. No tmux/screen/nohup protection. Evidence: no OOM in dmesg, no traceback, all 3 died simultaneously within 2min window, system resources healthy (927GB RAM free, disk 53%/61%, GPUs fine). Relaunched experiments with PPID=1 are running successfully on same hardware, confirming infrastructure is OK.","error_type":"infrastructure","fix_steps":["No action needed — experiments already relaunched (PID 642428/642506/642775) and running ~1h with healthy CPU/GPU","Log files appear stalled due to missing python -u flag (stdout block-buffered); process will flush on completion","Future launches: use tmux/screen + nohup + python -u to prevent recurrence"],"can_auto_fix":true,"affected_exps":["eval-obs-only-object-norm003-seed66","eval-obs-only-object-norm005-seed66","eval-obs-only-object-norm01-seed66"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "SSH session disconnected ~01:37 UTC sending SIGHUP to all 3 child processes. No tmux/screen/nohup protection. Evidence: no OOM in dmesg, no traceback, all 3 died simultaneously within 2min window, system resources healthy (927GB RAM free, disk 53%/61%, GPUs fine). Relaunched experiments with PPID=1 are running successfully on same hardware, confirming infrastructure is OK.",
    "error_type": "infrastructure",
    "fix_steps": [
      "No action needed — experiments already relaunched (PID 642428/642506/642775) and running ~1h with healthy CPU/GPU",
      "Log files appear stalled due to missing python -u flag (stdout block-buffered); process will flush on completion",
      "Future launches: use tmux/screen + nohup + python -u to prevent recurrence"
    ],
    "can_auto_fix": true,
    "affected_exps": [
      "eval-obs-only-object-norm003-seed66",
      "eval-obs-only-object-norm005-seed66",
      "eval-obs-only-object-norm01-seed66"
    ]
  }
}
```

</details>

---
