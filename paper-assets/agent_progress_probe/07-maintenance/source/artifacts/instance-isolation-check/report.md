# Instance Isolation — 论文 Patch 状态检查报告

## 1. 论文中 Instance Isolation 相关内容位置

### 位置 A: `analysis.tex` 第 14 行（主文正文）
circularity defense 段落中，作为三个 non-circular validation 之一：

> Second, instance isolation: removing 284 SWE-bench task instances (8.3\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by <0.1 pp (Table~\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.

### 位置 B: `appendix.tex` 第 147–165 行（附录表格）
`\subsection{Instance Isolation}` + `Table: instance_isolation`

| Model | Full | Unseen-only | Δ |
|-------|------|-------------|---|
| GB all | 0.9674 | 0.9669 | −0.05 pp |
| RF all | 0.9123 | 0.9121 | −0.01 pp |
| GB conf≥2 | 0.9919 | 0.9917 | −0.02 pp |
| RF conf≥2 | 0.9959 | 0.9962 | +0.03 pp |

Caption: "...284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3% of OH). All |Δ| < 0.1 pp..."

## 2. 数据一致性评估

| 数据项 | Registry Canonical | 论文 (analysis.tex) | 论文 (appendix.tex) | 一致? |
|--------|-------------------|--------------------|--------------------|-------|
| SWE train instances | 1,386 | — | 1,386 | ✅ |
| OH instances | 3,409 | — | 3,409 | ✅ |
| Overlap count | 284 | 284 | 284 | ✅ |
| Overlap % | 8.3% | 8.3% | 8.3% | ✅ |
| GB all full | 0.9674 | — | 0.9674 | ✅ |
| RF all full | 0.9123 | — | 0.9123 | ✅ |
| GB conf≥2 full | 0.9919 | — | 0.9919 | ✅ |
| RF conf≥2 full | 0.9959 | — | 0.9959 | ✅ |
| GB all unseen | 0.9669 | — | 0.9669 | ✅ |
| RF all unseen | 0.9121 | — | 0.9121 | ✅ |
| GB conf≥2 unseen | 0.9917 | — | 0.9917 | ✅ |
| RF conf≥2 unseen | 0.9962 | — | 0.9962 | ✅ |
| Delta claim | <0.1 pp | <0.1 pp | <0.1 pp | ✅ |

## 3. 旧版数据残留检查

搜索 `356` 和 `10.4` — **未发现任何旧版数据残留**。

## 4. 结论

**状态: ✅ 完全一致，无需修改。**

- 论文已有专门段落（analysis.tex 正文 + appendix 表格）讨论 instance isolation
- 所有数据点与 registry canonical 版本完全匹配
- 无旧版数据残留
- 正文引用附录表格的交叉引用 (`Table~\ref{tab:instance_isolation}`) 正确设置
