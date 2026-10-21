# code d157 launch and verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d157-launch-and-verify_20260520T145405_result.json`
- **Structured JSON:** [`a1057b8fa7d150283592.json`](../../sessions/a1/a1057b8fa7d150283592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D157 训练正常运行。**

| 项目 | 状态 |
|------|------|
| **PID** | 788433 |
| **GPU** | cuda:0, 44986MiB / 97887MiB |
| **进度** | step 4/500, ~6.9s/it |
| **预计耗时** | ~57 分钟 |
| **reward_mode** | shuffled_isr ✓ |
| **数据** | train_500_seed42.jsonl (C001 ✓) |
| **CUDA_VISIBLE_DEVICES** | 0 (C002/C005 ✓) |
| **save_total_limit** | 默认 1 (C003 ✓) |

前几步 reward log 正常：
- step 1: reward=0.270, prove_rate=0.250, isr=0.200, shuffle_proved=2
- step 3: reward=0.525, prove_rate=0.500, isr=0.250, shuffle_proved=4

shuffled_isr 模式正在工作（shuffle_proved 字段出现）。训练预计 ~1 小时内完成。

---
