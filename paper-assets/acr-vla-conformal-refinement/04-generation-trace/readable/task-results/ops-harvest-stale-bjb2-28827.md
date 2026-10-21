# ops harvest stale bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-stale-bjb2-28827_20260519T112217_result.json`
- **Structured JSON:** [`9b94464f3ca4328b5f8a.json`](../../sessions/9b/9b94464f3ca4328b5f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/7 实验 registry 全部更新完成。汇总：

```
exp_id                                  | success_rate | conclusion
----------------------------------------|-------------|----------
eval-obs-only-object-norm005-seed47     | 14%         | success
eval-perdof-object-norm03-seed47        | 5%          | success
eval-perdof-object-default-seed47       | 0%          | negative
eval-obs-only-object-default-seed48     | 17%         | success
eval-perdof-object-norm003-seed46       | 9%          | success
eval-random-selection-object-seed45     | 10%         | success
eval-obs-only-object-norm003-seed44-bjb2| 仍在运行     | —
```

**#1 (eval-obs-only-object-norm003-seed44-bjb2)** 仍在跑：tmux session `eval-obs-only-norm003-seed44-t16` 活跃，当前在 `pick_up_the_chocolate_pudding` task (rollout 9/10)，接近完成。输出 JSON 文件尚未生成（评估完所有 10 个 task 后才会写入）。无需干预，等自然结束后再采集。

---
