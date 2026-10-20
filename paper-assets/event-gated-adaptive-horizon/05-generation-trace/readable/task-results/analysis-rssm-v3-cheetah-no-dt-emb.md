# analysis rssm v3 cheetah no dt emb

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm_v3_cheetah_no_dt_emb_20260526T055747_result.json`
- **Structured JSON:** [`356abd0d0f045daec25c.json`](../../sessions/35/356abd0d0f045daec25c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Cheetah no_dt_emb RSSM v3 标准化分析结果

| 指标 | dt=1 | dt=2 | Ratio (dt2/dt1) |
|------|------|------|-----------------|
| **obs_mse** | 3.8129 ± 3.9308 | 3.8983 ± 3.6096 | **1.02x** |
| **reward_mae** | 0.1282 ± 0.1688 | 0.1288 ± 0.1684 | **1.01x** |

**Per-key obs_mse:**

| Key | dt=1 | dt=2 | Ratio |
|-----|------|------|-------|
| position | 0.00627 | 0.00921 | 1.47x |
| velocity | 7.6196 | 7.7873 | 1.02x |

**元信息：**
- Checkpoint: `exp_092_cheetah_no_dt_emb_s1` (220MB)
- Episodes: 112, Samples: 1000, Seed: 42
- Method: sequential_rollout, Device: cpu
- has_dt_embedding: false
- 输出文件: `logdir/rssm_v3_cheetah_no_dt_emb.json`

**关键发现：** no_dt_emb 在 Cheetah 上 dt2/dt1 ratio 非常接近 1（obs 1.02x, reward 1.01x），说明跳步对预测质量几乎没有影响。position 的 ratio 偏高（1.47x），但绝对误差极小（0.006→0.009），主要误差来源是 velocity（占 obs_mse 99%+）。

---
