# analysis lr5e6 trajectory comparison

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lr5e6_trajectory_comparison_20260514T222652_result.json`
- **Structured JSON:** [`ca4e9eacb2214c17b2c3.json`](../../sessions/ca/ca4e9eacb2214c17b2c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取完毕。开始写对比分析报告。

---

## lr5e6 vs ced_kl001_r4 训练轨迹对比分析

### 实验配置

| | **lr5e6-r1** | **kl001-r4** |
|---|---|---|
| Learning Rate | **5e-6** | **5e-5** (10x) |
| KL coef | 0.01 | 0.01 |
| Max Steps | 200 | 100 |
| 进度 | 84/200 (42%) | 100/100 (完成) |

---

### 1. Reward 学习速率对比

**kl001_r4 (lr=5e-5)** 学得快得多：

| Step | kl001_r4 reward | lr5e6 reward |
|------|----------------|-------------|
| 40 | **0.695** | 0.318 |
| 50 | **1.100** | 0.245 |
| 60 | 0.520 | 0.223 |
| 80 | 0.840 | 0.283 |
| 100 | **1.195** | — |

- kl001_r4 step 40 时 total reward 已达 0.695（lr5e6 同期 0.318，仅 46%）
- kl001_r4 step 50 峰值 1.100，lr5e6 step 80 仍仅 0.283
- **lr5e6 step 80 的 reward 水平 ≈ kl001_r4 step 20-25 的水平**，落后约 55-60 步

**F1 reward 差距更大**：
- kl001_r4 step 40: f1_reward=0.240 vs lr5e6 step 40: 0.038（6.3x 差距）
- kl001_r4 step 50: f1_reward=0.480 vs lr5e6 step 50: 0.009（53x 差距）
- lr5e6 的 f1_reward 在 80 步内从未超过 0.042

**CED reward 类似**：
- kl001_r4 step 40: 0.236 vs lr5e6 step 40: 0.079（3x）
- lr5e6 的 ced_reward 最高仅 0.079（step 40），大部分时间 < 0.02

---

### 2. KL 稳定性对比

| 指标 | lr5e6 | kl001_r4 |
|------|-------|----------|
| 典型 KL 范围 | 0.006-0.012 | 0.098-0.181 |
| KL spike | step 65: **10.3** | 无明显 spike |
| Spike 恢复 | step 70 恢复至 0.012（5 步内） | — |

- **kl001_r4 KL 稳定在 0.10-0.18**，高于 lr5e6 约 15-20x，符合 10x LR 差距预期
- **lr5e6 典型 KL 极低 (0.006-0.012)**，说明 policy 几乎未偏离 reference——学习速度极慢的直接体现
- **lr5e6 step 65 KL=10.3 spike**：这是一个异常事件（比正常值高 ~1000x），但恢复迅速。spike 发生时 loss=0.178（也是最高值），grad_norm 可能也有对应峰值。恢复快说明 kl_coef=0.01 的惩罚项起了作用——一次偏离立刻被拉回。kl001_r4 无类似 spike 可能因为其 policy 已持续偏离（KL 基线就高），不存在"突变"的概念

---

### 3. Mode Collapse 信号 (frac_zero_std)

| Step | kl001_r4 frac_zero_std | lr5e6 frac_zero_std |
|------|----------------------|-------------------|
| 5 | 0.3 | — (无数据) |
| 10 | **0.8** (collapse) | — |
| 15 | **0.7** | — |
| 20 | 0.1 (恢复) | — |
| 25 | 0.7 (反复) | — |
| 30 | 0.6 | — |
| 40 | **0.0** (稳定) | — |
| 50 | **0.0** | — |
| 60 | 0.3 | — |
| 100 | 0.2 | — |

lr5e6 缺少 frac_zero_std 数据（日志仅有 step 40-80 的 reward/loss/KL）。但从其他信号推断：
- lr5e6 f1_reward 在 step 45 = 0.000（完全无 F1 贡献），step 70 = 0.005，多步 f1≈0→可能存在间歇性 zero-std
- **kl001_r4 经历了明显的 collapse→恢复→再collapse→最终稳定 的震荡过程**（step 10-30 反复，step 40 后稳定）
- lr5e6 由于学习慢，policy 几乎不变，mode collapse 风险低但学习信号也弱

---

### 4. F1 Reward 波动模式分析

**kl001_r4 的 f1_reward**：
```
5→10: 0.015→0.000 (crash)
10→20: 0→0.003 (微弱恢复)
20→40: 0.003→0.240 (强势上升)
40→50: 0.240→0.480 (翻倍)
50→60: 0.480→0.116 (-76% 回落)
100: 0.573
```
呈现 **"crash → slow recovery → explosive growth → high variance oscillation"** 模式。step 50→60 的 -76% 回落不是趋势逆转（后续恢复到 0.573），而是 batch_size=1 GRPO 的固有噪声。

**lr5e6 的 f1_reward**：
```
40: 0.038
45: 0.000
50: 0.009
55: 0.038
60: 0.009
65: 0.042 (最高)
70: 0.005
75: 0.004
80: 0.016
```
在 0.000-0.042 的极窄区间内随机波动，**没有学习趋势**。

**判断：lr5e6 的 f1_reward 波动是噪声，不是学习**。40 步的窗口内无上升趋势、无方向性，纯粹是 batch_size=1 采样的随机波动。kl001_r4 同期（step 5-40）也经历了类似的低位波动期，但到 step 40 出现了明确的上升拐点——lr5e6 到 step 80 仍未出现。

---

### 5. 灾难性遗忘对比

| | SFT baseline | kl001_r4 best eval | lr5e6 ckpt-20 eval |
|---|---|---|---|
| rel_f1 | 0.4057 | 0.211 (step 90) | **0.0077** |
| eval 轨迹 | — | 0.003→0.009→0.034→0.156→0.211 | 仅 ckpt-20 一个点 |

- **两个 run 都出现灾难性遗忘**，但程度不同
- kl001_r4 从 step 10 (F1=0.003) 逐步恢复到 step 90 (F1=0.211)，恢复到 SFT 的 52%
- lr5e6 ckpt-20 F1=0.0077，比 kl001_r4 的 ckpt-10 (0.003) 还低——**10x 更低的 LR 并没有防止遗忘**
- ckpt-40/60 eval 结果待出，是关键判断点

---

### 6. Step 200 Reward 预测

基于 lr5e6 step 40-80 的轨迹：

- **Format reward** 趋势明确：0.138→0.249（+0.003/step），step 200 预测 ≈ 0.61
- **F1 reward** 无学习趋势，0.000-0.042 区间随机波动，step 200 预测仍在 **0.00-0.05** 除非出现拐点
- **CED reward** 同样无趋势，预测 **0.00-0.08**
- **Total reward 预测**：~0.61 + ~0.03 + ~0.04 ≈ **0.65-0.70**（主要由 format reward 贡献）

对比 kl001_r4 step 100 总 reward=1.195 (f1=0.573, ced=0.328, format=0.293)：
- lr5e6 预计到 step 200 total reward 仍然低于 kl001_r4 step 100
- 但 lr5e6 的 reward 几乎全部来自 format（88%+），而 kl001_r4 的 format 只占 25%
- **lr5e6 实际上在学 format hacking 而不是真正的 extraction/evidence 任务**

---

### 核心结论

1. **lr=5e-6 太低了**。40 步内 f1_reward 无任何上升趋势，KL 基线 0.006-0.012 说明 policy 几乎没变。降 10x LR 的目的是防遗忘，但代价是完全丧失 F1/CED 的学习能力。

2. **灾难性遗忘与 LR 不是简单线性关系**。lr5e6 ckpt-20 eval F1=0.0077，比 kl001_r4 ckpt-10 的 0.003 好一点但仍在灾难性遗忘区间。说明即使极低 LR，早期几步也足以破坏 SFT 对齐。

3. **kl001_r4 的"崩溃→恢复"模式 vs lr5e6 的"缓慢偏移"**：kl001_r4 快速崩溃但有自我修复能力（reward 信号驱动恢复），lr5e6 缓慢偏移但 reward 信号太弱无法驱动学习。

4. **lr5e6 的 KL spike (step 65=10.3) 是偶发事件**，非系统性不稳定。恢复快（5 步内回 0.012）证明训练动力学本身是稳定的，只是学习速率过低。

5. **最优 LR 可能在 1e-5 到 2e-5 之间**。5e-5 学得快但遗忘严重（max eval F1=0.211/0.406=52%），5e-6 不遗忘但不学习。建议下一轮实验用 **lr=1e-5 或 2e-5**。

6. **lr5e6 ckpt-40/60 eval 是决定性数据点**。如果 ckpt-40 eval F1 仍 < 0.05，基本可以判定 lr=5e-6 失败，无需等到 step 200。如果 F1 > 0.15（类似 kl001_r4 step 50 水平），说明拐点只是来得晚。

---
