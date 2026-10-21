# paper consistency check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency-check_20260518T072010_result.json`
- **Structured JSON:** [`b0b17880f7a56ab6f966.json`](../../sessions/b0/b0b17880f7a56ab6f966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，页数未变。以下是四项检查结果汇总：

---

### 1. Confounded 数据残留检查

4 处匹配，**全部 OK，无残留**：

| 文件 | 匹配内容 | 判断 |
|------|---------|------|
| `appendix_classifier.tex:59` | `$|\rho| = 0.30$ at $t{=}0.9$` | OK — corrected 相关系数值 |
| `appendix_lofo.tex:14` | `$-$0.33\,pp` | OK — LOFO 特征消融结果 |
| `results.tex:80` | permutation importance 0.35/0.23/0.18 | OK — 特征重要性值 |
| `results.tex:127` | `+0.3\,pp` | OK — ensemble vs single 对比 |

无 `sampling_ablation`、`top.p 0.80`、`top.p 0.95` 匹配。

### 2. LaTeX 引用完整性

- **Undefined refs**: 0（所有 `\ref{}` 都有对应 `\label{}`）
- **Unused labels**: 22 个，多为结构性 label（section/table/appendix），列举关键的：
  - Sections: `sec:conclusion`, `sec:ethics`, `sec:evaluation`, `sec:features`, `sec:introduction`, `sec:limitations`, `sec:related` 及子节
  - Tables: `tab:5class-logo`, `tab:5class-perclass`, `tab:ablation`, `tab:cross-model-perclass`, `tab:domain`, `tab:feature-ablation`, `tab:feature-corr`, `tab:lofo`, `tab:qlora`, `tab:seed-control`
  - Appendices: `app:feature-distributions`, `app:human-edit`, `app:qlora`, `app:qualitative`

这些 unused labels 不影响编译，但建议检查 `tab:ablation`、`tab:domain`、`app:qlora` 等是否应在正文中引用。

### 3. Cross-temp top_p footnote

已添加。在 `appendix_cross_temp.tex` 第 2 行末尾插入 footnote：
> "The $t{=}1.0$ data uses top-$p{=}0.95$ (vs. $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone."

### 4. 编译结果

| 指标 | 值 |
|------|---|
| 页数 | **26** |
| Errors | **0** |
| Undefined references | **0** |
| Warnings | **2**（均为 `'h' float specifier changed to 'ht'`，无害） |

---
