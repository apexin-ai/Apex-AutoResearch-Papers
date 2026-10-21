# 论文全文一致性检查报告

检查时间: 2026-05-18
论文路径: `docs/paper/`

## 1. 数值一致性

**总计: 155 个数值, 135 匹配, 9 不匹配, 11 未找到 registry 记录**

### 不匹配项

| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |
|---|---|---|---|
| introduction.tex:18 | L1: 24 heads | `l1_heads_gt50pct.trained` = **25** | ❌ 不匹配 |
| experiments.tex:12 | N = 63,228 | `lg_dino_extract.total_frames` = **63,728** | ❌ 不匹配 |
| experiments.tex:40 | L8 untrained readout: 95.5% | `dense_probe_L8_acc` untrained = **98.6%** | ❌ 不匹配 |
| experiments.tex:41 | L16 untrained readout: 91.1% | `dense_probe_L16_acc` untrained = **92.0%** | ❌ 不匹配 |
| experiments.tex:52 | VLA 24/32 heads (57.7%) | registry = **25/32** | ❌ 不匹配 |
| experiments.tex:91 | VLA: 24/32 heads | registry = **25/32** | ❌ 不匹配 |
| discussion.tex:8 | 0 → 9 → 24 heads | registry = 0, 9, **25** | ❌ 不匹配 |
| discussion.tex:13 | p = 0.002 (bootstrap CIs) | `task_paired_t.p` = **0.0018** | ❌ 不匹配 (rounding imprecise) |
| discussion.tex:18 | bottom-24 d = 0.57 | `bottom24_d` = **0.565** | ❌ 不匹配 (borderline rounding) |

### 分析

1. **L1 heads 24 vs 25** — 系统性问题，出现 4 次 (introduction, experiments×2, discussion)。需确认 50% 阈值下的正确 head 数量并全文统一。
2. **N = 63,228 vs 63,728** — 500 帧差异，需核实数据提取记录。
3. **Untrained readout L8/L16** — 论文 95.5%/91.1% vs registry 98.6%/92.0%。可能来自不同 probe run，appendix Table `tab:dense_routing` 与正文一致 (95.5%)，但与 registry 不一致。需确认哪个是最终结果。
4. **p = 0.002 vs 0.0018** — 精度损失。建议用准确值 0.0018 或写 "p < 0.002"。
5. **bottom-24 d = 0.57 vs 0.565** — 四舍五入边界。appendix 用 0.565，discussion 用 0.57。建议统一精度。

### 未找到 registry 记录 (11 项)

主要来自 appendix 中的 robustness 分析 (OOD diagnostics, permutation tests, per-DOF RSA, metric invariance) 和 Llama-2 base mid-depth attention profile，可能是本地计算未录入 registry。

---

## 2. 措辞问题

**总计: 8 处需修改**

### 残留强 claim (4 处)

| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |
|---|---|---|---|
| abstract.tex:4 | "the readout token serves as the **sole** multimodal convergence point" | 残留强claim | → "the **primary** multimodal convergence point" |
| related_work.tex:25 | "identify the readout token as the **sole** multimodal integration site" | 残留强claim | → "the **primary** multimodal integration site" |
| related_work.tex:29 | "the readout token serves as the **exclusive** multimodal hub" | 残留强claim | → "the **primary** multimodal hub" |
| experiments.tex:26 | "The readout is thus the **sole** locus of multimodal integration" | 残留强claim | → "the **primary** locus of multimodal integration" |

### AI 写作标志 — -ing 分词句尾 (4 处)

| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |
|---|---|---|---|
| conclusion.tex:4 | "...revealing that VLA fine-tuning primarily reorganizes..." | AI写作-ing | 拆为两句: "...VLA representations. The analysis reveals that..." |
| appendix.tex:72 | "...indicating stable but unspecialized processing." | AI写作-ing | → "). This indicates stable but unspecialized processing." |
| appendix.tex:461 | "...indicating that deep-layer stability derives from..." | AI写作-ing | → "; this indicates that deep-layer stability..." |
| appendix.tex:620 | "...indicating instruction-dominant heads have disproportionate influence..." | AI写作-ing | → "; instruction-dominant heads thus have disproportionate..." |

### 已清理确认 (无问题)

- em-dash (—): **0** 处
- 解释性 en-dash ( – ): **0** 处
- "Furthermore"/"Moreover"/"Additionally" 序列: **0** 处
- "It is worth noting"/"Notably": **0** 处
- 黑名单用词 (delve/leverage/utilize/facilitate/myriad/plethora): **0** 处
- "uniquely responsible"/"exclusively"/"solely driven"/"only instruction heads": **0** 处

### 新叙事关键词确认

| 关键词 | 出现位置 |
|---|---|
| "graded" | appendix.tex:676 ("graded, attention-ordered contribution to routing") |
| "distributed" | method.tex:4 ("how action-relevant structure is distributed across a VLA") |
| "primarily" | conclusion.tex:4, discussion.tex:5, appendix.tex:432 |
| "the primary" | abstract.tex:8, introduction.tex:21, introduction.tex:23, conclusion.tex:5 |

**注**: "preferentially" 和 "predominantly" 未出现，当前叙事依赖 "primarily"/"the primary"，用词略单一。

---

## 3. 交叉引用

**总 labels: 89 | 总 unique refs: 53 | 总 bib 条目: 46**

### 孤立 \label (defined but never referenced)

**附录 figure labels (5 个, 应修复):**
- appendix.tex:63 — `\label{fig:rsa_perlayer_curve}`
- appendix.tex:95 — `\label{fig:random_subset_ablation}`
- appendix.tex:210 — `\label{fig:ood_diagnostics}`
- appendix.tex:227 — `\label{fig:linear_vs_mlp}`
- appendix.tex:545 — `\label{fig:multilayer_attention}`

**附录 section labels (22 个):** 附录 subsection labels 未被引用，部分可能需要在正文添加 "see Appendix~\ref{...}" 引用。

**主文 section labels (9 个):** section labels 未被 `\ref` 引用属正常行为。

### 悬空 \ref (referenced but never defined)
无。

### 缺失 \cite (cited but not in .bib)
无。

### 未使用 bib 条目
0 条。全部 46 个 bib 条目均被引用。

### 其他问题
- 重复 labels: 无
- 缺失 `~\ref`: 无 (全部使用了非断空格)

---

## 4. 编译结果

### 编译环境
- Tool: `latexmk -pdf` (pdfTeX 3.141592653, TeX Live 2025)
- Location: local
- Output: `main.pdf` (26 pages, 555 KB)

### Errors: 0

### Warnings: 30

| 类型 | 数量 | 说明 |
|---|---|---|
| Float specifier `[h]` → `[ht]` | 17 | 全在 appendix.tex，改为 `[htbp]` 即可消除 |
| Underfull hbox | 3 | bibliography URL 断行，可用 `\url{}` 缓解 |
| Underfull vbox | 7 | 浮动体页面分布导致，排版调优问题 |
| Hyperref token | 3 | appendix.tex:638 section 标题含 `$R^2$`，用 `\texorpdfstring{$R^2$}{R2}` 修复 |

---

## 总结

| 检查项 | 问题数 | 严重程度 |
|---|---|---|
| 数值不匹配 | **9** 处 | 🔴 高 (其中 L1 heads 24→25 出现 4 次为系统性错误) |
| 残留强 claim | **4** 处 | 🟡 中 ("sole"/"exclusive" 与 graded routing 叙事矛盾) |
| AI 写作标志 | **4** 处 | 🟢 低 (-ing 分词句尾，仅 appendix 和 conclusion) |
| 孤立 figure labels | **5** 处 | 🟡 中 (appendix 图未被引用，违反 CLAUDE.md §1.1 "附录内容必须在正文中有明确引用") |
| 编译 warnings | **30** 处 | 🟢 低 (无 error，warnings 均为排版调优) |
| 悬空 ref / 缺失 cite | **0** 处 | ✅ 无问题 |
