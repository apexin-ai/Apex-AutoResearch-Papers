# ops check random seed42 and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_random_seed42_and_eval_20260518T085701_result.json`
- **Structured JSON:** [`9d764e930cba7c88c0f1.json`](../../sessions/9d/9d764e930cba7c88c0f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
contamination_60_random_seed42: DONE
  final PPL: 17.832
  checkpoint-1000 PPL: N/A (已被清理，无法对比)
  resume degradation: 无法直接评估（checkpoint-1000 不存在）
  train_loss: 6.413, 6103/6103 steps, ~3h runtime

contamination_60_grid_b0_3_seed42 eval:
  final PPL: 17.634
  checkpoint-1500 PPL: 18.583 (已知)
  checkpoint-5500 eval: 仍在运行中
```

grid_b0_3 从 ckpt-1500 (18.583) 到 final (17.634) 改善明显 (-0.949)。random baseline final (17.832) 略差于 grid_b0_3 final (17.634)，grid 加权方案有 ~1.1% PPL 优势。

---
