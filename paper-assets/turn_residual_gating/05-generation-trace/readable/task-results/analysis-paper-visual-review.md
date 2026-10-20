# analysis paper visual review

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_visual_review_20260522T043006_result.json`
- **Structured JSON:** [`1bbf283a80215edeacee.json`](../../sessions/1b/1bbf283a80215edeacee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 论文视觉审查报告

**总页数：10页 | 主体内容：8页 | EMNLP 2026 合规：✅ 通过**

（主体内容 §1–§7 结束于第8页底部，Limitations + References + Appendix 从第9页开始，不计入8页限制）

---

### 第1页 — Title / Abstract / §1 Introduction

| 严重程度 | 问题 |
|--------|------|
| **info** | Abstract 篇幅较长，约占 1/3 栏宽，在 ACL 模板允许范围内 |

- 标题、作者匿名标记、双栏排版均正常
- 无 text overflow，字体一致，margin 正常

---

### 第2页 — Figure 1 + Introduction 续

| 严重程度 | 问题 |
|--------|------|
| **warning** | Figure 1 信息密度极高，内部文字（如 box 内标注、箭头旁说明文字）在打印尺寸下偏小，可能影响可读性 |

- Figure 1 跨双栏，caption 完整，编号正确
- 三段式结构（Observation → Intervention → Result & Root Cause）颜色区分清晰（橙/绿/蓝/红）

---

### 第3页 — §2 Related Work

无问题。纯文本页面，小节划分清晰，无 overflow，无 orphan/widow lines。

---

### 第4页 — §3 Method

无问题。

- 公式 (1)–(7) 渲染正确，编号对齐
- 数学符号无乱码
- 小节标题层级正常

---

### 第5页 — §4 Experiments / §4.2 Main Results + Figure 2

| 严重程度 | 问题 |
|--------|------|
| **info** | Figure 2 图例线型较多（5条线），但颜色和线型区分充分，可读 |

- Figure 2 caption 完整，编号正确
- 坐标轴标签可读

---

### 第6页 — Table 1 + Figure 3 + Figure 4

| 严重程度 | 问题 |
|--------|------|
| **warning** | 本页视觉密度极高：1个跨栏表格 + 2个图（Figure 3 含2子图，Figure 4 含2子图），共挤在一页。Figure 3 和 Figure 4 的坐标轴标签和图例文字偏小 |
| **info** | Table 1 数据对齐正确，caption 完整，列标题清晰 |

- Table 1：IID / Held-out 两组指标分组清晰，数值对齐
- Figure 3：bar chart + line plot 双子图，虚线 baseline 标注在 caption 中
- Figure 4 (a)(b)：多线对比图，线型可区分但图例字号小

---

### 第7页 — Figure 5 + §5.2–§5.4

| 严重程度 | 问题 |
|--------|------|
| **info** | Figure 5 两个子图 (a)(b) 尺寸适中，散点可辨识 |

- Figure 5 caption 完整，编号正确
- 正文段落排版正常

---

### 第8页 — §5.5 Cross-Model Generality / §6 Discussion / §7 Conclusion

无问题。

- Conclusion 结束于本页底部，主体内容恰好 8 页
- 无 orphan lines，段落衔接自然

---

### 第9页 — §8 Limitations / References 开始

| 严重程度 | 问题 |
|--------|------|
| **info** | Limitations 约1段，覆盖 5 个要点（单种子验证、单损失类型、模型家族覆盖有限、未复现所有 ablation、未测交互效应），篇幅合理 |

- References 采用 ACL natbib 格式，格式一致

---

### 第10页 — References 续 / Appendix A & B

| 严重程度 | 问题 |
|--------|------|
| **info** | Table 2 (Loss Formulation Search) 使用 ✓/— 标记状态列，数据清晰 |

- Appendix A (Training Hyperparameters) 和 B (Loss Formulation Search) 排版正常
- Table 2 caption 完整，编号正确

---

### 总结

| 类别 | 数量 |
|------|------|
| Critical | 0 |
| Warning | 2 |
| Info | 5 |

**2个 Warning：**
1. **P2 Figure 1**：框架概览图信息密度高，内部标注文字偏小，建议检查打印/PDF 100% 缩放下是否可读
2. **P6 整页**：Table 1 + Figure 3 + Figure 4 同页堆叠，图表文字偏小。如有空间，考虑将一个图移至下页

无 critical 问题。公式渲染正确，所有图表均有 caption 和编号，无 text overflow，字体一致，页数合规。

---
