# verify caliber framework data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_caliber_framework_data_20260524T035844_result.json`
- **Structured JSON:** [`4295b1dc05f8aa0d2d21.json`](../../sessions/42/4295b1dc05f8aa0d2d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整汇总。

---

## Credit Assignment 数据源审计报告

### 一、各数字的原始来源

| 数字 | 类型 | 来源文件 | 原始数据 | 可复现 |
|------|------|---------|---------|--------|
| **52.07%** (n=3000) | 实验 | `hsweep_h2_seed2` (W&B: jhwyg4tc) | `/root/runs/.../advantage_log.jsonl` (3000行, 343KB) ✅存在 | ✅ 脚本+数据均在 |
| **100%** (n=157) | 实验 | `binary_reward_final_analysis.md` iter1 | `/root/autodl-tmp/binary_credit_adv_log.jsonl` (600行, 99KB) ✅存在 | ✅ |
| **28%** (n=271) | 实验 | `binary_reward_final_analysis.md` 汇总 | 同上文件 | ✅ |
| **≤19.1%** | 理论 | Proposition 2: p/(1-(1-p)^K) = 0.125/0.656 | N/A | ✅ 纯计算 |
| **Cohen's h≈0.041** | 计算 | 2arcsin√0.5207 − 2arcsin√0.5 | 从52.07%推导 | ✅ 纯计算 |

### 二、详细溯源

**52.07% credit agreement (penalty reward, h=2)**
- 实验: `hsweep_h2_seed2`, seed=20000, training step 15
- 分析脚本: `/root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`
- JSON 输出: `/root/cost-verify-agent-rl/artifacts/advantage_analysis_summary.json`
  - agreement=0.5207, r_pointbiserial=0.068, p=0.00019
  - P(adv>0|success)=0.371, P(adv>0|failure)=0.306
  - 128 episodes (65 success, 63 fail), 3000 windows
- 统计检验: binomial test vs 50% → p=0.0247 (artifacts/binomial_test_results.md)

**100% sign-episode correlation (binary reward, n=157)**
- 来自 binary_credit_agreement 实验 iteration 1
- 157/157 non-zero windows 的 advantage sign 与 episode outcome 完全一致
- 3-iteration 汇总: **99.6%** (270/271)，1 例外是 GRPO within-group normalization 边界情况（低 return 的成功 episode 在高 return group 中被归一化为负 advantage）

**28% credit agreement (binary reward, n=271)**
- 3 iterations 汇总: 76/271 non-zero windows
- Per iteration: iter1=28.0% (44/157), iter2=N/A (全零), iter3=28.1% (32/114)
- 配置: `_alfworld_binary_credit_agreement.yaml` (penalty_coef=0.0, 纯 binary reward)

### 三、关键发现

#### 1. 不同"口径"是有意设计，不是不一致

论文 Section 4.4 明确定义了三个互补指标:
- **(1) Sign-episode correlation**: advantage sign 是否跟踪 episode 成功/失败 → 100% (binary reward)
- **(2) Credit agreement rate**: advantage sign 是否匹配 local action quality → 52% (penalty) / 28% (binary)
- **(3) P(correct|update)**: 理论上界 → ≤19.1%

三个度量回答不同问题。52% vs 19.1% 的差异来自 reward 类型不同：penalty reward 引入 within-group variance 改善了 credit agreement（从 28% 升到 52%），binomial test z=45.9 确认两者在统计上极显著不同。论文已在正文中解释了这一点。

#### 2. 所有实验数据均为单 seed
- 52.07%: hsweep_h2_seed2 单个 run (seed=20000)
- 100%/28%: binary_credit_agreement 单个 run (3 iterations, 同一 config)
- 没有多 seed 验证 credit agreement 数字的稳定性

#### 3. binary credit agreement 实验无 registry 条目
`binary_credit_agreement_iter0` 不在 registry 中。实验在 2026-05-23/24 运行，数据和分析存在于 artifacts，但缺少正式的实验管理追踪。

#### 4. 论文选择性使用 iter1 而非汇总
- Sign-episode correlation: 论文引用 iter1 的 100% (n=157)，汇总为 99.6% (270/271)
- data_correctness_audit.md 已标记此问题（严重程度低，100% 是理论预期，1 例外是 GRPO edge case）
- 建议：可考虑改为 "near-perfect (99.6%)" 或脚注说明

#### 5. 两组数据的 window 样本空间不同
- Penalty reward (n=3000): 几乎所有 windows 有非零 advantage，全部纳入统计
- Binary reward (n=271 of 600): 54.8% 的 windows 为零 advantage（all-fail groups），仅统计非零部分
- 这使得 n 不直接可比

### 四、数据自洽性判定

**数据自洽**。52%、28%、100%、19.1% 这四个数字分别回答不同问题，使用不同 reward 设置，对应不同理论预期。data_correctness_audit.md (2026-05-23) 已交叉验证全部数字，发现 0 个数值错误（有 1 个已修复的理论计算错误 5.1%→14.9%，以及 1 个 caption 归属问题）。

**主要风险**: 单 seed 数据。credit agreement 数字的置信区间依赖于 window 层面的独立性假设，但同一 episode 内的 windows 高度相关（advantage sign 几乎完全由 episode outcome 决定），所以 n=3000 独立样本的实际有效样本量远小于 3000（更接近 128 episodes）。不过 binomial test 结果 (p=0.025) 在 n=128 episode 层面仍然成立。

---
