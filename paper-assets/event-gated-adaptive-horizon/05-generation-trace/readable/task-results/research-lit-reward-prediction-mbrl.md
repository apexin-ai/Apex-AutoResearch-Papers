# research lit reward prediction mbrl

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lit-reward-prediction-mbrl_20260514T142855_result.json`
- **Structured JSON:** [`2a47c53e06e951f5510d.json`](../../sessions/2a/2a47c53e06e951f5510d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

39 篇，6 篇新增全部写入。汇总结果：

---

**Direction 1: Reward prediction quality → MBRL performance** (3 篇新增)

| paper_id | venue | relevance | 关联 |
|---|---|---|---|
| `lee2024dreamsmooth` | ICLR 2024 | 5 | 直接证明 reward prediction 是 MBRL 瓶颈，sparse/ambiguous reward 导致 reward model 输出全零 |
| `ma2024harmonydream` | ICML 2024 | 5 | 观测 vs reward 预测任务在 world model 中存在主导效应，动态平衡可提升 10-69% |
| `lambert2020objective` | L4DC 2020 | 4 | 形式化 objective mismatch——one-step likelihood 与控制性能不相关 |

**Direction 2: MBRL 中的 seed sensitivity / training instability** (1 篇新增，已有 5 篇覆盖)

| paper_id | venue | relevance | 关联 |
|---|---|---|---|
| `bjorck2022variance` | ICLR 2022 | 3 | RL 方差主要来自训练早期的 outlier runs，与我们 seed 2 早期分叉一致 |

已有条目 (`henderson2018deep`, `nikishin2022primacy`, `qiao2023mind`, `hussing2024dissecting`, `barkley2024stealing`) 已充分覆盖此方向。**文献空白注记**：无论文专门研究 Dreamer 家族中 reward prediction 退化导致的 seed-dependent instability——这是我们的 novelty 点。

**Direction 3: Auxiliary task（reward prediction）的 conditioning 效应** (2 篇新增)

| paper_id | venue | relevance | 关联 |
|---|---|---|---|
| `jaderberg2017unreal` | ICLR 2017 | 4 | 奠基性工作：reward prediction 作为 auxiliary task 主动塑造共享表征 |
| `lyle2021auxiliary` | AISTATS 2021 | 4 | 理论分析：auxiliary task 将表征推向 transition operator 的 top eigenvectors |

**文献空白注记**：无论文研究 Dreamer world model 中 reward head 与 temporal conditioning 的耦合关系——我们发现去掉 dt_embedding 选择性地破坏 reward prediction（而非 dynamics）是一个未被文献覆盖的现象，对 novelty argument 有价值。

---
