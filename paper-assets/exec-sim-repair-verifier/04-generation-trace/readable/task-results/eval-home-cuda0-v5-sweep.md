# eval home cuda0 v5 sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-cuda0-v5-sweep_20260514T223019_result.json`
- **Structured JSON:** [`9726ee2d58ff373c4168.json`](../../sessions/97/9726ee2d58ff373c4168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sweep 脚本正在等待 ckpt-600 完成后自动继续跑 ckpt-4000 → 4200 → 4400 → 4600。

## 当前状态汇总

**GPU cuda:0**: 100% 利用率，31.7/32.6 GB 显存

**正在运行**: v5-ckpt600 val@5120 eval（PID 3179262，启动于 15:24）

**Sweep 脚本已部署**: PID 3180424，等 ckpt-600 完成后自动按序执行 ckpt-4000 → 4200 → 4400 → 4600 的 val@5120 eval

**v5 默认 eval 结果（max_seq_length=2048）汇总**:

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|-----------|----------|----------|---------|---------|----------------|
| ckpt-600  | 76.74    | 73.74    | 64.88   | 82.61   | +3.78pp        |
| ckpt-4000 | 81.51    | 72.56    | 56.90   | 88.23   | +8.55pp        |
| ckpt-4200 | 80.64    | 72.10    | 56.66   | 87.54   | +7.69pp        |
| ckpt-4400 | 82.11    | 73.94    | 59.34   | 88.54   | +9.16pp        |
| **ckpt-4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39pp** |

ckpt-4600 在 accuracy 和 f1_macro 上均最优。val@5120 结果待 sweep 完成后收集。

---
