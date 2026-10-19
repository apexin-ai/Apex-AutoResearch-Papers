# deploy bjb1 32546 update and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-update-and-deploy_20260519T180153_result.json`
- **Structured JSON:** [`20c94d68a0e537c008ad.json`](../../sessions/20/20c94d68a0e537c008ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 已完成实验 → DONE
| 实验 | SR | 状态 |
|------|-----|------|
| eval-vla-only-goal-seed42 | **71%** | DONE ✓ |
| eval-vla-only-goal-seed43 | **69%** | DONE ✓ |
| eval-obs-only-spatial-norm02-seed47 | **32%** | DONE ✓ |

### 仍在运行（bjb1-32546）
- GPU0: eval-vla-only-long-seed42
- GPU2: eval-vla-only-long-seed43
- GPU3: eval-vla-only-long-seed44

### 新部署实验 → RUNNING
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| eval-vla-only-long-seed46 | GPU1 (6284 MiB) | 26430 | RUNNING ✓ |
| eval-vla-only-goal-seed46 | GPU4 (5509 MiB) | 26499 | RUNNING ✓ |

### Long seed42/43/44
JSON 输出尚未生成，进程仍在跑（已运行约 1.4h）。

Cron 已注册，每小时 :23 自动检查新实验完成状态。GPU5 仍空闲。

---
