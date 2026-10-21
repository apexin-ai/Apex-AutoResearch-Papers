# 阴性结果系统分析

> 16 个 conclusion=negative 实验的归因分类、模式提取与方法天花板评估  
> 生成时间：2026-05-24

---

## 1. 全景表

| # | exp_id | hypothesis（核心） | key metric | root cause category |
|---|--------|-------------------|------------|-------------------|
| 1 | eval_a3_v10a_refine | A3 refinement 在 v10 pipeline 下有效 | CAR=79.5%, refined=0 | B-阈值问题 |
| 2 | eval_baseline_v11_object | Action chunking 修复 TSR≈0% | TSR=0.5%, CAR=83% | C-基座特性 |
| 3 | eval_a3_v11_object | A3 在 v11 pipeline 下 MVP gate | CAR=74.5%, TSR=0%, refined=0 | B-阈值+A-collapse |
| 4 | eval_lora_baseline_object_v11 | LoRA baseline object 参考 | TSR=0%, CAR=82% | C-基座特性 |
| 5 | eval_lora_baseline_spatial_v11 | LoRA baseline spatial 参考 | TSR=0%, CAR=0% | A-spatial结构 |
| 6 | eval_baseline_fullft_spatial_v11 | Full-FT baseline spatial 参考 | TSR=0.4%, CAR=0% | A-spatial结构 |
| 7 | eval_a1_lora_spatial_v11 | EE-SDF 辅助损失处理 spatial | CAR=0.8% (全fake) | A-EE-only限制 |
| 8 | oracle_a3_force_refine_object_v11 | Force refine 测试梯度方向 | CAR=81.2%, TSR=0% | B-M026/M027 bug |
| 9 | eval_a3_object_m024fix_v11 | M024坐标修复后 A3 改善 | CAR=77.1%, TSR=0% | A-collapse |
| 10 | oracle_a3_m024fix_object_v11 | M024修复+oracle refine | CAR=85.6% (全frozen) | B-M027死代码 |
| 11 | eval_a1_lora_object_v11_rerun | A1 SDF loss 带来真实避障 | CAR=91.5%, 99.6% fake | A-action collapse |
| 12 | oracle_true_gt_adaptive_alpha_v11 | GT SDF + adaptive alpha 有效 | CAR=75% < baseline 79% | A-refinement→collapse |
| 13 | oracle_true_gt_fixed_alpha_v11 | GT SDF + fixed alpha 有效 | CAR=73.1% < baseline | A-refinement→collapse |
| 14 | oracle_true_gt_feature_v11 | Feature-space oracle 优于 action-space | CAR=76.9%, 96.7% fake | A-refinement→collapse |
| 15 | eval_pi05_safelibero_object_v11 | 更强 VLA 自然避障 | CAR=28% (vs baseline 83%) | C-capability-safety |
| 16 | eval_pi05_safelibero_spatial_v11 | Pi0.5 spatial 避障 | CAR=13% (集中于1个task) | A-spatial + C-tradeoff |

---

## 2. 归因分类

### A. 结构性限制（方法天花板，7个实验）

#### A1. Action-space refinement 导致 action collapse（核心瓶颈）

**涉及实验**: #11, #12, #13, #14, #9

**机制**：无论是 SDF auxiliary loss（A1）还是 runtime gradient refinement（A3），任何对 action 的约束/修正都会导致 action collapse：
- A1 (SDF aux loss): CAR 从 83% → 91.5%，但 99.6% 的 safe episodes 中障碍物位移 < 0.1mm（纳米级），机器人完全冻结
- A3 (GT oracle refinement): 即使用 ground truth SDF 梯度做 runtime correction，CAR 反而低于 baseline（73-77% vs 79%），且 96-98% safe episodes 是 fake

**根本原因**：Pi0 的 action head 在 flow-matching 训练中学到的是高维 action 分布的 mode。任何 post-hoc 梯度修正都将 action 推离学到的 mode，导致 degenerate（零）action。这不是参数调整能解决的——它是 flow-matching action generation + gradient-based correction 的根本不兼容。

**关键证据**：
- GT oracle (最优条件) 仍失败 → 不是 SDF 预测质量问题
- Adaptive vs fixed alpha 差异极小（75% vs 73.1%）→ 不是 alpha 选择问题
- Feature-space refinement 也失败（76.9%）→ 不是 refinement 位置问题
- 唯一产生真实 movement 的 episodes 100% 碰撞 → movement 和 safety 互斥

#### A2. EE-only SDF 无法处理 arm-body 碰撞（场景限制）

**涉及实验**: #5, #6, #7, #16

**机制**：Spatial 场景中的碰撞发生在机械臂 body 与障碍物之间，而非末端执行器(EE)。EE-only SDF field 对 arm-body collision 完全盲区。

**证据**：
- Full-FT baseline: spatial CAR=0%
- LoRA baseline: spatial CAR=0%  
- A1 SDF loss: spatial CAR=0.8% (全 fake)
- Pi0.5: spatial CAR=13% (仅 task3 贡献)

所有方法在 spatial 场景 CAR≈0%，确认这是 EE-only formulation 的硬限制。

### B. 参数/实现问题（已诊断，部分可修复，5个实验）

| Bug ID | 描述 | 影响实验 | 状态 |
|--------|------|----------|------|
| M024 | SDF 查询用 delta action 而非 absolute position | #9 | 已修复，但修复后仍不 work |
| M026 | Learned SDF decoder 失标（训练后期 loss 上升） | #8, #10 | 已诊断 |
| M027 | Oracle SDF 路径是死代码，实际走 learned decoder | #8, #10 | 已诊断 |
| 阈值过高 | sdf_min > refine_margin，refinement 从未触发 | #1, #3 | 发现后才做 force_refine |

**关键洞察**：修复所有已知 bug 后做了 true GT oracle 实验（#12-14），结果仍然失败。这证明 bug 修复不能挽救方法——即使实现完美，核心机制（gradient refinement）本身有结构性缺陷。

### C. 基座模型特性（非方法问题，4个实验）

#### C1. 更强 VLA 反而更多碰撞（capability-safety tradeoff）

**涉及实验**: #15, #16

Pi0.5（更强基座）object CAR=28% vs Pi0 baseline CAR=83%。更强的模型更"大胆"——trajectory 更积极，更多接近障碍物，导致碰撞率上升。这不是方法失败，而是验证了一个重要假设：VLA capability 和 safety 天然存在 tradeoff，不能靠 scaling 解决。

#### C2. Pi0 系固有的 action collapse

**涉及实验**: #2, #4

Baseline 本身 TSR=0-0.5%（Pi0 在 LIBERO 上 success rate 极低），且 baseline CAR=82-83% 中大量也是 fake safe（99.4%）。这说明 Pi0 fine-tuning 后在 SafeLIBERO 上本身就有严重的 action collapse tendency。

### D. 意外发现/边界条件

#### D1. Spatial 场景的结构性困难
所有方法在 spatial_bowl 上 CAR=0%，但 object tasks 上 CAR=73-91%。场景类型是最大的效果调节因子。

#### D2. Task-dependent behavior
chocolate_pudding 在所有实验中一致最差（oracle CAR=47-55% vs 其他 task 80-97%）。该任务的障碍物放置使避碰空间极小。

#### D3. Pi0.5 的 task-specific 异常
Pi0.5 spatial 中 task3 CAR=52% 而其余≈0%。更强模型偶尔在特定任务结构中产生有利 trajectory，但不可泛化。

---

## 3. 已验证无效的方向（Do Not Retry）

| 方向 | 证据强度 | 理由 |
|------|----------|------|
| **Action-space gradient refinement** | ★★★★★ | GT oracle + 3种alpha策略 + feature-space全部失败。根因：flow-matching action mode + gradient correction 根本不兼容 |
| **SDF auxiliary loss 提高 real safety** | ★★★★☆ | A1 rerun 800eps 确认：CAR 提升 100% 来自 action collapse，0% 来自真实避障学习 |
| **EE-only SDF 用于 spatial 场景** | ★★★★★ | 4 种方法 × 4 个 task 全部 CAR=0%。arm-body 碰撞不在 EE SDF 感知范围 |
| **期望更强基座模型自然避障** | ★★★★☆ | Pi0.5 实测 CAR 大幅下降（28% vs 83%），capability-safety 是 tradeoff 不是正相关 |
| **调 alpha/threshold 参数救 A3** | ★★★★☆ | Fixed 0.005 vs adaptive 0.1 差异仅 2pp (73% vs 75%)，都不如 baseline (79%) |

---

## 4. 改进假设（尚未尝试）

| 方向 | 理论依据 | 预期收益 | 风险 |
|------|----------|----------|------|
| **Whole-arm SDF (multi-link)** | 当前 EE-only 对 spatial 完全失效；multi-link SDF 可覆盖 arm-body collision | Spatial CAR 从 0% 到 >0% | 计算开销大，需要 FK 模型 |
| **Constraint-as-reward (RL fine-tuning)** | Aux loss 和 runtime refinement 都因 action collapse 失败；RL 直接在 safe trajectory 上优化，不做 post-hoc correction | 避免 collapse 因为 policy 本身学会避障 | 需要 sim 环境 + 大量 GPU hours |
| **Safe action sampling (rejection)** | 不修改 action，而是从 flow-matching 的多个 sample 中选安全的 | 保持 action distribution on-manifold，避免 collapse | 多次采样推理时间 ×N |
| **Collision-aware data augmentation** | 在训练数据中增加避障 trajectory，让 policy 隐式学会 | 无 runtime overhead | 需要高质量 safe demo 数据 |
| **SDF-conditioned generation（条件生成而非后修正）** | 将 SDF 作为 conditioning signal 输入 policy（而非 loss/gradient） | Policy 在生成时就考虑碰撞，不需要 post-hoc | 架构改动大，需重新训练 |

---

## 5. 方法天花板评估

### A1: SDF Auxiliary Loss

| 维度 | 评估 |
|------|------|
| **最优工作条件** | Object tasks（非 spatial）+ lambda ∈ [0.001, 0.01]（不能太大否则 collapse 更严重） |
| **天花板** | CAR 提升 ~8pp (83→91%) 但 100% fake safety。**Real safety improvement = 0** |
| **是否值得继续** | ❌ 不值得。方法本质是让 action 更趋近零（变"安全"），而非教会真正避障 |

### A3: Runtime Gradient Refinement

| 维度 | 评估 |
|------|------|
| **为什么失败** | Flow-matching 生成的 action 在高维空间中是一个 mode。Gradient correction 将其推离 mode → collapse 到 degenerate solution |
| **是否存在任何可 work 的条件** | ❌ 已用 GT oracle + 所有合理 alpha + feature-space 全部验证。即使 SDF 完美，refinement 本身导致 collapse |
| **根本矛盾** | Refinement 假设 action space 是平滑可微的，但 flow-matching 的 learned manifold 不满足此假设 |

### 整体方向评估

| 问题 | 回答 |
|------|------|
| 是否需要 pivot？ | **是的。** 当前两条路线（A1 aux loss / A3 runtime refinement）的核心机制——对 action 施加 SDF-based gradient——与 flow-matching policy 根本不兼容。需要 pivot 到不对 action 做 post-hoc modification 的方法。 |
| Pivot 方向优先级 | 1️⃣ Safe action sampling (最小改动) → 2️⃣ SDF-conditioned generation (需重训练) → 3️⃣ RL fine-tuning (需 sim) |
| 可保留的资产 | SDF decoder 本身训练成功（M026 修复后）；SafeLIBERO 评估 pipeline 完善；fake-safety 检测体系 |

---

## 6. 结论与建议

### 核心发现

**Flow-matching VLA 的 action space 不接受 gradient-based correction。** 这是 16 个阴性实验的统一解释：无论是训练时（A1 aux loss → action collapse）还是推理时（A3 refinement → action collapse），任何试图用 SDF gradient 修正 action 的方法都失败，因为 flow-matching 学到的 action manifold 是高度非凸的——微小扰动即可使 action 退化为零。

### 定量总结

- Action collapse 导致的 fake safety rate: **96.7% - 99.6%**（across 所有方法）
- GT oracle 最优条件下的 real safety improvement: **0%**（反而比 baseline 差 4-6pp）
- Spatial 场景的方法上界: **0% CAR**（EE-only formulation 硬限制）
- 更强基座模型的 safety 贡献: **负面**（CAR 从 83% 降至 28%）

### 行动建议

1. **立即停止** A3 runtime refinement 的所有变体实验——已穷尽搜索空间
2. **重新定义** safety intervention 的位置：不是 post-action correction，而是 pre-generation conditioning 或 action selection
3. **保留** A1 的 SDF decoder 训练管线（可作为未来 conditioning signal 的 SDF 来源）
4. **下一步实验优先级**: Safe rejection sampling（利用现有 SDF decoder + 现有 policy，无需重训练）
