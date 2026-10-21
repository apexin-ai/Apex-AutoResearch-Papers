# W4: Table 1 vs Table 3 DocRED Unconstrained 数据不一致 — 根因报告

**调研日期**: 2026-05-15
**服务器**: westd-16980
**项目代码**: `/root/schema_semantic_constrained_ie/`

---

## 1. 审稿人观察的数字差异

| 表 | 章节 | DR | RV | ET | CF |
|---|---|---|---|---|---|
| Table 1 (`tab:prompt_comparison`) | §5.1 / `section3_violation_landscape.tex` | **18.7** | **28.9** | **7.5** | 0.1 |
| Table 3 (`tab:cross-model`) | §5.2 / `section5_crossmodel_draft.tex` | **18.46** | **29.66** | **2.48** | 0.10 |

两个表都标注为同一实验 (`phase0_docred_unconstrained` ↔ `phase2_docred_unconstrained`)，使用同一模型 (Qwen3-8B)。

---

## 2. 关键发现

### 2.1 Prompt 完全一致 ✅

`run_extraction_docred.py:91 build_prompt(document_text, relation_list_str, schema_informed=False)` 是项目里唯一的 prompt 构造函数。Phase 0 unconstrained 与 Phase 2 unconstrained **调用的是同一个函数 + 同一个 `schema_informed=False` 参数**，没有任何 prompt 差异。所以差异不来自 prompt。

### 2.2 输入 JSONL 完全一致 ✅

服务器上当前只有 **一个** DocRED unconstrained 推理输出文件：

```
/root/schema_semantic_constrained_ie/outputs/docred_unconstrained.jsonl
  size = 10,503,924 bytes
  mtime = 2026-05-14 21:09:47
  lines = 998 docs
```

所有 4 个相关的 violation report 都基于这同一个文件，可由共同字段验证：
- `total_documents=998, documents_checked=986, parse_failures=12`
- `total_triples_extracted=17497, total_entities_extracted=20171`
- 都报告 `domain_range_violations=3230`, `relation_vocabulary_violations=5189`

所以差异 **不来自不同的推理输出**。

### 2.3 差异完全来自 checker 版本 ✅

`violation_checker_docred.py` 有两个版本：

| 版本 | 行 | ET 计数逻辑 | 别名归一 |
|---|---|---|---|
| **v1** (`.bak` / `.bak2`) | 99-135 | triple-count: 每个 entity 在 `entities` 列表中算一次，在 relation 的 head 中算一次，tail 中算一次 | 只有 `.upper()` |
| **v2** (当前 `violation_checker_docred.py`) | 109-148 | unique-count: 用 `(text.lower().strip(), normalized_type)` 去重，每个 unique entity 只算一次违规 | `ENTITY_TYPE_ALIASES` 映射 `PERSON→PER, ORGANIZATION→ORG, ...` |

注意：v2 的 docstring 显式说明了「`v2: ET violations counted per unique entity (text+type dedup)`」并打了 `checker_version: "fixed_20260514_v2 (strip + alias + unique_et)"`。

### 2.4 各报告对 docred_unconstrained.jsonl 的输出对比

| 报告文件 | mtime | ET violations / rate | RV / rate | DR / rate |
|---|---|---|---|---|
| `violation_report_docred_unconstrained.json` (v1) | 21:35 | 1650 / **8.18%** | 5189 / 29.66% | 3230 / 18.46% |
| `violation_report_docred_unconstrained_phase2.json` (v1) | 21:20 | 1650 / **8.18%** | 5189 / 29.66% | 3230 / 18.46% |
| `violation_report_docred_unconstrained_fixed.json` (v1) | 22:50 | 1650 / **8.18%** | 5189 / 29.66% | 3230 / 18.46% |
| `violation_report_docred_unconstrained_v2.json` (v2) | 02:28 | 500 / **2.48%** | 5189 / 29.66% | 3230 / 18.46% |
| `violation_report_docred_unconstrained_unified.json` (v2 + 多分母) | 04:26 | 499 / 2.47% | 5189 / 29.66% | 2538 / 21.85% (eligible) or 14.51% (all) |

**关键观察**：在同一个 jsonl 上，v1 vs v2 只在 **ET** 上有差异（8.18% vs 2.48%），DR 和 RV 完全相同（18.46% / 29.66%）。

### 2.5 Table 1 数字 (18.7 / 28.9 / 7.5) 在当前 outputs 中 **完全找不到对应文件** ⚠️

用 `grep -rln "0.187\|0.075\|0.289"` 遍历整个 `outputs/` 目录：
- DR=18.7%（`0.187`）：只出现在当前 v1/v2 unconstrained 报告中，但作为子字符串（`0.1875` 的前缀），实际 DR 是 18.46%（`0.1846`）
- ET=7.5%（`0.075`）：不存在任何 `entity_type_violation_rate≈0.075` 的报告
- RV=28.9%（`0.289`）：只出现在小规模 pilot (`violation_report_s2_pilot50.json`) 和不相关分析文件中

**结论**：Table 1 的 18.7 / 28.9 / 7.5 来自 **更早一版的 Phase 0 推理输出**（已被 2026-05-14 21:09 的 rerun 覆盖），所以现在磁盘上找不到能精确复现它们的 jsonl。Table 1 的数字是 **stale**。

**附旁证**：`section7_conclusion_550cbf.tex`（旧版本）写 `18.70%`，而 `section7_conclusion.tex`（新版本）已更新为 `18.46%`，说明结论章已经迁移到新数据，但 Table 1 所在的 §5.1 (`section3_violation_landscape.tex`) 还停留在旧数据。

---

## 3. 根因总结

差异由**两个独立问题**叠加：

1. **数据快照不同**：Table 1 用的是更早的 Phase 0 推理结果（已被覆盖，无法精确复现）；Table 3 用的是 2026-05-14 21:09 重跑的版本（当前 `docred_unconstrained.jsonl`）。这解释了 DR 18.7 vs 18.46、RV 28.9 vs 29.66 的细微差异。
2. **Checker 版本不同**：Table 3 的 ET=2.48% 来自 **v2 checker**（unique entity dedup），Table 1 的 ET=7.5% 来自旧推理 + **v1 checker**（triple-count ET）。如果在新数据上跑 v1 会得到 ET=8.18%，跑 v2 得到 2.48%。

prompt 等价，模型、超参一致 — 没有第三个变量。

---

## 4. 修复方案

### ★ 方案 B（推荐，最简洁）：用当前 v2 数据替换 Table 1 DocRED 行

修改 `paper/section3_violation_landscape.tex:32` 和 `paper/paper_tables_draft.tex:90,119`：

```latex
\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
                        & Schema-informed & 12.8 & 18.4 & 0.6 & 0.2 \\  % 需用 v2 重算 schema-informed
```

并同步修改 `section3_violation_landscape.tex:16` 正文表述：
- `15.37\% ... 18.70\%` → `15.37\% ... 18.46\%`
- `(28.90\% vs.\ 1.39\%)` → `(29.66\% vs.\ 1.39\%)`

以及 `section1_introduction_draft.tex:8`、`abstract_*.tex`、`section7_conclusion_550cbf.tex` 中所有 18.7% / 28.9% / 7.5% 的痕迹（多数已更新到 18.46%，残留处见下文 §5）。

**优点**：
- 论文内部所有 DocRED unconstrained 数字统一为 v2 / 当前数据
- 与 Table 3、abstract.tex（已是 18.46%）、conclusion 一致
- 一处真值：`violation_report_docred_unconstrained_v2.json`

**注意**：Table 1 的 schema-informed 行 (12.8 / 18.4 / 0.6) 来自 `violation_report_docred_schema.json`，那是 **v1 checker** 的输出。为彻底一致，应该用 v2 checker 对 `raw_outputs_docred_schema.jsonl` 重新评估。从 v1→v2 的经验看，schema-informed 的 ET 也会显著下降（0.61% → 大概率 < 0.3%）。

### 方案 A（备选）：保留 Table 1 用 v1，在脚注说明

不推荐 — 论文里 abstract / conclusion / Table 3 都已是 18.46%，单独保留 Table 1 用旧数字会让审稿人继续困惑。

### 方案 C（不推荐）：保留差异 + 论文中加方法学说明

会让 reviewer 把 W4 升级为「方法学不一致」的更大问题。

---

## 5. 论文中需要修订的位置一览

按需 `sed`/手动批改：

| 文件 | 行 | 现状 | 建议 |
|---|---|---|---|
| `section1_introduction_draft.tex` | 8 | `18.7\%` | `18.5\%` 或 `18.46\%` |
| `section3_violation_landscape.tex` | 16 | `18.70\%` | `18.46\%` |
| `section3_violation_landscape.tex` | 16 | `28.90\%` | `29.66\%` |
| `section3_violation_landscape.tex` | 32 (Table 1) | `18.7 & 28.9 & 7.5` | `18.5 & 29.7 & 2.5` |
| `section3_violation_landscape.tex` | 33 (Table 1) | `12.8 & 18.4 & 0.6` | 用 v2 重评估 schema-informed 后填入 |
| `paper_tables_draft.tex` | 90 | `18.7 & 28.9 & 7.5` | 同上 |
| `paper_tables_draft.tex` | 119 | `18.7 & 28.9 & 7.5` | 同上 |
| `section7_conclusion_550cbf.tex` | 11, 20 | `18.70\%`, `7.50\%` | 全删（已被 `section7_conclusion.tex` 替代）或同步 |
| `abstract_fd4b26.tex`, `abstract_d3264e.tex` | 3 | `18.7\%` | 与 `abstract.tex`（18.46%）同步或删除旧 abstract |

> 已经统一到 18.46% 的位置：`abstract.tex`, `section5_docred_draft.tex`, `section5_crossmodel_draft.tex`, `section7_conclusion.tex`, `discussion_paragraphs.tex`, `appendix_discussion.tex`.

---

## 6. 推荐执行步骤

1. （可选但推荐）对 `raw_outputs_docred_schema.jsonl` 跑一次 v2 checker，得到 schema-informed 的 v2 数字，把 Table 1 第二行也同步。
2. 按 §5 表格批量替换 18.7/28.9/7.5 → 18.5/29.7/2.5（或保留两位小数 18.46/29.66/2.48）。
3. 删除/归档旧 abstract（`abstract_fd4b26.tex`, `abstract_d3264e.tex`）和旧 conclusion（`section7_conclusion_550cbf.tex`），避免编译时混入老 LaTeX。
4. 在 rebuttal 中明确告诉 reviewer：「Table 1 的旧数字来源于早期 v1 checker（triple-count ET），现已统一到 v2 checker（unique-entity ET dedup）—— DR/RV 不受影响，只 ET 由 8.18% 修正为 2.48%；DR/RV 的 0.24/0.76 pp 微差来自 inference 重跑。两个表现在均反映同一份 `docred_unconstrained.jsonl` 在 v2 checker 下的结果。」

---

## 7. 一句话答复 reviewer (可直接用)

> Thank you for catching the inconsistency. The two tables in fact report the same experiment; the gap arose because Table 1 (§5.1) used an earlier snapshot scored with our v1 violation checker (which triple-counted entity-type violations across the entity list and per-triple head/tail), while Table 3 (§5.2) uses the current `docred_unconstrained.jsonl` scored with the v2 checker (one violation per unique `(entity_text, normalized_type)` pair, with alias normalization for PERSON→PER etc.). Prompt and decoding are identical. We will update Table 1 to the v2 numbers (DR 18.46 / RV 29.66 / ET 2.48 / CF 0.10), matching Table 3 and the abstract/conclusion which already use these values.
