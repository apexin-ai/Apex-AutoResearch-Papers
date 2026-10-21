# ops analyze a000 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_analyze-a000-s42_20260514T233814_result.json`
- **Structured JSON:** [`5464a95267c1ad64d82e.json`](../../sessions/54/5464a95267c1ad64d82e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无日志文件。配置确认 `synthetic_ratio=0.0`（纯 real data）。下面是分析结果：

---

## α=0.0 Null Control 分析结果

### 配置确认
- Model: Pythia-410M, 10 generations, 5000 steps/gen, seed=42
- `synthetic_ratio=0.0` — 纯 real data 再训练

### Gen 0 vs Gen 10 核心指标对比

| 指标 | Gen 0 | Gen 10 | 变化幅度 |
|------|-------|--------|---------|
| token_entropy | 3.2342 | 3.0693 | **-5.1%** |
| ece | 0.0108 | 0.0164 | +51.7% |
| perplexity | 26.95 | 21.11 | **-21.7%** |
| distinct_1 | 0.0982 | 0.0847 | -13.8% |
| distinct_2 | 0.5178 | 0.4672 | -9.8% |
| distinct_3 | 0.8127 | 0.7760 | -4.5% |
| effective_rank | 46.61 | 44.82 | -3.8% |
| mauve | 0.0341 | 0.0303 | -11.0% |

### 趋势分析

**关键发现：存在非平坦 baseline。**

- **Perplexity 下降 -21.7%**：gen_0→gen_1 骤降（26.95→19.30），之后 gen_1→gen_10 近平坦（19.30→21.11，缓慢上升）。初始大跳反映模型对训练数据的快速适应（overfitting to train set），非合成数据效应。
- **Token entropy 下降 -5.1%**：同样 gen_0→gen_1 骤降后趋稳（gen_1-10 在 2.99-3.07 波动，无单调趋势）。
- **ECE 上升 +51.7%**：从 0.0108 上升到 0.0164。gen_1-10 区间在 0.011-0.017 波动，**有轻微上升趋势但幅度小**（绝对值仅 ~0.006）。
- **Distinct-n 下降**：gen_0→gen_2 降后趋稳，gen_2-10 区间波动 <1%。

### 结论

1. **Gen 0→1 的初始跳跃是 baseline artifact**：模型首次在 train set 上再训练 5000 步后快速适应，ppl/entropy 降低是正常过拟合行为，与合成污染无关。分析 α>0 实验时应将此 baseline drift 作为扣除项。

2. **Gen 1-10 区间近似平坦**：排除初始跳跃后，核心 canary 指标（token_entropy, distinct_n, effective_rank）无显著单调趋势，波动幅度 <2%。

3. **ECE 有轻微 drift**（~0.005 绝对值），可能是 calibration 在重复训练下自然漂移。α>0 实验中 ECE 的 signal 需与此 baseline drift 做差。

4. **Null control 基本符合预期**：无类似 model collapse 的加速退化模式。α>0 实验中超过此 baseline 的变化量可归因于合成数据污染。

---
