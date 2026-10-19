# ops collect 14b results and status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_14b_results_and_status_20260520T035003_result.json`
- **Structured JSON:** [`edf8ea7ede742576502e.json`](../../sessions/ed/edf8ea7ede742576502e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
14B TEAL global: [完成] HS=0.7051 PIQA=0.7470
14B BCE global:  [完成] HS=0.5343 PIQA=0.6828
MSE 50% train:   [完成] step 1000/1000, loss=0.0083, sparsity=0.539, checkpoint已保存 (152MB)
MSE 30% eval:    [运行中] arc_challenge 进行中 (525/1172, ~45%)
```

关键发现：BCE global 的 HS/PIQA 大幅低于 TEAL global（HS 差 17pp, PIQA 差 6.4pp），说明 BCE predictor 在 global_topk allocation 下表现严重退化。

---
