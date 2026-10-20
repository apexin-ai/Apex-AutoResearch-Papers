# audit bib verification

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bib_verification_20260514T022152_result.json`
- **Structured JSON:** [`dd8abd276f3318852e49.json`](../../sessions/dd/dd8abd276f3318852e49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修复已完成。验证报告如下：

---

## 验证报告

### 4 篇可疑引用

| # | bib key | 状态 | 问题 & 修复 |
|---|---------|------|------------|
| 1 | `shi2025generalization` | ✅ **真实** | arXiv:2509.16499 存在，NeurIPS 2025 Spotlight 确认。**作者 first name 全错**（LLM 幻觉）：Shiliang→Lianghe, Qiong→Meng, Zhen→Huijie, Jing→Zekai, Dacheng→Molei, Xiangyang→Qing。已修正。 |
| 2 | `basani2026diveye` | ✅ **真实** | arXiv:2509.18880 存在，TMLR 2026 (02/2026) 确认。**作者 first name 全错**：Yash→Advik Raj, Liyan→Pin-Yu。已修正。 |
| 3 | `zawalski2026codec` | ✅ **真实** | arXiv:2510.27055 存在，ICLR 2026 确认（OpenReview）。**作者名错且不完整**：Kacper→Michał，补全为 Zawalski/Boubdir/Bałazy/Nushi/Ribalta。已修正。 |
| 4 | `gambetta2025surplexity` | ✅ **真实** | arXiv:2410.12341 存在（v1 标题不同，当前版本标题匹配）。**作者名错且不完整**：Lorenzo→Daniele，补全 6 位作者。已修正。 |

### bib 格式修复

| # | 修复项 | 操作 |
|---|--------|------|
| 5 | `amin2025escaping` 作者补全 | `{others}` → 完整 6 人列表（Amin/Babakniya/Bie/Kong/Syed/Vassilvitskii） |
| 6 | `tirumala2024d4` key 年份不一致 | key 改为 `tirumala2023d4`，同步更新 `related_work.tex` + `introduction.tex` 中的 `\cite{}` |
| 7 | `xie2024doremi` key 年份不一致 | key 改为 `xie2023doremi`，同步更新 `related_work.tex` + `introduction.tex` 中的 `\cite{}` |
| 8 | PENDING 标记 | 删除 "PENDING formal verification" 注释，替换为 "verified 2026-05-14" |

### 关键发现

所有 4 篇论文均为真实存在的论文，arXiv ID、标题、venue 基本正确。但 **6 个 bib 条目的作者 first name 被 LLM 系统性地幻觉**（last name 正确但 first name 全部伪造）。这是典型的 LLM 引用生成问题——它能找到正确的论文但编造具体的名字细节。

重新编译 LaTeX 即可更新 `.bbl`/`.aux`。

---
