# analysis mvp2 eval lr5e6 r1 ckpt100

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_eval_lr5e6_r1_ckpt100_20260515T012129_result.json`
- **Structured JSON:** [`4cadc2a64f25fd9ba17c.json`](../../sessions/4c/4cadc2a64f25fd9ba17c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

## mvp2_eval_lr5e6_r1_ckpt100 结果

| 指标 | 值 |
|------|-----|
| **rel_f1** | **0.0138** |
| rel_precision | 0.0132 |
| rel_recall | 0.0144 |
| ign_f1 | 0.0138 |
| evi_f1 | 0.8504 |
| evi_precision | 0.9256 |
| evi_recall | 0.7866 |
| edcr | 0.9876 |
| format_ok_rate | 99.9% |
| field_compliance_rate | 81.6% |
| tp / pred / gold | 175 / 13300 / 12151 |
| n_truncated | 181/985 |
| inference_time | 5901.7s |

**结论：negative**。rel_f1=0.0138 远低于 pass criteria 0.30，也远低于 SFT baseline 0.4057。与 ckpt-80 (0.0116) 和 ckpt-60 (0.0093) 相当——模型预测了大量关系（13300）但几乎全错（tp 仅 175），说明 lr=5e-6 的 GRPO 训练在关系抽取准确性上严重退化，虽然格式和证据质量维持良好。

---
