# diagnose 5090b fewnerd t ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_5090b_fewnerd_t_ablation_20260521T003622_result.json`
- **Structured JSON:** [`a36cedcc33057f9d579f.json`](../../sessions/a3/a36cedcc33057f9d579f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验都还在运行，进度如下：

| 实验 | GPU | 进度 | 已推理时间 | 预计剩余 |
|------|-----|------|-----------|---------|
| **T=0.5** (exp_fewnerd_t05_s42) | cuda:0 (93% util) | **55%** (21009/37648) | ~10 min | ~8 min |
| **T=0.8** (exp_fewnerd_t08_s42) | cuda:1 (87% util) | **68%** (25726/37648) | ~12 min | ~6 min |
| **T=1.2** (exp_fewnerd_t12_s42) | cuda:2 (93% util) | **93%** (35089/37648) | ~17 min | ~1.5 min |

**说明：**
- 进程启动时间显示为 06:40 UTC（May 21），而非 22:41 UTC May 20。看起来这批是重启过的，实际推理阶段运行了约 10-17 分钟。
- 总共 37,648 个 prompts（N=8 × 4,706 examples）。
- 推理速度 ~5,750-5,860 toks/s input, ~3,080-3,140 toks/s output。
- 尚无输出文件（完成后写入 output/ 目录）。

**T=1.2 将在 ~1-2 分钟内完成，T=0.8 ~6 分钟，T=0.5 ~8-9 分钟。**

**cuda:3** 完全空闲（0% util, 2 MiB memory）。可以铺新任务，比如另一个 seed 的实验或其他数据集的 T-ablation。

要不要等完成后再来拉 metrics？或者先安排 cuda:3 的任务？

---
