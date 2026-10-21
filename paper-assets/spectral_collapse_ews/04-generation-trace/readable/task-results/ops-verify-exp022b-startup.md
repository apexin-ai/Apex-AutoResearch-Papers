# ops verify exp022b startup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-exp022b-startup_20260524T073831_result.json`
- **Structured JSON:** [`82daf71c5530bc63bbaa.json`](../../sessions/82/82daf71c5530bc63bbaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：exp_022b 启动失败，exp_020 正常运行。**

| 实验 | GPU | 状态 | 详情 |
|------|-----|------|------|
| exp_020 | cuda:0 | 正常运行 | PID 783957, 26422MiB, 96% 利用率，tmux session `exp_020` 存在 |
| exp_022b | cuda:1 | **启动失败** | GPU 空闲 (0MiB, 0%)，无 tmux session |

**exp_022b 失败原因**：日志全部内容为：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

启动脚本用了 `python` 而非 `python3`（或未激活 conda 环境）。没有 `exp_022` 的旧 session 需要清理。

需要我修复启动命令重新跑 exp_022b 吗？

---
