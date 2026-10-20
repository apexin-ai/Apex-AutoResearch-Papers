---
round: 3
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T02:30:43.031372+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 2 审稿报告（修订版）

**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models
**Venue**: EMNLP 2026 Main (via ARR)
**审稿人**: Reviewer 1（方法严谨性+实验有效性）、Reviewer 2（新颖性+Related Work+格式）
**轮次**: Round 2（修订评估，基于 Round 1 的 18 个 issue）
**模式**: 2-Reviewer 圆桌 + 交叉分享 + 视觉审查
**修订说明**: 交叉分享完整回复后补充 R2 发现的 "determines" 残留问题

---

## Summary

论文比较四种结构化剪枝标准（CKA-only、Standard/importance-only、RASP/composite、Random）在 GRPO 恢复训练下的表现差异，提出 "recovery capacity gradient"：CKA-only >> Random >> Standard > RASP。修订版新增 3-seed GRPO 验证、Qwen2.5-Math-7B 跨架构实验、15% 跨稀疏度验证、CKA 可靠性讨论，并将标题和 claims 重新 scope 为分析论文。

Round 1 评分 2.5/5，提出 6 个 Critical、8 个 Should-Fix、4 个 Minor。修订版实质性回应了大部分问题。

---

## Strengths

1. **核心发现统计可信**：CKA-only vs Standard 的 4.55pp gap 在 3 GRPO seeds 下稳健（64.39%±0.19 vs 59.84%±0.38, p=0.0009），两组范围不重叠
2. **实验控制显著改善**：Table 2 重建为 v5 controlled config（统一超参 + step 100 + patience=50），消除了 Round 1 最严重的混杂变量问题
3. **Post-SFT confound 反驳有效**：RASP（SFT 61.49%）> Standard（59.29%）但 RASP collapse 更严重；Qwen-Math CKA-only 初始 1.0% → SFT 51.5% vs Standard 18.5% → 21.0%，证明 post-SFT accuracy 不单调决定 GRPO outcome
4. **标题与 framing 改善显著**：新标题准确反映比较研究性质，claims 多处加 scope 限定（"in our experimental setting"、"a plausible mechanism"、"initial evidence"）
5. **CKA 可靠性讨论充分**：引用 Davari et al. 2023 和 Klabunde 2023，解释 intra-layer + linear CKA 如何规避已知问题，Spearman ρ≥0.964 经验验证
6. **Related Work 大幅充实**：orphan 引用从 8 降至 2，新增 doingmore2026、rac2025、ssgr2025、opsd2026 在语境中讨论
7. **跨稀疏度验证**：15% 时 CKA-only 优势扩大到 7.20pp（72.76% vs 65.56%，3-seed），趋势一致
8. **写作质量**：无 AI 写作痕迹，匿名合规，self-recovery overclaim 完全删除

---

## Weaknesses

### Critical（1 项）

**W1. 主文本超过 8 页 — desk rejection 风险** [R1+R2 共识, 视觉审查独立确认]
Section 5 (Discussion and Conclusion) 溢出至 page 9，Limitations 在 page 9 中段才开始。EMNLP 2026 long paper main text 限 8 页（Limitations 不计入但 Discussion/Conclusion 计入）。修订新增内容（CKA reliability 段、多种子报告、跨架构讨论、post-SFT confound 分析）导致溢出约 0.2-0.3 页。R1 在交叉回应中承认此前未充分检查页数，确认同意 critical。**必须在提交前修复。**

### Should-Fix（7 项）

**W2. Qwen-Math 跨架构验证仅 SFT，Abstract 声称 gradient 覆盖两个架构** [R1+R2 共识]
Table 12 仅报告 Post-Prune 和 Post-SFT 准确率。Abstract L4 声称 "we discover a recovery capacity gradient on both... architectures"，但 recovery capacity gradient（Section 3.5）定义为 GRPO peak reward。Qwen-Math 未测 GRPO，不能作为 GRPO gradient 的跨架构证据。建议修改 Abstract 区分两个架构的验证层级，Section 4.5 明确标注仅 SFT。

**W3. 正文 5 处 "determines" 残留，与标题 "Shape" 矛盾** [R2 交叉回应发现]
grep 确认 "determines" 出现在 introduction L4/L7、related_work L22、conclusion L4/L13 共 5 处，Abstract L3 有 "is determined"。标题用 "Shape"（恰当），其他段落用 "plausible mechanism"、"in our experimental setting"（恰当），但 5+1 处 "determines" 构成因果跳跃，与整体 scoping 策略逻辑矛盾。建议统一为 "shapes" 或 "significantly influences"。

**W4. 90.83% vs 81.27% unpruned accuracy 矛盾** [R1 发现]
experiments.tex 正文称 "The original unpruned model achieves 90.83% on GSM8K"，但 Table 2 Unpruned 行显示 81.27%。两个数字可能源于不同评估条件（如 max_new_tokens），但论文未解释。需一句说明。

**W5. GRPO 准确率改变 < 1pp — 实际效用存疑** [R2 发现, R1 部分 REBUT]
Table 2 所有方法 |Δ(SFT→GRPO)| < 1pp。R2 质疑 recovery capacity 的实用性。R1 REBUT 认为 reward trajectory 有独立诊断价值（active learning vs collapse），但同意应补充 300-step accuracy 数据。Extended 300-step training（Figure 5）仅报告 reward 未报告 accuracy——补充此数据可解决关切。

**W6. RASP/Random 仍为单种子** [R1+R2 共识]
CKA-only 和 Standard 有 3 seeds，但 RASP（peak 0.061, collapse）和 Random 仅 1 seed。RASP 的 full collapse 是论文最引人注目的 claim 之一，单种子基础薄弱。

**W7. Random baseline SFT/GRPO Acc 缺失** [R1 发现]
Table 2 中 Random 的 SFT Acc 和 GRPO Acc 为 "--"，仅有 Peak Rew.。4 种剪枝标准的对比实验缺 1 种的核心数据。

**W8. Post-SFT confound 在 DeepSeek-7B 上结构未变** [R1 发现, R2 部分同意]
Qwen-Math reversal 有力，但在主要实验平台 DeepSeek-7B 上，CKA-only 仍然 Post-SFT 最高（63.91% vs 59.29%）。RASP counter-example（61.49% > 59.29% 但 collapse）部分缓解，但未完全排除 Post-SFT accuracy 作为混杂变量。从 Round 1 Critical 降为 Should-Fix。

---

## Questions

1. 90.83% 和 81.27% 分别在什么评估条件下得到？如果是 max_new_tokens 差异，为什么 Table 2 和正文使用不同设置？
2. Extended training（300 steps）后各方法的 GSM8K accuracy 是多少？如果 accuracy 仍未改变，如何论证 reward 作为 leading indicator 的有效性？
3. Random baseline 的 SFT/GRPO accuracy 为什么缺失？是实验未做还是数据丢失？
4. RASP 在另一个种子下是否也 collapse？如果不 collapse，"recovery capacity gradient" 的底端如何成立？

---

## Missing References

未发现重大遗漏。Related Work 已充分覆盖 2024-2026 年结构化剪枝 + RLVR 领域主要工作。新增引用（davari2023cka, klabunde2023, doingmore2026, rac2025, ssgr2025, opsd2026）全部经 OpenAlex/arXiv 验证真实。

残留 2 个 orphan bib 条目（bai2024longbench, hendrycks2021mmlu），均为 benchmark 引用，建议删除或在实验 setup 中引用。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查完成（2 critical, 2 warning, 8 info）：

| 严重度 | 位置 | 发现 |
|--------|------|------|
| **critical** | page 9 | 主文本溢出至第 9 页（与 W1 一致） |
| **critical** | page 14 | 末页 Figure 6 仅占 30%，70% 空白 |
| warning | pages 3-5 | Method 连续 3 页无 figure/table |
| warning | page 12 | Appendix 极度拥挤（5 display items 挤一页） |
| info | page 1 | 标题/摘要排版规范，ACL 匿名格式正确 |
| info | page 2 | Figure 1 是比较框架图而非核心发现图 |
| info | pages 6-8 | 实验部分 display item 密度良好（3 页 7 items） |
| info | figures | 颜色方案跨图一致，色盲友好 |
| info | figure 3 | 子图 y 轴标签字号偏小（~7-8pt） |
| info | figure 4 | 热力图灰度打印时对比度可能不足 |

---

## Overall Assessment

### 评分

| Reviewer | Soundness | Excitement | Reproducibility | Overall | Confidence |
|----------|-----------|------------|-----------------|---------|------------|
| R1 | 3.0 | 3.0 | 3.0 | **3.0** | 4 |
| R2 | 3.0 | 2.5 | 3.5 | **3.0** | 4 |
| **共识** | **3.0** | **2.75** | **3.25** | **3.0** | **4** |

### 评分变化（Round 1 → Round 2）

| 维度 | Round 1 | Round 2 | Δ |
|------|---------|---------|---|
| Overall | 2.5 | **3.0** | **+0.5** |

### 收敛分析

两位 Reviewer 独立评分均为 3.0 (Findings)，交叉分享后确认共识，无未解决分歧。

**一致同意已解决**: 标题重写、多种子核心验证（p=0.0009）、CKA 可靠性讨论、Related Work 补全、patience 统一、Table 2 控制实验、Self-Healing 讨论、self-recovery 删除。

**一致同意仍需修复**: 页数超限（critical）、Qwen-Math 仅 SFT 但 Abstract overclaim、RASP/Random 单种子。

**唯一分歧**: GRPO |Δ|<1pp 的实用性——R2 视为 warning，R1 REBUT 认为 reward 有诊断价值但同意补充 300-step accuracy。不影响评分。

**Excitement 轻微分歧**: R1=3.0（认为对 reasoning compression 社区有 meaningful impact）vs R2=2.5（纯 empirical observation 无方法创新）。

### 结论

**Overall: 3.0 / 5 (Findings)**

修订版实质性改善了 Round 1 的核心问题。论文从 Borderline Findings (2.5) 上升到 Findings (3.0) 水平。

**必须修复（提交前）**:
1. 页数超限（W1）— desk rejection 风险

**强烈建议修复（提交前或 camera-ready）**:
2. Abstract L4 Qwen-Math framing（W2）— overclaim
3. 5+1 处 "determines" → "shapes"（W3）— 与标题/scoping 矛盾
4. 90.83% vs 81.27% 解释（W4）— 数据矛盾

**建议 camera-ready 修复**:
5-8. GRPO 效用论证、RASP 种子、Random accuracy、confound 讨论
9-10. GRPO/SFT 完整超参
11. 2 个 orphan bib

---

## Detailed Comments

### Round 1 Issue Resolution Summary

| ID | 原严重度 | Round 2 状态 | 说明 |
|----|----------|-------------|------|
| R1-N1 | critical | **in_progress** | Qwen-Math reversal 有力但仅 SFT → 降为 should-fix |
| R1-N2 | critical | **resolved** | v5 controlled config |
| R1-N3 | critical | **resolved** | patience=50 统一 |
| R1-N4 | critical | **resolved** | 3-seed, p=0.0009 |
| R2-N1 | critical | **resolved** | 标题重写 |
| R2-N2 | critical | **in_progress** | 多种子改善，RASP 单种子/跨架构无 GRPO 残留 |
| R1-W1 | warning | **in_progress** | 大部分修复，5 处 determines 残留 |
| R1-W2 | warning | **resolved** | overclaiming 修复 |
| R1-W3 | warning | **resolved** | TBD 删除 |
| R1-W5 | warning | **resolved** | ±std + p-values |
| R2-N3 | warning | **resolved** | Self-Healing 差异解释 |
| R2-W1 | warning | **in_progress** | 8→2 orphans |
| R2-W2 | warning | **resolved** | CKA reliability 段落 |
| R2-W4 | warning | **resolved** | bib 年份修正 |
| R1-M1 | info | **resolved** | training steps caveat |
| R1-M2 | info | **resolved** | self-recovery 删除 |
| R1-M3 | info | **in_progress** | 定义与使用不完全一致 |
| R1-M4 | info | **resolved** | reward 对齐 |

**Resolved**: 13/18 (72%)
**In-progress**: 5/18 (28%)

### Round 2 New Issues

| ID | 严重度 | 描述 | 来源 |
|----|--------|------|------|
| R2-NEW-N1 | **critical** | 主文本超过 8 页 | R1+R2+Visual |
| R2-NEW-W1 | warning | 90.83% vs 81.27% 矛盾 | R1 |
| R2-NEW-W2 | warning | Abstract Qwen-Math overclaim | R1+R2 |
| R2-NEW-W3 | warning | GRPO Δacc < 1pp 效用存疑 | R2 (R1 partial rebut) |
| R2-NEW-W4 | warning | RASP/Random 单种子 | R1+R2 |
| R2-NEW-W5 | warning | Random SFT/GRPO Acc 缺失 | R1 |
| R2-NEW-W6 | warning | 5 处 "determines" 残留 | R2 |
| R2-NEW-M1 | info | GRPO batch size/rollouts 未报告 | R1 |
| R2-NEW-M2 | info | SFT lr/batch/optimizer 未报告 | R1 |

### Issue Tracker

已更新至 `artifacts/review_issues.yaml`（Round 1 的 18 条 + Round 2 新增 11 条，共 29 条 + 2 visual）。