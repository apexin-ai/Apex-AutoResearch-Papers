# ops cqa1 collect goal long results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-collect-goal-long-results_20260521T023248_result.json`
- **Structured JSON:** [`3314ef879ea545f441f0.json`](../../sessions/33/3314ef879ea545f441f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成。

```
eval_xvla_goal_k09_seed42:
  status: completed
  suite: libero_goal
  success_rate: 70.2% (351/500)
  95% CI: [66.0%, 74.0%]
  per_task:
    T0=100% (open the middle drawer of the cabinet)
    T1=82%  (put the bowl on the stove)
    T2=96%  (put the wine bottle on top of the cabinet)
    T3=6%   (open the top drawer and put the bowl inside)
    T4=96%  (put the bowl on top of the cabinet)
    T5=0%   (push the plate to the front of the stove)
    T6=78%  (put the cream cheese in the bowl)
    T7=100% (turn on the stove)
    T8=46%  (put the bowl on the plate)
    T9=98%  (put the wine bottle on the rack)

eval_xvla_goal_k05_seed42:
  status: completed
  suite: libero_goal
  success_rate: 61.0% (305/500)
  95% CI: [56.7%, 65.2%]
  per_task:
    T0=82%  (open the middle drawer of the cabinet)
    T1=98%  (put the bowl on the stove)
    T2=100% (put the wine bottle on top of the cabinet)
    T3=40%  (open the top drawer and put the bowl inside)
    T4=100% (put the bowl on top of the cabinet)
    T5=0%   (push the plate to the front of the stove)
    T6=24%  (put the cream cheese in the bowl)
    T7=74%  (turn on the stove)
    T8=92%  (put the bowl on the plate)
    T9=0%   (put the wine bottle on the rack)

eval_xvla_baseline_long_seed42:
  status: completed
  suite: libero_10 (注意：日志显示 suite 是 libero_10，不是 libero_long)
  success_rate: 94.0% (470/500)
  95% CI: [91.6%, 95.8%]
  per_task:
    T0=96%  (put both the alphabet soup and the tomato sauce in the basket)
    T1=68%  (put both the cream cheese box and the butter in the basket)
    T2=100% (turn on the stove and put the moka pot on it)
    T3=98%  (put the black bowl in the bottom drawer of the cabinet and close it)
    T4=94%  (put the white mug on the left plate and put the yellow and white mug on the right plate)
    T5=96%  (pick up the book and place it in the back compartment of the caddy)
    T6=94%  (put the white mug on the plate and put the chocolate pudding to the right of the plate)
    T7=96%  (put both the alphabet soup and the cream cheese box in the basket)
    T8=100% (put both moka pots on the stove)
    T9=98%  (put the yellow and white mug in the microwave and close it)
```

注意 baseline 的 keep_ratio=1.00，且 suite 实际是 `libero_10` 而非 `libero_long`——文件名可能有误。

---
