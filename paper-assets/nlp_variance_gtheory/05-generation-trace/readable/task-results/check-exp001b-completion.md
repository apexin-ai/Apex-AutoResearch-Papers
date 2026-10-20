# check exp001b completion

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp001b_completion_20260521T083611_result.json`
- **Structured JSON:** [`8ed89aac235535a38518.json`](../../sessions/8e/8ed89aac235535a38518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 session 没有活跃 cron，监控已不存在（可能在之前的 session 中创建并已自行清除）。

**exp001b_resampling 实验完成，总结：**

- 3 组 × 86,400 records = 259,200 总记录，数据完整
- Accuracy：Sample 1 = 0.7207, Sample 2 = 0.6212, Sample 3 = 0.6860
- 运行时间 ~29 分钟（15:58 → 16:27）
- Registry 已标记 DONE/success，metrics 已记录

值得注意：3 组 accuracy 差异较大（0.62–0.72），说明 item sampling 对整体准确率有显著影响，后续 G-theory 分解可以量化这一点。

---
