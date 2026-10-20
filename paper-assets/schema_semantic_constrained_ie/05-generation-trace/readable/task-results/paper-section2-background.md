# paper section2 background

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section2_background_20260514T061320_result.json`
- **Structured JSON:** [`785d9c317c53f6b4fbee.json`](../../sessions/78/785d9c317c53f6b4fbee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section2_background.tex` 并注册。~580 words，3 个 subsection：

- **§2.1 IE Ontology Structure**: 形式化定义 $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$，type validity 条件，constraint tightness 定义，SciERC vs DocRED 对比数据
- **§2.2 Grammar-Constrained Decoding**: autoregressive generation + token mask $M_g$，XGrammar/Outlines/SGLang 引用，明确指出 CFG 无法表达 cross-field semantic constraints 的局限
- **§2.3 Problem Statement**: structural validity (a) vs type validity (b)，(a) context-free，(b) context-sensitive but prefix-decidable with state

符号与 Introduction 和 writing_plan notation_table 一致（$\mathcal{O}, \mathcal{E}, \mathcal{R}, \sigma, M_g$）。引用 key 沿用已有格式。需要 `enumitem` 宏包支持 `[label=(\alph*)]`。

---
