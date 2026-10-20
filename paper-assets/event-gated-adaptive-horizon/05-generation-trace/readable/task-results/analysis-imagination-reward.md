# analysis imagination reward

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_imagination_reward_20260515T132929_result.json`
- **Structured JSON:** [`164faec9965bb41bd569.json`](../../sessions/16/164faec9965bb41bd569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**CIVO 在 imagination level 确认成立。**

| Model | dt | Mean Reward Pred | vs dt=1 |
|---|---:|---:|---:|
| exp_008d | 1 | 0.462 | 1.00x |
| **exp_008d** | **2** | **1.386** | **3.00x** |
| exp_008d | 3 | 0.800 | 1.73x |
| exp_008d | 4 | 0.762 | 1.65x |
| exp_008f (no dt_emb) | 1 | 0.338 | — |
| exp_008f (no dt_emb) | 2 | 0.328 | ~1.00x |

关键发现：

1. **dt=2 imagination reward 是 dt=1 的 3 倍**。从相同初始状态出发，dt=2 的 reward prediction 在 6-7 步内从 0.59 涨到 1.70，而 dt=1 反而从 0.59 降到 0.37。

2. **dt=2 是最具毒性的**——过度乐观程度非单调：dt=2 > dt=3 > dt=4。dt=2 在训练中是最常见的非平凡 dt，使其 embedding 过拟合到 reward-favorable latent space 区域。

3. **与 posterior 分析不矛盾**。Posterior 分析发现 dt=2 underpredicts 真实 reward，那是因为 aggregated reward 本身更大难以预测。但 imagination 中 prior dynamics + dt=2 embedding 会生成"虚假乐观"的 latent 轨迹，reward head 在此产生系统性高估。

4. **exp_008f sanity check 通过**：无 dt embedding 时 dt=1 vs dt=2 差异 ≈ 0，证实膨胀完全由 trained dt embedding 引起。

5. **论文建议**：CIVO 叙述应明确为 imagination-level 现象。主要证据应是 per-step divergence curve（dt=1 vs dt=2 reward prediction 随 rollout step 的分叉图）。

---
