# analysis rssm onset checkpoint

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm-onset-checkpoint_20260526T113330_result.json`
- **Structured JSON:** [`e6eeff7f86a36414f52c.json`](../../sessions/e6/e6eeff7f86a36414f52c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the analysis:

## 结果

### 中间 checkpoint 不存在
所有实验只保留 `latest.pt`（DreamerV3 覆盖写入），**无法对 onset 时刻 checkpoint 运行 v3 standardized 分析**。

### Cheetah exp_097 CIVO 时间线
| Step | ve_ratio | alert |
|------|----------|-------|
| 15K | 0.009 | 0 |
| 25K | 0.120 | 0 |
| 35K | 0.350 | 0 |
| **45K** | **2.265** | **1** |
| 55K | 0.758 | 0 |
| 65K | 0.232 | 0 |
| 75K-105K | 0.17-0.31 | 0 |

CIVO alert 仅在 45K 触发一次（ve_ratio 从 0.35 暴涨到 2.26），之后回落。训练 loss 在 45K 无异常——position/velocity/reward loss 全部单调下降。

### 已有 RSSM 时序数据（exp_066b，Walker seed 1）
这是唯一保存了中间 checkpoint fidelity 的实验：

| Step | reward_ratio | obs_ratio |
|------|-------------|-----------|
| 10K | 0.89× | 0.99× |
| 20K | **1.22×** | 1.09× |
| 25K | **1.53×** | 1.08× |
| **35K** (Walker onset) | **1.49×** | **1.14×** |
| 45K | 1.38× | 1.15× |
| 60K | **1.80×** | 1.13× |
| 65K | 1.76× | 1.20× |

Walker 的 fidelity gap 从 ~20K 出现后 **从未闭合**，持续增长到训练结束。Final checkpoint (exp_008d): obs=1.35×, reward=1.63×。

### Final checkpoint 对比

| Env | Model | obs_ratio | reward_ratio |
|-----|-------|-----------|--------------|
| Cheetah | trained_dt_emb (105K) | 1.12× | **1.00×** |
| Cheetah | no_dt_emb | 1.03× | 1.01× |
| Walker | trained_dt_emb (final) | 1.35× | 1.63× |
| Walker | baseline | 1.57× | 1.56× |

### 结论

1. **无法直接验证** onset 时刻是否存在 transient RSSM fidelity gap——45K checkpoint 不存在
2. **Walker 代理数据**表明 gap 在 onset 前就已存在（~20K）且**从未闭合**
3. **Cheetah reward=1.00×** 有两种可能：(a) Cheetah 从未有 reward fidelity gap；(b) 曾有 transient gap 后闭合。训练 loss 不支持 (b)——45K 处无 loss 异常
4. CIVO alert 在 45K 的 ve_ratio=2.26 spike 是 **value function calibration 问题**（delta_ve=1.92），不是 RSSM fidelity 问题

**建议**：未来实验在 training 中每 10K 步跑 RSSM fidelity check（如 exp_066b 做的），或保留中间 checkpoint，才能回答这个问题。

---
