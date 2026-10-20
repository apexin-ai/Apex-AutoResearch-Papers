# diagnose eval llama rsft s42 with evidence 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_llama_rsft_s42_with_evidence_2048_20260521T071309_result.json`
- **Structured JSON:** [`f0ddacbaab88da22a3ad.json`](../../sessions/f0/f0ddacbaab88da22a3ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：实验实际已成功完成，是监控系统误判。**

日志显示 985/985 文档推理全部完成（4h16m），metrics.json 和 predictions.json 均已写入 `/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048/`。失败标记源于监控系统检测不到 sentinel 文件或 W&B 信号，5 次探测后自动标记为 failed。

关键结果：F1=0.5892, Ign-F1=0.5774, Evi-F1(DREEAM)=0.4719, EDCR=0.6143。

无需重试，仅需在 registry 中将状态从 failed 更正为 completed。报告已写入 `artifacts/diagnose_eval_llama_rsft_s42_with_evidence_2048.md`。

---
