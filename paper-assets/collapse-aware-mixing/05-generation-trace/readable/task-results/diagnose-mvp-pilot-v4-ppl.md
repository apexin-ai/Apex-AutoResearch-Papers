# diagnose mvp pilot v4 ppl

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_pilot_v4_ppl_20260512T153829_result.json`
- **Structured JSON:** [`25ea8366fef61f1e82ea.json`](../../sessions/25/25ea8366fef61f1e82ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果汇总：

---

**1. Checkpoint 路径**
`/root/autodl-tmp/output/G0/training/checkpoint-760`

**2. 评估结果**
- **Manual per-token CE mean: 114.7858**
- **Manual PPL: inf**（CE=114.79，exp(114.79) 溢出）
- **Batches evaluated: 50**（200 samples / batch_size=4）

**3. Transformers 对比**
- **Transformers reported loss (last batch): 108.3693**
- **Manual loss (last batch): 108.3693**
- **Ratio (transformers/manual): 1.00**

**4. 训练日志最后 20 行**（从之前抓取的日志）
```
step 760/1373 (55%) | ~28:41 elapsed | ~21:23 remaining | 2.09s/it
{'loss': 116.1764, 'grad_norm': 90.375,  'lr': 5.55e-06, 'epoch': 0.47}
{'loss': 106.9684, 'grad_norm': 106.375, 'lr': 5.17e-06, 'epoch': 0.51}
{'loss': 106.7754, 'grad_norm': 43.719,  'lr': 4.79e-06, 'epoch': 0.55}
Checkpoint saved: checkpoint-760 (step 760)
step 761-775 继续运行后 → "Terminated"
```

---

**关键发现**：CE loss ~114.79 极高（正常 LM 应在 2-4 范围），PPL 溢出到 inf。训练 loss 同样在 106-116 范围。训练日志末尾出现 "Terminated"，进程可能已被杀。这表明**模型训练已经 collapse**——loss 没有收敛，反而维持在 100+ 的异常水平。

---
