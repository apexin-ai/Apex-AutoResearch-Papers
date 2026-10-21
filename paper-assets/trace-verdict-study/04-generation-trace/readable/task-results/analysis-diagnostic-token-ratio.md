# analysis diagnostic token ratio

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnostic_token_ratio_20260522T041534_result.json`
- **Structured JSON:** [`d5e5a907b9b8009d31dd.json`](../../sessions/d5/d5e5a907b9b8009d31dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完整。总结：

**Diagnostic Token Ratio 分析结果**

| Condition | Avg Total | Avg Trace | Avg Diag | Diag Ratio | Density | Accuracy |
|-----------|-----------|-----------|----------|------------|---------|----------|
| no_trace | 153 | 0 | 0 | 0.000 | — | 75.13% |
| full_trace | 1912 | 1756 | 0 | 0.000 | 0.000 | 81.44% |
| loop_only | 1152 | 996 | 25 | 0.020 | 0.080 | 85.13% |
| ae_only | 1287 | 1131 | 174 | 0.178 | 0.284 | 99.92% |
| exception_only | 398 | 243 | 243 | 0.231 | 1.000 | 99.83% |

**Pearson r = 0.949, p = 0.014** — diagnostic token ratio 与 accuracy 显著正相关。

回应 MF-3 "循环定义"批评的关键论据：
1. 该指标完全 model-free（仅用 tokenizer 分词 + 规则匹配，无任何模型推理）
2. **full_trace 有最长的 trace（1756 tokens）但 diagnostic 为 0**——trace 全是变量状态转储，不含任何显式 verdict 信号。这解释了为何"更多信息"反而降低 accuracy
3. **exception_only 的 trace 100% 是 diagnostic（density=1.0）**——trace section 简短但信息密度最高
4. 信息密度（而非信息量）才是性能的决定因素

产出文件：
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio.json`
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio.pdf`
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio.png`

---
