# eval backbone scaling check results

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_backbone-scaling-check-results_20260516T212828_result.json`
- **Structured JSON:** [`4ee1670fc22342aeecc3.json`](../../sessions/4e/4ee1670fc22342aeecc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。实验结果总结：

```
=== Backbone Scaling Death Rate: Qwen2.5-0.5B ===

Per-task (death = score 0):
  freeze:                    death 4/5 (80%)
  lifespan-longest-lived:    death 4/5 (80%)
  measure-melting-point:     death 4/5 (80%)

Overall: death 12/15 (80.0%)
Comparison: Qwen2.5-7B death rate = 42.9%
Delta: +37.1pp

Conclusion: SUPPORTS "smaller model → higher death rate"
```

0.5B 模型在所有 3 个 task 上表现一致差——几乎每个 episode 都是 score=0（加上 2 个 score=-100 的更极端失败）。唯一非零正分是 melting-point 的一个 episode 得了 7.0 分。相比 7B 的 42.9% death rate，0.5B 的 80% 提供了强证据支持 backbone 容量对 agent 存活的重要性。

---
