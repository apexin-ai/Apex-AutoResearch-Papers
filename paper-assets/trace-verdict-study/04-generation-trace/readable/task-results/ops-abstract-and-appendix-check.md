# ops abstract and appendix check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_abstract-and-appendix-check_20260523T085224_result.json`
- **Structured JSON:** [`1321890d7975e9236be4.json`](../../sessions/13/1321890d7975e9236be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the full report.

---

## Part A: Appendix 交叉引用完整性

### 编译状态

- main.log (2026-05-23 15:14): **0 个 undefined reference warnings, 0 个 multiply-defined warnings**
- 仅 1 个 benign warning: `'h' float specifier changed to 'ht'`
- PDF 输出: 21 pages, 441KB

### ⚠️ CRITICAL: experiments.tex 文件损坏

**experiments.tex 存在 null byte 污染**，从约第 44 行开始出现乱码。关键事实：

| 文件 | 大小 | 修改时间 | \label 数量 |
|------|------|----------|------------|
| experiments.tex | 20,192 bytes | 15:57:38 | **仅 1 个** (sec:cross_model) |
| experiments.tex.bak | 16,653 bytes | 05-21 20:35 | **8 个** (cross_model, ablation, nomarker, density, additional, trace_length, calibration, debugbench) |

main.log 时间戳是 15:14，experiments.tex 损坏时间是 15:57。**当前 PDF 是在损坏之前编译的，内容正确。但下次重新编译会产生大量 undefined references 和乱码。**

### 19 个 Appendix Section 逐一确认

| # | Section 标题 | Label | 行号 | 实质内容 | 引用来源 |
|---|-------------|-------|------|---------|---------|
| 1 | Per-Class Performance Breakdown | `sec:per_class` | 1–33 | ✅ Table tab:per_class, 8+5 conditions | experiments.tex (table caption) |
| 2 | Training Details | `sec:training_details` | 34–102 | ✅ tab:hyperparams + tab:train_time | method.tex:44 |
| 3 | VOTA Extraction Algorithm | `sec:vota_algorithm` | 103–141 | ✅ Algorithm description | method.tex:25 |
| 4 | VOTA Trace Examples | `sec:vota_examples` | 142–199 | ✅ Input/output examples | method.tex:35 (fig caption) |
| 5 | Full Experimental Results | `sec:full_results` | 200–252 | ✅ Full per-seed table | experiments.tex:18 (table caption) |
| 6 | Tokenizer and Truncation Analysis | `sec:tokenizer_analysis` | 253–270 | ✅ DeepSeek truncation analysis | experiments.tex.bak:40,61; appendix internal |
| 7 | Persistent Error Analysis | `sec:irreducible` | 271–294 | ✅ GeneratorExit analysis | experiments.tex.bak:49; appendix:327 |
| 8 | Exception Type Accuracy Breakdown | `sec:exception_type` | 295–329 | ✅ Per-type breakdown table | experiments.tex.bak:180 |
| 9 | Exception Subcomponent Ablation | `sec:exc_subcomponent` | 330–360 | ✅ exc_type/stacktrace/message 分析 | ⚠️ **DANGLING — 无引用** |
| 10 | Trace Length Ablation | `sec:trace_length_full` | 361–548 | ✅ 187 行, 多表多图 | experiments.tex.bak:157,161 |
| 11 | Calibration Analysis | `sec:calibration_full` | 549–607 | ✅ 校准图表 | experiments.tex.bak:174 |
| 12 | Error Overlap Analysis | `sec:error_overlap` | 608–628 | ✅ Jaccard 分析 | experiments.tex.bak:177 |
| 13 | Cross-Dataset: DebugBench | `sec:debugbench_full` | 629–663 | ✅ DebugBench 详细结果 | experiments.tex.bak:184 |
| 14 | Cross-Model Robustness | `sec:robustness_analysis` | 664–676 | ✅ 鲁棒性分析 | experiments.tex.bak:62 |
| 15 | Training Dynamics | `sec:training_dynamics` | 677–695 | ✅ 损失曲线分析 | introduction.tex:20,26; discussion.tex:20 |
| 16 | Deduplication Statistics | `sec:dedup_stats` | 696–728 | ✅ 去重统计 | method.tex:17; experiments.tex:6 |
| 17 | Regex Baseline Analysis | `sec:regex_baselines` | 729–785 | ✅ 5 个 regex baseline 分析 | experiments.tex.bak:102,103,112 |
| 18 | Cross-Model Zero-Shot | `sec:zeroshot_cross_model` | 786–813 | ✅ 4 模型 zero-shot vs SFT | experiments.tex.bak:107 |
| 19 | Calibration Analysis (subsection) | `sec:calibration_analysis` | 814–834 | ✅ 4 模型 ECE/Brier 表 | ⚠️ **DANGLING — 无引用** |

### 问题汇总

1. **2 个 dangling labels**: `sec:exc_subcomponent` 和 `sec:calibration_analysis` 定义了但从未被 `\ref` 引用。内容本身有实质价值，建议在正文中补充引用（例如 experiments.tex 的 nomarker 或 calibration 段落）。

2. **experiments.tex 损坏**: 当前文件从第 44 行起有 null byte，7 个 `\label` 丢失。**下次 pdflatex 编译会崩溃**。需要从 .bak 恢复或修复。

3. **所有 19 个 appendix section 均有实质内容**，无空壳 section。

---

## Part B: Abstract 数字逐句核对

### Abstract 原文提取

> "complete traces achieve only 77--82% while compact exception events reach ≥99.33%"
> "A regex exploiting format markers matches this ceiling, but marker removal collapses it to 28.49% while SFT retains 97.65%"
> "Gradient masking attributes ≤4% of the 18--23pp gap to gradient dilution"

### 逐项核对

#### 1. "77--82%" (full_trace accuracy)

| Model | Table 值 | 来源 |
|-------|---------|------|
| Qwen-7B | 81.44±1.11 (multi-seed) / 81.76 (seed 42) | tab:cross_model / tab:per_class |
| Qwen-1.5B | 77.06† | tab:cross_model |
| CL-13B | 79.9§ | tab:cross_model |
| DS-6.7B | 79.16† | tab:cross_model |

- 范围: 77.06 → 81.44 (multi-seed mean) 或 77.06 → 81.76 (seed 42)
- Abstract "77--82%": 下界 77.06→77 ✅；上界 81.44→**81**（取整），81.76→82（取整）
- **结论: ✅ 一致** — 上界用的是 seed 42 的 81.76% 取整到 82%，可接受

#### 2. "≥99.33%" (exception_only minimum)

| Model | Multi-seed mean | Min single seed |
|-------|----------------|-----------------|
| Qwen-7B | 99.83±0.00 | 99.83 |
| Qwen-1.5B | 99.83±0.00 | 99.83 |
| CL-13B | 99.89±0.10 | 99.83 |
| DS-6.7B | 99.39±0.10 | **99.33** |

- 最低单种子值 = 99.33% (DeepSeek seed 42 和 seed 456)
- **结论: ✅ 精确一致** — ≥99.33% 是所有模型所有种子的下界

#### 3. "18--23pp gap" (exception_only − full_trace)

| Model | exception_only | full_trace | Gap |
|-------|---------------|------------|-----|
| Qwen-7B | 99.83 | 81.44 | **18.39pp** |
| Qwen-1.5B | 99.83 | 77.06 | **22.77pp** |
| CL-13B | 99.89 | 79.9 | **19.99pp** |
| DS-6.7B | 99.39 | 79.16 | **20.23pp** |

- 范围: 18.39 → 22.77pp → 取整 18 → 23pp
- **结论: ✅ 精确一致**

#### 4. "≤4%" gradient dilution

- 实测: gradient masking (99.8% mask) 导致 mean −0.61pp (3 seeds, Qwen-7B)
- 0.61pp / 18.39pp (Qwen-7B gap) = 3.3%
- **结论: ✅ 一致** — 3.3% < 4%

#### 5. "28.49%" (regex under marker removal)

- discussion.tex:24 和 introduction.tex:28 均引用 28.49%
- 来自 nomarker 实验的确定性结果
- **结论: ✅ 一致**

#### 6. "97.65%" (SFT under marker removal)

- introduction.tex:28: "SFT drops only 2pp (99.83%→97.65%)"
- discussion.tex:24: "SFT retains 97.65%"
- Drop: 99.83 − 97.65 = 2.18pp ≈ "2pp" ✅
- **结论: ✅ 一致**

#### 7. Abstract 中无其他定量数字

Abstract 其余为定性描述（"cross-dataset transfer", "two-tier signal hierarchy", "tail-truncated traces provide a viable fallback"）。无需核对。

### 关于"最后一句是否需要 tail-512 的 93-97% 数字锚点"

Abstract 最后一句: *"when unavailable, tail-truncated traces provide a viable fallback"*

正文支撑数字:
- discussion.tex:13: "Tail-truncated traces achieve 93--97% accuracy"
- tab:tail_cross_model 有 4 模型 tail-512 数据

**建议**: 可以加但非必须。Abstract 已有 6 个定量数字，信息密度高。"93--97%" 属于二级发现（fallback strategy），保持定性表述 "a viable fallback" 使 abstract 更清爽。若 reviewer 要求具体化，可改为 "a viable fallback (93--97% with tail-512 tokens)"。

### 总结

| 检查项 | 状态 |
|--------|------|
| Abstract 6 个数字 vs 正文/表格 | ✅ 全部一致 |
| experiments.tex 文件完整性 | ❌ **null byte 损坏，需修复** |
| Appendix 19 section 内容 | ✅ 均有实质内容 |
| Undefined references | ✅ 当前 PDF 无 (但重编译会出问题) |
| Dangling labels | ⚠️ 2 个: sec:exc_subcomponent, sec:calibration_analysis |

**最紧急**: experiments.tex 损坏需要修复（`cp experiments.tex.bak experiments.tex` 或从 git 恢复），否则下次编译会失败。

---
