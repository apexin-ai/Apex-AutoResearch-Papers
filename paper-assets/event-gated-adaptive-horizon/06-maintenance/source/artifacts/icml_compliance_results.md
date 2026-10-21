# ICML 2026 合规检查报告

**项目**: event-gated-adaptive-horizon
**论文**: Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3
**检查日期**: 2026-05-24
**PDF 总页数**: 24

---

## 1. 模板确认

✅ **通过**

- `main.tex` 使用 `\usepackage{icml2026}`
- 参考文献样式使用 `\bibliographystyle{icml2026}`
- `icml2026.sty` 和 `icml2026.bst` 均存在于 paper/ 目录

---

## 2. Broader Impact Statement 位置

✅ **通过**

- `\section*{Broader Impact Statement}` 存在于 `sections/conclusion.tex` 末尾
- 在 `main.tex` 中，`\input{sections/conclusion}`（含 Impact Statement）在 `\bibliography{references}` **之前**
- PDF 中 Impact Statement 位于第 6 页，References 从第 7 页开始

---

## 3. 页数限制（正文 ≤ 8 页）

✅ **通过**

- 正文（Introduction 至 Conclusion + Broader Impact）: **6 页**（第 1-6 页）
- References: 第 7 页起
- Appendix: 第 8-24 页
- 远低于 8 页限制

**正文章节分布**:
| 页码 | 内容 |
|------|------|
| 1 | Title, Abstract, Introduction |
| 2 | Related Work |
| 3 | Experimental Setup |
| 4-5 | Results |
| 6 | Discussion, Conclusion, Broader Impact Statement |

---

## 4. 匿名化检查

✅ **通过**

- **作者信息**: `\icmlauthor{Anonymous Authors}{anon}` + `\icmlaffiliation{anon}{Anonymous Institution}` ✅
- **代码声明**: "Code: upon acceptance." ✅（conclusion.tex）
- **机构名称**: 正文、方法、附录中均未出现可识别的机构名
- **"our group/lab/team" 等短语**: 未发现
- **个人网站**: 未发现

**外部 URL**:
- `\url{https://github.com/danijar/dreamerv3}` — methodology.tex 脚注中引用 DreamerV3 **官方公开仓库**，属于引用现有工作，非作者自有代码，**不构成匿名化违规**

---

## 5. 图表规范

⚠️ **部分需修复**

### 5.1 Caption 和 Label

✅ 所有 figure 和 table 均有 `\caption{}` 和 `\label{}`

**正文**: 2 figures, 2 tables — 全部有 caption + label
**附录**: 8 figures, 20 tables — 全部有 caption + label

### 5.2 正文引用检查

⚠️ **3 个 figure 未在正文中被 `\ref{}` 引用**:

| Label | 位置 | Caption 摘要 |
|-------|------|-------------|
| `fig:factorial_grid` | appendix.tex:385 | Factorial design 可视化 |
| `fig:entropy_dynamics` | appendix.tex:584 | Actor entropy trajectories |
| `fig:gradient_decomp` | appendix.tex:525 | Gradient contribution to $e_{\Delta t}$ |

这三个 figure 定义了 `\label{}` 但全文无 `\ref{}` 引用。建议在对应的 appendix 段落中添加 `Figure~\ref{fig:...}` 引用，或确认是否为孤立图表。

所有 table 均被引用。

---

## 6. Appendix 内部一致性

✅ **通过**

关键数值跨文件一致性检查:

| 数值 | 出现位置 | 是否一致 |
|------|---------|---------|
| Reward prediction gap 2.78× | Intro, Results, Discussion, Appendix | ✅ |
| NVE ≥ 1.5× 分类 27/30 | Intro, Methodology, Results, Conclusion | ✅ |
| AUROC = 0.957 (in-sample) | Intro, Methodology, Results, Discussion, Appendix | ✅ |
| LOEO AUROC = 0.988 | Intro, Appendix | ✅ |
| Dual critic ρ > 0.999 | Results, Conclusion, Appendix | ✅ |
| Baseline 915.7 @105K | Results (Table 1), Appendix (Table 3) | ✅ |
| SGS eval 448.3 / NVE 1.66× | Defined as `\sgseval` / `\sgsnve` macros，全局一致 | ✅ |

未发现正文与附录之间的数值矛盾或重复段落。

---

## 总结

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 1. 模板 | ✅ 通过 | icml2026.sty |
| 2. Impact Statement 位置 | ✅ 通过 | References 之前 |
| 3. 页数限制 | ✅ 通过 | 6/8 页 |
| 4. 匿名化 | ✅ 通过 | 无泄露 |
| 5. 图表规范 | ⚠️ 需修复 | 3 个 appendix figure 未被引用 |
| 6. Appendix 一致性 | ✅ 通过 | 数值一致 |

**需修复项（1 项）**:
- 在 appendix 中为 `fig:factorial_grid`、`fig:entropy_dynamics`、`fig:gradient_decomp` 添加 `Figure~\ref{...}` 引用
