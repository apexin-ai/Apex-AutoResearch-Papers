# 25 个阴性实验 Failure Pattern 分析

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

