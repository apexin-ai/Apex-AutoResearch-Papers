---
round: 16
review_mode: continue
overall_score: borderline (weak accept leaning) 6.5/10
timestamp: 2026-05-23T15:56:59.315198+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 审稿报告（继续审稿：R15→R16 修订评估）

**论文**：How VLA Fine-Tuning Changes Instruction Routing: A Cross-Architecture Analysis
**Venue**：CoRL 2026（8 页正文，corl_2026 模板，double-blind）
**审稿模式**：Continue（R15 weak reject 4.5/10 → R16 修订评估）
**Reviewer Panel**：R1（方法/统计）7/10，R2（Framing/Writing/Format）6/10
**交叉分享**：完成，无实质性分歧

---

## Summary

R16 修订实质性地解决了 R15 提出的核心问题。R15 的 6 个 must-fix 中 **6/6 RESOLVED**，10 个 should-fix 中 **8/10 RESOLVED 或 LARGELY RESOLVED**。论文从方法论上不可辩护的状态（sign test N=6、伪重复 CI、标题 overclaim、格式违规）转变为方法论上 defensible 的跨架构分析研究。

**关键改进**：
- 统计框架从 sign test (N=6, p=0.016) 全面转向 effect-size + CI (MCCV n=1000, demo-level splitting)，量化了 CI inflation
- 标题从 "Three Architectures, One Routing Pattern" 改为描述性 "How VLA Fine-Tuning Changes Instruction Routing: A Cross-Architecture Analysis"
- NLP control 从一句话扩展为完整实验段落（Llama-2-7b-chat, ΔR²=0.000）
- 所有 7 条 setlength 格式 hack 移除，正文 ≤8 页
- Abstract 从 ~220 词精简至 ~137 词
- 并发工作（Fang 2026, Buurmeijer 2026）获得 dedicated differentiation 段落

---

## Strengths

1. **方法论诚实度**：作者不仅修复了统计问题，还量化了修复的影响（demo-level split 使 R² 从 0.75-0.8 降至 0.4-0.6），展示了对伪重复问题的深入理解。

2. **Effect-size 框架设计合理**：ΔR² > 0.10 阈值有双重辩护（语义：10% 绝对方差变化；稳健性：0.08/0.10/0.20 同一分组），VLM-to-VLA 最小值 (0.156) 与 VLA-to-VLA 最大值 (0.086) 之间有 ~2× gap，分离不依赖精确阈值选择。

3. **NLP control 有效**：Llama-2-7b-chat 作为 same-backbone-different-objective control，ΔR²=0.000 clean 排除了 "generic fine-tuning artifact" 解释。

4. **Claims 恰当收窄**：N=2 限制在 Limitations 显式标注，"convergent" 仅在描述性上下文中使用（附 "qualitative pattern" 限定词），Cohen's d 改为 "medium-to-large"。

5. **并发工作区分系统**：behavioral (Fang 2026) vs representational (本文) 的区分清晰准确。

6. **格式合规**：setlength 全部移除，正文 ≤8 页，术语统一，Abstract 精简。

---

## Weaknesses（按严重程度排序）

### Must-Fix（0 项）

无。R15 的所有 must-fix 均已 RESOLVED。

### Should-Fix（4 项）

1. **[SF-1] 主文 Limitations 缺少 open-loop 声明**（R16-N3, R2 发现, R1 AGREE）
   - 主文 Limitations 列出 N=2、LIBERO-only、causal-decoder only、NORA checkpoints、single checkpoint，但未提及所有分析均为 open-loop。Appendix 有覆盖但主文遗漏。对 CoRL 受众这是自然关切。
   - **修复**：加一句 "All analyses are open-loop; closed-loop behavioral validation is left for future work."

2. **[SF-2] 残余动态语言**（R14-W2, R1 发现 PARTIALLY RESOLVED, R2 AGREE minor）
   - 标题和核心 claims 已改用中性语言，但正文仍有 3-5 处动态表述（"creates", "induces", "stabilizes"），在单 checkpoint 设计下技术上不严谨。
   - **修复**：替换为 "is associated with" / "corresponds to" / "differs between"。

3. **[SF-3] arXiv 引用未更新**（R12-W3, R2 发现, R1 AGREE minor）
   - touvron2023_llama2, black2024_pi0 仍为 arXiv 版本。
   - **修复**：Camera-ready 前检查是否有正式发表版本并更新。

4. **[SF-4] NLP control 仅覆盖 Llama-2 backbone**（R16-N1, 两位均判 minor）
   - VLM→VLA exit collapse 主要在 TracVLA (Phi-3) 和 NORA (Qwen2.5) 上观察到，但 NLP control 仅用 Llama-2。Single-backbone control 已足以排除 generic artifact，但不完美。
   - **修复**：Limitations 注明此局限。

### Minor / Cosmetic（3 项）

5. **[M-1] Table 2 脚注密度**（R16-N2, 两位均判 minor）——6 种标记增加认知负荷。考虑将 metric 类型升级为列内标识。

6. **[M-2] Pages 4-5, 7 文本密集**（R15-I3, 视觉审查 warning）——连续 3-4 页无 display item。可考虑从 Appendix 提升一个 figure。

7. **[M-3] Figure 1 子面板标签偏小**（R15-I2, 视觉审查 info）——Caption 已从 15 行缩至 3 行（改善），但面板密度仍高。

---

## Questions

1. ΔR² > 0.10 阈值是否预注册或有先验依据？目前的 post-hoc 辩护（敏感性分析）已充分，但预注册声明会更强。
2. 是否有计划在 camera-ready 或 follow-up 中加入 Phi-3-mini-chat 或 Qwen2.5-instruct 的 NLP control probing？

---

## Missing References

无新增缺失引用。R15 提出的 Fang et al. 2026 已补充。

---

## External Review

未返回（本轮未请求外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查完成（0 critical, 2 warning, 10 info）：
- **Warning**：Pages 4-5 和 page 7 连续纯文本，缺乏视觉锚点（与 R15-I3 一致）
- **Info**：Figure 1 面板密集但 caption 改善；Figure 2/3 清晰可读；Table 1/2 排版规范；全文无 LaTeX 渲染错误；行号/页码/匿名标记正确；References 格式统一
- 无页面溢出，无格式违规

---

## Overall Assessment

| 维度 | R15 评分 | R16 评分 | 变化 |
|------|---------|---------|------|
| Reviewer 1（方法/统计） | 5/10 | 7/10 | +2 |
| Reviewer 2（Framing/Writing） | 5/10 | 6/10 | +1 |
| **综合** | **4.5/10** | **6.5/10** | **+2** |

**综合评分：6.5/10 — Borderline (Weak Accept 倾向)**

**评分理由**：

R16 修订将论文从 "方法论不可辩护" 提升至 "方法论 defensible"。统计框架的根本性升级（demo-level MCCV、effect-size + CI 替代 sign test、TOST δ 收紧至 0.10）、NLP control 的完善、claims 的恰当收窄、格式合规——这些都是实质性改进而非表面修补。

上调幅度（+2）的限制因素是结构性的：N=2 independent VLM-to-VLA transitions 仍然有限（无法通过统计方法弥补）；LIBERO-only 无法验证 generalizability；无 closed-loop validation 意味着 representational findings 与 robot behavior 的关联仍为推测；并发工作（Swann 2026: 6 models × 4 benchmarks）在 scale 上远超本文。

**对 AC 的建议**：论文在 6-7/10 区间，取决于对方法论 soundness（偏 7）vs. novelty/impact breadth（偏 6）的相对权重。R1 和 R2 在所有技术判断上一致，评分差异仅反映审查视角不同。Camera-ready 需修复 4 项 should-fix（open-loop 声明、动态语言、arXiv 引用、NLP control 覆盖度声明），均为 trivially fixable。

---

## Detailed Comments

### R15→R16 Issue Resolution Summary

| R15 Issue | Category | R16 Status |
|-----------|----------|------------|
| R15-N1 伪重复/CI偏窄 | method/critical | ✅ RESOLVED |
| R15-N2 NLP control不足 | method/critical | ✅ RESOLVED |
| R15-N3 并发工作区分 | writing/critical | ✅ RESOLVED |
| R15-N4 setlength违规 | format/critical | ✅ RESOLVED |
| R14-N1 Convergent overclaim | framing/critical | ✅ RESOLVED |
| R12-N2 页面溢出 | format/critical | ✅ RESOLVED |
| R12-N3 Abstract过载 | writing/critical | ✅ RESOLVED |
| R9-N6 Sign test power | experiment/warning | ✅ RESOLVED |
| R9-W4 Cohen's d混合metric | method/warning | ✅ RESOLVED |
| R15-W1 可读性 | writing/warning | ✅ RESOLVED |
| R15-W2 定位模糊 | framing/warning | ✅ RESOLVED |
| R15-W3 d≥0.45 framing | framing/warning | ✅ RESOLVED |
| R15-W4 TOST δ=0.30 | method/warning | ✅ LARGELY RESOLVED |
| R15-W5 Cross-Benchmark命名 | writing/warning | ✅ RESOLVED |
| R15-W6 Discussion重复 | writing/warning | ✅ RESOLVED |
| R14-DIV1 Linear probe | method/info | ✅ RESOLVED |
| R14-W2 动态语言 | experiment/warning | ⚠️ PARTIALLY RESOLVED |
| R12-W3 arXiv引用 | writing/warning | ❌ STILL_OPEN (minor) |

### R16 新发现

| Issue | Category | Severity | Both Agree |
|-------|----------|----------|------------|
| R16-N1 NLP control 单backbone | experiment | info | ✅ |
| R16-N2 Table 2 脚注密度 | writing | info | ✅ |
| R16-N3 Open-loop 主文声明缺失 | writing | info | ✅ |