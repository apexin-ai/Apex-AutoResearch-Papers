---
round: 4
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T03:19:34.368679+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 审稿报告

**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models
**Venue**: EMNLP 2026 Main (via ARR)
**审稿人**: Reviewer 1（方法严谨性+实验有效性）、Reviewer 2（新颖性+格式合规+写作质量）
**轮次**: Round 3（第二次修订评估）
**模式**: 2-Reviewer 圆桌 + 交叉分享 + 视觉审查

---

## Summary

Round 2 报告提出 1 critical（页数超限）+ 7 should-fix + 2 minor + 2 visual 问题，共 16 个 in_progress issues。作者通过 D094 action matrix 全面修复：主文本压缩至 8 页、"determines" 全部替换为 "shapes"、Abstract 区分 GRPO vs SFT 验证层级、90.83% 脚注解释、超参数表完整、orphan bib 清零、Appendix 重排。

本轮验证确认：**Round 2 的全部 critical 和 should-fix 问题均已解决**。仅存 3 个 minor 级别新问题（"strongest evidence" 措辞、300-step seed 未标注、无代码发布声明），均不阻塞接收。

---

## Strengths

1. **核心发现统计可信**：CKA-only vs Standard 4.55pp gap，3-seed p=0.0009，范围不重叠
2. **实验控制完善**：Table 2 v5 controlled config，patience 统一，超参数表完整（Appendix tab:hyperparams 覆盖 GRPO + SFT 全部参数）
3. **Claims 与证据匹配**：标题 "Shape" = 正文 "shapes/significantly influences"，Abstract 区分 GRPO(DeepSeek) vs SFT(Qwen-Math)，全文因果语言自洽
4. **格式合规**：主文本严格 ≤ 8 页，13 页总长，匿名合规，ACL 模板正确
5. **引用完整**：38 bib 全部引用，0 orphan，新增引用均经验证真实
6. **数据矛盾已解释**：90.83% vs 81.27% 脚注说明 SFT catastrophic forgetting
7. **透明度高**：RASP/Random 单种子脚注标注，Random checkpoint 缺失标注，Limitations 4 段覆盖全面
8. **写作质量**：无 AI 痕迹，无 "determines" 残留，self-recovery 已删除

---

## Weaknesses

本轮无 critical 或 should-fix 级别问题。

### Minor（3 项，均非阻塞）

**M1. "strongest evidence" 措辞** [R1 flag, R2 可接受]
experiments.tex L120 "provides the strongest evidence that recovery capacity is shaped by preserved network structure"——R1 认为 SFT-only 结果称 "strongest" 偏强，建议 "suggestive/additional"。R2 认为在当前语境下可接受（已用 "shaped by"，L121 标注仅 SFT）。不影响评分。

**M2. 300-step accuracy 未标注 seed** [R1 flag]
experiments.tex L75 的 300-step accuracy 数据为单 seed 结果，未标注 seed 编号。建议 camera-ready 标注 "(seed 42)" 或 "(single seed)"。

**M3. 无代码/checkpoint 发布声明** [R1 flag]
Ethics Statement 提及公开模型/数据，但无代码发布承诺。ARR Reproducibility 维度可能扣分。建议在 camera-ready 或 rebuttal 中说明发布计划。

---

## Questions

无阻塞性问题。此前提出的 4 个 Questions 均已在修订中回答：
1. 90.83% vs 81.27% → 脚注解释 SFT catastrophic forgetting ✓
2. 300-step accuracy → 已引入数据 ✓
3. Random 缺失 → checkpoint 未保存脚注 ✓
4. RASP 单种子 → Limitations 披露 + f0 collapse 论证 ✓

---

## Missing References

无遗漏。38 bib entries，38 cited，0 orphan，0 missing。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查完成（0 critical, 4 warning, 9 info）：

| 严重度 | 位置 | 发现 |
|--------|------|------|
| warning | pages 3-5 | Method 连续 3 页缺 figure/table（公式部分缓解） |
| warning | page 7 | 3 display items 拥挤（Figure 3+4 + Table 2） |
| warning | page 7 | Figure 3 子图文字 ≤7pt，接近可读性下限 |
| warning | page 7 | Figure 4 layer 轴标签密集 |
| info | 全文 | 无 margin 溢出，ACL 模板合规，公式渲染正确，颜色方案一致 |

**与 Round 2 对比**: Critical 从 2 降至 0（页数合规 + Figure 6 空白已修复）。Warning 从 2 降至主要集中在 page 7 display item 密度，属排版偏好而非合规问题。

---

## Overall Assessment

### 评分

| Reviewer | Soundness | Excitement | Reproducibility | Overall | Confidence |
|----------|-----------|------------|-----------------|---------|------------|
| R1 | 3.5 | 3.0 | 3.0 | **3.0** | 4 |
| R2 | 3.0 | 2.5 | 3.5 | **3.0** | 4 |
| **共识** | **3.25** | **2.75** | **3.25** | **3.0** | **4** |

### 评分历史

| 轮次 | Overall | 关键变化 |
|------|---------|--------|
| Round 1 | 2.5 | 6 critical issues |
| Round 2 | 3.0 | 5/6 critical resolved, 1 critical new (page limit) |
| **Round 3** | **3.0** | All critical/should-fix resolved, 3 minor residual |

### 收敛分析

两位 Reviewer 独立评分均为 3.0 (Findings)，交叉分享后完全收敛。

**共识**:
- 所有 critical 和 should-fix 问题已解决
- 论文格式合规，写作质量高，claims 与证据匹配
- 推荐 Findings track 接收
- 残留 minor 问题不阻塞接收

**轻微分歧**:
- R1 Soundness 3.5 vs R2 3.0：R1 认为 3-seed 统计支撑和完整超参值得更高 soundness
- R1 Excitement 3.0 vs R2 2.5：R2 认为 empirical observation + trivial 方法限制了 excitement
- R1 标记 S6 (recovery capacity 定义不一致) 为 STILL_OPEN，R2 认为已解决——不影响评分

### 结论

**Overall: 3.0 / 5 (Findings)**

论文经过三轮修订，已从 Borderline Findings (2.5) 稳定提升至 Findings (3.0)。所有阻塞性问题已解决。作为一篇 well-controlled empirical study，论文清晰地回答了 "pruning criterion 如何影响 RLVR recovery" 这个问题，核心发现有统计支撑，claims 与证据范围匹配。

**推荐**: Accept for Findings。

**Camera-ready 建议（非阻塞）**:
1. "strongest evidence" → "suggestive evidence"（M1）
2. 300-step accuracy 标注 seed（M2）
3. 添加代码发布声明（M3）
4. Table 1 reward metrics 补 ±std（R1 M1）

**提升至 Conference (3.5+) 需要**（超出当前 scope）:
- Random/RASP 3-seed 验证
- Qwen-Math GRPO 实验
- 第二种 RL 算法验证
- 代码/checkpoint 发布

---

## Issue Tracker Summary

| 类别 | 总数 | Resolved | In-progress | Open |
|------|------|----------|-------------|------|
| Round 1 | 18 | 17 | 1 (R1-M3 定义) | 0 |
| Round 2 | 13 | 13 | 0 | 0 |
| Round 3 | 3 | 0 | 0 | 3 |
| **Total** | **34** | **30** | **1** | **3** |

已更新至 `artifacts/review_issues.yaml`。