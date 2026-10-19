# diagnose scalar eval cron

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scalar-eval-cron_20260515T014456_result.json`
- **Structured JSON:** [`f408b4836d4ec58cb0d4.json`](../../sessions/f4/f408b4836d4ec58cb0d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID**: 288939
- **Log**: `/root/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log`
- **GPU**: cuda:2, 1450 MiB 显存占用
- **启动时间**: 09:34 (约 11 分钟前)
- **进度**: 0/10 tasks 完成。日志只有 16 行，停在 `[eval] 10 tasks loaded.`，说明正在跑第 1 个 task 的 rollouts，还没有任何 task 完成输出。
- **错误**: 无。模型加载正常（SmolVLA + CRM scalar_unc），CPU 160% 活跃运行中。
- **参数**: `--mode crm_scalar --benchmark spatial --n_rollouts 10 --K 10 --crm_checkpoint crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1`

---
