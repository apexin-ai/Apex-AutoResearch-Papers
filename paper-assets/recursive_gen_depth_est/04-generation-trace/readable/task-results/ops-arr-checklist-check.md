# ops arr checklist check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_arr-checklist-check_20260518T075448_result.json`
- **Structured JSON:** [`ebb8a99351dd19e0123b.json`](../../sessions/eb/ebb8a99351dd19e0123b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed. Here's the full report:

---

## ARR / EMNLP 2026 投稿检查报告

### 任务 1: ARR Responsible NLP Checklist 必填项

Checklist 在 OpenReview 上以表单填写，非论文内嵌。各 section 问题：

| Section | 问题 | 适用性 |
|---------|------|--------|
| **A1** | 是否描述了工作的 limitations？ | 必填 |
| **A2** | 是否讨论了潜在风险？ | 必填 |
| **B1** | 是否引用了所用 artifacts 的创建者？ | 有 artifacts 则必填 |
| **B2** | 是否讨论了 license/使用条款？ | 有 artifacts 则必填 |
| **B3** | 是否讨论了使用方式与 intended use 的一致性？ | 有 artifacts 则必填 |
| **B4** | 是否检查了数据中的个人信息/冒犯内容？ | 有数据则必填 |
| **B5** | 是否提供了 artifacts 文档（domain/language 覆盖等）？ | 有 artifacts 则必填 |
| **B6** | 是否报告了数据相关统计（样本数、train/test split 等）？ | 有数据则必填 |
| **C1** | 是否报告了模型参数量、计算预算、基础设施？ | 有实验则必填 |
| **C2** | 是否描述了实验设置（超参搜索、最佳超参值）？ | 有实验则必填 |
| **C3** | 是否报告了结果的描述性统计（error bars 等）？ | 有实验则必填 |
| **C4** | 是否报告了所用现有 package 的实现细节？ | 有外部包则必填 |
| **D1-D5** | 人类标注/参与者相关 | 本文不涉及 |
| **E1** | 是否披露了 AI assistant 使用情况？ | 如使用则必填 |

---

### 任务 2: 论文内容逐项检查

#### 1. Ethics Statement
**✅ 通过** — `conclusion.tex:57-62`，包含：使用的公开模型列表、无人类受试者、无私人数据、方法意图说明、潜在误用风险讨论、代码发布承诺。内容充实。

#### 2. Broader Impact Statement
**⚠️ 不强制但建议** — ARR/EMNLP 不单独要求 Broader Impact section（checklist A2 覆盖）。Ethics Statement 中已讨论了误用风险。Appendix `section_appendix.tex:653-667` 的 Extended Discussion 中有 "depth-graduated curation" 和 "provenance toolkit" 讨论，隐含了积极影响。满足 A2 要求。

#### 3. Reproducibility Statement
**❌ 缺失** — 无单独的 Reproducibility section。论文正文中散布了超参数（`method.tex:33`: LoRA r=16, α=32, lr 2e-4, batch 8, 3 epochs）、数据规模（180K samples）、RF 配置（200 trees）等，但未集中说明：
- **缺少**：总计算预算（GPU hours）、使用的硬件型号（checklist C1）
- **缺少**：超参搜索策略说明（checklist C2 要求说明是否做了 hyperparameter search）
- **缺少**：代码框架/库版本（scikit-learn 版本、transformers 版本等，checklist C4）

**建议**：在 Appendix 或 Ethics Statement 后添加简短的 Reproducibility paragraph。

#### 4. Limitations Section
**✅ 通过** — `conclusion.tex:1-56`，共 10 个 paragraph，覆盖面广：cross-strategy 约束、strategy-unknown 部署、d0 inflation、controlled vs ecological 设定、domain FPR、adversarial robustness、EDD monotonicity、reference model 依赖、single LoRA、passage length/domain shift。非常充实。

#### 5. 匿名化
**✅ 通过** — 
- `main.tex:24`: `\author{Anonymous}`
- `\usepackage[review]{acl}` 自动启用匿名化
- 全文 grep 未发现作者姓名、机构名、GitHub URL（`acl.sty` 内的 github URL 是样式文件本身，不影响）
- `conclusion.tex:62` "Code and data will be released upon acceptance" — 标准匿名表述，合规

#### 6. 行号
**✅ 通过** — `main.tex:4`: `\usepackage[review]{acl}`，`acl.sty:19` 确认 `review` 选项启用 `\acl@linenumberstrue`，自动加载 `lineno` 包并在 `\begin{document}` 时调用 `\linenumbers`。

#### 7. 页数
**⚠️ 需要编译确认** — 粗略估计正文内容（Abstract → Discussion/Conclusion, 不含 Limitations/Ethics/References/Appendix）：

| Section | 估计页数 |
|---------|---------|
| Abstract | ~0.3 |
| Introduction | ~1.3 |
| Related Work | ~0.8 |
| Method (含 table, equation) | ~1.8 |
| Atlas (含 3 tables, 3 figures) | ~2.0 |
| Generalization (含 3 tables, 1 figure) | ~1.5 |
| Discussion/Conclusion | ~0.3 |
| **合计** | **~8.0** |

正好卡在 8 页限制边缘。Limitations + Ethics 在 references 之后不计入页数限制。**强烈建议编译后确认实际页数**，如超 8 页需压缩。

---

### 汇总

| 检查项 | 状态 |
|--------|------|
| Ethics Statement | ✅ 存在且充实 |
| Broader Impact | ⚠️ 无单独 section，但 Ethics + Extended Discussion 覆盖 A2 |
| Reproducibility | ❌ 缺少：计算预算、硬件、库版本、超参搜索策略 |
| Limitations | ✅ 非常充实 |
| 匿名化 | ✅ 无泄露 |
| 行号 | ✅ review 模式已启用 |
| 页数 | ⚠️ 估计 ~8 页，需编译确认 |
| AI Assistant 披露 (E1) | ❌ 如使用了 AI 辅助写作/编码，需在 checklist 中披露 |

**优先修复**：添加 Reproducibility 信息（计算资源、库版本），填写 checklist 时确保 C1/C4 有对应 section 号。

Sources:
- [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [Checklist PDF](https://aclrollingreview.org/static/responsibleNLPresearch.pdf)
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Author Guidelines](https://aclrollingreview.org/authors)

---
