---
round: 2
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T01:30:43.909109+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2（Fresh Review）

**论文**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
**目标 Venue**: CoRL 2026 (Deadline: 2026-05-29)
**审稿模式**: 圆桌会议，2 名 Reviewer，1 轮独立审稿 + 交叉回应
**日期**: 2026-05-19

---

## Summary

本文对两种 VLA 架构（SmolVLA/pixel-shuffle connector, 0.5B; OpenVLA/MLP projector, 7B）进行跨架构 closed-loop vision token pruning 评估。核心发现：pixel-shuffle connector 导致 cliff-edge failure（59.2% → 0% SR，k=0.95 仅移除 7/128 tokens 即崩溃），而 MLP projector 优雅退化（74.0% → 37.4%）。提出 attention entropy ratio 作为 compressibility 信号，并设计 cross-attention re-encoding 模块（Smart Compress）在 75% token 压缩下保持 61.6% SR。论文还指出 offline metrics 无法预测 closed-loop failure。

---

## Strengths

1. **研究问题重要且及时**：VLA token efficiency 是 real-time robotic control 核心瓶颈。Cliff-edge failure（59.2% → 0%, 即使 k=0.95）是此前未被报告的现象，对 VLA 系统设计者有直接警示价值。

2. **SmolVLA 消融设计系统**：7 种配置覆盖 scoring（learned ACIS vs random）、retention ratio（k∈{0.5,0.7,0.9,0.95}）、mechanism（zero-mask, true removal, ToMe）三轴。All-zero 结论说服力强——不是某个 pruning 方法的失败，而是架构层面的。

3. **控制实验设计合理**：Extended training control（45.0% vs 44.8%, p > 0.9）有效排除额外训练时间的混淆；official checkpoint 验证（59.2% → 0%）排除 undertrained weights 解释。

4. **写作质量高**：叙事线清晰连贯（问题→发现→解释→方案），无明显 AI 写作痕迹，专有名词定义到位，段落过渡自然。格式合规（8 页正文，匿名化正确，Limitations section 存在）。

5. **Closed-loop vs offline metric disconnect 有价值**：Action error 分析（111.5% relative error, gripper inversion）提供了 mechanistic 理解。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [Consensus: R1+R2]** Scale confound 未解决，核心因果 claim 过强

SmolVLA (0.5B) vs OpenVLA (7B) 在 connector 和 scale 上同时不同（14x scale 差异）。论文 4 条 disentangling 论据评估：(1) official checkpoint cliff-edge 排除 training quality 但不排除 scale；(2) k=0.95 collapse 是最有力论据——小扰动导致灾难性失败指向架构脆弱性；(3) entropy ratio 存在循环论证风险（更大模型可能天然学到更 selective attention）；(4) pixel-shuffle mechanistic account 有说服力但不完整。

**核心问题**：Abstract 和 Conclusion 中 "compressibility is attributable to the vision connector design" 是因果断言，但证据只支持更弱的相关性。Matched-scale 实验是解决此问题的唯一可靠方式。

**建议**：将 "attributable to" 改为 "associated with" 或 "primarily shaped by"；在 Abstract/Conclusion 中明确标注 scale confound 未排除。

**MF-2 [Consensus: R1+R2]** Multi-seed 仅 2 seeds，不符合 CoRL 标准

2 个 seed（42, 43）无法计算可靠方差估计（自由度=1）。"half-range" 不是标准统计量度。M=96 的 5.6pp 差异（52.6% vs 58.2%）是所有配置中最大的，Table 8 caption 却声称 "All configurations show low variance across seeds"，属 selective reporting。CoRL 标准要求至少 3 seeds（通常 5）。

**建议**：增加至少 1 个 seed（total ≥ 3）；报告 mean ± std；弱化 "robustness" 措辞。

**MF-3 [Consensus: R1+R2]** Baseline 复现严重偏低（44.8% vs 官方 87.3%），Smart Compress 在 official checkpoint 上未验证

42.5pp 的差距仅归因于 "smaller batch"，具体 batch size 值未给出。Smart Compress 全部实验建立在偏低 baseline 上——在 underfitting 模型上的 pruning sensitivity 可能与正常训练模型不同。M=128 passthrough (59.8%) ≈ official checkpoint (59.2%) 暗示 cross-attention module 可能只是替代 large-batch training 的效果（adapter 效应）。

**建议**：在 official checkpoint 上运行 Smart Compress；报告具体 batch size 和训练配置差异；讨论 baseline quality 对结论的影响。

**MF-4 [R2 Must-Fix, R1 Partially Agrees]** 遗漏多篇直接竞争的 VLA token efficiency 工作

以下 2025-2026 工作完全未被引用（R1 验证存在性后确认）：
- **Compressor-VLA** (arXiv 2511.18950) — 直接竞争：cross-attention VLA token compression on LIBERO，STC 模块与 Smart Compress 高度相似
- **SpecPrune-VLA** (arXiv 2509.05614) — Action-aware VLA token pruning on LIBERO + real robot
- **LightVLA** (arXiv 2509.12594) — Differentiable VLA token pruning, ICRA 2026
- **"See What Matters"** (ICML 2026) — Grid-based VLA compression（concurrent work）
- **"Don't Run with Scissors"** (arXiv 2510.08464) — VLA pruning fragility（注：R1 指出这是 weight pruning 非 token pruning，但主题 "pruning breaks VLA" 相关）

R1 特别指出：Compressor-VLA 在 LIBERO 上用类似 cross-attention 达到 97.1% SR，使 Smart Compress 作为独立方法的增量存疑。遗漏不影响本文实验内部有效性，但严重影响 novelty positioning。

**建议**：全面补充引用；与 Compressor-VLA 做定性或定量对比；重新评估 positioning。

**MF-5 [R2 Must-Fix, R1 Partially Agrees]** Smart Compress 方法新颖性不足，需重新定位

Cross-attention pooling with learned queries 是 BLIP-2 (2023) 已确立的设计。论文 Related Work 虽提到 Q-Former/Perceiver 但未讨论与 Smart Compress 的具体技术差异。

**Reviewer 共识**：Smart Compress 作为架构本身不 novel，但作为 diagnostic tool 验证 "re-encoding > deletion" 假说有价值（M=128 passthrough control 是 Q-Former/Compressor-VLA 论文未做的实验设计）。论文需要选择定位：要么重新定位为 mechanistic validation，要么与 Compressor-VLA 做正式 head-to-head 比较。

**建议**：将 Smart Compress 贡献重新定位为 diagnostic experiment（验证 re-encoding hypothesis），而非独立方法贡献。

### Should-Fix（影响评分但不一票否决）

**SF-1 [Consensus]** 仅 LIBERO simulation 评估，CoRL 期望 real-robot 或多 benchmark。LIBERO-Object 的 10 个 tabletop pick-and-place 任务复杂度有限。Cross-suite 泛化（Object → Spatial/Goal）仍在同一 benchmark 家族内。

**SF-2 [Consensus]** OpenVLA 实验不对称——SmolVLA 测试 learned + random scoring，OpenVLA 仅 random。这使跨架构对比不完全公平。建议讨论为什么不影响核心结论或引用 VLA-IAP 结果作为间接证据。

**SF-3 [Consensus]** M=96 performance dip（52.6%, multi-seed mean 55.4%）未解释。Table 2 caption 通过排除 M=96 维持 "flat" 叙事，属 selective reporting。需给出假说或额外分析。

**SF-4 [Consensus]** "performance-neutral deployment benefit" 措辞不准确。实际 latency 改善仅 1.06x（6%），且 SR 变化是提升（44.8% → 61.6%）。跨任务时 LIBERO-Goal 有 6.6pp 下降。建议限定为 in-distribution 场景并准确描述收益和成本。

**SF-5 [Consensus]** Offline metric disconnect 论证不完整。Table 7 展示 3.4x action error 本身不是 "misleadingly positive" 信号。需展示某个常用 offline metric（如 per-step action loss distribution）看起来正常但 closed-loop 崩溃的对比。

**SF-6 [R1]** 引用数量偏少（26 条 vs CoRL 标准 35-50+）。补充遗漏工作后应接近 32-35 条。

**SF-7 [R1]** Smart Compress 训练细节不完整——Appendix 缺 learning rate, optimizer, batch size, weight decay, warmup schedule, GPU 型号/数量。影响 reproducibility。

### Minor Issues

1. Table 1 小数精度不统一（SR 用整数 % 但 CI 用两位小数）
2. Appendix D 采样量不对等（SmolVLA 2400 vs OpenVLA 250 frames）
3. 贡献列表引用 EfficientVLA 支撑 Contribution 1——R1 认为合理（corroborating evidence），R2 认为应标明 "supported by concurrent findings"
4. bib 条目：black2024pi0 未匹配到，ghosh2024octo first author 标注不一致
5. 无 code availability 声明

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
1. Scale confound 是核心方法论弱点，因果 claim 需降级
2. 2 seeds 不符合 CoRL 标准，需增加
3. Baseline 偏低对 Smart Compress 可信度的影响需解决
4. Compressor-VLA 等 4+ 篇直接相关工作必须引用
5. "performance-neutral deployment benefit" 措辞不准确
6. LIBERO-only 评估不足
7. M=96 dip 属 selective reporting
8. Smart Compress 跨任务 generalization 下降被淡化

---

## Reviewer Divergence

**"First cross-architecture closed-loop evaluation" claim [R2: Must-Fix → R1: REBUT]**

R2 认为 SpecPrune-VLA/LightVLA/"See What Matters" 等工作可能已做类似评估，"first" claim 不准确。R1 逐一验证后认为无其他工作做了 connector-type 对比分析，claim 在精确限定下仍成立。R1 建议更精确的表述："first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control"。

**Director 判断**：R1 的验证更细致，在补充所有遗漏引用并重新验证后，更精确限定的 "first" claim 应可成立。建议采纳 R1 的限定方案。

**Smart Compress 新颖性 [R2: Must-Fix → R1: Partially Agree]**

R2 认为 Smart Compress 与 Q-Former 机制几乎相同，新颖性不足。R1 认为架构不 novel 但作为 diagnostic tool（M=128 passthrough 验证 re-encoding hypothesis）有独特实验价值。

**Director 判断**：两位观点互补。Smart Compress 不应定位为独立方法贡献，而应定位为验证 "re-encoding > deletion" 假说的 diagnostic experiment。这一重新定位可同时缓解两位 Reviewer 的担忧。

---

## Questions to Authors

1. **[R1]** Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)——cross-attention module 的 22.2M 参数是否本质上是 adapter，增益来自额外参数容量而非 re-encoding？
2. **[R1]** ACIS scorer 的 Stage-1-only 训练是否导致 scorer 质量不足？如果 scorer 失败，"scoring-independent" 结论的信息量有限。
3. **[R1]** OpenVLA degradation curve 近似线性——是否有理论预期？
4. **[R2]** 如何 position Smart Compress 相对于 Compressor-VLA（LIBERO 上 97.1% SR with cross-attention compression）？
5. **[共同]** 是否可在 official checkpoint 上运行 Smart Compress 以验证增益在强 baseline 下是否成立？
6. **[共同]** 是否考虑过 matched-scale 控制实验（同 backbone 不同 connector）？

---

## Missing References

**必须引用**（R1+R2 共识）：
1. Compressor-VLA (arXiv 2511.18950, Nov 2025) — 直接竞争，cross-attention VLA token compression on LIBERO
2. SpecPrune-VLA (arXiv 2509.05614, Sep 2025) — Action-aware VLA token pruning on LIBERO + real robot
3. LightVLA (arXiv 2509.12594, Sep 2025, ICRA 2026) — Differentiable VLA token pruning
4. "See What Matters" (ICML 2026) — Grid-based VLA compression（concurrent work）

**建议引用**：
5. "Don't Run with Scissors" (arXiv 2510.08464, Oct 2025) — VLA weight pruning fragility（相关但非直接竞争）
6. SparseVLM (arXiv 2410.04417, ICML 2025) — Training-free VLM token sparsification
7. SparseVILA (arXiv 2510.17777, ICCV 2025) — Decoupled visual sparsity
8. RoboFlamingo — Cross-attention vision connector VLA（connector taxonomy 补充）

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回**（requested at 2026-05-19T01:12:32, pending）

---

## Overall Assessment

**Rating: Weak Reject (4/10)**
**Confidence: 4/5 (High)**

| 维度 | 分数 | 理由 |
|------|------|------|
| Originality | 3/5 | Cliff-edge failure 发现有价值但 pixel-shuffle 的脆弱性从架构角度看 partially expected；Smart Compress 机制不 novel |
| Quality | 2.5/5 | SmolVLA 消融严谨，但 scale confound 未解决、2-seed 统计不足、baseline 偏低 42.5pp 构成可信度担忧 |
| Clarity | 4/5 | 写作清晰，结构好，无 AI 痕迹，但部分 claim 过强 |
| Significance | 3/5 | 对 practitioner 有参考价值（connector 选择需考虑压缩性），但 Smart Compress 实用价值有限（1.06x speedup）|
| Relevance | 4/5 | VLA efficiency 是 CoRL 核心话题 |
| Limitations | 3/5 | 诚实报告 LIBERO-only 和 scale confound，但未覆盖 baseline quality 问题和遗漏工作的影响 |

**一句话总结**：论文发现了有价值的现象（pixel-shuffle connector 的 cliff-edge failure），SmolVLA 侧消融设计系统充分，但五个核心问题——因果 claim 过强（scale confound）、2-seed 统计不足、baseline 偏低且 Smart Compress 未在强 baseline 上验证、遗漏 4+ 篇直接竞争工作（特别是 Compressor-VLA）、Smart Compress 需重新定位——共同将论文拉低至 accept 线以下。

**提升至 accept 的路径**（按优先级）：
1. 补充 Compressor-VLA 等遗漏引用，重新 position Smart Compress 为 diagnostic experiment
2. 弱化因果语言（attributable to → associated with）
3. 增加至少 1 个 seed（total ≥ 3），报告 mean ± std
4. 在 official checkpoint 上运行 Smart Compress
5. 补充训练细节（lr, optimizer, batch size 等）

---

## Detailed Comments

### 对每个贡献 claim 的评估

**Contribution 1（Architecture-dependent compressibility）**：核心发现有价值，但因果 claim 超出证据。k=0.95 collapse 是最有力的架构脆弱性证据。需降级因果语言并更充分承认 scale confound。

**Contribution 2（Mechanistic explanation via entropy ratio）**：N=2 architectures 的观察不足以建立预测性 signal。"preliminary diagnostic signal" 的措辞合理但需进一步弱化预测性含义。Entropy ratio 可能部分由 scale 驱动，存在循环论证风险。

**Contribution 3（Cross-attention re-encoding）**：M=128 passthrough control 是有价值的实验设计（证明增益来自 re-encoding），但 (a) 机制与 Q-Former 相同，(b) Compressor-VLA 已在同 benchmark 上用类似方法取得更好结果，(c) 仅在偏低 baseline 上验证。需重新定位为 diagnostic experiment 而非独立方法。

**Contribution 4（Offline metric disconnect）**：论证方向正确但数据支撑不完整。需展示 "offline metric 看起来正常但 closed-loop 崩溃" 的具体对比。

### 格式合规检查

- 正文约 7 页（8 页限制内）✓
- 匿名化正确 ✓
- Limitations section 存在且实质性 ✓
- corl_2026.sty 模板 ✓
- 行号启用（submission 模式）✓
- 引用数量偏少（26 条，建议 35+）⚠️
- 训练细节不完整（影响 reproducibility）⚠️
- 无 code availability 声明 ⚠️