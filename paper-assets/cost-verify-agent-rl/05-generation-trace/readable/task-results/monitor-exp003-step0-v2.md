# monitor exp003 step0 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp003_step0_v2_20260513T234540_result.json`
- **Structured JSON:** [`75472c718bc8364ad42b.json`](../../sessions/75/75472c718bc8364ad42b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 0 训练指标已出，Step 1 已开始。** 以下是关键数值：

---

### 核心指标（Step 0）

| 指标 | 值 | 评估 |
|------|-----|------|
| **pg_loss** | 0.000176 | 极小但非零，梯度信号微弱 |
| **advantage mean/max/min** | 0.0087 / 2.47 / -0.559 | 有方差但均值接近零 |
| **manager_invalid_action** | **95.3%** | 极高，几乎全是无效动作 |
| **action_is_valid** | 1.9% | 与 invalid 一致 |
| **raw_reward** | 0.0 | 无奖励信号 |
| **avg_episode_return** | 0.0 | 无回报 |
| **success rate** | 0.78% (1/128) | 仅 1 个 episode 成功 |
| **pass@8** | 6.25% | 8 次采样中偶有成功 |
| **ppo_kl** | 0.003 | 极小，模型几乎没变 |
| **actor/entropy** | 0.0877 | 非常低 |
| **actor/grad_norm** | 2.496 | 正常范围 |
| **critic/score/mean** | -4.68 | 大部分 episode 负分 |

### 时间分析（Step 0）

| 阶段 | 耗时 |
|------|------|
| **Step 0 总耗时** | **5743.5s ≈ 95.7 min** |
| rollout 生成 (gen) | 3642.6s (63.4%) |
| multi-turn collapse | 1984.3s (34.5%) |
| actor update | 53.4s (0.9%) |
| ref forward | 17.7s |
| old_log_prob | 13.7s |

### Step 1 状态
- 已开始，进度条显示 `1/100 [1:35:43<157:56:47]`
- 预估剩余 ~158 小时（按当前速度）
- GPU 利用率当前 0%，内存 48GB/卡 — 可能正在做 rollout 的环境交互阶段

### 诊断

**核心问题：95.3% 无效动作率。** 模型产生的动作绝大多数无法被 ALFWorld 环境解析，导致 reward 几乎为零，pg_loss 极小。训练在"学习"但学不到什么有意义的东西。按 158 小时完成 100 步来看，效率极低。

---
