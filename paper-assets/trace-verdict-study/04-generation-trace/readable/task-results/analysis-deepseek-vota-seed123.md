# analysis deepseek vota seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_vota_seed123_20260520T023530_result.json`
- **Structured JSON:** [`75657d6dda4aed255a46.json`](../../sessions/75/75657d6dda4aed255a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**deepseek_vota_seed123: accuracy=99.16%** (CI: [98.57%, 99.66%])

- **假设被推翻**：原假设 [82%, 88%] 不成立，实际远超预期
- **与 seed42 (84.45%) 差距 +14.71pp**：seed42 大概率是 outlier，seed123 与其他模型的 VOTA 结果一致（Qwen-7B 99.05%, CodeLlama 98.57%）
- train_loss=0.0625, eval_loss=0.110
- deepseek_vota_seed456 已在 PREPARING，作为 tie-breaker 仲裁 seed42 是否为 outlier
- 报告已写入 artifacts 并注册（art_20260520_5a6c0f）

---
