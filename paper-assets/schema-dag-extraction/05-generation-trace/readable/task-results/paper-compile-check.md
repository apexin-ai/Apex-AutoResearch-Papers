# paper compile check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_check_20260516T073931_result.json`
- **Structured JSON:** [`56b737bf472b0683bd75.json`](../../sessions/56/56b737bf472b0683bd75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 预检查结果

### §5 位置和词数
- **文件**: `sdgd_negative.tex`
- **标题**: "Why Naive Decomposition Fails" (`\label{sec:sdgd}`)
- **位置**: `main.tex` 第 33 行 `\input{sdgd_negative}`
- **当前词数**: 245 词（含 LaTeX 命令）
- **结构**: 1 个 section 标题 + 2 个 paragraph（"Merge amplification as the bottleneck" 和 "Confidence gating does not resolve the problem"）

### 贡献列表第 4 条（introduction.tex 第 19 行）
> **Informative negative result.** Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.

### Abstract 中的 mitigation 内容
Abstract 最后一句已包含 SDGD 相关内容：
> "Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE."

**总结**: §5 目前非常精简（245 词，2 段），仅覆盖 merge amplification 和 confidence gating 失败。Abstract 和贡献列表都已提及此 negative result，措辞一致。

---
