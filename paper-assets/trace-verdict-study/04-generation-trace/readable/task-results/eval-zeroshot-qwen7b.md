# eval zeroshot qwen7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_zeroshot_qwen7b_20260517T130756_result.json`
- **Structured JSON:** [`76b698bf452cf0e841da.json`](../../sessions/76/76b698bf452cf0e841da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Zero-shot baseline 完成。结果汇总：

## Zero-shot vs SFT 对比

| 指标 | Zero-shot | SFT |
|------|-----------|-----|
| **Accuracy** | **89.08%** (95% CI: [87.31%, 90.76%]) | **99.83%** |
| Majority baseline | 71.51% (always pass) | - |
| Lift over baseline | +17.56pp | - |

**Per-class F1:**

| | Precision | Recall | F1 |
|--|-----------|--------|------|
| Pass | 0.8815 | 0.9788 | 0.9276 |
| Fail | 0.9265 | 0.6696 | 0.7774 |

**关键发现：**
- 130/1190 条预测错误，0 条 unknown
- 模型输出 "yes"（945）/ "no"（245），映射为 pass/fail
- 主要错误模式：**fail 样本被预测为 pass**（模型倾向于回答 "yes"）。Fail recall 仅 66.96%，说明模型对 fail 的判断能力显著不足
- SFT 将 accuracy 从 89.08% 提升到 99.83%，提升 **10.75pp**，充分证明 SFT 的必要性

结果已存储在 `/root/autodl-tmp/trace-verdict-study-checkpoints/zeroshot_qwen7b_exception_only/eval_results_mapped.json`。

---
