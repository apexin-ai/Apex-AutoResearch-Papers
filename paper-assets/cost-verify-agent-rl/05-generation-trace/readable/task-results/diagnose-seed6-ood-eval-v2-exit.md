# diagnose seed6 ood eval v2 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed6_ood_eval_v2_exit_20260521T142026_result.json`
- **Structured JSON:** [`88c2d58582b43a7321cc.json`](../../sessions/88/88c2d58582b43a7321cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：exp029_seed6_ood_eval_v2 成功完成。**

| 指标 | 值 |
|------|-----|
| OOD success_rate | **29.1%** (39/134) |
| pass@1 | 29.1% |
| num_actions | 36.6 |
| action_is_effective | 97.3% |
| action_is_valid | 63.2% |
| manager_invalid_action | 2.7% |

进程正常退出，134 个 OOD tasks 全部评估完毕（耗时 ~1171s）。日志末尾的 wandb BrokenPipeError 是无害的 atexit 清理错误。Registry 已更新为 success + metrics，failure_reason 已清除，cron 已无需清理（不存在）。GPU cuda:2 已释放。

---
