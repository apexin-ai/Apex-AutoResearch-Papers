# eval plan 008 v4 0 6b 4b nothinking

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-008-v4-0_6b-4b-nothinking_20260515T210317_result.json`
- **Structured JSON:** [`e60865c9a57f8772127e.json`](../../sessions/e6/e60865c9a57f8772127e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 eval 完成。汇总结果：

```
=== 0.6B enable_thinking=False eval ===
Seed 42: balanced_acc=0.6241, internal_recall=0.6000, eval_loss=N/A
Seed 43: balanced_acc=0.5574, internal_recall=0.6000, eval_loss=N/A
Mean: balanced_acc=0.5908±0.0472

=== 4B enable_thinking=False eval ===
Seed 42: balanced_acc=0.6241, internal_recall=0.5333, eval_loss=N/A
Seed 43: balanced_acc=0.5463, internal_recall=0.4667, eval_loss=N/A
Mean: balanced_acc=0.5852±0.0550

=== 统一 enable_thinking=False 三模型对比 ===
| Model     | Seed 42 | Seed 43 | Mean±Std        |
|-----------|---------|---------|-----------------|
| 0.6B      | 0.6241  | 0.5574  | 0.5908±0.0472   |
| 1.7B (ref)| 0.5761  | 0.4852  | 0.5307±0.0643   |
| 4B        | 0.6241  | 0.5463  | 0.5852±0.0550   |
```

注：`routing_eval_sft.py` 是 generation-based eval，不输出 eval_loss。结果文件已保存到 `results/plan-008-v4/` 下的 4 个 `_nothinking.json` 文件。

---
