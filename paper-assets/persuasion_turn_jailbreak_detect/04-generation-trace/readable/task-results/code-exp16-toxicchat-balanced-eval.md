# code exp16 toxicchat balanced eval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-toxicchat-balanced-eval_20260520T012109_result.json`
- **Structured JSON:** [`0e277ea2b5f115999829.json`](../../sessions/0e/0e277ea2b5f115999829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果如下：

```
toxicchat_eval.jsonl (408条, 204jb/204bn) 上的 Macro F1:

9-class:
  seed42:  0.6235
  seed123: 0.5165
  seed456: 0.5091
  mean±std: 0.5497±0.0523

vanilla:
  seed42:  0.3655
  seed123: 0.3567
  seed456: 0.3445
  mean±std: 0.3556±0.0086
```

结果已保存至 `results/exp16_toxicchat_balanced.json`。9-class 在平衡集上 macro F1 比 vanilla 高约 19.4 个百分点（0.550 vs 0.356）。vanilla 的 F1 极低（~0.36），说明在平衡数据上它几乎把大部分样本预测成了同一类。

---
