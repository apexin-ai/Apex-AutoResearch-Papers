# analysis dt embedding cosine sim

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dt-embedding-cosine-sim_20260526T115405_result.json`
- **Structured JSON:** [`f1f4111f6413268582a7.json`](../../sessions/f1/f1f4111f6413268582a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Cosine Similarity (dt=1 vs dt=2)

| 配置 | 类型 | cos(dt1, dt2) |
|------|------|--------------|
| exp_008d_civo_trigger_s3 | trained Walker | **-0.655** |
| exp_008d_civo_trigger_s4 | trained Walker | **-0.672** |
| exp_059_walker_trained_s5 | trained Walker | **-0.903** |
| exp_010b_cheetah_civo_trigger_s0 | trained Cheetah | **-0.803** |
| exp_097_cheetah_008d_s3 | trained Cheetah | **-0.684** |
| exp_057_frozen_dt_emb_walker_s2 | frozen Walker | -0.150 |
| exp_058_frozen_dt_emb_cheetah_s1 | frozen Cheetah | 0.069 |
| exp_084_frozen_dt_emb_walker_s0 | frozen Walker | 0.203 |
| exp_100_walker_008a_s1 | untrained (008a) | 0.024 |

### 差异模式

- **Trained dt_emb**: dt=1 和 dt=2 的 embedding 强烈反相关（cosine -0.65 ~ -0.9），RSSM 学会将"正常步"和"跳步"编码为几乎相反的方向
- **Frozen dt_emb**: cosine ≈ 0（-0.15 ~ 0.20），停留在随机初始化附近，norms 始终很小（~0.05）
- **Untrained/008a**: cosine ≈ 0.02，几乎正交。注意 dt1_norm=0.72 但 dt2_norm=0.07 — 因为 008a 无 subsample，dt 始终为 1，dt=2 embedding 几乎未被梯度更新
- **训练动态**（Panel B）: 前 25k 步 cosine 急剧下降到 -0.9，之后缓慢回升至 -0.65~-0.85 区间

### 图表路径

- 服务器: `/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/dt_embedding_cosine_similarity.pdf`
- 本地: `artifacts/dt_embedding_cosine_similarity.png`

---
