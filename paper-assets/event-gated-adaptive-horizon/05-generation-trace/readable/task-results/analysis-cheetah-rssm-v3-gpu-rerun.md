# analysis cheetah rssm v3 gpu rerun

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cheetah-rssm-v3-gpu-rerun_20260526T080630_result.json`
- **Structured JSON:** [`9bd9186ab803976d1e79.json`](../../sessions/9b/9bd9186ab803976d1e79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 运行完成（119.5秒）。结果如下：

## Cheetah trained_dt_emb RSSM v3 标准化分析结果

**exp_097_cheetah_008d_s3** | 112 episodes, 4480 transitions | cuda:0 | seed=42

| Metric | dt=1 | dt=2 | Ratio (dt2/dt1) |
|--------|------|------|-----------------|
| **obs_MSE** | 5.1314 (±4.847) | 4.8513 (±4.283) | **0.95×** |
| **reward_MAE** | 0.1406 (±0.166) | 0.1408 (±0.166) | **1.00×** |

**Per-key obs_MSE:**

| Key | dt=1 | dt=2 | Ratio |
|-----|------|------|-------|
| position | 0.00427 | 0.00835 | 1.95× |
| velocity | 10.259 | 9.694 | 0.94× |

关键发现：**旧的 2.78× reward gap 不成立。** trained_dt_emb 模型在 cheetah 上 dt=1 vs dt=2 的 reward ratio 几乎是 1.00×（reward_MAE 差异 < 0.2%），obs ratio 甚至略低于 1（0.95×，dt=2 预测反而略好于 dt=1）。这说明该模型的 multi-step prediction quality 非常稳定，没有显著退化。

JSON 已保存至 `logdir/rssm_v3_cheetah_trained_dt_emb_gpu.json`。

---
