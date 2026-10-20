# ops urgent progress check 0518b

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-progress-check-0518b_20260518T130149_result.json`
- **Structured JSON:** [`1c8319eb30e8400de578.json`](../../sessions/1c/1c8319eb30e8400de578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```
exp_007 (r=0.2, cuda:0, PID 188503): ALIVE | Gen 1/5 完成, Gen 2 训练中 (step 2800, generating done)
exp_008 (r=0.3, cuda:1, PID 194372): ALIVE | Gen 1/10 完成, Gen 2 生成中 (13120/35000 samples)

GPU:
  GPU0: 25017 MiB, 99% util (exp_007)
  GPU1: 25017 MiB, 94% util (exp_008)
```

**已完成 gen 数据：**

| | gen0 (baseline) | gen1 |
|---|---|---|
| **exp_007 (r=0.2)** | eff_rank=417.5, log_det=2366.7, ppl=9.554, d4=0.7414 | eff_rank=476.7, log_det=2367.5, ppl=10.282, d4=0.6737 |
| **exp_008 (r=0.3)** | eff_rank=417.5, log_det=2366.7, ppl=9.554, d4=0.7414 | eff_rank=476.9, log_det=2366.1, ppl=10.193, d4=0.6894 |

**SLV 趋势（log_det）：**
- exp_007: 2366.7 → 2367.5 (+0.8, 微涨)
- exp_008: 2366.7 → 2366.1 (-0.6, 微降)

两个实验 gen1 都出现 eff_rank 跳升 (~417→477)、ppl 上升、d4 下降，符合典型的首代退化模式。r=0.3 的 d4 保留略优于 r=0.2 (0.6894 vs 0.6737)，real data 补充效果可见。log_det 目前变化极小，需要更多 gen 数据才能判断趋势方向。

---
