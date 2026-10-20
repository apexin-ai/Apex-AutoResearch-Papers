# 双路叙事框架草稿

> 日期：2026-05-14 | 状态：待 seed=0 结果决定路径

## 路径 A：seed=0 复现 eff_rank 反升

### Core Insight（1-2 句）

Holdout spectral effective rank 在 iterative model collapse 中反直觉地上升——模型生成完全坍缩到单一 token 时，权重空间的谱维度反而膨胀。这说明 spectral diversity 与 generative diversity 是根本解耦的，挑战了"谱指标可监测 collapse"的隐含假设。

### Story Arc

1. **问题**：Iterative synthetic training 导致 model collapse 已被系统验证（Shumailov et al., Nature 2024），即使极低比例的 synthetic data 也有风险（Dohmatob & Feng, ICLR 2025）。现有 adaptive data mixing 方法（DoReMi, Aioli）基于 loss 信号而非 collapse 特异性指标，无法在 collapse 早期主动干预。
2. **假设被挑战**：Spectral effective rank 作为 representation diversity 的度量（Jha & Reagen, EMNLP 2025），被隐含假设可监测 model collapse——谱集中意味着表示退化，谱分散意味着表示健康。多项工作用 spectral metrics 分析模型质量（SIGMA, Spectral Scaling Laws），但未在 iterative collapse 场景下验证。
3. **发现**：Pythia-1B 在 wikitext-103 上经 3 代纯 synthetic 训练后（seed=42），生成 unigram entropy 从 6.93 降至 0.00（unique tokens: 23586→1），模型完全 mode-collapsed。然而 holdout spectral effective rank 从 676.96 **上升**至 683.44（+0.96%），PPL 仅从 13.27 涨至 13.59（+2.4%）。**待 seed=0 验证是否 multi-seed robust**（mvp_seed0_replication_r2 进行中）。
4. **机制解释**：Mode collapse 导致权重矩阵对少数 output directions 的梯度持续放大，其他方向缺乏抑制信号而自由漂移，导致奇异值谱从"少数主导、长尾衰减"变为"多方向均匀分散"——即 spectral flattening。这与 "On the Spectral Flattening of Quantized Embeddings"（arXiv 2602.00969）的独立发现一致：他们观察到量化噪声使截断 SV 谱尾上抬、stable rank 上升，同样伴随 representational collapse。本质上，effective rank 测量的是权重空间的"均匀分散程度"，而非输出分布的"多样性"——两者可以也确实反向运动。
5. **正确信号**：N-gram entropy 在 G1 第 2 个 checkpoint（step 152, 10M tokens）即检测到 collapse（unigram entropy -43.5%），远早于 PPL 的微弱反应。这与 Shi et al.（NeurIPS 2025 Spotlight）的发现一致：entropy 基指标是 collapse 最有效的检测手段。Surplexity（Gambetta et al., 2024）作为 perplexity 变体也指向同一方向。N-gram entropy 的优势在于：(a) 不需要额外模型推理，仅需 CPU 上的 O(N) 统计；(b) 检测延迟远短于 eff_rank——n-gram entropy 在 G1 step 152 即触发（-43.5%），而 generated eff_rank 直到 G1 final（step 305）才显示显著变化，检测延迟约 2 倍（注：holdout eff_rank 始终未触发，方向相反）。
6. **干预**：PI 控制器以 unigram entropy 为反馈信号，动态调节 real/synthetic mixing ratio。当 entropy 低于 setpoint（G0 baseline × 0.9），控制器增加 real data 比例以抵抗 collapse；entropy 恢复后释放 ratio 以利用 synthetic data 的 augmentation 价值。这是首个将 collapse detection 接入闭环控制器的 data mixing 框架，填补了"collapse-aware adaptive mixing"的文献空白。

### Core Claims

- **Claim 1 (Decoupling)**：Holdout spectral effective rank 与 generative model collapse 完全解耦——在 seed=42 上，模型生成从 23K+ unique tokens 坍缩至 1 token 时，eff_rank 反而上升 +0.96%。**待 seed=0 验证 multi-seed robustness**。
  - *支撑实验*：mvp_pilot_v7（seed=42）已完成 + mvp_seed0_replication_r2（seed=0，进行中），3 代纯 synthetic training
  - *扩展验证*：Pythia-410M / Pythia-2.8B 跨规模复现（如资源允许）

- **Claim 2 (Superior Detection)**：N-gram entropy 比 spectral effective rank 更早、更可靠地检测 iterative model collapse——在 G1 第 2 个 checkpoint（10M tokens, step 152）即检测到 collapse（-43.5%），检测延迟约为 generated eff_rank 的 1/2（eff_rank 直到 G1 final step 305 才显著变化），且 holdout eff_rank 始终未触发（方向相反）。
  - *支撑实验*：pivot_b_verification（18 checkpoint 全对比），mvp_pilot_v7 逐 checkpoint 数据
  - *扩展验证*：多 seed + 多规模下的 detection delay 对比

- **Claim 3 (Effective Intervention)** ⚠️ **SPECULATIVE — 当前零实验支撑**：基于 n-gram entropy 的 PI 控制器能用更少的 real data 实现与高 real-data 固定比例相当的 collapse 抑制效果——在 5 代 iterative training 中维持 entropy ≥ 0.9×baseline 的同时，real data 用量低于 fixed w=0.7 策略。
  - *支撑实验*：Plan A 实验矩阵 Phase 1（6 策略 × 1 seed × 5 gens）+ Phase 2（top-3 × 3 seeds × 5 gens）— **尚未开始**
  - *前提*：需要 Plan A 实验完成并验证 PI 控制器确实优于 fixed-ratio baselines
  - *降级条件*：如果 Claim 3 最终不成立（PI 未显著优于 fixed ratio），论文降级为 EMNLP Findings track，仅保留 Claim 1-2（decoupling + detection）

### 需要的实验支撑

| Claim | 已有数据 | 待做实验 | 优先级 |
|-------|---------|---------|--------|
| Claim 1 | v7 (seed=42) 3 代数据 | seed=0 复现（RUNNING）；Pythia-410M/2.8B 跨规模（可选） | P0 (seed=0)，P2 (跨规模) |
| Claim 2 | pivot_b_verification 18 ckpt 对比 | 多 seed 下检测时间对比 | P1 |
| Claim 3 | 无（需要新实验） | Plan A 全矩阵：B0/B1-30/B1-50/B1-70/B2/PI × 5 gens × 3 seeds | P0（论文核心） |

### 目标 Venue

- **首选：EMNLP 2026 Main Conference**（deadline ~2026-06）
  - 理由：(1) 结合了 negative result（Claim 1-2）和 positive contribution（Claim 3），比纯 negative result 论文更有吸引力；(2) EMNLP 对 empirical findings + practical contributions 接受度高；(3) synthetic data / model collapse 是 2025-2026 热点话题
  - 风险：Claim 3 实验量大（~12 天 GPU），deadline 前能否完成取决于 GPU 可用性
- **备选：NeurIPS 2026**（deadline ~2026-05 末 或 ~2026-06）
  - 理由：更大的 venue，更适合 novel paradigm（控制论视角），但竞争更激烈
- **保底：EMNLP 2026 Findings**
  - 如果 Claim 3 实验结果不够强（PI 仅小幅优于 fixed-ratio），降级投 Findings

### 预期审稿人质疑 & 预备回应

- **Q1: 只在 Pythia-1B + wikitext-103 上验证，generalizability 如何？**
  - 回应：(a) Spectral Flattening 论文在不同模型（量化场景）独立观察到 eff_rank 上升 = collapse，支持现象的普遍性；(b) 计划扩展 Pythia-410M/2.8B 验证 scale robustness；(c) n-gram entropy 作为 model-agnostic 统计量，不依赖特定架构。
  - 兜底：如果只做了 1B，承认 limitation 但强调 Pythia-1B 是 collapse 研究的标准 testbed（Shumailov et al. 也用类似规模）。

- **Q2: eff_rank 反升的机制解释是否有因果证据，还是 post-hoc 叙事？**
  - 回应：(a) 提供逐 checkpoint 的 singular value 分布可视化，展示谱从"peaked"到"flat"的演化；(b) 与 Spectral Flattening 论文的理论分析交叉验证；(c) 设计对照实验：对 collapsed model 做 rank-constrained fine-tuning（限制 SV 谱不变），观察 collapse 行为是否改变——如果不变，则确认 eff_rank 与 collapse 无因果关系。
  - 兜底：作为 empirical finding 仍有价值，因果机制可留作 future work。

- **Q3: PI 控制器 vs 简单 threshold 策略（bang-bang），为什么需要 PI？**
  - 回应：(a) 实验矩阵包含 B2（threshold/bang-bang）作为 baseline，直接对比；(b) PI 的优势在于 smooth 调节——threshold 会在边界处频繁 switching（w 在 0.3 和 0.9 之间跳动），导致训练不稳定；(c) PI 的 integral 项能自动补偿 steady-state error（threshold 无此能力）。
  - 关键：如果实验显示 threshold 已经足够好，诚实报告——这本身也是一个有价值的发现（"simple baselines work"）。

- **Q4: N-gram entropy 已经被其他工作（Shi et al., Gambetta et al.）使用过，novelty 在哪？**
  - 回应：(a) 已有工作用 entropy 做 data selection/filtering（静态），我们首次将其作为 online feedback signal 驱动 mixing ratio 的闭环控制器（动态）；(b) 已有工作未系统对比 entropy vs spectral metrics 在 iterative collapse 检测中的优劣——我们提供了首个 head-to-head 对比；(c) 贡献不仅是"用 entropy"，而是"用 entropy + 控制器 = collapse-aware adaptive mixing"这一完整框架。

- **Q5: 3 代是否足以声称 "model collapse"？真实场景下可能数十代。**
  - 回应：(a) 3 代已足以实现完全 collapse（G2 unique_tokens=1），这与 Shumailov et al. 一致；(b) Plan A 实验扩展到 5 代以观察 PI 的长期稳定性；(c) 实际应用中关键是 early detection + intervention（在 collapse 早期干预），而非等到完全 collapse 后再修复——因此 3-5 代的观察窗口是合理的。

---

## 路径 B：seed=0 未复现 eff_rank 反升

### Core Insight（1-2 句）

Holdout spectral effective rank 在 model collapse 中的行为是 seed-dependent 的——seed=42 观察到反升，但 seed=0 未复现。这本身是一个 cautionary tale：spectral metrics 的不稳定性使其不适合作为 collapse 检测信号，同时暴露了小规模 collapse 研究中 seed sensitivity 被普遍忽视的问题。

### Story Arc（两个子选项）

#### B-1: Negative Result Paper

1. **问题**：Spectral effective rank 被广泛用于衡量 representation diversity（Jha & Reagen, EMNLP 2025），并被隐含假设可监测 model collapse。但其在 iterative collapse 场景下的表现从未被系统评估。
2. **测试**：在 Pythia-1B + wikitext-103 上运行 3 代纯 synthetic training，跨 2 个 seed 评估 holdout spectral effective rank 的 collapse 检测能力。
3. **发现 1（seed=42）**：eff_rank 在 complete collapse（unique_tokens=1）时反升 +0.96%，与 collapse 解耦。
4. **发现 2（seed=0）**：eff_rank 行为不同（[具体数据待填]），说明 eff_rank 对 collapse 的响应是 seed-sensitive 的。
5. **结论**：无论 eff_rank 反升还是 seed-dependent，都说明它不是 reliable 的 collapse 检测信号。N-gram entropy 在两个 seed 上都一致检测到 collapse（待验证），是更 robust 的替代。
6. **建议**：呼吁社区不要将 spectral rank metrics 作为 collapse proxy，并要求 collapse 研究报告 multi-seed 结果。

**叙事弱点（与 Path A 对比）：**
- 少了"反直觉的一致性发现"这一最锐利的 hook
- 变成了"方法不 work + 不 robust"的双重否定，论文吸引力下降
- Claim 3（PI 控制器）仍可保留，但与 negative result 部分的叙事联系变弱——"我们测了 spectral metrics 不行（且结果不一致），然后改用 entropy + 控制器"会让审稿人质疑动机的 post-hoc 性质

#### B-2: Archive

- **条件**：
  1. seed=0 中 eff_rank 行为既不反升也不显著下降（即噪声中无信号），**且**
  2. n-gram entropy 的 detection 在 seed=0 上与 seed=42 不一致（collapse 行为本身不 robust），**且**
  3. 团队判断 GPU 资源更适合投入其他项目
- **判断标准**：如果 collapse 行为本身在不同 seed 间差异巨大（不仅仅是 eff_rank 响应不同，而是 collapse 进程本身不同），说明实验设计有根本问题（20M tokens/gen 可能太少、Pythia-1B 不够大），此时 archive 比 patch 更高效
- **保留物**：(a) v7 全部数据和代码归档到 repo；(b) related_work_survey.md 和 plan_a_technical_design.md 可被未来项目复用；(c) ROADMAP.md 记录完整的决策链作为经验参考

### 需要的实验支撑（如果走 B-1）

| 实验 | 目的 | 优先级 |
|------|------|--------|
| seed=0 完整数据分析 | 确认 eff_rank 行为，对比 seed=42 | P0 |
| seed=7 第三组复现 | 将 seed-sensitivity 的论证从 N=2 提升到 N=3 | P1 |
| Pythia-410M seed=42 复现 | 排除 "model scale 导致" 的 confound | P1 |
| N-gram entropy multi-seed 一致性 | 验证 entropy 作为 robust 替代 | P0 |
| Plan A 实验（缩减版） | PI 控制器仍可作为 positive contribution（但优先级降低） | P2 |

**GPU 成本估算：** ~4-5 天（3 seeds × 3 gens + 可能的 410M 实验），显著低于 Path A 的 12 天。

### 目标 Venue（如果走 B-1）

- **首选：EMNLP 2026 Findings**
  - 理由：Findings 对 negative results 更友好；较低的 novelty bar 适合 "X doesn't work + here's why" 类论文
  - 风险：即使 Findings，纯 negative result 接受率也不确定
- **备选：NeurIPS 2026 Datasets & Benchmarks Track** 或 **COLM 2026**
  - 如果包装为 "benchmark for collapse detection metrics"，可投 D&B
- **备选：Workshop paper**（如 NeurIPS Workshop on Synthetic Data, ICML FM-Wild 等）
  - 风险最低，发表周期最快，适合"尽快出手、释放 GPU"的策略

---

## 路径选择决策树

```
seed=0 结果出来
    │
    ├── eff_rank 反升（与 seed=42 一致，变化方向相同）
    │   └── 走 Path A
    │       ├── Claim 1-2 confirmed → 立即启动 Plan A 实验
    │       └── 目标 EMNLP 2026 Main / NeurIPS 2026
    │
    ├── eff_rank 下降或不变（与 seed=42 方向不同）
    │   ├── n-gram entropy 仍一致检测 collapse
    │   │   └── 走 Path B-1（negative result paper）
    │   │       └── 目标 EMNLP 2026 Findings
    │   └── n-gram entropy 也不一致
    │       └── 走 Path B-2（archive）
    │
    └── collapse 本身未发生（seed=0 的模型未 collapse）
        └── 检查实验配置是否正确
            ├── 配置正确 → 走 Path B-2（collapse 不 robust = 实验设计有问题）
            └── 配置错误 → 修复后重跑
```
