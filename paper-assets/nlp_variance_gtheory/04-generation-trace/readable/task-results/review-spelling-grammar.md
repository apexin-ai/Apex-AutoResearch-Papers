# review spelling grammar

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_spelling_grammar_20260523T175737_result.json`
- **Structured JSON:** [`81b6a3c45e693fc38094.json`](../../sessions/81/81b6a3c45e693fc38094.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是完整报告。

---

## 论文拼写/语法/术语一致性检查报告

检查范围：`docs/paper/` 下全部 8 个 tex 文件（main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）

---

### 1. 术语一致性问题

#### 1A. "multi-condition" vs "multi-facet" 术语混用 ⚠️

| 位置 | 用法 | 指代 |
|------|------|------|
| `abstract.tex:1` | "multi-condition design" | 推荐的 3p×3s 设计 (178 items) |
| `experiments.tex` 全文 | "multi-facet design" | 完整 1,296-condition 设计 (55 items) |
| `appendix.tex` 表格 | "Multi-facet (2,304 cond.)" | 跨模型完整设计 |

**问题**：Abstract 用 "multi-condition" 指推荐设计，正文用 "multi-facet" 指完整设计。读者可能误认为两者指同一设计。建议 Abstract 统一为 "multi-facet" 或明确标注 "3-prompt × 3-seed"。

#### 1B. $p$ 符号双重含义 ⚠️

- `method.tex:20`：定义 "$p$ = item"（facet 标签）
- `appendix.tex:13`："items with $p \in [0.5, 0.8]$"（item difficulty/概率）
- `appendix.tex` 多处：$p(1-p)$（Bernoulli 方差上界中的概率）

同一符号 $p$ 同时表示 item facet 和 item difficulty。虽然上下文可区分，但容易造成混淆。

#### 1C. 其他术语 ✅ 一致

- **G-theory / G-study / D-study**：全文统一使用连字符形式
- **Henderson Method~I**：全文一致
- **nondeterminism**：全文统一不加连字符（3 处）
- **Benchmark 名称**（MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH）：一致，表格中简写 (Hella.) 合理
- **BF16 / FP16 / FP32**：一致
- **exp-001 / exp-002**：正文中统一小写，表格 caption 句首大写 (Exp-001)，符合英文规范

---

### 2. 硬编码章节号（LaTeX 最佳实践违规）⚠️

文件中同时存在 `\S\ref{}` 和硬编码 `\S X.X` 两种引用方式，重排章节后硬编码引用会失效：

| 位置 | 硬编码引用 | 应改为 |
|------|-----------|--------|
| `method.tex:27` | `(\S3.6)` | `(\S\ref{sec:model_facet})` |
| `method.tex:79` | `\S4.1` | `\S\ref{sec:single_model}` |
| `method.tex:83` | `(\S4.5)` | `(\S\ref{sec:scale_validation})` |

同一文件中 `\S\ref{sec:exp002}`（line 27 末尾）正确使用了 `\ref{}`，说明是遗漏而非风格选择。

---

### 3. 拼写错误 ✅

**未发现拼写错误。** 检查了全部正文文本，包括：
- 常见误拼模式（teh, adn, benchamrk, evalution, reproducability, generalizabilty, decompostion, methodolgy, temperture 等）均无命中
- 专业术语（generalizability, reproducibility, decomposition, differential, psychometric, nondeterminism 等）拼写正确

---

### 4. 语法问题 ✅

- **冠词 a/an**：未发现错误（无 "a ANOVA"、"a MMLU"、"an Henderson" 等）
- **主谓一致**：正确
- **Oxford comma**：全文一致使用
- **"tradeoff"**：仅 abstract 出现一次，无 "trade-off" 变体，保持一致

---

### 5. 连字符/大小写一致性 ✅

全文一致使用以下形式，无不一致：
- `open-weight`（连字符）
- `instruction-tuned`（连字符）
- `item-level`（作形容词时连字符）
- `cross-model`（连字符）
- `single-condition`（连字符）
- `format-associated`（连字符）
- `multi-facet`（连字符）
- `quasi-random`（连字符）

---

### 6. 其他发现

#### 6A. Table 1 温度 level 与 record count 不一致 ⚠️

Table 1 exp-001 列显示 Temperature = **3** levels，但 Total records = **460,800**†。按 3 temps 计算应为 691,200 (8×200×6×6×3×4)。实际 460,800 = 8×200×6×6×**2**×4。

`method.tex:29` 的 Sample sizes 段落明确写了 "2 temperatures"，与 Table 1 的 "3" 矛盾。虽然脚注说明是 "BF16 balanced subset for cross-model analysis"，但未解释 temperature 从 3 降为 2 的原因。读者验算时会发现数字对不上。

**建议**：在 Table 1 加注说明 cross-model subset 使用 2 个 temperature level，或将 Total records 改为完整 exp-001 的记录数。

#### 6B. Abstract word count ✅

约 155 词，远低于 200 词限制。

---

### 总结

| 类别 | 状态 | 数量 |
|------|------|------|
| 术语一致性 | ⚠️ 需注意 | 2 项（multi-condition/multi-facet 混用、$p$ 双重含义） |
| 硬编码章节号 | ⚠️ 应修复 | 3 处 |
| 拼写错误 | ✅ 无 | 0 |
| 语法错误 | ✅ 无 | 0 |
| 连字符/大小写 | ✅ 一致 | 0 |
| 表格数据一致性 | ⚠️ 需澄清 | 1 处（Table 1 温度 levels） |

最需要修复的是 3 处硬编码章节号（简单的 find-replace）和 abstract 中 "multi-condition" 与正文 "multi-facet" 的术语统一。

---
