# ops exp007 progress check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp007-progress-check_20260518T145239_result.json`
- **Structured JSON:** [`71778a50ddf102040b13.json`](../../sessions/71/71778a50ddf102040b13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the status:

```
exp_007 (r=0.2): ALIVE (6h01m uptime) | Gen 2/5 完成 | 当前阶段: Gen 3 生成中 (36800/40000 samples)

  Gen 0: log_det=2366.7, eff_rank=417.6, ppl=9.554, d4=0.741
  Gen 1: log_det=2367.5, eff_rank=476.7, ppl=10.282, d4=0.674, loss=1.765
  Gen 2: log_det=2358.3, eff_rank=481.6, ppl=10.741, d4=0.498, loss=1.671

  SLV趋势: top1 急降 (1943→961→882), eff_rank 上升 (418→477→482)
  log_det 稳定 (2367→2367→2358), ppl 缓慢上升, d4 持续下降

exp_008 (r=0.3): ALIVE | Gen 2/10 完成 | 当前阶段: Gen 3 生成中 (11520/35000 samples)

  Gen 0: eff_rank=417.5, ppl=9.554, d4=0.741  (same baseline)
  Gen 1: eff_rank=476.9, ppl=10.19, d4=0.689
  Gen 2: eff_rank=484.2, ppl=10.59, d4=0.489, loss=1.774
```

r=0.2 和 r=0.3 的 Gen 0-2 趋势接近：eff_rank 升、ppl 升、d4 降。r=0.3 的 d4 下降略快 (0.489 vs 0.498)，但 ppl 稍低 (10.59 vs 10.74)。log_det 在 r=0.2 上 Gen 2 开始微降 (2358 vs 2367)，后续 gen 是否加速下降值得关注。

---
