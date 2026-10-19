---
round: 1
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T01:05:47.491292+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告：Sample, Select, Correct: Inference-Time Action Refinement for Frozen VLAs

**Venue**: CoRL 2026 Main Conference | **Deadline**: 2026-05-29
**审稿模式**: 3 Reviewer 圆桌 + 交叉回应 | **轮次**: Round 1（已收敛）

---

## Summary

本文提出 sample-select-correct pipeline 用于 frozen flow-matching VLA 的推理时动作修正：抽取 K=10 个 action samples，L2 argmin 选择最接近均值的 candidate，再用 ~327K 参数的 MLP (CRM) 预测有界残差修正。在 LIBERO-Object 上报告 17.6±2.6% vs VLA-only 11.6±1.1%。论文提供了 component decomposition（发现 selection 单独无效、correction 是主要驱动力）、conditioning ablation（conformal features 反而有害）和 applicability boundary 分析（tokenized VLAs 不适用）。LIBERO-Spatial 上无效果。

---

## Strengths

**S1. 系统性的 component decomposition** [R1, R2 共识]
拆解 random selection、argmin selection、CRM correction 的各自贡献，发现 selection alone 不 work 而 correction 是关键驱动力。这种系统性消融在 VLA 文献中较少见。

**S2. 诚实的负面结果报告** [R1, R2, R3 共识]
LIBERO-Spatial null result、conformal features 失效、absolute performance 仅 17.6%、个别 seed 上修正反而降低性能（seed 43）均被坦诚报告。Limitations 节列出 7 项限制，不回避核心弱点。

**S3. 写作质量干净，AI 痕迹极少** [R3 确认]
全文 em-dash 零处（正文）、Furthermore/Moreover/Additionally 零处、黑名单词汇零处。仅 4 处轻微 -ing 分词结尾。在当前投稿中属于写作风格最干净的论文之一。

**S4. Applicability boundary 分析** [R1 确认]
OpenVLA (tokenized) vs SmolVLA (flow-matching) 的 action diversity 对比（Figure 4, per-DOF variance < 10^{-30}）有效建立了方法的架构适用边界。

**S5. 轻量实用设计** [R3 确认]
~327K 参数、~0.3ms 推理开销，base VLA 完全不修改，作为 post-hoc module attach 的设计在部署场景下有实际意义。

---

## Weaknesses

### Critical（影响接收决定）

**C1. 统计方法根本性错误** [R1 提出, R2 R3 一致同意]
论文将跨 seed 的 episodes pooled 后做 Fisher's exact test（experiments.tex L51），但同一 seed 下的 episodes 共享 CRM 权重和随机状态，不满足独立性假设。p=0.0042 是伪显著（pseudo-replication）。论文确实提供了部分缓解证据——"All seven obs_only seeds exceed the VLA-only mean"（等价于 sign test, p≈0.008 单侧），但未正式报告此检验。核心统计结论的可信度受到严重影响。
- 位置：Abstract L4, experiments.tex L49-52, L86

**C2. 核心 claim 与 K-scaling 数据内部矛盾** [R1 提出, R2 R3 一致同意]
Abstract 和正文反复声称 "the entire benefit derives from learned correction"（Abstract L5, experiments.tex L94, discussion.tex L16），但 K=1 CRM 为 10.3%（3 seeds），低于 VLA-only 的 11.6%——correction alone 反而有害。更严重的是，Appendix L16 报告 K=1 为 10.3%，L18 却将其描述为 "at the VLA-only level (11.6%)"，同一段落内数据描述直接矛盾（R3 发现）。真实结论应为 "multi-sample selection 是 correction 有效工作的前提条件，两者的协同效应是 driver"。

**C3. 各方法 seed 数不一致且无解释** [R1 提出, R2 R3 一致同意]
Table 1 中 obs_only 7 seeds、VLA-only 5 seeds、Argmin 6 seeds、Random 仅 3 seeds。论文未在任何地方解释原因。最关键的 random vs argmin 比较仅基于 3 seeds，统计功效极低。不解释的不一致 seed 数引起 selection bias 嫌疑。

**C4. 新颖性不足** [R2 提出, R3 从 framing 角度同意]
Pipeline 的三个组件中，selection 被自己的实验否定，correction 是标准的 supervised residual learning (Silver et al., 2018) + L2 clipping，observation conditioning 是直觉性设计。与最接近的 A2C2 相比，剩余的真实技术差异（magnitude clipping + obs conditioning）不足以构成单独论文的方法贡献。

**C5. 标题与结论矛盾** [R2 提出, R3 强烈同意]
"Sample, Select, Correct" 暗示三步均有独立贡献，但实验证明 sample 和 select 单独无效（random K=10 ≈ VLA-only, argmin ≈ random）。标题设置了错误的读者预期。

**C6. 正文超 8 页限制** [R3 提出, R2 同意]
正文含 Discussion + Limitations + Conclusion 共 9 页，超出 CoRL 2026 规定的 8 页限制 1 页。格式违规可能导致 desk reject。

**C7. 缺失 AI Disclosure Statement** [R3 提出, R2 同意]
CoRL 2026 要求作者简要说明 generative AI 工具使用方式，论文中完全缺失。

### Major（影响评分但非一票否决）

**M1. 实验范围过窄** [R2 提出, R1 R3 部分同意]
全部实验仅在 LIBERO (仿真) + SmolVLA (450M) 上进行。未测试其他 VLA backbone（π₀, Octo）、其他 benchmark（RLBench, MetaWorld），也无 real-robot 验证。R3 部分反驳：CoRL 不硬性要求 real-robot，但三人均认为范围过窄。

**M2. LIBERO-Spatial null result 仅 1 seed** [R1 提出, R2 R3 同意]
Table 1 Spatial 列全部为 seed 42 单次结果。鉴于 Object 上 per-seed std 达 2.6pp，1 个 seed 不足以支撑 "correction does not help for spatial reasoning" 的结论（论文 Contribution 3 的重要支撑）。

**M3. 缺少与 A2C2 的实际实验对比** [R1 提出, R2 R3 同意]
论文将 A2C2 定位为 "closest concurrent work" 并列出三点差异，但对比仅停留在文字层面。Limitations 节也未说明为何缺少定量对比。

**M4. 24 条 orphan bib entries + 引用不足** [R1 R2 R3 独立标记]
Bib 51 条中仅 25 条被引用。Diffusion Policy (Chi 2023)、RT-2 (Brohan 2023)、Octo (Ghosh 2024)、Conformalized Teleoperation (Zhao 2024) 等重要工作在 bib 中但未引用。Gauss1857/Lagrange1788 模板残留未清理。

**M5. Magnitude 分析某些 ε 仅 1 seed** [R1 提出, R3 同意]
Figure 2 caption 写 "±1 std across seeds (n=1-7 per point)"，n=1 时 error bars 无意义，造成视觉误导。

**M6. CRM 训练覆盖全部评估 tasks，无 cross-task 泛化验证** [R1 提出, R2 同意]
CRM 在全部 20 LIBERO tasks 的 demo 上训练并在同一 20 tasks 上评估，无法判断是 task-agnostic 修正能力还是 task-specific 记忆。

**M7. 论文 method paper vs analysis paper 定位不清** [R2 提出, R3 强烈同意]
Abstract/Method 以 method paper 口吻（"We propose..."），但核心价值在 component decomposition 和 negative results。身份混淆使审稿人难以评价——method paper 标准下 novelty 不够，analysis paper 标准下 scope 不够。

**M8. Related Work 缺少 Conformal Prediction 专门讨论** [R2 提出]
论文核心贡献之一是 conformal features 失效，但 Related Work 缺少 CP in robotics 的系统 positioning。

### Minor

**m1.** "safety factor" 用语在机器人学语境中引起歧义 [R1, R3] — 建议改为 "critical design factor"
**m2.** L2 argmin 选择缺乏理论动机 [R1, R2]
**m3.** CRM 架构无 ablation [R1, R2]
**m4.** DOF 首次使用未展开为 Degrees of Freedom [R3, R2 同意降级为 minor]
**m5.** 4 处 -ing 分词短语结尾 [R3]
**m6.** Table 2 最优未加粗，与 Table 1 不一致 [R3]
**m7.** Figure 1 信息密度偏低，在超页数时占用空间大 [R3]
**m8.** Per-task analysis 仅 seed 42 [R1]
**m9.** LLM test-time compute scaling 类比不恰当 [R2, R3] — d=6 连续 vs 高维离散差异太大

---

## Reviewer Consensus [AGREE]

以下关键问题三位 Reviewer 达成完全共识：

1. **Fisher's exact test 独立性违反**（C1）— 统计方法需修正，但 sign test (7/7) 提供替代方向性证据
2. **核心 claim "entire benefit from correction" 与 K=1 数据矛盾**（C2）— 需全面修正 framing
3. **Seed 数不一致无解释**（C3）— 必须解释或统一
4. **缺 A2C2 实验对比**（M3）— 应复现或在 Limitations 明确解释
5. **24 orphan bib + 关键引用缺失**（M4）— 需清理并补充引用
6. **标题与结论矛盾**（C5）— 需修改标题

## Reviewer Divergence [REBUT]

1. **Real-robot 实验的必要性**（R2-N3）：R2 视为 Critical，R3 部分反驳认为 CoRL 不硬性要求。**Director 判断：降为 Major，但实验范围窄的综合问题仍然严重。**
2. **DOF/MLP/MSE 缩写定义**（R3-W4）：R3 标为 Major，R2 反驳认为是 CoRL 受众的标准术语。**Director 判断：降为 Minor，但首次使用展开 DOF 为佳。**
3. **"safety factor" 用语严重度**（R1-W8）：R1 标 Minor，R2 认为更接近用词歧义而非错误。**Director 判断：Minor，改为 "design factor" 即可。**

---

## Questions（需要作者澄清）

Q1. 各方法 seed 数为何不同？是否有 seeds 被丢弃？如果是计算资源限制，请明确说明。
Q2. K=1 CRM (10.3%) 低于 VLA-only (11.6%)，如何维持 "entire benefit from correction" 的 claim？Appendix 中 10.3% 被描述为 "at the VLA-only level (11.6%)" 是文字错误还是有其他解释？
Q3. 是否做过 seed-level 统计检验（如 sign test, Wilcoxon）？如果做了，p-value 多少？
Q4. 为何不复现 A2C2 做直接对比？代码是否不可用？
Q5. CRM 在 LIBERO-Spatial 训练数据上的 offline MSE 如何？是否有 leave-task-out 的泛化测试？
Q6. LIBERO-Spatial 35% vs 34% 的差异是否在 noise 范围内？能否提供多 seed 结果？
Q7. 论文的定位是 method paper 还是 analysis paper？这影响贡献评估标准。

---

## Missing References

### 已在 bib 中但未引用（必须纳入 Related Work）：
1. **Chi et al., 2023 (Diffusion Policy)** — action diffusion 基础工作
2. **Brohan et al., 2023 (RT-2)** — VLA 标志性工作
3. **Ghosh et al., 2024 (Octo)** — 开源 generalist robot policy
4. **Zhao et al., 2024 (Conformalized Teleoperation)** — CP in robotic action spaces
5. **Zhou et al., 2025 (ACP-CBF)** — conformal prediction + safety in robotics
6. **Wang et al., 2025 (CPLoop)** — CP in trajectory optimization
7. **Johannink et al., 2019** — residual RL for robot control

### bib 中不存在但建议补充：
8. **ACT (Zhao et al., 2023)** — action chunking 基础工作
9. 2025-2026 最新 VLA 工作（HPT, CrossFormer 等 generalist policies）

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置未开启 paperreview_ai）。

---

## Overall Assessment

**Overall Score: Weak Reject (4/10)**
**Confidence: High (4/5)**

| Reviewer | Round 1 | 交叉后 | 角色 |
|----------|---------|--------|------|
| R1 | 4/10 | 4/10 | 方法/实验 |
| R2 | 4/10 | 4/10 (下调趋势) | 新颖性/定位 |
| R3 | 3/5 (~6/10) | 2.5/5 (~5/10) | 写作/格式 |

**综合评价**：

论文方向有意义（inference-time refinement for frozen VLAs），消融设计系统，写作干净直接，负面结果报告诚实——这些是值得肯定的优势。

但存在多层面的根本性问题使其未达到 CoRL 2026 接收标准：

1. **可信度层**：统计方法有根本缺陷（Fisher independence violation），核心 claim 与 K=1 数据矛盾且 Appendix 内部数据描述不一致，seed 数不一致无解释。审稿人无法信任论文报告的主要结论。

2. **贡献层**：技术新颖性不足（标准 MLP + L2 clipping），核心分析发现（selection 无用）在低维连续空间中可预期，标题与结论矛盾，论文定位在 method 和 analysis 之间摇摆。

3. **范围层**：单一 VLA backbone + 单一 benchmark family + 纯仿真 + Spatial 上无效。17.6% 绝对成功率远未达部署水平。

4. **合规层**：正文超 8 页限制（可能 desk reject），缺 AI disclosure，bib 残留未清理。

**最核心的修改优先级**：
1. 修正统计方法 + 统一 seed 数 → 恢复结果可信度
2. 修正 "correction is sole driver" framing → 消除内部矛盾
3. 压缩至 8 页 + 添加 AI disclosure → 满足格式合规
4. 在至少一个额外 VLA backbone 上验证 → 扩展实验范围
5. 补充 A2C2 对比（或明确解释为何缺失）→ 建立相对基准

论文最有价值的部分是诚实的 component decomposition 和 negative results（conformal features 失效、applicability boundary）。如果重新定位为 analysis paper 并大幅扩展实验范围（多 VLA、多 benchmark），有潜力成为有价值的贡献。当前版本作为 method paper 投 CoRL 顶会，贡献增量和实验范围均不足。

---

## Detailed Comments（逐节）

### Abstract
- p=0.0042 基于有缺陷的 Fisher test，需替换为有效统计量
- "directed residual correction is the sole meaningful driver" 与 K=1 数据矛盾，需修正
- 227 词结构完整，信息密度合理

### Introduction
- 5 段叙事结构清晰，Contribution 列表每条有对应支撑
- Contribution 1 的 "entire benefit from correction" phrasing 需修正
- Contribution 2 的 "critical safety factor" 用语有歧义
- 与 LLM test-time compute 的对比可简化（低维连续 vs 高维离散差异太大，类比深度不足）

### Related Work
- 三小节（VLA Robustness, Residual Policy Learning, Inference-Time Compute Scaling）组织合理
- 缺少 Conformal Prediction for Robotics 专门小节
- A2C2 的三点差异讨论充分但缺乏实验支撑
- 引用密度偏低（25 条 cited），关键工作（Diffusion Policy, RT-2, Octo）遗漏

### Method
- 形式化完整（Eq. 1-3），复现性好
- L2 argmin 选择缺乏理论动机
- CRM 架构选择无 ablation 支撑
- Figure 1 信息密度偏低，在超页数时尤其浪费空间

### Experiments
- 多处内容与 Method 重复（CRM variants 描述），可压缩
- 统计协议段落报告了不一致 seed 数但未解释
- Pipeline decomposition 结论有价值但 claim 需修正
- Spatial 结论基于单 seed，不充分
- Figure 2 中 n=1 的点不应展示 error bars

### Discussion
- "Selection vs correction" 段落与 Introduction/Experiments 有重叠，在超页数时应压缩
- "When does action-level correction help?" 分析合理但可更简练
- 论文在 method/analysis 定位间摇摆

### Limitations
- 7 条坦诚全面
- 遗漏：缺少与外部 baseline（A2C2 等）的实验对比
- 遗漏：Spatial null result 仅 1 seed 的统计局限

### Appendix
- K-scaling 分析有价值（K=5 captures ~88% of benefit）
- L16 报告 K=1 为 10.3%，L18 将其描述为 "at the VLA-only level (11.6%)" — 内部数据矛盾
- Applicability boundary (Figure 4) 有说服力
- Per-task analysis 仅 seed 42，代表性有限

### References
- 24 条 orphan entries（含模板残留 Gauss1857/Lagrange1788）
- 需清理并将关键工作纳入正文讨论