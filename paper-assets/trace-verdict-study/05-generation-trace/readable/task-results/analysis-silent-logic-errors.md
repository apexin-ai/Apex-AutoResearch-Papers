# analysis silent logic errors

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_silent-logic-errors_20260517T003826_result.json`
- **Structured JSON:** [`3e30f91ca4f8d2e3662c.json`](../../sessions/3e/3e30f91ca4f8d2e3662c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/trace-verdict-study/docs/paper/silent_error_analysis.md`。

**核心发现**：

1. **70 个 silent logic errors**（占 fail 的 20.6%）：label=fail 但无 exception trace
2. **除 no_trace 外所有 condition 在这些样本上 100% 准确**，但这不是真实能力，而是**标签泄漏**：
   - Pass 样本用 `[No exception data in trace]`
   - Silent fail 样本用 `[No trace available]`
   - 两个不同 placeholder 让模型无需代码理解即可区分
3. **no_trace 是唯一的真实度量**：72.9% 准确率，19 个错误全部是误判为 pass（集中在 HumanEval/31、HumanEval/12）
4. **论文影响**：exception_only 的总体 accuracy 有约 20% fail 样本被 shortcut 贡献。建议统一 placeholder 文本后重新评估，或在论文中分开报告 exception-bearing fail 子集的准确率。

---
