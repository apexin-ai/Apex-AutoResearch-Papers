# paper latex compile check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_latex-compile-check_20260519T171006_result.json`
- **Structured JSON:** [`107f94d5c4c4f087d2b6.json`](../../sessions/10/107f94d5c4c4f087d2b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。汇总报告：

---

## 编译 & 一致性检查报告

### 1. 编译状态：成功

- **输出**: `main.pdf`, 8 pages, 255KB
- **Errors**: 0
- **Warnings**: 0（无 LaTeX Warning）
- **Overfull hbox**: 1 处（experiments.tex L22-33, 4.65pt — 低于 5pt 阈值，忽略）
- **Underfull**: 多处 underfull hbox/vbox，均为常见排版松散提示，无害

### 2. 引用检查

| 检查项 | 结果 |
|--------|------|
| `\ref{}` / `\S\ref{}` 无对应 `\label{}` | 0 个，全部匹配 |
| `\cite{}` 无对应 bib 条目 | 0 个，全部匹配 |
| bib 条目未被引用 | 0 个 |
| `\label{}` 未被引用 | 8 个（见下） |

**未引用的 label**（定义了但全文无 `\ref` 或 `\S\ref` 指向）：
- 4 个顶层 section label：`sec:intro`, `sec:method`, `sec:experiments`, `sec:related` — 通过子节 label 引用，无需修复
- 4 个 subsection label：`subsec:setup`, `subsec:cross_scale`, `subsec:alt_ews`, `subsec:second_order` — 未被任何交叉引用，可保留或清理

### 3. 数据一致性

**r_crit bound — 全文统一为 $(0.25, 0.3]$** ：
| 位置 | 表述 | 一致？ |
|------|------|--------|
| Abstract L7 | $(0.25, 0.3]$ | ✓ |
| Method L41 | $0.25 < r_{\text{crit}} \leq 0.3$ | ✓ |
| Experiments L139 | $0.25 < r_{\text{crit}} \leq 0.3$ | ✓ |
| Conclusion L4 | $r_{\text{crit}} \in (0.25, 0.3]$ | ✓ |

**残留 "(0.2, 0.25]" 表述**: 无，已清理干净。

**关键数字交叉验证**：
| 指标 | Abstract | Conclusion | Experiments | 一致？ |
|------|----------|------------|-------------|--------|
| 加速倍率 | 2.43× | 2.43× | 2.43× (L56) | ✓ |
| 三阶段结构 | Gen 0-2, 2-4, 4-10 | 一致 | 一致 | ✓ |
| SLV Gen10 (r=0.5) | — | — | 2572, +8.7% (L68,135) | ✓ |
| SLV Gen10 (r=0.3) | — | — | 2511.1, +6.1% (L138) | ✓ |

**注意**: Experiments L72 出现 "$0.2 < r_{\text{crit}} \leq 0.5$" 是 §4.4 的初始宽界，在 §4.5 L139 被收紧为 $(0.25, 0.3]$ — 叙事逻辑正确，非不一致。

### 4. 页数统计

| 内容 | 页数 |
|------|------|
| 主文本 (Abstract → Conclusion + Limitations) | **6 页** |
| References | 2 页 |
| 合计 | 8 页 |

**结论**: 主文本 6 页，远低于 EMNLP 2026 的 8 页限制。

---

**备注**: `sections/limitations.tex` 文件存在但未被 `main.tex` 引入，limitations 作为 `\paragraph` 嵌入在 conclusion.tex 末尾。EMNLP 通常要求 limitations 作为独立 section — 如需合规可单独拆出。

---
