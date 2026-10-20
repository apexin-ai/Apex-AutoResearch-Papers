# check qwen random status fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-random-status-fix_20260514T080407_result.json`
- **Structured JSON:** [`d6fecd0c96bd86f39d79.json`](../../sessions/d6/d6fecd0c96bd86f39d79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇总：**

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| bf16_qw_rand_s015 | 95899 | cuda:0 (78%) | 24/50 | RUNNING ✓ |
| bf16_qw_rand_s020 | 96294 | cuda:2 (80%) | 15/50 | RUNNING ✓ |
| bf16_qw_rand_s025 | 96437 | cuda:3 (76%) | 15/50 | RUNNING ✓ |

- 3 个进程全部确认在跑，GPU 显存各占 ~25GB
- Registry 已从 QUEUED 更新为 RUNNING
- 已注册每 8 分钟监控 cron，实验完成后自动更新 registry 并注册 artifact

---
