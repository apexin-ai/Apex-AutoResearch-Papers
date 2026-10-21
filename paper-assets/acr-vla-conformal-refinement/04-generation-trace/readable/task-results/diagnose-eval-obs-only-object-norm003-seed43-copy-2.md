# diagnose eval obs only object norm003 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed43_20260518T204126_result.json`
- **Structured JSON:** [`80f638678d7f84b72925.json`](../../sessions/80/80f638678d7f84b72925.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：SIGHUP（session 终止）**，不是 OOM 或代码错误。tmux server 已完全消失，导致挂在其下的进程收到 HUP 信号退出。同服务器上 GPU 2/3 的其他实验仍在正常运行（它们可能是在不同 session 启动的）。

**进度**：4/10 tasks 完成（alphabet_soup 0%, cream_cheese 10%, salad_dressing 20%, bbq_sauce 40%），第 5 个 task（ketchup）在 rollout 6/10 处被杀。无 JSON 输出文件。

**重试建议**：
- GPU 0 和 1 均空闲，可直接重跑
- 同样的命令，无需改参数
- 关键：用 `nohup` 启动或确保 tmux session 稳定，避免第三次 SIGHUP

---
