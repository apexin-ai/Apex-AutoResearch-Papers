# review reference audit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_reference_audit_20260523T173713_result.json`
- **Structured JSON:** [`9101beae4a1e55406c90.json`](../../sessions/91/9101beae4a1e55406c90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已读取完毕，开始交叉分析。

---

## Reference 审计报告

### 1. 总量统计

| 指标 | 数量 |
|------|------|
| 正文 unique cite keys | **59** |
| Bib 条目数 | **59** |

### 2. Undefined Citations（正文 cite 了但 bib 没有）

**0 个。** 所有正文引用均有对应 bib 条目。

### 3. Unused Bib Entries（bib 有但未 cite）

**0 个。** 所有 bib 条目均在正文中被引用。

### 4. 重复条目

**0 个。**

### 5. 不完整条目

所有条目均具备 author（或 editor）、title、year、venue 四个基本字段。**无缺失。**

### 6. Key-Metadata 不一致（需关注）

| 条目 key | 问题 | 详情 |
|----------|------|------|
| `wei2025gtheory` | **Key 与首作者不符** | Key 暗示首作者 "Wei"，实际首作者是 **Song, Dan**。应为 `song2025gtheory` |
| `varannot2025gtheory` | **Key 年份与实际年份不符** | Key 写 `2025`，但 year 字段为 **2026**，arXiv ID `2601` 确认为 2026 年 1 月发表 |

### 7. 格式一致性问题

#### 7a. `and others` 缩写（3 处）
以下条目用 `and others` 代替完整作者列表，与其余 56 条目（列出全部作者）不一致：
- `qian2026benchmark` — `Qian, Qi and Huang, Chengsong and Xu, Jingwen and others`
- `burnell2023rethink` — `Burnell, Ryan and Schellaert, Wout and Burden, John and others`
- `liang2023helm` — `Liang, Percy and ... and Kumar, Ananya and others`

#### 7b. 缺少 `url` 字段（3 处）
大部分条目都有 `url`，以下三个没有：
- `qian2026benchmark`
- `liang2023helm`
- `kiela2021dynabench`

#### 7c. `brittlebench2026` key 格式
该 key 未包含首作者姓名（其他所有条目均以 `lastname+year` 命名），虽不影响编译但风格不统一。首作者是 Romanou，建议改为 `romanou2026brittlebench`。

### 8. 总结

| 类别 | 数量 |
|------|------|
| Undefined citations | 0 |
| Unused entries | 0 |
| 重复条目 | 0 |
| 缺必要字段 | 0 |
| Key-metadata 不一致 | **2** (`wei2025gtheory`, `varannot2025gtheory`) |
| `and others` 缩写不一致 | **3** |
| 缺 url | **3** |
| Key 命名风格不一致 | **1** (`brittlebench2026`) |

整体引用质量良好，无编译阻断性问题。主要建议修正 2 个 key-metadata 不一致项（`wei2025gtheory` → `song2025gtheory`，`varannot2025gtheory` → `varannot2026gtheory`）和补全 3 个 `and others` 的完整作者列表。

---
