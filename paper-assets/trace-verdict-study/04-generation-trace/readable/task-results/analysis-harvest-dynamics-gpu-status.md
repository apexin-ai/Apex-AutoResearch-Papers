# analysis harvest dynamics gpu status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_dynamics_gpu_status_20260519T053914_result.json`
- **Structured JSON:** [`3fbffb03fb94a2b96d01.json`](../../sessions/3f/3fbffb03fb94a2b96d01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
GPU STATUS:
  cuda:0: Idle, 31°C, 49GB/98GB (model loaded, not computing)
  cuda:1: 100% util, 70°C, 41GB/98GB — running full_trace dynamics (PID 485347)

EXCEPTION_ONLY DYNAMICS (qwen7b_exception_only_dynamics_seed42):
  Status: ✅ 完成
  Learning curve:
    step  50: acc=0.9933  loss=0.1897  (pass_f1=0.9953, fail_f1=0.9883)
    step 100: acc=0.9933  loss=0.1272
    step 150: acc=0.9933  loss=0.0793
    step 200: acc=0.9983  loss=0.0475  ← 跳跃点，之后饱和
    step 250: acc=0.9983  loss=0.0437
    step 300: acc=0.9983  loss=0.0378
    step 350: acc=0.9983  loss=0.0333
    step 400: acc=0.9983  loss=0.0347
    step 444: acc=0.9983  loss=0.0329  (pass_f1=0.9988, fail_f1=0.9971)
  
  关键发现: step 200 饱和 (99.83%)，之后 loss 继续下降但 acc 不再变化
  Pass precision=1.0 (零 false positive), Fail recall=1.0 (零 false negative for fail)

FULL_TRACE DYNAMICS (qwen7b_full_trace_dynamics_seed42):
  Status: 🔄 训练中 step 356/444 (80%)
  ~28s/step, 剩余 88 steps ≈ 41 min 训练 + batch eval ≈ 1h15m 完成
  ETA: ~14:55 UTC
  尚无 eval 数据（batch eval 在训练完成后执行）
```

Exception_only 的 dynamics 非常 clean：50 步就到 99.3%，200 步饱和在 99.83%。这个 task 对 Qwen-7B 来说几乎 trivial。full_trace 的 dynamics 对比将更有意义，看是否收敛更慢或有不同的 plateau pattern。

需要我等 full_trace 完成后再收割，还是先用 exception_only 的数据做什么？

---
