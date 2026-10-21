# ops kill ghost process

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-ghost-process_20260525T203930_result.json`
- **Structured JSON:** [`ebd26cd63d5b74fc53ff.json`](../../sessions/eb/ebd26cd63d5b74fc53ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **PID 986901 已 kill**，GPU 完全释放（双卡均 0MiB）
- **来源**: exp_024，Phase 1 fixed_mix / pythia-410m / seed=44 / gpu=0，由 agent worker 通过 ssh_execute nohup 启动但未注册 registry。bash_history 无记录、无 tmux、无 crontab，确认是 worker 幽灵进程
- **运行了约 67 分钟**，Gen 0 已完成并存了 checkpoint，Gen 1 生成到 ~80% 被 kill，无最终 results JSON 产出
- **无其他异常训练进程**，audit 相关文件不存在

报告已写入 `artifacts/ghost_process_investigation.md`。

---
