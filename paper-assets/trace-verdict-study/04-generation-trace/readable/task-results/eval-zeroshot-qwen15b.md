# eval zeroshot qwen15b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_zeroshot_qwen15b_20260517T140613_result.json`
- **Structured JSON:** [`0d7fbe22939b3520ef8e.json`](../../sessions/0d/0d7fbe22939b3520ef8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**模型**：`Qwen2.5-Coder-1.5B-Instruct`（路径：`/root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct`）

### 关键发现

1.5B 模型**不遵循 "pass/fail" 输出格式**，全部输出 "yes/no/let's..." 形式，strict 匹配下 accuracy = 0%。

用 lenient 映射（yes→pass, no→fail）后：

| 指标 | 1.5B zero-shot | 7B zero-shot | 7B SFT |
|------|---------------|-------------|--------|
| **Accuracy** | **93.45%** | 89.08% | 99.83% |
| 95% CI | [92.02%, 94.79%] | — | — |
| Pass F1 | 0.969 | — | — |
| Fail F1 | 0.873 | — | — |
| Unknown | 24 (2.0%) | — | — |

### Raw Output 分布

| 输出 | 数量 | 映射 |
|------|------|------|
| "yes, the" | 607 | → pass |
| "yes, this" | 282 | → pass |
| "no, this" | 277 | → fail |
| "let's examine" | 18 | → unknown |
| "let's walk" | 5 | → unknown |
| "to determine if" | 1 | → unknown |

### 错误模式

- **严重偏向 pass**：几乎所有错误都是 label=fail 但预测为 pass（输出 "yes, this"）
- Pass recall 99.06% vs Fail recall 79.35%：对 fail 样本漏检严重
- 24 条 unknown（"let's examine/walk"）= 模型试图分析而非直接回答，全部来自 fail 样本

### 意外结论

1.5B lenient（93.45%）**竟然超过** 7B strict（89.08%）。可能原因：
- 7B 的 89.08% 也是 strict 匹配，如果 7B 也有 yes/no 输出被丢弃为 unknown，则 7B lenient 可能更高
- 或者 1.5B-Coder 在简单二分类任务上足够强，只是不遵循格式

建议确认 7B 的 raw output 分布，看是否也存在 yes/no 输出被错误标记为 unknown 的情况。

---
