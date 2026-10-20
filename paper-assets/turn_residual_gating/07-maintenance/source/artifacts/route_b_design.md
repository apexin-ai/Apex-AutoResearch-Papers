# Route B: Negative Result / Analysis Paper 实验设计

> 前提条件: LoRA-only eval 确认 gating 贡献为零（LoRA-only ≈ TG），或路线 A two-stage 失败后无缝转入
> 基于: paper_framing.md NF1-NF4, decisions D014-D017, memory.md v7 eval 发现
> 最后更新: 2026-05-19

---

## 1. 论文定位选项

### Option A: "Why Residual Gating Fails to Recover Goal Attention in Multi-Turn Dialogue"

- **定位**: 对 Dongre et al. (2605.12922) 诊断的首个系统性架构干预尝试 + 完整失败机制分析
- **核心贡献**: not "what works" but "why the most principled approach doesn't work and what this tells us about the problem's hardness"
- **叙事线**: Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98) → 自然推论: 在 residual connection 上施加 gate 即可恢复 attention → ThreadGate 是这一推论的最直接实现 → 它的失败揭示了 NTP-GAR 梯度冲突和 attention pattern 泛化性这两个更深层的障碍
- **强点**: ThreadGate 的设计动机直接来自 Dongre 的 residual probe evidence，不是 ad hoc 尝试；失败机制（NF1-NF3）有完整量化；对所有基于 attention steering 的方法有警示意义
- **弱点**: 只有一种干预方法族（residual gating），审稿人可能质疑"你只试了一种方法"
- **缓解**: UG/LoRA-only 消融 + Dongre 自己的 goal re-injection 也失败 = 两种独立干预路线均失败
- **竞争力**: Findings ~70%，加跨模型验证有冲 main 的可能

### Option B: "The Training-Inference Generalization Gap in Attention Steering"

- **定位**: 发现并量化 GAR 作为训练信号的泛化性根本问题
- **核心贡献**: 30x training-inference GAR gap + 机制分析（NTP-GAR 梯度冲突导致 attention pattern 过拟合）
- **叙事线**: GAR 在训练中可被有效优化（0.02→0.48）→ 但训练学到的 attention pattern 不泛化到新对话（推理 GAR=0.016）→ 根因是 NTP loss 主导使 gate 学到反向 turn conditioning → 这意味着所有基于辅助 attention loss 的方法都面临相同泛化障碍
- **强点**: 泛化性问题对所有 attention steering 方法都有意义（不只是 residual gating）；30x gap 是一个 striking 数字
- **弱点**: 需要更多方法（不只 ThreadGate/UG）验证泛化性问题的普遍性；claim 的 scope 大于证据
- **缓解**: Dongre 的 goal re-injection 失败可作为间接 evidence；Base model 在 ultrachat 上 GAR≈eval GAR 排除数据分布解释
- **竞争力**: 如果泛化性 claim 立得住 → main track 潜力更高；但需要更强的实验支撑

### Option C: "A Comprehensive Analysis of Goal Attention Recovery Mechanisms"

- **定位**: 系统性比较多种 GAR 恢复策略的 survey/analysis paper
- **额外工作量**: 需实现 2-3 种额外干预方法（positional bias calibration, attention re-weighting, periodic goal re-injection with proper training），每种 ~10-15h GPU，时间预算不允许
- **竞争力**: 如果做全了很强，但 EMNLP deadline 前完不成
- **结论**: 不推荐，除非路线 A/B 审稿人要求 major revision 时再扩展

### 推荐: Option A 为主，Option B 作为 framing 的一部分

Option A 的 scope 更聚焦、证据更充分、写作负担更小。Option B 的泛化性洞察作为 Discussion section 的核心论点融入，而非作为独立 paper 的中心 claim（避免 overclaim）。

---

## 2. 核心消融实验（四路 eval）

### 实验设计

四个条件在同一组 standard_conversations.json（base model 生成，5 组 × 10 轮）上评估，消除文本 confound（NF4 修正）。

| 条件 | 隔离目标 | GAR-ours | GAR-Dongre | nGAR | Gate profile | 状态 |
|------|----------|----------|-----------|------|-------------|------|
| Base (无训练) | 自然衰减 baseline | ~0.01 (ultrachat 已验证) | 待跑 | 待跑 | N/A | ✅ ultrachat 已跑，standard_conv 待统一 eval |
| TG v7 | 完整 ThreadGate | 0.016 (旧 eval) | 待重跑 | 待重跑 | 已有（D014 数据） | 待 standard_conv 统一 eval |
| UG | turn conditioning 增量 | 待跑 | 待跑 | 待跑 | 待跑 | ✅ 训练完成，eval 待做 |
| LoRA-only | gating 机制增量 | 待跑 | 待跑 | 待跑 | N/A (gate≡1.0) | 训练中 ~47.5% |

### 关键对比

1. **TG vs LoRA-only**: gating 机制是否有非零贡献（D012 核心问题）
2. **TG vs UG**: turn conditioning 是否有增量（如果两者 ≈，则 turn conditioning 无效）
3. **LoRA-only vs Base**: LoRA 微调本身是否改善/恶化 GAR
4. **所有条件 vs Base**: 任何训练干预是否改善推理时 GAR

### 预期结果（negative result 假设下）

- TG ≈ UG ≈ LoRA-only >> Base（LoRA 微调略改善 GAR，但 gating 无增量贡献）
- 或 TG ≈ UG ≈ LoRA-only ≈ Base（所有干预在推理时均无效）
- 任一结果都支撑 "residual gating 对推理时 GAR 无显著影响" 的 negative conclusion

---

## 3. 机制分析实验

### 3.1 NTP-GAR 梯度冲突量化

- **目的**: 量化 NTP loss 和 GAR loss 在 gate 参数上的梯度方向和幅度，为 NF1（反向 turn conditioning）提供机制解释
- **方法**: 在 v7 最终 checkpoint 上，取 10 个 ultrachat 样本做 single-step forward：
  1. 分别计算 ∇_gate(L_NTP) 和 ∇_gate(L_GAR)（28 层 × 每层 gate bias 参数）
  2. 逐层计算 cosine similarity: cos(∇_NTP, ∇_GAR)
  3. 计算梯度幅度比: ||∇_NTP|| / ||∇_GAR||
- **预期**: 
  - cosine < 0（两个梯度方向冲突），尤其在 GAR 已收敛的 late training 阶段
  - ||∇_NTP|| >> ||∇_GAR||（NTP 梯度幅度远大于 GAR），解释为什么 NTP 主导了 gate 学习方向
  - 不同 turn position 的冲突程度不同：早期 turn（短序列）冲突小，晚期 turn（长序列）NTP 梯度放大，冲突加剧
- **与 NF1 关系**: 如果晚期 turn 的 NTP 梯度推 gate→1.0 最强烈，直接解释为什么 gates 在晚期 turn 变为 passive（NF1 核心发现）
- **GPU 时间**: ~10min（10 次 forward+backward，无需训练）
- **代码**: 修改 train_threadgate.py，关闭 optimizer step，分别 backward 两个 loss 记录梯度

### 3.2 Gate Profile 深入分析

已有数据的深度挖掘，无需新实验，纯分析工作。

#### 3.2.1 Turn-by-turn gate 值变化（已有 D014 数据）
- 完整 28 层 × 10 turn 的 gate heatmap
- 标注 NF1 发现：27/28 层 diff (turn1 - turn21) < 0
- 识别异常层（唯一 diff > 0 的层是哪一层？是否与 Dongre goal-encoding 层有关？）

#### 3.2.2 Layer-wise gate 与 Dongre goal-encoding layers 对比
- Dongre 报告 Qwen-2.5-7B goal encoding 从 L5 开始（probe AUC 陡升）
- 训练时 L3/L4 为最低 gate（与 L4/L5 onset 位置 coincides，C4 suggestive）
- 推理时 L14/L23 动态范围最大（与训练不一致）
- 分析：为什么训练-推理的 critical layer 不同？是否与 NTP 梯度在不同层的相对强度有关？

#### 3.2.3 UG vs TG gate profile 对比
- 如果 UG 也产生相似的 per-layer 分化模式（L3/L4 最低）→ 分化是 GAR loss 驱动的，与 turn conditioning 无关
- 如果 UG 分化模式不同 → turn conditioning 确实影响了哪些层被抑制（即使方向错误）
- 已有线索（ROADMAP.md）：UG 训练也产生与 TG 相同的 per-layer 分化模式

### 3.3 Attention Pattern 可视化

- **目的**: 直观展示训练前后 attention 在 goal tokens 上的实际分布，让读者"看到"问题
- **方法**: 
  1. 取 3 个 standard_conversations 样本
  2. 对 Base / TG / UG / LoRA-only 四个条件提取 attention weights（全层全头）
  3. 对每个条件：绘制 goal tokens 上的平均 attention heatmap（x 轴 = 层，y 轴 = turn）
  4. 对比 TG 训练时（ultrachat 数据）vs 推理时（standard_conv 数据）的 attention pattern → 可视化 30x 过拟合
- **预期**: 
  - Base: 明确的 turn-wise attention 衰减
  - TG/UG/LoRA-only: 与 Base 差异极小（GAR 改善不泛化）
  - TG 训练时: goal tokens attention 显著增强（GAR=0.48 的视觉对应）
- **GPU 时间**: ~20min（四个模型各 forward 一次，提取 attention weights）
- **图表**: 1 个 4×1 subfigure（四个条件的 attention heatmap）+ 1 个训练 vs 推理对比图

### 3.4 GAR 泛化性分析

- **已有**: 训练 GAR=0.48 vs 推理 GAR=0.016（NF2，30x 断层，confirmed non-bug by D015）
- **已有**: Base model GAR on ultrachat ≈ GAR on eval data（~0.01），排除数据分布假设
- **新增 per-layer GAR breakdown**:
  - 目的：哪些层的 GAR 过拟合最严重？是否与 gate 分化最大的层相关？
  - 方法：分别在训练数据和 eval 数据上计算逐层 GAR，绘制 per-layer GAR ratio (train/eval)
  - 预期：所有层都过拟合，但 L3/L4（gate 分化最大层）可能过拟合更严重或更轻微 — 任一结果都有分析价值
- **新增 training trajectory GAR 泛化曲线**:
  - 目的：GAR 过拟合是渐进的还是突发的？与三阶段训练动力学（plateau → phase transition → convergence）的哪个阶段对应？
  - 方法：在训练过程的 5 个 checkpoint（gs50, gs100, gs150, gs200, gs400）上分别计算 eval GAR
  - 预期：训练 GAR 在 gs75-144 急升（phase transition），eval GAR 是否同步上升？如果不同步 → 过拟合在 phase transition 阶段即开始
- **GPU 时间**: ~30min（5 个 checkpoint × 1 次 eval forward）

### 3.5 训练动力学三阶段分析（已有数据，需可视化）

v7 训练呈现清晰的三阶段动力学（memory.md 记录），这是 paper 的亮点之一：

1. **Plateau (gs0-75)**: GAR ≈ 0.02，gate 在初始状态附近微调
2. **Phase transition (gs75-144)**: GAR 从 0.02 急升至 0.48，gate profile 快速分化
3. **Convergence (gs144+)**: GAR 稳定在 target=0.5 附近，gate_std plateau 在 0.05+

- **可视化**: 训练 GAR + gate_mean + gate_std + L_NTP + L_GAR 的五合一 training dynamics 图
- **叙事价值**: 说明 MSE 双向 loss 确实能驱动 gate 学到有意义的结构，问题不在训练而在泛化
- **数据来源**: v7_training_dynamics_csv（已有 artifact）

---

## 4. 跨模型验证（Llama-3.1-8B-Instruct）

跨模型验证是 Route B 从 Findings 冲 main track 的关键加分项（D017）。

### 4.1 Phase 1 复现：GAR 衰减诊断

- **目的**: 在第二个模型上确认 GAR 衰减现象（Dongre 已在 12 个模型上验证，但我们需要自己的数据来做完整对比）
- **方法**: 用 Phase 1 GAR 诊断脚本在 Llama-3.1-8B-Instruct 上跑
- **预期**: 同样观察到 GAR 衰减（Dongre 在 Llama-3.1-8B 上报告 27-48% 衰减范围）
- **代码适配**: turn_utils.py 已支持 Llama chat template（D015 后完成）
- **模型路径**: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/（ModelScope 通道，已有 tokenizer，权重 ~16GB 需下载）
- **GPU 时间**: ~30min
- **磁盘**: 需先清理 Qwen cache 腾出空间（当前 15G/30G 可用，Llama 权重 ~16GB）

### 4.2 ThreadGate v7 训练

- **目的**: 在 Llama 上复现 ThreadGate 的 negative finding
- **方法**: 用与 Qwen v7 相同的设置（MSE+gate_div, λ_gar=1.0, λ_div=1.0, 3 epoch）
- **预期**: 
  - 训练 GAR 同样可被优化到 ~0.5（MSE loss 有效性是模型无关的）
  - 推理 GAR 同样过拟合（如果确认 → NF2 普遍性加强）
  - Turn conditioning 同样反向（如果确认 → NF1 是 NTP-GAR 竞争的结构性后果，不是 Qwen 特有的）
- **代码适配**: threadgate.py 自动读取 hidden_dim (4096 for Llama vs 3584 for Qwen) / num_layers (32 for Llama vs 28 for Qwen)
- **GPU 时间**: ~6h（Llama-3.1-8B 比 Qwen-2.5-7B 稍大）

### 4.3 消融（可选，视时间预算）

- 如果时间允许：在 Llama 上也跑 UG + LoRA-only 消融
- 如果时间不允许：只做 TG + Base 对比，消融数据仅在 Qwen 上报告
- GPU 时间（如做）: UG ~6h + LoRA-only ~6h

### 4.4 跨模型 gate profile 对比

- 如果 Llama 上也出现类似的 per-layer 分化模式（某些浅层 gate 最低）→ 更强的普遍性 evidence
- 如果 Llama 的 critical layer 不同（如 L2 最低，对应 Dongre 报告 Llama goal-encoding onset 在 L2）→ 说明 gate 确实学到了模型特异的 goal-encoding 结构，但仍然无法泛化到推理
- 两种结果都有分析价值

---

## 5. 与 Dongre et al. (2605.12922) 的关系

### 互补定位

| 维度 | Dongre et al. | 本文 |
|------|---------------|------|
| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认（Qwen 70.8% raw, 21% normalized），我们的测量定义更宽（含 first user query） |
| 机制分析 | residual probe AUC=0.98（goal info 持续存在） | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |
| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |

### 共同推论

两种独立干预路线（prompt-level goal re-injection + architecture-level residual gating）均失败，共同指向：

1. 简单的 attention steering 不足以对抗 NTP 的优化压力
2. 需要更深层的架构改变（如 decoupled goal-processing pathway，或 inference-time attention intervention 绕过训练泛化问题）

### 我们的独特增量

Dongre 诊断了问题，但没有解释为什么干预难以成功。我们量化了三个具体障碍：
1. **NTP-GAR 梯度冲突**（NF1 + 3.1 实验）: NTP loss 在 gate 参数上的梯度方向与 GAR loss 相反
2. **Attention pattern 不泛化**（NF2 + 3.4 实验）: 训练中学到的 attention redistribution 不迁移到新对话
3. **Gate 干预强度不足**（NF3）: 推理时 gate 仅 2-7% attenuation，远不足以改变 attention pattern

---

## 6. 论文结构草案（Option A framing）

1. **Abstract** (150-250 words): 问题（GAR 衰减）→ 动机（Dongre residual probe → residual gating 是自然方案）→ 方法（ThreadGate）→ 核心发现（三个失败机制）→ 意义
2. **Introduction** (5 段): 多轮对话退化 → Dongre 诊断 + residual stream 持续性 → ThreadGate 设计动机 → 三个 negative findings 概述 → 贡献列表
3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering
4. **Background**: GAR 定义（cite Dongre）+ residual stream persistence 证据
5. **Method**: ThreadGate 架构 + MSE+gate_div loss + 训练设置
6. **Experiments**: 四路消融 + 跨模型验证 + 训练动力学
7. **Analysis**: NTP-GAR 梯度冲突 + GAR 泛化性分析 + gate profile 深入分析 + attention 可视化
8. **Discussion**: 为什么 residual gating 不够 + 对 attention steering 方法的启示 + 潜在解决方向
9. **Conclusion**: negative result 总结 + 对社区的建议

### 贡献列表（草案）

1. 首个基于 residual stream persistence 证据设计的架构级 GAR 恢复干预（ThreadGate），及其完整失败分析
2. 发现并量化 NTP-GAR 梯度冲突导致 turn conditioning 反向学习的机制
3. 量化 GAR 训练信号的泛化性问题（30x training-inference gap），对所有基于辅助 attention loss 的方法有警示意义
4. 四路消融 + 跨模型验证的完整实验设计，为后续研究提供 baseline 和诊断工具

---

## 7. 实验时间表

| 实验 | GPU 时间 | 依赖 | 预计完成 |
|------|----------|------|----------|
| LoRA-only 训练完成 | ~3h (剩余) | 无 | D+0 (2026-05-19) |
| 四路 eval on standard_conv (Qwen) | ~1h | LoRA-only 完成 | D+0 |
| 梯度冲突分析 (3.1) | ~10min | v7 checkpoint | D+0 |
| Attention 可视化 (3.3) | ~20min | 四路 checkpoint | D+0 |
| GAR 泛化曲线 — 5 checkpoints (3.4) | ~30min | v7 中间 checkpoints | D+1 |
| 训练动力学可视化 (3.5) | ~0 (纯绘图) | v7_training_dynamics_csv | D+0 |
| Gate profile 深入分析 (3.2) | ~0 (纯分析) | 四路 eval 数据 | D+1 |
| Llama 模型下载 | ~30min (网络) | 磁盘清理 | D+1 |
| Phase 1 GAR 诊断 (Llama) | ~30min | Llama 模型下载 | D+1 |
| TG v7 训练 (Llama) | ~6h | Llama 模型下载 | D+2 |
| Llama eval + gate profile | ~1h | Llama TG 完成 | D+2 |
| [可选] Llama UG + LoRA-only | ~12h | Llama TG eval | D+3-4 |

**总 GPU 时间**: ~12h（核心）+ ~12h（可选 Llama 消融）
**写作启动**: D+2（Qwen 全部数据就绪后可开始 Method/Background/Related Work）
**完整初稿**: D+7-10（假设跨模型验证顺利）

---

## 8. 风险与应急

| 风险 | 概率 | 影响 | 应急 |
|------|------|------|------|
| LoRA-only 意外优于 TG（gating 有负面贡献） | 低 | 叙事调整：gating 不仅无效还有害（更强的 negative finding） | 额外分析 why gating hurts |
| Llama 上 GAR 衰减模式与 Qwen 显著不同 | 中 | 跨模型 claim 弱化 | 聚焦 Qwen 深度分析，Llama 作为补充 |
| Llama 上 ThreadGate 意外成功 | 极低 | 整个 negative framing 需要重写 | 转回 Route A，Qwen 失败 + Llama 成功本身是更有趣的故事 |
| 磁盘空间不足以同时存 Qwen + Llama checkpoints | 中 | Llama 实验延迟 | 先完成 Qwen 所有分析，删除中间 checkpoints，再下载 Llama |
| 审稿人认为"只测了 residual gating 一种方法，negative result 太窄" | 高 | reject 风险 | Discussion 中系统性分析为什么其他方法（attention re-weighting, positional bias）也面临类似障碍；cite Dongre goal re-injection 失败 |
| 梯度冲突分析结果不显著（cosine ≈ 0 而非 < 0） | 中 | NF1 的机制解释弱化 | 转为 "orthogonal gradients = GAR loss 无法有效引导 gate" 的叙事（NTP 不一定反对，但 GAR 信号太弱被淹没） |
