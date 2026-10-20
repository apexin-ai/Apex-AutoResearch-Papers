# analysis cwm unparseable samples

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-unparseable-samples_20260517T084428_result.json`
- **Structured JSON:** [`bf2dba1d71558f1c9253.json`](../../sessions/bf/bf2dba1d71558f1c9253.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已写入 `artifacts/qualitative_cwm_examples.json`。

3 个样本覆盖了两种 unparseable 失败模式和一个 parseable 对比：

| ID | Model | Failure Mode |
|---|---|---|
| `qwen3-repo-cwm-unparseable-1` | Qwen3-4B repo | 幻觉完整 Django test runner 日志（1248 tokens），无 pass/fail verdict |
| `qwen3-repo-cwm-unparseable-2` | Qwen3-4B repo | 幻觉源代码 + 重复退化（`from _pytest.config import ...` 无限循环直到截断，4542 tokens） |
| `deepseek-func-cwm-parseable-1` | DeepSeek-6.7B func | 正确输出 `FAIL: SyntaxError: expected ':'`（31 tokens），格式完全符合预期 |

核心发现：repo-level CWM 的 unparseable 不是单一原因，而是两种不同的退化模式——(a) 模型把 CWM 任务误解为 execution trace 生成，(b) 模型在长 context 下陷入 autoregressive degeneration。func-level 输入短而明确，DeepSeek 完全没有这个问题。

---
