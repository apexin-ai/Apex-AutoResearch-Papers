# analysis adv log v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adv-log-v2_20260518T025214_result.json`
- **Structured JSON:** [`ddba964a7509a3447571.json`](../../sessions/dd/ddba964a7509a3447571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本成功运行。核心结果：

### 数据概览
- 3000 条记录，128 episodes（65 成功 / 63 失败），16 个 window positions

### 4 维度分析结果

**1. Advantage Sign vs Episode Outcome**
- Sign-outcome agreement: **52.07%**（仅略高于随机）
- Point-biserial r = **0.068** (p=1.94e-04)，统计显著但效应极弱
- P(adv>0 | success) = 37.06%，P(adv>0 | failure) = 30.60%，差距仅 ~6.5pp

**2. Advantage Sign vs Window Position**
- 早期 steps 正 advantage 比例 ~38%，晚期下降至 0%（但晚期样本极少：pos 13-15 仅 2-6 条）
- Sign-outcome agreement 随 position 增大从 ~50% 升至 ~67%，但样本量不足以下结论
- Sign rate std = 0.1297

**3. Magnitude Decay Fitting**
- Fitted γ = **0.9426**，R² = **0.5627**
- |Adv| 从 pos 0 的 0.016 衰减到后期 ~0.01，存在中等程度的 magnitude decay

**4. Success vs Failure Distribution**
- Success mean = +0.000734，Failure mean = −0.005438
- Distribution overlap = **0.8785**（高重叠 → 两类分布几乎不可分）

### Verdict
**弱 sign misattribution 或无 misattribution**。advantage sign 与 episode outcome 的关联极弱（r=0.068），正负 advantage 的分布高度重叠。

### 生成文件
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis.pdf`
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis.png`
- `/root/cost-verify-agent-rl/artifacts/advantage_analysis_summary.json`

---
