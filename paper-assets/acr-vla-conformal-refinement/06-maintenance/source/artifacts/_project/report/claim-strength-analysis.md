# Claim Strength Analysis — 2026-05-13 21:00 UTC

## 1. 完整数据表

### 1A. MVP — Point-Reaching Motivating Experiment (DONE ✅)

| Condition | Aniso | Unc Source | Per-DOF (B) MSE | Scalar (A) MSE | None (C) MSE | B vs A Δ | B vs C Δ |
|-----------|-------|-----------|-----------------|----------------|--------------|----------|----------|
| Group 1   | 5:1   | Oracle    | 0.0679          | 0.0765         | 0.0925       | −11.2%   | −26.5%   |
| Group 2   | 2:1   | Oracle    | 0.0283          | 0.0371         | 0.0448       | −23.9%   | −36.9%   |
| Group 3   | 1.5:1 | Oracle    | 0.0214          | 0.0295         | 0.0344       | −27.4%   | −37.8%   |
| Group 4   | 5:1   | K=10 Est  | 0.0735          | 0.0788         | 0.0882       | −6.7%    | −16.7%   |
| Group 5   | 2:1   | K=10 Est  | 0.0320          | 0.0375         | 0.0422       | −14.7%   | −24.2%   |
| Group 6   | 1.5:1 | K=10 Est  | 0.0245          | 0.0295         | 0.0326       | −16.9%   | −24.8%   |

**Key takeaways:**
- Per-DOF 在所有 6 个条件下一致优于 scalar 和 none
- Oracle→K=10 估计衰减约 5-15pp（Group 1→4: 11.2%→6.7%），但 B>A>C 排序不变
- 弱各向异性 (1.5:1) 下 per-DOF 优势反而更大（27.4% oracle, 16.9% K=10）
- **结论: MVP PASS — 核心假设初步验证**

### 1B. eval-spatial-v5-full — SmolVLA Baseline (RUNNING 🔄, 2/10 tasks)

| Task | Success Rate | n |
|------|-------------|---|
| pick_up_bowl_between_plate_and_ramekin → plate | **90%** | 9/10 |
| pick_up_bowl_next_to_ramekin → plate | **80%** | 8/10 |
| pick_up_bowl_from_table_center → plate | ⏳ 0/5 (进行中) | — |
| Tasks 4-10 | ⏳ 未开始 | — |

- **部分均值 (2 tasks): 85%** — 但仅 2/10 tasks，Task 3 目前 0/5
- SmolVLA 论文报告 libero_spatial 78-85%（20 rollouts）
- 如果 Task 3+ 拉低均值，最终可能在 50-80% 区间

### 1C. eval-reconvla-spatial-v2 — ReconVLA Baseline (RUNNING 🔄, 2/10 tasks)

| Task | Success Rate | n |
|------|-------------|---|
| pick_up_bowl_between_plate_and_ramekin → plate | **90%** | 9/10 |
| pick_up_bowl_next_to_ramekin → plate | **90%** | 9/10 |
| Tasks 3-10 | ⏳ 未开始 | — |

- **部分均值 (2 tasks): 90%** — ReconVLA 在前两个 task 比 vla_only 高 5pp
- 注意：这是 standard LIBERO（无 perturbation），ReconVLA 在无偏移下选 K 个中最好的，可能略高于 mean
- **关键缺失：无 perturbed 环境对比 — 这才是 ACR-VLA 的 value proposition**

### 1D. eval-object-v4-full — SmolVLA on Object Suite (RUNNING 🔄, Task 1 进行中)

| Task | Success Rate | n |
|------|-------------|---|
| pick_up_alphabet_soup → basket | ⏳ 0/5 (进行中) | — |
| Tasks 2-10 | ⏳ 未开始 | — |

- 第一个 task 5 rollouts 全失败，信号不乐观
- Object suite 通常比 spatial 更难

### 1E. CRM Training (RUNNING 🔄, epoch 32/50)

| Metric | Value |
|--------|-------|
| Architecture | MLP 1030D→256→256→30D (337K params) |
| Training data | 26,737 samples (spatial 12,167 + object 14,570) |
| Best val_loss | **0.009412** (epoch 31) |
| Current train_loss | ~0.016 |
| Convergence | 稳定下降中，val/train gap 健康 |

- 训练正常收敛，无 overfitting 迹象
- **但还没有 eval（success rate on actual tasks）— CRM 训练完还需 ACR-VLA eval**

### 1F. Precompute-k5 (RUNNING 🔄)

- K=5 sensitivity ablation 数据预计算中
- 完成后需 crm-train-k5 + eval

### 1G. 已失败/作废实验

| Experiment | 原因 |
|-----------|------|
| eval-spatial-v3-full | buggy wrapper（D014 前），结果无效 |
| eval-spatial-v4-full | camera_names 缺失，v5 已修复 |
| plan_014-reconvla-baseline | 用了未微调的 smolvla_base，0% success |
| precompute-v1/v2/v3 | buggy wrapper / 旧代码，全部重做为 v4 |

---

## 2. Core Claims 支撑强度评估

### Claim 1: Per-DOF conformal features enable dimension-selective correction
> CGS 40D > scalar Euclidean distance > no uncertainty conditioning

| Evidence | Status | Strength |
|----------|--------|----------|
| MVP 6 conditions: B>A>C 一致 | ✅ Done | **Strong** (synthetic) |
| A3 ablation: CRM w/o conformal vs full | ❌ Not started | — |
| A4 ablation: scalar vs per-DOF on LIBERO | ❌ Not started | — |
| Feature importance analysis | ❌ Not started | — |
| CRM training converging | 🔄 Running | Weak (indirect) |

**当前支撑: Moderate ⚠️**
- MVP 在合成数据上 strong evidence，但 **synthetic→LIBERO 泛化未验证**
- A3 ablation 是 make-or-break：如果 CRM without conformal features 仅差 <2%，claim 不成立
- CRM 训练收敛只说明网络能学，不说明 conformal features 是关键
- **升级条件**: A3 gap >5% + A4 per-DOF>scalar on LIBERO → 可升级为 "显著优于"
- **降级风险**: Dream median 预警 per-DOF vs scalar 仅 +2.1%。如果实验确认，需 reframe 为 "structured uncertainty features" 整体优势

### Claim 2: ACI+COC maintains calibrated uncertainty under distribution shift
> Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新

| Evidence | Status | Strength |
|----------|--------|----------|
| COC-success Spearman ρ | ❌ Not started | — |
| ACI convergence | ❌ Not started | — |
| Ellipsoid volume vs static | ❌ Not started | — |
| Perturbed environment eval | ❌ Not started | — |

**当前支撑: No Evidence ❌**
- 零实验数据。ACI 和 COC 代码可能还未实现或未在 LIBERO 上测试
- 这是论文第二核心 claim，**完全空白是最大风险**
- Kill criterion (ρ < 0.3 AND no volume shrinkage) 无法评估

### Claim 3: ACR-VLA is orthogonal to training-time methods (SRPO stacking)
> ACR-VLA + SRPO > SRPO alone

| Evidence | Status | Strength |
|----------|--------|----------|
| ACR-VLA + SRPO eval | ❌ Not started | — |
| SRPO baseline | ❌ Not started (需要 SRPO checkpoint) | — |

**当前支撑: No Evidence ❌**
- SRPO 82.1% 是文献数字，未在本项目中复现
- 需要获取 SRPO checkpoint 或使用其公开结果
- 如果 ACR-VLA 本身 success rate 不高，stacking claim 无基础

---

## 3. 支撑矩阵总结

| Claim | 当前强度 | 关键缺失 | Make-or-Break |
|-------|---------|---------|---------------|
| **C1: Per-DOF > scalar** | **Moderate** (MVP only) | A3/A4 ablation on LIBERO | A3 gap <2% → kill |
| **C2: ACI+COC calibration** | **No Evidence** | 全部验证实验 | ρ < 0.3 → kill |
| **C3: SRPO stacking** | **No Evidence** | SRPO checkpoint + stacking eval | gain <2% → downgrade |

---

## 4. 实验计划空白 + 优先级排序

### 已在跑（等结果）
1. **eval-spatial-v5-full** — SFT gate 判定（~1h）
2. **eval-object-v4-full** — object baseline（~2h）
3. **crm-train-v1** — CRM 训练完成（~1h）
4. **eval-reconvla-spatial-v2** — ReconVLA baseline（~2h）
5. **precompute-k5** — K=5 ablation 数据（~1h）

### 待启动 — 按优先级排序

| 优先级 | 实验 | 目的 | 支撑 Claim | 预计 GPU-hours | 前置条件 |
|--------|------|------|-----------|---------------|---------|
| **P0** | **ACR-VLA eval (per-DOF mode)** | 首个完整 ACR-VLA 结果 | C1 | 2-4h | crm-train-v1 done |
| **P0** | **A3 ablation: CRM obs_only** | C1 make-or-break | C1 | 4-6h (train+eval) | precompute-v4 done |
| **P0** | **A4 ablation: CRM scalar_unc** | per-DOF vs scalar on LIBERO | C1 | 4-6h | precompute-v4 done |
| **P1** | **Perturbed env eval** | perturbation 下 ACR-VLA 提升 | C1+C2 | 4-8h | ACR-VLA eval baseline |
| **P1** | **COC metric + ACI online** | C2 核心验证 | C2 | 2-4h | perturbed eval infra |
| **P1** | **K sensitivity sweep (K=5,10,15,20)** | reviewer concern #1 | C1 | 8-10h | precompute-k5 done |
| **P1** | **Held-out perturbation test** | conformal vs memorization | C1 | 4-6h | perturbed eval infra |
| **P2** | **Multi-seed replication (3 seeds)** | 统计可靠性 | All | 20-30h | P0 all pass |
| **P2** | **SRPO stacking** | C3 验证 | C3 | 10-15h | SRPO checkpoint |
| **P2** | **Feature importance analysis** | per-DOF contribution | C1 | 1-2h | CRM trained |

### 关键路径
```
crm-train-v1 (eta ~1h) → ACR-VLA eval (2-4h) → A3/A4 ablation (4-6h each, 可并行)
                                                ↘ Perturbed eval (4-8h) → COC/ACI (C2)
```

---

## 5. 诚实评估 & 建议

### 当前状态
- **Phase 1 尚未完成**：连 SmolVLA baseline 和 ACR-VLA 第一个完整结果都没有
- 3 个 Core Claims 中 **1 个有部分支撑（合成数据），2 个零证据**
- CRM 训练收敛是好信号，但不等于 task success 提升

### 最关键的下一步
1. **等 crm-train-v1 完成 → 立即启动 ACR-VLA eval on spatial** — 这是 C1 从 synthetic→real 的首个数据点
2. **等 eval-spatial-v5-full 完成 → SFT gate** — 如果 base VLA <50%，所有后续实验意义存疑
3. **A3 ablation (obs_only CRM)** — 尽快排期，这是 C1 的 kill criterion

### 论文 timeline 风险
- ICLR 2027 DDL Sep-Oct 2026，还有 ~4-5 个月
- 当前进度：仅 MVP + 基础设施搭建。核心 LIBERO 实验 0 个完成
- P0 实验（ACR-VLA eval + A3 + A4）最乐观需 2-3 天
- C2 (ACI+COC) 实验基础设施可能还需搭建
- 需要至少 2-3 周高密度实验才能有足够论文数据
