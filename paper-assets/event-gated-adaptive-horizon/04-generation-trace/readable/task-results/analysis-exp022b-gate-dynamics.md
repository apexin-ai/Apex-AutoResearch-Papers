# analysis exp022b gate dynamics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp022b-gate-dynamics_20260517T140002_result.json`
- **Structured JSON:** [`be3f4091654b2ae67c34.json`](../../sessions/be/be3f4091654b2ae67c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。完整数据已保存到 `artifacts/analysis/exp_022b_analysis.json`。

---

## exp_022b Gate 学习动态分析

### 1. Gate Temporal Abstraction: 学到了有意义的时间抽象

Gate **没有退化到 dt=1**。dt_1_frac 从 6.5% 缓慢增长到 14.5%，始终是少数派。

| 阶段 | Steps | dt_mean | 特征 |
|------|-------|---------|------|
| 探索期 | 5k-35k | 4.4→3.5 | 向短 horizon 探索，dt1 增到 12.4% |
| 回弹期 | 35k-55k | 3.5→4.1 | 重新探索长 horizon |
| 收敛期 | 55k-105k | 4.1→3.4 | 稳定在 short-biased 分布 |

最终分布峰值在 dt=2-3（21%+21%），长尾延伸到 dt=8，8 个 dt 值全程都在使用。

### 2. Gate Entropy: 缓慢健康收敛

- 经验熵: 2.01 → 1.90（均匀分布最大值 ~2.08），仅下降 5.5%
- entropy_ratio: 0.97 → 0.91，终态仍保留 91% 的最大熵
- **没有收敛到固定策略**，gate 保留了显著的探索能力

### 3. Eval 曲线: 高原-突破模式

```
5k:   37.4  (近随机)
15k-85k: ~140-170 平台期（高方差）
95k:  247.5  ← 突破
105k: 300.7  ← 最终值，baseline 的 9.1×
```

晚期突破恰好与 gate 收敛到 short-biased 分布同期，暗示 gate 找到了有效的时间结构。

### 4. CIVO: 完全健康

- ve_ratio 峰值 0.22（step 55k），远低于 1.5× 阈值
- ve_ratio 之后单调下降到 0.075
- **civo/alert = 0 全程**，零警报
- 对比 exp_008d（CIVO 崩溃），frozen dt_emb + learned gate 架构彻底消除了 CIVO

### 关键结论

frozen dt_emb + learned gate 架构将时间表征与时间决策分离，阻断了导致 CIVO 的反馈环。Gate 学到了非平凡的时间抽象策略（short-biased 但保留多样性），且与 eval 性能的晚期突破高度相关。

---
