# diag cqa1 speed issue

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cqa1-speed-issue_20260526T020558_result.json`
- **Structured JSON:** [`a427f88860e70f696128.json`](../../sessions/a4/a427f88860e70f696128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**用户的判断错误。实验运行正常，不要 kill。**

### 实际情况

| 项 | 值 |
|----|----|
| **模型** | SmolVLA（`/root/autodl-tmp/models/smolvla_libero/`） |
| **模式** | `adaptive_conformal_crm`, K=2, max_corr=0.2 |
| **CRM ckpt** | `crm_smolvla_3suite_v1/crm_best.pt` |
| **Benchmark** | LIBERO-Goal, 10 tasks, n_rollouts=20, max_steps=300 |
| **进程启动** | 08:32:58 |
| **当前进度** | 6/6 进程都已完成 **5/10 tasks**（即 100/200 rollouts），第 6 个 task 进行中 |
| **实际 wall clock** | ~93 分钟（**不是 10 小时**） |
| **速率** | ~0.93 min/rollout，预计总耗时 ~3 小时 |

### GPU/资源

- 6× RTX 4090D，每个进程 3516 MiB（SmolVLA + CRM K=2 合理）
- GPU util 20-29%，CPU 600-660%（LIBERO simulation 在 CPU 上跑，正常）

### 根因分析

不存在"慢 100x"的问题。**用户记忆/读数有误**。可能误把 "5/10 task 完成" 看成 "1/10"，或者把 tmux session 创建时间（07:37 birth）误当成进程启动时间——但进程实际 08:32 才启动，1.5 小时跑完 5 个 task 完全符合预期。

### 建议

**继续等待，不要 kill。** 预计 ~1.5 小时后（约 11:30）6 个进程全部完成。

---
