# temp-adv-distill-vla — Research Dashboard

> 最后更新: 2026-05-15 04:36 UTC | 更新原因: 根据 Reviewer 审查修正：补充 Gate 2 量化标准、kill/pivot 路径、VIP fallback、RINSE 对比

## 核心方向
Temporal Advantage Distillation (TAD)：用 IQL 在冻结 VLA 特征上计算 per-timestep advantage，作为 AWR 权重做 VLA BC fine-tuning，down-weight 演示数据中的噪声 timestep（犹豫、修正、停顿），提升策略鲁棒性。目标投稿 CoRL 2026（abstract DDL 2026-05-25/26，paper DDL 2026-05-28/29）。

## 当前进展
- **阶段**: MVP 验证（设计完成，待 GPU 资源）
- **基础设施**: 未配置（无服务器/GPU/代码路径）— 阻塞中
- **实验**: 无
- **Reviewer 评审**: borderline (clarity 4, feasibility 4, impact 3, novelty 3)
  - 核心担忧：AWR+IQL 是成熟技术组合，需证明优于 RINSE 等简单运动学方法

## MVP 验证方案
**核心假设**: 冻结 VLA 特征上的 IQL advantage 能有效区分高/低质量 demonstration timestep，且优于简单运动学指标；AWR 加权后的 fine-tuning 优于 vanilla BC。

**Gate 定义与 Kill/Pivot 路径**:

| Gate | 通过标准 | 失败处置 |
|------|----------|----------|
| Gate 1 (特征验证) | 三级 fallback 任一通过即可：(a) raw cos_sim Spearman ρ > 0.8 (>80% 轨迹)；(b) trained progress predictor R² > 0.8；(c) VIP features cos_sim ρ > 0.8 | 三级全失败 → **项目 kill**（特征基础不存在） |
| Gate 2 (Advantage 分离) | IQL advantage IQR > 0.1（归一化）**且** no-op 组 vs progress 组 Mann-Whitney U p < 0.05 + Cohen's d > 0.5 **且** IQL advantage AUROC > RINSE SAL/TED AUROC（区分 no-op/progress） | IQR 不足 → **pivot** 到 trajectory-level advantage ranking；AUROC 不优于 RINSE → 评估是否仍有 complementary value，否则 **项目 kill** |
| Gate 3 (性能提升) | AWR fine-tuning success rate > vanilla BC ≥ 3%（至少 1 个 LIBERO suite） | 先排查实现 bug（1 轮）；排除 bug 后仍失败 → **项目 kill**（核心 hypothesis 不成立） |

**MVP 实验步骤（最小化）**:
1. 环境搭建：OpenVLA-OFT checkpoint + LIBERO 数据集 + 依赖
2. Phase 0: 提取冻结特征（多层）→ 验证 progress structure（三级 fallback）→ 选定 reward signal（Gate 1）
3. Phase 1: IQL 训练（τ=0.8）→ advantage 分布分析 + 与 RINSE SAL/TED 对比 AUROC（Gate 2）
4. Phase 2: AWR LoRA fine-tuning vs BC baseline（LIBERO-Object）→ 比较 success rate（Gate 3）

**预计资源**: ~20 H100-h，2-3 天

## 近期任务
- [ ] 用户确认 GPU 服务器并配置项目（**阻塞项**）
- [ ] Agent 搭建环境（OpenVLA-OFT + LIBERO + 依赖）
- [ ] Phase 0: 特征提取与验证（Gate 1）
- [ ] Phase 1: IQL 训练 + advantage vs RINSE AUROC 对比（Gate 2）
- [ ] Phase 2: AWR vs BC 对比实验（Gate 3）

## GPU 预算
- 本项目分配: 待配置
- MVP 预算: ~20 H100-h
- 全量实验预算: ~195 H100-h（含 ablation + baselines + evaluation）

## Reviewer 担忧追踪
| 担忧 | 应对 | 状态 |
|------|------|------|
| AWR+IQL 创新性不足 | Gate 2 直接对比 IQL advantage vs RINSE SAL/TED 的 AUROC | 待验证 |
| RINSE 用简单指标已达 16-20% | 需证明 IQL 在 same-progress-but-different-quality states 上区分力更强 | 待验证 |

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D008 | 2026-05-15 | 项目 Kill：Gate 2 四条路径全部失败，核心假设不成立（t/T reward 不含 time | phase1_iql_vip_scaled, phase1_delta_progress, phase1_iql_vip, phase0_feature_val |
| D007 | 2026-05-15 | Δprogress 失败（AUROC 0.53），确认 reward signal（t/T）不含 n | phase1_delta_progress, phase1_iql_vip, phase1_iql_vip_scaled |
| D006 | 2026-05-15 | Gate 2 评估协议有循环缺陷，修订 pass 标准：drop AUROC vs SAL/TED， | phase1_iql_vip |
| D005 | 2026-05-15 | 修正 D004：批准 Option A（Δprogress AUROC）+ reward scali | phase1_iql_vip |
| D004 | 2026-05-15 | Gate 2 失败（IQL AUROC≈0.5 vs TED 0.62）；批准 1 轮 reward | phase1_iql_vip |
| D003 | 2026-05-15 | Gate 1 通过 (MLP on VIP, R²=0.985)；采用策略 A：VIP 先跑通 MV | phase0_feature_val |
| D002 | 2026-05-15 | Gate 1 策略调整：先跑 VIP fallback(c)，同时后台修复 OpenVLA 下载 | phase0_feature_val |
| D001 | 2026-05-15 | MVP 方案：3-gate 验证（特征单调性 → advantage 分离度 → AWR vs BC | — |

