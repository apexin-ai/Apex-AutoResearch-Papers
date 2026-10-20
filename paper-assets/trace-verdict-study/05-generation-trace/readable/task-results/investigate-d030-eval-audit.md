# investigate d030 eval audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d030_eval_audit_20260515T224453_result.json`
- **Structured JSON:** [`b5f12ca2dc8e0dfe59a7.json`](../../sessions/b5/b5f12ca2dc8e0dfe59a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**deepseek_vota_seed42**：84.45% → **15.97%**（需修正）
- 983/1190 (82.6%) 预测为垃圾 token（"these"/"this"/"given"/"assert" 等）
- 模型在 final checkpoint 发生 mode collapse
- 模拟 lenient parser (garbage→pass) 可重建到 83.36%，接近报告的 84.45%
- evaluate.py 的 `classify_prediction` 在 git 历史中从未有 lenient 逻辑，84.45% 来源推测为提交前的 ad-hoc 评估

**deepseek_no_trace_seed42**：73.36% **已验证正确**
- 重新评估结果完全一致
- 0% garbage token（842 pass + 348 fail，全部有效）
- 不受 parser 问题影响

报告已注册：`art_20260515_b6e1f6`

---
