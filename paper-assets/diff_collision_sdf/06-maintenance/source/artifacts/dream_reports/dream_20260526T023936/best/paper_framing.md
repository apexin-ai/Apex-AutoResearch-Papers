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
**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标
**术语修正 (D023)**: 论文中 fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主，明确区分 "obstacle displacement" 和 "EE displacement"

**dfCAR 定位 (D024 Dream 反馈)**:
- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR
- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑
- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)
- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）
- 待确认：800ep Pi0+A1 eval 数据是否可 post-hoc 提取 EE displacement

### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)
更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。

**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
**限制**: 仅 2 model families; Pi0 的 "高 CAR" 来自 action collapse; 降级为 observation, 不 claim 因果

### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)
End-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。

**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系
**限制**: "EE-only 不够" 是 expected result; 缺乏 full-body SDF 对照

### Claim 4: Fine-tuning Produces Real Avoidance; SDF is Redundant (Negative Finding — 证据强度 ★★★★) [D025]
LoRA fine-tuning on collision-free SafeLIBERO demonstrations produces genuine collision avoidance (+29pp CAR, EE displacement ~0.48m, 0% fake safety) WITHOUT explicit geometric supervision. Adding SDF auxiliary loss contributes 0pp additional CAR — geometric supervision is redundant when demonstrations already encode avoidance behavior. Both LoRA-only and LoRA+SDF suffer identical catastrophic task performance collapse (TSR 73%→6%).

**证据 (confirmed, D025)**:
- LoRA-only (2 seeds): CAR=55.3%, TSR=6.3%, EE disp=0.478m, frozen=0%
- LoRA+SDF λ=0.005 (3 seeds): CAR=50.5%, TSR=6.8%
- LoRA+SDF λ=0.01 (3 seeds): CAR=52.8%, TSR=6.8%
- Per-task CAR pattern 完全一致——高/低 CAR 由任务布局决定，非 SDF loss
- SDF delta = -3pp (不显著, 在 ±3.5pp SE 内)

**Claim 措辞**: "LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance (+29pp CAR, 0% fake safety) on Pi0.5. Explicit SDF geometric supervision adds no additional benefit — the avoidance signal is already implicit in the training data. Both conditions suffer equal catastrophic task performance collapse (TSR: 73%→6%), indicating the tradeoff is a property of fine-tuning, not geometric supervision."

**论文价值**: 这是一个有价值的 negative finding——揭示 VLA collision avoidance 的来源是训练数据中的隐式安全信号，而非显式几何感知。这对"safety-by-design"方法论有重要启示。

**禁区**: SDF works / SDF contributes / geometric supervision helps

**待确认**:
- LoRA seed2 (plan_013) → 3v3 seeds 统计确认
- Phase 2 λ=0 → 如果 SDF 无效，"removing SDF" 的实验解读需调整
- Lambda=0.1 → 更强 SDF penalty 是否改变结论？

### Phase 2 重新解读 (D025 后)

Phase 2 (λ=0 resume from 10K SDF checkpoint) 的意义已改变：
- 原意图：测试 SDF safety encoding 是否 persist → 如果 SDF 本身无效，persist 什么？
- 新解读：Phase 2 测试的是"10K 步 SDF 训练是否改变了模型行为相对于 LoRA-only"
- 如果 Phase 2 CAR ≈ LoRA-only (55%) → 进一步确认 SDF 无效（模型回归 LoRA-only 水平）
- 如果 Phase 2 CAR < LoRA-only → SDF 训练可能造成持久损伤
- 如果 Phase 2 CAR > LoRA-only → SDF 可能有微妙的持久效应（需要更多证据）

## Anticipated Reviewer Concerns

### R1 (最致命): Generalizability
"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?"
→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)
→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%

### R2: Novelty of EE-only limitation
→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary

### R3: No solution
"诊断了问题但没解决"
→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要

### R4: Action collapse is trivial
→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论

### R5 (更新 D025): SDF redundancy — why bother testing it?
"SDF 无效不是早该预见的吗？"
→ **应对**: (1) 先验地，SDF geometric supervision 是合理的 safety method（motion planning 领域广泛使用）; (2) negative result 的价值在于排除一条看似合理的路径; (3) 关键 insight 不是 "SDF 失败" 而是 "avoidance 来自 demo imitation, not geometry" — 这对未来 safety method 设计有指导意义

### R6 (新 D025): Fine-tuning collapse — is this just catastrophic forgetting?
"TSR 73%→6% 可能只是小数据 fine-tuning 的 catastrophic forgetting，不是 safety 相关的发现"
→ **应对**: (1) 可能确实是 catastrophic forgetting，但这恰恰说明当前 VLA fine-tuning pipeline 不适合 safety adaptation; (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR — 模型学到了"保守行为"而非"安全行为"; (3) 区分 conservative avoidance vs genuine safety awareness 是后续工作方向

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

### Block 5: Fine-tuning Attribution — Real Avoidance from Demonstrations, Not Geometry (Claim 4, D025)
- **Evidence**: LoRA-only 2 seeds + SDF 3 seeds × 2 lambdas, per-task comparison
- **Key finding**: LoRA-only CAR=55% ≥ SDF CAR=52%, both TSR≈6%, identical per-task patterns
- **Narrative**: Fine-tuning on collision-free demonstrations produces genuine collision avoidance (+29pp CAR, 0% fake safety). Explicit SDF geometric supervision adds nothing. The avoidance signal is implicit in the training data. But both conditions suffer catastrophic task performance collapse — the model learns conservative behavior, not safe behavior.
- **Sub-narrative**: lambda curve (if SDF is redundant at 0.005/0.01, is it redundant at 0.1 too?) + Phase 2 (does SDF leave any persistent effect?)

### 叙事原则
1. 每个 block 是 **evidence for structural claims**
2. Block 间逻辑递进：metric 有缺陷 (B1) → 强模型也不安全 (B2) → runtime 修正失败 (B3) → scope 边界 (B4) → fine-tuning 产生真实避障但 SDF 冗余 (B5)
3. B5 是 diagnostic result + negative finding，展示"避障可实现但来源不是几何感知"

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
- [x] **LoRA baseline** (Claim 4 attribution) — DONE: CAR=55%, SDF delta=0pp → SDF redundant (D025)
- [ ] **LoRA baseline seed2** (plan_013) — 统计确认, RUNNING on westd-45947
- [ ] **Phase 2 λ=0** — RUNNING on cuda:3, 解读已调整(D025)
- [ ] **OpenVLA zero-shot eval** — BLOCKED (模型下载损坏)
- [ ] **spatial_bowl A1 训练** — RUNNING on cuda:0, ~20h
- [ ] **Lambda=0.1 × 2 seeds** — RUNNING on cuda:1-2, ~20h
- [ ] **Pi0.5 baseline re-eval** — 启动中 westd-45947, 补 EE displacement baseline 数据
- [ ] **Claim 1 EE disp re-eval** (术语验证) — 启动中 GPU 1, ~45min
- [ ] Lambda=0.1 bracket (4-point curve) — 待 GPU 释放
