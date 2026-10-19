# code exp pathb annotation validation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_pathb_annotation_validation_20260517T065326_result.json`
- **Structured JSON:** [`b90532e1bc2a6359607f.json`](../../sessions/b9/b90532e1bc2a6359607f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

## 结果总结

**exp_pathb_annotation_validation: NEGATIVE**

| 方法 | F1 (safety) | CP Agreement (±1) | 判定 |
|------|------------|-------------------|------|
| TF-IDF + LR | 0.5899 | 56.1% | FAIL |
| MiniLM + LR | 0.5149 | 53.4% | FAIL |

**阈值**: F1 >= 0.90, CP >= 85%

**核心失败原因**: Safety recall 极低（41-46%），简单分类器无法区分 CoT 中语义细微的安全意识表达与普通推理。CP MAE 达 5-6 句，预测的 critical point 偏离严重。

**结论**: 本地分类器方法不可行。Path B 数据生成需要 LLM-based annotation（API 调用或 fine-tune DeBERTa 做 16-class 分类）。

---
