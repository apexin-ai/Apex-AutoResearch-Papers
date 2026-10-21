# paper compile d110 fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_d110_fix_20260523T032715_result.json`
- **Structured JSON:** [`ec63c9e288fa5a99fc6d.json`](../../sessions/ec/ec63c9e288fa5a99fc6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译结果：

| 项目 | 结果 |
|------|------|
| 编译状态 | **成功，0 errors** |
| Warnings | 16（均为 hyperref PDF string token 和 float specifier，无实质问题） |
| 总页数 | **18 页** |
| 正文页数 | **10 页**（Appendix A 从第 11 页开始） |

---

**表格验证 (`tab_domain_model_kstar_full.tex`)**：

1. **脚注中的 scorer 名称**：
   - 第 24 行 `\textsuperscript{$\dagger$}` 脚注：提到 "cross-family scorer (**Pythia-1.4B**)"  ✅
   - 但同一脚注也提到 "**Qwen-1.5B scorer** yields $K^*{=}2$" — 这是描述 scorer artifact 现象，不是推荐值。Pythia-1.4B 作为 cross-family scorer 出现在脚注中。✅

2. **arXiv K\*=3 的 `\textsuperscript` 标记**：
   - Qwen2.5-7B (第 13 行): `\textbf{3}\textsuperscript{$\|$}` ✅
   - LLaMA-3.1-8B (第 15 行): `\textbf{3}\textsuperscript{$\|$}` ✅
   - Mistral-7B (第 16 行): `\textbf{3}\textsuperscript{$\|$}` ✅

三个模型的 arXiv K\*=3 单元格均带有 `\textsuperscript{$\|$}` 标记，对应脚注 `‖` 解释了 scorer-matched 与 cross-scorer bootstrap CI 的关系。

**注意**：正文 10 页超出 EMNLP 2026 的 8 页限制，需要压缩 2 页。

---
