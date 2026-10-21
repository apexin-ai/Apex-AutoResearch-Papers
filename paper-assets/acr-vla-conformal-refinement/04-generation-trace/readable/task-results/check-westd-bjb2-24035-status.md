# check westd bjb2 24035 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-bjb2-24035-status_20260526T075118_result.json`
- **Structured JSON:** [`7f65d7e4a357b757f4fb.json`](../../sessions/7f/7f65d7e4a357b757f4fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== SERVER: westd-49937 ===
[DONE] westd-pi05-adaptive-goal-s42:   SR=88.0% (20×10=200)  logs/eval_goal_adaptive_pi05_seed42.json
[DONE] westd-pi05-adaptive-goal-s43:   SR=87.5% (20×10=200)  logs/eval_goal_adaptive_pi05_seed43.json
[DONE] westd-pi05-crm-k2-goal-s42:     SR=85.5% (20×10=200)  logs/eval_goal_crm_k2_pi05_seed42.json
[DONE] westd-pi05-adaptive-object-s42: SR=83.5% (20×10=200)  logs/eval_object_adaptive_pi05_seed42.json
（全部 GPU 空闲，4 个实验均已收割就绪）

=== SERVER: bjb2-24035 ===
[RUNNING] westd-pi05-adaptive-object-s43:
  PID 3035, etime=3h34m52s, GPU util 28%, mem 11.7GB
  进度：5/10 任务完成（100/200 rollouts）
  分任务 SR（已完成）：alphabet_soup 95% | cream_cheese 75% | salad_dressing 95% | bbq_sauce 75% | ketchup 55%
  partial mean SR ≈ 79.0%
  log: /tmp/westd-pi05-adaptive-object-s43.log
  ETA：每任务约 40min，剩 5 任务 → 还需 ~3h（约 18:30-19:00 完成）
```

**关键发现**：
- westd 4 个全部完成，可立即收割（结果都很合理：adaptive goal 87-88%，crm_k2 85.5%，adaptive object 83.5%）
- bjb2 上的 object-s43 还需 ~3h；对照 object-s42=83.5%，当前 5 任务均值 79% 略偏低但属正常波动
- bjb2 上没有 cron 监控，完成后需手动检查输出 JSON 位置（`logs/eval_object_adaptive_pi05_seed43.json`）

---
