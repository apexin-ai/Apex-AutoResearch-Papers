# analysis mvp c1 s137

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_c1_s137_20260518T131632_result.json`
- **Structured JSON:** [`cf9d3170c7d267f8f2d2.json`](../../sessions/cf/cf9d3170c7d267f8f2d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/mvp_c1_s137_analysis.md`。汇总：

**mvp_c1_s137 训练结果：**

| 指标 | s137 | s42 | 差异 |
|------|------|-----|------|
| final_train_loss | 0.2471 | 0.2437 | +0.0034 |
| avg_train_loss | 0.4423 | 0.4426 | -0.0003 |
| train_runtime (s) | 8549 | 5761 | +48.4% |

两个 seed 的 loss 几乎一致，训练稳定可复现。

**GPU 当前状态：不空闲。** 两个进程在跑：
1. **C1_s42 eval**（PID 25961）— code task，占 17 GB 显存，已运行 ~2.5 小时
2. **mvp_c4_s42 训练**（PID 40217）— condition4_full_tbab，21:16 刚启动

**注意：** s137 训练时长比 s42 长 48%（8549s vs 5761s），大概率是因为 eval 进程同时在 GPU 上运行争抢资源。现在 C4 训练和 eval 又在共享 GPU，可能再次出现类似情况。

---
