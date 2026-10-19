# ops restore plan005

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restore_plan005_20260515T202723_result.json`
- **Structured JSON:** [`cee3d580fac472ad44b5.json`](../../sessions/ce/cee3d580fac472ad44b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### (1) plan_005 subsumption test — **已正常完成** (EXIT_CODE=0)

PID 129873 已退出，但日志显示实验跑完了全部 50 个样本，结果已保存到 `results/subsumption_test/subsumption_results.json` (15KB, May 16 04:20)。

关键结果：
| 指标 | 值 |
|------|-----|
| Linearity ratio | 0.2644 ± 0.0073 |
| Magnitude ratio | 0.1578 ± 0.0088 |
| Cosine similarity | 0.1962 ± 0.0268 |
| ‖D(s)‖ mean | 482.65 |
| ‖D(c)‖ mean | 76.20 |
| ‖interaction‖ | 147.74 |

结论：**Weak subsumption — significant non-linear interaction detected.** SPON 校正项与 predictor 蒸馏项之间存在明显的非线性交互，不能简单叠加。

### (2) 采取的操作

无需恢复。plan_005 是正常退出，不是被 kill。

cuda:1 上的 PID 131619 也已退出（ps 查不到），nvidia-smi 可能是缓存残留。

### (3) bce_isocompute_v2 (PID 129187) — **运行中**

状态 `Rl`（running），当前 step 600/1000，loss=0.6696，1.05s/step，预计还需 ~7 分钟完成。

---
