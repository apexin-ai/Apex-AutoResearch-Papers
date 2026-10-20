# eval fewshot qwen7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fewshot_qwen7b_20260517T140557_result.json`
- **Structured JSON:** [`13bf510360a0f383774c.json`](../../sessions/13/13bf510360a0f383774c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## 3-Shot Few-Shot Baseline 结果

### 选用的 3 个 examples (train set)
| Example | Train Index | Label | 描述 |
|---------|------------|-------|------|
| 1 | 1851 | **pass** | `is_decimal()` — caught ValueError（try/except 捕获异常，测试通过） |
| 2 | 875 | **fail** | `triangle_area()` — AssertionError |
| 3 | 30 | **fail** | `rolling_max()` — AssertionError |

### Accuracy 对比
| Method | Accuracy | 95% CI |
|--------|----------|--------|
| Zero-shot | 89.08% | — |
| **3-shot** | **90.84%** | [89.08%, 92.44%] |
| SFT | 99.83% | — |

3-shot 相比 zero-shot 提升约 **+1.76pp**，但远不及 SFT。

### Per-class Metrics
| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| Pass | 0.9245 | 0.9495 | 0.9368 |
| Fail | 0.8639 | 0.8053 | 0.8336 |

### 错误分析
- 总错误：109/1190
- **fail→pass (66)**: 主要错误模式，模型倾向于预测 pass
- **pass→fail (43)**: 次要错误
- Unknown: **0** (比 zero-shot 好，所有输出都是 pass/fail)
- Truncated: 0（first prompt 1874 tokens，在 4096 限制内）
- Raw output 分布：pass=874, fail=316

### 产出文件
- `/root/autodl-tmp/trace-verdict-study-checkpoints/fewshot_qwen7b_exception_only/eval_results.json`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/fewshot_qwen7b_exception_only/predictions.jsonl`
- `/root/autodl-tmp/trace-verdict-study-checkpoints/fewshot_qwen7b_exception_only/error_examples.json`

---
