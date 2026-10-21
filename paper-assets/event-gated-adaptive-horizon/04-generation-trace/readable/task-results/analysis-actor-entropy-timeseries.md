# analysis actor entropy timeseries

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor-entropy-timeseries_20260526T115350_result.json`
- **Structured JSON:** [`a1c11cfb680a4244a164.json`](../../sessions/a1/a1c11cfb680a4244a164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成。汇报如下：

## Actor Entropy 时序分析

### 数据可用性
- **Healthy**: exp_001_baseline, exp_008a, exp_100 — 全部可用
- **Collapsed**: exp_008d, exp_006, exp_097 — 全部可用
- **Mitigated**: 仅 exp_008e_v3 (s0) 可用，**exp_070/080/081 不存在于服务器上**

### 各组趋势

**Healthy（蓝）**
- 所有实验从 ~8.1 开始，快速下降至 -5.2 区间（~85K step）
- exp_001 baseline 长跑 505K step，在 105K 后出现 **entropy 回升**（-5.2 → -1.5），对应 return 从 ~600 提升到 ~950，说明 actor 在策略收敛后重新探索
- exp_008a/exp_100 在 105K 结束时稳定在 -5.24/-5.27，走势与 baseline 早期完全一致

**Collapsed（红）**
- exp_008d: 熵下降明显更慢，15K 时仍为 +0.48（healthy 已到 -1.15），55K 止于 -4.88 即训练终止（仅 6 个数据点）
- exp_006: 65K 步内下降到 -5.12 后训练终止（7 个数据点），深度接近 healthy 但 return 已崩至 133
- **exp_097（cheetah）最突出**：35K 触底 -4.91 后 entropy **反弹**至 105K 时的 -0.69，这不是 baseline 式的健康回升——伴随的是 return 从 359 降到 148，说明策略在退化过程中丧失确定性

**Mitigated（绿）**
- exp_008e_v3: 走势与 healthy 组几乎完全重合，105K 时 -5.18，无异常波动

### Collapsed 组 CIVO onset 与 entropy 关系
- exp_008d: entropy 在训练全程偏高（下降慢），没有明确的 onset 拐点——entropy 是**持续受损**而非突变
- exp_006: entropy 曲线本身无明显异常，collapse 体现在 ve_ratio 飙升（55K 时 0.93，65K 时 2.72）而非 entropy 剧变
- exp_097: 35K-105K 的 entropy 反弹是最清晰的异常信号，与 performance degradation 同步

### 图表路径
- PDF: `/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/actor_entropy_comparison.pdf`
- PNG: `/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/actor_entropy_comparison.png`

---
