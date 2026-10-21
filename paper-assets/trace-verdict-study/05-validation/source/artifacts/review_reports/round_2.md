---
round: 2
review_mode: 
overall_score: 3.0
timestamp: 2026-05-18T20:05:55.694659+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 (Continue Mode)

**论文**: Exception Events Are All You Need: Component Ablation for Trace-Based Verdict Prediction
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿编排**: 2 Reviewers（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + 完整性 + Related Work）
**轮次**: Round 2 (Continue Mode)，1 轮收敛（交叉回应 16 AGREE / 1 REBUT）

---

## Summary

本文对 verdict prediction 中 execution trace 的各组件进行系统消融，扩展至四模型（Qwen-7B、Qwen-1.5B、CodeLlama-13B、DeepSeek-6.7B）三架构家族 1.5B-13B 参数范围。核心发现：exception events 单独在所有四模型上达到 ≥99.33% 准确率。新增 format-marker ablation (nomarker condition) 证明 ~91% 的 exception 信号为语义性（非格式 shortcut）。信息密度分解框架量化 gradient dilution (~26%) vs information overload (~74%)。Tail-truncation 实验发现 256→512 token 区间存在显著性能跳跃，且跨模型一致。

---

## Round 1 → Round 2 修复状态总览

**已解决 10/16** | **部分解决 4/16** | **未解决 1/16** | **部分引用卫生 1/16**

### 已解决 (10)

| Issue | 证据 |
|-------|------|
| R2-N2 实验 scope | 4 模型 3 架构 1.5B-13B，Table 1 完整数据，Conclusion 声明适当限定 |
| R2-W1 标题 vs ae_only | Multi-seed 反转（exception_only 99.83±0.00 > ae_only 99.64±0.49）+ Discussion 解释 |
| R2-W3 SBFL 文献 | Related Work 新增 FL 段落 + Ochiai/Tarantula/DStar/AutoFL/AgentFL/LLM4FL 引用 |
| R1-W2 DeepSeek 归因 | "hypothesize" + "direct evidence lacking"，恰当标记为推测性 |
| R1-W3 数据循环依赖 | Limitations 第六/七条详述 self-familiarity + error distribution bias |
| R1-W4 VOTA truncation | CodeLlama VOTA 98.57% 解耦截断 confound + 正文 caveat |
| R1-M4 Discussion | 从 ~10 行扩展至 65 行 8 段实质内容 |
| R1-M6 代码发布 | ARR checklist "upon acceptance" |
| R5-MCNEMAR | B4 vs SFT p<0.001 / B5 vs SFT p=0.041 正确区分 |
| R5-DEBUGBENCH | Conclusion 中 DebugBench 为已完成工作 |

### 部分解决 (4)

| Issue | 改善 | 残留 |
|-------|------|------|
| R1-N1 格式伪影 | nomarker ablation (97.65% vs B4 93.61%, 4.04pp gap) 大幅增强语义证据 | Discussion 仍引用 B5 McNemar p=0.041 作为主要证据，应降级为辅助 |
| R1-N2 统计推断 | §2.2 正文早期披露重复率 (48.99% test) | 表格 CI 仍基于 n=1190 独立假设；effect size 足够大，方向性结论 robust |
| R1-N3 因果分解 | 全文 "approximately" 限定语 + §4.5 交互效应 caveat | label_only 混淆变量（优化动态改变）未讨论；仅 Qwen-7B seed=42 |
| R-BIB 引用卫生 | 多数 orphan 已清理 | dong2024composition orphan 残留；foster2025mutation 作者疑误；widyasari2024fusefl 名称不一致 |

### 未解决 (1)

| Issue | 说明 |
|-------|------|
| R2-N3 单 seed | VOTA, loop_only, label_only, full_trace, no_trace 仍全部单 seed；Qwen-1.5B 全条件单 seed |

---

## Strengths

1. **系统性消融 + 跨模型泛化**: 7-condition ablation 扩展至 4 模型 3 架构家族，exception dominance 跨模型 gap 仅 0.56pp (99.33-99.89%)
2. **Format-marker ablation 新增**: nomarker condition 证明 ~91% 语义信号（Qwen-7B 3-seed 97.65%±0.96, Qwen-1.5B 97.82%），将 SFT 贡献从"可能是 shortcut"提升至"大部分是语义理解"
3. **信息密度分解框架**: gradient dilution ~26% vs information overload ~74%，该领域首个定量分解，方向性 insight 有价值
4. **Phase transition 跨模型一致**: 256→512 tail tokens 区间 +14.7-23.0pp，对 trace-augmented systems 有直接工程价值
5. **Discussion 质量大幅提升**: 从 10 行扩展至 8 段深入机制分析（exception vs ae_only 解释、format marker 讨论等）
6. **Related Work 补全**: SBFL + fault localization 文献覆盖完整
7. **Limitations 诚实全面**: 8 条，含 self-familiarity bias、error distribution bias、seed variance 详细数据
8. **实验透明度**: 13+ 附录，regression baselines (B1-B5)，training dynamics，calibration 分析

---

## Weaknesses

### Must-Fix（影响提交）

**C1 [critical, 强共识] PDF 编译严重损坏**
编译 PDF 仅 2 页，标题为旧版本（"Model-Agnostic Fault Detection"），Figure 交叉引用显示 "Figure ??"，仅 1 条 reference。tex 源文件内容完整，这是 engineering blocker。提交前必须重新编译并验证。

### Should-Fix（影响评分）

**W1 [warning, 强共识] Table 1 caption 事实性错误**
experiments.tex:16 声称 "ae_only and loop_only ablations tested on Qwen-7B (3 seeds)"，但 Table 8 确认 loop_only 仅 seed=42。必须修正为 "ae_only (3 seeds); loop_only (single seed)"。

**W2 [warning, 共识] Abstract 数据堆砌**
Abstract 含 ~14-15 个独立数字，密度过高。R2 标为 critical，R1 rebut 降级（每个数字服务叙事，ARR 不评 Abstract 数字密度），共识为 warning。建议精简至 5-6 个核心数字。

**W3 [warning, 共识] Qwen-1.5B 全条件单 seed**
支撑 "scale invariance" 的 1.5B 端缺方差估计。CodeLlama-13B 也无 Appendix 完整结果表。建议至少补 Qwen-1.5B exception_only 3 seeds。

**W4 [warning, 共识] CI 未修正为 cluster-robust**
表格 CI 仍基于 n=1,190 独立假设（test set 48.99% duplicates，effective n≈607）。Effect size 极大 (24.70pp)，方向性结论 robust，但建议至少在 Table caption 注明假设，Appendix 报告 dedup sensitivity。

**W5 [warning, 共识] GPU-hours 不一致**
Ethics "under 20 GPU-hours" vs ARR checklist "~50 GPU-hours"。实际计算量保守估计 ≥50。

**W6 [warning, 共识] CodeLlama tail-1024/2048 未完成**
Table tail_cross_model 标注 "pending retraining"，cross-model budget curve 实际基于 3 模型。提交前如无法完成应在 caption 明确。

**W7 [warning] 引用问题残留**
- foster2025mutation 作者归属疑误（bib=foster vs OpenAlex=harman）
- widyasari2024fusefl 正文称 "FuseFL" 但 bib 标题不含此名
- dong2024composition orphan 未清理

### Minor

**M1** "sharp phase transition" 措辞缺中间数据点（tail-384），建议改为 "steep transition"
**M2** related_work.tex:5 "leveraged" → "used"（AI 用词）
**M3** Discussion B5 McNemar p=0.041 应降级为辅助证据，nomarker ablation 作为主要证据
**M4** 新增 FL 引用（widyasari2024llm4fl, mukherjee2025llmfl, kang2024autofl）未经 OpenAlex 验证

---

## Reviewer Consensus

两位 Reviewer 在所有关键问题上高度一致（交叉回应 16 AGREE / 1 REBUT）。

| 问题 | R1 | R2 | 共识 |
|------|-----|-----|------|
| PDF 编译损坏 | AGREE (engineering blocker) | critical | **强共识** |
| Abstract 数据堆砌 | REBUT: warning | critical | R1 rebut→**降级 warning** |
| Table 1 caption 错误 | warning | AGREE | **强共识** |
| 单 seed 覆盖度 | UNRESOLVED | PARTIALLY | 共识（R1 更严厉） |
| CI 未修正 | PARTIALLY | AGREE | 共识 |
| Format marker residual | PARTIALLY | AGREE | 共识 |
| Qwen-1.5B 单 seed | warning | warning | 共识 |
| GPU-hours 不一致 | info | AGREE | 共识 |
| CodeLlama tail pending | info | warning | 共识 |

## Reviewer Divergence

**评分差异**: R1 = 3.0 (Findings), R2 = 3.0-3.5 (Findings/Borderline Conference)

核心分歧在权重分配：R1 侧重统计方法论（CI 未修正 + 单 seed = blocking），R2 侧重新颖性和工程价值（跨模型一致性 + 信息密度分解框架有价值）。R2 承认 R1 的 3.0 在当前状态下也是合理的。两个视角互补。

---

## Questions（需要作者澄清）

1. Table 1 caption 中 "loop_only (3 seeds)" 是否为笔误？Table 8 确认仅 seed=42。
2. Ethics statement GPU-hours "under 20" 与 ARR checklist "~50" 哪个是准确值？
3. CodeLlama tail-1024/2048 实验能否在 5/25 deadline 前完成？
4. foster2025mutation 的正确第一作者是谁？
5. widyasari2024fusefl 引用的是哪篇论文？bib 标题与正文使用的名称 "FuseFL" 不一致。

---

## Missing References

Round 1 遗漏的 SBFL/FL 文献已补充。无新的 missing references，但新增引用需经 OpenAlex 验证真实性。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。

---

## Overall Assessment

**评分：3.0 (Findings) — R1/R2 range: 3.0-3.5**
**置信度：4/5**

**与 Round 1 (2.5 weak reject) 对比**：论文有显著改善（+0.5），从 weak reject 升至 Findings 水平。

**关键改善**：
- 实验从 2 模型扩展至 4 模型 3 架构 1.5B-13B（R2-N2 resolved）
- Format-marker ablation 新增，大幅增强核心论证（~91% 语义信号）（R1-N1 partially resolved）
- CodeLlama VOTA 98.57% 解耦截断 confound（R1-W4 resolved）
- Discussion 质量大幅提升（R1-M4 resolved）
- Related Work SBFL/FL 补全（R2-W3 resolved）
- Limitations 诚实全面（R1-W3 resolved）
- 泛化性声明与证据更匹配（R2-N2, R2-W1 resolved）

**残留弱点**：
1. 多数消融条件仅单 seed（R2-N3 unresolved）
2. CI 未修正为 cluster-robust（方向性结论 robust，但技术瑕疵）
3. Table 1 caption 事实性错误
4. Abstract 数字密度偏高
5. PDF 编译损坏（engineering blocker）

**升级路径（3.0 → 3.5-4.0）**：
1. 修正 Table 1 caption + GPU-hours + PDF 编译 → 消除事实性/工程问题
2. Abstract 精简至 5-6 个核心数字 → 提升可读性
3. Table caption 加 CI caveat + Appendix dedup sensitivity → 消除统计方法论红旗
4. Qwen-1.5B exception_only 补 3 seeds → 强化 scale invariance claim
5. loop_only / VOTA 补 seed → 强化 Tier 层级划分

以上 1-3 可在 deadline 前完成，有望升至 3.5 (Borderline Conference)。4-5 需要额外实验资源。

---

## Detailed Comments

### Abstract
- ~14 个数字密度过高，建议保留核心数字：≥99.33%（四模型 exception dominance）、~91%（语义信号比例）、~74%/26%（信息密度分解）。其余用自然语言表述。

### §1 Introduction
- 无新问题。Contribution 与正文对应关系清晰。

### §2 Method
- §2.2 重复率披露（39.45% train, 48.99% test）是 Round 1 以来的改善。

### §3 Experiments
- Table 1 caption "loop_only (3 seeds)" 事实性错误，必须修正。
- CodeLlama tail-1024/2048 "pending retraining"，如 deadline 前无法完成应在 caption 说明。

### §4 Analysis
- §4.4 nomarker ablation 是本轮最有价值的新增实验。
- §4.5 "approximately decomposes" 措辞改善，但 label_only 混淆变量未讨论。
- "sharp phase transition" 建议改为 "steep transition"。

### §5 Discussion
- 从 10 行扩展至 65 行 8 段，质量大幅提升。
- B5 McNemar p=0.041 作为 semantic understanding 证据应降级为辅助，nomarker ablation 作为主要证据。

### §6 Related Work
- SBFL + FL 段落补全，positioning 清晰。

### §7 Conclusion
- DebugBench 不再列为 future work，已修正。

### Limitations
- 8 条，含 self-familiarity bias 和 error distribution bias，诚实全面。

### Ethics Statement
- GPU-hours "under 20" 与 ARR checklist "~50" 不一致，必须统一。

### References
- foster2025mutation 作者归属待核实（bib=foster vs OpenAlex=harman）
- widyasari2024fusefl 引用名称不一致（正文 "FuseFL" vs bib 标题）
- dong2024composition orphan 未清理
- "leveraged" → "used"

### Appendix
- Table 8 确认 loop_only 仅 seed=42，与 Table 1 caption 矛盾
- 缺 Qwen-1.5B 和 CodeLlama-13B 完整结果附表