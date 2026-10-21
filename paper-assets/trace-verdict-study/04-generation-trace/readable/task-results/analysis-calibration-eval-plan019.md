# analysis calibration eval plan019

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_calibration_eval_plan019_20260520T104357_result.json`
- **Structured JSON:** [`3d1eced43d9a355243d6.json`](../../sessions/3d/3d1eced43d9a355243d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**Cross-model (exception_only)**:
- 4 模型 ECE 均 < 0.007，calibration 良好
- Qwen-1.5B 和 CodeLlama-13B 并列最优 ECE (0.0020)；模型规模不影响 calibration
- CodeLlama-13B 的 MCE 显著最低 (0.041 vs 0.75+)，因为它没有单点高置信度错误
- DeepSeek-6.7B 最差：ECE 3×、Brier 5× 高于其他模型

**Cross-condition (Qwen-7B)**:
- ae_only 最优 (ECE=0.0004)，exception_only 次之 (0.0027)，vota 第三 (0.0054)
- 低准确率条件 (no_trace/label_only/loop_only/full_trace) ECE 在 0.08–0.17，系统性过度自信

---
