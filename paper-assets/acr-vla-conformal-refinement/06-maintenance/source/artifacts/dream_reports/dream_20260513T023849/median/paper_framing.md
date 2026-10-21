# Paper Framing — acr-vla-conformal-refinement

## Target Venue
- Primary: CoRL 2026 (abstract May 26, paper May 29) — 极紧，需 GPU 扩容至 ≥2x H100 才可行
- Backup: ICLR 2027 (expected deadline ~Sep-Oct 2026) — 充足时间
- 决策点: 若 3 天内 GPU 未扩容，放弃 CoRL，瞄 ICLR 2027

## Core Insight
Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode "which action dimensions are uncertain and how they co-vary" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.

## Core Claims (3 条，均可证伪)
1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 45D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。
   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis
   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立

2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。
   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static
   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI

3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。
   - 验证: ACR-VLA + SRPO > SRPO alone
   - Kill criterion: stacking gain < 2% → claim 降级为"complementary in principle"

## Story Spine
- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。
- **Gap**: ReconVLA 用标量 Euclidean distance 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作。CP-in-the-Loop 通过 planning 闭环但非学习型参数化。UPS 用 CP 做策略门控但不将 conformal 特征作为校正网络输入。A2C2/PLD 学习残差但不利用 calibrated uncertainty features。
- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码"哪些维度不确定+跨维度协方差"，使 CRM 能做维度选择性校正。
- **Headline result template**: "On LIBERO-Plus, ACR-VLA improves base VLA success by X%, and when stacked on SRPO (82.1%), achieves Y% — demonstrating that inference-time conformal correction provides orthogonal value beyond training-time optimization."

## Anticipated Reviewer Concerns
1. **K=10 covariance 估计可靠性** (p/n=0.7): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。若审稿人追问，可加 K=20 ablation。
2. **CRM 131K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度。ablation 可测 dim 512 版本。
3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 是透明呈现。
4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。
5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric uncertainty（在分布内也高），CGS 捕获 epistemic uncertainty（分布偏移时升高）。A7 ablation 验证区分。
