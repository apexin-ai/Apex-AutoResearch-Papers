# paper table4 crossref trace

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table4-crossref-trace_20260523T110010_result.json`
- **Structured JSON:** [`5c9f450f6b9b79b312cd.json`](../../sessions/5c/5c9f450f6b9b79b312cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

溯源完成。以下是完整报告：

---

## 溯源结果

### 1. 两组数字的确切来源

| 文件 | Generator 数 | Generators | F1 (Pythia/OLMo/Qwen ref) |
|------|------------|-----------|---------------------------|
| `review_p2f_cross_ref_bias.json` | **5** | olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b | **0.803 / 0.807 / 0.816** ← 论文用的 |
| `table4_cross_ref_logo.json` | **6** | 同上 + **qwen3-8b** | **0.789 / 0.795 / 0.813** |
| `cross_ref_results.json` | **6** | 同上 | 同上（由 `cross_ref_analysis.py` 生成）|

### 2. 差异原因

`cross_ref_analysis.py` 读取 `features_all_models.csv`，该文件现在包含 **6 个 generator**（含 qwen3-8b）。qwen3-8b 是所有 generator 中最难分类的（per-fold F1 仅 0.686–0.757），包含它会拉低平均 F1 约 0.014。

`review_p2f_cross_ref_bias.json` 是早期在 5-gen 子集上运行的结果（由已删除的 `run_cross_ref_bias.py` 生成），当时 qwen3-8b 尚未加入 cross-ref feature 文件。

### 3. "excluding all Pythia generators" — **论文中不存在此描述**

我搜索了所有 `.tex` 文件，**未找到** "excluding all Pythia generators" 这个表述。论文实际写的是：

- `table4.tex` 正文："5-generator subset **(Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)**"  
- Caption："5-gen LOGO subset"
- `appendix_generator_subsets.tex`："Py-2.8B/1B, OLMo, Qw-1.7B/0.6B"

这些描述**正确**——5-gen 子集包含 Pythia，排除的是 qwen3-8b、llama、mistral（后期扩展的 generator）。

### 4. 应该用哪组数字

**当前论文数字 (0.803/0.807/0.816) 是正确的**，与论文描述的 5-gen 子集一致。`table4_cross_ref_logo.json` 的 6-gen 数字是后期 `cross_ref_analysis.py` 意外包含了 qwen3-8b 的结果，与论文描述的子集不匹配。

### 5. 需要修正的内容

**无需修改论文**。Table 4 的数字、子集描述、caption 三者自洽。`table4_cross_ref_logo.json` 是一个后期产生的不一致文件，不应替换论文数字。

---
