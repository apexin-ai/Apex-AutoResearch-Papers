# ColliForce-VLA Paper Framing

> 维护者: Director | 最后更新: 2026-05-26 UTC | D023 修正：30K collapse 叙事被推翻，SDF 效果跨步数一致 | Post-MVP research phase

## Core Insight

VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 "安全" 指标虚高。我们通过大规模实证分析（70+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明 SDF auxiliary loss 能产生真实碰撞避免——但代价极端。

## Working Title

"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"

> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献

## Target Venue

**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)
**定位**: Diagnostic/evaluation methodology paper with positive method contribution
**Fit**: Robotics safety track — "VLA safety metrics are fundamentally broken" 对社区有直接影响

## Core Claims

### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)
Standard CAR metric is systematically contaminated. On SafeLIBERO, A1 (SDF auxiliary loss on Pi0) achieves 91.5% CAR, but 99.6% of safe episodes show obstacle displacement < 0.1mm — the robot is frozen, not collision-avoiding. "Collision-free" ≠ "collision-avoiding."

**证据**: 800 episodes A1 per-episode analysis (obstacle displacement ~5nm median); TSR=0% 独立确认 action collapse; Pi0.5 baseline 56/56 safe episodes = geometric path safety (非 avoidance 行为)
**贡献**: 提出 EE displacement-filtered CAR (real_CAR) 作为修正指标
**术语修正 (D023)**: 论文中 fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主，明确区分 "obstacle displacement" 和 "EE displacement"

### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)
更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。

**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
**限制**: 仅 2 model families; Pi0 的 "高 CAR" 来自 action collapse; 降级为 observation, 不 claim 因果

### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)
End-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。

**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系
**限制**: "EE-only 不够" 是 expected result; 缺乏 full-body SDF 对照

### Claim 4: SDF Produces Real but Extreme Safety (Method Contribution — 证据强度 ★★★★)
SDF auxiliary training loss on capable VLA (Pi0.5) reliably induces real collision avoidance: CAR improves from baseline 27% to 50-55% (+25pp), with EE displacement ~0.5m confirming genuine avoidance behavior (0% fake safety). Effect is stable across 3 seeds × 2 lambdas × all checkpoints (10K-30K). However, the safety-performance tradeoff is extreme: TSR drops from 73% to 5-9% (-65pp).

**证据 (confirmed, D023)**:
- 3 seeds × 2 lambdas: avg EE disp 0.47-0.51m, 0% fake, CAR 49-55%
- 效果跨 checkpoint 步数一致（10K/16K/30K 无差异）—— 不存在 "sweet spot" 或 "collapse"
- Tradeoff 是 loss 权重问题，非训练动态问题

**Claim 措辞**: "Training-time SDF auxiliary loss reliably produces real collision avoidance (+25pp displacement-filtered CAR, 0% fake_safe) on Pi0.5, but at severe task performance cost (TSR: 73%→5-9%). The tradeoff is stable across training — not a training artifact but a structural property of the current loss weighting."

**禁区**: SOTA / consistently outperforms / general solution / "tradeoff is fundamental" (可能只是 lambda 未优化)

**待确认 (影响 claim 强度)**:
- LoRA baseline CAR → 决定 SDF 归因强度 (ETA ~09:30 UTC May 26)
- Phase 2 λ=0 → 如果 TSR 恢复+CAR 保留 → 升级为 "two-phase training strategy" claim

### LoRA 归因场景（Claim 4 强度取决于此）

| LoRA-only CAR | SDF 增量 | 叙事策略 |
|---------------|----------|----------|
| ~27% (≈baseline) | +25pp 全归 SDF | "geometric supervision is the driver" — 最强 |
| ~35% | +18pp | "LoRA helps, SDF adds major benefit" — 仍强 |
| ~45% | +8pp | "LoRA is primary, SDF dose-dependent margin" — 需 lambda 曲线 |
| ~55%+ (≈SDF) | ≈0pp | SDF 无效 → pure analysis paper |

### Phase 2 升级路径

如果 Phase 2 (λ=0 resume from 10K) 结果：
- TSR ≥ 40% + CAR ≥ 40% → **"Two-phase safety encoding"** 成为独立技术贡献, 论文从 diagnostic 升级为 solution paper
- TSR 恢复但 CAR 也回落 → "safety requires continuous supervision" (informative negative)
- TSR 不恢复 → SDF 造成不可逆损伤 (strong negative, 支持 "tradeoff is severe" narrative)

## Anticipated Reviewer Concerns

### R1 (最致命): Generalizability
"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?"
→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)
→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%

### R2: Novelty of EE-only limitation
→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary

### R3: No solution
"诊断了问题但没解决"
→ **应对**: (1) EE displacement metric 是 positive 工具贡献; (2) SDF 确实产生真实避障，只是 tradeoff 极端; (3) Phase 2 如果成功 → 有 partial solution; (4) diagnostic framework 有方法论价值
→ **如果 Phase 2 成功**: R3 被完全化解

### R4: Action collapse is trivial
→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论

### R5 (新): SDF tradeoff too extreme to be useful
"TSR 73%→9% 说明 SDF 作为 safety method 不实用"
→ **应对**: (1) 本文不 claim SDF 是实用 solution，是 probe/case study; (2) Phase 2 / lambda tuning 是改善路径; (3) extreme tradeoff 本身是有价值的发现 — 说明 naive geometric supervision 不够

## Narrative Structure (5 Blocks)

### Block 1: Fake Safety Revelation (Claim 1)
- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)
- **Key finding**: CAR=91.5%, obstacle displacement < 0.1mm in 99.6% safe episodes, TSR=0%
- **Metric**: "obstacle displacement < 0.1mm" + "TSR=0%" 双证据 = action collapse = fake safety
- **Contribution**: displacement-filtered CAR

### Block 2: Stronger Models ≠ Safer (Claim 2)
- **Evidence**: eval_pi05_safelibero_object_v11 + spatial_v11
- **Key finding**: Pi0.5 CAR=28%, real_safe via geometric path (not avoidance behavior)
- **Narrative**: Capability↑ → motion↑ → collision↑; apparent safety is either frozen (Pi0) or path geometry (Pi0.5)

### Block 3: Oracle Upper Bound (Claim 3)
- **Evidence**: 3 oracle variants, all < baseline
- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help
- **Presentation**: Single unified table

### Block 4: EE-only Boundary (Claim 3)
- **Evidence**: spatial task eval, arm-body collision analysis
- **Narrative**: EE-only SDF = structural scope limit

### Block 5: SDF Training — Real Safety with Extreme Tradeoff (Claim 4, NEW)
- **Evidence**: Pi0.5+A1 3 seeds × 2 lambdas, all checkpoints consistent
- **Key finding**: CAR 27%→50-55% (+25pp), TSR 73%→5-9% (-65pp), EE disp ~0.5m (real avoidance)
- **Narrative**: SDF auxiliary loss DOES produce genuine collision avoidance — the first method to achieve real (non-fake) safety improvement on a capable VLA. But the extreme tradeoff reveals that naive geometric supervision disrupts task execution.
- **Sub-narrative**: LoRA attribution + Phase 2 recovery (if data available)

### 叙事原则
1. 每个 block 是 **evidence for structural claims**
2. Block 间逻辑递进：metric 有缺陷 (B1) → 强模型也不安全 (B2) → runtime 修正失败 (B3) → scope 边界 (B4) → training-time 方法可以但代价极端 (B5)
3. B5 是 positive result，展示"问题可解"但暴露新的 tradeoff 问题

## Figure Plan

| ID | 内容 | 优先级 | 数据来源 | 状态 |
|----|------|--------|---------|------|
| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 重要 | 设计 | 待做 |
| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | **必须** | 修复后 eval JSON | 数据就绪 |
| Fig 3 | TSR-CAR scatter (多模型 + SDF tradeoff 线) | 重要 | 全部 eval 数据 | 数据就绪 |
| Fig 4 | Oracle refinement CAR bar chart | **必须** | 3 oracle + baselines | 数据就绪 |
| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |
| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | **必须** | LoRA baseline + SDF 数据 | 待 LoRA 完成 |
| Table 2 | Phase 2 λ=0 ablation 结果 | 重要 | Phase 2 训练 | RUNNING |

## Dependencies (Research Phase)

- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval — confirmed real avoidance (D023)
- [x] EE displacement 修正 eval — 3 seeds corrected, all consistent
- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)
- [x] Oracle 3 variants (Claim 3) — all < baseline
- [x] Spatial/object collision analysis (Claim 3) — arm-body dominant
- [x] Pi0.5 baseline 3-seed (Claim 2) — CAR=26.8±1.6%
- [ ] **LoRA baseline** (Claim 4 attribution) — RUNNING, ETA ~09:30 UTC May 26
- [ ] **Phase 2 λ=0** (potential upgrade) — RUNNING on cuda:3
- [ ] **OpenVLA zero-shot eval** (Claim 1 generalization) — 启动中
- [ ] **spatial_bowl A1 训练** (Claim 4 generalization) — RUNNING on cuda:0, ~24h
- [ ] **Claim 1 EE disp re-eval** (术语验证) — 启动中 GPU 1, ~45min
- [ ] Lambda=0.1 bracket (4-point curve) — 待 GPU 释放
