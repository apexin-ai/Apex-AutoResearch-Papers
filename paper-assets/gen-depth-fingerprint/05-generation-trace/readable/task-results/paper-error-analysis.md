# paper error analysis

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_error-analysis_20260523T095732_result.json`
- **Structured JSON:** [`7b413a20bf4c92cbfc4f.json`](../../sessions/7b/7b413a20bf4c92cbfc4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存到本地。下面是完整分析结果。

---

## 错误分析结果

### 二分类 (gen-1 vs gen-2+) 错误分布

| Generator | N | FP | FN | Err% | F1 |
|-----------|---:|---:|---:|-----:|----:|
| Mistral-7B | 3853 | 75 | 1659 | **45.0** | 0.581 |
| Qwen3-8B | 3502 | 93 | 1104 | 34.2 | 0.703 |
| Llama-3.2-3B | 3685 | 82 | 1030 | 30.2 | 0.750 |
| OLMo-2-1B | 3718 | 154 | 900 | 28.3 | 0.776 |
| Pythia-2.8B | 3614 | 129 | 737 | 24.0 | 0.813 |
| Qwen3-1.7B | 3621 | 175 | 639 | 22.5 | 0.831 |
| Qwen3-0.6B | 3542 | 234 | 511 | 21.0 | 0.846 |
| Pythia-1B | 3560 | 188 | 460 | **18.2** | 0.867 |
| **Overall** | **29095** | **1130** | **7040** | **28.1** | — |

### 三大关键发现

**1. 错误高度不对称：86.2% 是 FN**
gen-2+ 被误判为 gen-1 的比例远高于反向，说明深层生成文本经常保留 gen-1 的统计特性。

**2. Depth-2 是主要混淆边界**
| Depth | Errors/N | Rate | Type |
|-------|----------|------|------|
| 1 | 1130/7896 | 14.3% | FP |
| 2 | 3637/7512 | **48.4%** | FN |
| 3 | 2051/7032 | 29.2% | FN |
| 4 | 1352/6655 | 20.3% | FN |

Mistral-7B 在 depth-2 的 FN 率高达 **74.1%**，Pythia-1B 仅 33.0%。

**3. 误分类样本占据特征重叠区**
- 5/7 特征显著不同 (p<10^{-294})：entropy_mean (+0.69), TTR (+0.16), hapax_ratio (+0.14)
- 2 特征无差异 (p>0.05)：entropy_max, tail_decay
- 预测置信度边距：正确=0.351 vs 错误=0.212

### 3-class 混淆矩阵 (%)

| True \ Pred | gen-0 | gen-1 | gen-2+ |
|-------------|------:|------:|-------:|
| gen-0 | **99.2** | 0.8 | 0.1 |
| gen-1 | 7.3 | **78.4** | 14.3 |
| gen-2+ | 3.0 | 30.2 | **66.7** |

### 已保存文件
- LaTeX 表格+段落：`artifacts/_project/paper/appendix_error_analysis.tex`
- 分析脚本：`artifacts/_project/chart/comprehensive_error_analysis.py`
- 服务器 JSON：`experiments/error_analysis/comprehensive_error_analysis.json`

---
