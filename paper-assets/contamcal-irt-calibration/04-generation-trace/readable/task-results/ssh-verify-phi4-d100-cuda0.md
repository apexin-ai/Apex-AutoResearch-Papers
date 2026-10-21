# ssh verify phi4 d100 cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-phi4-d100-cuda0_20260519T080332_result.json`
- **Structured JSON:** [`d6f2da867f391baada0e.json`](../../sessions/d6/d6f2da867f391baada0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phi-4 d100 确认已在 cuda:0 正常运行。**

| 项目 | 状态 |
|---|---|
| cuda:0 进程 | PID 121916，55774 MiB / 97887 MiB，GPU-Util 89% |
| 训练进度 | **36 / 4159 steps** (~0.9%)，~2.35 s/step，ETA ~2.7h |
| loss | 1.624 → 1.529（正常下降） |
| token accuracy | 0.626 → 0.647（正常上升） |
| lora_alpha | 32（符合规范） |

注：PID 121916 是实际 GPU 进程（121911 的子进程），torch compile workers (122485-122488) 也已启动。tmux 命令在 read-only 模式下被拦截，但 ps 输出确认 phi-4 train_sft.py 进程链存活。

---
