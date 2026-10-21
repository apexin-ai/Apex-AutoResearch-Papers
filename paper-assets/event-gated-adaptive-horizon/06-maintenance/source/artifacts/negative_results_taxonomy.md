# Negative Results 分类清单

总计：**35** 个 negative 实验

## 分类总览

| 类别 | 数量 | 占比 | 代表实验 |
|------|------|------|----------|
| TCN 跨环境/剂量失败 | 10 | 28.6% | exp_030a (Cheetah σ=0.2), exp_031 (PickCube σ=0.2) |
| SGS 干预失败 | 5 | 14.3% | exp_016e (reward-head SGS), exp_018_s2 (full-SGS seed 2) |
| Dual-critic / Wide-critic 跨环境失败 | 5 | 14.3% | exp_034 (Cheetah dual-critic), exp_038 (Walker s2 non-CIVO collapse) |
| dt>1 本身退化 | 5 | 14.3% | exp_007 (fixed dt=4), exp_008f_s4 (no-dt-emb control) |
| CIVO 复现/表征（诊断性 negative） | 4 | 11.4% | exp_009e (CIVO collapse confirmed), exp_008e_v3_s3 (stochastic collapse) |
| Event-gate 机制失败 | 3 | 8.6% | exp_005 (v4 collapse @85K) |
| RAVE 干预失败 | 2 | 5.7% | exp_028 (ceiling=2.0), exp_028_ceil15 (ceiling=1.5) |
| Frozen dt_emb 失败 | 1 | 2.9% | exp_015b (gradient starvation) |

---

## 详细分组

### 类别 1：TCN 跨环境/剂量失败（10 个）

TCN (Temporal Conditioning Noise) 在 Walker σ=0.2 上成功，但在其他环境或剂量下普遍失败。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_027_tcn_walker_s0 | TCN σ=0.5 抑制 CIVO | Walker | eval peak 240@35K, oscillatory; eval_105K=95.5 | σ=0.5 过量：NVE 一度自修正但后续震荡性 CIVO，eval 大幅波动 |
| exp_027_tcn_walker_s1 | TCN σ=0.5 seed 1 复现 | Walker | eval peak 364.9@75K, last10 mean 233.1 | σ=0.5 跨 seed 不稳定，eval 振幅大（94.6–364.9），不可靠 |
| exp_029b_tcn_walker_s2_sigma02 | TCN σ=0.2 seed 2 方差表征 | Walker | eval peak 177.67@55K, CIVO onset @65K | s0=91% s1=45% s2=collapsed。σ=0.2 在 Walker 上高方差，2/4 seeds 仍崩溃 |
| exp_029c_tcn_walker_s0_sigma01 | σ=0.1 最低有效剂量测试 | Walker | eval peak 490.7@165K, final 328.3 | σ=0.1 未阻止 CIVO（NVE 曾 breach），但最终 eval 尚可；剂量不足以可靠抑制 |
| exp_029d_tcn_walker_s3_sigma02 | TCN σ=0.2 seed 3 统计补充 | Walker | eval peak 349.6@95K, CIVO onset @105K sudden blowup | 健康→突然崩溃（NVE 0.67@95K→3.0@105K），TCN σ=0.2 无法防止晚期 CIVO |
| exp_030a_tcn_cheetah_s0_sigma02 | TCN σ=0.2 跨环境验证 (Cheetah) | Cheetah | eval 299.5@35K→31.9@55K, NVE 1.903@55K | **σ=0.2 对 Cheetah 完全无效**，NVE 直接 breach 1.5×，eval 崩溃 |
| exp_030b_tcn_cheetah_s0_sigma05 | σ=0.5 Cheetah 环境适配剂量 | Cheetah | eval peak ~211.7@125K, NVE peak 10.67@55K | σ=0.5 未抑制 CIVO（NVE 10.67×），eval 长期低迷（68–211，baseline ~548） |
| exp_030c_tcn_cheetah_s0_sigma10 | σ=1.0 Cheetah 高剂量 | Cheetah | eval peak 371.7@35K, final 47.2 | σ=1.0 仍未抑制 Cheetah CIVO，eval 最终崩至 47.2（baseline ~548） |
| exp_031_tcn_pickcube_s0_sigma02 | TCN σ=0.2 跨域验证 (PickCube) | PickCube | eval peak 28.6@162K, NVE peak 3.71 | **PickCube 上 TCN 完全失败**，NVE 3.71×，gate entropy=0（gate 锁死） |
| exp_031b_tcn_pickcube_s0_sigma05 | σ=0.5 PickCube 剂量提升 | PickCube | eval peak 29.1, NVE peak 3.3@42K | σ=0.5 同样失败，NVE 仍达 3.3×，仅在 72.5K 后才被抑制 |

**模式**：TCN 仅在 Walker σ=0.2 的部分 seeds 上有效（~50% success rate）。Cheetah（所有 σ 失败）和 PickCube（σ=0.2/0.5 失败）跨环境泛化彻底失败。表征级干预不足以应对高强度 CIVO。

---

### 类别 2：SGS 干预失败（5 个）

Selective Gradient Stopping（梯度阻断）干预的全面否定——从 reward-head SGS 到 full-SGS 到 obs-decoder SGS，均无法可靠抑制 CIVO。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_016e_sgs_walker_s1 | Reward-head SGS 阻断 CIVO 梯度通路 | Walker | NVE peak 10.42@95K, eval 31.7@95K | **关键发现**：reward loss 对 dt_emb.weight 梯度贡献=0，reward-head SGS 是 no-op。真正梯度来源是 decoder heads |
| exp_018v2_full_sgs_walker_s1 | Full-SGS 阻断所有 decoder→dt_emb 梯度 | Walker | eval peak 499.6@75K, NVE mean 1.23 (45K-105K), late collapse @112K | CIVO 减少 79% 但未消除；**晚期崩溃** @112K，eval 448→下降 |
| exp_018_full_sgs_s2 | Full-SGS seed 2 可靠性验证 | Walker | eval peak ~488@75K, final 40.8@105K, NVE 1.66@95K | **Seed 2 崩溃**，直接否定 018v2 的结论。Full-SGS 不可靠 |
| exp_021_full_sgs_cheetah_s1 | Full-SGS 跨环境验证 (Cheetah) | Cheetah | NVE peak 9.94@45K, eval final 221.5 (baseline 38.7%) | CIVO 类型=transient_self_correcting，NVE 仍达 9.94×。比 baseline 好 4.3× 但远未达标 |
| exp_025_obs_sgs_walker_s2 | Obs-decoder-only SGS | Walker | VE ratio 0.8-1.4, eval 66-90 (baseline ~930) | CIVO 部分抑制但 **eval 仅 baseline 7-10%**。obs-decoder SGS 摧毁性能同时未消除 CIVO |

**模式**：梯度干预路线全面否定。Full-SGS 0/3 seeds 可靠，Obs-decoder SGS 0/6 有效。关键洞察：CIVO 的梯度来源不是 reward head 而是 decoder heads（016e 发现），但即使阻断全部 decoder 梯度也只是延迟而非消除 CIVO。

---

### 类别 3：Dual-critic / Wide-critic 跨环境失败（5 个）

架构级干预（双 critic / 宽 critic）在部分环境有效但跨环境泛化存在问题。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_034 | Dual-critic 抑制 Cheetah CIVO | Cheetah | eval peak 315.7, final 97.5, NVE peak 1.753 | CIVO 未被阻止（两次 CIVO trigger @55K/105K），v1/v2 divergence 仅 0.004（双 critic 几乎无差异） |
| exp_034_dual_critic_cheetah | Dual-critic Cheetah（TCN 全失败后的架构级干预） | Cheetah | eval peak 315.7@45K, final 97.5, dual-wave CIVO | **双波 CIVO**：CIVO 被短暂抑制后二次爆发。Cheetah 上架构级干预也失败 |
| exp_036_dual_critic_pickcube | Dual-critic PickCube | PickCube | eval peak 27.7, final 27.7, NVE peak 2.3 | CIVO 被标记 prevented（NVE 终值 0.2）但 eval 极低（27.7），gate 锁死 dt=2。功能性失败 |
| exp_037_wide_critic_cheetah | Wide single critic (容量假说) Cheetah | Cheetah | eval peak 350.1, final 146.1, NVE peak 3.6 | NVE 仍达 3.6×（baseline 70.64×减至 3.6× 但远未消除），eval 崩至 146.1 |
| exp_038_dual_critic_walker_s2 | Dual-critic Walker seed 2 统计补充 | Walker | eval peak 354@155K, **collapse to 99.6@175K**, NVE≤0.3 | **Non-CIVO collapse**：CIVO 被阻止（NVE≤0.3）但 eval 仍崩溃至 99.6，暴露非 CIVO 退化机制 |

**模式**：Dual-critic 在 Walker 2/3 seeds 有效但第三 seed 暴露 non-CIVO collapse。Cheetah 上完全失败（双 critic 几乎无差异化）。PickCube 上 CIVO 指标好但功能性 eval 极差。架构级干预也非万能。

---

### 类别 4：dt>1 本身退化（5 个）

temporal subsampling 自身导致的性能退化，与 CIVO 无关——即使没有 CIVO 现象，dt>1 也带来显著性能损失。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_006_fixed_dt2 | Fixed dt=2 诊断（无 learned gate） | Walker | eval peak 485.3@35K, 65K 崩至 132.86 | dt=2 本身导致崩溃，非 gate 机制问题。VE ratio @65K=3.67 |
| exp_007_fixed_dt4 | Fixed dt=4 诊断 | Walker | eval peak 176.9@25K, 45K=144 (baseline 443) | dt=4 性能显著低于 baseline，进程 12.5min 后异常退出 |
| exp_008c_no_subsample_dt2_h8 | Subsample OFF + dt=2 imagination + H=8 | Walker | eval plateau ~241@55K-65K (baseline 616@65K) | 无 subsample 下 dt=2 imagination 也只达 baseline 39%，compounding error 是瓶颈 |
| exp_008f_s4 | No-dt-emb 控制组 seed 4 | Walker | eval 306.5@105K, peak 487.5@55K (baseline ~930) | 无 CIVO（NVE 0.58）但 eval 仅 baseline 33%。移除 dt_emb 避免 CIVO 但代价是巨大性能损失 |
| exp_009c_008f_walker_s2 | No-dt-emb 控制组 seed 2 | Walker | eval 148.34@105K, peak 359@75K | 比 seed 1（503@105K）更差，**无 dt_emb 方案 seed 方差极大且性能不可接受** |

**模式**：dt>1 即使在最优配置下（fixed dt、no gate、no dt_emb）也带来 40-70% 的性能损失。这是 temporal subsampling 的根本局限——RSSM 对 dt>1 的多步预测质量不足，compounding error 随 horizon 累积。

---

### 类别 5：CIVO 复现/表征（诊断性 negative）（4 个）

这些实验的 negative 结论是因为它们确认了 CIVO 现象的存在和严重性，是诊断性实验而非干预实验。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_009e_008d_walker_s1 | 008d CIVO 复现（seed 1 延长至 105K） | Walker | NVE 4.13@55K, eval 131.08@105K | CIVO collapse 确认：eval 从正常水平崩至 131，actor_loss 翻正@85K |
| exp_009b_008d_walker_s2 | 008d CIVO 复现（seed 2） | Walker | NVE peak 1.62@45K (transient), eval 268 | CIVO 未复现（self-corrected），但 eval 仍远低于 baseline。NVE>1.5× threshold 可靠但 collapse 是随机的 |
| exp_008e_v3_s3 | dt=1/H=15 多 seed 验证 | Walker | NVE 4.02@105K, eval 92.7, collapse @85K-95K | dt=1 配置仍出现 CIVO collapse（1/3 seeds），证明 CIVO 是随机性的 |
| exp_008e_v3_walker_s2 | dt=1/H=15 seed 2 crown jewel 验证 | Walker | eval peak 715@85K→137@105K, NVE 3.78× | C6 配置 collapse：即使 gate 锁定 dt=1，1/3 seeds 仍崩溃。Collapse 是随机的 |

**模式**：CIVO 是随机性事件（30-50% 发生率），即使在最保守配置（dt=1）下仍可发生。NVE>1.5× 是可靠的早期预警指标，但 collapse 发生与否有随机性。

---

### 类别 6：Event-gate 机制失败（3 个）

项目最初提出的 event-gated adaptive horizon 核心机制的早期失败。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_003_event_gated_v2 | Event-gated v2 | Walker | eval 92.3-118.7@105K-115K, gate entropy ratio 0.796 | C1 return FAIL (baseline 0.13×)，gate 分布有多样性但 return 极低 |
| exp_004_event_gated_v3 | 修复 imagination dt 约束后的 v3 | Walker | — | 修复 logits masking 后仍失败 |
| exp_005_event_gated_v4 | Learned gate 改善 sample efficiency | Walker | eval peak 541.18@55K→98.84@145K (baseline ~950) | 早期有希望（55K 达 541）但后期崩溃至 98.84。Gate mean 收敛到 ~2.0，学习不稳定 |

**模式**：Learned gate 机制从 v2 到 v4 持续失败。核心问题：gate 的 dt>1 选择引入 CIVO 现象，而 gate 本身无法学会规避这一问题。这一失败直接催生了 CIVO 研究方向的转向。

---

### 类别 7：RAVE 干预失败（2 个）

Reality-Anchored Value Estimation（直接 clip value ratio）的失败。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_028_rave_walker_s0 | RAVE ceiling=2.0 cap imagination value | Walker | eval peak 204.6, 105K=29, VE ratio 3.183@105K | **RAVE 完全失败**：ceiling=2.0 未阻止 VE ratio 上升至 3.183，eval 崩至 29 |
| exp_028_rave_walker_s0_ceil15 | RAVE ceiling=1.5 更激进 cap | Walker | eval peak 180.1@35K, 135K=39.1 | Tighter ceiling 同样失败，eval 持续下降至 39.1。Value capping 无法解决根因 |

**模式**：直接 clip value ratio 不仅未能抑制 CIVO，反而可能干扰正常的 value 学习。CIVO 的根因不在 value 数值大小，而在 value 的结构性偏差。

---

### 类别 8：Frozen dt_emb 失败（1 个）

冻结 dt_emb 权重的因果诊断实验。

| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
|--------|-----------|------|----------|----------|
| exp_015b_frozen_dt_emb | Frozen dt_emb 隔离训练 vs 存在的因果效应 | Walker | eval 204.2@105K, peak 211.2@65K (baseline ~930) | **Gradient starvation**：冻结 dt_emb 导致 actor_loss 接近 0（0.000179@105K），entropy 异常低（-4.855）。证明 dt_emb 训练对正常学习是必要的 |

**模式**：不能通过冻结 dt_emb 来避免 CIVO——dt_emb 的梯度流对整体学习至关重要，阻断它会导致 gradient starvation。

---

## 跨类别观察

### 1. 干预层级递进失败链
项目经历了清晰的干预层级递进：**梯度级（SGS）→ 表征级（TCN）→ 值函数级（RAVE）→ 架构级（dual-critic）**。每一级都因不同原因失败，揭示 CIVO 是一个多层面问题：
- 梯度阻断（SGS）：延迟但不消除 CIVO
- 噪声注入（TCN）：环境敏感、剂量窗口极窄
- 值裁剪（RAVE）：未触及根因
- 架构冗余（dual-critic）：Cheetah 上双 critic 无差异化，Walker 上暴露 non-CIVO collapse

### 2. 环境依赖性是系统性障碍
几乎所有干预方法都表现出强烈的环境依赖性。在 Walker 上部分有效的方法迁移到 Cheetah（更强 CIVO）或 PickCube（不同动力学）后失败。这表明 CIVO 的严重程度和机制可能因环境而异。

### 3. CIVO 的随机性本质
即使在相同配置下，CIVO collapse 也只在 30-50% 的 seeds 上发生（exp_008e_v3 系列：3 seeds 中 1 个 collapse；exp_029 系列：4 seeds 中 2 个 collapse）。这意味着单 seed 实验无法可靠判断干预是否有效。

### 4. 非 CIVO 退化机制
exp_038 揭示了一个重要盲点：成功抑制 CIVO（NVE≤0.3）后仍可能出现 eval collapse。这说明 dt>1 imagination 还存在 CIVO 以外的退化机制，可能与 compounding error 或 policy exploration 相关。

### 5. dt>1 的根本性限制
5 个 dt>1 退化实验（类别 4）表明，即使完全解决 CIVO，temporal subsampling 本身也带来 40-70% 的性能损失。这对项目的实用价值构成了根本性挑战——CIVO 只是 dt>1 问题的一个维度。
