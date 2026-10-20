---
round: 17
review_mode: continue
overall_score: 7/10 — Weak Accept (conditional)
timestamp: 2026-05-27T01:08:59.271606+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告（继续审稿：R16→R17 修订评估）

**论文**：Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis
**Venue**：CoRL 2026（8 页正文，corl_2026 模板，double-blind）
**审稿模式**：Continue（R16 borderline 6.5/10 → R17 修订评估）
**Reviewer Panel**：R1（方法/统计/内容质量）7.5/10，R2（Framing/Writing/Format）6/10
**交叉分享**：完成，关键判断达成共识

---

## Summary

R17 在 R16 基础上完成了两项实质性改进和多项 polish。论文方法论从 defensible 进一步提升至 solid——NLP control 覆盖度从 1/3 扩展到 3/3 backbone 家族，counterfactual metric 不可比性问题通过 Table 2 重构彻底解决。

然而，`\enlargethispage{12\baselineskip}` 构成新的格式违规（R15-N4 的变体复发），且 Discussion 中出现一处基于 non-significant correlation 的 overclaim（"replacing costly rollout evaluation"）。两位 Reviewer 共识：这些是 Should-Fix 级别问题，应作为 conditional acceptance 的修改条件，而非 rejection 依据。

**R16→R17 SF Resolution**：R16 的 4 项 Should-Fix 中 **2/4 RESOLVED**（SF-2 动态语言、SF-4 NLP control 覆盖），**1/4 RESOLVED**（SF-3 arXiv 引用），**1/4 N/A**（SF-1 open-loop 声明已在 R16→R17 间修复）。

---

## Strengths

1. **NLP control 全覆盖（3/3 backbone families）**：Llama-2-7b-chat（匹配 OpenVLA）、Phi-3-mini-4k-instruct（匹配 TracVLA）、Qwen2.5-3B-Instruct（匹配 NORA），三者 ΔR² = 0.000–0.008。这是对 "exit collapse is VLA-specific" claim 的最有力证据——排除了 generic fine-tuning artifact 解释，跨三个不同架构家族。Qwen2.5 匹配不完美（缺 vision encoder）已在脚注诚实标注。（R1 RESOLVED，R2 AGREE）

2. **Counterfactual 指标分离**：Table 2 仅含 Cohen's d（OpenVLA + TracVLA），NORA cosine distance 独立讨论于 §4.4.2。彻底消除了 R9-W4 以来反复提出的 metric 不可比性问题。Cohen's d 范围从 0.45–1.97 修正为 0.45–1.52，更 honest。（R1 判为"改进而非问题"，R2 AGREE）

3. **动态语言全面清理**：标题完全静态化（"Instruction Routing in Fine-Tuned VLAs"），全文使用 "associated with"/"correlational"，显式 caveat "Exit collapse is correlational"。唯一残余 "develop" 在 observational 语境下可接受。（R1 RESOLVED，R2 AGREE）

4. **"Reference" 术语统一**：消除了 "untrained" 对 OXE-pretrained OpenVLA 的误导性。全文一致使用 "reference" 指代 comparison baseline。（R1 判为"纯改进"，R2 AGREE）

5. **Permutation test 补充统计支撑**：Appendix A.37 新增 permutation test (p=0.008)，补充了 effect-size + CI 框架的 inferential 支撑。与 R16 框架互补。（两位均判方向正确）

6. **Label-permutation controls**：对 counterfactual perturbation 的 instruction labels 做 shuffle 后 sensitivity 消失，确认原始结果非 trivial correlation。Standard robustness check。

---

## Weaknesses（按严重程度排序）

### Must-Fix（0 项）

无。

### Should-Fix（3 项）

1. **[SF-1] `\enlargethispage{12\baselineskip}` 格式违规**（R17-N4 + R15-N4 变体复发，R2 发现，R1 AGREE）
   - **位置**：`discussion.tex` line 1，影响 PDF page 8
   - **效果**：page 8 文本区域高度增加 ~144pt（~5cm），额外容纳 ~12 行 Discussion 内容。CoRL 模板自身仅用 `\enlargethispage{2\baselineskip}`（首页 notice box），作者用量为模板的 6 倍。
   - **性质**：与 R15-N4 的 `\setlength` 性质不同（单页标准命令 vs 全局模板参数修改），但效果相同——容纳超出 8 页限制的内容。R2 指出论文实际内容量约 8.3-8.5 页。
   - **R1/R2 共识**：Should-Fix，conditional acceptance 条件。
   - **修复**：删除 `\enlargethispage{12\baselineskip}`，将 Practical implications 段落（~13 行）精简至 3-4 行或移入 Appendix。同时删除 `\vspace{-4pt}` 等 negative spacing。

2. **[SF-2] "replacing costly rollout evaluation" overclaim**（R17-N5，R1 交叉回应中发现）
   - **位置**：`discussion.tex` line 14
   - **问题**：论文支撑 ΔR² 作为 checkpoint selector 的唯一证据是 ρ = 0.583, p = 0.10, n = 9（non-significant correlation）。用 non-significant evidence 支撑 "replacing" 表述与论文通篇 observational/correlational framing 不一致。
   - **修复**："replacing" → "supplementing" 或 "providing a complementary signal to"；或在 "replacing" 后插入 caveat "(pending validation; ρ = 0.583, p = 0.10, n = 9)"。

3. **[SF-3] Permutation test scheme 描述不足**（R17-N1，R1 发现，R2 AGREE）
   - **位置**：§4.6 + Appendix A.37
   - **问题**：报告 "permutation test p = 0.008" 但未说明：(a) shuffle 对象；(b) permutation 次数；(c) test statistic。p = 0.008 对于 N=2 architectures 的 permutation space 需要解释来源。
   - **修复**：A.37 补充 2-3 句说明 permutation procedure。

### Minor / Cosmetic（2 项）

4. **[M-1] Checkpoint selection 基于 non-significant correlation 应显式标注**（R17-N2，两位均判 minor）
   - §5 Practical implications 中 ρ = 0.583, p = 0.10, n = 9 的 hedging 已充分（"suggest...each requiring independent validation"），但建议显式标注 "non-significant at conventional levels"。

5. **[M-2] Pages 3-4 连续纯文本**（R15-I3，视觉审查 warning 一致）
   - 与 R16 相同。Related Work 尾部 + Method §3.1-3.3 连续两页无 display item。

---

## Questions

1. Permutation test (p=0.008) 的具体 scheme 是什么？是 label permutation（shuffle trained/reference per cell）还是其他方式？使用多少 permutations？Test statistic 是什么？
2. 是否考虑在 camera-ready 中将 Practical implications 移入 Appendix 以解决格式问题？这既解决 `\enlargethispage` 的需要，又保留了 speculative implications 的完整性。

---

## Missing References

无新增缺失引用。

---

## External Review

未请求（本轮未启用外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查完成（0 critical, 2 warning, 18 info）：
- **Warning**：(1) Pages 3-4 连续两页纯文本（Related Work 尾部 + Method），无 display item；(2) Figure 14 (page 22) y 轴标签约 5pt，低于可读性基准
- **Info 亮点**：Figure 2 全宽热力图清晰；Figure 3 三面板线图视觉密度佳；Tables 1-2 booktabs 风格整洁；References 无未解析引用；GenAI 声明位置合规；Appendix Figure 25 Claim-evidence 流程图颜色编码清晰
- 无页面溢出（但 page 8 依赖 `\enlargethispage` 达成）
- 无 LaTeX 渲染错误

---

## Overall Assessment

| 维度 | R15 评分 | R16 评分 | R17 评分 | 变化 |
|------|---------|---------|---------|------|
| Reviewer 1（方法/统计） | 5/10 | 7/10 | 7.5/10 | +0.5 |
| Reviewer 2（Framing/Writing） | 5/10 | 6/10 | 6/10 | ±0 |
| **综合** | **4.5/10** | **6.5/10** | **7/10** | **+0.5** |

**综合评分：7/10 — Weak Accept**

**评分理由：**

R17 完成了从 R15 (4.5/10) 到当前 (7/10) 的累积改进轨迹：

- **R15→R16 (+2.0)**：统计框架根本性修复（demo-level MCCV、effect-size+CI 替代 sign test、TOST δ 收紧、claims 收窄、格式合规）
- **R16→R17 (+0.5)**：NLP control 3/3 全覆盖、metric 分离、术语/语言 polish、permutation test 补充

R1 (7.5) 与 R2 (6.0) 之间 1.5 分的差距来自审查视角不同而非事实分歧：
- **R1 侧重方法论严谨性**：R17 在此维度出色——统计框架 sound、NLP controls 完善、claims 恰当 hedged → 7.5
- **R2 侧重 contribution significance + 格式合规**：N=2 convergence 有限、LIBERO-only、描述性发现、格式违规 → 6.0（排除格式后 R2 自评 6.5）

**综合取 7/10 的理由**：R2 确认排除格式问题后评分为 6.5，与 R1 的 7.5 均在 Weak Accept 区间。格式问题（`\enlargethispage`、"replacing" overclaim）均为 trivially fixable 的 camera-ready 条件。取 R1 和 R2（排除格式后）的均值 7.0 作为综合评分。

**对 AC 的建议**：

**Conditional Weak Accept。** Camera-ready 前必须完成 3 项 Should-Fix：
1. 删除 `\enlargethispage{12\baselineskip}`，精简 Discussion 使正文 ≤8 页（无格式 hack）
2. "replacing" → "supplementing"
3. Appendix A.37 补充 permutation scheme 细节

论文的 acceptance 取决于 AC 对以下 trade-off 的判断：
- **方法论 soundness**（偏 accept）：统计框架 defensible，NLP controls 全覆盖，claims 恰当 hedged
- **Novelty/impact breadth**（偏 borderline）：N=2 independent transitions，LIBERO-only，open-loop only，描述性而非 prescriptive findings
- **CoRL scope fit**（AC 裁量）：纯 representational analysis 无物理机器人实验。论文定位为 "complementary" 分析，是否符合 CoRL 受众预期由 AC 判断

残余结构性限制（已承认，不影响接收决定）：N=2 clean VLM-to-VLA transitions、LIBERO-only benchmark、single checkpoint per architecture、open-loop analysis without closed-loop validation。这些在 Limitations 和 Extended Discussion 中充分承认。

---

## Detailed Comments

### R16→R17 Issue Resolution Summary

| R16 Issue | Category | R17 Status |
|-----------|----------|------------|
| R16-SF1 Open-loop 主文声明 | writing | ✅ RESOLVED（R16→R17 间已修复） |
| R16-SF2 (R14-W2) 动态语言残留 | framing | ✅ RESOLVED |
| R16-SF3 (R12-W3) arXiv 引用 | writing | ✅ RESOLVED（black2024_pi0 → RSS 2025） |
| R16-SF4 (R16-N1) NLP control 单 backbone | experiment | ✅ RESOLVED（3/3 覆盖） |

### R17 新发现

| Issue | Category | Severity | Both Agree |
|-------|----------|----------|------------|
| R17-N4 \enlargethispage 格式违规 | format | Should-Fix | ✅ |
| R17-N5 "replacing" overclaim | framing | Should-Fix | ✅（R1 发现） |
| R17-N1 Permutation scheme 描述不足 | method | Should-Fix | ✅ |
| R17-N2 Non-significant correlation 标注 | framing | Minor | ✅ |
| R17-N3 标题信息量降低 | writing | Negligible | ✅（trade-off，不需修改） |

### R15-N4 格式违规追踪

| Round | 机制 | 严重程度 | 状态 |
|-------|------|---------|------|
| R15 | 7 × \setlength（全局间距修改） | Critical | 提出 |
| R16 | 清除全部 setlength | — | RESOLVED |
| R17 | \enlargethispage{12\baselineskip}（单页 margin 变形） | Should-Fix | 复发（变体） |

这一 recurring pattern 表明论文内容量持续在 8 页限制边缘。根本解决方案是精简 Discussion（将 Practical implications 移入 Appendix），而非引入新的格式手段。