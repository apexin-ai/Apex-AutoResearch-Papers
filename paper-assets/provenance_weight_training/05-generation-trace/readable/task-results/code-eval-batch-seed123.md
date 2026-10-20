# code eval batch seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_batch_seed123_20260514T142912_result.json`
- **Structured JSON:** [`4249991571975d96b5ba.json`](../../sessions/42/4249991571975d96b5ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法验证通过。

**结果汇总：**

- **b=2.0, b=3.0 的 eval 已完成**，结果在 `output/eval_results/grid_b{2,3}_0_seed123_eval.json`
- **b=5.0 还在训练**（step 5092/6103），脚本已准备好等训练完成后跑

**脚本路径：** `/root/provenance_weight_training/run_eval_missing_seed123.sh`

**运行方式：** b5.0 训练完成后（出现 `final/` 目录），执行：
```
CUDA_VISIBLE_DEVICES=<空闲GPU> bash run_eval_missing_seed123.sh
```

脚本会自动跳过已有 eval 结果的 checkpoint 和尚未完成训练的 checkpoint。

---
