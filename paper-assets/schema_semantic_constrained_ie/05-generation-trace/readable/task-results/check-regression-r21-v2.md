# check regression r21 v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_regression-r21-v2_20260523T043926_result.json`
- **Structured JSON:** [`6deb0dbb3b6122d683fa.json`](../../sessions/6d/6deb0dbb3b6122d683fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Regression Check Results

### A. 内容检查

**1. Abstract** ✅ 通过
- `abstract.tex` 完整，无 TODO/XX.XX 占位符，无残留旧文本。

**2. §1 Introduction — WikiEvents "preliminary pilot study"** ✅ 通过
- `section1_introduction_draft.tex:26`: "a preliminary pilot study on WikiEvents (n${=}$20 test documents)"
- `section5_wikievents_draft.tex:10`: "As a preliminary pilot study, we apply OntoCoDec to event extraction (EE)"
- 两处均已标注。

**3. Table 1 caption** ✅ 通过
- `section5_scierc_draft.tex:62-68`: caption 为客观描述（"Five-way ablation on SciERC"），无过强确定性声明。

**4. §5 — 70B AWQ 脚注** ✅ 通过
- `section5_runtime.tex:15`: `\footnote{All 70B experiments use AWQ INT4 quantization; logit-level effects on constraint enforcement are not isolated.}`

**5. Limitations — DocRED dev set** ✅ 通过
- `main.tex:89`: "DocRED experiments evaluate on the development set, as test set annotations are not publicly available."
- `section3_violation_landscape.tex:10` 也有脚注声明。

**6. §3 — Corollary → Empirical Observation** ✅ 通过
- `section3_method_draft.tex:39`: `\textbf{Empirical Observation} (scale-dependent enabling dependency)`
- 全文无 "Corollary" 出现。

---

### B. 交叉引用检查

- ✅ 无 undefined references
- ✅ 无 multiply defined labels
- ✅ 无 citation warnings

---

### C. 页数检查

- 总页数：38 页（含 appendix）
- ⚠️ **无法从 log 精确判断正文页数**。main.tex 结构：§1-§7 正文 → `\clearpage` → Limitations → Ethics → Bibliography → Appendix。需要打开 PDF 确认正文是否 ≤ 8 页。

---

### D. 全局问题搜索

- ✅ **TODO/FIXME**: 6 个 TODO 均在 `section6_relwork_outline.tex`（未被 main.tex 引用的草稿文件），不影响编译输出。
- ✅ **XX.XX/TBD/PLACEHOLDER**: 无。
- ✅ **textcolor{red}**: 仅 `\TBD` 命令定义（`main.tex:22`），全文未调用。
- ⚠️ **Overfull/Underfull boxes**: log 中有 136 处，属常见排版警告，但数量偏多，建议编译后目视检查是否有明显溢出。

---

### 总结

| 类别 | 状态 |
|------|------|
| A1-A6 内容检查 | ✅ 全部通过 |
| B 交叉引用 | ✅ 无问题 |
| C 页数 | ⚠️ 需目视确认正文 ≤ 8 页 |
| D 全局 | ⚠️ 136 个 overfull/underfull box 警告 |

---
