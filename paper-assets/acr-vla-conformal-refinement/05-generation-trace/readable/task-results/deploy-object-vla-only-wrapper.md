# deploy object vla only wrapper

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_object-vla-only-wrapper_20260523T015707_result.json`
- **Structured JSON:** [`b07ab715469daae87047.json`](../../sessions/b0/b07ab715469daae87047.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

## 报告

| Seed | tmux session | PID | GPU | 显存占用 |
|------|-------------|-----|-----|---------|
| 42 | obj_vla_s42 | 455214 | cuda:3 | 5630 MiB |
| 43 | obj_vla_s43 | 455415 | cuda:4 | 5630 MiB |
| 44 | obj_vla_s44 | 455618 | cuda:5 | 5630 MiB |

- **启动状态**：3 个 seed 全部成功，无 argparse error，已加载 10 个 LIBERO-Object tasks，正在 rollout
- **GPU 隔离**：cuda:0,1,2 未受影响（CRM eval 正常运行），cuda:3,4,5 各占用 5630 MiB
- **注意**：首次尝试因 tmux 内未激活 conda 导致 `python: command not found`，已修复并重新部署

---
