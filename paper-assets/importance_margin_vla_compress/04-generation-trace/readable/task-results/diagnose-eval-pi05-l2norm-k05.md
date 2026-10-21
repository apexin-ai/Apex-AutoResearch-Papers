# diagnose eval pi05 l2norm k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k05_20260521T072610_result.json`
- **Structured JSON:** [`21aea7a5081939b3f4c6.json`](../../sessions/21/21aea7a5081939b3f4c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### eval_pi05_l2norm_k05_object_seed42

**进程死因：正常完成退出，非异常。**

- PID 838823 已不存在，但 log 显示所有 10 个 task × 50 episodes 全部跑完
- 结束时间：2026-05-21 15:23:00（耗时 95.6 分钟）
- 无 OOM、无 CUDA error、无异常
- 结果文件已保存：`eval_results/pi05_l2norm_k0.50_libero_object.json`

**结果：SR = 33.4%（vs baseline 98.2%，-64.8pp）**

Per-task 分布极不均匀：
| Task | SR |
|------|-----|
| T0 alphabet_soup | 50% |
| T1 cream_cheese | 14% |
| T2 salad_dressing | 0% |
| T3 bbq_sauce | 0% |
| T4 ketchup | 54% |
| T5 tomato_sauce | 38% |
| T6 butter | 28% |
| T7 milk | 64% |
| T8 chocolate_pudding | 38% |
| T9 orange_juice | 48% |

**假设"CV=0.055 predicts immunity"被强烈否定。** π0.5 的线性投影虽然产生均匀 L2norm 分布（低 CV），但 50% token removal 仍导致灾难性性能下降。

### eval_pi05_random_k05_object_seed42

**正在运行中**，15:21 启动，当前在 T0 ep=20（SR 85%）。GPU 0 上有活跃进程。无异常。

### 不需要重跑

L2norm 实验已完整完成，结果已保存。Random 实验正在正常推进。

---
