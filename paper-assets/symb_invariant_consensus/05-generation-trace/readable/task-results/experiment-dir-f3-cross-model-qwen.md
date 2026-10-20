# experiment dir f3 cross model qwen

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-f3-cross-model-qwen_20260520T164047_result.json`
- **Structured JSON:** [`c521e282b9c0ef8a073c.json`](../../sessions/c5/c521e282b9c0ef8a073c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| 指标 | 值 |
|------|-----|
| **Original SICA acc** | 0.533 (16/30) |
| **Cross-model filtered SICA acc** | 0.533 (16/30) |
| **SC acc** | 0.533 (16/30) |
| **Constraint keep rate** | 67.6% |
| **McNemar p-value** | 1.0 |
| **Discordant pairs** | 0 |
| **Prediction flips** | 1 (folio_18: orig=False→filt=Unknown, but both wrong; gold=True) |

三种方法在 30 题 pilot 上准确率完全相同。Cross-model 过滤掉约 32.4% 的 constraints，但几乎没有改变预测结果——仅 folio_18 从 False 翻转到 Unknown（均错误），总准确率不变。

结果写入 `/root/symb_invariant_consensus/results/dir_f3_cross_model_verification/results.json`，verifier_model = Qwen2.5-14B-Instruct。

---
