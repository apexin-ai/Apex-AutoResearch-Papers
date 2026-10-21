# analyze qwen15b loop only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_loop_only_seed42_20260520T084230_result.json`
- **Structured JSON:** [`b45467e00445ed2081ee.json`](../../sessions/b4/b45467e00445ed2081ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## qwen15b_loop_only_seed42 结果

**Accuracy: 78.3%** (95% CI: [76.1%, 80.7%])，lift over majority baseline +6.8pp。

| Metric | Pass | Fail |
|--------|------|------|
| Precision | 0.83 | 0.64 |
| Recall | 0.88 | 0.55 |
| F1 | 0.85 | 0.59 |

## 跨模型 loop_only 对比

| Model | Params | Accuracy | Δ vs Qwen-7B |
|-------|--------|----------|---------------|
| **Qwen-7B** | 7B | **86.05%** | — |
| DeepSeek-Coder | 6.7B | 81.26% | -4.8pp |
| **Qwen-1.5B** | 1.5B | **78.32%** | **-7.7pp** |
| CodeLlama | 13B | 76.56% | -9.5pp |

## Conclusion: **success**

78.3% 落在预期 75-85% 范围内。Qwen-1.5B 在 loop_only 条件下仍有意义地超过 majority baseline（+6.8pp），但 fail 召回仅 0.55，说明 1.5B 规模对低信号密度条件的 fail 案例区分力有限。cuda:0 已清空，无残留进程。Registry 已更新至 DONE。

---
