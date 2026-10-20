# Writing Readiness Assessment
> 评估日期: 2026-05-14 | 截稿: 2026-05-25 (剩余 11 天)

## 数据资产盘点

| 数据 | 状态 | 说明 |
|------|------|------|
| v6 importance ×4 (s015/s020/s025/s030) | ✅ 完成 | bootstrap CI p=0.0000, gradient 11-42× |
| v5 random ×4 (s015/s020/s025/s030) | ✅ 完成 | flat gradient ~1×, 50 problems each |
| v6 random ×4 (s015/s020/s025/s030) | 🔄 运行中 | 预计数小时完成 |
| Qwen cross-model replication | ❌ 被 kill | 速度问题未解决 (37-75min/题 vs DeepSeek 2min/题) |
| 文献地图 | ✅ 30+ 条目 | 3 名独立 Worker 确认 gap |
| 机制解释 | ✅ 完成 | Entropy-Discrimination Collapse |
| Crossover 现象 | ✅ 有数据 | s=0.25 high phase importance 优于 random |

## 可立即开写的章节

### 1. Related Work
- **理由**: literature_map.yaml 有 30+ 条目，分类完整（direct-competitor, method-component, background, evaluation）
- **数据来源**: literature_map.yaml + 3 Worker 文献空白确认
- **内容**: (a) KV cache compression 单轴方法 (b) compound compression interaction (c) phase-dependent behavior in LLMs (d) 定位 gap: 无人研究 phase-dependent strategy crossover in compound sparsity

### 2. Method / Problem Formulation
- **理由**: 实验框架已固定，不依赖任何在跑实验
- **数据来源**: artifacts 中的代码 (interaction_index.py, phase_segmentation.py, compound_forward.py)
- **内容**: (a) Interaction Index 形式化定义 (b) Phase segmentation 方案 (c) Compound sparsity framework (head pruning × token eviction) (d) importance-based vs random masking protocol

### 3. Experimental Setup
- **理由**: 所有实验配置已确定
- **数据来源**: 实验注册表 + 代码
- **内容**: (a) 模型: DeepSeek-R1-Distill-Qwen-7B (b) 数据: MATH-500 (c) Sparsity levels: 0.15/0.20/0.25/0.30 (d) Phase 划分: high/mid/low (e) Bootstrap CI: B=10000 (f) 硬件: 4× RTX 6000 Pro 96G

### 4. Introduction (主体部分)
- **理由**: 核心 story arc 已明确——phase-modulated compound interaction 是 strategy-dependent 的
- **数据来源**: memory.md (framing 指导 + D015 GO 依据)
- **内容**: (a) Compound sparsity 是实际部署的必然趋势 (b) 已有工作假设 compound = always bad (SparK) (c) 我们发现 severity 是 phase-modulated 且 strategy-dependent (d) Crossover: importance 在某些 phase 反而比 random 差 (e) 机制: Entropy-Discrimination Collapse
- **注意**: 具体数字可先用 placeholder，最终对齐 results

## 可写骨架的章节

### 5. Results
- **已有**: v6 importance 全部数据 + v5 random baseline 全部数据，足以支撑核心 claim
- **还缺**: (a) v6 random 结果 (运行中，数小时内) — 用于 v6 同代码对比，但 v5 random 已可支撑论证 (b) Cross-model (Qwen) 数据 — 增强 generalizability
- **策略**: 用 v6 importance + v5 random 先写主表和主要分析，v6 random 到后补入 robustness check

### 6. Analysis / Discussion
- **已有**: (a) Entropy-Discrimination Collapse 机制解释 (b) Crossover 现象 (s=0.25) (c) Sub-exponential 增长特征
- **还缺**: (a) Cross-model 是否复现 crossover (b) v6 random 是否改变 gradient ratio 的数值（不太可能改变结论方向）
- **策略**: 先写机制分析和 implications 部分，cross-model paragraph 留空

### 7. Abstract / Conclusion
- **已有**: 核心 claim 和数字
- **策略**: Results 成型后最后写，确保数字一致

## 必须等实验的章节

### Cross-model Generalization 段落 (Results §4.3 或 §5)
- **等什么**: Qwen2.5-7B-Instruct importance + random 实验
- **阻塞**: 速度问题 (37-75min/题)，根因未确认 (output_attentions 二次方开销 / 生成 token 过多)
- **预计**: 即使修复，完整 4-sparsity × 2-strategy 需 ~2-3 天
- **风险**: 如果 11 天内无法完成，论文可能只有单模型结果

## 写作优先级建议

| 优先级 | 章节 | 预估工时 | 理由 |
|--------|------|----------|------|
| P0 | Method + Experimental Setup | 1 天 | 纯技术写作，无数据依赖，是其他章节的基础 |
| P1 | Related Work | 1 天 | 文献已齐，定位 gap 是论文 novelty 的关键论证 |
| P2 | Results (主表 + 核心分析) | 1.5 天 | v6 importance + v5 random 数据已足够写核心 claim |
| P3 | Introduction | 1 天 | 需要 Results 初稿的 framing 反馈 |
| P4 | Analysis / Discussion | 1 天 | 机制解释已有，但需 Results 定稿后校准措辞 |
| P5 | Abstract + Conclusion | 0.5 天 | 最后写 |
| P6 | Cross-model results (如果来得及) | 0.5 天 | 取决于 Qwen 速度问题修复进度 |

总写作工时: ~6-7 天（含迭代），剩余 11 天理论上可行。

## 关键风险

1. **Cross-model replication 可能来不及**: Qwen 速度问题未解决，最坏情况只有单模型 (DeepSeek) 结果。EMNLP reviewer 可能要求 generalizability evidence → 准备 limitation 段落 + rebuttal 策略
2. **v6 random 如果结果异常**: 虽然 v5 random 已确认 flat gradient，但 v6 代码路径不同 (per_problem_ii)。如果 v6 random 出现非平坦 pattern，需重新审视 claim → 概率低但影响大
3. **无 paper_framing.md**: Director 的 framing 指导散落在 memory.md ("emergent phase-strategy interaction"，非 "importance metric limitation")，建议整理成正式 framing 文档再开写 Introduction
4. **图表制作时间**: 需要 phase gradient 可视化、crossover 图、主结果表 → 至少 1 天额外工作
5. **单模型 + 单数据集**: 即使 Qwen 来不及，MATH-500 是唯一 benchmark → 考虑是否能快速加一个 reasoning benchmark (如 GSM8K) 增强说服力