# eval acr spatial v4 default

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acr-spatial-v4-default_20260514T200936_result.json`
- **Structured JSON:** [`9fa48b2eb7b6f14dd38c.json`](../../sessions/9f/9fa48b2eb7b6f14dd38c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 未释放。pid 197062 仍在运行，是一个使用 CRM v2 checkpoint 的 eval：

```
python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt
```

这不是之前 kill 的 v3（pid 197057），而是另一个 v2 eval 进程。需要 kill 掉 197062 才能释放 cuda:0。要 kill 吗？

---
