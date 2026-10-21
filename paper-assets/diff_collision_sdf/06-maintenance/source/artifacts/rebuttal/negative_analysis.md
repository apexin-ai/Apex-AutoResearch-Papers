# Rebuttal 准备——25 个阴性实验 Failure Pattern 分析

## 分类统计

### A. 支持论文 Claims 的预期阴性（20/25，80%）

**A1. SDF 训练信号从未出现（7 个，支撑 Claim 3）**
stepwise 系列 (16K/20K/22K/24K/28K, 2 seeds) + Phase 2 λ=0：CAR 始终在 52-56.5% null 区间内。跨 6 个 checkpoint、2 seeds、20× λ 范围，SDF 信号从未 emerge。系统性 null，不是超参未调优。

**A2. Oracle 反效果（3 个，支撑 Claim 2）**
adaptive/fixed/feature-space 三种 oracle 策略：CAR 分别 75%/73.1%/76.9%，均低于 baseline 79-82%。机制一致：EE 推离 → 臂杆旋入障碍。

**A3. Action Collapse / Fake Safety（5 个，支撑 Claim 1）**
A1 SDF (91.5% CAR, 99.6% fake)、baselines (82-83% CAR, TSR≈0%)、A3 SDF (74.5% CAR, refined=0)。

**A4. Spatial 场景全面失败（5 个，支撑 full-body SDF 必要性）**
LoRA/Full-FT/A1/SDF 在 spatial 场景 CAR≈0%。碰撞源是 arm-body 而非 EE-obstacle。

### B. Bug 污染的历史实验（3/25，12%）
oracle_a3_m024fix、oracle_a3_force_refine、eval_a3_object_m024fix：受 M027 oracle 死代码影响。已在论文中排除。

### C. 基座模型基线探测（2/25，8%）
Pi0.5 base eval (CAR=28%, 98.2% fake) 和 spatial eval (CAR=13%)。

## Reviewer 最可能质疑 + 回应

**Q1: "25 个 negative——没 try hard enough？超参不优？"**
反驳：SDF 覆盖 λ ∈ {0.005, 0.01, 0.1}（20× 范围），oracle 覆盖 3 种策略 + GT SDF，跨 2 model families，7 个 checkpoints。如果超参是问题，至少某个组合应该 work。

**Q2: "Oracle 用了 action-collapsed baseline 不公平"**
反驳：Pi0.5 LoRA 非 collapsed 验证（CAR 51.9% vs 56.5%, -4.6pp），per-task pattern 一致。

**Q3: "为什么不做 full-body SDF？"**
反驳：贡献是诊断性的——先确认 WHY EE-only 失败，再指向 full-body 作为必要路径。

## Rebuttal 框架

**框架 1: 阴性结果本身就是贡献**
25 个阴性不是"方法不 work"，而是证明当前评估体系存在结构性缺陷。三个发现跨 100+ 实验、6000+ episodes、两个 VLA 家族稳健成立。

**框架 2: 统计诚实性**
MDE ≈ 5.6pp at 80% power，2-5pp 效应无法解析。即使存在 2-3pp 效应，其安全价值也可疑——EE-only 结构上无法防止 arm-link 碰撞。

**框架 3: 预期 vs 意外**
唯一"意外"是 A3 learned SDF refined_count=0——但恰好揭示 collision-free demonstrations 中 EE 本来就远离障碍物，SDF 值自然为正。不是 bug 而是 demonstration data subsumes SDF signal 的直接后果。
