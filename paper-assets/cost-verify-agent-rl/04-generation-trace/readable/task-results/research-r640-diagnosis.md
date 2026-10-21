# research r640 diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r640-diagnosis_20260517T173203_result.json`
- **Structured JSON:** [`264827e847443eb5db01.json`](../../sessions/26/264827e847443eb5db01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### Q3: reward 信号是什么？

`step_rewards.py` 中的 `assign_step_rewards()` 定义了非二值的 per-step reward：
- **中间步**: 如果 action invalid → `-0.1`，否则 `0`
- **终端步**: `episode_reward`（二值 0/1） + penalty（如 invalid）

然后 `compute_step_discounted_returns()` 做反向折扣：`R_t = r_t + γ * R_{t+1}`（γ=0.95）

### Q5: hsweep_h2 的 reward config

hsweep_h2 config 没有显式设置 `invalid_action_penalty_coef`，代码默认值为 **0.1**（`agent_trainer.py:959`）。所以该实验确实使用了 penalty shaping。

### Q4: step_return 与 advantage 的关系（关键发现）

`compute_grpo_step_advantage()` 实现：
```
advantage[i] = (step_return[i] - mean(group)) / (std(group) + eps)
```

**advantage 就是 step_return 的 z-score 归一化**。两者在同一 group（uid）内 r = 1.0（数学恒等），跨 group 由于不同 μ/σ 才会 < 1.0。

logged advantage 还额外有一个 response_mask 平均化的 artifact：
```python
_adv_val = float(advantages[_i].mean())  # 包含 mask 中的零
```
→ 实际记录值 = scalar_advantage × fill_ratio（逐样本变化），进一步降低了 r。

### Q2: within-episode advantage 是否相同？

否。Episode 95（failed, uid="11"）的 7 个 window 有不同的 step_return（-0.41 到 -0.23）和不同的 advantage。variation 完全由 `invalid_action_penalty` 累积造成——不同 window 后续有不同数量的 invalid actions。

### Q1: training step 信息

log 中无 training_step 字段，共 600 条 = 3 次 step × 200 samples/step，无法按 step 分段。

---

## 最终判定

**r(adv, step_return) = 0.640 的来源是 (b) + (a) 的混合：**

**(b) 同源/近同义反复（主因）**：advantage 就是 step_return 的 group z-score 归一化。两者是同一变量的两种表示。r 从 1.0 降到 0.640 的原因是：
1. 跨 group 池化（不同 uid 有不同 μ/σ）
2. response_mask 平均化 artifact（不同 window 的 fill_ratio 不同）

**(a) invalid_action_penalty（辅因）**：penalty=0.1 使得 failed episode 内的 step_return 非零且有 variation，制造了"看似有 local differentiation"的假象。但这个 variation 只反映 format errors（invalid actions），不反映 task progress。

**结论：r=0.640 不反驳 sign misattribution 假说。它是分析伪影——测量了同一变量的两个数学相关表达，不代表真正的 per-window credit assignment。**

---
