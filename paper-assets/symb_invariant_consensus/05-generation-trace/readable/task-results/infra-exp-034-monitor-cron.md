# infra exp 034 monitor cron

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp-034-monitor-cron_20260518T211028_result.json`
- **Structured JSON:** [`fb86eee5ef42a4fc0fcb.json`](../../sessions/fb/fb86eee5ef42a4fc0fcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 监控已注册（每小时 :17 触发，session-only）。

**汇总：**

| 项目 | 值 |
|---|---|
| 进度 | **180/600** |
| tmux session | `exp034_run` |
| Python PID | **69808** |
| VLLM PID | **68846** (cuda:1, 88230MiB, 98% util) |
| 模型 | Qwen2.5-14B-Instruct |
| avg 速度 | 67.7s/问题 |
| ETA | ~475 min (~**7.9 小时**，约 13:05 UTC) |
| cron job | `e820d976`，每小时 :17 检查 |

**问题：** Registry 状态机卡住——从 ANALYZING(failed) 尝试恢复到 RUNNING 时，经过 DONE→DEPLOYING→DEPLOYED 后 DEPLOYED 没有合法的出向转移，当前停留在 DEPLOYED。notes 已更新记录实际运行状态。如需彻底修复 registry 状态，可能需要直接编辑 registry 文件。

---
