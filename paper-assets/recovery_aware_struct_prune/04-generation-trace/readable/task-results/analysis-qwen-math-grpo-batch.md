# analysis qwen math grpo batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_math_grpo_batch_20260516T154535_result.json`
- **Structured JSON:** [`e331d6c90c07d1a6b5ea.json`](../../sessions/e3/e331d6c90c07d1a6b5ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the complete analysis:

---

## 实验结果分析

```
=== grpo_rasp_qwen_math_v3 (RASP 20%) ===
训练状态: 正常完成 (EXIT_CODE=0)
总 steps: 100/100
Collapse: YES | onset: step 1 (immediate) | type: PERMANENT
frac_reward_zero_std: 0.65 → 0.675 (range 0.55-0.70, sustained high)
Reward: 0.049 → 0.061 (peak: 0.083 at step 20)
Gradient norm: 0.73 → 1.62 (spike to 14.88 at step 80)
Completion length: 1015 → 1006 (stuck near 1024, clipped_ratio 0.975-1.0)
关键发现: 模型从一开始就陷入退化生成——几乎所有补全都达到 max_length 1024，
  极少自然终止。entropy 极低 (0.065-0.08)，模型生成高度重复。
  与 DeepSeek RASP 20% 类似的 permanent collapse，但严重程度稍轻
  (frac=0.55-0.7 vs DeepSeek 0.95)。
```

```
=== grpo_standard_qwen_math_v3 (Standard 20%) ===
训练状态: 正常完成 (EXIT_CODE=0)
总 steps: 100/100
Collapse: YES | onset: step 1 (immediate) | type: PERMANENT
frac_reward_zero_std: 0.75 → 0.85 (peak: 0.90 at step 30)
Reward: 0.063 → 0.044 (peak: 0.069 at step 80)
Gradient norm: 10.5 → 0.40 (spike to 130 at step 80, otherwise <2)
Completion length: 943 → 921 (clipped_ratio 0.83-0.89)
关键发现: COLLAPSE 比 RASP 更严重！frac_reward_zero_std 持续 0.75-0.9，
  意味着 75-90% 的 batch 无任何 reward 信号。grad_norm 大部分时间极低 (<0.2)
  说明梯度消失，仅 step 80 爆发性 spike (130)。entropy 较高 (0.17-0.20) 
  表明输出有一定多样性但无法产生正确答案。
```

```
=== grpo_rasp_25_qwen_math (RASP 25%) ===
训练状态: 正常完成 (EXIT_CODE=0)
总 steps: 100/100
Collapse: NO
frac_reward_zero_std: 0.575 → 0.35 (趋势下降，健康!)
Reward: 0.112 → 0.206 (peak: 0.225 at step 80)
Gradient norm: 0.29 → 1.99 (稳定, range 0.3-4.3)
Completion length: 773 → 812 (clipped_ratio 0.64-0.72, 大量自然终止)
关键发现: 无 collapse！frac_reward_zero_std 从 0.575 逐步降至 0.35，
  reward 是 20% 模型的 3-4x。模型能正常生成有意义的数学解答并自然终止。
  这与预期完全相反——25% 剪枝反而没有 collapse。
```

```
=== grpo_standard_25_qwen_math (Standard 25%) ===
训练状态: 正常完成 (EXIT_CODE=0)
总 steps: 100/100
Collapse: NO (但有严重训练不稳定)
frac_reward_zero_std: 0.375 → 0.325 (range 0.225-0.425, 低且健康)
Reward: 0.201 → 0.182 (peak: 0.209 at step 80)
Gradient norm: 3.22 → 4.78 (spike to 23 at step 90)
Completion length: 511 → 527 (clipped_ratio 0.32-0.39, 最短补全)
关键发现: 无 reward collapse，但有严重 KL/loss 爆炸：
  - Step 20: kl=56.08, loss=2.64
  - Step 80: kl=4.1e6(!), loss=2.2e5(!)
  模型已严重偏离 reference，但仍产出有效答案。这是另一种不稳定模式。
```

---

## 对比总结表

| 维度 | RASP 20% | Standard 20% | RASP 25% | Standard 25% |
|------|----------|-------------|----------|-------------|
| Collapse | YES (permanent) | YES (permanent, 更严重) | **NO** | **NO** |
| frac_zero_std (final) | 0.675 | 0.85 | 0.35 | 0.325 |
| frac_zero_std (peak) | 0.70 | **0.90** | 0.575 | 0.425 |
| Reward (final) | 0.061 | 0.044 | **0.206** | 0.182 |
| Reward (peak) | 0.083 | 0.069 | **0.225** | 0.209 |
| Comp length | ~1010-1024 | ~920-950 | ~750-812 | ~510-595 |
| Clipped ratio | 0.975-1.0 | 0.83-0.89 | 0.64-0.72 | 0.32-0.39 |
| Entropy | 0.065-0.08 | 0.17-0.20 | 0.09-0.12 | 0.23-0.26 |
| KL stability | 正常 | 正常 | 正常 | **爆炸** (4.1e6) |
| Grad norm stability | spike to 14.9 | spike to 130 | 稳定 | spike to 23 |

---

## 与 DeepSeek 对比 & C2 验证结论

**C1 (Reward-accuracy decoupling)**:  部分复现。20% 模型的 reward 始终极低 (0.03-0.08)，与模型实际生成能力脱钩。但 25% 模型反而不脱钩。

**C2 (Collapse severity gradient: RASP > Standard > Unpruned)**:  **未复现，甚至反转！**

- DeepSeek 上：RASP 20% collapse 最严重 (frac→0.95), Standard 20% 轻微 (transient dip)
- Qwen Math 上：**Standard 20% collapse 更严重** (frac=0.75-0.9) > RASP 20% (frac=0.55-0.7)
- 梯度方向完全反转：Standard > RASP

**25% 加剧 collapse**: **未复现，完全相反！**

- 25% 模型（RASP 和 Standard 均）无 collapse，reward 是 20% 的 3-4 倍
- 可能原因：25% 剪枝后模型"更笨"但更 plastic——生成更短、更多样的输出，不容易卡在退化循环中；20% 模型保留了更多能力但恰好陷入了 max-length repetition 陷阱

**核心发现**：Qwen2.5-Math-7B 的 collapse 动态与 DeepSeek 显著不同。C2 的 collapse gradient 在此模型上不成立。这可能意味着 collapse sensitivity 是高度模型依赖的，不是一个普适的 pruning→GRPO 规律。

---
