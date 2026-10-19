---
round: 33
review_mode: continue
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T04:52:13.300892+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 33 审稿报告

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 ARR (Long Paper)
**审稿模式**: 继续审稿（基于 Round 32 报告）
**Reviewer**: R1（方法严谨性 + 页面合规）, R2（新颖性 + 完整性）
**轮次**: 2 轮（初审 + 交叉分享）

---

## Summary

R33 的核心修改包括：(1) 将 Conclusion 合并入 Discussion（§5 → "Discussion and Conclusion"），(2) 移除 `\enlargethispage` hack，(3) 压缩 §4.3–4.5 使正文自然适配 8 页，(4) 新增 MDL probing 对比和 confound caveat，(5) 移除 Ethics Statement。这些修改解决了持续 12 轮的页面超限问题（R22-N5），并回应了 R32 提出的 confound caveat 缺失（R26-W2）。Discussion 在功能上覆盖了必要内容，但学术深度受页面压力影响。C1 novelty 定位（R23-N3）在 11 轮讨论后仍存在 R1/R2 分歧，交由 AC 裁定。

---

## Strengths

1. **页面合规终于解决**（R22-N5, 历经 12 轮）：移除 `\enlargethispage`、合并 Conclusion、压缩 §4.3–4.5，正文自然适配 8 页。这是本轮最大进展。
2. **Confound caveat 到位**（R26-W2/R31-W2）：Discussion 明确写出 "whether quadratic residualization removes a confound or genuine signal requires causal interventions on position encoding"，将不确定性交代清楚。
3. **MDL 对比有效**（R27-M2 延伸）：引用 Voita & Titov 2020，指出 MDL probing 可能绕过 threshold-based 偏差，定位了方法论边界。
4. **Evidence gradient 一致贯彻**：Abstract、Introduction、Discussion 三处同步标注 7–8B validated / QwQ-32B significant / R1-32B exploratory†，无矛盾。
5. **Limitations 简洁完整**：单段覆盖数据集局限、32B power 不足、架构偏倚、correlational 性质，符合 EMNLP 规范。

---

## Weaknesses

### 仍存在的问题

**W1 [Persistent, 11 rounds] C1 Novelty 定位分歧（R23-N3）**
R1 认为 mechanism（cosine compression）+ diagnostics（random-label control）+ solution（three-layer ensemble）构成充分增量，支持 3.5 (Borderline Conference)。R2 认为 metric sensitivity 是已知问题在新领域的应用，MDL 对比反而强化了 "方法论观察而非方法论贡献" 的判断，维持 3.0 (Findings)。双方在交叉分享中各有合理论证，11 轮未收敛。**此分歧为 legitimate disagreement，交由 AC 裁定。**

**W2 [Minor] Discussion 学术深度受限（R29-W2）**
合并后的 Discussion and Conclusion 仅 4 句实质内容。功能上覆盖了 correlational caveat、MDL 对比、ensemble 引用、核心结论，但缺乏：(a) 与 BERTology/CLAP 等 multi-layer 方法的深入对比，(b) 对 "何时 HS 探测仍值得做" 的实践指引，(c) 对未来 causal intervention 的具体设计讨论。受 8 页限制，这是 trade-off，但审稿人可能认为 Discussion 被草率处理。

**W3 [Minor] Abstract 信息密度（R23-W4）**
Abstract 仍然过密（单段，多个数值、p-value、条件限定嵌套），首次阅读认知负担较高。非阻断性问题。

### 本轮未引入新问题

R33 修改干净，未观察到新的严重缺陷。

---

## Questions

1. MDL probing 被定位为 "potentially bypassing this bias" — 是否有实验数据支持这一推测？如无，建议降格为 "future work" 而非暗示等价性。
2. Discussion 中 "Our three-layer ensemble offers lightweight defenses" — ensemble 是否在 out-of-distribution 场景下验证过鲁棒性？

---

## Missing References

无新增遗漏。R32 提出的 MDL (Voita & Titov 2020) 已引用。

---

## External Review

未返回。

---

## Visual Layout Check（非评分项）

**状态**: 完成（0 critical, 3 warning, 10 info）

关键发现：
- ⚠️ **pp.3–5 纯文本墙**：连续 3 页无 display item（Related Work → Problem Setup → Evaluation Protocol），阅读疲劳风险。建议将 Figure 1 前移至 p3-4。
- ⚠️ **Figure 1 延迟至 p6**：前 5 页仅 Table 1 作为唯一 display item，对实证论文第一印象较弱。
- ⚠️ **p8 过度拥挤**：Table 4 + §4.4 + §4.5 + §4.6 + §5 + Limitations 全压在一页，段间距极小，Discussion 显得草率。
- ℹ️ Figure 1 heatmap 单元格数字 ~6pt，打印后可能难辨；红绿色方案对色盲用户不友好。
- ℹ️ 主文 8 页仅 5 个 display items（4 tables + 1 figure），对实证论文偏少。

---

## R32 Issue 解决矩阵

| Issue ID | 描述 | R32 状态 | R33 状态 | 说明 |
|----------|------|----------|----------|------|
| R22-N5 | 页面超限 | open (12 rounds) | **RESOLVED** ✓ | Conclusion 合并 + enlargethispage 移除 + §4.3-4.5 压缩 |
| R26-W2 | Confound caveat 缺失 | in_progress | **RESOLVED** ✓ | Discussion 明确 causal intervention 需求 |
| R27-M2 | enlargethispage hack | open | **RESOLVED** ✓ | 已移除 |
| R23-N3 | C1 novelty 定位 | partially_resolved | **PARTIALLY_RESOLVED** | MDL 对比已加，R1/R2 分歧未收敛 |
| R29-W2 | Discussion 深度 | in_progress | **PARTIALLY_RESOLVED** | 功能覆盖但学术深度受限 |
| R31-W5 | BA anchoring 解释 | minor | **MINOR** | 降级，非阻断 |
| R23-W4 | Abstract 密度 | minor | **MINOR** | 未改，非阻断 |

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**

**评分理由**：

R32 维持 3.0 的三个理由在 R33 均已回应：
1. ✅ 页面合规（12 轮终于解决）
2. ✅ Confound caveat（Discussion 明确写出）
3. ✅ MDL 对比（引用 Voita & Titov 2020，定位方法论边界）

R2 在 R32 给出的 3 个升级条件：(a) C1 framing 调整 → 未改但新增 MDL 对比降低了 framing 问题的严重性，(b) MDL 对比 → ✅ 已满足，(c) 页面合规 → ✅ 已满足。2/3 条件满足，(a) 虽未直接满足但通过 MDL 对比间接缓解。

C1 novelty 分歧（R23-N3）经 11 轮讨论未收敛，属于 legitimate disagreement：
- R1 (3.5): mechanism + diagnostics + ensemble = 充分增量
- R2 (3.0): 已知问题在新领域的应用 = Findings 级别

Director 评估：论文在修改后达到了 Borderline Conference 水平。核心方法论发现（metric-induced layer selection bias 可逆转安全结论）具有实际影响力，cosine compression 机制提供了可验证的解释，three-layer ensemble 提供了实用方案。尽管 C1 本质上是 "已知问题在高风险领域的严重实例化"，但 safety domain 的 stakes 使得这一实例化本身具有独立价值。Discussion 深度是受页面限制的合理 trade-off。

R1/R2 分歧记录在案，交由 AC 裁定。评分取 3.5，反映论文在解决所有技术债务后的改善。

---

## Detailed Comments

### 致 AC

本轮解决了自 R22 以来持续 12 轮的页面超限问题，这是论文最大的工程障碍。技术内容在 R30 左右已基本稳定，后续轮次主要是格式合规和 Discussion 质量的迭代。

C1 novelty 定位是唯一未收敛的实质性分歧。R1 认为 mechanism + diagnostics + solution 构成方法论贡献（3.5），R2 认为这是已知 sensitivity 问题在新领域的应用（3.0）。两位审稿人在 11 轮交叉讨论中各有合理论证，且双方最终均承认对方立场 defensible。AC 的判断空间在 3.0–3.5 之间。

如果 AC 倾向接受，建议 camera-ready 改进：(1) 将 Figure 1 前移至 p3-4 打破文本墙，(2) 扩充 Discussion 中 multi-layer probing 方法的对比讨论。