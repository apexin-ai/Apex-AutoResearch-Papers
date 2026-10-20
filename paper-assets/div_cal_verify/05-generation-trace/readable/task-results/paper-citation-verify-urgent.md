# paper citation verify urgent

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation_verify_urgent_20260514T082255_result.json`
- **Structured JSON:** [`86b0fd4a9467b72b8a08.json`](../../sessions/86/86b0fd4a9467b72b8a08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修复完成。以下是结构化审计报告：

## 引用审计报告

**总数**: 43 条
**已验证**: 43 条（全部通过 WebSearch 或 OpenAlex 确认真实存在）
**问题**: 4 条（已全部修复）
**Orphan（bib 有但未引用）**: 0 条
**Missing（引用了但 bib 无）**: 0 条

### 修复记录

| # | 条目 | 问题 | 修复方式 |
|---|------|------|----------|
| 1 | `dohmatob2025strong` | author 字段含非法 "Others" | 补全为 `Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia` |
| 2 | `garrido2023rankme` | 标题错误 + 会议错误（写成 ICLR，实为 ICML） | 标题更正为 "...of Pretrained Self-Supervised Representations by Their Rank"，venue 改为 ICML |
| 3 | `laurent2024feature` | — | WebSearch 确认标题 "Feature Collapse" 和 ICLR 2024 均正确，无需修改 |
| 4 | `karwowski2024goodhart` | — | WebSearch 确认 ICLR 2024 收录，条目正确，无需修改 |

### 新增引用

| 条目 | 说明 |
|------|------|
| `dohmatob2024tale` | "A Tale of Tails: Model Collapse as a Change of Scaling Laws", ICML 2024. 已添加到 `references.bib` 并在 `related_work.tex` §2.1 引用 |

### OpenAlex API 误报（无需修复）

- `jing2022understanding` — API 将 "Jing, Li"（姓 Jing 名 Li）误解析为 first_author=li，bib 正确
- `alemohammad2024self` — API 返回 first_author=casco-rodriguez，实际第一作者确认为 Alemohammad，bib 正确
- `liu2024selectit` — API 混淆 "Liu, Liangxin" 的姓名顺序，bib 正确

---
